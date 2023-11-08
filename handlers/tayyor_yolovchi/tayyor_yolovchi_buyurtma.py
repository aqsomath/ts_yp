import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.tayyor_buyurtmalar.tayyor_yolovchi_tugmalar import (
    andijon_yolo,buxoro_yolo,fargona_yolo,jizzax_yolota,namangan_yolo,
    navoiy_yolota,qashqadaryo_yolo,samarqand_yolota,sirdaryo_yolo,
    surxondaryo_yolo,toshkent_yolo,xorazm_yolo
)

from keyboards.inline.yolovchi.viloyatlar import viloyat_a, viloyatlar_yol_a
from loader import dp, db




@dp.callback_query_handler(text="chertib_olish")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga bormoqchisiz ? ",reply_markup=viloyatlar_yol_a)

yolovchi = {
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
    "Chortoq": "yolovc_chortoq",
    "Chust ": "yolovc_chust",
    "Kosonsoy ": "yolovc_kosonsoy",
    "Mingbuloq": "yolovc_mingbuloq",
    "Namangan ": "yolovc_namshaxar",
    "Norin": "yolovc_norin",
    "Pop ": "yolovc_pop",
    "To'raqo'rg'on": "yolovc_toraqo'rg'on",
    "Uchqo'rg'on": "yolovc_uchqo'rgo'n",
    "Uychi": "yolovc_uychi",
    "Yangiqo'rg'on": "yolovc_yangiqor",
    "Davlatobod ": "yolovc_davlatobod",
    "Yangi Namangan": "yolovc_yangi namangan",
    "Oqoltin" :"yolovc_oqoltin",
    "Boyovut" :"yolovc_boyovut" ,
    "Guliston" :"yolovc_guliston",
    "Xovos" : "yolovc_xovos",
    "Mirzaobod" : "yolovc_mirzaobod",
    "Sardoba" :"yolovc_sardoba",
    "Sayxunobod" :"yolovc_sayxunobod",
    "Sirdaryo" :"yolovc_shaxri",
    "Bekobod": "yolovc_bekobod",
    "Boʻstonliq": "yolovc_bostonliq",
    "Boʻka": "yolovc_boka",
    "Chinoz": "yolovc_chinoz",
    "Qibray": "yolovc_qibray",
    "Ohangaron": "yolovc_ohangaron",
    "Oqqoʻrgʻon": "yolovc_oqqorgon",
    "Parkent": "yolovc_parkent",
    "Piskent": "yolovc_piskent",
    "Quyi Chirchiq": "yolovc_quyichirchiq",
    "Oʻrta Chirchiq": "yolovc_ortachirchiq",
    "Yangiyoʻl": "yolovc_yangiyol",
    "Yuqori Chirchiq": "yolovc_yuqorichirchiq",
    "Zangiota": "yolovc_zangiota",
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
    "Konimex" :"yolovc_konimex",
    "Karmana" :"yolovc_karmana",
    "Qiziltepa" :"yolovc_qiziltepa",
    "Xatirchi" :"yolovc_xatirchi",
    "Navbahor" :"yolovc_navbahor",
    "Nurota" :"yolovc_nurota",
    "Tomdi" :"yolovc_tomdi",
    "Uchquduq" :"yolovc_uchquduq",
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
for key,value in yolovchi.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="bashara_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="tortibolish"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="chertib_olish"))
        orders = await db.select_tayyor_yolovchi()
        buyurtma = []
        for i in orders:
            if i[0]==call.data[7:]:
                lis=[]
                lis.append(i[1])
                lis.append(i[2])
                buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor yo'lovchi mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="bashara_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"bashara_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="download"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="chertib_olish"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="download")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaaxax")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="tortibolish")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])


for key,value in viloyat_a.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_yolovchi()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="sled_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="filtsec"))
        buyurtma = []
        data = await state.get_data()
        tuman=data.get("tuman")
        for i in orders:
            if i[3] == call.data[7:] and i[0]==tuman:
                if i[1] and [2] is not None:
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma) == 0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor yo'lovchi mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data[7:],"viloyatga":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)


@dp.callback_query_handler(text_contains="sled_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sled_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="shdgsdsdsduyf"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="filtsec"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sdsasasada65656":buyurtma[curr_page]})

@dp.callback_query_handler(text="shdgsdsdsduyf")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sdsasasada65656")
            await call.message.answer(buyurtma[1])

ss={
    "x_sjduuwgfuwgdkgjda": andijon_yolo,
    "x_akilwyiwefsdjksd": namangan_yolo,
    "x_kdjhaigdakhdksa": fargona_yolo,
    "x_allaskalkdaslkjd": buxoro_yolo,
    "x_euywiudhkns":toshkent_yolo ,
    "x_jweytfugdiahjash": sirdaryo_yolo,
    "x_qdwqwdqwsasxa": surxondaryo_yolo,
    "x_asasdsadasd": qashqadaryo_yolo,
    "x_dfdsfdsgfdsfgfd": xorazm_yolo,
    "x_fghgfjghjgfh": navoiy_yolota,
    "x_reggfvdvdvcx": jizzax_yolota,
    "x_tyhjyjghfh": samarqand_yolota,
}
@dp.callback_query_handler(text="filtsec")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key[2:]:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="qswae_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"qswae_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="ajgajsasg"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"6as4d6as4d65as6d4":buyurtma[curr_page]})


@dp.callback_query_handler(text="ajgajsasg")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("6as4d6as4d65as6d4")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="dsasassdl")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="yolo_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_yolovchi()
    print(orders)
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="qswae_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="dsasassdl"))
    buyurtma = []
    data = await state.get_data()
    tuman=data.get("tuman")
    viloyatiga=data.get("viloyatga")
    for i in orders:
        if i[0] == tuman:
            print(i[0])
            if i[3]==viloyatiga:
             print(i[3])
             if i[4]==call.data[5:].capitalize():
                print(i[4])
                lis = []
                lis.append(i[1])
                lis.append(i[2])
                buyurtma.append(lis)
    if len(buyurtma) == 0:
        await call.message.answer(" Bu tumanda ayni paytdda tayyor yo'lovchi mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)









