from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from lib.null_safety import getval

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    user_names = f"{html.quote(getval(message.from_user.full_name))}"
    user_link = (
        f"<a href='tg://user?id={getval(message.from_user.id)}'>{user_names}</a>"
    )
    await message.answer(f"Hi {user_link}!")
