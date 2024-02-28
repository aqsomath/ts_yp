from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import andijon_callback
tshahar={
        "Toshkent shahar":"Toshkent shahar",
        "Bektemir":"Bektemir tumani",
        "Mirzo Ulug‘bek":"Mirzo Ulug'bek tumani",
        "Mirobod tumani":"Mirobod tumani",
        "Olmazor tumani":"Olmazor tumani",
        "Sirg‘ali tumani":"Sirg'ali tumani",
        "Uchtepa tumani":"Uchtepa tumani",
        "Chilonzor tumani":"Chilonzor tumani",
        "Shayxontohur tumani":"Shayxontohur tumani",
        "Yunusobod tumani":"Yunusobod tumani",
        "Yakkasaroy tumani":"Yakkasaroy tumani",
        "Yashnobod tumani":"Yashnobod tumani",
        "Ortga":"ortga",
        "Bosh menu":"atmen",
         }
tosh_shsha=InlineKeyboardMarkup(row_width=2)
for key,value in tshahar.items():
    tosh_shsha.insert(InlineKeyboardButton(text=key,callback_data=value))
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
    "Hammasini rad etish":"Xahh",
    "Bosh menu": "glavmenu",
    "Ortga":"qaytamiz",

}

andijon_old = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    andijon_old.insert(InlineKeyboardButton(text=key, callback_data=andijon_callback.new(item_name=value)))

an = {
    "Andijon shahar": "andijon shaxar",
    "Andijon tuman": "andijon tuman",
    "Xonabod shahar": "xonabod shahar",
    "Ulug'nor":"ulug'nor tuman",
    "Asaka":"asaka tuman",
    "Baliqchi":"baliqchi tuman",
    "Bo'ston ":"bo'ston tuman",
    "Buloqbosh":"buloqboshi tuman",
    "Izboskan":"izboskan tuman",
    "Jalaquduq":"jalaquduq tuman",
    "Xoʻjaobod":"xo'jabod tuman",
    "Qoʻrgʻontepa":"qo'rg'ontepa tuman",
    "Marhamat":"marhamat tuman",
    "Oltinkoʻl":"oltinko'l tuman",
    "Paxtaobod":"paxtaobod tuman",
    "Shahrixon":"shaxrixon tuman",
}
andijon_yol = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    andijon_yol.insert(InlineKeyboardButton(text=key, callback_data=value))

andijon_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
andijon_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qoraqalpoq={
"Nukus shahri":"Nukus shahar",
"Amudaryo tumani":"Amudaryo tumani",
"Beruniy tumani":"Beruniy tumani",
"Kegeyli tumani":"Kegeyli tumani",
"Qanliko‘l tumani":"Qanliko'l tumani",
"Qorao‘zak tumani":"Qorao'zak tumani",
"Qo‘ng‘irot tumani":"Qo'ng'irot tumani",
"Mo‘ynoq tumani":"Mo'ynoq tumani",
"Nukus tumani":"Nukus tumani",
"Taxiatosh tumani":"Taxiatosh tumani",
"Taxtako‘pir tumani":"Taxtako'prik tumani",
"To‘rtko‘l tumani":"To'rtko'l tumani",
"Xo‘jayli tumani":"Xo'jayli tumani",
"Chimboy tumani":"Chimboy tumani",
"Sho‘manoy tumani":"Sho'manoy tumani",
"Ellikqal’a tumani":"Ellikqal'a tumani",
"Ortga":"ortga",
"Bosh menu":"atmen"
}
qoraqalpogiston_yol = InlineKeyboardMarkup()
for key,value in qoraqalpoq.items():
    qoraqalpogiston_yol.insert(InlineKeyboardButton(text=key,callback_data=value))






anxx= {
    "Ulug'nor":"ulugnor",
    "Andijon shahar":"shaxar",
    "Asaka":"asaka",
    "Baliqchi":"baliqchi",
    "Bo'ston ":"boz",
    "Buloqbosh":"buloqboshi",
    "Izboskan":"izboskan",
    "Jalaquduq":"jalaquduq",
    "Xoʻjaobod":"xojabod",
    "Qoʻrgʻontepa":"qorgontepa",
    "Marhamat":"marhamat",
    "Oltinkoʻl":"oltinkol",
    "Paxtaobod":"paxtaobod",
    "Shahrixon":"shaxrixon",
    "Xonabod":"xonabod",
    "Boshqa viloyat":"boshqaviloyat",
    "Bosh menu": "glavmenu",
    "Ortga":"qaytamiz",

}

andijon_pochta_uchun = InlineKeyboardMarkup(row_width=3)
for key,value in anxx.items():
    andijon_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))