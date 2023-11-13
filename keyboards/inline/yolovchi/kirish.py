from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import kirish_callback, menu_callback

kirish = InlineKeyboardMarkup(row_width=2)
kirish.insert(InlineKeyboardButton(text="Haydovchimisiz", callback_data=kirish_callback.new(item_name='haydovchi')))
kirish.insert(InlineKeyboardButton(text="Yo'lovchimisiz", callback_data=kirish_callback.new(item_name='yolovchi')))




menu = {
    "Yo'lovchi reys belgilash":'texikerak',
    "Tayyor taksi":'tayyortaksi',
    "Yuk yuborish kerak":'yukyuborishkerak',
    "Tayyor yuk mashinasi": "tayyoryukmashinasi",
    "Pochta yuborish kerak":'pochtayuborishkerak',
    "Tayyor pochta mashinasi":"tayyorpochtamashinasi",
    "Sayohatga mashina kerak":'sayohatgamashina',
    "Tayyor sayohatga mashina":'tayyorsayohatgamashina',
    "Mening buyurtmalarim":"meningbuyurtmalarim",
    "Admin bilan bog'lanish":"adminbilanboglanish",
}
umumiy_menu = InlineKeyboardMarkup(row_width=2)
for key,value in menu.items():
    umumiy_menu.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))



necha_kishisizlar = InlineKeyboardMarkup(
   inline_keyboard =[
                [
                    InlineKeyboardButton(text="1", callback_data="1"),
                    InlineKeyboardButton(text="2", callback_data="2"),
                    InlineKeyboardButton(text="3", callback_data="3"),
                    InlineKeyboardButton(text="4", callback_data="4"),
                    InlineKeyboardButton(text="5", callback_data="5"),
                ]
    ],

    row_width=2
)
necha_kishisizlar_yuk = InlineKeyboardMarkup(
   inline_keyboard =[
                [
                    InlineKeyboardButton(text="1", callback_data="1"),
                    InlineKeyboardButton(text="2", callback_data="2"),
                    InlineKeyboardButton(text="3", callback_data="3"),
                    InlineKeyboardButton(text="4", callback_data="4"),
                    InlineKeyboardButton(text="0", callback_data="0"),
                ]
    ],

    row_width=2
)

oldi_kerakmi = InlineKeyboardMarkup(row_width=2)
oldi_kerakmi.insert(InlineKeyboardButton(text="Xa kerak", callback_data="Oldi o'rindiq kerak"))
oldi_kerakmi.insert(InlineKeyboardButton(text="Yo'q kerak emas", callback_data="Oldi o'rindiq kerak emas"))


yuk_mashina_turi = InlineKeyboardMarkup(row_width=2)
yuk_mashina_turi.insert(InlineKeyboardButton(text='Kamaz',callback_data='Kamaz'))
yuk_mashina_turi.insert(InlineKeyboardButton(text='Zil',callback_data='Zil'))
yuk_mashina_turi.insert(InlineKeyboardButton(text='Labo',callback_data='Labo'))



qanday_avto=InlineKeyboardMarkup(row_width=3)
qanday_avto.insert(InlineKeyboardButton(text='Ekonom', callback_data="Ekonom",))
qanday_avto.insert(InlineKeyboardButton(text='Komfort', callback_data="Komfort"))
qanday_avto.insert(InlineKeyboardButton(text='Biznez klass', callback_data="Biznes klass"))
qanday_avto.insert(InlineKeyboardButton(text="Farqi yo'q", callback_data="Farqi yo'q"))

tasdiq_oxir = InlineKeyboardMarkup(row_width=2)
tasdiq_oxir.insert(InlineKeyboardButton(text="Xa", callback_data="Confirm"))
tasdiq_oxir.insert(InlineKeyboardButton(text="Yo'q", callback_data="UnConfirm"))