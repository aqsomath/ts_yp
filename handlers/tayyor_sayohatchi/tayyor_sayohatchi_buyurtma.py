import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp, db





yolovchi = {
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
    "Chortoq": "sayyoh_chortoq",
    "Chust ": "sayyoh_chust",
    "Kosonsoy ": "sayyoh_kosonsoy",
    "Mingbuloq": "sayyoh_mingbuloq",
    "Namangan ": "sayyoh_namshaxar",
    "Norin": "sayyoh_norin",
    "Pop ": "sayyoh_pop",
    "To'raqo'rg'on": "sayyoh_toraqo'rg'on",
    "Uchqo'rg'on": "sayyoh_uchqo'rgo'n",
    "Uychi": "sayyoh_uychi",
    "Yangiqo'rg'on": "sayyoh_yangiqor",
    "Davlatobod ": "sayyoh_davlatobod",
    "Yangi Namangan": "sayyoh_yangi namangan",
    "Oqoltin" :"sayyoh_oqoltin",
    "Boyovut" :"sayyoh_boyovut" ,
    "Guliston" :"sayyoh_guliston",
    "Xovos" : "sayyoh_xovos",
    "Mirzaobod" : "sayyoh_mirzaobod",
    "Sardoba" :"sayyoh_sardoba",
    "Sayxunobod" :"sayyoh_sayxunobod",
    "Sirdaryo" :"sayyoh_shaxri",
    "Bekobod": "sayyoh_bekobod",
    "Boʻstonliq": "sayyoh_bostonliq",
    "Boʻka": "sayyoh_boka",
    "Chinoz": "sayyoh_chinoz",
    "Qibray": "sayyoh_qibray",
    "Ohangaron": "sayyoh_ohangaron",
    "Oqqoʻrgʻon": "sayyoh_oqqorgon",
    "Parkent": "sayyoh_parkent",
    "Piskent": "sayyoh_piskent",
    "Quyi Chirchiq": "sayyoh_quyichirchiq",
    "Oʻrta Chirchiq": "sayyoh_ortachirchiq",
    "Yangiyoʻl": "sayyoh_yangiyol",
    "Yuqori Chirchiq": "sayyoh_yuqorichirchiq",
    "Zangiota": "sayyoh_zangiota",
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
    "Konimex" :"sayyoh_konimex",
    "Karmana" :"sayyoh_karmana",
    "Qiziltepa" :"sayyoh_qiziltepa",
    "Xatirchi" :"sayyoh_xatirchi",
    "Navbahor" :"sayyoh_navbahor",
    "Nurota" :"sayyoh_nurota",
    "Tomdi" :"sayyoh_tomdi",
    "Uchquduq" :"sayyoh_uchquduq",
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
for key,value in yolovchi.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="sharshara_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="suqubolish"))
        orders = await db.select_tayyor_sayohatchi()
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
@dp.callback_query_handler(text="suqubolish")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="sharshara_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sharshara_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="ffkkkdjk"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="ffkkkdjk")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaaxax")
            await call.message.answer(buyurtma[1])




