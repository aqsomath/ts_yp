import asyncio

from aiogram import types,filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.tariflar.asosiy import fourth, fifth
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import kirish, umumiy_menu
from loader import dp, db, bot


@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    if len(fourth)>0:
        fourth.append(message.from_user.id)
    if len(fifth)>0:
        fifth.append(message.from_user.id)
        five = await db.select_tarif(tarif_name='fifth')
        await asyncio.sleep(five[3]*24*60*60)
        fifth.remove(message.from_user.id)
    existing_user = await db.select_user(telegram_id=message.from_user.id)
    if existing_user:
        pass
    else:
        await db.add_user(full_name=message.from_user.full_name, username=message.from_user.username,
                          telegram_id=message.from_user.id,balans=0)
    user = await db.select_user(telegram_id=message.from_user.id)
    if user is not None:
        if user[5]==True:
            await message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
            await message.delete()

        elif user[6]==True:
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




