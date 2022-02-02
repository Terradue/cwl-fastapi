import os

import redis

USERNAME = os.environ.get("CWLFASTAPI_REDIS_USERNAME")
PASSWORD = os.environ.get("CWLFASTAPI_REDIS_PASSWORD")


def get_redis_connection(hostname, port, username=USERNAME, password=PASSWORD):
    client_kwargs = {"host": hostname, "port": port, "decode_responses": True}
    if password:
        client_kwargs["password"] = password
    if username:
        client_kwargs["username"] = username

    return redis.Redis(**client_kwargs)
