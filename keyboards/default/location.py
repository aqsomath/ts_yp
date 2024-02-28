from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


lokatsiya = ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="Lokatsiya yuborish", request_location=True),
                        ],
                    ],
                    resize_keyboard=True
)
keyingisi = InlineKeyboardMarkup(row_width=2)
keyingisi.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
keyingisi.insert(InlineKeyboardButton(text='Keyingisi',callback_data='yingisi'))
keyingisi.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
phone_number = ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="Kontak yuborish", request_contact=True),
                        ],
                    ],
                    resize_keyboard=True,one_time_keyboard=True
)

orqaga_qaytish= InlineKeyboardMarkup(row_width=2)
# orqaga_qaytish.insert(InlineKeyboardButton(text='Keyingisi',callback_data='keyingisi'))
orqaga_qaytish.insert(InlineKeyboardButton(text='Ortga',callback_data='ortga'))
orqaga_qaytish.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
#
phone_ortga = InlineKeyboardMarkup(row_width=2)

phone_ortga.insert(InlineKeyboardButton(text='Ortga',callback_data='ortga'))
phone_ortga.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))