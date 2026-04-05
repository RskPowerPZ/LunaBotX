import asyncio
import uvloop
import re
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties
from loguru import logger
import psutil

from config import *
from nsfwkiller.utils.nsfw_detector import is_nsfw
from nsfwkiller.utils.keyboard import get_main_keyboard, get_help_keyboard, get_verify_keyboard
from nsfwkiller.utils.database import init_db, log_nsfw, get_stats

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
logger.add("nsfw_bot.log", rotation="10 MB", level="INFO", colorize=True)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

LINK_MODE = "mute"   # default mode

# ====================== START ======================
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    welcome_text = """
✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇʀ ʙᴏᴛ

ᴀ ᴘʀᴏғᴇssɪᴏɴᴀʟ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ʙᴏᴛ ᴅᴇsɪɢɴᴇᴅ ғᴏʀ ᴍᴏᴅᴇʀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴄᴏᴍᴍᴜɴɪᴛɪᴇs ⚡

??️ ᴀᴄᴛɪᴠᴇ ᴍᴏᴅᴜʟᴇs
• ʙɪᴏ ʟɪɴᴋ ʀᴇsᴛʀɪᴄᴛᴏʀ — ʙɪᴏ ʟɪɴᴋs / @ᴜsᴇʀɴᴀᴍᴇs
• ɴsғᴡ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ — ᴋᴇʏᴡᴏʀᴅ ᴛᴇxᴛ, sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋs, ᴏᴘᴛɪᴏɴᴀʟ ᴀɪ

?? ᴘᴏᴡᴇʀғᴜʟ ғᴇᴀᴛᴜʀᴇs
• ᴀᴜᴛᴏ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ
• sᴍᴀʀᴛ ᴀɴᴛɪ-sᴘᴀᴍ sʏsᴛᴇᴍ
• ʙɪᴏ ʟɪɴᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ
• ɴsғᴡ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ
• ᴍᴏᴅᴇʀɴ ᴀᴅᴍɪɴ ᴛᴏᴏʟs

?? ɴᴏᴛᴇ
✦ ᴛʜɪs ʙᴏᴛ ᴡᴏʀᴋs ʙᴇsᴛ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ sᴜᴘᴇʀɢʀᴏᴜᴘs.

?? ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴇxᴘʟᴏʀᴇ ʜᴇʟᴘ, ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
"""
    await message.answer(welcome_text, reply_markup=get_main_keyboard())


# ====================== BIO RESTRICTOR (NEW JOIN) ======================
@dp.message(F.new_chat_members)
async def bio_restrictor(message: types.Message):
    for new_user in message.new_chat_members:
        if new_user.is_bot:
            continue
        try:
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=new_user.id,
                permissions=types.ChatPermissions(can_send_messages=False)
            )
        except:
            pass

        mention = f'<a href="tg://user?id={new_user.id}">{new_user.full_name}</a>'
        bio_msg = (
            f"?? <b>Hello {mention}!</b>\n\n"
            f"?? <b>First remove URL or any username in your bio</b>\n"
            f"After removing links/@usernames, click the button below to get unmuted."
        )
        await message.answer(bio_msg, reply_markup=get_verify_keyboard())


# ====================== VERIFY BUTTON (UNMUTE) ======================
@dp.callback_query(F.data == "verify_bio")
async def verify_bio_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    try:
        await bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False
            )
        )
        mention = f'<a href="tg://user?id={user_id}">{callback.from_user.full_name}</a>'
        await callback.message.edit_text(
            f"✅ <b>Verified successfully!</b>\n{mention} you can now chat freely.",
            reply_markup=None
        )
        await callback.answer("✅ Unmuted! Chat freely now.", show_alert=False)
    except Exception as e:
        await callback.answer("❌ Bot must be admin with restrict rights.", show_alert=True)


# ====================== FIXED NSFW DETECTION ======================
@dp.message(F.chat.type.in_({"group", "supergroup"}) & (F.photo | F.video | F.animation | F.sticker | F.document))
async def delete_nsfw(message: types.Message):
    if not message.from_user:
        return

    if message.photo:
        media = message.photo[-1]
        content_type = "photo"
    elif message.video:
        media = message.video
        content_type = "video"
    elif message.animation:
        media = message.animation
        content_type = "animation"
    elif message.sticker:
        media = message.sticker
        content_type = "sticker"
    elif message.document:
        media = message.document
        content_type = "document"
    else:
        return

    try:
        file = await bot.download(media)
        file.seek(0)                    # ← IMPORTANT FIX (error yahin se aa raha tha)
        file_bytes = file.read()

        is_nsfw_flag, score = await is_nsfw(file_bytes, content_type)

        if is_nsfw_flag:
            await message.delete()
            mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>'
            warn = f"?? <b>NSFW Deleted</b>\nScore: {score:.2f}\nUser: {mention}"
            await message.answer(warn)

            # Log NSFW (Redis error ko ignore kar diya)
            try:
                await log_nsfw(message.from_user.id, message.chat.id, score, content_type)
            except:
                pass

            if AUTO_MUTE:
                try:
                    await bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions=types.ChatPermissions(can_send_messages=False))
                    await asyncio.sleep(MUTE_DURATION)
                    await bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions=message.chat.permissions)
                except:
                    pass
            if AUTO_BAN:
                await bot.ban_chat_member(message.chat.id, message.from_user.id)

    except Exception as e:
        logger.error(f"NSFW error: {e}")


# ====================== LINK + @USERNAME DETECTION (Existing + New members) ======================
@dp.message(F.chat.type.in_({"group", "supergroup"}) & F.text)
async def link_restrictor(message: types.Message):
    text = message.text.lower()
    if re.search(r'http[s]?://|www\.|t\.me/|@\w{4,}', text):   # link ya username detect
        mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>'
        action = LINK_MODE
        try:
            if action == "ban":
                await bot.ban_chat_member(message.chat.id, message.from_user.id)
                await message.answer(f"?? {mention} banned for sending link/username!")
            elif action == "kick":
                await bot.ban_chat_member(message.chat.id, message.from_user.id)
                await bot.unban_chat_member(message.chat.id, message.from_user.id)
                await message.answer(f"?? {mention} kicked for sending link/username!")
            else:  # mute
                await bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions=types.ChatPermissions(can_send_messages=False))
                await message.answer(f"?? {mention} muted for sending link/username!")
        except:
            pass


# ====================== MODERATION COMMANDS ======================
@dp.message(Command("ban", "mute", "kick"))
async def moderation_commands(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Reply karo user ko!")
        return
    user = message.reply_to_message.from_user
    cmd = message.text.split()[0][1:].lower()
    mention = f'<a href="tg://user?id={user.id}">{user.full_name}</a>'
    try:
        if cmd == "ban":
            await bot.ban_chat_member(message.chat.id, user.id)
            await message.answer(f"?? {mention} banned!")
        elif cmd == "mute":
            await bot.restrict_chat_member(message.chat.id, user.id, permissions=types.ChatPermissions(can_send_messages=False))
            await message.answer(f"?? {mention} muted!")
        elif cmd == "kick":
            await bot.ban_chat_member(message.chat.id, user.id)
            await bot.unban_chat_member(message.chat.id, user.id)
            await message.answer(f"?? {mention} kicked!")
    except:
        await message.answer("Permission nahi hai ya user admin hai.")


# ====================== SET LINK MODE ======================
@dp.message(Command("setlinkmode"))
async def set_link_mode(message: types.Message):
    global LINK_MODE
    try:
        mode = message.text.split()[1].lower()
        if mode in ["ban", "mute", "kick"]:
            LINK_MODE = mode
            await message.answer(f"✅ Link mode set to <b>{mode.upper()}</b>", parse_mode="HTML")
        else:
            await message.answer("❌ Use: /setlinkmode ban / mute / kick")
    except:
        await message.answer("Usage: /setlinkmode ban/mute/kick")


# ====================== STATS ======================
@dp.message(Command("stats"))
async def stats_cmd(message: types.Message):
    total, today = await get_stats()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    await message.answer(
        f"<b>?? NSFW Killer Stats</b>\n"
        f"Total Deleted: <code>{total}</code>\n"
        f"Today: <code>{today}</code>\n"
        f"CPU: <code>{cpu}%</code> | RAM: <code>{ram}%</code>\n"
        f"Link Mode: <b>{LINK_MODE.upper()}</b>",
        reply_markup=get_main_keyboard()
    )


# ====================== HELP ======================
@dp.callback_query(F.data == "help")
async def help_callback(callback: types.CallbackQuery):
    help_text = """
?? <b>HELP & COMMANDS MENU</b>

?? <b>Moderation</b>
/ban @user - Ban
/mute @user - Mute
/kick @user - Kick

?? <b>Link Mode</b>
/setlinkmode ban
/setlinkmode mute
/setlinkmode kick

?? <b>Bio Protection</b>
Auto mute on join + message pe link/username detect

?? Bot ko Admin banao (Delete + Restrict rights)
"""
    await callback.message.edit_text(help_text, reply_markup=get_help_keyboard())


@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "verify_bio":
        return
    await callback.answer("LunaBotX running at full power ⚡", show_alert=True)


# ====================== BOT START ======================
async def main():
    await init_db()
    logger.info("?? LunaBotX Group Manager + Bio + Link + NSFW Started Successfully!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
