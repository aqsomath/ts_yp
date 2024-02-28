from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


yes_not = InlineKeyboardMarkup(row_width=2)
yn = {
    "Xa ✅":"yesss",
    "Yo'q ❌":"nott",
    "Qo'shimcha ma'lumot kiritish 📝":"add_information",
    "Ortga":"ortga",


}
for key,value in yn.items():
    yes_not.insert(InlineKeyboardButton(text=key, callback_data=value))

