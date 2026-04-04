from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

NSFW_THRESHOLD = float(os.getenv("NSFW_THRESHOLD", 0.65))
AUTO_MUTE = os.getenv("AUTO_MUTE", "True").lower() == "true"
AUTO_BAN = os.getenv("AUTO_BAN", "False").lower() == "true"
MUTE_DURATION = int(os.getenv("MUTE_DURATION", 3600))

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
