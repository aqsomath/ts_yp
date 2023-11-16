from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import andijon_callback

x=["Ulug'nor","Andijon shahar",
   "Asaka","Baliqchi","Bo'ston",
   "Buloqbosh","Izboskan","Jalaquduq",
   "Xoʻjaobod","Qoʻrgʻontepa","Marhamat",
   "Oltinkoʻl","Paxtaobod","Shahrixon","Xonabod"
   ]
an = {
    "✅ Ulug'nor":"ulugnor",
    "✅ Andijon shahar":"shaxar",
    "✅ Asaka":"asaka",
    "✅ Baliqchi":"baliqchi",
    "✅ Bo'ston ":"boz",
    "✅ Buloqbosh":"buloqboshi",
    "✅ Izboskan":"izboskan",
    "✅ Jalaquduq":"jalaquduq",
    "✅ Xoʻjaobod":"xojabod",
    "✅ Qoʻrgʻontepa":"qorgontepa",
    "✅ Marhamat":"marhamat",
    "✅ Oltinkoʻl":"oltinkol",
    "✅ Paxtaobod":"paxtaobod",
    "✅ Shahrixon":"shaxrixon",
    "✅ Xonabod":"xonabod",
}
andijon_old = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    andijon_old.insert(InlineKeyboardButton(text=key, callback_data=andijon_callback.new(item_name=value)))

an = {
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
andijon_yol = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    andijon_yol.insert(InlineKeyboardButton(text=key, callback_data=value))

andijon_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
andijon_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



ansss = {
    "Ulug'nor":"x_ulug'nor",
    "Andijon shahar":"x_andijon shaxar",
    "Asaka":"x_asaka",
    "Baliqchi":"x_baliqchi",
    "Bo'ston ":"x_bo'ston",
    "Buloqbosh":"x_buloqboshi",
    "Izboskan":"x_izboskan",
    "Jalaquduq":"x_jalaquduq",
    "Xoʻjaobod":"x_xo'jabod",
    "Qoʻrgʻontepa":"x_qo'rg'ontepa",
    "Marhamat":"x_marhamat",
    "Oltinkoʻl":"x_oltinko'l",
    "Paxtaobod":"x_paxtaobod",
    "Shahrixon":"x_shaxrixon",
    "Xonabod":"x_xonabod",
}
andijon_x = InlineKeyboardMarkup(row_width=3)
for key,value in ansss.items():
    andijon_x.insert(InlineKeyboardButton(text=key, callback_data=value))
anss = {
    "Ulug'nor":"poch_ulug'nor",
    "Andijon shahar":"poch_andijon shaxar",
    "Asaka":"poch_asaka",
    "Baliqchi":"poch_baliqchi",
    "Bo'ston ":"poch_bo'ston",
    "Buloqbosh":"poch_buloqboshi",
    "Izboskan":"poch_izboskan",
    "Jalaquduq":"poch_jalaquduq",
    "Xoʻjaobod":"poch_xo'jabod",
    "Qoʻrgʻontepa":"poch_qo'rg'ontepa",
    "Marhamat":"poch_marhamat",
    "Oltinkoʻl":"poch_oltinko'l",
    "Paxtaobod":"poch_paxtaobod",
    "Shahrixon":"poch_shaxrixon",
    "Xonabod":"poch_xonabod",
}
andijon_pochta = InlineKeyboardMarkup(row_width=3)
for key,value in anss.items():
    andijon_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
    
anssaa = {
    "Ulug'nor":"yuuk_ulug'nor",
    "Andijon shahar":"yuuk_andijon shaxar",
    "Asaka":"yuuk_asaka",
    "Baliqchi":"yuuk_baliqchi",
    "Bo'ston ":"yuuk_bo'ston",
    "Buloqbosh":"yuuk_buloqboshi",
    "Izboskan":"yuuk_izboskan",
    "Jalaquduq":"yuuk_jalaquduq",
    "Xoʻjaobod":"yuuk_xo'jabod",
    "Qoʻrgʻontepa":"yuuk_qo'rg'ontepa",
    "Marhamat":"yuuk_marhamat",
    "Oltinkoʻl":"yuuk_oltinko'l",
    "Paxtaobod":"yuuk_paxtaobod",
    "Shahrixon":"yuuk_shaxrixon",
    "Xonabod":"yuuk_xonabod",
}
andijon_yuuk = InlineKeyboardMarkup(row_width=3)
for key,value in anssaa.items():
    andijon_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))


yuk_and = {
    "Ulug'nor":"mash_ulug'nor",
    "Andijon shahar":"mash_andijon shaxar",
    "Asaka":"mash_asaka",
    "Baliqchi":"mash_baliqchi",
    "Bo'ston ":"mash_bo'ston",
    "Buloqbosh":"mash_buloqboshi",
    "Izboskan":"mash_izboskan",
    "Jalaquduq":"mash_jalaquduq",
    "Xoʻjaobod":"mash_xo'jabod",
    "Qoʻrgʻontepa":"mash_qo'rg'ontepa",
    "Marhamat":"mash_marhamat",
    "Oltinkoʻl":"mash_oltinko'l",
    "Paxtaobod":"mash_paxtaobod",
    "Shahrixon":"mash_shaxrixon",
    "Xonabod":"mash_xonabod",
}
andijon_yuuk_mashina = InlineKeyboardMarkup(row_width=3)
for key,value in yuk_and.items():
    andijon_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
    