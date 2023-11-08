from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import toshkent_callback

toshkent = {
    "✅ Bekobod":"bekobod",
    "✅ Boʻstonliq":"bostonliq",
    "✅ Boʻka":"boka",
    "✅ Chinoz":"chinoz",
    "✅ Qibray":"qibray",
    "✅ Ohangaron":"ohangaron",
    "✅ Oqqoʻrgʻon":"oqqorgon",
    "✅ Parkent":"parkent",
    "✅ Piskent":"piskent",
    "✅ Quyi Chirchiq":"quyichirchiq",
    "✅ Oʻrta Chirchiq":"ortachirchiq",
    "✅ Yangiyoʻl":"yangiyol",
    "✅ Yuqori Chirchiq":"yuqorichirchiq",
    "✅ Zangiota":"zangiota"
}

toshkent_viloyati_tumanlari = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent.items():
    toshkent_viloyati_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=toshkent_callback.new(item_name=value)))


toshkent_y = {
    "Bekobod":"bekobod",
    "Boʻstonliq":"bostonliq",
    "Boʻka":"boka",
    "Chinoz":"chinoz",
    "Qibray":"qibray",
    "Ohangaron":"ohangaron",
    "Oqqoʻrgʻon":"oqqorgon",
    "Parkent":"parkent",
    "Piskent":"piskent",
    "Quyi Chirchiq":"quyichirchiq",
    "Oʻrta Chirchiq":"ortachirchiq",
    "Yangiyoʻl":"yangiyol",
    "Yuqori Chirchiq":"yuqorichirchiq",
    "Zangiota":"zangiota",

}

toshkent_yol = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_y.items():
    toshkent_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))





toshkent_yz = {
    "Bekobod":"x_bekobod",
    "Boʻstonliq":"x_bostonliq",
    "Boʻka":"x_boka",
    "Chinoz":"x_chinoz",
    "Qibray":"x_qibray",
    "Ohangaron":"x_ohangaron",
    "Oqqoʻrgʻon":"x_oqqorgon",
    "Parkent":"x_parkent",
    "Piskent":"x_piskent",
    "Quyi Chirchiq":"x_quyichirchiq",
    "Oʻrta Chirchiq":"x_ortachirchiq",
    "Yangiyoʻl":"x_yangiyol",
    "Yuqori Chirchiq":"x_yuqorichirchiq",
    "Zangiota":"x_zangiota",

}

toshkent_x = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_yz.items():
    toshkent_x.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


toshkent_yaz = {
    "Bekobod":"poch_bekobod",
    "Boʻstonliq":"poch_bostonliq",
    "Boʻka":"poch_boka",
    "Chinoz":"poch_chinoz",
    "Qibray":"poch_qibray",
    "Ohangaron":"poch_ohangaron",
    "Oqqoʻrgʻon":"poch_oqqorgon",
    "Parkent":"poch_parkent",
    "Piskent":"poch_piskent",
    "Quyi Chirchiq":"poch_quyichirchiq",
    "Oʻrta Chirchiq":"poch_ortachirchiq",
    "Yangiyoʻl":"poch_yangiyol",
    "Yuqori Chirchiq":"poch_yuqorichirchiq",
    "Zangiota":"poch_zangiota",

}

toshkent_pochta= InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_yaz.items():
    toshkent_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


toshkent_yaz1 = {
    "Bekobod":"yuuk_bekobod",
    "Boʻstonliq":"yuuk_bostonliq",
    "Boʻka":"yuuk_boka",
    "Chinoz":"yuuk_chinoz",
    "Qibray":"yuuk_qibray",
    "Ohangaron":"yuuk_ohangaron",
    "Oqqoʻrgʻon":"yuuk_oqqorgon",
    "Parkent":"yuuk_parkent",
    "Piskent":"yuuk_piskent",
    "Quyi Chirchiq":"yuuk_quyichirchiq",
    "Oʻrta Chirchiq":"yuuk_ortachirchiq",
    "Yangiyoʻl":"yuuk_yangiyol",
    "Yuqori Chirchiq":"yuuk_yuqorichirchiq",
    "Zangiota":"yuuk_zangiota",

}

toshkent_yuuk= InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_yaz1.items():
    toshkent_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


toshkent_yaz12 = {
    "Bekobod":"mash_bekobod",
    "Boʻstonliq":"mash_bostonliq",
    "Boʻka":"mash_boka",
    "Chinoz":"mash_chinoz",
    "Qibray":"mash_qibray",
    "Ohangaron":"mash_ohangaron",
    "Oqqoʻrgʻon":"mash_oqqorgon",
    "Parkent":"mash_parkent",
    "Piskent":"mash_piskent",
    "Quyi Chirchiq":"mash_quyichirchiq",
    "Oʻrta Chirchiq":"mash_ortachirchiq",
    "Yangiyoʻl":"mash_yangiyol",
    "Yuqori Chirchiq":"mash_yuqorichirchiq",
    "Zangiota":"mash_zangiota",

}

toshkent_yuuk_mashina= InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_yaz12.items():
    toshkent_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))