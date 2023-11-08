from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import navoiy_callback

navoiy = {
"✅ Konimex" :"konimex",
"✅ Karmana" :"karmana",
"✅ Qiziltepa" :"qiziltepa",
"✅ Xatirchi" :"xatirchi",
"✅ Navbahor" :"navbahor",
"✅ Nurota" :"nurota",
"✅ Tomdi" :"tomdi",
"✅ Uchquduq" :"uchquduq"
}
navoiy_tumanlari = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy.items():
    navoiy_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=navoiy_callback.new(item_name=value)))

navoiy_y = {
"Konimex" :"konimex",
"Karmana" :"karmana",
"Qiziltepa" :"qiziltepa",
"Xatirchi" :"xatirchi",
"Navbahor" :"navbahor",
"Nurota" :"nurota",
"Tomdi" :"tomdi",
"Uchquduq" :"uchquduq",

}
navoiy_yol = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_y.items():
    navoiy_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_yx = {
"Konimex" :"x_konimex",
"Karmana" :"x_karmana",
"Qiziltepa" :"x_qiziltepa",
"Xatirchi" :"x_xatirchi",
"Navbahor" :"x_navbahor",
"Nurota" :"x_nurota",
"Tomdi" :"x_tomdi",
"Uchquduq" :"x_uchquduq",

}
navoiy_x = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_yx.items():
    navoiy_x.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_yzx = {
"Konimex" :"poch_konimex",
"Karmana" :"poch_karmana",
"Qiziltepa" :"poch_qiziltepa",
"Xatirchi" :"poch_xatirchi",
"Navbahor" :"poch_navbahor",
"Nurota" :"poch_nurota",
"Tomdi" :"poch_tomdi",
"Uchquduq" :"poch_uchquduq",

}
navoiy_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_yzx.items():
    navoiy_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

navoiy_yuk = {
"Konimex" :"yuuk_konimex",
"Karmana" :"yuuk_karmana",
"Qiziltepa" :"yuuk_qiziltepa",
"Xatirchi" :"yuuk_xatirchi",
"Navbahor" :"yuuk_navbahor",
"Nurota" :"yuuk_nurota",
"Tomdi" :"yuuk_tomdi",
"Uchquduq" :"yuuk_uchquduq",

}
navoiy_yuukta = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_yuk.items():
    navoiy_yuukta.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yuukta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_yuukta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_yuk1 = {
"Konimex" :"mash_konimex",
"Karmana" :"mash_karmana",
"Qiziltepa" :"mash_qiziltepa",
"Xatirchi" :"mash_xatirchi",
"Navbahor" :"mash_navbahor",
"Nurota" :"mash_nurota",
"Tomdi" :"mash_tomdi",
"Uchquduq" :"mash_uchquduq",

}
navoiy_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_yuk1.items():
    navoiy_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
