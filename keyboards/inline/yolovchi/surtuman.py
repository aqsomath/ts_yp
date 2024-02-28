from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import surxon_callback

surxondaryo = {
"✅ Angor":"angor",
"✅ Bandixon":"bandixon",
"✅ Boysun":"boysun",
"✅ Denov" :"denov",
"✅ Jarqoʻrgʻon":"jarqorgon",
"✅ Qiziriq":"qiziriq",
"✅ Qumqoʻrgʻon":"qumqorgon",
"✅ Muzrabod":"muzrabod",
"✅ Oltinsoy":"oltinsoy",
"✅ Sariosiyo":"sariosiyo",
"✅ Sherobod":"sherobod",
"✅ Shoʻrchi":"shorchi" ,
"✅ Termiz":"termiz",
"✅ Uzun":"uzun"
}
surxondaryo_tuman = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo.items():
    surxondaryo_tuman.insert(InlineKeyboardButton(text=key, callback_data=surxon_callback.new(item_name=value)))

surxondaryo_y = {
"Termiz shahar":"termiz shahar",
"Termiz tuman":"termiz tumani",
"Angor":"angor tumani",
"Bandixon":"bandixon tumani",
"Boysun":"boysun tumani",
"Denov" :"denov tumani",
"Jarqoʻrgʻon":"jarqorgon tumani",
"Qiziriq":"qiziriq tumani",
"Qumqoʻrgʻon":"qumqorgon tumani",
"Muzrabod":"muzrabod tumani",
"Oltinsoy":"oltinsoy tumani",
"Sariosiyo":"sariosiyo tumani",
"Sherobod":"sherobod tumani",
"Shoʻrchi":"shorchi tumani" ,
"Uzun":"uzun tumani",

}
surxondaryo_yol = InlineKeyboardMarkup(row_width=2)
for key,value in surxondaryo_y.items():
    surxondaryo_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




surxondaryo_yx = {
"Angor":"x_angor",
"Bandixon":"x_bandixon",
"Boysun":"x_boysun",
"Denov" :"x_denov",
"Jarqoʻrgʻon":"x_jarqorgon",
"Qiziriq":"x_qiziriq",
"Qumqoʻrgʻon":"x_qumqorgon",
"Muzrabod":"x_muzrabod",
"Oltinsoy":"x_oltinsoy",
"Sariosiyo":"x_sariosiyo",
"Sherobod":"x_sherobod",
"Shoʻrchi":"x_shorchi" ,
"Termiz":"x_termiz",
"Uzun":"x_uzun",

}
surxondaryo_x = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yx.items():
    surxondaryo_x.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_yax = {
"Angor":"poch_angor",
"Bandixon":"poch_bandixon",
"Boysun":"poch_boysun",
"Denov" :"poch_denov",
"Jarqoʻrgʻon":"poch_jarqorgon",
"Qiziriq":"poch_qiziriq",
"Qumqoʻrgʻon":"poch_qumqorgon",
"Muzrabod":"poch_muzrabod",
"Oltinsoy":"poch_oltinsoy",
"Sariosiyo":"poch_sariosiyo",
"Sherobod":"poch_sherobod",
"Shoʻrchi":"poch_shorchi" ,
"Termiz":"poch_termiz",
"Uzun":"poch_uzun",

}
surxondaryo_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yax.items():
    surxondaryo_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


surxondaryo_yuk = {
"Angor":"yuuk_angor",
"Bandixon":"yuuk_bandixon",
"Boysun":"yuuk_boysun",
"Denov" :"yuuk_denov",
"Jarqoʻrgʻon":"yuuk_jarqorgon",
"Qiziriq":"yuuk_qiziriq",
"Qumqoʻrgʻon":"yuuk_qumqorgon",
"Muzrabod":"yuuk_muzrabod",
"Oltinsoy":"yuuk_oltinsoy",
"Sariosiyo":"yuuk_sariosiyo",
"Sherobod":"yuuk_sherobod",
"Shoʻrchi":"yuuk_shorchi" ,
"Termiz":"yuuk_termiz",
"Uzun":"yuuk_uzun",

}
surxondaryo_yuuk = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yuk.items():
    surxondaryo_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yuuk.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_yuuk.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_yuk1 = {
"Angor":"mash_angor",
"Bandixon":"mash_bandixon",
"Boysun":"mash_boysun",
"Denov" :"mash_denov",
"Jarqoʻrgʻon":"mash_jarqorgon",
"Qiziriq":"mash_qiziriq",
"Qumqoʻrgʻon":"mash_qumqorgon",
"Muzrabod":"mash_muzrabod",
"Oltinsoy":"mash_oltinsoy",
"Sariosiyo":"mash_sariosiyo",
"Sherobod":"mash_sherobod",
"Shoʻrchi":"mash_shorchi" ,
"Termiz":"mash_termiz",
"Uzun":"mash_uzun",

}
surxondaryo_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yuk1.items():
    surxondaryo_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_PO = {
    "Angor":"angor",
    "Bandixon":"bandixon",
    "Boysun":"boysun",
    "Denov" :"denov",
    "Jarqoʻrgʻon":"jarqorgon",
    "Qiziriq":"qiziriq",
    "Qumqoʻrgʻon":"qumqorgon",
    "Muzrabod":"muzrabod",
    "Oltinsoy":"oltinsoy",
    "Sariosiyo":"sariosiyo",
    "Sherobod":"sherobod",
    "Shoʻrchi":"shorchi" ,
    "Termiz":"termiz",
    "Uzun":"uzun",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}
surxondaryo_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_PO.items():
    surxondaryo_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))
