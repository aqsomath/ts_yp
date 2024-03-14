from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

taxi_reys_callback = CallbackData("sayohat", "item_name")

viloyat = {
    "Andijon":"santi",
    "Namangan":"milli",
    "Farg'ona":"detsi",
    "Buxoro":"kilo",
    "Toshkent":"tonna",
    "Sirdaryo":"mega",
    "Surxondaryo":"mikro",
    "Qashqadaryo":"makro",
    "Xorazm":"nano",
    "Navoiy":"piko",
    "Jizzax":"kvadrat",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Samarqand":"diogonal",
    "Ortga":"hdisdjsdhk",
}
tax_resy_vil: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    tax_resy_vil.insert(InlineKeyboardButton(text=key, callback_data=value))


reys_ortgaa = InlineKeyboardMarkup(row_width=3)

oylar = {
    "Bugun":"Bugun",
    "Ertaga":"Ertaga",
    "Indinga":"Indinga",
    "Kiritish":"Qoldakiritish",
}
for key, value in oylar.items():
    reys_ortgaa.insert(InlineKeyboardButton(text=key, callback_data=value))
reys_ortgaa.insert(InlineKeyboardButton(text='Ortga',callback_data="ortga"))
reys_ortgaa.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data="atmen"))