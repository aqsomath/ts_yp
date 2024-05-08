from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import time_callback

soat = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "10":"10",
    "11":"11",
    "12":"12",
    "13":"13",
    "14":"14",
    "15":"15",
    "16":"16",
    "17":"17",
    "18":"18",
    "19":"19",
    "20":"20",
    "21":"21",
    "22":"22",
    "23":"23",
    "00":"00",


}


time = InlineKeyboardMarkup(row_width=6)
for key,value in soat.items():
    time.insert(InlineKeyboardButton(text=key, callback_data=value))
time.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
time.insert(InlineKeyboardButton(text='Ortga',callback_data='ortga'))
