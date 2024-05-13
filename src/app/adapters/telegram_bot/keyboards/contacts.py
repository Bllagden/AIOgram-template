from aiogram.utils.keyboard import (  # type: ignore[attr-defined]
    KeyboardButton,
    ReplyKeyboardBuilder,
)

CONTACTS_GEO_BUTTON = KeyboardButton(
    text="Запросить геолокацию",
    request_location=True,
)

CONTACTS_NUM_BUTTON = KeyboardButton(
    text="Запросить контакт",
    request_contact=True,
)


BUILDER = ReplyKeyboardBuilder(
    markup=[
        [
            CONTACTS_GEO_BUTTON,
            CONTACTS_NUM_BUTTON,
        ],
    ],
)
