import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.andtuman import andijon_yuuk_mashina
from keyboards.inline.yolovchi.buxtuman import buxoro_yuuk_mashina
from keyboards.inline.yolovchi.fartuman import fargona_yuuk_mashina
from keyboards.inline.yolovchi.jizztuman import jizzax_yuuk_mashina
from keyboards.inline.yolovchi.namtuman import namangan_yuuk_mashina
from keyboards.inline.yolovchi.navoiytuman import navoiy_yuuk_mashina
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_yuuk_mashina
from keyboards.inline.yolovchi.samartuman import samarqand_yuuk_mashina
from keyboards.inline.yolovchi.sirtuman import sirdaryo_yuuk_mashina
from keyboards.inline.yolovchi.surtuman import surxondaryo_yuuk_mashina
from keyboards.inline.yolovchi.toshtuman import toshkent_yuuk_mashina
from keyboards.inline.yolovchi.viloyatlar import  viloyat_t, viloyatlar_yol_t
from keyboards.inline.yolovchi.xorazmtuman import xorazm_yuuk_mashina
from loader import dp, db




@dp.callback_query_handler(text="track_choose")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga boradigan yuk mashinasi kerak ? ",reply_markup=viloyatlar_yol_t)

yuk_mashina = {
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
    "Chortoq": "mashin_chortoq",
    "Chust ": "mashin_chust",
    "Kosonsoy ": "mashin_kosonsoy",
    "Mingbuloq": "mashin_mingbuloq",
    "Namangan ": "mashin_namshaxar",
    "Norin": "mashin_norin",
    "Pop ": "mashin_pop",
    "To'raqo'rg'on": "mashin_toraqo'rg'on",
    "Uchqo'rg'on": "mashin_uchqo'rgo'n",
    "Uychi": "mashin_uychi",
    "Yangiqo'rg'on": "mashin_yangiqor",
    "Davlatobod ": "mashin_davlatobod",
    "Yangi Namangan": "mashin_yangi namangan",
    "Oqoltin" :"mashin_oqoltin",
    "Boyovut" :"mashin_boyovut" ,
    "Guliston" :"mashin_guliston",
    "Xovos" : "mashin_xovos",
    "Mirzaobod" : "mashin_mirzaobod",
    "Sardoba" :"mashin_sardoba",
    "Sayxunobod" :"mashin_sayxunobod",
    "Sirdaryo" :"mashin_shaxri",
    "Bekobod": "mashin_bekobod",
    "Boʻstonliq": "mashin_bostonliq",
    "Boʻka": "mashin_boka",
    "Chinoz": "mashin_chinoz",
    "Qibray": "mashin_qibray",
    "Ohangaron": "mashin_ohangaron",
    "Oqqoʻrgʻon": "mashin_oqqorgon",
    "Parkent": "mashin_parkent",
    "Piskent": "mashin_piskent",
    "Quyi Chirchiq": "mashin_quyichirchiq",
    "Oʻrta Chirchiq": "mashin_ortachirchiq",
    "Yangiyoʻl": "mashin_yangiyol",
    "Yuqori Chirchiq": "mashin_yuqorichirchiq",
    "Zangiota": "mashin_zangiota",
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
    "Konimex" :"mashin_konimex",
    "Karmana" :"mashin_karmana",
    "Qiziltepa" :"mashin_qiziltepa",
    "Xatirchi" :"mashin_xatirchi",
    "Navbahor" :"mashin_navbahor",
    "Nurota" :"mashin_nurota",
    "Tomdi" :"mashin_tomdi",
    "Uchquduq" :"mashin_uchquduq",
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
for key,value in yuk_mashina.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="yukbet_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="getit"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="track_choose"))
        orders = await db.select_tayyor_yuk_haydovchi()
        print(orders)
        buyurtma = []
        for i in orders:
            if i[0]==call.data[7:]:
                if i[1] and [2] is not None:
                    lis=[]
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer(" Bu tumanda ayni paytdda tayyor yuk mashinasi mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="yukbet_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"yukbet_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="sugurib_olish"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="track_choose"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sasasddd":buyurtma[curr_page]})


@dp.callback_query_handler(text="sugurib_olish")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sasasddd")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="getit")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])


for key,value in viloyat_t.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_yuk_haydovchi()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="sadsdasdasd_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="jonatish"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="yuk_filt_off"))
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
            await call.message.answer("Bu tumanda ayni paytdda tayyor yuk mashinasi mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data[7:],"viloyatga":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text="jonatish")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_1")
            await call.message.answer(buyurtma[0][1])
@dp.callback_query_handler(text_contains="sadsdasdasd_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sadsdasdasd_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="sddfsfererfw"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="yuk_filt_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sdasasasada65656":buyurtma[curr_page]})

@dp.callback_query_handler(text="sddfsfererfw")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sdasasasada65656")
            await call.message.answer(buyurtma[1])

ss={
    "sjduuwgfuwgdkgjda": andijon_yuuk_mashina,
    "akilwyiwefsdjksd": namangan_yuuk_mashina,
    "kdjhaigdakhdksa": fargona_yuuk_mashina,
    "allaskalkdaslkjd": buxoro_yuuk_mashina,
    "euywiudhkns":toshkent_yuuk_mashina ,
    "jweytfugdiahjash": sirdaryo_yuuk_mashina,
    "qdwqwdqwsasxa": surxondaryo_yuuk_mashina,
    "asasdsadasd": qashqadaryo_yuuk_mashina,
    "dfdsfdsgfdsfgfd": xorazm_yuuk_mashina,
    "fghgfjghjgfh": navoiy_yuuk_mashina,
    "reggfvdvdvcx": jizzax_yuuk_mashina,
    "tyhjyjghfh": samarqand_yuuk_mashina,
}
@dp.callback_query_handler(text="yuk_filt_off")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="shakl_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"shakl_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="asiausiusiuas"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"5as5a4s654a":buyurtma[curr_page]})


@dp.callback_query_handler(text="asiausiusiuas")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("5as5a4s654a")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="xzhgxhzxhgzx")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="mash_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_yuk_haydovchi()
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="shakl_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="xzhgxhzxhgzx"))
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
                if i[1] and [2] is not None:
                    print(i[4])
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
    if len(buyurtma) == 0:
        await call.message.answer("Bu tumanda ayni paytdda tayyor yuk mashinasi mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)









