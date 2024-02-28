from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import sirdaryo_callback

sirdaryo = {
"✅ Oqoltin" :"oqoltin",
"✅ Boyovut" :"boyovut" ,
"✅ Guliston" :"guliston",
"✅ Xovos" : "xovos",
"✅ Mirzaobod" : "mirzaobod",
"✅ Sardoba" :"sardoba",
"✅ Sayxunobod" :"sayxunobod",
"✅ Sirdaryo" :"sirdaryo shaxri"
}


sirdaryo_viloyati_tumanlari = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo.items():
    sirdaryo_viloyati_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=sirdaryo_callback.new(item_name=value)))


sirdaryo_y = {
"Sirdaryo shahar" :"sirdaryo shahar",
"Sirdaryo tuman" :"sirdaryo tumani",
"Guliston shahar" :"guliston shahar",
"Yangiyer shahar" :"yangiyer shahar",
"Shirin shahar" :"shirin shahar",
"Oqoltin" :"oqoltin tumani",
"Boyovut" :"boyovut tumani" ,
"Guliston" :"guliston tumani",
"Xovos" : "xovos tumani",
"Mirzaobod" : "mirzaobod tumani",
"Sardoba" :"sardoba tumani",
"Sayxunobod" :"sayxunobod tumani",

}


sirdaryo_yol = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y.items():
    sirdaryo_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


sirdaryo_yx = {
"Oqoltin" :"x_oqoltin",
"Boyovut" :"x_boyovut" ,
"Guliston" :"x_guliston",
"Xovos" : "x_xovos",
"Mirzaobod" : "x_mirzaobod",
"Sardoba" :"x_sardoba",
"Sayxunobod" :"x_sayxunobod",
"Sirdaryo shaxar" :"x_sirdaryo shaxri",

}


sirdaryo_x = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_yx.items():
    sirdaryo_x.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

sirdaryo_yax = {
"Oqoltin" :"poch_oqoltin",
"Boyovut" :"poch_boyovut" ,
"Guliston" :"poch_guliston",
"Xovos" : "poch_xovos",
"Mirzaobod" : "poch_mirzaobod",
"Sardoba" :"poch_sardoba",
"Sayxunobod" :"poch_sayxunobod",
"Sirdaryo" :"poch_sirdaryo shaxri",

}


sirdaryo_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_yax.items():
    sirdaryo_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y1ax = {
"Oqoltin" :"yuuk_oqoltin",
"Boyovut" :"yuuk_boyovut" ,
"Guliston" :"yuuk_guliston",
"Xovos" : "yuuk_xovos",
"Mirzaobod" : "yuuk_mirzaobod",
"Sardoba" :"yuuk_sardoba",
"Sayxunobod" :"yuuk_sayxunobod",
"Sirdaryo" :"yuuk_sirdaryo shaxri",

}


sirdaryo_yuuk = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y1ax.items():
    sirdaryo_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y1ax1 = {
"Oqoltin" :"mash_oqoltin",
"Boyovut" :"mash_boyovut" ,
"Guliston" :"mash_guliston",
"Xovos" : "mash_xovos",
"Mirzaobod" : "mash_mirzaobod",
"Sardoba" :"mash_sardoba",
"Sayxunobod" :"mash_sayxunobod",
"Sirdaryo" :"mash_sirdaryo shaxri",

}


sirdaryo_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y1ax1.items():
    sirdaryo_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


sirdaryo_pochta_uchun_1 = {
    "Oqoltin" :"oqoltin",
    "Boyovut" :"boyovut" ,
    "Guliston" :"guliston",
    "Xovos" : "xovos",
    "Mirzaobod" : "mirzaobod",
    "Sardoba" :"sardoba",
    "Sayxunobod" :"sayxunobod",
    "Sirdaryo" :"sirdaryo shaxri",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}


sirdaryo_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_pochta_uchun_1.items():
    sirdaryo_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))

