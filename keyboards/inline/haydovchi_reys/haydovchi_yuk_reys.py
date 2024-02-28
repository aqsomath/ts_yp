from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

taxi_yuk_callback = CallbackData("yuk_tashish", "item_name")

viloyat = {
    "Andijon":"monday",
    "Namangan":"tuesday",
    "Farg'ona":"wenesday",
    "Buxoro":"thursday",
    "Toshkent shahar":"kent shahar",
    "Toshkent":"friday",
    "Sirdaryo":"saturday",
    "Surxondaryo":"sunday",
    "Qashqadaryo":"january",
    "Xorazm":"february",
    "Navoiy":"march",
    "Jizzax":"june",
    "Samarqand":"july",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"ortga",
}
tax_yuk_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    tax_yuk_vil.insert(InlineKeyboardButton(text=key, callback_data=value))


yuk_ortgaa = InlineKeyboardMarkup(row_width=2)
yuk_ortgaa.insert(InlineKeyboardButton(text='ortga',callback_data="ortga"))
yuk_ortgaa.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data="atmen"))