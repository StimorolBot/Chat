import asyncio
from typing import TYPE_CHECKING
from aio_pika.abc import AbstractIncomingMessage

from src.core.logger_conf import rmq_logger
from src.rmq.config import get_connection, ROUTING_KEY
from src.bot.operation import send_msg_error

if TYPE_CHECKING:
    from aio_pika.channel import Channel


async def callback(msg: AbstractIncomingMessage):
    rmq_logger.debug(f"[consumer] Сообщение: {msg} успешно получено")
    rmq_logger.debug(f"[consumer] Тело сообщения: {msg.body}")
    await send_msg_error(msg=msg.body)


async def consume_msg(channel: "Channel"):
    queue = await channel.declare_queue(ROUTING_KEY)
    await queue.consume(callback, no_ack=True)


async def consumer():
    async with await get_connection() as connection:
        rmq_logger.info(f"[consumer] Подключение: {connection}")
        async with connection.channel() as channel:
            await consume_msg(channel)
            rmq_logger.info(" [consumer] Ожидание сообщений... Для выхода нажмите CTRL+C")
            await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(consumer())
    except KeyboardInterrupt:
        rmq_logger.info(f"[consumer] Соединение закрыто")
