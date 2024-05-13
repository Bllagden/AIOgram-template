from datetime import UTC, datetime

from aiogram import F, Router, html
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(F.text)
async def echo_with_time_handler(message: Message) -> None:
    time_now = datetime.now(tz=UTC).strftime("%H:%M")
    added_text = html.underline(
        f"Команда не распознана\nСоздано по UTC в {time_now}",  # noqa: RUF001
    )
    print("echo")  # noqa: T201
    await message.answer(
        text=f"{message.text}\n\n{added_text}",
        reply_markup=ReplyKeyboardRemove(),
    )
