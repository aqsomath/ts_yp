from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

taxi_sayohat_callback = CallbackData("haydovchi_sayohat", "item_name")

viloyat = {
    "Andijon":"alif",
    "Namangan":"ba",
    "Farg'ona":"ta",
    "Buxoro":"sa",
    "Toshkent shahar":"kent shahar",
    "Toshkent":"jim",
    "Sirdaryo":"ha",
    "Surxondaryo":"xo",
    "Qashqadaryo":"ayn",
    "Xorazm":"goyn",
    "Navoiy":"sod",
    "Jizzax":"dod",
    "Samarqand":"mim",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"ortga",
    "Bosh menu":"boshmenu",
}
tax_say_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    tax_say_vil.insert(InlineKeyboardButton(text=key, callback_data=value))


reys_ortgaa = InlineKeyboardMarkup(row_width=2)
reys_ortgaa.insert(InlineKeyboardButton(text='ortga',callback_data="ortga"))
reys_ortgaa.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data="atmen"))