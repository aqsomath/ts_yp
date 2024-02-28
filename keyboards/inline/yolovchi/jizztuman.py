from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import jizzax_callback

jizzax = {
"✅ Arnasoy" :"arnasoy",
"✅ Baxmal" :"baxmal",
"✅ Doʻstlik" :"dostlik",
"✅ Forish" :"forish",
"✅ Gʻallaorol" :"gallarol",
"✅ Sharof Rashidov ":"sharof rashidov",
'✅ Mirzachoʻl' :'mirzachol',
"✅ Paxtakor" :"paxtakor",
"✅ Yangiobod" :"yangi obod",
'✅ Zomin' :"zomin",
'✅ Zafarobod' :"zafarobod",
'✅ Zarbdor' :"zarbdor"
}
jizzax_tumanlari = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax.items():
    jizzax_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=jizzax_callback.new(item_name=value)))


jizzax_y = {
"Jizzax shahar" :"jizzax shahar",
"Arnasoy" :"arnasoy tumani",
"Baxmal" :"baxmal tumani",
"Doʻstlik" :"do'stlik tumani",
"Forish" :"forish tumani",
"Gʻallaorol" :"g'allarol tumani",
"Sharof Rashidov ":"sharof rashidov tumani",
'Mirzachoʻl' :'mirzachol tumani',
"Paxtakor" :"paxtakor tumani",
"Yangiobod" :"yangi obod tumani",
'Zomin' :"zomin tumani",
'Zafarobod' :"zafarobod tumani",
'Zarbdor' :"zarbdor tumani",

}
jizzax_yol = InlineKeyboardMarkup(row_width=2)
for key, value in jizzax_y.items():
    jizzax_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

jizzax_yx = {
"Arnasoy" :"x_arnasoy",
"Baxmal" :"x_baxmal",
"Doʻstlik" :"x_do'stlik",
"Forish" :"x_forish",
"Gʻallaorol" :"x_g'allarol",
"Sharof Rashidov ":"x_sharof rashidov",
'Mirzachoʻl' :'x_mirzachol',
"Paxtakor" :"x_paxtakor",
"Yangiobod" :"x_yangi obod",
'Zomin' :"x_zomin",
'Zafarobod' :"x_zafarobod",
'Zarbdor' :"x_zarbdor",

}
jizzax_x = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_yx.items():
    jizzax_x.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



jizzax_yxaa = {
"Arnasoy" :"poch_arnasoy",
"Baxmal" :"poch_baxmal",
"Doʻstlik" :"poch_do'stlik",
"Forish" :"poch_forish",
"Gʻallaorol" :"poch_g'allarol",
"Sharof Rashidov ":"poch_sharof rashidov",
'Mirzachoʻl' :'poch_mirzachol',
"Paxtakor" :"poch_paxtakor",
"Yangiobod" :"poch_yangi obod",
'Zomin' :"poch_zomin",
'Zafarobod' :"poch_zafarobod",
'Zarbdor' :"poch_zarbdor",

}
jizzax_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_yxaa.items():
    jizzax_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_ydcsdas = {
"Arnasoy" :"yuuk_arnasoy",
"Baxmal" :"yuuk_baxmal",
"Doʻstlik" :"yuuk_do'stlik",
"Forish" :"yuuk_forish",
"Gʻallaorol" :"yuuk_g'allarol",
"Sharof Rashidov ":"yuuk_sharof rashidov",
'Mirzachoʻl' :'yuuk_mirzachol',
"Paxtakor" :"yuuk_paxtakor",
"Yangiobod" :"yuuk_yangi obod",
'Zomin' :"yuuk_zomin",
'Zafarobod' :"yuuk_zafarobod",
'Zarbdor' :"yuuk_zarbdor",

}
jizzax_yuukta = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_ydcsdas.items():
    jizzax_yuukta.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yuukta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_yuukta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_ydcsdas1 = {
"Arnasoy" :"mash_arnasoy",
"Baxmal" :"mash_baxmal",
"Doʻstlik" :"mash_do'stlik",
"Forish" :"mash_forish",
"Gʻallaorol" :"mash_g'allarol",
"Sharof Rashidov ":"mash_sharof rashidov",
'Mirzachoʻl' :'mash_mirzachol',
"Paxtakor" :"mash_paxtakor",
"Yangiobod" :"mash_yangi obod",
'Zomin' :"mash_zomin",
'Zafarobod' :"mash_zafarobod",
'Zarbdor' :"mash_zarbdor",

}
jizzax_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_ydcsdas1.items():
    jizzax_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



izzax_pov = {
    "Arnasoy" :"arnasoy",
    "Baxmal" :"baxmal",
    "Doʻstlik" :"do'stlik",
    "Forish" :"forish",
    "Gʻallaorol" :"g'allarol",
    "Sharof Rashidov":"sharof rashidov",
    'Mirzachoʻl' :'mirzachol',
    "Paxtakor" :"paxtakor",
    "Yangiobod" :"yangi obod",
    'Zomin' :"zomin",
    'Zafarobod' :"zafarobod",
    'Zarbdor' :"zarbdor",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}
jizzax_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key, value in izzax_pov.items():
    jizzax_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))
