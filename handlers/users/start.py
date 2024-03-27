from aiogram import types,filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.edit_district.sozlamalar import haydovchilar_royxati
from handlers.users.yolovchi_tuman.yolovchimisiz import yolovchilar_royxati
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import kirish, umumiy_menu
from loader import dp, db, bot

admin_ids = [6132434228,343103355]

@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    existing_user = await db.select_user(telegram_id=message.from_user.id)
    if existing_user:
        pass
    else:
        await db.add_user(full_name=message.from_user.full_name, username=message.from_user.username,
                          telegram_id=message.from_user.id)
    yolovchi = await db.select_yolovchi(telegram_id=message.from_user.id)
    if yolovchi is not None:
        await message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await message.delete()


    elif message.from_user.id in haydovchilar_royxati:
        driver = {
            "Haydovchi reys belgilash": 'yolovchikerak',
            "Tayyor yo'lovchi": 'tayyoryolovchi',
            "Yuk kerak": 'yukkerak',
            "Tayyor yuk": "tayyoryuk",
            "Pochta kerak": 'pochtakerak',
            "Tayyor pochta": "tayyorpochta",
            "Sayohatchilar kerak": 'sayohatgayolovchi',
            "Tayyor sayohatchi": "tayyorsayohatchi",
            "Mening buyurtmalarim": "meningbuyurtmalarim",
            "Admin bilan bog'lanish": "adminbilanboglanish",
            "Sozlamalar": "nastroyki",
            "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"
        }
        markup = InlineKeyboardMarkup(row_width=2)
        for key, value in driver.items():
            markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
        await message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await message.delete()
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=kirish)




