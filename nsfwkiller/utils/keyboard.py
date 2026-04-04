from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Primary", callback_data="primary", style="primary"),
            InlineKeyboardButton(text="Success", callback_data="success", style="success")
        ],
        [
            InlineKeyboardButton(text="Danger", callback_data="danger", style="danger")
        ],
        [
            InlineKeyboardButton(text="🔥 NSFW Killer", callback_data="emoji_test", icon_custom_emoji_id="5474667187258006816")
        ]
    ])
