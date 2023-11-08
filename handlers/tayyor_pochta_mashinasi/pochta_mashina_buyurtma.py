import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_mashina import (
    andijon_pmas,buxoro_pmas,fargona_pmas,jizzax_pmasta,namangan_pmas,
    navoiy_pmasta,qashqadaryo_pmas,samarqand_pmasta,sirdaryo_pmas,
    surxondaryo_pmas,toshkent_pmas,xorazm_pmas
)

from keyboards.inline.yolovchi.viloyatlar import viloyat_e, viloyatlar_yol_e
from loader import dp, db




@dp.callback_query_handler(text="ccccccc")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga pochta yubormoqchisiz ? ",reply_markup=viloyatlar_yol_e)

yolovchi = {
    "Ulug'nor":"pocmas_ulug'nor",
    "Andijon shahar":"pocmas_andddshaxar",
    "Asaka":"pocmas_asaka",
    "Baliqchi":"pocmas_baliqchi",
    "Bo'ston ":"pocmas_bo'ston",
    "Buloqbosh":"pocmas_buloqboshi",
    "Izboskan":"pocmas_izboskan",
    "Jalaquduq":"pocmas_jalaquduq",
    "Xoʻjaobod":"pocmas_xo'jabod",
    "Qoʻrgʻontepa":"pocmas_qo'rg'ontepa",
    "Marhamat":"pocmas_marhamat",
    "Oltinkoʻl":"pocmas_oltinko'l",
    "Paxtaobod":"pocmas_paxtaobod",
    "Shahrixon":"pocmas_shaxrixon",
    "Xonabod":"pocmas_xonabod",
    "Olot" :"pocmas_olot",
    "Buxoro" :"pocmas_buxshaxar",
    "Gʻijduvon" :"pocmas_gijduvon",
    "Jondor" :"pocmas_jondor",
    "Kogon" :"pocmas_kogon",
    "Qorakoʻl" :"pocmas_qorakol",
    "Qorovulbozor" : "pocmas_qorovulbozor",
    "Peshku" :"pocmas_peshku",
    "Romitan" :"pocmas_romitan",
    "Shofirkon" :"pocmas_shofirkon",
    "Vobkent" :"pocmas_vobkent",
    "Oltiariq":"pocmas_oltiariq",
    "Bagʻdod ":"pocmas_bog'dod",
    "Beshariq ":"pocmas_beshariq",
    "Buvayda" :"pocmas_buvayda",
    "Dangʻara" :"pocmas_dangara",
    "Fargʻona" :"pocmas_vodil",
    "Furqat" :"pocmas_furqat",
    "Qoʻshtepa":"pocmas_qoshtepa",
    "Quva" :"pocmas_quva",
    "Rishton":"pocmas_rishton",
    "Soʻx" :"pocmas_sox",
    "Toshloq":"pocmas_toshloq",
    "Oʻzbekiston":"pocmas_ozbekiston",
    "Uchkoʻprik" :"pocmas_uchkoprik",
    "Yozyovon" :"pocmas_yozyovon",
    "Chortoq": "pocmas_chortoq",
    "Chust ": "pocmas_chust",
    "Kosonsoy ": "pocmas_kosonsoy",
    "Mingbuloq": "pocmas_mingbuloq",
    "Namangan ": "pocmas_namshaxar",
    "Norin": "pocmas_norin",
    "Pop ": "pocmas_pop",
    "To'raqo'rg'on": "pocmas_toraqo'rg'on",
    "Uchqo'rg'on": "pocmas_uchqo'rgo'n",
    "Uychi": "pocmas_uychi",
    "Yangiqo'rg'on": "pocmas_yangiqor",
    "Davlatobod ": "pocmas_davlatobod",
    "Yangi Namangan": "pocmas_yangi namangan",
    "Oqoltin" :"pocmas_oqoltin",
    "Boyovut" :"pocmas_boyovut" ,
    "Guliston" :"pocmas_guliston",
    "Xovos" : "pocmas_xovos",
    "Mirzaobod" : "pocmas_mirzaobod",
    "Sardoba" :"pocmas_sardoba",
    "Sayxunobod" :"pocmas_sayxunobod",
    "Sirdaryo" :"pocmas_shaxri",
    "Bekobod": "pocmas_bekobod",
    "Boʻstonliq": "pocmas_bostonliq",
    "Boʻka": "pocmas_boka",
    "Chinoz": "pocmas_chinoz",
    "Qibray": "pocmas_qibray",
    "Ohangaron": "pocmas_ohangaron",
    "Oqqoʻrgʻon": "pocmas_oqqorgon",
    "Parkent": "pocmas_parkent",
    "Piskent": "pocmas_piskent",
    "Quyi Chirchiq": "pocmas_quyichirchiq",
    "Oʻrta Chirchiq": "pocmas_ortachirchiq",
    "Yangiyoʻl": "pocmas_yangiyol",
    "Yuqori Chirchiq": "pocmas_yuqorichirchiq",
    "Zangiota": "pocmas_zangiota",
    "Arnasoy" :"pocmas_arnasoy",
    "Baxmal" :"pocmas_baxmal",
    "Doʻstlik" :"pocmas_dostlik",
    "Forish" :"pocmas_forish",
    "Gʻallaorol" :"pocmas_gallarol",
    "Sharof Rashidov ":"pocmas_shrashidov",
    'Mirzachoʻl' :'pocmas_mirzachol',
    "Paxtakor" :"pocmas_paxtakor",
    "Yangiobod" :"pocmas_yangobod",
    'Zomin' :"pocmas_zomin",
    'Zafarobod' :"pocmas_zafarobod",
    'Zarbdor' :"pocmas_zarbdor",
    "Konimex" :"pocmas_konimex",
    "Karmana" :"pocmas_karmana",
    "Qiziltepa" :"pocmas_qiziltepa",
    "Xatirchi" :"pocmas_xatirchi",
    "Navbahor" :"pocmas_navbahor",
    "Nurota" :"pocmas_nurota",
    "Tomdi" :"pocmas_tomdi",
    "Uchquduq" :"pocmas_uchquduq",
    'Bulungʻur' :"pocmas_bulungur",
    'Ishtixon' :"pocmas_ishtixon",
    'Jomboy' :"pocmas_jomboy",
    'Kattaqoʻrgʻon' :"pocmas_kattaqorgon",
    'Qoʻshrabot' :"pocmas_qoshrabot",
    'Narpay' :"pocmas_narpay",
    'Nurobod' :"pocmas_nurobod",
    'Oqdaryo' :"pocmas_oqdaryo",
    'Paxtachi' :"pocmas_paxtachi",
    'Payariq' :"pocmas_payariq",
    'Pastdargʻom' :"pocmas_pastdargom",
    'Samarqand' :"pocmas_samashahar",
    'Toyloq' :"pocmas_toyloq",
    "Bogʻot" :"pocmas_bogot",
    "Gurlan" :"pocmas_gurlan",
    "Xonqa" :"pocmas_xonqa",
    "Hazorasp" :"pocmas_hazorasp",
    "Xiva" :"pocmas_xiva",
    "Qoʻshkoʻpir" :"pocmas_qoshkorik",
    "Shovot" :"pocmas_shovot",
    "Urganch" :"pocmas_urganch",
    "Yangiariq" :"pocmas_yangiariq",
    "Yangibozor" :"pocmas_yangibozor",
    "Tupproqqalʼa" :"pocmas_tuproqqala",
    "Dehqonobod":"pocmas_dehqonobod",
    "Kasbi":"pocmas_kasbi",
    "Kitob":"pocmas_kitob",
    "Koson":"pocmas_koson",
    "Koʻkdala":"pocmas_kokdala",
    "Mirishkor":"pocmas_mirishkor",
    "Muborak":"pocmas_muborak",
    "Nishon":"pocmas_nishon",
    "Qamashi":"pocmas_qamashi" ,
    "Qarshi":"pocmas_qarshi",
    "Yakkabogʻ" :"pocmas_yakkabog",
    "Gʻuzor":"pocmas_guzor",
    "Shahrisabz":"pocmas_shahrisabz",
    "Chiroqchi":"pocmas_chiroqchi",

}
for key,value in yolovchi.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="peoskk5454s_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="bbbbbb"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="ccccccc"))
        orders = await db.select_tayyor_pochta_mashina()
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
            await call.message.answer("Bu tumanda ayni paytdda tayyor pochta mashinasi mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="peoskk5454s_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"peoskk5454s_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="eeeeeee"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="ccccccc"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"xaaxax":buyurtma[curr_page]})


@dp.callback_query_handler(text="eeeeeee")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("xaaxax")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="bbbbbb")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])


for key,value in viloyat_e.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_pochta_mashina()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="fffffff_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="2f22f22f"))
        buyurtma = []
        data = await state.get_data()
        tuman=data.get("tuman")
        for i in orders:
            if i[3] == call.data[7:] and i[0]==tuman:
                lis = []
                lis.append(i[1])
                lis.append(i[2])
                buyurtma.append(lis)
        if len(buyurtma) == 0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor pochta mashinasi mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data[7:],"viloyatga":call.data[7:]})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)


@dp.callback_query_handler(text_contains="fffffff_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"fffffff_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="asqweqwqw"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="2f22f22f"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"sdsasasada65656":buyurtma[curr_page]})

@dp.callback_query_handler(text="asqweqwqw")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("sdsasasada65656")
            await call.message.answer(buyurtma[1])

ss={
    "x_sjduuwgfuwgdkgjda": andijon_pmas,
    "x_akilwyiwefsdjksd": namangan_pmas,
    "x_kdjhaigdakhdksa": fargona_pmas,
    "x_allaskalkdaslkjd": buxoro_pmas,
    "x_euywiudhkns":toshkent_pmas ,
    "x_jweytfugdiahjash": sirdaryo_pmas,
    "x_qdwqwdqwsasxa": surxondaryo_pmas,
    "x_asasdsadasd": qashqadaryo_pmas,
    "x_dfdsfdsgfdsfgfd": xorazm_pmas,
    "x_fghgfjghjgfh": navoiy_pmasta,
    "x_reggfvdvdvcx": jizzax_pmasta,
    "x_tyhjyjghfh": samarqand_pmasta,
}
@dp.callback_query_handler(text="2f22f22f")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key[2:]:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="akakaka_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"akakaka_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="qwduqwiu"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"6as4d6as4daaa65as6d4":buyurtma[curr_page]})


@dp.callback_query_handler(text="qwduqwiu")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("6as4d6as4daaa65as6d4")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="qoagsfhqoqo")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="pmas_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_pochta_mashina()
    print(orders)
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="akakaka_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="qoagsfhqoqo"))
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
        await call.message.answer(" Bu tumanda ayni paytdda tayyor pochta mashinasi mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)









