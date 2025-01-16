import taskiq_fastapi
from taskiq import InMemoryBroker
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from unibot.settings import settings

result_backend = RedisAsyncResultBackend(
    redis_url=str(settings.redis_url.with_path("/1")),
)
broker = AioPikaBroker(
    str(settings.rabbit_url),
).with_result_backend(result_backend)

if settings.environment.lower() == "pytest":
    broker = InMemoryBroker()  # type: ignore

taskiq_fastapi.init(
    broker,
    "unibot.web.application:get_app",
)
