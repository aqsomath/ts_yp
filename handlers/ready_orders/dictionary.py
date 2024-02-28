from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

all_district = {

    "Andijon shahar": "andijon shaxar",
    "Andijon tuman": "andijon tuman",
    "Xonabod shahar": "xonabod shahar",
    "Ulug'nor":"ulug'nor tuman",
    "Asaka":"asaka tuman",
    "Baliqchi":"baliqchi tuman",
    "Bo'ston ":"bo'ston tuman",
    "Buloqbosh":"buloqboshi tuman",
    "Izboskan":"izboskan tuman",
    "Jalaquduq":"jalaquduq tuman",
    "Xoʻjaobod":"xo'jabod tuman",
    "Qoʻrgʻontepa":"qo'rg'ontepa tuman",
    "Marhamat":"marhamat tuman",
    "Oltinkoʻl":"oltinko'l tuman",
    "Paxtaobod":"paxtaobod tuman",
    "Shahrixon":"shaxrixon tuman",
"Namangan shahar": "namangan shahar",
    "Namangan tuman": "namangan tumani",
    "Chortoq":"chortoq tumani",
    "Chust ":"chust tumani",
    "Kosonsoy ":"kosonsoy tumani",
    "Mingbuloq":"mingbuloq tumani",
    "Norin":"norin tumani",
    "Pop ":"pop tumani",
    "To'raqo'rg'on":"toraqo'rg'on tumani",
    "Uchqo'rg'on":"uchqo'rgo'n tumani",
    "Uychi":"uychi tumani",
    "Yangiqo'rg'on":"yangi qo'rg'on tumani",
    "Yangi Namangan":"yangi namangan tumani",
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
"Buxoro shahri" :"buxoro shaxar",
"Buxoro tuman" :"buxoro tuman",
"Kogon shahar" :"kogon shahar",
"Kogon tuman" :"kogon tuman",
"Olot" :"olot tuman",
"Gʻijduvon" :"g'ijduvon tuman",
"Jondor" :"jondor tuman",
"Qorakoʻl" :"qorako'l tuman",
"Qorovulbozor" : "qorovulbozor tuman",
"Peshku" :"peshku tuman",
"Romitan" :"romitan tuman",
"Shofirkon" :"shofirkon tuman",
"Vobkent" :"vobkent tuman",
"Toshkent tuman":"toshkent tuman",
    "Angren shahar":"angren shahar",
    "Bekobod shahar":"bekobod shahar",
    "Nurafshon shahar":"nurafshon shahar",
    "Omaliq shahar":"olmaliq shahar",
    "Ohangaron shahar":"ohangaron shahar",
    "Chirchiq shahar":"chirchiq shahar",
    "Yangiyo'l shahar":"yangiyo'l shahar",
    "Bekobod":"bekobod tumani",
    "Boʻstonliq":"bostonliq tumani",
    "Boʻka":"boka tumani",
    "Chinoz":"chinoz tumani",
    "Qibray":"qibray tumani",
    "Ohangaron":"ohangaron tumani",
    "Oqqoʻrgʻon":"oqqorgon tumani",
    "Parkent":"parkent tumani",
    "Piskent":"piskent tumani",
    "Quyi Chirchiq":"quyichirchiq tumani",
    "Oʻrta Chirchiq":"ortachirchiq tumani",
    "Yangiyoʻl":"yangiyol tumani",
    "Yuqori Chirchiq":"yuqorichirchiq tumani",
    "Zangiota":"zangiota tumani",
    "Qo'yliq":"qoyliq",
"Sirdaryo shahar" :"sirdaryo shahar",
"Sirdaryo tuman" :"sirdaryo tumani",
"Guliston shahar" :"guliston shahar",
"Yangiyer shahar" :"yangiyer shahar",
"Shirin shahar" :"shirin shahar",
"Oqoltin" :"oqoltin tumani",
"Boyovut" :"boyovut tumani" ,
"Guliston" :"guliston tumani",
"Xovos" : "xovos tumani",
"Mirzaobod" : "mirzaobod tumani",
"Sardoba" :"sardoba tumani",
"Sayxunobod" :"sayxunobod tumani",
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
"Qarshi shahar":"qarshi shahar",
"Shahrisabz shahar":"shahrisabz shahar",
"Dehqonobod":"dehqonobod tumani",
"Kasbi":"kasbi tumani",
"Kitob":"kitob tumani",
"Koson":"koson tumani",
"Koʻkdala":"kokdala tumani",
"Mirishkor":"mirishkor tumani",
"Muborak":"muborak tumani",
"Nishon":"nishon tumani",
"Qamashi":"qamashi tumani" ,
"Yakkabogʻ" :"yakkabog tumani",
"Gʻuzor":"guzor tumani",
"Shahrisabz tuman":"shahrisabz tumani",
"Qarshi tuman":"qarshi tuman",
"Chiroqchi":"chiroqchi tumani",
"Xiva shahar" :"xiva shahar",
"Urganch shahar" :"urganch shahar",
"Bogʻot" :"bog'ot tumani",
"Gurlan" :"gurlan tumani",
"Xonqa" :"xonqa tumani",
"Hazorasp" :"hazorasp tumani",
"Xiva" :"xiva tumani",
"Qoʻshkoʻpir" :"qoshko'prik tumani",
"Shovot" :"shovot tumani",
"Urganch" :"urganch tumani",
"Yangiariq" :"yangiariq tumani",
"Yangibozor" :"yangibozor tumani",
"Tupproqqalʼa" :"tuproqqal'a tumani",
"Navoiy shahar" :"navoiy shahar",
"Zarafshon shahar" :"zarafshon shahar",
"Konimex" :"konimex tumani",
"Karmana" :"karmana tumani",
"Qiziltepa" :"qiziltepa tumani",
"Xatirchi" :"xatirchi tumani",
"Navbahor" :"navbahor tumani",
"Nurota" :"nurota tumani",
"Tomdi" :"tomdi tumani",
"Uchquduq" :"uchquduq tumani",
"Jizzax shahar" :"jizzax shahar",
"Arnasoy" :"arnasoy tumani",
"Baxmal" :"baxmal tumani",
"Doʻstlik" :"do'stlik tumani",
"Forish" :"forish tumani",
"Gʻallaorol" :"g'allarol tumani",
"Sharof Rashidov ":"sharof rashidov tumani",
'Mirzachoʻl' :'mirzachol tumani',
"Paxtakor" :"paxtakor tumani",
"Yangiobod" :"yangi obod tumani",
'Zomin' :"zomin tumani",
'Zafarobod' :"zafarobod tumani",
'Zarbdor' :"zarbdor tumani",
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
"Toshkent shahar":"Toshkent shahar",
        "Bektemir":"Bektemir tumani",
        "Mirzo Ulug‘bek":"Mirzo Ulug'bek tumani",
        "Mirobod tumani":"Mirobod tumani",
        "Olmazor tumani":"Olmazor tumani",
        "Sirg‘ali tumani":"Sirg'ali tumani",
        "Uchtepa tumani":"Uchtepa tumani",
        "Chilonzor tumani":"Chilonzor tumani",
        "Shayxontohur tumani":"Shayxontohur tumani",
        "Yunusobod tumani":"Yunusobod tumani",
        "Yakkasaroy tumani":"Yakkasaroy tumani",
        "Yashnobod tumani":"Yashnobod tumani",
"Nukus shahri":"Nukus shahar",
"Amudaryo tumani":"Amudaryo tumani",
"Beruniy tumani":"Beruniy tumani",
"Kegeyli tumani":"Kegeyli tumani",
"Qanliko‘l tumani":"Qanliko'l tumani",
"Qorao‘zak tumani":"Qorao'zak tumani",
"Qo‘ng‘irot tumani":"Qo'ng'irot tumani",
"Mo‘ynoq tumani":"Mo'ynoq tumani",
"Nukus tumani":"Nukus tumani",
"Taxiatosh tumani":"Taxiatosh tumani",
"Taxtako‘pir tumani":"Taxtako'prik tumani",
"To‘rtko‘l tumani":"To'rtko'l tumani",
"Xo‘jayli tumani":"Xo'jayli tumani",
"Chimboy tumani":"Chimboy tumani",
"Sho‘manoy tumani":"Sho'manoy tumani",
"Ellikqal’a tumani":"Ellikqal'a tumani",

}





tumanlar_all={
"Sirdaryo shahar" :"sirdaryo shahar1",
"Sirdaryo tuman" :"sirdaryo tumani1",
"Guliston shahar" :"guliston shahar1",
"Yangiyer shahar" :"yangiyer shahar1",
"Shirin shahar" :"shirin shahar1",
"Oqoltin" :"oqoltin tumani1",
"Boyovut" :"boyovut tumani1" ,
"Guliston" :"guliston tumani1",
"Xovos" : "xovos tumani1",
"Mirzaobod" : "mirzaobod tumani1",
"Sardoba" :"sardoba tumani1",
"Sayxunobod" :"sayxunobod tumani1",
"Andijon shahar": "andijon shaxar1",
    "Andijon tuman": "andijon tuman1",
    "Xonabod shahar": "xonabod shahar1",
    "Ulug'nor":"ulug'nor tuman1",
    "Asaka":"asaka tuman1",
    "Baliqchi":"baliqchi tuman1",
    "Bo'ston ":"bo'ston tuman1",
    "Buloqbosh":"buloqboshi tuman1",
    "Izboskan":"izboskan tuman1",
    "Jalaquduq":"jalaquduq tuman1",
    "Xoʻjaobod":"xo'jabod tuman1",
    "Qoʻrgʻontepa":"qo'rg'ontepa tuman1",
    "Marhamat":"marhamat tuman1",
    "Oltinkoʻl":"oltinko'l tuman1",
    "Paxtaobod":"paxtaobod tuman1",
    "Shahrixon":"shaxrixon tuman1",
"Namangan shahar": "namangan shahar1",
    "Namangan tuman": "namangan tumani1",
    "Chortoq":"chortoq tumani1",
    "Chust ":"chust tumani1",
    "Kosonsoy ":"kosonsoy tumani1",
    "Mingbuloq":"mingbuloq tumani1",
    "Norin":"norin tumani1",
    "Pop ":"pop tumani1",
    "To'raqo'rg'on":"toraqo'rg'on tumani1",
    "Uchqo'rg'on":"uchqo'rgo'n tumani1",
    "Uychi":"uychi tumani1",
    "Yangiqo'rg'on":"yangi qo'rg'on tumani1",
    "Yangi Namangan":"yangi namangan tumani1",
"Fargʻona shaxar" :"farg'ona shahar1",
"Fargʻona tuman1" :"farg'ona tuman1",
"Qo'qon shahar":"qo'qon shahar1",
"Quvasoy shahar":"quvasoy shahar1",
"Marg'ilon shahar":"marg'ilon shahar1",
"Oltiariq":"oltiariq tuman1",
"Bagʻdod ":"bog'dod tuman1",
"Beshariq ":"beshariq tuman1",
"Buvayda" :"buvayda tuman1",
"Dangʻara" :"dangara tuman1",
"Furqat" :"furqat tuman1",
"Qoʻshtepa":"qo'shtepa tuman1",
"Quva" :"quva tuman1",
"Rishton":"rishton tuman1",
"Soʻx" :"sox tuman1",
"Toshloq":"toshloq tuman1",
"Oʻzbekiston":"o'zbekiston tuman1",
"Uchkoʻprik" :"uchko'prik tuman1",
"Yozyovon" :"yozyovon tuman1",
"Buxoro shahri" :"buxoro shaxar1",
"Buxoro tuman1" :"buxoro tuman1",
"Kogon shahar" :"kogon shahar1",
"Kogon tuman" :"kogon tuman1",
"Olot" :"olot tuman1",
"Gʻijduvon" :"g'ijduvon tuman1",
"Jondor" :"jondor tuman1",
"Qorakoʻl" :"qorako'l tuman1",
"Qorovulbozor" : "qorovulbozor tuman1",
"Peshku" :"peshku tuman1",
"Romitan" :"romitan tuman1",
"Shofirkon" :"shofirkon tuman1",
"Vobkent" :"vobkent tuman1",
    "Toshkent tuman": "toshkent tuman1",
    "Angren shahar": "angren shahar1",
    "Bekobod shahar": "bekobod shahar1",
    "Nurafshon shahar": "nurafshon shahar1",
    "Omaliq shahar": "olmaliq shahar1",
    "Ohangaron shahar": "ohangaron shahar1",
    "Chirchiq shahar": "chirchiq shahar1",
    "Yangiyo'l shahar": "yangiyo'l shahar1",
    "Bekobod": "bekobod tumani1",
    "Boʻstonliq": "bostonliq tumani1",
    "Boʻka": "boka tumani1",
    "Chinoz": "chinoz tumani1",
    "Qibray": "qibray tumani1",
    "Ohangaron": "ohangaron tumani1",
    "Oqqoʻrgʻon": "oqqorgon tumani1",
    "Parkent": "parkent tumani1",
    "Piskent": "piskent tumani1",
    "Quyi Chirchiq": "quyichirchiq tumani1",
    "Oʻrta Chirchiq": "ortachirchiq tumani1",
    "Yangiyoʻl": "yangiyol tumani1",
    "Yuqori Chirchiq": "yuqorichirchiq tumani1",
    "Zangiota": "zangiota tumani1",
    "Qo'yliq": "qoyliq1",
"Termiz shahar":"termiz shahar1",
"Termiz tuman":"termiz tumani1",
"Angor":"angor tumani1",
"Bandixon":"bandixon tumani1",
"Boysun":"boysun tumani1",
"Denov" :"denov tumani1",
"Jarqoʻrgʻon":"jarqorgon tumani1",
"Qiziriq":"qiziriq tumani1",
"Qumqoʻrgʻon":"qumqorgon tumani1",
"Muzrabod":"muzrabod tumani1",
"Oltinsoy":"oltinsoy tumani1",
"Sariosiyo":"sariosiyo tumani1",
"Sherobod":"sherobod tumani1",
"Shoʻrchi":"shorchi tumani1" ,
"Uzun":"uzun tumani1",
"Qarshi shahar":"qarshi shahar1",
"Shahrisabz shahar":"shahrisabz shahar1",
"Dehqonobod":"dehqonobod tumani1",
"Kasbi":"kasbi tumani1",
"Kitob":"kitob tumani1",
"Koson":"koson tumani1",
"Koʻkdala":"kokdala tumani1",
"Mirishkor":"mirishkor tumani1",
"Muborak":"muborak tumani1",
"Nishon":"nishon tumani1",
"Qamashi":"qamashi tumani1" ,
"Yakkabogʻ" :"yakkabog tumani1",
"Gʻuzor":"guzor tumani1",
"Shahrisabz tuman":"shahrisabz tumani1",
"Qarshi tuman":"qarshi tuman1",
"Chiroqchi":"chiroqchi tumani1",
"Xiva shahar" :"xiva shahar1",
"Urganch shahar" :"urganch shahar1",
"Bogʻot" :"bog'ot tumani1",
"Gurlan" :"gurlan tumani1",
"Xonqa" :"xonqa tumani1",
"Hazorasp" :"hazorasp tumani1",
"Xiva" :"xiva tumani1",
"Qoʻshkoʻpir" :"qoshko'prik tumani1",
"Shovot" :"shovot tumani1",
"Urganch" :"urganch tumani1",
"Yangiariq" :"yangiariq tumani1",
"Yangibozor" :"yangibozor tumani1",
"Tupproqqalʼa" :"tuproqqal'a tumani1",
"Navoiy shahar" :"navoiy shahar1",
"Zarafshon shahar" :"zarafshon shahar1",
"Konimex" :"konimex tumani1",
"Karmana" :"karmana tumani1",
"Qiziltepa" :"qiziltepa tumani1",
"Xatirchi" :"xatirchi tumani1",
"Navbahor" :"navbahor tumani1",
"Nurota" :"nurota tumani1",
"Tomdi" :"tomdi tumani1",
"Uchquduq" :"uchquduq tumani1",
"Jizzax shahar" :"jizzax shahar1",
"Arnasoy" :"arnasoy tumani1",
"Baxmal" :"baxmal tumani1",
"Doʻstlik" :"do'stlik tumani1",
"Forish" :"forish tumani1",
"Gʻallaorol" :"g'allarol tumani1",
"Sharof Rashidov ":"sharof rashidov tumani1",
'Mirzachoʻl' :'mirzachol tumani1',
"Paxtakor" :"paxtakor tumani1",
"Yangiobod" :"yangi obod tumani1",
'Zomin' :"zomin tumani1",
'Zafarobod' :"zafarobod tumani1",
'Zarbdor' :"zarbdor tumani1",
'Samarqand shaxar' :"samarqand shahar1",
'Kattaqoʻrgʻon shahar' :"kattaqorgon shahar1",
'Bulungʻur' :"bulungur tumani1",
'Ishtixon' :"ishtixon tumani1",
'Jomboy' :"jomboy tumani1",
'Kattaqoʻrgʻon tuman' :"kattaqorgon tumani1",
'Qoʻshrabot' :"qoshrabot tumani1",
'Narpay' :"narpay tumani1",
'Nurobod' :"nurobod tumani1",
'Oqdaryo' :"oqdaryo tumani1",
'Paxtachi' :"paxtachi tumani1",
'Payariq' :"payariq tumani1",
'Pastdargʻom' :"pastdargom tumani1",
'Samarqand tuman' :"samarqand tumani1",
'Toyloq' :"toyloq tumani1",
    "Toshkent shahar": "Toshkent shahar1",
    "Bektemir": "Bektemir tumani1",
    "Mirzo Ulug‘bek": "Mirzo Ulug'bek tumani1",
    "Mirobod tumani": "Mirobod tumani1",
    "Olmazor tumani": "Olmazor tumani1",
    "Sirg‘ali tumani": "Sirg'ali tumani1",
    "Uchtepa tumani": "Uchtepa tumani1",
    "Chilonzor tumani": "Chilonzor tumani1",
    "Shayxontohur tumani": "Shayxontohur tumani1",
    "Yunusobod tumani": "Yunusobod tumani1",
    "Yakkasaroy tumani": "Yakkasaroy tumani1",
    "Yashnobod tumani": "Yashnobod tumani1",
   
"Nukus shahri":"Nukus shahar1",
"Amudaryo tumani":"Amudaryo tumani1",
"Beruniy tumani":"Beruniy tumani1",
"Kegeyli tumani":"Kegeyli tumani1",
"Qanliko‘l tumani":"Qanliko'l tumani1",
"Qorao‘zak tumani":"Qorao'zak tumani1",
"Qo‘ng‘irot tumani":"Qo'ng'irot tumani1",
"Mo‘ynoq tumani":"Mo'ynoq tumani1",
"Nukus tumani":"Nukus tumani1",
"Taxiatosh tumani":"Taxiatosh tumani1",
"Taxtako‘pir tumani":"Taxtako'prik tumani1",
"To‘rtko‘l tumani":"To'rtko'l tumani1",
"Xo‘jayli tumani":"Xo'jayli tumani1",
"Chimboy tumani":"Chimboy tumani1",
"Sho‘manoy tumani":"Sho'manoy tumani1",
"Ellikqal’a tumani":"Ellikqal'a tumani1",

}







an = {
    "Andijon shahar": "andijon shaxar1",
    "Andijon tuman": "andijon tuman1",
    "Xonabod shahar": "xonabod shahar1",
    "Ulug'nor":"ulug'nor tuman1",
    "Asaka":"asaka tuman1",
    "Baliqchi":"baliqchi tuman1",
    "Bo'ston ":"bo'ston tuman1",
    "Buloqbosh":"buloqboshi tuman1",
    "Izboskan":"izboskan tuman1",
    "Jalaquduq":"jalaquduq tuman1",
    "Xoʻjaobod":"xo'jabod tuman1",
    "Qoʻrgʻontepa":"qo'rg'ontepa tuman1",
    "Marhamat":"marhamat tuman1",
    "Oltinkoʻl":"oltinko'l tuman1",
    "Paxtaobod":"paxtaobod tuman1",
    "Shahrixon":"shaxrixon tuman1",
}
andijon_yol_1 = InlineKeyboardMarkup(row_width=3)
for key,value in an.items():
    andijon_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))

andijon_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
andijon_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

namangan_y2 = {
    "Namangan shahar": "namangan shahar1",
    "Namangan tuman": "namangan tumani1",
    "Chortoq":"chortoq tumani1",
    "Chust ":"chust tumani1",
    "Kosonsoy ":"kosonsoy tumani1",
    "Mingbuloq":"mingbuloq tumani1",
    "Norin":"norin tumani1",
    "Pop ":"pop tumani1",
    "To'raqo'rg'on":"toraqo'rg'on tumani1",
    "Uchqo'rg'on":"uchqo'rgo'n tumani1",
    "Uychi":"uychi tumani1",
    "Yangiqo'rg'on":"yangi qo'rg'on tumani1",
    "Yangi Namangan":"yangi namangan tumani1",

}

namangan_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in namangan_y2.items():
    namangan_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
namangan_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

fargona_y2 = {
"Fargʻona shaxar" :"farg'ona shahar1",
"Fargʻona tuman1" :"farg'ona tuman1",
"Qo'qon shahar":"qo'qon shahar1",
"Quvasoy shahar":"quvasoy shahar1",
"Marg'ilon shahar":"marg'ilon shahar1",
"Oltiariq":"oltiariq tuman1",
"Bagʻdod ":"bog'dod tuman1",
"Beshariq ":"beshariq tuman1",
"Buvayda" :"buvayda tuman1",
"Dangʻara" :"dangara tuman1",
"Furqat" :"furqat tuman1",
"Qoʻshtepa":"qo'shtepa tuman1",
"Quva" :"quva tuman1",
"Rishton":"rishton tuman1",
"Soʻx" :"sox tuman1",
"Toshloq":"toshloq tuman1",
"Oʻzbekiston":"o'zbekiston tuman1",
"Uchkoʻprik" :"uchko'prik tuman1",
"Yozyovon" :"yozyovon tuman1",

}

fargona_yol_1 = InlineKeyboardMarkup(row_width=2)
for key, value in fargona_y2.items():
    fargona_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
fargona_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))
buxoro_y = {
"Buxoro shahri" :"buxoro shaxar1",
"Buxoro tuman1" :"buxoro tuman1",
"Kogon shahar" :"kogon shahar1",
"Kogon tuman" :"kogon tuman1",
"Olot" :"olot tuman1",
"Gʻijduvon" :"g'ijduvon tuman1",
"Jondor" :"jondor tuman1",
"Qorakoʻl" :"qorako'l tuman1",
"Qorovulbozor" : "qorovulbozor tuman1",
"Peshku" :"peshku tuman1",
"Romitan" :"romitan tuman1",
"Shofirkon" :"shofirkon tuman1",
"Vobkent" :"vobkent tuman1",

}

buxoro_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in buxoro_y.items():
    buxoro_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
buxoro_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

toshkent_y = {
    "Toshkent tuman": "toshkent tuman1",
    "Angren shahar": "angren shahar1",
    "Bekobod shahar": "bekobod shahar1",
    "Nurafshon shahar": "nurafshon shahar1",
    "Omaliq shahar": "olmaliq shahar1",
    "Ohangaron shahar": "ohangaron shahar1",
    "Chirchiq shahar": "chirchiq shahar1",
    "Yangiyo'l shahar": "yangiyo'l shahar1",
    "Bekobod": "bekobod tumani1",
    "Boʻstonliq": "bostonliq tumani1",
    "Boʻka": "boka tumani1",
    "Chinoz": "chinoz tumani1",
    "Qibray": "qibray tumani1",
    "Ohangaron": "ohangaron tumani1",
    "Oqqoʻrgʻon": "oqqorgon tumani1",
    "Parkent": "parkent tumani1",
    "Piskent": "piskent tumani1",
    "Quyi Chirchiq": "quyichirchiq tumani1",
    "Oʻrta Chirchiq": "ortachirchiq tumani1",
    "Yangiyoʻl": "yangiyol tumani1",
    "Yuqori Chirchiq": "yuqorichirchiq tumani1",
    "Zangiota": "zangiota tumani1",
    "Qo'yliq": "qoyliq1",
}

toshkent_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in toshkent_y.items():
    toshkent_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
toshkent_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

sirdaryo_y = {
"Sirdaryo shahar" :"sirdaryo shahar1",
"Sirdaryo tuman" :"sirdaryo tumani1",
"Guliston shahar" :"guliston shahar1",
"Yangiyer shahar" :"yangiyer shahar1",
"Shirin shahar" :"shirin shahar1",
"Oqoltin" :"oqoltin tumani1",
"Boyovut" :"boyovut tumani1" ,
"Guliston" :"guliston tumani1",
"Xovos" : "xovos tumani1",
"Mirzaobod" : "mirzaobod tumani1",
"Sardoba" :"sardoba tumani1",
"Sayxunobod" :"sayxunobod tumani1",

}


sirdaryo_yol_1 = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y.items():
    sirdaryo_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
sirdaryo_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

surxondaryo_y = {
"Termiz shahar":"termiz shahar1",
"Termiz tuman":"termiz tumani1",
"Angor":"angor tumani1",
"Bandixon":"bandixon tumani1",
"Boysun":"boysun tumani1",
"Denov" :"denov tumani1",
"Jarqoʻrgʻon":"jarqorgon tumani1",
"Qiziriq":"qiziriq tumani1",
"Qumqoʻrgʻon":"qumqorgon tumani1",
"Muzrabod":"muzrabod tumani1",
"Oltinsoy":"oltinsoy tumani1",
"Sariosiyo":"sariosiyo tumani1",
"Sherobod":"sherobod tumani1",
"Shoʻrchi":"shorchi tumani1" ,
"Uzun":"uzun tumani1",

}
surxondaryo_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in surxondaryo_y.items():
    surxondaryo_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
surxondaryo_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))
qashqadaryo_y = {
"Qarshi shahar":"qarshi shahar1",
"Shahrisabz shahar":"shahrisabz shahar1",
"Dehqonobod":"dehqonobod tumani1",
"Kasbi":"kasbi tumani1",
"Kitob":"kitob tumani1",
"Koson":"koson tumani1",
"Koʻkdala":"kokdala tumani1",
"Mirishkor":"mirishkor tumani1",
"Muborak":"muborak tumani1",
"Nishon":"nishon tumani1",
"Qamashi":"qamashi tumani1" ,
"Yakkabogʻ" :"yakkabog tumani1",
"Gʻuzor":"guzor tumani1",
"Shahrisabz tuman":"shahrisabz tumani1",
"Qarshi tuman":"qarshi tuman1",
"Chiroqchi":"chiroqchi tumani1",

}
qashqadaryo_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in qashqadaryo_y.items():
    qashqadaryo_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
qashqadaryo_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))
xorazm_yol_1 = InlineKeyboardMarkup(row_width=2)
xorazm_y = {
"Xiva shahar" :"xiva shahar1",
"Urganch shahar" :"urganch shahar1",
"Bogʻot" :"bog'ot tumani1",
"Gurlan" :"gurlan tumani1",
"Xonqa" :"xonqa tumani1",
"Hazorasp" :"hazorasp tumani1",
"Xiva" :"xiva tumani1",
"Qoʻshkoʻpir" :"qoshko'prik tumani1",
"Shovot" :"shovot tumani1",
"Urganch" :"urganch tumani1",
"Yangiariq" :"yangiariq tumani1",
"Yangibozor" :"yangibozor tumani1",
"Tupproqqalʼa" :"tuproqqal'a tumani1",

}
for key,value in xorazm_y.items():
    xorazm_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
xorazm_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))

navoiy_y = {
"Navoiy shahar" :"navoiy shahar1",
"Zarafshon shahar" :"zarafshon shahar1",
"Konimex" :"konimex tumani1",
"Karmana" :"karmana tumani1",
"Qiziltepa" :"qiziltepa tumani1",
"Xatirchi" :"xatirchi tumani1",
"Navbahor" :"navbahor tumani1",
"Nurota" :"nurota tumani1",
"Tomdi" :"tomdi tumani1",
"Uchquduq" :"uchquduq tumani1",

}
navoiy_yol_1 = InlineKeyboardMarkup(row_width=2)
for key,value in navoiy_y.items():
    navoiy_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
navoiy_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))
jizzax_y = {
"Jizzax shahar" :"jizzax shahar1",
"Arnasoy" :"arnasoy tumani1",
"Baxmal" :"baxmal tumani1",
"Doʻstlik" :"do'stlik tumani1",
"Forish" :"forish tumani1",
"Gʻallaorol" :"g'allarol tumani1",
"Sharof Rashidov ":"sharof rashidov tumani1",
'Mirzachoʻl' :'mirzachol tumani1',
"Paxtakor" :"paxtakor tumani1",
"Yangiobod" :"yangi obod tumani1",
'Zomin' :"zomin tumani1",
'Zafarobod' :"zafarobod tumani1",
'Zarbdor' :"zarbdor tumani1",

}
jizzax_yol_1 = InlineKeyboardMarkup(row_width=2)
for key, value in jizzax_y.items():
    jizzax_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
jizzax_yol_1.insert(InlineKeyboardButton(text='Ortga',callback_data='kshkfheiiisuyruy'))
samarqaand_y = {
'Samarqand shaxar' :"samarqand shahar1",
'Kattaqoʻrgʻon shahar' :"kattaqorgon shahar1",
'Bulungʻur' :"bulungur tumani1",
'Ishtixon' :"ishtixon tumani1",
'Jomboy' :"jomboy tumani1",
'Kattaqoʻrgʻon tuman' :"kattaqorgon tumani1",
'Qoʻshrabot' :"qoshrabot tumani1",
'Narpay' :"narpay tumani1",
'Nurobod' :"nurobod tumani1",
'Oqdaryo' :"oqdaryo tumani1",
'Paxtachi' :"paxtachi tumani1",
'Payariq' :"payariq tumani1",
'Pastdargʻom' :"pastdargom tumani1",
'Samarqand tuman' :"samarqand tumani1",
'Toyloq' :"toyloq tumani1",

}
samarqand_yol_1 = InlineKeyboardMarkup(row_width=2)
for key, value in samarqaand_y.items():
    samarqand_yol_1.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yol_1.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
samarqand_yol_1.insert(InlineKeyboardButton(text='ortga',callback_data='kshkfheiiisuyruy'))
tshahar={
        "Toshkent shahar":"Toshkent shahar1",
        "Bektemir":"Bektemir tumani1",
        "Mirzo Ulug‘bek":"Mirzo Ulug'bek tumani1",
        "Mirobod tumani":"Mirobod tumani1",
        "Olmazor tumani":"Olmazor tumani1",
        "Sirg‘ali tumani":"Sirg'ali tumani1",
        "Uchtepa tumani":"Uchtepa tumani1",
        "Chilonzor tumani":"Chilonzor tumani1",
        "Shayxontohur tumani":"Shayxontohur tumani1",
        "Yunusobod tumani":"Yunusobod tumani1",
        "Yakkasaroy tumani":"Yakkasaroy tumani1",
        "Yashnobod tumani":"Yashnobod tumani1",
        "Ortga":"kshkfheiiisuyruy",
        "Bosh menu":"ogirilish",
         }
tosh_shsha_1=InlineKeyboardMarkup(row_width=2)
for key,value in tshahar.items():
    tosh_shsha_1.insert(InlineKeyboardButton(text=key,callback_data=value))
qoraqalpoq={
"Nukus shahri":"Nukus shahar1",
"Amudaryo tumani":"Amudaryo tumani1",
"Beruniy tumani":"Beruniy tumani1",
"Kegeyli tumani":"Kegeyli tumani1",
"Qanliko‘l tumani":"Qanliko'l tumani1",
"Qorao‘zak tumani":"Qorao'zak tumani1",
"Qo‘ng‘irot tumani":"Qo'ng'irot tumani1",
"Mo‘ynoq tumani":"Mo'ynoq tumani1",
"Nukus tumani":"Nukus tumani1",
"Taxiatosh tumani":"Taxiatosh tumani1",
"Taxtako‘pir tumani":"Taxtako'prik tumani1",
"To‘rtko‘l tumani":"To'rtko'l tumani1",
"Xo‘jayli tumani":"Xo'jayli tumani1",
"Chimboy tumani":"Chimboy tumani1",
"Sho‘manoy tumani":"Sho'manoy tumani1",
"Ellikqal’a tumani":"Ellikqal'a tumani1",
"Ortga":"kshkfheiiisuyruy",
"Bosh menu":"ogirilish",
}
qoraqalpogiston_yol_1 = InlineKeyboardMarkup()
for key,value in qoraqalpoq.items():
    qoraqalpogiston_yol_1.insert(InlineKeyboardButton(text=key,callback_data=value))











an2 = {
    "Andijon shahar": "andijon shaxar",
    "Andijon tuman": "andijon tuman",
    "Xonabod shahar": "xonabod shahar",
    "Ulug'nor":"ulug'nor tuman",
    "Asaka":"asaka tuman",
    "Baliqchi":"baliqchi tuman",
    "Bo'ston ":"bo'ston tuman",
    "Buloqbosh":"buloqboshi tuman",
    "Izboskan":"izboskan tuman",
    "Jalaquduq":"jalaquduq tuman",
    "Xoʻjaobod":"xo'jabod tuman",
    "Qoʻrgʻontepa":"qo'rg'ontepa tuman",
    "Marhamat":"marhamat tuman",
    "Oltinkoʻl":"oltinko'l tuman",
    "Paxtaobod":"paxtaobod tuman",
    "Shahrixon":"shaxrixon tuman",
}
andijon_yol_2 = InlineKeyboardMarkup(row_width=3)
for key,value in an2.items():
    andijon_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))

andijon_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
andijon_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

namangan_y2 = {
    "Namangan shahar": "namangan shahar",
    "Namangan tuman": "namangan tumani",
    "Chortoq":"chortoq tumani",
    "Chust ":"chust tumani",
    "Kosonsoy ":"kosonsoy tumani",
    "Mingbuloq":"mingbuloq tumani",
    "Norin":"norin tumani",
    "Pop ":"pop tumani",
    "To'raqo'rg'on":"toraqo'rg'on tumani",
    "Uchqo'rg'on":"uchqo'rgo'n tumani",
    "Uychi":"uychi tumani",
    "Yangiqo'rg'on":"yangi qo'rg'on tumani",
    "Yangi Namangan":"yangi namangan tumani",

}

namangan_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in namangan_y2.items():
    namangan_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))

namangan_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
namangan_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

fargona_y2 = {
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

fargona_yol_2 = InlineKeyboardMarkup(row_width=2)
for key, value in fargona_y2.items():
    fargona_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))

fargona_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
fargona_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))
buxoro_y = {
"Buxoro shahri" :"buxoro shaxar",
"Buxoro tuman" :"buxoro tuman",
"Kogon shahar" :"kogon shahar",
"Kogon tuman" :"kogon tuman",
"Olot" :"olot tuman",
"Gʻijduvon" :"g'ijduvon tuman",
"Jondor" :"jondor tuman",
"Qorakoʻl" :"qorako'l tuman",
"Qorovulbozor" : "qorovulbozor tuman",
"Peshku" :"peshku tuman",
"Romitan" :"romitan tuman",
"Shofirkon" :"shofirkon tuman",
"Vobkent" :"vobkent tuman",

}

buxoro_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in buxoro_y.items():
    buxoro_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
buxoro_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
buxoro_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

toshkent_y = {
    "Toshkent tuman":"toshkent tuman",
    "Angren shahar":"angren shahar",
    "Bekobod shahar":"bekobod shahar",
    "Nurafshon shahar":"nurafshon shahar",
    "Omaliq shahar":"olmaliq shahar",
    "Ohangaron shahar":"ohangaron shahar",
    "Chirchiq shahar":"chirchiq shahar",
    "Yangiyo'l shahar":"yangiyo'l shahar",
    "Bekobod":"bekobod tumani",
    "Boʻstonliq":"bostonliq tumani",
    "Boʻka":"boka tumani",
    "Chinoz":"chinoz tumani",
    "Qibray":"qibray tumani",
    "Ohangaron":"ohangaron tumani",
    "Oqqoʻrgʻon":"oqqorgon tumani",
    "Parkent":"parkent tumani",
    "Piskent":"piskent tumani",
    "Quyi Chirchiq":"quyichirchiq tumani",
    "Oʻrta Chirchiq":"ortachirchiq tumani",
    "Yangiyoʻl":"yangiyol tumani",
    "Yuqori Chirchiq":"yuqorichirchiq tumani",
    "Zangiota":"zangiota tumani",
    "Qo'yliq":"qoyliq",

}

toshkent_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in toshkent_y.items():
    toshkent_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
toshkent_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
toshkent_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

sirdaryo_y = {
"Sirdaryo shahar" :"sirdaryo shahar",
"Sirdaryo tuman" :"sirdaryo tumani",
"Guliston shahar" :"guliston shahar",
"Yangiyer shahar" :"yangiyer shahar",
"Shirin shahar" :"shirin shahar",
"Oqoltin" :"oqoltin tumani",
"Boyovut" :"boyovut tumani" ,
"Guliston" :"guliston tumani",
"Xovos" : "xovos tumani",
"Mirzaobod" : "mirzaobod tumani",
"Sardoba" :"sardoba tumani",
"Sayxunobod" :"sayxunobod tumani",

}


sirdaryo_yol_2 = InlineKeyboardMarkup(row_width=4)
for key,value in sirdaryo_y.items():
    sirdaryo_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
sirdaryo_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
sirdaryo_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

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
surxondaryo_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in surxondaryo_y.items():
    surxondaryo_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
surxondaryo_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
surxondaryo_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))
qashqadaryo_y = {
"Qarshi shahar":"qarshi shahar",
"Shahrisabz shahar":"shahrisabz shahar",
"Dehqonobod":"dehqonobod tumani",
"Kasbi":"kasbi tumani",
"Kitob":"kitob tumani",
"Koson":"koson tumani",
"Koʻkdala":"kokdala tumani",
"Mirishkor":"mirishkor tumani",
"Muborak":"muborak tumani",
"Nishon":"nishon tumani",
"Qamashi":"qamashi tumani" ,
"Yakkabogʻ" :"yakkabog tumani",
"Gʻuzor":"guzor tumani",
"Shahrisabz tuman":"shahrisabz tumani",
"Qarshi tuman":"qarshi tuman",
"Chiroqchi":"chiroqchi tumani",

}
qashqadaryo_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in qashqadaryo_y.items():
    qashqadaryo_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
qashqadaryo_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
qashqadaryo_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))
xorazm_yol_2 = InlineKeyboardMarkup(row_width=2)
xorazm_y = {
"Xiva shahar" :"xiva shahar",
"Urganch shahar" :"urganch shahar",
"Bogʻot" :"bog'ot tumani",
"Gurlan" :"gurlan tumani",
"Xonqa" :"xonqa tumani",
"Hazorasp" :"hazorasp tumani",
"Xiva" :"xiva tumani",
"Qoʻshkoʻpir" :"qoshko'prik tumani",
"Shovot" :"shovot tumani",
"Urganch" :"urganch tumani",
"Yangiariq" :"yangiariq tumani",
"Yangibozor" :"yangibozor tumani",
"Tupproqqalʼa" :"tuproqqal'a tumani",

}
for key,value in xorazm_y.items():
    xorazm_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
xorazm_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
xorazm_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))

navoiy_y = {
"Navoiy shahar" :"navoiy shahar",
"Zarafshon shahar" :"zarafshon shahar",
"Konimex" :"konimex tumani",
"Karmana" :"karmana tumani",
"Qiziltepa" :"qiziltepa tumani",
"Xatirchi" :"xatirchi tumani",
"Navbahor" :"navbahor tumani",
"Nurota" :"nurota tumani",
"Tomdi" :"tomdi tumani",
"Uchquduq" :"uchquduq tumani",

}
navoiy_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in navoiy_y.items():
    navoiy_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
navoiy_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
navoiy_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))
jizzax_y = {
"Jizzax shahar" :"jizzax shahar",
"Arnasoy" :"arnasoy tumani",
"Baxmal" :"baxmal tumani",
"Doʻstlik" :"do'stlik tumani",
"Forish" :"forish tumani",
"Gʻallaorol" :"g'allarol tumani",
"Sharof Rashidov ":"sharof rashidov tumani",
'Mirzachoʻl' :'mirzachol tumani',
"Paxtakor" :"paxtakor tumani",
"Yangiobod" :"yangi obod tumani",
'Zomin' :"zomin tumani",
'Zafarobod' :"zafarobod tumani",
'Zarbdor' :"zarbdor tumani",

}
jizzax_yol_2 = InlineKeyboardMarkup(row_width=2)
for key, value in jizzax_y.items():
    jizzax_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
jizzax_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
jizzax_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='ksjhfksdhfkshfk'))
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
samarqand_yol_2 = InlineKeyboardMarkup(row_width=2)
for key, value in samarqaand_y.items():
    samarqand_yol_2.insert(InlineKeyboardButton(text=key, callback_data=value))
samarqand_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
samarqand_yol_2.insert(InlineKeyboardButton(text='ortga',callback_data='ksjhfksdhfkshfk'))
tshahar={
        "Toshkent shahar":"Toshkent shahar",
        "Bektemir":"Bektemir tumani",
        "Mirzo Ulug‘bek":"Mirzo Ulug'bek tumani",
        "Mirobod tumani":"Mirobod tumani",
        "Olmazor tumani":"Olmazor tumani",
        "Sirg‘ali tumani":"Sirg'ali tumani",
        "Uchtepa tumani":"Uchtepa tumani",
        "Chilonzor tumani":"Chilonzor tumani",
        "Shayxontohur tumani":"Shayxontohur tumani",
        "Yunusobod tumani":"Yunusobod tumani",
        "Yakkasaroy tumani":"Yakkasaroy tumani",
        "Yashnobod tumani":"Yashnobod tumani",
        "Ortga":"ksjhfksdhfkshfk",
        "Bosh menu":"ogirilish",
         }
tosh_shsha_2=InlineKeyboardMarkup(row_width=2)
for key,value in tshahar.items():
    tosh_shsha_2.insert(InlineKeyboardButton(text=key,callback_data=value))
qoraqalpoq={
"Nukus shahri":"Nukus shahar",
"Amudaryo tumani":"Amudaryo tumani",
"Beruniy tumani":"Beruniy tumani",
"Kegeyli tumani":"Kegeyli tumani",
"Qanliko‘l tumani":"Qanliko'l tumani",
"Qorao‘zak tumani":"Qorao'zak tumani",
"Qo‘ng‘irot tumani":"Qo'ng'irot tumani",
"Mo‘ynoq tumani":"Mo'ynoq tumani",
"Nukus tumani":"Nukus tumani",
"Taxiatosh tumani":"Taxiatosh tumani",
"Taxtako‘pir tumani":"Taxtako'prik tumani",
"To‘rtko‘l tumani":"To'rtko'l tumani",
"Xo‘jayli tumani":"Xo'jayli tumani",
"Chimboy tumani":"Chimboy tumani",
"Sho‘manoy tumani":"Sho'manoy tumani",
"Ellikqal’a tumani":"Ellikqal'a tumani",
"Ortga":"ksjhfksdhfkshfk",
"Bosh menu":"ogirilish",
}
qoraqalpogiston_yol_2 = InlineKeyboardMarkup()
for key,value in qoraqalpoq.items():
    qoraqalpogiston_yol_2.insert(InlineKeyboardButton(text=key,callback_data=value))



viloyat = {
    "Andijon":"andijon",
    "Namangan":"namangan",
    "Farg'ona":"farg'ona",
    "Buxoro":"buxoro",
    "Toshkent":"toshkent",
    "Sirdaryo":"sirdaryo",
    "Surxondaryo":"surxondaryo",
    "Qashqadaryo":"qashqadaryo",
    "Xorazm":"xorazm",
    "Navoiy":"navoiy",
    "Jizzax":"jizzax",
    "Samarqand":"samarqand",
    "Toshkent shahar":"kent shahar",
    "Qoraqalpog'iston":"qoraqalpoq",
}

viloyatlar_yol_2 = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    viloyatlar_yol_2.insert(InlineKeyboardButton(text=key, callback_data=key))

viloyatlar_yol_2.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
viloyatlar_yol_2.insert(InlineKeyboardButton(text='Ortga',callback_data='askskhdkshdkfhs'))





viloyat1 = {
    "Andijon":"1andijon",
    "Namangan":"1namangan",
    "Farg'ona":"1farg'ona",
    "Buxoro":"1buxoro",
    "Toshkent":"1toshkent",
    "Sirdaryo":"1sirdaryo",
    "Surxondaryo":"1surxondaryo",
    "Qashqadaryo":"1qashqadaryo",
    "Xorazm":"1xorazm",
    "Navoiy":"1navoiy",
    "Jizzax":"1jizzax",
    "Samarqand":"1samarqand",
    "Toshkent shahar":"1kent shahar",
    "Qoraqalpog'iston":"1qoraqalpoq",
}

viloyatlar_yol_21 = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat1.items():
    viloyatlar_yol_21.insert(InlineKeyboardButton(text=key, callback_data=value))

viloyatlar_yol_21.insert(InlineKeyboardButton(text='Bosh menu',callback_data='ogirilish'))
viloyatlar_yol_21.insert(InlineKeyboardButton(text='Ortga',callback_data='askskhdwkdhkjdsdkshdkfhs'))