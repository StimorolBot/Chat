import os
from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


class BotConf(BaseSettings):
    TOKEN: str
    ADMIN_ID: int

    model_config = SettingsConfigDict(env_file=f"{os.path.dirname(os.path.abspath(__file__))}/.env")


bot_conf = BotConf()
bot = Bot(token=bot_conf.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
