from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from states.yuk_reys_states import Yuk_reys_andijon

from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import tax_yuk_vil, taxi_yuk_callback
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1, umumiy_menu, kirish
from loader import dp, db


@dp.callback_query_handler(menu_callback.filter(item_name='yukkerak'))
async def yuk_reys_asosiy(call:CallbackQuery):
    
        await call.message.answer("Qaysi viloyatlardan yuk olasiz ? ",reply_markup=tax_yuk_vil)
        await Yuk_reys_andijon.asosiy.set()
        await call.message.delete()
@dp.callback_query_handler(text='ortga',state=Yuk_reys_andijon.asosiy)
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