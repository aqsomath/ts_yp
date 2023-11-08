import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.andtuman import andijon_yuuk
from keyboards.inline.yolovchi.buxtuman import buxoro_yuuk
from keyboards.inline.yolovchi.fartuman import fargona_yuuk
from keyboards.inline.yolovchi.jizztuman import  jizzax_yuukta
from keyboards.inline.yolovchi.namtuman import namangan_yuuk
from keyboards.inline.yolovchi.navoiytuman import  navoiy_yuukta
from keyboards.inline.yolovchi.qashtuman import  qashqadaryo_yuuk
from keyboards.inline.yolovchi.samartuman import  samarqand_yuukta
from keyboards.inline.yolovchi.sirtuman import sirdaryo_yuuk
from keyboards.inline.yolovchi.surtuman import  surxondaryo_yuuk
from keyboards.inline.yolovchi.toshtuman import toshkent_yuuk
from keyboards.inline.yolovchi.viloyatlar import  viloyatlar_yol_y, viloyat_y
from keyboards.inline.yolovchi.xorazmtuman import  xorazm_yuuk
from loader import dp, db




@dp.callback_query_handler(text="yigish_off")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga bormoqchisiz ? ",reply_markup=viloyatlar_yol_y)

pochta = {
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
    "Chortoq": "yukbor_chortoq",
    "Chust ": "yukbor_chust",
    "Kosonsoy ": "yukbor_kosonsoy",
    "Mingbuloq": "yukbor_mingbuloq",
    "Namangan ": "yukbor_namshaxar",
    "Norin": "yukbor_norin",
    "Pop ": "yukbor_pop",
    "To'raqo'rg'on": "yukbor_toraqo'rg'on",
    "Uchqo'rg'on": "yukbor_uchqo'rgo'n",
    "Uychi": "yukbor_uychi",
    "Yangiqo'rg'on": "yukbor_yangiqor",
    "Davlatobod ": "yukbor_davlatobod",
    "Yangi Namangan": "yukbor_yangi namangan",
    "Oqoltin" :"yukbor_oqoltin",
    "Boyovut" :"yukbor_boyovut" ,
    "Guliston" :"yukbor_guliston",
    "Xovos" : "yukbor_xovos",
    "Mirzaobod" : "yukbor_mirzaobod",
    "Sardoba" :"yukbor_sardoba",
    "Sayxunobod" :"yukbor_sayxunobod",
    "Sirdaryo" :"yukbor_shaxri",
    "Bekobod": "yukbor_bekobod",
    "Boʻstonliq": "yukbor_bostonliq",
    "Boʻka": "yukbor_boka",
    "Chinoz": "yukbor_chinoz",
    "Qibray": "yukbor_qibray",
    "Ohangaron": "yukbor_ohangaron",
    "Oqqoʻrgʻon": "yukbor_oqqorgon",
    "Parkent": "yukbor_parkent",
    "Piskent": "yukbor_piskent",
    "Quyi Chirchiq": "yukbor_quyichirchiq",
    "Oʻrta Chirchiq": "yukbor_ortachirchiq",
    "Yangiyoʻl": "yukbor_yangiyol",
    "Yuqori Chirchiq": "yukbor_yuqorichirchiq",
    "Zangiota": "yukbor_zangiota",
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
    "Konimex" :"yukbor_konimex",
    "Karmana" :"yukbor_karmana",
    "Qiziltepa" :"yukbor_qiziltepa",
    "Xatirchi" :"yukbor_xatirchi",
    "Navbahor" :"yukbor_navbahor",
    "Nurota" :"yukbor_nurota",
    "Tomdi" :"yukbor_tomdi",
    "Uchquduq" :"yukbor_uchquduq",
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
for key,value in pochta.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="sahifa_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="natijano"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="yigish_off"))
        orders = await db.select_tayyor_yuk()
        buyurtma = []
        for i in orders:
            if i[0]==call.data[7:]:
                if i[1] and [2] is not None:

                    lis=[]
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor yuk mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="sahifa_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sahifa_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="olmoq"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="yigish_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="olmoq")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaaxax")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="natijano")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])


for key,value in viloyat_y.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_yuk()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="jurnal_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="2_filt_off"))
        buyurtma = []
        data = await state.get_data()
        tuman=data.get("tuman")
        for i in orders:
            if i[3] == call.data[8:] and i[0]==tuman:
                if i[1] and [2] is not None:
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma) == 0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor yuk mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data[8:],"viloyatga":call.data[8:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)


@dp.callback_query_handler(text_contains="jurnal_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"jurnal_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="shdgsduyf"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="2_filt_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sdasada65656":buyurtma[curr_page]})

@dp.callback_query_handler(text="shdgsduyf")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sdasada65656")
            await call.message.answer(buyurtma[1])

ss={
    "x_sjduuwgfuwgdkgjda": andijon_yuuk,
    "x_akilwyiwefsdjksd": namangan_yuuk,
    "x_kdjhaigdakhdksa": fargona_yuuk,
    "x_allaskalkdaslkjd": buxoro_yuuk,
    "x_euywiudhkns":toshkent_yuuk ,
    "x_jweytfugdiahjash": sirdaryo_yuuk,
    "x_qdwqwdqwsasxa": surxondaryo_yuuk,
    "x_asasdsadasd": qashqadaryo_yuuk,
    "x_dfdsfdsgfdsfgfd": xorazm_yuuk,
    "x_fghgfjghjgfh": navoiy_yuukta,
    "x_reggfvdvdvcx": jizzax_yuukta,
    "x_tyhjyjghfh": samarqand_yuukta,
}
@dp.callback_query_handler(text="2_filt_off")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key[2:]:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="asqwwe_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"asqwwe_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="asaww111212"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"6as4d6as4d65as6d4":buyurtma[curr_page]})


@dp.callback_query_handler(text="asaww111212")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("6as4d6as4d65as6d4")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="dssdl")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="yuuk_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_yuk()
    print(orders)
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="asqwwe_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="dssdl"))
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
        await call.message.answer("333 Bu tumanda ayni paytdda tayyor yuk mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)









