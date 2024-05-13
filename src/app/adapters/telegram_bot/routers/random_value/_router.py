from random import randint
from typing import Annotated

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import Message
from aioinject import Inject
from aioinject.ext.aiogram import inject

from app.adapters.telegram_bot.keyboards import random_call
from app.adapters.telegram_bot.mixins import RemoveKeyboardMixin
from app.core.some.repository import SomeRepository
from lib.di import INJECTED

router = Router()


@router.message(Command(commands=["random", "r"]))
async def random_handler(message: Message) -> None:
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=random_call.BUILDER.as_markup(),
    )


@router.callback_query(F.data == "random_value")
class RandomCallbackHandler(CallbackQueryHandler, RemoveKeyboardMixin):

    @inject
    async def handle(
        self,
        repository: Annotated[SomeRepository, Inject] = INJECTED,
    ) -> None:
        await self._remove_keyboard()

        print(repository)  # noqa: T201
        await self.bot.send_message(
            chat_id=self.from_user.id,
            text=str(randint(1, 10)),  # noqa: S311
        )
