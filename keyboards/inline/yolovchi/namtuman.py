from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import namangan_callback

namangan_tumanlari = {
    "✅ Chortoq":"chortoq",
    "✅ Chust ":"chust",
    "✅ Kosonsoy ":"kosonsoy",
    "✅ Mingbuloq":"mingbuloq",
    "✅ Namangan ":"namangan shaxar",
    "✅ Norin":"norin",
    "✅ Pop ":"pop",
    "✅ To'raqo'rg'on":"toraqorgon",
    "✅ Uchqo'rg'on":"uchqorgon",
    "✅ Uychi":"uychi",
    "✅ Yangiqo'rg'on":"yangi qorgon",
    "✅ Davlatobod ":"davlatobod",
    "✅ Yangi Namangan":"yangi namangan"
}

namangan = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_tumanlari.items():
    namangan.insert(InlineKeyboardButton(text=key, callback_data=namangan_callback.new(item_name=value)))


namangan_y = {
    "Chortoq":"chortoq",
    "Chust ":"chust",
    "Kosonsoy ":"kosonsoy",
    "Mingbuloq":"mingbuloq",
    "Namangan ":"namangan shaxar",
    "Norin":"norin",
    "Pop ":"pop",
    "To'raqo'rg'on":"toraqo'rg'on",
    "Uchqo'rg'on":"uchqo'rgo'n",
    "Uychi":"uychi",
    "Yangiqo'rg'on":"yangi qo'rg'on",
    "Davlatobod ":"davlatobod",
    "Yangi Namangan":"yangi namangan",

}

namangan_yol = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_y.items():
    namangan_yol.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



namangan_xx = {
    "Chortoq":"x_chortoq",
    "Chust ":"x_chust",
    "Kosonsoy ":"x_kosonsoy",
    "Mingbuloq":"x_mingbuloq",
    "Namangan ":"x_namangan shaxar",
    "Norin":"x_norin",
    "Pop ":"x_pop",
    "To'raqo'rg'on":"x_toraqo'rg'on",
    "Uchqo'rg'on":"x_uchqo'rgo'n",
    "Uychi":"x_uychi",
    "Yangiqo'rg'on":"x_yangi qo'rg'on",
    "Davlatobod ":"x_davlatobod",
    "Yangi Namangan":"x_yangi namangan",

}

namangan_x = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_xx.items():
    namangan_x.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


namangan_x = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_xx.items():
    namangan_x.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


namangan_xxa = {
    "Chortoq":"poch_chortoq",
    "Chust ":"poch_chust",
    "Kosonsoy ":"poch_kosonsoy",
    "Mingbuloq":"poch_mingbuloq",
    "Namangan ":"poch_namangan shaxar",
    "Norin":"poch_norin",
    "Pop ":"poch_pop",
    "To'raqo'rg'on":"poch_toraqo'rg'on",
    "Uchqo'rg'on":"poch_uchqo'rgo'n",
    "Uychi":"poch_uychi",
    "Yangiqo'rg'on":"poch_yangi qo'rg'on",
    "Davlatobod ":"poch_davlatobod",
    "Yangi Namangan":"poch_yangi namangan",

}

namangan_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_xxa.items():
    namangan_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


namangan_axxa = {
    "Chortoq":"yuuk_chortoq",
    "Chust ":"yuuk_chust",
    "Kosonsoy ":"yuuk_kosonsoy",
    "Mingbuloq":"yuuk_mingbuloq",
    "Namangan ":"yuuk_namangan shaxar",
    "Norin":"yuuk_norin",
    "Pop ":"yuuk_pop",
    "To'raqo'rg'on":"yuuk_toraqo'rg'on",
    "Uchqo'rg'on":"yuuk_uchqo'rgo'n",
    "Uychi":"yuuk_uychi",
    "Yangiqo'rg'on":"yuuk_yangi qo'rg'on",
    "Davlatobod ":"yuuk_davlatobod",
    "Yangi Namangan":"yuuk_yangi namangan",

}

namangan_yuuk = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_axxa.items():
    namangan_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


namangan_mashina = {
    "Chortoq":"mash_chortoq",
    "Chust ":"mash_chust",
    "Kosonsoy ":"mash_kosonsoy",
    "Mingbuloq":"mash_mingbuloq",
    "Namangan ":"mash_namangan shaxar",
    "Norin":"mash_norin",
    "Pop ":"mash_pop",
    "To'raqo'rg'on":"mash_toraqo'rg'on",
    "Uchqo'rg'on":"mash_uchqo'rgo'n",
    "Uychi":"mash_uychi",
    "Yangiqo'rg'on":"mash_yangi qo'rg'on",
    "Davlatobod ":"mash_davlatobod",
    "Yangi Namangan":"mash_yangi namangan",

}

namangan_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_mashina.items():
    namangan_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))