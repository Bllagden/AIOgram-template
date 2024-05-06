from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from app.adapters.telegram_bot.callbacks import RandomCallback

RANDOM_BUTTON = InlineKeyboardButton(
    text="Нажми меня",
    callback_data=RandomCallback().pack(),
)


BUILDER = InlineKeyboardBuilder(
    markup=[
        [RANDOM_BUTTON],
    ],
)
