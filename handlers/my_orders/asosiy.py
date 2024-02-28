from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp, db

@dp.callback_query_handler(menu_callback.filter(item_name="meningbuyurtmalarim"))
async def my_orders_head(call:CallbackQuery):
    markup=InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yuk olishlar", callback_data="yukyuborishlar"))
    markup.insert(InlineKeyboardButton(text="Yuk mashinasiga buyurtma", callback_data="yukmashinasigabuyurtma"))
    markup.insert(InlineKeyboardButton(text="Pochta olishlar", callback_data="pochtayuborishlar"))
    markup.insert(InlineKeyboardButton(text="Pochta taxiga buyurtma", callback_data="pochtayuborishlar"))
    markup.insert(InlineKeyboardButton(text="Yo'lovchi olishlar", callback_data="yolovchiqabulqilish"))
    markup.insert(InlineKeyboardButton(text="Taxiga buyurtma", callback_data="yolovchiqabulqilish"))
    markup.insert(InlineKeyboardButton(text="Sayohatchi olishlar", callback_data="sayyohqabulqilish"))
    markup.insert(InlineKeyboardButton(text="Sayohat taxiga buyurtma", callback_data="sayyohqabulqilish"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytamiz"))

    await call.message.answer("Sizning buyurtmalaringiz !",reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(text="yukmashinasigabuyurtma")
async def yuk_yuborishlar_buyurtmalari(call:CallbackQuery):

    orders=await db.select_tayyor_yuk()
    for order in orders:
        print(order[1])
        # print(order[2])
        # print(order[3])
        # print(order[4])
@dp.callback_query_handler(text="Qaytamiz")
async def ortga_qaytish(call:CallbackQuery):
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