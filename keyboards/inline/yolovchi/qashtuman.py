from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import qashqadaryo_callback

qashqadaryo = {
"✅ Dehqonobod":"dehqonobod",
"✅ Kasbi":"kasbi",
"✅ Kitob":"kitob",
"✅ Koson":"koson",
"✅ Koʻkdala":"kokdala",
"✅ Mirishkor":"mirishkor",
"✅ Muborak":"muborak",
"✅ Nishon":"nishon",
"✅ Qamashi":"qamashi" ,
"✅ Qarshi":"qarshi",
"✅ Yakkabogʻ" :"yakkabog",
"✅ Gʻuzor":"guzor",
"✅ Shahrisabz":"shahrisabz",
"✅ Chiroqchi":"chiroqchi"
}
qashqadaryo_tumanlari = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo.items():
    qashqadaryo_tumanlari.insert(InlineKeyboardButton(text=key, callback_data=qashqadaryo_callback.new(item_name=value)))


qashqadaryo_y = {
"Dehqonobod":"dehqonobod",
"Kasbi":"kasbi",
"Kitob":"kitob",
"Koson":"koson",
"Koʻkdala":"kokdala",
"Mirishkor":"mirishkor",
"Muborak":"muborak",
"Nishon":"nishon",
"Qamashi":"qamashi" ,
"Qarshi":"qarshi",
"Yakkabogʻ" :"yakkabog",
"Gʻuzor":"guzor",
"Shahrisabz":"shahrisabz",
"Chiroqchi":"chiroqchi",

}
qashqadaryo_yol = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_y.items():
    qashqadaryo_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


qashqadaryo_yx = {
"Dehqonobod":"x_dehqonobod",
"Kasbi":"x_kasbi",
"Kitob":"x_kitob",
"Koson":"x_koson",
"Koʻkdala":"x_kokdala",
"Mirishkor":"x_mirishkor",
"Muborak":"x_muborak",
"Nishon":"x_nishon",
"Qamashi":"x_qamashi" ,
"Qarshi":"x_qarshi",
"Yakkabogʻ" :"x_yakkabog",
"Gʻuzor":"x_guzor",
"Shahrisabz":"x_shahrisabz",
"Chiroqchi":"x_chiroqchi",

}
qashqadaryo_x = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_yx.items():
    qashqadaryo_x.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


qashqadaryo_yax = {
"Dehqonobod":"poch_dehqonobod",
"Kasbi":"poch_kasbi",
"Kitob":"poch_kitob",
"Koson":"poch_koson",
"Koʻkdala":"poch_kokdala",
"Mirishkor":"poch_mirishkor",
"Muborak":"poch_muborak",
"Nishon":"poch_nishon",
"Qamashi":"poch_qamashi" ,
"Qarshi":"poch_qarshi",
"Yakkabogʻ" :"poch_yakkabog",
"Gʻuzor":"poch_guzor",
"Shahrisabz":"poch_shahrisabz",
"Chiroqchi":"poch_chiroqchi",

}
qashqadaryo_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_yax.items():
    qashqadaryo_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


qashqadaryo_yuk = {
"Dehqonobod":"yuuk_dehqonobod",
"Kasbi":"yuuk_kasbi",
"Kitob":"yuuk_kitob",
"Koson":"yuuk_koson",
"Koʻkdala":"yuuk_kokdala",
"Mirishkor":"yuuk_mirishkor",
"Muborak":"yuuk_muborak",
"Nishon":"yuuk_nishon",
"Qamashi":"yuuk_qamashi" ,
"Qarshi":"yuuk_qarshi",
"Yakkabogʻ" :"yuuk_yakkabog",
"Gʻuzor":"yuuk_guzor",
"Shahrisabz":"yuuk_shahrisabz",
"Chiroqchi":"yuuk_chiroqchi",

}
qashqadaryo_yuuk = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_yuk.items():
    qashqadaryo_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



qashqadaryo_yuk1 = {
"Dehqonobod":"mash_dehqonobod",
"Kasbi":"mash_kasbi",
"Kitob":"mash_kitob",
"Koson":"mash_koson",
"Koʻkdala":"mash_kokdala",
"Mirishkor":"mash_mirishkor",
"Muborak":"mash_muborak",
"Nishon":"mash_nishon",
"Qamashi":"mash_qamashi" ,
"Qarshi":"mash_qarshi",
"Yakkabogʻ" :"mash_yakkabog",
"Gʻuzor":"mash_guzor",
"Shahrisabz":"mash_shahrisabz",
"Chiroqchi":"mash_chiroqchi",

}
qashqadaryo_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_yuk1.items():
    qashqadaryo_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
