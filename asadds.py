import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.statics.admin_panel import user_of_banned
from handlers.users.tariflar import first,fifth,fourth,second,third
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp, db, bot

markup_1 = InlineKeyboardMarkup(row_width=2)
markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                     callback_data="Mijozbormaydiganbolibdi"))
markup_1.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
print(markup_1["inline_keyboard"][0][0]["callback_data"])