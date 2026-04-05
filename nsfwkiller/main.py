import asyncio
import uvloop
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger
import psutil
import orjson

from config import *
from nsfwkiller.utils.nsfw_detector import is_nsfw
from nsfwkiller.utils.keyboard import get_main_keyboard
from nsfwkiller.utils.database import init_db, log_nsfw, get_stats

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
logger.add("nsfw_bot.log", rotation="10 MB", level="INFO", colorize=True)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    help_text = (
        "<b>🔥 NSFW Killer Bot Activated</b>\n\n"
        "✅ Har photo, video, GIF, sticker, document auto scan hota hai\n"
        "🚫 NSFW content turant delete + log\n"
        "📊 /stats → Total deleted count\n"
        "⚙️ Admin commands available\n\n"
        "<i>Bot ko group mein Admin banao with Delete + Restrict rights.</i>"
    )
    await message.answer(help_text, reply_markup=get_main_keyboard())

@dp.message(lambda m: m.chat.type in ["group", "supergroup"] and (m.photo or m.video or m.animation or m.sticker or m.document))
async def delete_nsfw(message: types.Message):
    if not message.from_user:
        return
    content_type = "video" if message.video else "photo"
    file = await bot.download(message)
    file_bytes = await file.read()
    is_nsfw_flag, score = await is_nsfw(file_bytes, content_type)
    if is_nsfw_flag:
        await message.delete()
        warn = f"🚫 <b>NSFW Deleted</b>\nScore: {score:.2f}\nUser: {message.from_user.mention}"
        await message.answer(warn)
        await log_nsfw(message.from_user.id, message.chat.id, score, content_type)
        if AUTO_MUTE:
            try:
                await bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions=types.ChatPermissions(can_send_messages=False))
                await asyncio.sleep(MUTE_DURATION)
                await bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions=message.chat.permissions)
            except:
                pass
        if AUTO_BAN:
            await bot.ban_chat_member(message.chat.id, message.from_user.id)

@dp.message(Command("stats"))
async def stats_cmd(message: types.Message):
    total, today = await get_stats()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    await message.answer(
        f"<b>📊 NSFW Killer Stats</b>\n"
        f"Total Deleted: <code>{total}</code>\n"
        f"Today: <code>{today}</code>\n"
        f"CPU: <code>{cpu}%</code> | RAM: <code>{ram}%</code>",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer("NSFW Killer Bot running at full power 🔥", show_alert=True)

async def main():
    await init_db()
    logger.info("🚀 NSFW Killer Bot Started (uvloop + Redis + OpenCV + colored buttons)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
