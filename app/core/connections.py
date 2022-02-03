import redis
from pydantic import RedisDsn
from app.core import config


def get_redis_connection() -> redis.Redis:
    return redis.Redis.from_url(config.settings.redis.dsn)
