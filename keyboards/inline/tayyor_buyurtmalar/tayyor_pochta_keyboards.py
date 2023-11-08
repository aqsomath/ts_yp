from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

an = {
    "Ulug'nor":"pochta_ulug'nor",
    "Andijon shahar":"pochta_andddshaxar",
    "Asaka":"pochta_asaka",
    "Baliqchi":"pochta_baliqchi",
    "Bo'ston ":"pochta_bo'ston",
    "Buloqbosh":"pochta_buloqboshi",
    "Izboskan":"pochta_izboskan",
    "Jalaquduq":"pochta_jalaquduq",
    "Xoʻjaobod":"pochta_xo'jabod",
    "Qoʻrgʻontepa":"pochta_qo'rg'ontepa",
    "Marhamat":"pochta_marhamat",
    "Oltinkoʻl":"pochta_oltinko'l",
    "Paxtaobod":"pochta_paxtaobod",
    "Shahrixon":"pochta_shaxrixon",
    "Xonabod":"pochta_xonabod",

}
tayyor_pochta_and = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    tayyor_pochta_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_pochta_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_pochta_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_y = {
"Olot" :"pochta_olot",
"Buxoro" :"pochta_buxshaxar",
"Gʻijduvon" :"pochta_gijduvon",
"Jondor" :"pochta_jondor",
"Kogon" :"pochta_kogon",
"Qorakoʻl" :"pochta_qorakol",
"Qorovulbozor" : "pochta_qorovulbozor",
"Peshku" :"pochta_peshku",
"Romitan" :"pochta_romitan",
"Shofirkon" :"pochta_shofirkon",
"Vobkent" :"pochta_vobkent",

}

buxoro_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_y.items():
    buxoro_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_y = {
"Oltiariq":"pochta_oltiariq",
"Bagʻdod ":"pochta_bog'dod",
"Beshariq ":"pochta_beshariq",
"Buvayda" :"pochta_buvayda",
"Dangʻara" :"pochta_dangara",
"Fargʻona" :"pochta_vodil",
"Furqat" :"pochta_furqat",
"Qoʻshtepa":"pochta_qoshtepa",
"Quva" :"pochta_quva",
"Rishton":"pochta_rishton",
"Soʻx" :"pochta_sox",
"Toshloq":"pochta_toshloq",
"Oʻzbekiston":"pochta_ozbekiston",
"Uchkoʻprik" :"pochta_uchkoprik",
"Yozyovon" :"pochta_yozyovon",

}

fargona_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_y.items():
    fargona_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_y = {
    "Chortoq":"pochta_chortoq",
    "Chust ":"pochta_chust",
    "Kosonsoy ":"pochta_kosonsoy",
    "Mingbuloq":"pochta_mingbuloq",
    "Namangan ":"pochta_namshaxar",
    "Norin":"pochta_norin",
    "Pop ":"pochta_pop",
    "To'raqo'rg'on":"pochta_toraqo'rg'on",
    "Uchqo'rg'on":"pochta_uchqo'rgo'n",
    "Uychi":"pochta_uychi",
    "Yangiqo'rg'on":"pochta_yangiqor",
    "Davlatobod ":"pochta_davlatobod",
    "Yangi Namangan":"pochta_yangi namangan",

}

namangan_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_y.items():
    namangan_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y = {
"Oqoltin" :"pochta_oqoltin",
"Boyovut" :"pochta_boyovut" ,
"Guliston" :"pochta_guliston",
"Xovos" : "pochta_xovos",
"Mirzaobod" : "pochta_mirzaobod",
"Sardoba" :"pochta_sardoba",
"Sayxunobod" :"pochta_sayxunobod",
"Sirdaryo" :"pochta_shaxri",

}


sirdaryo_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y.items():
    sirdaryo_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_y = {
"Angor":"pochta_angor",
"Bandixon":"pochta_bandixon",
"Boysun":"pochta_boysun",
"Denov" :"pochta_denov",
"Jarqoʻrgʻon":"pochta_jarqorgon",
"Qiziriq":"pochta_qiziriq",
"Qumqoʻrgʻon":"pochta_qumqorgon",
"Muzrabod":"pochta_muzrabod",
"Oltinsoy":"pochta_oltinsoy",
"Sariosiyo":"pochta_sariosiyo",
"Sherobod":"pochta_sherobod",
"Shoʻrchi":"pochta_shorchi" ,
"Termiz":"pochta_termiz",
"Uzun":"pochta_uzun",

}
surxondaryo_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_y.items():
    surxondaryo_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_y = {
"Dehqonobod":"pochta_dehqonobod",
"Kasbi":"pochta_kasbi",
"Kitob":"pochta_kitob",
"Koson":"pochta_koson",
"Koʻkdala":"pochta_kokdala",
"Mirishkor":"pochta_mirishkor",
"Muborak":"pochta_muborak",
"Nishon":"pochta_nishon",
"Qamashi":"pochta_qamashi" ,
"Qarshi":"pochta_qarshi",
"Yakkabogʻ" :"pochta_yakkabog",
"Gʻuzor":"pochta_guzor",
"Shahrisabz":"pochta_shahrisabz",
"Chiroqchi":"pochta_chiroqchi",

}
qashqadaryo_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_y.items():
    qashqadaryo_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
xorazm_y = {
"Bogʻot" :"pochta_bogot",
"Gurlan" :"pochta_gurlan",
"Xonqa" :"pochta_xonqa",
"Hazorasp" :"pochta_hazorasp",
"Xiva" :"pochta_xiva",
"Qoʻshkoʻpir" :"pochta_qoshkorik",
"Shovot" :"pochta_shovot",
"Urganch" :"pochta_urganch",
"Yangiariq" :"pochta_yangiariq",
"Yangibozor" :"pochta_yangibozor",
"Tupproqqalʼa" :"pochta_tuproqqala",

}
for key,value in xorazm_y.items():
    xorazm_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_y = {
'Bulungʻur' :"pochta_bulungur",
'Ishtixon' :"pochta_ishtixon",
'Jomboy' :"pochta_jomboy",
'Kattaqoʻrgʻon' :"pochta_kattaqorgon",
'Qoʻshrabot' :"pochta_qoshrabot",
'Narpay' :"pochta_narpay",
'Nurobod' :"pochta_nurobod",
'Oqdaryo' :"pochta_oqdaryo",
'Paxtachi' :"pochta_paxtachi",
'Payariq' :"pochta_payariq",
'Pastdargʻom' :"pochta_pastdargom",
'Samarqand' :"pochta_samashahar",
'Toyloq' :"pochta_toyloq",

}
samarqand_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_y.items():
    samarqand_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_y = {
"Konimex" :"pochta_konimex",
"Karmana" :"pochta_karmana",
"Qiziltepa" :"pochta_qiziltepa",
"Xatirchi" :"pochta_xatirchi",
"Navbahor" :"pochta_navbahor",
"Nurota" :"pochta_nurota",
"Tomdi" :"pochta_tomdi",
"Uchquduq" :"pochta_uchquduq",

}
navoiy_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_y.items():
    navoiy_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_y = {
"Arnasoy" :"pochta_arnasoy",
"Baxmal" :"pochta_baxmal",
"Doʻstlik" :"pochta_dostlik",
"Forish" :"pochta_forish",
"Gʻallaorol" :"pochta_gallarol",
"Sharof Rashidov ":"pochta_shrashidov",
'Mirzachoʻl' :'pochta_mirzachol',
"Paxtakor" :"pochta_paxtakor",
"Yangiobod" :"pochta_yangobod",
'Zomin' :"pochta_zomin",
'Zafarobod' :"pochta_zafarobod",
'Zarbdor' :"pochta_zarbdor",

}
jizzax_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_y.items():
    jizzax_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_y = {
    "Bekobod":"pochta_bekobod",
    "Boʻstonliq":"pochta_bostonliq",
    "Boʻka":"pochta_boka",
    "Chinoz":"pochta_chinoz",
    "Qibray":"pochta_qibray",
    "Ohangaron":"pochta_ohangaron",
    "Oqqoʻrgʻon":"pochta_oqqorgon",
    "Parkent":"pochta_parkent",
    "Piskent":"pochta_piskent",
    "Quyi Chirchiq":"pochta_quyichirchiq",
    "Oʻrta Chirchiq":"pochta_ortachirchiq",
    "Yangiyoʻl":"pochta_yangiyol",
    "Yuqori Chirchiq":"pochta_yuqorichirchiq",
    "Zangiota":"pochta_zangiota",

}

toshkent_tayyor_pochta = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_y.items():
    toshkent_tayyor_pochta.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_pochta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_pochta.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



an1 = {
    "Ulug'nor":"yukbor_ulug'nor",
    "Andijon shahar":"yukbor_andddshaxar",
    "Asaka":"yukbor_asaka",
    "Baliqchi":"yukbor_baliqchi",
    "Bo'ston ":"yukbor_bo'ston",
    "Buloqbosh":"yukbor_buloqboshi",
    "Izboskan":"yukbor_izboskan",
    "Jalaquduq":"yukbor_jalaquduq",
    "Xoʻjaobod":"yukbor_xo'jabod",
    "Qoʻrgʻontepa":"yukbor_qo'rg'ontepa",
    "Marhamat":"yukbor_marhamat",
    "Oltinkoʻl":"yukbor_oltinko'l",
    "Paxtaobod":"yukbor_paxtaobod",
    "Shahrixon":"yukbor_shaxrixon",
    "Xonabod":"yukbor_xonabod",

}
tayyor_yukbor_and = InlineKeyboardMarkup(row_width=3)
for key,value in an1.items():
    tayyor_yukbor_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_yukbor_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_yukbor_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_y1 = {
"Olot" :"yukbor_olot",
"Buxoro" :"yukbor_buxshaxar",
"Gʻijduvon" :"yukbor_gijduvon",
"Jondor" :"yukbor_jondor",
"Kogon" :"yukbor_kogon",
"Qorakoʻl" :"yukbor_qorakol",
"Qorovulbozor" : "yukbor_qorovulbozor",
"Peshku" :"yukbor_peshku",
"Romitan" :"yukbor_romitan",
"Shofirkon" :"yukbor_shofirkon",
"Vobkent" :"yukbor_vobkent",

}

buxoro_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_y1.items():
    buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_y1 = {
"Oltiariq":"yukbor_oltiariq",
"Bagʻdod ":"yukbor_bog'dod",
"Beshariq ":"yukbor_beshariq",
"Buvayda" :"yukbor_buvayda",
"Dangʻara" :"yukbor_dangara",
"Fargʻona" :"yukbor_vodil",
"Furqat" :"yukbor_furqat",
"Qoʻshtepa":"yukbor_qoshtepa",
"Quva" :"yukbor_quva",
"Rishton":"yukbor_rishton",
"Soʻx" :"yukbor_sox",
"Toshloq":"yukbor_toshloq",
"Oʻzbekiston":"yukbor_ozbekiston",
"Uchkoʻprik" :"yukbor_uchkoprik",
"Yozyovon" :"yukbor_yozyovon",

}

fargona_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_y1.items():
    fargona_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_y1 = {
    "Chortoq":"yukbor_chortoq",
    "Chust ":"yukbor_chust",
    "Kosonsoy ":"yukbor_kosonsoy",
    "Mingbuloq":"yukbor_mingbuloq",
    "Namangan ":"yukbor_namshaxar",
    "Norin":"yukbor_norin",
    "Pop ":"yukbor_pop",
    "To'raqo'rg'on":"yukbor_toraqo'rg'on",
    "Uchqo'rg'on":"yukbor_uchqo'rgo'n",
    "Uychi":"yukbor_uychi",
    "Yangiqo'rg'on":"yukbor_yangiqor",
    "Davlatobod ":"yukbor_davlatobod",
    "Yangi Namangan":"yukbor_yangi namangan",

}

namangan_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_y1.items():
    namangan_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y1 = {
"Oqoltin" :"yukbor_oqoltin",
"Boyovut" :"yukbor_boyovut" ,
"Guliston" :"yukbor_guliston",
"Xovos" : "yukbor_xovos",
"Mirzaobod" : "yukbor_mirzaobod",
"Sardoba" :"yukbor_sardoba",
"Sayxunobod" :"yukbor_sayxunobod",
"Sirdaryo" :"yukbor_shaxri",

}


sirdaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y1.items():
    sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_y1 = {
"Angor":"yukbor_angor",
"Bandixon":"yukbor_bandixon",
"Boysun":"yukbor_boysun",
"Denov" :"yukbor_denov",
"Jarqoʻrgʻon":"yukbor_jarqorgon",
"Qiziriq":"yukbor_qiziriq",
"Qumqoʻrgʻon":"yukbor_qumqorgon",
"Muzrabod":"yukbor_muzrabod",
"Oltinsoy":"yukbor_oltinsoy",
"Sariosiyo":"yukbor_sariosiyo",
"Sherobod":"yukbor_sherobod",
"Shoʻrchi":"yukbor_shorchi" ,
"Termiz":"yukbor_termiz",
"Uzun":"yukbor_uzun",

}
surxondaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_y1.items():
    surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_y1= {
"Dehqonobod":"yukbor_dehqonobod",
"Kasbi":"yukbor_kasbi",
"Kitob":"yukbor_kitob",
"Koson":"yukbor_koson",
"Koʻkdala":"yukbor_kokdala",
"Mirishkor":"yukbor_mirishkor",
"Muborak":"yukbor_muborak",
"Nishon":"yukbor_nishon",
"Qamashi":"yukbor_qamashi" ,
"Qarshi":"yukbor_qarshi",
"Yakkabogʻ" :"yukbor_yakkabog",
"Gʻuzor":"yukbor_guzor",
"Shahrisabz":"yukbor_shahrisabz",
"Chiroqchi":"yukbor_chiroqchi",

}
qashqadaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_y1.items():
    qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
xorazm_y1 = {
"Bogʻot" :"yukbor_bogot",
"Gurlan" :"yukbor_gurlan",
"Xonqa" :"yukbor_xonqa",
"Hazorasp" :"yukbor_hazorasp",
"Xiva" :"yukbor_xiva",
"Qoʻshkoʻpir" :"yukbor_qoshkorik",
"Shovot" :"yukbor_shovot",
"Urganch" :"yukbor_urganch",
"Yangiariq" :"yukbor_yangiariq",
"Yangibozor" :"yukbor_yangibozor",
"Tupproqqalʼa" :"yukbor_tuproqqala",

}
for key,value in xorazm_y1.items():
    xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_y1 = {
'Bulungʻur' :"yukbor_bulungur",
'Ishtixon' :"yukbor_ishtixon",
'Jomboy' :"yukbor_jomboy",
'Kattaqoʻrgʻon' :"yukbor_kattaqorgon",
'Qoʻshrabot' :"yukbor_qoshrabot",
'Narpay' :"yukbor_narpay",
'Nurobod' :"yukbor_nurobod",
'Oqdaryo' :"yukbor_oqdaryo",
'Paxtachi' :"yukbor_paxtachi",
'Payariq' :"yukbor_payariq",
'Pastdargʻom' :"yukbor_pastdargom",
'Samarqand' :"yukbor_samashahar",
'Toyloq' :"yukbor_toyloq",

}
samarqand_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_y1.items():
    samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_y1 = {
"Konimex" :"yukbor_konimex",
"Karmana" :"yukbor_karmana",
"Qiziltepa" :"yukbor_qiziltepa",
"Xatirchi" :"yukbor_xatirchi",
"Navbahor" :"yukbor_navbahor",
"Nurota" :"yukbor_nurota",
"Tomdi" :"yukbor_tomdi",
"Uchquduq" :"yukbor_uchquduq",

}
navoiy_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_y1.items():
    navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_y1 = {
"Arnasoy" :"yukbor_arnasoy",
"Baxmal" :"yukbor_baxmal",
"Doʻstlik" :"yukbor_dostlik",
"Forish" :"yukbor_forish",
"Gʻallaorol" :"yukbor_gallarol",
"Sharof Rashidov ":"yukbor_shrashidov",
'Mirzachoʻl' :'yukbor_mirzachol',
"Paxtakor" :"yukbor_paxtakor",
"Yangiobod" :"yukbor_yangobod",
'Zomin' :"yukbor_zomin",
'Zafarobod' :"yukbor_zafarobod",
'Zarbdor' :"yukbor_zarbdor",

}
jizzax_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_y1.items():
    jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_y1 = {
    "Bekobod":"yukbor_bekobod",
    "Boʻstonliq":"yukbor_bostonliq",
    "Boʻka":"yukbor_boka",
    "Chinoz":"yukbor_chinoz",
    "Qibray":"yukbor_qibray",
    "Ohangaron":"yukbor_ohangaron",
    "Oqqoʻrgʻon":"yukbor_oqqorgon",
    "Parkent":"yukbor_parkent",
    "Piskent":"yukbor_piskent",
    "Quyi Chirchiq":"yukbor_quyichirchiq",
    "Oʻrta Chirchiq":"yukbor_ortachirchiq",
    "Yangiyoʻl":"yukbor_yangiyol",
    "Yuqori Chirchiq":"yukbor_yuqorichirchiq",
    "Zangiota":"yukbor_zangiota",

}

toshkent_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_y1.items():
    toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))





an2 = {
    "Ulug'nor":"mashin_ulug'nor",
    "Andijon shahar":"mashin_andddshaxar",
    "Asaka":"mashin_asaka",
    "Baliqchi":"mashin_baliqchi",
    "Bo'ston ":"mashin_bo'ston",
    "Buloqbosh":"mashin_buloqboshi",
    "Izboskan":"mashin_izboskan",
    "Jalaquduq":"mashin_jalaquduq",
    "Xoʻjaobod":"mashin_xo'jabod",
    "Qoʻrgʻontepa":"mashin_qo'rg'ontepa",
    "Marhamat":"mashin_marhamat",
    "Oltinkoʻl":"mashin_oltinko'l",
    "Paxtaobod":"mashin_paxtaobod",
    "Shahrixon":"mashin_shaxrixon",
    "Xonabod":"mashin_xonabod",

}
tayyor_mashin_and = InlineKeyboardMarkup(row_width=3)
for key,value in an2.items():
    tayyor_mashin_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_mashin_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_mashin_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_b1 = {
"Olot" :"mashin_olot",
"Buxoro" :"mashin_buxshaxar",
"Gʻijduvon" :"mashin_gijduvon",
"Jondor" :"mashin_jondor",
"Kogon" :"mashin_kogon",
"Qorakoʻl" :"mashin_qorakol",
"Qorovulbozor" : "mashin_qorovulbozor",
"Peshku" :"mashin_peshku",
"Romitan" :"mashin_romitan",
"Shofirkon" :"mashin_shofirkon",
"Vobkent" :"mashin_vobkent",

}

buxoro_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_b1.items():
    buxoro_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_b1 = {
"Oltiariq":"mashin_oltiariq",
"Bagʻdod ":"mashin_bog'dod",
"Beshariq ":"mashin_beshariq",
"Buvayda" :"mashin_buvayda",
"Dangʻara" :"mashin_dangara",
"Fargʻona" :"mashin_vodil",
"Furqat" :"mashin_furqat",
"Qoʻshtepa":"mashin_qoshtepa",
"Quva" :"mashin_quva",
"Rishton":"mashin_rishton",
"Soʻx" :"mashin_sox",
"Toshloq":"mashin_toshloq",
"Oʻzbekiston":"mashin_ozbekiston",
"Uchkoʻprik" :"mashin_uchkoprik",
"Yozyovon" :"mashin_yozyovon",

}

fargona_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_b1.items():
    fargona_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_b1 = {
    "Chortoq":"mashin_chortoq",
    "Chust ":"mashin_chust",
    "Kosonsoy ":"mashin_kosonsoy",
    "Mingbuloq":"mashin_mingbuloq",
    "Namangan ":"mashin_namshaxar",
    "Norin":"mashin_norin",
    "Pop ":"mashin_pop",
    "To'raqo'rg'on":"mashin_toraqo'rg'on",
    "Uchqo'rg'on":"mashin_uchqo'rgo'n",
    "Uychi":"mashin_uychi",
    "Yangiqo'rg'on":"mashin_yangiqor",
    "Davlatobod ":"mashin_davlatobod",
    "Yangi Namangan":"mashin_yangi namangan",

}

namangan_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_b1.items():
    namangan_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_b1 = {
"Oqoltin" :"mashin_oqoltin",
"Boyovut" :"mashin_boyovut" ,
"Guliston" :"mashin_guliston",
"Xovos" : "mashin_xovos",
"Mirzaobod" : "mashin_mirzaobod",
"Sardoba" :"mashin_sardoba",
"Sayxunobod" :"mashin_sayxunobod",
"Sirdaryo" :"mashin_shaxri",

}


sirdaryo_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_b1.items():
    sirdaryo_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_b1 = {
"Angor":"mashin_angor",
"Bandixon":"mashin_bandixon",
"Boysun":"mashin_boysun",
"Denov" :"mashin_denov",
"Jarqoʻrgʻon":"mashin_jarqorgon",
"Qiziriq":"mashin_qiziriq",
"Qumqoʻrgʻon":"mashin_qumqorgon",
"Muzrabod":"mashin_muzrabod",
"Oltinsoy":"mashin_oltinsoy",
"Sariosiyo":"mashin_sariosiyo",
"Sherobod":"mashin_sherobod",
"Shoʻrchi":"mashin_shorchi" ,
"Termiz":"mashin_termiz",
"Uzun":"mashin_uzun",

}
surxondaryo_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_b1.items():
    surxondaryo_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_b1= {
"Dehqonobod":"mashin_dehqonobod",
"Kasbi":"mashin_kasbi",
"Kitob":"mashin_kitob",
"Koson":"mashin_koson",
"Koʻkdala":"mashin_kokdala",
"Mirishkor":"mashin_mirishkor",
"Muborak":"mashin_muborak",
"Nishon":"mashin_nishon",
"Qamashi":"mashin_qamashi" ,
"Qarshi":"mashin_qarshi",
"Yakkabogʻ" :"mashin_yakkabog",
"Gʻuzor":"mashin_guzor",
"Shahrisabz":"mashin_shahrisabz",
"Chiroqchi":"mashin_chiroqchi",

}
qashqadaryo_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_b1.items():
    qashqadaryo_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
xorazm_b1 = {
"Bogʻot" :"mashin_bogot",
"Gurlan" :"mashin_gurlan",
"Xonqa" :"mashin_xonqa",
"Hazorasp" :"mashin_hazorasp",
"Xiva" :"mashin_xiva",
"Qoʻshkoʻpir" :"mashin_qoshkorik",
"Shovot" :"mashin_shovot",
"Urganch" :"mashin_urganch",
"Yangiariq" :"mashin_yangiariq",
"Yangibozor" :"mashin_yangibozor",
"Tupproqqalʼa" :"mashin_tuproqqala",

}
for key,value in xorazm_b1.items():
    xorazm_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_b1 = {
'Bulungʻur' :"mashin_bulungur",
'Ishtixon' :"mashin_ishtixon",
'Jomboy' :"mashin_jomboy",
'Kattaqoʻrgʻon' :"mashin_kattaqorgon",
'Qoʻshrabot' :"mashin_qoshrabot",
'Narpay' :"mashin_narpay",
'Nurobod' :"mashin_nurobod",
'Oqdaryo' :"mashin_oqdaryo",
'Paxtachi' :"mashin_paxtachi",
'Payariq' :"mashin_payariq",
'Pastdargʻom' :"mashin_pastdargom",
'Samarqand' :"mashin_samashahar",
'Toyloq' :"mashin_toyloq",

}
samarqand_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_b1.items():
    samarqand_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_b1 = {
"Konimex" :"mashin_konimex",
"Karmana" :"mashin_karmana",
"Qiziltepa" :"mashin_qiziltepa",
"Xatirchi" :"mashin_xatirchi",
"Navbahor" :"mashin_navbahor",
"Nurota" :"mashin_nurota",
"Tomdi" :"mashin_tomdi",
"Uchquduq" :"mashin_uchquduq",

}
navoiy_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_b1.items():
    navoiy_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_b1 = {
"Arnasoy" :"mashin_arnasoy",
"Baxmal" :"mashin_baxmal",
"Doʻstlik" :"mashin_dostlik",
"Forish" :"mashin_forish",
"Gʻallaorol" :"mashin_gallarol",
"Sharof Rashidov ":"mashin_shrashidov",
'Mirzachoʻl' :'mashin_mirzachol',
"Paxtakor" :"mashin_paxtakor",
"Yangiobod" :"mashin_yangobod",
'Zomin' :"mashin_zomin",
'Zafarobod' :"mashin_zafarobod",
'Zarbdor' :"mashin_zarbdor",

}
jizzax_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_b1.items():
    jizzax_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_b1 = {
    "Bekobod":"mashin_bekobod",
    "Boʻstonliq":"mashin_bostonliq",
    "Boʻka":"mashin_boka",
    "Chinoz":"mashin_chinoz",
    "Qibray":"mashin_qibray",
    "Ohangaron":"mashin_ohangaron",
    "Oqqoʻrgʻon":"mashin_oqqorgon",
    "Parkent":"mashin_parkent",
    "Piskent":"mashin_piskent",
    "Quyi Chirchiq":"mashin_quyichirchiq",
    "Oʻrta Chirchiq":"mashin_ortachirchiq",
    "Yangiyoʻl":"mashin_yangiyol",
    "Yuqori Chirchiq":"mashin_yuqorichirchiq",
    "Zangiota":"mashin_zangiota",

}

toshkent_tayyor_mashin = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_b1.items():
    toshkent_tayyor_mashin.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_mashin.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_mashin.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




an1 = {
    "Ulug'nor":"yukbor_ulug'nor",
    "Andijon shahar":"yukbor_andddshaxar",
    "Asaka":"yukbor_asaka",
    "Baliqchi":"yukbor_baliqchi",
    "Bo'ston ":"yukbor_bo'ston",
    "Buloqbosh":"yukbor_buloqboshi",
    "Izboskan":"yukbor_izboskan",
    "Jalaquduq":"yukbor_jalaquduq",
    "Xoʻjaobod":"yukbor_xo'jabod",
    "Qoʻrgʻontepa":"yukbor_qo'rg'ontepa",
    "Marhamat":"yukbor_marhamat",
    "Oltinkoʻl":"yukbor_oltinko'l",
    "Paxtaobod":"yukbor_paxtaobod",
    "Shahrixon":"yukbor_shaxrixon",
    "Xonabod":"yukbor_xonabod",

}
tayyor_yukbor_and = InlineKeyboardMarkup(row_width=3)
for key,value in an1.items():
    tayyor_yukbor_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_yukbor_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_yukbor_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_y1 = {
"Olot" :"yukbor_olot",
"Buxoro" :"yukbor_buxshaxar",
"Gʻijduvon" :"yukbor_gijduvon",
"Jondor" :"yukbor_jondor",
"Kogon" :"yukbor_kogon",
"Qorakoʻl" :"yukbor_qorakol",
"Qorovulbozor" : "yukbor_qorovulbozor",
"Peshku" :"yukbor_peshku",
"Romitan" :"yukbor_romitan",
"Shofirkon" :"yukbor_shofirkon",
"Vobkent" :"yukbor_vobkent",

}

buxoro_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_y1.items():
    buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_y1 = {
"Oltiariq":"yukbor_oltiariq",
"Bagʻdod ":"yukbor_bog'dod",
"Beshariq ":"yukbor_beshariq",
"Buvayda" :"yukbor_buvayda",
"Dangʻara" :"yukbor_dangara",
"Fargʻona" :"yukbor_vodil",
"Furqat" :"yukbor_furqat",
"Qoʻshtepa":"yukbor_qoshtepa",
"Quva" :"yukbor_quva",
"Rishton":"yukbor_rishton",
"Soʻx" :"yukbor_sox",
"Toshloq":"yukbor_toshloq",
"Oʻzbekiston":"yukbor_ozbekiston",
"Uchkoʻprik" :"yukbor_uchkoprik",
"Yozyovon" :"yukbor_yozyovon",

}

fargona_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_y1.items():
    fargona_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_y1 = {
    "Chortoq":"yukbor_chortoq",
    "Chust ":"yukbor_chust",
    "Kosonsoy ":"yukbor_kosonsoy",
    "Mingbuloq":"yukbor_mingbuloq",
    "Namangan ":"yukbor_namshaxar",
    "Norin":"yukbor_norin",
    "Pop ":"yukbor_pop",
    "To'raqo'rg'on":"yukbor_toraqo'rg'on",
    "Uchqo'rg'on":"yukbor_uchqo'rgo'n",
    "Uychi":"yukbor_uychi",
    "Yangiqo'rg'on":"yukbor_yangiqor",
    "Davlatobod ":"yukbor_davlatobod",
    "Yangi Namangan":"yukbor_yangi namangan",

}

namangan_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_y1.items():
    namangan_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y1 = {
"Oqoltin" :"yukbor_oqoltin",
"Boyovut" :"yukbor_boyovut" ,
"Guliston" :"yukbor_guliston",
"Xovos" : "yukbor_xovos",
"Mirzaobod" : "yukbor_mirzaobod",
"Sardoba" :"yukbor_sardoba",
"Sayxunobod" :"yukbor_sayxunobod",
"Sirdaryo" :"yukbor_shaxri",

}


sirdaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y1.items():
    sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_y1 = {
"Angor":"yukbor_angor",
"Bandixon":"yukbor_bandixon",
"Boysun":"yukbor_boysun",
"Denov" :"yukbor_denov",
"Jarqoʻrgʻon":"yukbor_jarqorgon",
"Qiziriq":"yukbor_qiziriq",
"Qumqoʻrgʻon":"yukbor_qumqorgon",
"Muzrabod":"yukbor_muzrabod",
"Oltinsoy":"yukbor_oltinsoy",
"Sariosiyo":"yukbor_sariosiyo",
"Sherobod":"yukbor_sherobod",
"Shoʻrchi":"yukbor_shorchi" ,
"Termiz":"yukbor_termiz",
"Uzun":"yukbor_uzun",

}
surxondaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_y1.items():
    surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_y1= {
"Dehqonobod":"yukbor_dehqonobod",
"Kasbi":"yukbor_kasbi",
"Kitob":"yukbor_kitob",
"Koson":"yukbor_koson",
"Koʻkdala":"yukbor_kokdala",
"Mirishkor":"yukbor_mirishkor",
"Muborak":"yukbor_muborak",
"Nishon":"yukbor_nishon",
"Qamashi":"yukbor_qamashi" ,
"Qarshi":"yukbor_qarshi",
"Yakkabogʻ" :"yukbor_yakkabog",
"Gʻuzor":"yukbor_guzor",
"Shahrisabz":"yukbor_shahrisabz",
"Chiroqchi":"yukbor_chiroqchi",

}
qashqadaryo_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_y1.items():
    qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
xorazm_y1 = {
"Bogʻot" :"yukbor_bogot",
"Gurlan" :"yukbor_gurlan",
"Xonqa" :"yukbor_xonqa",
"Hazorasp" :"yukbor_hazorasp",
"Xiva" :"yukbor_xiva",
"Qoʻshkoʻpir" :"yukbor_qoshkorik",
"Shovot" :"yukbor_shovot",
"Urganch" :"yukbor_urganch",
"Yangiariq" :"yukbor_yangiariq",
"Yangibozor" :"yukbor_yangibozor",
"Tupproqqalʼa" :"yukbor_tuproqqala",

}
for key,value in xorazm_y1.items():
    xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_y1 = {
'Bulungʻur' :"yukbor_bulungur",
'Ishtixon' :"yukbor_ishtixon",
'Jomboy' :"yukbor_jomboy",
'Kattaqoʻrgʻon' :"yukbor_kattaqorgon",
'Qoʻshrabot' :"yukbor_qoshrabot",
'Narpay' :"yukbor_narpay",
'Nurobod' :"yukbor_nurobod",
'Oqdaryo' :"yukbor_oqdaryo",
'Paxtachi' :"yukbor_paxtachi",
'Payariq' :"yukbor_payariq",
'Pastdargʻom' :"yukbor_pastdargom",
'Samarqand' :"yukbor_samashahar",
'Toyloq' :"yukbor_toyloq",

}
samarqand_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_y1.items():
    samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_y1 = {
"Konimex" :"yukbor_konimex",
"Karmana" :"yukbor_karmana",
"Qiziltepa" :"yukbor_qiziltepa",
"Xatirchi" :"yukbor_xatirchi",
"Navbahor" :"yukbor_navbahor",
"Nurota" :"yukbor_nurota",
"Tomdi" :"yukbor_tomdi",
"Uchquduq" :"yukbor_uchquduq",

}
navoiy_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_y1.items():
    navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_y1 = {
"Arnasoy" :"yukbor_arnasoy",
"Baxmal" :"yukbor_baxmal",
"Doʻstlik" :"yukbor_dostlik",
"Forish" :"yukbor_forish",
"Gʻallaorol" :"yukbor_gallarol",
"Sharof Rashidov ":"yukbor_shrashidov",
'Mirzachoʻl' :'yukbor_mirzachol',
"Paxtakor" :"yukbor_paxtakor",
"Yangiobod" :"yukbor_yangobod",
'Zomin' :"yukbor_zomin",
'Zafarobod' :"yukbor_zafarobod",
'Zarbdor' :"yukbor_zarbdor",

}
jizzax_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_y1.items():
    jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_y1 = {
    "Bekobod":"yukbor_bekobod",
    "Boʻstonliq":"yukbor_bostonliq",
    "Boʻka":"yukbor_boka",
    "Chinoz":"yukbor_chinoz",
    "Qibray":"yukbor_qibray",
    "Ohangaron":"yukbor_ohangaron",
    "Oqqoʻrgʻon":"yukbor_oqqorgon",
    "Parkent":"yukbor_parkent",
    "Piskent":"yukbor_piskent",
    "Quyi Chirchiq":"yukbor_quyichirchiq",
    "Oʻrta Chirchiq":"yukbor_ortachirchiq",
    "Yangiyoʻl":"yukbor_yangiyol",
    "Yuqori Chirchiq":"yukbor_yuqorichirchiq",
    "Zangiota":"yukbor_zangiota",

}

toshkent_tayyor_yukbor = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_y1.items():
    toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_yukbor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


# TAYYOR YO'LOVCHI


an265 = {
    "Ulug'nor":"yolovc_ulug'nor",
    "Andijon shahar":"yolovc_andddshaxar",
    "Asaka":"yolovc_asaka",
    "Baliqchi":"yolovc_baliqchi",
    "Bo'ston ":"yolovc_bo'ston",
    "Buloqbosh":"yolovc_buloqboshi",
    "Izboskan":"yolovc_izboskan",
    "Jalaquduq":"yolovc_jalaquduq",
    "Xoʻjaobod":"yolovc_xo'jabod",
    "Qoʻrgʻontepa":"yolovc_qo'rg'ontepa",
    "Marhamat":"yolovc_marhamat",
    "Oltinkoʻl":"yolovc_oltinko'l",
    "Paxtaobod":"yolovc_paxtaobod",
    "Shahrixon":"yolovc_shaxrixon",
    "Xonabod":"yolovc_xonabod",

}
tayyor_yolovc_and = InlineKeyboardMarkup(row_width=3)
for key,value in an265.items():
    tayyor_yolovc_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_yolovc_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_yolovc_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_b156 = {
"Olot" :"yolovc_olot",
"Buxoro" :"yolovc_buxshaxar",
"Gʻijduvon" :"yolovc_gijduvon",
"Jondor" :"yolovc_jondor",
"Kogon" :"yolovc_kogon",
"Qorakoʻl" :"yolovc_qorakol",
"Qorovulbozor" : "yolovc_qorovulbozor",
"Peshku" :"yolovc_peshku",
"Romitan" :"yolovc_romitan",
"Shofirkon" :"yolovc_shofirkon",
"Vobkent" :"yolovc_vobkent",

}

buxoro_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_b156.items():
    buxoro_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_b156 = {
"Oltiariq":"yolovc_oltiariq",
"Bagʻdod ":"yolovc_bog'dod",
"Beshariq ":"yolovc_beshariq",
"Buvayda" :"yolovc_buvayda",
"Dangʻara" :"yolovc_dangara",
"Fargʻona" :"yolovc_vodil",
"Furqat" :"yolovc_furqat",
"Qoʻshtepa":"yolovc_qoshtepa",
"Quva" :"yolovc_quva",
"Rishton":"yolovc_rishton",
"Soʻx" :"yolovc_sox",
"Toshloq":"yolovc_toshloq",
"Oʻzbekiston":"yolovc_ozbekiston",
"Uchkoʻprik" :"yolovc_uchkoprik",
"Yozyovon" :"yolovc_yozyovon",

}

fargona_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_b156.items():
    fargona_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_b156 = {
    "Chortoq":"yolovc_chortoq",
    "Chust ":"yolovc_chust",
    "Kosonsoy ":"yolovc_kosonsoy",
    "Mingbuloq":"yolovc_mingbuloq",
    "Namangan ":"yolovc_namshaxar",
    "Norin":"yolovc_norin",
    "Pop ":"yolovc_pop",
    "To'raqo'rg'on":"yolovc_toraqo'rg'on",
    "Uchqo'rg'on":"yolovc_uchqo'rgo'n",
    "Uychi":"yolovc_uychi",
    "Yangiqo'rg'on":"yolovc_yangiqor",
    "Davlatobod ":"yolovc_davlatobod",
    "Yangi Namangan":"yolovc_yangi namangan",

}

namangan_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_b156.items():
    namangan_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_b156 = {
"Oqoltin" :"yolovc_oqoltin",
"Boyovut" :"yolovc_boyovut" ,
"Guliston" :"yolovc_guliston",
"Xovos" : "yolovc_xovos",
"Mirzaobod" : "yolovc_mirzaobod",
"Sardoba" :"yolovc_sardoba",
"Sayxunobod" :"yolovc_sayxunobod",
"Sirdaryo" :"yolovc_shaxri",

}


sirdaryo_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_b156.items():
    sirdaryo_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_b156 = {
"Angor":"yolovc_angor",
"Bandixon":"yolovc_bandixon",
"Boysun":"yolovc_boysun",
"Denov" :"yolovc_denov",
"Jarqoʻrgʻon":"yolovc_jarqorgon",
"Qiziriq":"yolovc_qiziriq",
"Qumqoʻrgʻon":"yolovc_qumqorgon",
"Muzrabod":"yolovc_muzrabod",
"Oltinsoy":"yolovc_oltinsoy",
"Sariosiyo":"yolovc_sariosiyo",
"Sherobod":"yolovc_sherobod",
"Shoʻrchi":"yolovc_shorchi" ,
"Termiz":"yolovc_termiz",
"Uzun":"yolovc_uzun",

}
surxondaryo_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_b156.items():
    surxondaryo_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_b156= {
"Dehqonobod":"yolovc_dehqonobod",
"Kasbi":"yolovc_kasbi",
"Kitob":"yolovc_kitob",
"Koson":"yolovc_koson",
"Koʻkdala":"yolovc_kokdala",
"Mirishkor":"yolovc_mirishkor",
"Muborak":"yolovc_muborak",
"Nishon":"yolovc_nishon",
"Qamashi":"yolovc_qamashi" ,
"Qarshi":"yolovc_qarshi",
"Yakkabogʻ" :"yolovc_yakkabog",
"Gʻuzor":"yolovc_guzor",
"Shahrisabz":"yolovc_shahrisabz",
"Chiroqchi":"yolovc_chiroqchi",

}
qashqadaryo_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_b156.items():
    qashqadaryo_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
xorazm_b156 = {
"Bogʻot" :"yolovc_bogot",
"Gurlan" :"yolovc_gurlan",
"Xonqa" :"yolovc_xonqa",
"Hazorasp" :"yolovc_hazorasp",
"Xiva" :"yolovc_xiva",
"Qoʻshkoʻpir" :"yolovc_qoshkorik",
"Shovot" :"yolovc_shovot",
"Urganch" :"yolovc_urganch",
"Yangiariq" :"yolovc_yangiariq",
"Yangibozor" :"yolovc_yangibozor",
"Tupproqqalʼa" :"yolovc_tuproqqala",

}
for key,value in xorazm_b156.items():
    xorazm_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_b156 = {
'Bulungʻur' :"yolovc_bulungur",
'Ishtixon' :"yolovc_ishtixon",
'Jomboy' :"yolovc_jomboy",
'Kattaqoʻrgʻon' :"yolovc_kattaqorgon",
'Qoʻshrabot' :"yolovc_qoshrabot",
'Narpay' :"yolovc_narpay",
'Nurobod' :"yolovc_nurobod",
'Oqdaryo' :"yolovc_oqdaryo",
'Paxtachi' :"yolovc_paxtachi",
'Payariq' :"yolovc_payariq",
'Pastdargʻom' :"yolovc_pastdargom",
'Samarqand' :"yolovc_samashahar",
'Toyloq' :"yolovc_toyloq",

}
samarqand_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_b156.items():
    samarqand_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_b156 = {
"Konimex" :"yolovc_konimex",
"Karmana" :"yolovc_karmana",
"Qiziltepa" :"yolovc_qiziltepa",
"Xatirchi" :"yolovc_xatirchi",
"Navbahor" :"yolovc_navbahor",
"Nurota" :"yolovc_nurota",
"Tomdi" :"yolovc_tomdi",
"Uchquduq" :"yolovc_uchquduq",

}
navoiy_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_b156.items():
    navoiy_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_b156 = {
"Arnasoy" :"yolovc_arnasoy",
"Baxmal" :"yolovc_baxmal",
"Doʻstlik" :"yolovc_dostlik",
"Forish" :"yolovc_forish",
"Gʻallaorol" :"yolovc_gallarol",
"Sharof Rashidov ":"yolovc_shrashidov",
'Mirzachoʻl' :'yolovc_mirzachol',
"Paxtakor" :"yolovc_paxtakor",
"Yangiobod" :"yolovc_yangobod",
'Zomin' :"yolovc_zomin",
'Zafarobod' :"yolovc_zafarobod",
'Zarbdor' :"yolovc_zarbdor",

}
jizzax_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_b156.items():
    jizzax_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_b156 = {
    "Bekobod":"yolovc_bekobod",
    "Boʻstonliq":"yolovc_bostonliq",
    "Boʻka":"yolovc_boka",
    "Chinoz":"yolovc_chinoz",
    "Qibray":"yolovc_qibray",
    "Ohangaron":"yolovc_ohangaron",
    "Oqqoʻrgʻon":"yolovc_oqqorgon",
    "Parkent":"yolovc_parkent",
    "Piskent":"yolovc_piskent",
    "Quyi Chirchiq":"yolovc_quyichirchiq",
    "Oʻrta Chirchiq":"yolovc_ortachirchiq",
    "Yangiyoʻl":"yolovc_yangiyol",
    "Yuqori Chirchiq":"yolovc_yuqorichirchiq",
    "Zangiota":"yolovc_zangiota",

}

toshkent_tayyor_yolovc = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_b156.items():
    toshkent_tayyor_yolovc.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_yolovc.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_yolovc.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



# TAYYOR POCHTA MASHINASI
#################################
################################
#############################
ssdas = {
    "Ulug'nor":"pocmas_ulug'nor",
    "Andijon shahar":"pocmas_andddshaxar",
    "Asaka":"pocmas_asaka",
    "Baliqchi":"pocmas_baliqchi",
    "Bo'ston ":"pocmas_bo'ston",
    "Buloqbosh":"pocmas_buloqboshi",
    "Izboskan":"pocmas_izboskan",
    "Jalaquduq":"pocmas_jalaquduq",
    "Xoʻjaobod":"pocmas_xo'jabod",
    "Qoʻrgʻontepa":"pocmas_qo'rg'ontepa",
    "Marhamat":"pocmas_marhamat",
    "Oltinkoʻl":"pocmas_oltinko'l",
    "Paxtaobod":"pocmas_paxtaobod",
    "Shahrixon":"pocmas_shaxrixon",
    "Xonabod":"pocmas_xonabod",

}
tayyor_pocmas_and = InlineKeyboardMarkup(row_width=3)
for key,value in ssdas.items():
    tayyor_pocmas_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_pocmas_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_pocmas_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_b1561 = {
"Olot" :"pocmas_olot",
"Buxoro" :"pocmas_buxshaxar",
"Gʻijduvon" :"pocmas_gijduvon",
"Jondor" :"pocmas_jondor",
"Kogon" :"pocmas_kogon",
"Qorakoʻl" :"pocmas_qorakol",
"Qorovulbozor" : "pocmas_qorovulbozor",
"Peshku" :"pocmas_peshku",
"Romitan" :"pocmas_romitan",
"Shofirkon" :"pocmas_shofirkon",
"Vobkent" :"pocmas_vobkent",

}

buxoro_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_b1561.items():
    buxoro_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_b15s6 = {
"Oltiariq":"pocmas_oltiariq",
"Bagʻdod ":"pocmas_bog'dod",
"Beshariq ":"pocmas_beshariq",
"Buvayda" :"pocmas_buvayda",
"Dangʻara" :"pocmas_dangara",
"Fargʻona" :"pocmas_vodil",
"Furqat" :"pocmas_furqat",
"Qoʻshtepa":"pocmas_qoshtepa",
"Quva" :"pocmas_quva",
"Rishton":"pocmas_rishton",
"Soʻx" :"pocmas_sox",
"Toshloq":"pocmas_toshloq",
"Oʻzbekiston":"pocmas_ozbekiston",
"Uchkoʻprik" :"pocmas_uchkoprik",
"Yozyovon" :"pocmas_yozyovon",

}

fargona_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_b15s6.items():
    fargona_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_b15s6 = {
    "Chortoq":"pocmas_chortoq",
    "Chust ":"pocmas_chust",
    "Kosonsoy ":"pocmas_kosonsoy",
    "Mingbuloq":"pocmas_mingbuloq",
    "Namangan ":"pocmas_namshaxar",
    "Norin":"pocmas_norin",
    "Pop ":"pocmas_pop",
    "To'raqo'rg'on":"pocmas_toraqo'rg'on",
    "Uchqo'rg'on":"pocmas_uchqo'rgo'n",
    "Uychi":"pocmas_uychi",
    "Yangiqo'rg'on":"pocmas_yangiqor",
    "Davlatobod ":"pocmas_davlatobod",
    "Yangi Namangan":"pocmas_yangi namangan",

}

namangan_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_b15s6.items():
    namangan_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_b15s6 = {
"Oqoltin" :"pocmas_oqoltin",
"Boyovut" :"pocmas_boyovut" ,
"Guliston" :"pocmas_guliston",
"Xovos" : "pocmas_xovos",
"Mirzaobod" : "pocmas_mirzaobod",
"Sardoba" :"pocmas_sardoba",
"Sayxunobod" :"pocmas_sayxunobod",
"Sirdaryo" :"pocmas_shaxri",

}


sirdaryo_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_b15s6.items():
    sirdaryo_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_pocmas = {
"Angor":"pocmas_angor",
"Bandixon":"pocmas_bandixon",
"Boysun":"pocmas_boysun",
"Denov" :"pocmas_denov",
"Jarqoʻrgʻon":"pocmas_jarqorgon",
"Qiziriq":"pocmas_qiziriq",
"Qumqoʻrgʻon":"pocmas_qumqorgon",
"Muzrabod":"pocmas_muzrabod",
"Oltinsoy":"pocmas_oltinsoy",
"Sariosiyo":"pocmas_sariosiyo",
"Sherobod":"pocmas_sherobod",
"Shoʻrchi":"pocmas_shorchi" ,
"Termiz":"pocmas_termiz",
"Uzun":"pocmas_uzun",

}
surxondaryo_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_pocmas.items():
    surxondaryo_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_pocmas= {
"Dehqonobod":"pocmas_dehqonobod",
"Kasbi":"pocmas_kasbi",
"Kitob":"pocmas_kitob",
"Koson":"pocmas_koson",
"Koʻkdala":"pocmas_kokdala",
"Mirishkor":"pocmas_mirishkor",
"Muborak":"pocmas_muborak",
"Nishon":"pocmas_nishon",
"Qamashi":"pocmas_qamashi" ,
"Qarshi":"pocmas_qarshi",
"Yakkabogʻ" :"pocmas_yakkabog",
"Gʻuzor":"pocmas_guzor",
"Shahrisabz":"pocmas_shahrisabz",
"Chiroqchi":"pocmas_chiroqchi",

}
qashqadaryo_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_pocmas.items():
    qashqadaryo_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
xorazm_pocmas = {
"Bogʻot" :"pocmas_bogot",
"Gurlan" :"pocmas_gurlan",
"Xonqa" :"pocmas_xonqa",
"Hazorasp" :"pocmas_hazorasp",
"Xiva" :"pocmas_xiva",
"Qoʻshkoʻpir" :"pocmas_qoshkorik",
"Shovot" :"pocmas_shovot",
"Urganch" :"pocmas_urganch",
"Yangiariq" :"pocmas_yangiariq",
"Yangibozor" :"pocmas_yangibozor",
"Tupproqqalʼa" :"pocmas_tuproqqala",

}
for key,value in xorazm_pocmas.items():
    xorazm_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_pocmas = {
'Bulungʻur' :"pocmas_bulungur",
'Ishtixon' :"pocmas_ishtixon",
'Jomboy' :"pocmas_jomboy",
'Kattaqoʻrgʻon' :"pocmas_kattaqorgon",
'Qoʻshrabot' :"pocmas_qoshrabot",
'Narpay' :"pocmas_narpay",
'Nurobod' :"pocmas_nurobod",
'Oqdaryo' :"pocmas_oqdaryo",
'Paxtachi' :"pocmas_paxtachi",
'Payariq' :"pocmas_payariq",
'Pastdargʻom' :"pocmas_pastdargom",
'Samarqand' :"pocmas_samashahar",
'Toyloq' :"pocmas_toyloq",

}
samarqand_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_pocmas.items():
    samarqand_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_pocmas = {
"Konimex" :"pocmas_konimex",
"Karmana" :"pocmas_karmana",
"Qiziltepa" :"pocmas_qiziltepa",
"Xatirchi" :"pocmas_xatirchi",
"Navbahor" :"pocmas_navbahor",
"Nurota" :"pocmas_nurota",
"Tomdi" :"pocmas_tomdi",
"Uchquduq" :"pocmas_uchquduq",

}
navoiy_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_pocmas.items():
    navoiy_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_pocmas = {
"Arnasoy" :"pocmas_arnasoy",
"Baxmal" :"pocmas_baxmal",
"Doʻstlik" :"pocmas_dostlik",
"Forish" :"pocmas_forish",
"Gʻallaorol" :"pocmas_gallarol",
"Sharof Rashidov ":"pocmas_shrashidov",
'Mirzachoʻl' :'pocmas_mirzachol',
"Paxtakor" :"pocmas_paxtakor",
"Yangiobod" :"pocmas_yangobod",
'Zomin' :"pocmas_zomin",
'Zafarobod' :"pocmas_zafarobod",
'Zarbdor' :"pocmas_zarbdor",

}
jizzax_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_pocmas.items():
    jizzax_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_pocmas = {
    "Bekobod":"pocmas_bekobod",
    "Boʻstonliq":"pocmas_bostonliq",
    "Boʻka":"pocmas_boka",
    "Chinoz":"pocmas_chinoz",
    "Qibray":"pocmas_qibray",
    "Ohangaron":"pocmas_ohangaron",
    "Oqqoʻrgʻon":"pocmas_oqqorgon",
    "Parkent":"pocmas_parkent",
    "Piskent":"pocmas_piskent",
    "Quyi Chirchiq":"pocmas_quyichirchiq",
    "Oʻrta Chirchiq":"pocmas_ortachirchiq",
    "Yangiyoʻl":"pocmas_yangiyol",
    "Yuqori Chirchiq":"pocmas_yuqorichirchiq",
    "Zangiota":"pocmas_zangiota",

}

toshkent_tayyor_pocmas = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_pocmas.items():
    toshkent_tayyor_pocmas.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_pocmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_pocmas.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



# TAYYOR SAYOHATCHI
#####################
#################################
################################
##############################


jza = {
    "Ulug'nor":"sayyoh_ulug'nor",
    "Andijon shahar":"sayyoh_andddshaxar",
    "Asaka":"sayyoh_asaka",
    "Baliqchi":"sayyoh_baliqchi",
    "Bo'ston ":"sayyoh_bo'ston",
    "Buloqbosh":"sayyoh_buloqboshi",
    "Izboskan":"sayyoh_izboskan",
    "Jalaquduq":"sayyoh_jalaquduq",
    "Xoʻjaobod":"sayyoh_xo'jabod",
    "Qoʻrgʻontepa":"sayyoh_qo'rg'ontepa",
    "Marhamat":"sayyoh_marhamat",
    "Oltinkoʻl":"sayyoh_oltinko'l",
    "Paxtaobod":"sayyoh_paxtaobod",
    "Shahrixon":"sayyoh_shaxrixon",
    "Xonabod":"sayyoh_xonabod",

}
tayyor_sayyoh_and = InlineKeyboardMarkup(row_width=3)
for key,value in jza.items():
    tayyor_sayyoh_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_sayyoh_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_sayyoh_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_b15612 = {
"Olot" :"sayyoh_olot",
"Buxoro" :"sayyoh_buxshaxar",
"Gʻijduvon" :"sayyoh_gijduvon",
"Jondor" :"sayyoh_jondor",
"Kogon" :"sayyoh_kogon",
"Qorakoʻl" :"sayyoh_qorakol",
"Qorovulbozor" : "sayyoh_qorovulbozor",
"Peshku" :"sayyoh_peshku",
"Romitan" :"sayyoh_romitan",
"Shofirkon" :"sayyoh_shofirkon",
"Vobkent" :"sayyoh_vobkent",

}

buxoro_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_b15612.items():
    buxoro_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_b15s62 = {
"Oltiariq":"sayyoh_oltiariq",
"Bagʻdod ":"sayyoh_bog'dod",
"Beshariq ":"sayyoh_beshariq",
"Buvayda" :"sayyoh_buvayda",
"Dangʻara" :"sayyoh_dangara",
"Fargʻona" :"sayyoh_vodil",
"Furqat" :"sayyoh_furqat",
"Qoʻshtepa":"sayyoh_qoshtepa",
"Quva" :"sayyoh_quva",
"Rishton":"sayyoh_rishton",
"Soʻx" :"sayyoh_sox",
"Toshloq":"sayyoh_toshloq",
"Oʻzbekiston":"sayyoh_ozbekiston",
"Uchkoʻprik" :"sayyoh_uchkoprik",
"Yozyovon" :"sayyoh_yozyovon",

}

fargona_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_b15s62.items():
    fargona_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_b15s62 = {
    "Chortoq":"sayyoh_chortoq",
    "Chust ":"sayyoh_chust",
    "Kosonsoy ":"sayyoh_kosonsoy",
    "Mingbuloq":"sayyoh_mingbuloq",
    "Namangan ":"sayyoh_namshaxar",
    "Norin":"sayyoh_norin",
    "Pop ":"sayyoh_pop",
    "To'raqo'rg'on":"sayyoh_toraqo'rg'on",
    "Uchqo'rg'on":"sayyoh_uchqo'rgo'n",
    "Uychi":"sayyoh_uychi",
    "Yangiqo'rg'on":"sayyoh_yangiqor",
    "Davlatobod ":"sayyoh_davlatobod",
    "Yangi Namangan":"sayyoh_yangi namangan",

}

namangan_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_b15s62.items():
    namangan_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_b15s62 = {
"Oqoltin" :"sayyoh_oqoltin",
"Boyovut" :"sayyoh_boyovut" ,
"Guliston" :"sayyoh_guliston",
"Xovos" : "sayyoh_xovos",
"Mirzaobod" : "sayyoh_mirzaobod",
"Sardoba" :"sayyoh_sardoba",
"Sayxunobod" :"sayyoh_sayxunobod",
"Sirdaryo" :"sayyoh_shaxri",

}


sirdaryo_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_b15s62.items():
    sirdaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_sayyoh = {
"Angor":"sayyoh_angor",
"Bandixon":"sayyoh_bandixon",
"Boysun":"sayyoh_boysun",
"Denov" :"sayyoh_denov",
"Jarqoʻrgʻon":"sayyoh_jarqorgon",
"Qiziriq":"sayyoh_qiziriq",
"Qumqoʻrgʻon":"sayyoh_qumqorgon",
"Muzrabod":"sayyoh_muzrabod",
"Oltinsoy":"sayyoh_oltinsoy",
"Sariosiyo":"sayyoh_sariosiyo",
"Sherobod":"sayyoh_sherobod",
"Shoʻrchi":"sayyoh_shorchi" ,
"Termiz":"sayyoh_termiz",
"Uzun":"sayyoh_uzun",

}
surxondaryo_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_sayyoh.items():
    surxondaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_sayyoh= {
"Dehqonobod":"sayyoh_dehqonobod",
"Kasbi":"sayyoh_kasbi",
"Kitob":"sayyoh_kitob",
"Koson":"sayyoh_koson",
"Koʻkdala":"sayyoh_kokdala",
"Mirishkor":"sayyoh_mirishkor",
"Muborak":"sayyoh_muborak",
"Nishon":"sayyoh_nishon",
"Qamashi":"sayyoh_qamashi" ,
"Qarshi":"sayyoh_qarshi",
"Yakkabogʻ" :"sayyoh_yakkabog",
"Gʻuzor":"sayyoh_guzor",
"Shahrisabz":"sayyoh_shahrisabz",
"Chiroqchi":"sayyoh_chiroqchi",

}
qashqadaryo_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_sayyoh.items():
    qashqadaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
xorazm_sayyoh = {
"Bogʻot" :"sayyoh_bogot",
"Gurlan" :"sayyoh_gurlan",
"Xonqa" :"sayyoh_xonqa",
"Hazorasp" :"sayyoh_hazorasp",
"Xiva" :"sayyoh_xiva",
"Qoʻshkoʻpir" :"sayyoh_qoshkorik",
"Shovot" :"sayyoh_shovot",
"Urganch" :"sayyoh_urganch",
"Yangiariq" :"sayyoh_yangiariq",
"Yangibozor" :"sayyoh_yangibozor",
"Tupproqqalʼa" :"sayyoh_tuproqqala",

}
for key,value in xorazm_sayyoh.items():
    xorazm_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_sayyoh = {
'Bulungʻur' :"sayyoh_bulungur",
'Ishtixon' :"sayyoh_ishtixon",
'Jomboy' :"sayyoh_jomboy",
'Kattaqoʻrgʻon' :"sayyoh_kattaqorgon",
'Qoʻshrabot' :"sayyoh_qoshrabot",
'Narpay' :"sayyoh_narpay",
'Nurobod' :"sayyoh_nurobod",
'Oqdaryo' :"sayyoh_oqdaryo",
'Paxtachi' :"sayyoh_paxtachi",
'Payariq' :"sayyoh_payariq",
'Pastdargʻom' :"sayyoh_pastdargom",
'Samarqand' :"sayyoh_samashahar",
'Toyloq' :"sayyoh_toyloq",

}
samarqand_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_sayyoh.items():
    samarqand_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_sayyoh = {
"Konimex" :"sayyoh_konimex",
"Karmana" :"sayyoh_karmana",
"Qiziltepa" :"sayyoh_qiziltepa",
"Xatirchi" :"sayyoh_xatirchi",
"Navbahor" :"sayyoh_navbahor",
"Nurota" :"sayyoh_nurota",
"Tomdi" :"sayyoh_tomdi",
"Uchquduq" :"sayyoh_uchquduq",

}
navoiy_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_sayyoh.items():
    navoiy_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_sayyoh = {
"Arnasoy" :"sayyoh_arnasoy",
"Baxmal" :"sayyoh_baxmal",
"Doʻstlik" :"sayyoh_dostlik",
"Forish" :"sayyoh_forish",
"Gʻallaorol" :"sayyoh_gallarol",
"Sharof Rashidov ":"sayyoh_shrashidov",
'Mirzachoʻl' :'sayyoh_mirzachol',
"Paxtakor" :"sayyoh_paxtakor",
"Yangiobod" :"sayyoh_yangobod",
'Zomin' :"sayyoh_zomin",
'Zafarobod' :"sayyoh_zafarobod",
'Zarbdor' :"sayyoh_zarbdor",

}
jizzax_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_sayyoh.items():
    jizzax_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_sayyoh = {
    "Bekobod":"sayyoh_bekobod",
    "Boʻstonliq":"sayyoh_bostonliq",
    "Boʻka":"sayyoh_boka",
    "Chinoz":"sayyoh_chinoz",
    "Qibray":"sayyoh_qibray",
    "Ohangaron":"sayyoh_ohangaron",
    "Oqqoʻrgʻon":"sayyoh_oqqorgon",
    "Parkent":"sayyoh_parkent",
    "Piskent":"sayyoh_piskent",
    "Quyi Chirchiq":"sayyoh_quyichirchiq",
    "Oʻrta Chirchiq":"sayyoh_ortachirchiq",
    "Yangiyoʻl":"sayyoh_yangiyol",
    "Yuqori Chirchiq":"sayyoh_yuqorichirchiq",
    "Zangiota":"sayyoh_zangiota",

}

toshkent_tayyor_sayyoh = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_sayyoh.items():
    toshkent_tayyor_sayyoh.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_sayyoh.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_sayyoh.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))





# TAYYOR SAYOHATCHI MASHINA # 
##############################
###########################################
##########################################
##############################################
#######################################


jz656a = {
    "Ulug'nor":"massay_ulug'nor",
    "Andijon shahar":"massay_andddshaxar",
    "Asaka":"massay_asaka",
    "Baliqchi":"massay_baliqchi",
    "Bo'ston ":"massay_bo'ston",
    "Buloqbosh":"massay_buloqboshi",
    "Izboskan":"massay_izboskan",
    "Jalaquduq":"massay_jalaquduq",
    "Xoʻjaobod":"massay_xo'jabod",
    "Qoʻrgʻontepa":"massay_qo'rg'ontepa",
    "Marhamat":"massay_marhamat",
    "Oltinkoʻl":"massay_oltinko'l",
    "Paxtaobod":"massay_paxtaobod",
    "Shahrixon":"massay_shaxrixon",
    "Xonabod":"massay_xonabod",

}
tayyor_massay_and = InlineKeyboardMarkup(row_width=3)
for key,value in jz656a.items():
    tayyor_massay_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_massay_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_massay_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


buxoro_massay = {
"Olot" :"massay_olot",
"Buxoro" :"massay_buxshaxar",
"Gʻijduvon" :"massay_gijduvon",
"Jondor" :"massay_jondor",
"Kogon" :"massay_kogon",
"Qorakoʻl" :"massay_qorakol",
"Qorovulbozor" : "massay_qorovulbozor",
"Peshku" :"massay_peshku",
"Romitan" :"massay_romitan",
"Shofirkon" :"massay_shofirkon",
"Vobkent" :"massay_vobkent",

}

buxoro_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_massay.items():
    buxoro_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


fargona_massay = {
"Oltiariq":"massay_oltiariq",
"Bagʻdod ":"massay_bog'dod",
"Beshariq ":"massay_beshariq",
"Buvayda" :"massay_buvayda",
"Dangʻara" :"massay_dangara",
"Fargʻona" :"massay_vodil",
"Furqat" :"massay_furqat",
"Qoʻshtepa":"massay_qoshtepa",
"Quva" :"massay_quva",
"Rishton":"massay_rishton",
"Soʻx" :"massay_sox",
"Toshloq":"massay_toshloq",
"Oʻzbekiston":"massay_ozbekiston",
"Uchkoʻprik" :"massay_uchkoprik",
"Yozyovon" :"massay_yozyovon",

}

fargona_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_massay.items():
    fargona_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

namangan_massay = {
    "Chortoq":"massay_chortoq",
    "Chust ":"massay_chust",
    "Kosonsoy ":"massay_kosonsoy",
    "Mingbuloq":"massay_mingbuloq",
    "Namangan ":"massay_namshaxar",
    "Norin":"massay_norin",
    "Pop ":"massay_pop",
    "To'raqo'rg'on":"massay_toraqo'rg'on",
    "Uchqo'rg'on":"massay_uchqo'rgo'n",
    "Uychi":"massay_uychi",
    "Yangiqo'rg'on":"massay_yangiqor",
    "Davlatobod ":"massay_davlatobod",
    "Yangi Namangan":"massay_yangi namangan",

}

namangan_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_massay.items():
    namangan_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_massay = {
"Oqoltin" :"massay_oqoltin",
"Boyovut" :"massay_boyovut" ,
"Guliston" :"massay_guliston",
"Xovos" : "massay_xovos",
"Mirzaobod" : "massay_mirzaobod",
"Sardoba" :"massay_sardoba",
"Sayxunobod" :"massay_sayxunobod",
"Sirdaryo" :"massay_shaxri",

}


sirdaryo_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_massay.items():
    sirdaryo_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

surxondaryo_massay = {
"Angor":"massay_angor",
"Bandixon":"massay_bandixon",
"Boysun":"massay_boysun",
"Denov" :"massay_denov",
"Jarqoʻrgʻon":"massay_jarqorgon",
"Qiziriq":"massay_qiziriq",
"Qumqoʻrgʻon":"massay_qumqorgon",
"Muzrabod":"massay_muzrabod",
"Oltinsoy":"massay_oltinsoy",
"Sariosiyo":"massay_sariosiyo",
"Sherobod":"massay_sherobod",
"Shoʻrchi":"massay_shorchi" ,
"Termiz":"massay_termiz",
"Uzun":"massay_uzun",

}
surxondaryo_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_massay.items():
    surxondaryo_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

qashqadaryo_massay= {
"Dehqonobod":"massay_dehqonobod",
"Kasbi":"massay_kasbi",
"Kitob":"massay_kitob",
"Koson":"massay_koson",
"Koʻkdala":"massay_kokdala",
"Mirishkor":"massay_mirishkor",
"Muborak":"massay_muborak",
"Nishon":"massay_nishon",
"Qamashi":"massay_qamashi" ,
"Qarshi":"massay_qarshi",
"Yakkabogʻ" :"massay_yakkabog",
"Gʻuzor":"massay_guzor",
"Shahrisabz":"massay_shahrisabz",
"Chiroqchi":"massay_chiroqchi",

}
qashqadaryo_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_massay.items():
    qashqadaryo_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor_massay = InlineKeyboardMarkup(row_width=4)
xorazm_massay = {
"Bogʻot" :"massay_bogot",
"Gurlan" :"massay_gurlan",
"Xonqa" :"massay_xonqa",
"Hazorasp" :"massay_hazorasp",
"Xiva" :"massay_xiva",
"Qoʻshkoʻpir" :"massay_qoshkorik",
"Shovot" :"massay_shovot",
"Urganch" :"massay_urganch",
"Yangiariq" :"massay_yangiariq",
"Yangibozor" :"massay_yangibozor",
"Tupproqqalʼa" :"massay_tuproqqala",

}
for key,value in xorazm_massay.items():
    xorazm_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_massay = {
'Bulungʻur' :"massay_bulungur",
'Ishtixon' :"massay_ishtixon",
'Jomboy' :"massay_jomboy",
'Kattaqoʻrgʻon' :"massay_kattaqorgon",
'Qoʻshrabot' :"massay_qoshrabot",
'Narpay' :"massay_narpay",
'Nurobod' :"massay_nurobod",
'Oqdaryo' :"massay_oqdaryo",
'Paxtachi' :"massay_paxtachi",
'Payariq' :"massay_payariq",
'Pastdargʻom' :"massay_pastdargom",
'Samarqand' :"massay_samashahar",
'Toyloq' :"massay_toyloq",

}
samarqand_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_massay.items():
    samarqand_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_massay = {
"Konimex" :"massay_konimex",
"Karmana" :"massay_karmana",
"Qiziltepa" :"massay_qiziltepa",
"Xatirchi" :"massay_xatirchi",
"Navbahor" :"massay_navbahor",
"Nurota" :"massay_nurota",
"Tomdi" :"massay_tomdi",
"Uchquduq" :"massay_uchquduq",

}
navoiy_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_massay.items():
    navoiy_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_massay = {
"Arnasoy" :"massay_arnasoy",
"Baxmal" :"massay_baxmal",
"Doʻstlik" :"massay_dostlik",
"Forish" :"massay_forish",
"Gʻallaorol" :"massay_gallarol",
"Sharof Rashidov ":"massay_shrashidov",
'Mirzachoʻl' :'massay_mirzachol',
"Paxtakor" :"massay_paxtakor",
"Yangiobod" :"massay_yangobod",
'Zomin' :"massay_zomin",
'Zafarobod' :"massay_zafarobod",
'Zarbdor' :"massay_zarbdor",

}
jizzax_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_massay.items():
    jizzax_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



toshkent_massay = {
    "Bekobod":"massay_bekobod",
    "Boʻstonliq":"massay_bostonliq",
    "Boʻka":"massay_boka",
    "Chinoz":"massay_chinoz",
    "Qibray":"massay_qibray",
    "Ohangaron":"massay_ohangaron",
    "Oqqoʻrgʻon":"massay_oqqorgon",
    "Parkent":"massay_parkent",
    "Piskent":"massay_piskent",
    "Quyi Chirchiq":"massay_quyichirchiq",
    "Oʻrta Chirchiq":"massay_ortachirchiq",
    "Yangiyoʻl":"massay_yangiyol",
    "Yuqori Chirchiq":"massay_yuqorichirchiq",
    "Zangiota":"massay_zangiota",

}

toshkent_tayyor_massay = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_massay.items():
    toshkent_tayyor_massay.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor_massay.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor_massay.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))





