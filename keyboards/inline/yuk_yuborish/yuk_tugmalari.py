from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

yuk_callback = CallbackData("viloyat", "item_name")

yuk_viloyatlar = InlineKeyboardMarkup(row_width=2)
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
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga": "Ortga",
    "Bosh menu": "Bosh menu",

}


for i,m in viloyat.items():
    yuk_viloyatlar.insert(InlineKeyboardButton(text=i,callback_data=m))




qanaqa_avto = InlineKeyboardMarkup(row_width=2)
qanaqa_avto.insert(InlineKeyboardButton(text='Kamaz',callback_data='Kamaz'))
qanaqa_avto.insert(InlineKeyboardButton(text='Zil',callback_data='Zil'))
qanaqa_avto.insert(InlineKeyboardButton(text='Labo',callback_data='Labo'))

ana = {
    "Ulug'nor":"ulug'nor",
    "Andijon shahar":"andijon shaxar",
    "Asaka":"asaka",
    "Baliqchi":"baliqchi",
    "Bo'ston ":"bo'ston",
    "Buloqbosh":"buloqboshi",
    "Izboskan":"izboskan",
    "Jalaquduq":"jalaquduq",
    "Xoʻjaobod":"xo'jabod",
    "Qoʻrgʻontepa":"qo'rg'ontepa",
    "Marhamat":"marhamat",
    "Oltinkoʻl":"oltinko'l",
    "Paxtaobod":"paxtaobod",
    "Shahrixon":"shaxrixon",
    "Xonabod":"xonabod",
}
andijon_yuk = InlineKeyboardMarkup(row_width=3)
for key,value in ana.items():
    andijon_yuk.insert(InlineKeyboardButton(text=key, callback_data=value))

andijon_yuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
andijon_yuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


uch_tugma = InlineKeyboardMarkup(row_width=3)
uch_tugma.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
uch_tugma.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
uch_tugma.insert(InlineKeyboardButton(text='Keyingisi',callback_data='Keyingisi'))
