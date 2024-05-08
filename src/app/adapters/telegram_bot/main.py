import contextlib
from collections.abc import AsyncIterator, Sequence

from aiogram import Bot, Dispatcher, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aioinject import Container
from aioinject.ext.aiogram import AioInjectMiddleware

from app.di import create_container
from app.settings import TelegramBotSettings
from lib.settings import get_settings

from .middleware import SomeMiddleware
from .routers import contacts, echo, random_value, start, telegram_id

MAIN_ROUTERS: Sequence[Router] = [
    start.router,
    contacts.router,
    random_value.router,
    telegram_id.router,
    echo.router,
]


def _configure_middlewares(core_router: Router, container: Container) -> None:
    core_router.message.outer_middleware.register(AioInjectMiddleware(container))
    core_router.callback_query.outer_middleware.register(AioInjectMiddleware(container))

    core_router.message.outer_middleware.register(SomeMiddleware())
    core_router.callback_query.outer_middleware.register(SomeMiddleware())


def _register_routes(core_router: Router, routers: Sequence[Router]) -> None:
    for router in routers:
        core_router.include_router(router)


@contextlib.asynccontextmanager
async def create_bot() -> AsyncIterator[Bot]:
    settings = get_settings(TelegramBotSettings)
    async with AiohttpSession() as session:
        yield Bot(
            token=settings.token.get_secret_value(),
            session=session,
            parse_mode=ParseMode.HTML,
        )


async def main() -> None:
    main_router = Router()
    container = create_container()

    _configure_middlewares(main_router, container)
    _register_routes(main_router, MAIN_ROUTERS)

    dispatcher = Dispatcher()
    dispatcher.include_router(main_router)

    async with create_bot() as bot:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(
            commands=[
                BotCommand(command="start", description="Старт"),
                BotCommand(command="contacts", description="Контакты"),
                BotCommand(command="random", description="Рандом_call"),
                BotCommand(command="r", description="Сокращение от '/random'"),
                BotCommand(command="id", description="Telegram ID"),
            ],
        )
        await dispatcher.start_polling(bot)
