from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import kirish_callback, menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol
from loader import dp, db
from states.yolovchi_reys_states import Yolovchi_andijon


yolovchilar_royxati = []

@dp.callback_query_handler(kirish_callback.filter(item_name='yolovchi'))
async def haydovchi(call:CallbackQuery):
        yolovchilar_royxati.append(call.from_user.id)
        await db.add_yolovchi(username=call.from_user.username,telegram_id=call.from_user.id)
        await db.haydovchi_set(haydovchi=False, telegram_id=call.from_user.id)
        await db.yolovchi_set(yolovchi=True, telegram_id=call.from_user.id)
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)

@dp.callback_query_handler(menu_callback.filter(item_name='texikerak'),state=None)
async def yolovchi(call:CallbackQuery):
    last_get_orders = await db.get_order_joined_in_last_day_2()
    count = []
    for order in last_get_orders:
        if order[1] == call.from_user.id:
            count.append(call.from_user.id)
    if len(count) > 5:
        await call.message.answer("Kechirasiz bugungi limitingiz tugadi !")
    else:
        await call.message.answer("Qayerdan yurmoqchisiz ? \n",reply_markup=viloyatlar_yol)
        await call.message.delete()
        await Yolovchi_andijon.asosiy.set()



@dp.callback_query_handler(text='atmen')
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='ortga')
async def haydovchi(call:CallbackQuery,state: FSMContext):
    
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()
        await state.finish()

@dp.callback_query_handler(menu_callback.filter(item_name='haydovchibolibdavometish'))
async def haydovchi_bolib(call:CallbackQuery):
    driver = await db.select_driver(telegram_id=call.from_user.id)
    if driver is not None:
        await db.haydovchi_set(haydovchi=True, telegram_id=call.from_user.id)
        await db.yolovchi_set(yolovchi=False, telegram_id=call.from_user.id)
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
    else:
        await db.add_driver(tashiman_odam=None, tashiman_pochta=None, tashiman_yuk=True,
                            sayohatchi_tashiman=None,
                            telegram_id=call.from_user.id)
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
@dp.callback_query_handler(menu_callback.filter(item_name='yolovchibolibdavometish'))
async def haydovchi_bolib(call:CallbackQuery):
    await db.haydovchi_set(haydovchi=False, telegram_id=call.from_user.id)
    await db.yolovchi_set(yolovchi=True, telegram_id=call.from_user.id)
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()