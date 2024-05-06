from typing import TypeVar
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict

# from pydantic import SecretStr

TSettings = TypeVar("TSettings", bound=BaseSettings)


class TelegramBotSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="bot_")

    token: str  # SecretStr


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="database_")

    driver: str = "postgresql+asyncpg"
    name: str
    username: str
    password: str
    host: str

    echo: bool = False

    @property
    def url(self) -> str:
        password = quote_plus(self.password)
        return f"{self.driver}://{self.username}:{password}@{self.host}/{self.name}"
