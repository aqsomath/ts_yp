from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import fargona_callback

fargona_t = {
"✅ Oltiariq":"olti",
"✅ Bagʻdod ":"bogdod",
"✅ Beshariq ":"beshariq",
"✅ Buvayda" :"buvayda",
"✅ Dangʻara" :"dangara",
"✅ Fargʻona" :"fargona",
"✅ Furqat" :"furqat",
"✅ Qoʻshtepa":"qoshtepa",
"✅ Quva" :"quva",
"✅ Rishton":"rishton",
"✅ Soʻx" :"sox",
"✅ Toshloq":"toshloq",
"✅ Oʻzbekiston":"ozbekiston",
"✅ Uchkoʻprik" :"uchkoprik",
"✅ Yozyovon" :"yozyovon",
}

fargona = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_t.items():
    fargona.insert(InlineKeyboardButton(text=key, callback_data=fargona_callback.new(item_name=value)))


fargona_y = {
"Fargʻona shaxar" :"farg'ona shahar",
"Fargʻona tuman" :"farg'ona tuman",
"Qo'qon shahar":"qo'qon shahar",
"Quvasoy shahar":"quvasoy shahar",
"Marg'ilon shahar":"marg'ilon shahar",
"Oltiariq":"oltiariq tuman",
"Bagʻdod ":"bog'dod tuman",
"Beshariq ":"beshariq tuman",
"Buvayda" :"buvayda tuman",
"Dangʻara" :"dangara tuman",
"Furqat" :"furqat tuman",
"Qoʻshtepa":"qo'shtepa tuman",
"Quva" :"quva tuman",
"Rishton":"rishton tuman",
"Soʻx" :"sox tuman",
"Toshloq":"toshloq tuman",
"Oʻzbekiston":"o'zbekiston tuman",
"Uchkoʻprik" :"uchko'prik tuman",
"Yozyovon" :"yozyovon tuman",

}

fargona_yol = InlineKeyboardMarkup(row_width=2)
for key, value in fargona_y.items():
    fargona_yol.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



fargona_xaa = {
"Oltiariq":"x_oltiariq",
"Bagʻdod ":"x_bog'dod",
"Beshariq ":"x_beshariq",
"Buvayda" :"x_buvayda",
"Dangʻara" :"x_dangara",
"Fargʻona" :"x_fergana ",
"Furqat" :"x_furqat",
"Qoʻshtepa":"x_qo'shtepa",
"Quva" :"x_quva",
"Rishton":"x_rishton",
"Soʻx" :"x_sox",
"Toshloq":"x_toshloq",
"Oʻzbekiston":"x_o'zbekiston",
"Uchkoʻprik" :"x_uchko'prik",
"Yozyovon" :"x_yozyovon",

}

fargona_x = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_xaa.items():
    fargona_x.insert(InlineKeyboardButton(text=key, callback_data=value))
    
fargona_asas = {
"Oltiariq":"poch_oltiariq",
"Bagʻdod ":"poch_bog'dod",
"Beshariq ":"poch_beshariq",
"Buvayda" :"poch_buvayda",
"Dangʻara" :"poch_dangara",
"Fargʻona" :"poch_fergana ",
"Furqat" :"poch_furqat",
"Qoʻshtepa":"poch_qo'shtepa",
"Quva" :"poch_quva",
"Rishton":"poch_rishton",
"Soʻx" :"poch_sox",
"Toshloq":"poch_toshloq",
"Oʻzbekiston":"poch_o'zbekiston",
"Uchkoʻprik" :"poch_uchko'prik",
"Yozyovon" :"poch_yozyovon",

}

fargona_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_asas.items():
    fargona_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))



fargona_assas = {
"Oltiariq":"yuuk_oltiariq",
"Bagʻdod ":"yuuk_bog'dod",
"Beshariq ":"yuuk_beshariq",
"Buvayda" :"yuuk_buvayda",
"Dangʻara" :"yuuk_dangara",
"Fargʻona" :"yuuk_fergana ",
"Furqat" :"yuuk_furqat",
"Qoʻshtepa":"yuuk_qo'shtepa",
"Quva" :"yuuk_quva",
"Rishton":"yuuk_rishton",
"Soʻx" :"yuuk_sox",
"Toshloq":"yuuk_toshloq",
"Oʻzbekiston":"yuuk_o'zbekiston",
"Uchkoʻprik" :"yuuk_uchko'prik",
"Yozyovon" :"yuuk_yozyovon",

}

fargona_yuuk = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_assas.items():
    fargona_yuuk.insert(InlineKeyboardButton(text=key, callback_data=value))
    
fargona_yuk_mashina = {
"Oltiariq":"mash_oltiariq",
"Bagʻdod ":"mash_bog'dod",
"Beshariq ":"mash_beshariq",
"Buvayda" :"mash_buvayda",
"Dangʻara" :"mash_dangara",
"Fargʻona" :"mash_fergana ",
"Furqat" :"mash_furqat",
"Qoʻshtepa":"mash_qo'shtepa",
"Quva" :"mash_quva",
"Rishton":"mash_rishton",
"Soʻx" :"mash_sox",
"Toshloq":"mash_toshloq",
"Oʻzbekiston":"mash_o'zbekiston",
"Uchkoʻprik" :"mash_uchko'prik",
"Yozyovon" :"mash_yozyovon",

}

fargona_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_yuk_mashina.items():
    fargona_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
    

fargona_sdjht = {
    "Oltiariq":"oltiariq",
    "Bagʻdod ":"bog'dod",
    "Beshariq ":"beshariq",
    "Buvayda" :"buvayda",
    "Dangʻara" :"dangara",
    "Fargʻona" :"fergana",
    "Furqat" :"furqat",
    "Qoʻshtepa":"qo'shtepa",
    "Quva" :"quva",
    "Rishton":"rishton",
    "Soʻx" :"sox",
    "Toshloq":"toshloq",
    "Oʻzbekiston":"o'zbekiston",
    "Uchkoʻprik" :"uchko'prik",
    "Yozyovon" :"yozyovon",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",
}

fargona_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_sdjht.items():
    fargona_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))

