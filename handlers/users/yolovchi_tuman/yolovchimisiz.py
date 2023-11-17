from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import kirish_callback, menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol
from loader import dp


@dp.callback_query_handler(kirish_callback.filter(item_name='yolovchi'))
async def haydovchi(call:CallbackQuery):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)


@dp.callback_query_handler(menu_callback.filter(item_name='texikerak'),state=None)
async def yolovchi(call:CallbackQuery):
    await call.message.answer("Qayerdan yurmoqchisiz ? \n",reply_markup=viloyatlar_yol)




@dp.callback_query_handler(text='atmen')
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='ortga')
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()

@dp.callback_query_handler(menu_callback.filter(item_name='haydovchibolibdavometish'))
async def haydovchi_bolib(call:CallbackQuery):
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
        "Filtrlash": "filtrlash_1",
        "Viloyatlarni filtrlash": "viloyalarnifiltrlash",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)