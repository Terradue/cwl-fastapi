import json
import os
from pathlib import Path
from typing import Any, Dict
from app.core import config

from pydantic import BaseModel, BaseSettings, RedisDsn

from app.types.runners import RunnerDefinition


def json_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    """
    A simple settings source that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """
    encoding = settings.__config__.env_file_encoding
    return json.loads(
        Path(os.getenv("CWL_FASTAPI_CONFIG_PATH", "config.json")).read_text(encoding)
    )


class RedisConfig(BaseModel):
    dsn: RedisDsn = "redis://user:pass@localhost:6379/1"
    prefix: str = "cwlfastapi"


class Settings(BaseSettings):
    app_name: str = "CWL FastAPI"

    redis: RedisConfig = RedisConfig()

    runners: list[RunnerDefinition] = list[RunnerDefinition]()
    
    class Config:
        env_file = ".env"
        env_prefix = "CWL_FASTAPI_"
        env_nested_delimiter = "__"

        fields = {"redis.dsn": {"env": ["service_redis_dsn", "redis_url"]}}

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                json_config_settings_source,
            )


settings = Settings()
