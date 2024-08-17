from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import Message
from aiogram.filters import Command


if TYPE_CHECKING:
    from aiogram import Dispatcher


async def command_start_handler(message: Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


async def command_bad_handler(message: Message):
    await message.answer(f"Неизвестная команда: '{message.text}'!")


def register_handlers(dp: "Dispatcher"):
    dp.message.register(command_start_handler, Command(commands=["start"]))
    dp.message.register(command_bad_handler)
