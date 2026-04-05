from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import redis.asyncio as redis
from datetime import datetime
from loguru import logger
import os

Base = declarative_base()

class NSFWLog(Base):
    __tablename__ = "nsfw_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    chat_id = Column(Integer)
    score = Column(Float)
    content_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Force SQLite + aiosqlite (no psycopg2 interference)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///nsfw_logs.db")
if not DATABASE_URL.startswith("sqlite+aiosqlite"):
    DATABASE_URL = "sqlite+aiosqlite:///nsfw_logs.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    connect_args={"check_same_thread": False}  # SQLite safety
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.success("✅ Database initialized (SQLite + async)")

async def log_nsfw(user_id: int, chat_id: int, score: float, content_type: str):
    try:
        async with AsyncSessionLocal() as session:
            async with session.begin():
                log = NSFWLog(
                    user_id=user_id,
                    chat_id=chat_id,
                    score=score,
                    content_type=content_type
                )
                session.add(log)
        
        await redis_client.incr("total_deleted")
        await redis_client.incr(f"deleted:{datetime.utcnow().strftime('%Y-%m-%d')}")
        logger.success(f"NSFW logged | Score: {score:.2f}")
    except Exception as e:
        logger.error(f"DB error: {e}")

async def get_stats():
    try:
        total = int(await redis_client.get("total_deleted") or 0)
        today = int(await redis_client.get(f"deleted:{datetime.utcnow().strftime('%Y-%m-%d')}") or 0)
        return total, today
    except:
        return 0, 0
