from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.adapters.telegram_bot.keyboards import contacts

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
