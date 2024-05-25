from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.users.tariflar.asosiy import second, third, first, fifth, fourth,hammaga_bepul
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu, kirish
from loader import db, dp




@dp.callback_query_handler(text="hammagapullikqilish")
async def hammaga_pullik(call:CallbackQuery):
    fourth.clear()
    fifth.clear()
    hammaga_bepul.clear()
    await call.message.answer("Hamma uchun pullik bo'ldi !!!")

@dp.callback_query_handler(text="hammagabepulqilish")
async def hammaga_pullik(call:CallbackQuery):
    users = await db.select_all_users()
    for user in users:
        hammaga_bepul.append(user[3])
    await call.message.answer("Hamma uchun bepul bo'ldi !!!")