from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

taxi_pochta_callback = CallbackData("pochta_tashish", "item_name")

viloyat = {
    "Andijon":"raz",
    "Namangan":"dva",
    "Farg'ona":"tri",
    "Buxoro":"chitiri",
    "Toshkent shahar":"kent shahar",
    "Toshkent":"pyat",
    "Sirdaryo":"shest",
    "Surxondaryo":"sem",
    "Qashqadaryo":"vosem",
    "Xorazm":"devit",
    "Navoiy":"desit",
    "Jizzax":"adinatsat",
    "Samarqand":"dvinatsad",
    "Qoraqalpog'iston":"qoraqalpoq",
}
tax_pochta_vil: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    tax_pochta_vil.insert(InlineKeyboardButton(text=key, callback_data=value))
tax_pochta_vil.insert(InlineKeyboardButton(text="Ortga ", callback_data="oderjflls"))
tax_pochta_vil.insert(InlineKeyboardButton(text="Buyurtmani bekor qilish ", callback_data="appfoo"))

yuk_ortgaa = InlineKeyboardMarkup(row_width=2)
yuk_ortgaa.insert(InlineKeyboardButton(text='ortga',callback_data="ortga"))
yuk_ortgaa.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data="atmen"))