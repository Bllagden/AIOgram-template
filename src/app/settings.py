from typing import TypeVar
from urllib.parse import quote_plus

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


class TelegramBotSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="bot_")

    token: SecretStr


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="db_")

    driver: str = "postgresql+asyncpg"
    host: str
    port: str
    username: str
    password: str
    name: str

    echo: bool

    @property
    def url(self) -> str:
        password = quote_plus(self.password)
        return f"{self.driver}://{self.username}:{password}@{self.host}:{self.port}/{self.name}"
