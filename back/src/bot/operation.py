from src.bot.config import bot, bot_conf


async def send_msg_error(msg: bytes):
    await bot.send_message(chat_id=bot_conf.ADMIN_ID, text=msg.decode())
