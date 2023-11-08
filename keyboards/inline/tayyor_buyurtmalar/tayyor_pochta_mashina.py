from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

anssaa = {
    "Ulug'nor": "pmas_ulug'nor",
    "Andijon shahar": "pmas_andijon shaxar",
    "Asaka": "pmas_asaka",
    "Baliqchi": "pmas_baliqchi",
    "Bo'ston ": "pmas_bo'ston",
    "Buloqbosh": "pmas_buloqboshi",
    "Izboskan": "pmas_izboskan",
    "Jalaquduq": "pmas_jalaquduq",
    "Xoʻjaobod": "pmas_xo'jabod",
    "Qoʻrgʻontepa": "pmas_qo'rg'ontepa",
    "Marhamat": "pmas_marhamat",
    "Oltinkoʻl": "pmas_oltinko'l",
    "Paxtaobod": "pmas_paxtaobod",
    "Shahrixon": "pmas_shaxrixon",
    "Xonabod": "pmas_xonabod",
}
andijon_pmas = InlineKeyboardMarkup(row_width=3)
for key, value in anssaa.items():
    andijon_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_axxa = {
    "Chortoq": "pmas_chortoq",
    "Chust ": "pmas_chust",
    "Kosonsoy ": "pmas_kosonsoy",
    "Mingbuloq": "pmas_mingbuloq",
    "Namangan ": "pmas_namangan shaxar",
    "Norin": "pmas_norin",
    "Pop ": "pmas_pop",
    "To'raqo'rg'on": "pmas_toraqo'rg'on",
    "Uchqo'rg'on": "pmas_uchqo'rgo'n",
    "Uychi": "pmas_uychi",
    "Yangiqo'rg'on": "pmas_yangi qo'rg'on",
    "Davlatobod ": "pmas_davlatobod",
    "Yangi Namangan": "pmas_yangi namangan",

}

namangan_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in namangan_axxa.items():
    namangan_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
namangan_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

fargona_assas = {
    "Oltiariq": "pmas_oltiariq",
    "Bagʻdod ": "pmas_bog'dod",
    "Beshariq ": "pmas_beshariq",
    "Buvayda": "pmas_buvayda",
    "Dangʻara": "pmas_dangara",
    "Fargʻona": "pmas_fergana ",
    "Furqat": "pmas_furqat",
    "Qoʻshtepa": "pmas_qo'shtepa",
    "Quva": "pmas_quva",
    "Rishton": "pmas_rishton",
    "Soʻx": "pmas_sox",
    "Toshloq": "pmas_toshloq",
    "Oʻzbekiston": "pmas_o'zbekiston",
    "Uchkoʻprik": "pmas_uchko'prik",
    "Yozyovon": "pmas_yozyovon",

}

fargona_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_assas.items():
    fargona_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))

buxoro_aasa = {
    "Olot": "pmas_olot",
    "Buxoro": "pmas_buxoro shaxar",
    "Gʻijduvon": "pmas_g'ijduvon",
    "Jondor": "pmas_jondor",
    "Kogon": "pmas_kogon",
    "Qorakoʻl": "pmas_qorako'l",
    "Qorovulbozor": "pmas_qorovulbozor",
    "Peshku": "pmas_peshku",
    "Romitan": "pmas_romitan",
    "Shofirkon": "pmas_shofirkon",
    "Vobkent": "pmas_vobkent",

}

buxoro_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in buxoro_aasa.items():
    buxoro_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
buxoro_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

toshkent_yaz1 = {
    "Bekobod": "pmas_bekobod",
    "Boʻstonliq": "pmas_bostonliq",
    "Boʻka": "pmas_boka",
    "Chinoz": "pmas_chinoz",
    "Qibray": "pmas_qibray",
    "Ohangaron": "pmas_ohangaron",
    "Oqqoʻrgʻon": "pmas_oqqorgon",
    "Parkent": "pmas_parkent",
    "Piskent": "pmas_piskent",
    "Quyi Chirchiq": "pmas_quyichirchiq",
    "Oʻrta Chirchiq": "pmas_ortachirchiq",
    "Yangiyoʻl": "pmas_yangiyol",
    "Yuqori Chirchiq": "pmas_yuqorichirchiq",
    "Zangiota": "pmas_zangiota",

}

toshkent_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in toshkent_yaz1.items():
    toshkent_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
toshkent_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

sirdaryo_y1ax = {
    "Oqoltin": "pmas_oqoltin",
    "Boyovut": "pmas_boyovut",
    "Guliston": "pmas_guliston",
    "Xovos": "pmas_xovos",
    "Mirzaobod": "pmas_mirzaobod",
    "Sardoba": "pmas_sardoba",
    "Sayxunobod": "pmas_sayxunobod",
    "Sirdaryo": "pmas_sirdaryo shaxri",

}

sirdaryo_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in sirdaryo_y1ax.items():
    sirdaryo_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
sirdaryo_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

surxondaryo_yuk = {
    "Angor": "pmas_angor",
    "Bandixon": "pmas_bandixon",
    "Boysun": "pmas_boysun",
    "Denov": "pmas_denov",
    "Jarqoʻrgʻon": "pmas_jarqorgon",
    "Qiziriq": "pmas_qiziriq",
    "Qumqoʻrgʻon": "pmas_qumqorgon",
    "Muzrabod": "pmas_muzrabod",
    "Oltinsoy": "pmas_oltinsoy",
    "Sariosiyo": "pmas_sariosiyo",
    "Sherobod": "pmas_sherobod",
    "Shoʻrchi": "pmas_shorchi",
    "Termiz": "pmas_termiz",
    "Uzun": "pmas_uzun",

}
surxondaryo_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in surxondaryo_yuk.items():
    surxondaryo_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
surxondaryo_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

surxondaryo_yuk = {
    "Angor": "pmas_angor",
    "Bandixon": "pmas_bandixon",
    "Boysun": "pmas_boysun",
    "Denov": "pmas_denov",
    "Jarqoʻrgʻon": "pmas_jarqorgon",
    "Qiziriq": "pmas_qiziriq",
    "Qumqoʻrgʻon": "pmas_qumqorgon",
    "Muzrabod": "pmas_muzrabod",
    "Oltinsoy": "pmas_oltinsoy",
    "Sariosiyo": "pmas_sariosiyo",
    "Sherobod": "pmas_sherobod",
    "Shoʻrchi": "pmas_shorchi",
    "Termiz": "pmas_termiz",
    "Uzun": "pmas_uzun",

}
surxondaryo_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in surxondaryo_yuk.items():
    surxondaryo_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
surxondaryo_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

qashqadaryo_yuk = {
    "Dehqonobod": "pmas_dehqonobod",
    "Kasbi": "pmas_kasbi",
    "Kitob": "pmas_kitob",
    "Koson": "pmas_koson",
    "Koʻkdala": "pmas_kokdala",
    "Mirishkor": "pmas_mirishkor",
    "Muborak": "pmas_muborak",
    "Nishon": "pmas_nishon",
    "Qamashi": "pmas_qamashi",
    "Qarshi": "pmas_qarshi",
    "Yakkabogʻ": "pmas_yakkabog",
    "Gʻuzor": "pmas_guzor",
    "Shahrisabz": "pmas_shahrisabz",
    "Chiroqchi": "pmas_chiroqchi",

}
qashqadaryo_pmas = InlineKeyboardMarkup(row_width=4)
for key, value in qashqadaryo_yuk.items():
    qashqadaryo_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
qashqadaryo_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

xorazm_pmas = InlineKeyboardMarkup(row_width=4)
xorazm_yuk = {
    "Bogʻot": "pmas_bog'ot",
    "Gurlan": "pmas_gurlan",
    "Xonqa": "pmas_xonqa",
    "Hazorasp": "pmas_hazorasp",
    "Xiva": "pmas_xiva",
    "Qoʻshkoʻpir": "pmas_qoshko'prik",
    "Shovot": "pmas_shovot",
    "Urganch": "pmas_urganch",
    "Yangiariq": "pmas_yangiariq",
    "Yangibozor": "pmas_yangibozor",
    "Tupproqqalʼa": "pmas_tuproqqal'a",

}
for key, value in xorazm_yuk.items():
    xorazm_pmas.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_pmas.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
xorazm_pmas.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

navoiy_yuk = {
    "Konimex": "pmas_konimex",
    "Karmana": "pmas_karmana",
    "Qiziltepa": "pmas_qiziltepa",
    "Xatirchi": "pmas_xatirchi",
    "Navbahor": "pmas_navbahor",
    "Nurota": "pmas_nurota",
    "Tomdi": "pmas_tomdi",
    "Uchquduq": "pmas_uchquduq",

}
navoiy_pmasta = InlineKeyboardMarkup(row_width=4)
for key, value in navoiy_yuk.items():
    navoiy_pmasta.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_pmasta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
navoiy_pmasta.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

jizzax_ydcsdas = {
    "Arnasoy": "pmas_arnasoy",
    "Baxmal": "pmas_baxmal",
    "Doʻstlik": "pmas_do'stlik",
    "Forish": "pmas_forish",
    "Gʻallaorol": "pmas_g'allarol",
    "Sharof Rashidov ": "pmas_sharof rashidov",
    'Mirzachoʻl': 'pmas_mirzachol',
    "Paxtakor": "pmas_paxtakor",
    "Yangiobod": "pmas_yangi obod",
    'Zomin': "pmas_zomin",
    'Zafarobod': "pmas_zafarobod",
    'Zarbdor': "pmas_zarbdor",

}
jizzax_pmasta = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_ydcsdas.items():
    jizzax_pmasta.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_pmasta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
jizzax_pmasta.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))

samarqaand_yasasa = {
    'Bulungʻur': "pmas_bulungur",
    'Ishtixon': "pmas_ishtixon",
    'Jomboy': "pmas_jomboy",
    'Kattaqoʻrgʻon': "pmas_kattaqorgon",
    'Qoʻshrabot': "pmas_qoshrabot",
    'Narpay': "pmas_narpay",
    'Nurobod': "pmas_nurobod",
    'Oqdaryo': "pmas_oqdaryo",
    'Paxtachi': "pmas_paxtachi",
    'Payariq': "pmas_payariq",
    'Pastdargʻom': "pmas_pastdargom",
    'Samarqand': "pmas_samarqand shahar",
    'Toyloq': "pmas_toyloq",

}
samarqand_pmasta = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_yasasa.items():
    samarqand_pmasta.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_pmasta.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish', callback_data='atmen'))
samarqand_pmasta.insert(InlineKeyboardButton(text='ortga', callback_data='ortga'))