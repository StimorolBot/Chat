from aio_pika import Message
from typing import TYPE_CHECKING

from src.core.logger_conf import rmq_logger
from src.rmq.config import get_connection, ROUTING_KEY

if TYPE_CHECKING:
    from aio_pika.channel import Channel

# sudo rabbitmq-server –detached


async def produce_msg(channel: "Channel", msg: bytes):
    queue = await channel.declare_queue(ROUTING_KEY)
    await channel.default_exchange.publish(
        Message(msg), routing_key=queue.name
    )
    rmq_logger.debug(f"[publisher] Сообщение: '{msg.decode()}' отправлено в очередь: {queue}")


async def publisher(msg: bytes):
    async with await get_connection() as connection:
        rmq_logger.info(f"[publisher] Подключение: {connection}")
        async with connection.channel() as channel:
            rmq_logger.debug(f"[publisher] Канал создан: {channel}")
            await produce_msg(channel=channel, msg=msg)
