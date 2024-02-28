from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

taxi_tayyor_callback = CallbackData("tayyor_taxi", "item_name")

viloyat = {
    "Andijon":"raz",
    "Namangan":"dva",
    "Farg'ona":"tri",
    "Buxoro":"chitiri",
    "Toshkent":"pyat",
    "Toshkent shahar":"kent shahar",
    "Sirdaryo":"shest",
    "Surxondaryo":"sem",
    "Qashqadaryo":"vosem",
    "Xorazm":"devit",
    "Navoiy":"desit",
    "Jizzax":"adinatsat",
    "Samarqand":"dvinatsad",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"Ortga",
    "Bosh menu":"Bosh menu",
}
tax_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    tax_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=taxi_tayyor_callback.new(item_name=value)))

taxi_tayyor_callback_and = CallbackData("tayyor_taxi_and", "item_name")


an = {
    "Ulug'nor":"ulug'nor",
    "Andijon shahar":"andddshaxar",
    "Asaka":"asaka",
    "Baliqchi":"baliqchi",
    "Bo'ston ":"bo'ston",
    "Buloqbosh":"buloqboshi",
    "Izboskan":"izboskan",
    "Jalaquduq":"jalaquduq",
    "Xoʻjaobod":"xo'jabod",
    "Qoʻrgʻontepa":"qo'rg'ontepa",
    "Marhamat":"marhamat",
    "Oltinkoʻl":"oltinko'l",
    "Paxtaobod":"paxtaobod",
    "Shahrixon":"shaxrixon",
    "Xonabod":"xonabod",

}
tayyor_and = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    tayyor_and.insert(InlineKeyboardButton(text=key, callback_data=value))

tayyor_and.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
tayyor_and.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


namangan_y = {
    "Chortoq":"chortoq",
    "Chust ":"chust",
    "Kosonsoy ":"kosonsoy",
    "Mingbuloq":"mingbuloq",
    "Namangan ":"namshaxar",
    "Norin":"norin",
    "Pop ":"pop",
    "To'raqo'rg'on":"toraqo'rg'on",
    "Uchqo'rg'on":"uchqo'rgo'n",
    "Uychi":"uychi",
    "Yangiqo'rg'on":"yangiqor",
    "Davlatobod ":"davlatobod",
    "Yangi Namangan":"newnam",

}

namangan_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in namangan_y.items():
    namangan_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
namangan_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




fargona_y = {
"Oltiariq":"oltiariq",
"Bagʻdod ":"bog'dod",
"Beshariq ":"beshariq",
"Buvayda" :"buvayda",
"Dangʻara" :"dangara",
"Fargʻona" :"vodil",
"Furqat" :"furqat",
"Qoʻshtepa":"qoshtepa",
"Quva" :"quva",
"Rishton":"rishton",
"Soʻx" :"sox",
"Toshloq":"toshloq",
"Oʻzbekiston":"ozbekiston",
"Uchkoʻprik" :"uchkoprik",
"Yozyovon" :"yozyovon",

}

fargona_tayyor = InlineKeyboardMarkup(row_width=4)
for key, value in fargona_y.items():
    fargona_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
fargona_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



buxoro_y = {
"Olot" :"olot",
"Buxoro" :"buxshaxar",
"Gʻijduvon" :"gijduvon",
"Jondor" :"jondor",
"Kogon" :"kogon",
"Qorakoʻl" :"qorakol",
"Qorovulbozor" : "qorovulbozor",
"Peshku" :"peshku",
"Romitan" :"romitan",
"Shofirkon" :"shofirkon",
"Vobkent" :"vobkent",

}

buxoro_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in buxoro_y.items():
    buxoro_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
buxoro_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



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

toshkent_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in toshkent_y.items():
    toshkent_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
toshkent_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))




sirdaryo_y = {
"Oqoltin" :"oqoltin",
"Boyovut" :"boyovut" ,
"Guliston" :"guliston",
"Xovos" : "xovos",
"Mirzaobod" : "mirzaobod",
"Sardoba" :"sardoba",
"Sayxunobod" :"sayxunobod",
"Sirdaryo" :"sshaxri",

}


sirdaryo_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y.items():
    sirdaryo_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
sirdaryo_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


surxondaryo_y = {
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

}
surxondaryo_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in surxondaryo_y.items():
    surxondaryo_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
surxondaryo_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))

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
qashqadaryo_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in qashqadaryo_y.items():
    qashqadaryo_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
qashqadaryo_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


xorazm_tayyor = InlineKeyboardMarkup(row_width=4)
xorazm_y = {
"Bogʻot" :"bogot",
"Gurlan" :"gurlan",
"Xonqa" :"xonqa",
"Hazorasp" :"hazorasp",
"Xiva" :"xiva",
"Qoʻshkoʻpir" :"qoshkorik",
"Shovot" :"shovot",
"Urganch" :"urganch",
"Yangiariq" :"yangiariq",
"Yangibozor" :"yangibozor",
"Tupproqqalʼa" :"tuproqqala",

}
for key,value in xorazm_y.items():
    xorazm_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
xorazm_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


samarqaand_y = {
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
'Samarqand' :"samashahar",
'Toyloq' :"toyloq",

}
samarqand_tayyor = InlineKeyboardMarkup(row_width=4)
for key, value in samarqaand_y.items():
    samarqand_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
samarqand_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


navoiy_y = {
"Konimex" :"konimex",
"Karmana" :"karmana",
"Qiziltepa" :"qiziltepa",
"Xatirchi" :"xatirchi",
"Navbahor" :"navbahor",
"Nurota" :"nurota",
"Tomdi" :"tomdi",
"Uchquduq" :"uchquduq",

}
navoiy_tayyor = InlineKeyboardMarkup(row_width=4)
for key,value in navoiy_y.items():
    navoiy_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
navoiy_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))


jizzax_y = {
"Arnasoy" :"arnasoy",
"Baxmal" :"baxmal",
"Doʻstlik" :"dostlik",
"Forish" :"forish",
"Gʻallaorol" :"gallarol",
"Sharof Rashidov ":"shrashidov",
'Mirzachoʻl' :'mirzachol',
"Paxtakor" :"paxtakor",
"Yangiobod" :"yangobod",
'Zomin' :"zomin",
'Zafarobod' :"zafarobod",
'Zarbdor' :"zarbdor",

}
jizzax_tayyor = InlineKeyboardMarkup(row_width=4)
for key, value in jizzax_y.items():
    jizzax_tayyor.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_tayyor.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='atmen'))
jizzax_tayyor.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))
