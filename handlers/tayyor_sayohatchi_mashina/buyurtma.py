import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp, db





yolovchi = {
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
    "Chortoq": "massay_chortoq",
    "Chust ": "massay_chust",
    "Kosonsoy ": "massay_kosonsoy",
    "Mingbuloq": "massay_mingbuloq",
    "Namangan ": "massay_namshaxar",
    "Norin": "massay_norin",
    "Pop ": "massay_pop",
    "To'raqo'rg'on": "massay_toraqo'rg'on",
    "Uchqo'rg'on": "massay_uchqo'rgo'n",
    "Uychi": "massay_uychi",
    "Yangiqo'rg'on": "massay_yangiqor",
    "Davlatobod ": "massay_davlatobod",
    "Yangi Namangan": "massay_yangi namangan",
    "Oqoltin" :"massay_oqoltin",
    "Boyovut" :"massay_boyovut" ,
    "Guliston" :"massay_guliston",
    "Xovos" : "massay_xovos",
    "Mirzaobod" : "massay_mirzaobod",
    "Sardoba" :"massay_sardoba",
    "Sayxunobod" :"massay_sayxunobod",
    "Sirdaryo" :"massay_shaxri",
    "Bekobod": "massay_bekobod",
    "Boʻstonliq": "massay_bostonliq",
    "Boʻka": "massay_boka",
    "Chinoz": "massay_chinoz",
    "Qibray": "massay_qibray",
    "Ohangaron": "massay_ohangaron",
    "Oqqoʻrgʻon": "massay_oqqorgon",
    "Parkent": "massay_parkent",
    "Piskent": "massay_piskent",
    "Quyi Chirchiq": "massay_quyichirchiq",
    "Oʻrta Chirchiq": "massay_ortachirchiq",
    "Yangiyoʻl": "massay_yangiyol",
    "Yuqori Chirchiq": "massay_yuqorichirchiq",
    "Zangiota": "massay_zangiota",
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
    "Konimex" :"massay_konimex",
    "Karmana" :"massay_karmana",
    "Qiziltepa" :"massay_qiziltepa",
    "Xatirchi" :"massay_xatirchi",
    "Navbahor" :"massay_navbahor",
    "Nurota" :"massay_nurota",
    "Tomdi" :"massay_tomdi",
    "Uchquduq" :"massay_uchquduq",
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
for key,value in yolovchi.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="michael_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="alala"))
        orders = await db.select_tayyor_sayohatchi_mashina()
        buyurtma = []
        for i in orders:
            if i[0]==call.data[7:]:
                if i[1] and [2] is not None:
                    lis=[]
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor sayohatchi mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)
@dp.callback_query_handler(text="alala")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="michael_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"michael_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="sdcscccdef"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="sdcscccdef")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaaxax")
            await call.message.answer(buyurtma[1])




