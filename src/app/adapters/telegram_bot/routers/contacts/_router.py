from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.adapters.telegram_bot.keyboards import contacts
from lib.null_safety import getval

router = Router()


@router.message(Command("contacts"))
async def contacts_handler(message: Message) -> None:
    await message.answer(
        "Запрос контактов",
        reply_markup=contacts.BUILDER.as_markup(
            one_time_keyboard=True,
            resize_keyboard=True,
        ),
    )


@router.message(F.contact)
async def contact_handler(message: Message) -> None:
    phone_number = getval(message.contact.phone_number)
    print(phone_number)
