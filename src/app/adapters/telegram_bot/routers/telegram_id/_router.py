from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from lib.null_safety import getval

router = Router()


@router.message(Command("id"))
async def id_handler(message: Message) -> None:
    tele_id = getval(message.from_user.id)
    await message.answer(str(tele_id))
