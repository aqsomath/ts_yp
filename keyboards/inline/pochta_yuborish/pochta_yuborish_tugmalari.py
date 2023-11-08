from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

pochta_callback = CallbackData("viloyat_pochta", "item_name")

pochta_viloyatlar = InlineKeyboardMarkup(row_width=2)
viloyat = {
    "Andijon":"111",
    "Namangan":"222",
    "Farg'ona":"333",
    "Buxoro":"4444",
    "Toshkent":"5555",
    "Sirdaryo":"6666",
    "Surxondaryo":"7777",
    "Qashqadaryo":"8888",
    "Xorazm":"9999",
    "Navoiy":"101010",
    "Jizzax":"121212",
    "Samarqand":"131313",
}


for i,m in viloyat.items():
  pochta_viloyatlar.insert(InlineKeyboardButton(text=i,callback_data=pochta_callback.new(item_name=m)))

