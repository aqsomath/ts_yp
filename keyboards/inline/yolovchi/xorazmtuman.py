from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import xorazm_callback

xorazm_tumanlari = InlineKeyboardMarkup(row_width=4)
xorazm = {
"✅ Bogʻot" :"bogot",
"✅ Gurlan" :"gurlan",
"✅ Xonqa" :"xonqa",
"✅ Hazorasp" :"hazorasp",
"✅ Xiva" :"xiva",
"✅ Qoʻshkoʻpir" :"qoshkoprik",
"✅ Shovot" :"shovot",
"✅ Urganch" :"urganch",
"✅ Yangiariq" :"yangiariq",
"✅ Yangibozor" :"yangibozor",
"✅ Tupproqqalʼa" :"tuproqqala"
}
for key,value in xorazm.items():
    xorazm_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=xorazm_callback.new(item_name=value)))


xorazm_yol = InlineKeyboardMarkup(row_width=4)
xorazm_y = {
"Bogʻot" :"bog'ot",
"Gurlan" :"gurlan",
"Xonqa" :"xonqa",
"Hazorasp" :"hazorasp",
"Xiva" :"xiva",
"Qoʻshkoʻpir" :"qoshko'prik",
"Shovot" :"shovot",
"Urganch" :"urganch",
"Yangiariq" :"yangiariq",
"Yangibozor" :"yangibozor",
"Tupproqqalʼa" :"tuproqqal'a",

}
for key,value in xorazm_y.items():
    xorazm_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

xorazm_x = InlineKeyboardMarkup(row_width=4)
xorazm_yx = {
"Bogʻot" :"x_bog'ot",
"Gurlan" :"x_gurlan",
"Xonqa" :"x_xonqa",
"Hazorasp" :"x_hazorasp",
"Xiva" :"x_xiva",
"Qoʻshkoʻpir" :"x_qoshko'prik",
"Shovot" :"x_shovot",
"Urganch" :"x_urganch",
"Yangiariq" :"x_yangiariq",
"Yangibozor" :"x_yangibozor",
"Tupproqqalʼa" :"x_tuproqqal'a",

}
for key,value in xorazm_yx.items():
    xorazm_x.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

xorazm_pochta = InlineKeyboardMarkup(row_width=4)
xorazm_yzzx = {
"Bogʻot" :"poch_bog'ot",
"Gurlan" :"poch_gurlan",
"Xonqa" :"poch_xonqa",
"Hazorasp" :"poch_hazorasp",
"Xiva" :"poch_xiva",
"Qoʻshkoʻpir" :"poch_qoshko'prik",
"Shovot" :"poch_shovot",
"Urganch" :"poch_urganch",
"Yangiariq" :"poch_yangiariq",
"Yangibozor" :"poch_yangibozor",
"Tupproqqalʼa" :"poch_tuproqqal'a",

}
for key,value in xorazm_yzzx.items():
    xorazm_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



xorazm_yuuk= InlineKeyboardMarkup(row_width=4)
xorazm_yuk = {
"Bogʻot" :"yuuk_bog'ot",
"Gurlan" :"yuuk_gurlan",
"Xonqa" :"yuuk_xonqa",
"Hazorasp" :"yuuk_hazorasp",
"Xiva" :"yuuk_xiva",
"Qoʻshkoʻpir" :"yuuk_qoshko'prik",
"Shovot" :"yuuk_shovot",
"Urganch" :"yuuk_urganch",
"Yangiariq" :"yuuk_yangiariq",
"Yangibozor" :"yuuk_yangibozor",
"Tupproqqalʼa" :"yuuk_tuproqqal'a",

}
for key,value in xorazm_yuk.items():
    xorazm_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

xorazm_yuuk_mashina= InlineKeyboardMarkup(row_width=4)
xorazm_yuk1 = {
"Bogʻot" :"mash_bog'ot",
"Gurlan" :"mash_gurlan",
"Xonqa" :"mash_xonqa",
"Hazorasp" :"mash_hazorasp",
"Xiva" :"mash_xiva",
"Qoʻshkoʻpir" :"mash_qoshko'prik",
"Shovot" :"mash_shovot",
"Urganch" :"mash_urganch",
"Yangiariq" :"mash_yangiariq",
"Yangibozor" :"mash_yangibozor",
"Tupproqqalʼa" :"mash_tuproqqal'a",

}
for key,value in xorazm_yuk1.items():
    xorazm_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
