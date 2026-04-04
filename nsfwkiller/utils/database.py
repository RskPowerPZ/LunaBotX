from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

engine = create_engine(os.getenv("DATABASE_URL"), echo=False)
SessionLocal = sessionmaker(bind=engine)
redis_client = redis.from_url(os.getenv("REDIS_URL"))

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def log_nsfw(user_id: int, chat_id: int, score: float, content_type: str):
    try:
        session = SessionLocal()
        log = NSFWLog(user_id=user_id, chat_id=chat_id, score=score, content_type=content_type)
        session.add(log)
        session.commit()
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
