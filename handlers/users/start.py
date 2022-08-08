from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nЭто бот был создан для стать на сайте directprobi.ru\nНапишите комманду \help чтобы получить подробную информацию о возможнастях бота")
