from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.yolovchi.kirish import kirish
from loader import dp
from utils.db_api.postgresql import Database

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=kirish)





