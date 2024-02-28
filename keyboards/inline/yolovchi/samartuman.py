from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import samarqand_callback

samarqaand = {
'✅ Bulungʻur' :"bulungur",
'✅ Ishtixon' :"ishtixon",
'✅ Jomboy' :"jomboy",
'✅ Kattaqoʻrgʻon' :"kattaqorgon",
'✅ Qoʻshrabot' :"qoshrabot",
'✅ Narpay' :"narpay",
'✅ Nurobod' :"nurobodoo",
'✅ Oqdaryo' :"oqdaryo",
'✅ Paxtachi' :"paxtachi",
'✅ Payariq' :"payariq",
'✅ Pastdargʻom' :"pastdargom",
'✅ Samarqand' :"samarqand shahar",
'✅ Toyloq' :"toyloq"

}
samarqaand_tumalari = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand.items():
    samarqaand_tumalari.insert(InlineKeyboardButton(text=key, callback_data=samarqand_callback.new(item_name=value)))


samarqaand_y = {
'Samarqand shaxar' :"samarqand shahar",
'Kattaqoʻrgʻon shahar' :"kattaqorgon shahar",
'Bulungʻur' :"bulungur tumani",
'Ishtixon' :"ishtixon tumani",
'Jomboy' :"jomboy tumani",
'Kattaqoʻrgʻon tuman' :"kattaqorgon tumani",
'Qoʻshrabot' :"qoshrabot tumani",
'Narpay' :"narpay tumani",
'Nurobod' :"nurobod tumani",
'Oqdaryo' :"oqdaryo tumani",
'Paxtachi' :"paxtachi tumani",
'Payariq' :"payariq tumani",
'Pastdargʻom' :"pastdargom tumani",
'Samarqand tuman' :"samarqand tumani",
'Toyloq' :"toyloq tumani",

}
samarqand_yol = InlineKeyboardMarkup(row_width=2)
for key, value in samarqaand_y.items():
    samarqand_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



samarqaand_yx = {
'Bulungʻur' :"x_bulungur",
'Ishtixon' :"x_ishtixon",
'Jomboy' :"x_jomboy",
'Kattaqoʻrgʻon' :"x_kattaqorgon",
'Qoʻshrabot' :"x_qoshrabot",
'Narpay' :"x_narpay",
'Nurobod' :"x_nurobod",
'Oqdaryo' :"x_oqdaryo",
'Paxtachi' :"x_paxtachi",
'Payariq' :"x_payariq",
'Pastdargʻom' :"x_pastdargom",
'Samarqand' :"x_samarqand shahar",
'Toyloq' :"x_toyloq",

}
samarqand_x = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yx.items():
    samarqand_x.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_x.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_x.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_yaax = {
'Bulungʻur' :"poch_bulungur",
'Ishtixon' :"poch_ishtixon",
'Jomboy' :"poch_jomboy",
'Kattaqoʻrgʻon' :"poch_kattaqorgon",
'Qoʻshrabot' :"poch_qoshrabot",
'Narpay' :"poch_narpay",
'Nurobod' :"poch_nurobod",
'Oqdaryo' :"poch_oqdaryo",
'Paxtachi' :"poch_paxtachi",
'Payariq' :"poch_payariq",
'Pastdargʻom' :"poch_pastdargom",
'Samarqand' :"poch_samarqand shahar",
'Toyloq' :"poch_toyloq",

}
samarqand_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yaax.items():
    samarqand_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_yasasa = {
'Bulungʻur' :"yuuk_bulungur",
'Ishtixon' :"yuuk_ishtixon",
'Jomboy' :"yuuk_jomboy",
'Kattaqoʻrgʻon' :"yuuk_kattaqorgon",
'Qoʻshrabot' :"yuuk_qoshrabot",
'Narpay' :"yuuk_narpay",
'Nurobod' :"yuuk_nurobod",
'Oqdaryo' :"yuuk_oqdaryo",
'Paxtachi' :"yuuk_paxtachi",
'Payariq' :"yuuk_payariq",
'Pastdargʻom' :"yuuk_pastdargom",
'Samarqand' :"yuuk_samarqand shahar",
'Toyloq' :"yuuk_toyloq",

}
samarqand_yuukta = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yasasa.items():
    samarqand_yuukta.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yuukta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_yuukta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_yasasa1 = {
'Bulungʻur' :"mash_bulungur",
'Ishtixon' :"mash_ishtixon",
'Jomboy' :"mash_jomboy",
'Kattaqoʻrgʻon' :"mash_kattaqorgon",
'Qoʻshrabot' :"mash_qoshrabot",
'Narpay' :"mash_narpay",
'Nurobod' :"mash_nurobod",
'Oqdaryo' :"mash_oqdaryo",
'Paxtachi' :"mash_paxtachi",
'Payariq' :"mash_payariq",
'Pastdargʻom' :"mash_pastdargom",
'Samarqand' :"mash_samarqand shahar",
'Toyloq' :"mash_toyloq",

}
samarqand_yuuk_mashina = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yasasa1.items():
    samarqand_yuuk_mashina.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yuuk_mashina.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_yuuk_mashina.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




samarqaand_sd = {
    'Bulungʻur' :"bulungur",
    'Ishtixon' :"ishtixon",
    'Jomboy' :"jomboy",
    'Kattaqoʻrgʻon' :"kattaqorgon",
    'Qoʻshrabot' :"qoshrabot",
    'Narpay' :"narpay",
    'Nurobod' :"nurobod",
    'Oqdaryo' :"oqdaryo",
    'Paxtachi' :"paxtachi",
    'Payariq' :"payariq",
    'Pastdargʻom' :"pastdargom",
    'Samarqand' :"samarqand shahar",
    'Toyloq' :"toyloq",
    "Boshqa viloyat": "boshqaviloyat",

    "Bosh menu": "glavmenu",
    "Ortga": "qaytamiz",

}
samarqaand_pochta_uchun = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_sd.items():
    samarqaand_pochta_uchun.insert(InlineKeyboardButton(text=key, callback_data=value))
