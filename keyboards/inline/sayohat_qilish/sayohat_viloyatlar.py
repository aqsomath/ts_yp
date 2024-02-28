from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

sayohat_callback = CallbackData("sayohat", "item_name")

viloyat = {
    "Andijon":"dushanba",
    "Namangan":"seshanba",
    "Farg'ona":"chorshanba",
    "Buxoro":"payshanba",
    "Toshkent":"juma",
    "Toshkent shahar":"kent shahar",
    "Sirdaryo":"shanba",
    "Surxondaryo":"yakshanba",
    "Qashqadaryo":"iyul",
    "Xorazm":"july",
    "Navoiy":"avgust",
    "Jizzax":"sentabr",
    "Samarqand":"oktabr",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"Ortga",
    "Bosh menu":"Bosh menu",
}
sayohat_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    sayohat_vil.insert(InlineKeyboardButton(text=key, callback_data=value))
