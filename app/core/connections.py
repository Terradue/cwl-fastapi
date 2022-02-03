import os
from pydantic import RedisDsn
import redis


def get_redis_connection(redis_dsn: RedisDsn) -> redis.Redis:
    return redis.Redis.from_url(redis_dsn)
