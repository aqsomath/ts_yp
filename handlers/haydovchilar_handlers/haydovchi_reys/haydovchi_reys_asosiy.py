from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from states.haydovchi_reys_states import Reys_andijon

from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import tax_resy_vil, taxi_reys_callback
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1, kirish, umumiy_menu
from loader import dp, db


@dp.callback_query_handler(menu_callback.filter(item_name='yolovchikerak'))
async def yolovchi_kerak(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ",reply_markup=tax_resy_vil)
        await Reys_andijon.asosiy.set()
        await call.message.delete()


@dp.callback_query_handler(text='hdisdjsdhk',state=Reys_andijon.asosiy)
async def orga(call:CallbackQuery,state:FSMContext):
        user = await db.select_user(telegram_id=call.from_user.id)
        if user is not None:
                if user[5] == True:
                        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                                  reply_markup=umumiy_menu)
                        await call.message.delete()
                        await state.finish()
                elif user[6] == True:
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
                                markup.insert(InlineKeyboardButton(text=key,
                                                                   callback_data=menu_callback.new(item_name=value)))
                        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !",
                                                  reply_markup=markup)
                        await call.message.delete()
                        await state.finish()
                else:
                        await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
                        await state.finish()


