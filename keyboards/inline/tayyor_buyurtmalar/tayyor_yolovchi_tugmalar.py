from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

anssaa = {
    "Ulug'nor":"yolo_ulug'nor",
    "Andijon shahar":"yolo_andijon shaxar",
    "Asaka":"yolo_asaka",
    "Baliqchi":"yolo_baliqchi",
    "Bo'ston ":"yolo_bo'ston",
    "Buloqbosh":"yolo_buloqboshi",
    "Izboskan":"yolo_izboskan",
    "Jalaquduq":"yolo_jalaquduq",
    "Xoʻjaobod":"yolo_xo'jabod",
    "Qoʻrgʻontepa":"yolo_qo'rg'ontepa",
    "Marhamat":"yolo_marhamat",
    "Oltinkoʻl":"yolo_oltinko'l",
    "Paxtaobod":"yolo_paxtaobod",
    "Shahrixon":"yolo_shaxrixon",
    "Xonabod":"yolo_xonabod",
}
andijon_yolo = InlineKeyboardMarkup(row_width=3)
for key,value in anssaa.items():
    andijon_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
    
    
namangan_axxa = {
    "Chortoq":"yolo_chortoq",
    "Chust ":"yolo_chust",
    "Kosonsoy ":"yolo_kosonsoy",
    "Mingbuloq":"yolo_mingbuloq",
    "Namangan ":"yolo_namangan shaxar",
    "Norin":"yolo_norin",
    "Pop ":"yolo_pop",
    "To'raqo'rg'on":"yolo_toraqo'rg'on",
    "Uchqo'rg'on":"yolo_uchqo'rgo'n",
    "Uychi":"yolo_uychi",
    "Yangiqo'rg'on":"yolo_yangi qo'rg'on",
    "Davlatobod ":"yolo_davlatobod",
    "Yangi Namangan":"yolo_yangi namangan",

}

namangan_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_axxa.items():
    namangan_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



fargona_assas = {
"Oltiariq":"yolo_oltiariq",
"Bagʻdod ":"yolo_bog'dod",
"Beshariq ":"yolo_beshariq",
"Buvayda" :"yolo_buvayda",
"Dangʻara" :"yolo_dangara",
"Fargʻona" :"yolo_fergana ",
"Furqat" :"yolo_furqat",
"Qoʻshtepa":"yolo_qo'shtepa",
"Quva" :"yolo_quva",
"Rishton":"yolo_rishton",
"Soʻx" :"yolo_sox",
"Toshloq":"yolo_toshloq",
"Oʻzbekiston":"yolo_o'zbekiston",
"Uchkoʻprik" :"yolo_uchko'prik",
"Yozyovon" :"yolo_yozyovon",

}

fargona_yolo = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_assas.items():
    fargona_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
    

buxoro_aasa = {
"Olot" :"yolo_olot",
"Buxoro" :"yolo_buxoro shaxar",
"Gʻijduvon" :"yolo_g'ijduvon",
"Jondor" :"yolo_jondor",
"Kogon" :"yolo_kogon",
"Qorakoʻl" :"yolo_qorako'l",
"Qorovulbozor" : "yolo_qorovulbozor",
"Peshku" :"yolo_peshku",
"Romitan" :"yolo_romitan",
"Shofirkon" :"yolo_shofirkon",
"Vobkent" :"yolo_vobkent",

}

buxoro_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_aasa.items():
    buxoro_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

toshkent_yaz1 = {
    "Bekobod":"yolo_bekobod",
    "Boʻstonliq":"yolo_bostonliq",
    "Boʻka":"yolo_boka",
    "Chinoz":"yolo_chinoz",
    "Qibray":"yolo_qibray",
    "Ohangaron":"yolo_ohangaron",
    "Oqqoʻrgʻon":"yolo_oqqorgon",
    "Parkent":"yolo_parkent",
    "Piskent":"yolo_piskent",
    "Quyi Chirchiq":"yolo_quyichirchiq",
    "Oʻrta Chirchiq":"yolo_ortachirchiq",
    "Yangiyoʻl":"yolo_yangiyol",
    "Yuqori Chirchiq":"yolo_yuqorichirchiq",
    "Zangiota":"yolo_zangiota",

}

toshkent_yolo= InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_yaz1.items():
    toshkent_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



sirdaryo_y1ax = {
"Oqoltin" :"yolo_oqoltin",
"Boyovut" :"yolo_boyovut" ,
"Guliston" :"yolo_guliston",
"Xovos" : "yolo_xovos",
"Mirzaobod" : "yolo_mirzaobod",
"Sardoba" :"yolo_sardoba",
"Sayxunobod" :"yolo_sayxunobod",
"Sirdaryo" :"yolo_sirdaryo shaxri",

}


sirdaryo_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y1ax.items():
    sirdaryo_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


surxondaryo_yuk = {
"Angor":"yolo_angor",
"Bandixon":"yolo_bandixon",
"Boysun":"yolo_boysun",
"Denov" :"yolo_denov",
"Jarqoʻrgʻon":"yolo_jarqorgon",
"Qiziriq":"yolo_qiziriq",
"Qumqoʻrgʻon":"yolo_qumqorgon",
"Muzrabod":"yolo_muzrabod",
"Oltinsoy":"yolo_oltinsoy",
"Sariosiyo":"yolo_sariosiyo",
"Sherobod":"yolo_sherobod",
"Shoʻrchi":"yolo_shorchi" ,
"Termiz":"yolo_termiz",
"Uzun":"yolo_uzun",

}
surxondaryo_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yuk.items():
    surxondaryo_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


surxondaryo_yuk = {
"Angor":"yolo_angor",
"Bandixon":"yolo_bandixon",
"Boysun":"yolo_boysun",
"Denov" :"yolo_denov",
"Jarqoʻrgʻon":"yolo_jarqorgon",
"Qiziriq":"yolo_qiziriq",
"Qumqoʻrgʻon":"yolo_qumqorgon",
"Muzrabod":"yolo_muzrabod",
"Oltinsoy":"yolo_oltinsoy",
"Sariosiyo":"yolo_sariosiyo",
"Sherobod":"yolo_sherobod",
"Shoʻrchi":"yolo_shorchi" ,
"Termiz":"yolo_termiz",
"Uzun":"yolo_uzun",

}
surxondaryo_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_yuk.items():
    surxondaryo_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




qashqadaryo_yuk = {
"Dehqonobod":"yolo_dehqonobod",
"Kasbi":"yolo_kasbi",
"Kitob":"yolo_kitob",
"Koson":"yolo_koson",
"Koʻkdala":"yolo_kokdala",
"Mirishkor":"yolo_mirishkor",
"Muborak":"yolo_muborak",
"Nishon":"yolo_nishon",
"Qamashi":"yolo_qamashi" ,
"Qarshi":"yolo_qarshi",
"Yakkabogʻ" :"yolo_yakkabog",
"Gʻuzor":"yolo_guzor",
"Shahrisabz":"yolo_shahrisabz",
"Chiroqchi":"yolo_chiroqchi",

}
qashqadaryo_yolo = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_yuk.items():
    qashqadaryo_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_yolo= InlineKeyboardMarkup(row_width=4)
xorazm_yuk = {
"Bogʻot" :"yolo_bog'ot",
"Gurlan" :"yolo_gurlan",
"Xonqa" :"yolo_xonqa",
"Hazorasp" :"yolo_hazorasp",
"Xiva" :"yolo_xiva",
"Qoʻshkoʻpir" :"yolo_qoshko'prik",
"Shovot" :"yolo_shovot",
"Urganch" :"yolo_urganch",
"Yangiariq" :"yolo_yangiariq",
"Yangibozor" :"yolo_yangibozor",
"Tupproqqalʼa" :"yolo_tuproqqal'a",

}
for key,value in xorazm_yuk.items():
    xorazm_yolo.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yolo.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_yolo.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



navoiy_yuk = {
"Konimex" :"yolo_konimex",
"Karmana" :"yolo_karmana",
"Qiziltepa" :"yolo_qiziltepa",
"Xatirchi" :"yolo_xatirchi",
"Navbahor" :"yolo_navbahor",
"Nurota" :"yolo_nurota",
"Tomdi" :"yolo_tomdi",
"Uchquduq" :"yolo_uchquduq",

}
navoiy_yolota = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_yuk.items():
    navoiy_yolota.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yolota.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_yolota.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_ydcsdas = {
"Arnasoy" :"yolo_arnasoy",
"Baxmal" :"yolo_baxmal",
"Doʻstlik" :"yolo_do'stlik",
"Forish" :"yolo_forish",
"Gʻallaorol" :"yolo_g'allarol",
"Sharof Rashidov ":"yolo_sharof rashidov",
'Mirzachoʻl' :'yolo_mirzachol',
"Paxtakor" :"yolo_paxtakor",
"Yangiobod" :"yolo_yangi obod",
'Zomin' :"yolo_zomin",
'Zafarobod' :"yolo_zafarobod",
'Zarbdor' :"yolo_zarbdor",

}
jizzax_yolota = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_ydcsdas.items():
    jizzax_yolota.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yolota.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_yolota.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




samarqaand_yasasa = {
'Bulungʻur' :"yolo_bulungur",
'Ishtixon' :"yolo_ishtixon",
'Jomboy' :"yolo_jomboy",
'Kattaqoʻrgʻon' :"yolo_kattaqorgon",
'Qoʻshrabot' :"yolo_qoshrabot",
'Narpay' :"yolo_narpay",
'Nurobod' :"yolo_nurobod",
'Oqdaryo' :"yolo_oqdaryo",
'Paxtachi' :"yolo_paxtachi",
'Payariq' :"yolo_payariq",
'Pastdargʻom' :"yolo_pastdargom",
'Samarqand' :"yolo_samarqand shahar",
'Toyloq' :"yolo_toyloq",

}
samarqand_yolota = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yasasa.items():
    samarqand_yolota.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yolota.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_yolota.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))