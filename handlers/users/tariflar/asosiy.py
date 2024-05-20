from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp, db
first = []
second = []
third = []
fourth = []
fifth = []
hammaga_bepul = []

@dp.callback_query_handler(text='barchatariflar')
async def tarif_conf(call:CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Hamma uchun bepul", callback_data="hammagabepulqilish"))
    markup.insert(InlineKeyboardButton(text="Hamma uchun pullik", callback_data="hammagapullikqilish"))
    markup.insert(InlineKeyboardButton(text="1 - tarif", callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif", callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif", callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif", callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif", callback_data="conffifthsetting"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Adminbolimgaqayt"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="skldjuiuiuiuiererere"))
    await call.message.answer("Ta'riflar bo'limi",reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(text='Adminbolimgaqayt')
async def adminga_qaytish(call:CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Statistika", callback_data="umumiystatistika"))
    markup.insert(InlineKeyboardButton(text="Foydalanuvchilar", callback_data="foydalanuvchilarniqidirish"))
    markup.insert(InlineKeyboardButton(text="Adminlar", callback_data="adminlarroyxati"))
    markup.insert(InlineKeyboardButton(text="Buyurtmalar", callback_data="baribuyurtmalar"))
    markup.insert(InlineKeyboardButton(text="Ban qilish", callback_data="banqilish"))
    markup.insert(InlineKeyboardButton(text="Bandan chiqarish", callback_data="bandanchiqarish"))
    markup.insert(InlineKeyboardButton(text="Tariflar", callback_data='barchatariflar'))
    markup.insert(InlineKeyboardButton(text="Balans to'ldirish", callback_data="Balanstoldirish"))
    markup.insert(InlineKeyboardButton(text="Balans ayirish", callback_data="Balansayrish"))
    await call.message.answer(reply_markup=markup, text="Admin bo'lim")
    await call.message.delete()



@dp.callback_query_handler(text="skldjuiuiuiuiererere")
async def menuu(call:CallbackQuery):
    yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
    if yolovchi is not None:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    else:
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