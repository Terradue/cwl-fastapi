from fastapi import FastAPI
from redis import exceptions

from app.core import config
from app.core.connections import get_redis_connection
from app.core.redis import KeySchema


def configure(app: FastAPI) -> None:
    key_schema = KeySchema(config.settings.redis.prefix)
    redis_client = get_redis_connection()

    try:
        redis_client.ping()
    except exceptions.AuthenticationError:
        app.logger.error(
            "Redis authentication failed. Make sure you set "
            "$CWLFASTAPI_REDIS_PASSWORD to the correct password "
            "for your Redis instance. Stopping server."
        )
        raise
