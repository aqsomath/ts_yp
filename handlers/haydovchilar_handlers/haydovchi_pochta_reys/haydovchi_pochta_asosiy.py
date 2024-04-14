from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.haydovchi_reys.haydovchi_pochta_reys import tax_pochta_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import kirish, umumiy_menu
from loader import dp, db
from states.haydovchi_pochta_states import Reys_pochta_andijon


@dp.callback_query_handler(menu_callback.filter(item_name='pochtakerak'))
async def yuk_reys_asosiy(call:CallbackQuery):
    
        await call.message.answer("Qaysi viloyatlardan pochta olasiz ? ",reply_markup=tax_pochta_vil)
        await Reys_pochta_andijon.asosiy.set()
        await call.message.delete()
@dp.callback_query_handler(text=["oderjflls","appfoo"],state=Reys_pochta_andijon.asosiy)
async def p_qayt(call:CallbackQuery,state:FSMContext):
    yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
    haydovchi = await db.select_haydovchi(telegram_id=call.from_user.id)
    if yolovchi is not None:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()
        await state.finish()

    elif haydovchi is not None:
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
        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await call.message.delete()
        await state.finish()

    else:
        await call.message.answer(f"Salom, {call.message.from_user.full_name}!", reply_markup=kirish)
        await state.finish()

