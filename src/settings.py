import enum
import os
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL

TEMP_DIR = Path(gettempdir())


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = False
    environment: str = "dev"

    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_pass: str = "postgres"

    redis_host: str = "redis"
    redis_port: int = 6379
    redis_user: str = ""
    redis_pass: str = ""

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass
        )

    @property
    def redis_url(self) -> URL:
        """
        Assemble REDIS URL from settings.

        :return: redis URL.
        """
        return URL.build(
            scheme="redis",
            host=self.redis_host,
            port=self.redis_port,
            user=self.redis_user,
            password=self.redis_pass
        )

    # @property
    # def rabbit_url(self) -> URL:
    #     """
    #     Assemble RabbitMQ URL from settings.
    #
    #     :return: rabbit URL.
    #     """
    #     return URL.build(
    #         scheme="amqp",
    #         host=self.rabbit_host,
    #         port=self.rabbit_port,
    #         user=self.rabbit_user,
    #         password=self.rabbit_pass,
    #         path=self.rabbit_vhost,
    #     )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        env_file_encoding="utf-8",
    )


settings = Settings()
