from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import buxoro_callback

buxoro = {
"✅ Olot" :"olot",
"✅ Buxoro" :"buxor",
"✅ Gʻijduvon" :"gijduvon",
"✅ Jondor" :"jondor",
"✅ Kogon" :"kogon",
"✅ Qorakoʻl" :"qorakol",
"✅ Qorovulbozor" : "qorovul",
"✅ Peshku" :"peshku",
"✅ Romitan" :"romitan",
"✅ Shofirkon" :"shofirkon",
"✅ Vobkent" :"vobkent"
}

buxoro_viloyati_tumanlari = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro.items():
    buxoro_viloyati_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=value))



buxoro_y = {
"Buxoro shahri" :"buxoro shaxar",
"Buxoro tuman" :"buxoro tuman",
"Kogon shahar" :"kogon shahar",
"Kogon tuman" :"kogon tuman",
"Olot" :"olot tuman",
"Gʻijduvon" :"g'ijduvon tuman",
"Jondor" :"jondor tuman",
"Qorakoʻl" :"qorako'l tuman",
"Qorovulbozor" : "qorovulbozor tuman",
"Peshku" :"peshku tuman",
"Romitan" :"romitan tuman",
"Shofirkon" :"shofirkon tuman",
"Vobkent" :"vobkent tuman",

}

buxoro_yol = InlineKeyboardMarkup(row_width=2)
for key,value in buxoro_y.items():
    buxoro_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_yz = {
"Olot" :"x_olot",
"Buxoro shaxar" :"x_buxoro shaxar",
"Gʻijduvon" :"x_g'ijduvon",
"Jondor" :"x_jondor",
"Kogon" :"x_kogon",
"Qorakoʻl" :"x_qorako'l",
"Qorovulbozor" : "x_qorovulbozor",
"Peshku" :"x_peshku",
"Romitan" :"x_romitan",
"Shofirkon" :"x_shofirkon",
"Vobkent" :"x_vobkent",

}

buxoro_x = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_yz.items():
    buxoro_x.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_asa = {
"Olot" :"poch_olot",
"Buxoro" :"poch_buxoro shaxar",
"Gʻijduvon" :"poch_g'ijduvon",
"Jondor" :"poch_jondor",
"Kogon" :"poch_kogon",
"Qorakoʻl" :"poch_qorako'l",
"Qorovulbozor" : "poch_qorovulbozor",
"Peshku" :"poch_peshku",
"Romitan" :"poch_romitan",
"Shofirkon" :"poch_shofirkon",
"Vobkent" :"poch_vobkent",

}

buxoro_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_asa.items():
    buxoro_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_aasa = {
"Olot" :"yuuk_olot",
"Buxoro" :"yuuk_buxoro shaxar",
"Gʻijduvon" :"yuuk_g'ijduvon",
"Jondor" :"yuuk_jondor",
"Kogon" :"yuuk_kogon",
"Qorakoʻl" :"yuuk_qorako'l",
"Qorovulbozor" : "yuuk_qorovulbozor",
"Peshku" :"yuuk_peshku",
"Romitan" :"yuuk_romitan",
"Shofirkon" :"yuuk_shofirkon",
"Vobkent" :"yuuk_vobkent",

}

buxoro_yuuk = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_aasa.items():
    buxoro_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



buxoro_aasa1 = {
"Olot" :"yuuk_olot",
"Buxoro" :"mash_buxoro shaxar",
"Gʻijduvon" :"mash_g'ijduvon",
"Jondor" :"mash_jondor",
"Kogon" :"mash_kogon",
"Qorakoʻl" :"mash_qorako'l",
"Qorovulbozor" : "mash_qorovulbozor",
"Peshku" :"mash_peshku",
"Romitan" :"mash_romitan",
"Shofirkon" :"mash_shofirkon",
"Vobkent" :"mash_vobkent",

}

buxoro_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_aasa1.items():
    buxoro_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




navi_poch = {
    "Konimex" :"konimex",
    "Karmana" :"karmana",
    "Qiziltepa" :"qiziltepa",
    "Xatirchi" :"xatirchi",
    "Navbahor" :"navbahor",
    "Nurota" :"nurota",
    "Tomdi" :"tomdi",
    "Uchquduq" :"uchquduq",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}

navoiy_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key,value in navi_poch.items():
    navoiy_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))

buxoro_okdo = {
    "Olot" :"olot",
    "Buxoro" :"buxoro shaxar",
    "Gʻijduvon" :"g'ijduvon",
    "Jondor" :"jondor",
    "Kogon" :"kogon",
    "Qorakoʻl" :"qorako'l",
    "Qorovulbozor" : "qorovulbozor",
    "Peshku" :"peshku",
    "Romitan" :"romitan",
    "Shofirkon" :"shofirkon",
    "Vobkent" :"vobkent",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}

buxoro_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_okdo.items():
    buxoro_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))
