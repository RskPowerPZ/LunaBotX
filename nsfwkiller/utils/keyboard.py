from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

EMOJI_ID = "5474667187258006816"   # aapka diya hua emoji ID

def get_main_keyboard():
    """Start aur normal messages ke liye colored buttons"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⚡ ᴍʏ ɢʀᴏᴜᴘs", callback_data="my_groups", style="primary"),
                InlineKeyboardButton(text="✨ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help", style="success")
            ],
            [
                InlineKeyboardButton(text="↗ sᴜᴘᴘᴏʀᴛ", url="https://t.me/YOUR_SUPPORT_GROUP", style="primary"),
                InlineKeyboardButton(text="✦ ᴏᴡɴᴇʀ", url="https://t.me/DarkBhaiFan", style="success")
            ],
            [
                InlineKeyboardButton(
                    text="?? Explore Features",
                    callback_data="features",
                    icon_custom_emoji_id=EMOJI_ID,
                    style="primary"
                )
            ]
        ]
    )
    return keyboard


def get_help_keyboard():
    """Help menu ke liye colored buttons"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="?? Moderation", callback_data="help_mod", style="primary")],
            [InlineKeyboardButton(text="?? NSFW Protection", callback_data="help_nsfw", style="danger")],
            [InlineKeyboardButton(text="?? Link Modes", callback_data="help_link", style="success")],
            [InlineKeyboardButton(text="?? Stats", callback_data="help_stats", style="primary")],
            [InlineKeyboardButton(text="?? Back to Main", callback_data="start_back", style="danger")]
        ]
    )
    return keyboard


def get_verify_keyboard():
    """Bio verification ke liye Green button"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Verify",
                    callback_data="verify_bio",
                    style="success"          # Green color
                )
            ]
        ]
    )
    return keyboard
