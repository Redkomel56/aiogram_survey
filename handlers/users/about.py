from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp

@dp.message_handler(Command('about'))
async def about(message: types.Message):
    text = """Scenic Spots - это сайт-фотогалерея, который позволит вам узнать о новых местах, куда сходить, куда прогуляться, он выдаст вам полезную информацию о том где это, покажет как туда добраться и адрес. Также покажет фотографии из этого места."""
    await message.answer(text=text)