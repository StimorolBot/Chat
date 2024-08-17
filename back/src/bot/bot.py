import sys
import asyncio
import logging

from src.bot.config import dp, bot
from src.bot.handlers import register_handlers


async def main():
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
