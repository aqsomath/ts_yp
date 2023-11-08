import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.andtuman import andijon_x, andijon_pochta
from keyboards.inline.yolovchi.buxtuman import buxoro_x, buxoro_pochta
from keyboards.inline.yolovchi.fartuman import fargona_x, fargona_pochta
from keyboards.inline.yolovchi.jizztuman import jizzax_x, jizzax_pochta
from keyboards.inline.yolovchi.namtuman import namangan_x, namangan_pochta
from keyboards.inline.yolovchi.navoiytuman import navoiy_x, navoiy_pochta
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_x, qashqadaryo_pochta
from keyboards.inline.yolovchi.samartuman import samarqand_x, samarqand_pochta
from keyboards.inline.yolovchi.sirtuman import sirdaryo_x, sirdaryo_pochta
from keyboards.inline.yolovchi.surtuman import surxondaryo_x, surxondaryo_pochta
from keyboards.inline.yolovchi.toshtuman import toshkent_x, toshkent_pochta
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol_x, viloyat_x, viloyat_z, viloyatlar_yol_z
from keyboards.inline.yolovchi.xorazmtuman import xorazm_x, xorazm_pochta
from loader import dp, db




@dp.callback_query_handler(text="saralash_off")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga bormoqchisiz ? ",reply_markup=viloyatlar_yol_z)

pochta = {
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
    "Chortoq": "pochta_chortoq",
    "Chust ": "pochta_chust",
    "Kosonsoy ": "pochta_kosonsoy",
    "Mingbuloq": "pochta_mingbuloq",
    "Namangan ": "pochta_namshaxar",
    "Norin": "pochta_norin",
    "Pop ": "pochta_pop",
    "To'raqo'rg'on": "pochta_toraqo'rg'on",
    "Uchqo'rg'on": "pochta_uchqo'rgo'n",
    "Uychi": "pochta_uychi",
    "Yangiqo'rg'on": "pochta_yangiqor",
    "Davlatobod ": "pochta_davlatobod",
    "Yangi Namangan": "pochta_yangi namangan",
    "Oqoltin" :"pochta_oqoltin",
    "Boyovut" :"pochta_boyovut" ,
    "Guliston" :"pochta_guliston",
    "Xovos" : "pochta_xovos",
    "Mirzaobod" : "pochta_mirzaobod",
    "Sardoba" :"pochta_sardoba",
    "Sayxunobod" :"pochta_sayxunobod",
    "Sirdaryo" :"pochta_shaxri",
    "Bekobod": "pochta_bekobod",
    "Boʻstonliq": "pochta_bostonliq",
    "Boʻka": "pochta_boka",
    "Chinoz": "pochta_chinoz",
    "Qibray": "pochta_qibray",
    "Ohangaron": "pochta_ohangaron",
    "Oqqoʻrgʻon": "pochta_oqqorgon",
    "Parkent": "pochta_parkent",
    "Piskent": "pochta_piskent",
    "Quyi Chirchiq": "pochta_quyichirchiq",
    "Oʻrta Chirchiq": "pochta_ortachirchiq",
    "Yangiyoʻl": "pochta_yangiyol",
    "Yuqori Chirchiq": "pochta_yuqorichirchiq",
    "Zangiota": "pochta_zangiota",
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
    "Konimex" :"pochta_konimex",
    "Karmana" :"pochta_karmana",
    "Qiziltepa" :"pochta_qiziltepa",
    "Xatirchi" :"pochta_xatirchi",
    "Navbahor" :"pochta_navbahor",
    "Nurota" :"pochta_nurota",
    "Tomdi" :"pochta_tomdi",
    "Uchquduq" :"pochta_uchquduq",
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
for key,value in pochta.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="onpage_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="saralash_off"))
        orders = await db.select_tayyor_pochta()
        buyurtma = []
        for i in orders:
            if i[0]==call.data[7:]:
                lis=[]
                if i[1] and [2] is not None:
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer(" Bu tumanda ayni paytdda tayyor pochta mavjud emas !")
        else:
            await state.update_data({"buyurtma_pochta":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="onpage_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_pochta")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"onpage_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="kutib_olish"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="saralash_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="kutib_olish")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaxax")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="receive")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])


for key,value in viloyat_z.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_pochta()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="offpaage_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="ikkinchi_filt_off"))
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
            await call.message.answer("Bu tumanda ayni paytdda tayyor pochta mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data[7:],"viloyatga":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)


@dp.callback_query_handler(text_contains="offpaage_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"offpaage_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="vvvlllaa"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="ikkinchi_filt_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sdasada65656":buyurtma[curr_page]})

@dp.callback_query_handler(text="vvvlllaa")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sdasada65656")
            await call.message.answer(buyurtma[1])

ss={
    "sjduuwgfuwgdkgjda": andijon_pochta,
    "akilwyiwefsdjksd": namangan_pochta,
    "kdjhaigdakhdksa": fargona_pochta,
    "allaskalkdaslkjd": buxoro_pochta,
    "euywiudhkns":toshkent_pochta ,
    "jweytfugdiahjash": sirdaryo_pochta,
    "qdwqwdqwsasxa": surxondaryo_pochta,
    "asasdsadasd": qashqadaryo_pochta,
    "dfdsfdsgfdsfgfd": xorazm_pochta,
    "fghgfjghjgfh": navoiy_pochta,
    "reggfvdvdvcx": jizzax_pochta,
    "tyhjyjghfh": samarqand_pochta,
}
@dp.callback_query_handler(text="ikkinchi_filt_off")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="qogoz_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"qogoz_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="fguuwfrgewuit"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"6as4d6as4d65as6d4":buyurtma[curr_page]})


@dp.callback_query_handler(text="fguuwfrgewuit")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("6as4d6as4d65as6d4")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="654646d6sd465d46s54d")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="poch_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_pochta()
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="qogoz_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="654646d6sd465d46s54d"))
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
                if i[1] and [2] is not None:
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
    if len(buyurtma) == 0:
        await call.message.answer("Bu tumanda ayni paytdda tayyor pochta mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)









