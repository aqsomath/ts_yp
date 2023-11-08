import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.haydovchi_reys.tayyor_taxi_keyboards import tax_tayin_vil
from keyboards.inline.yolovchi.andtuman import andijon_x
from keyboards.inline.yolovchi.buxtuman import buxoro_x
from keyboards.inline.yolovchi.fartuman import  fargona_x
from keyboards.inline.yolovchi.jizztuman import  jizzax_x
from keyboards.inline.yolovchi.namtuman import  namangan_x
from keyboards.inline.yolovchi.navoiytuman import  navoiy_x
from keyboards.inline.yolovchi.qashtuman import  qashqadaryo_x
from keyboards.inline.yolovchi.samartuman import  samarqand_x
from keyboards.inline.yolovchi.sirtuman import  sirdaryo_x
from keyboards.inline.yolovchi.surtuman import  surxondaryo_x
from keyboards.inline.yolovchi.toshtuman import  toshkent_x
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol_x, viloyat_x
from keyboards.inline.yolovchi.xorazmtuman import  xorazm_x
from loader import dp, db



@dp.callback_query_handler(text='ortga')
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatdan taxi kerak",reply_markup=tax_tayin_vil)




@dp.callback_query_handler(text="filt_off")
async def filt_offf(call:CallbackQuery,state:FSMContext):

    await call.message.answer("Aynan qaysi viloyatga bormoqchisiz ? ",reply_markup=viloyatlar_yol_x)


ansa = {
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
    "Oltiariq":"xxxoltiariq",
    "Bagʻdod ":"bog'dod",
    "Beshariq ":"beshariq",
    "Buvayda" :"buvayda",
    "Dangʻara" :"dangara",
    "Fargʻona" :"fergana ",
    "Furqat" :"furqat",
    "Qoʻshtepa":"qo'shtepa",
    "Quva" :"quva",
    "Rishton":"rishton",
    "Soʻx" :"sox",
    "Toshloq":"toshloq",
    "Oʻzbekiston":"o'zbekiston",
    "Uchkoʻprik" :"uchko'prik",
    "Yozyovon" :"yozyovon",
    "Konimex" :"konimex",
    "Karmana" :"karmana",
    "Qiziltepa" :"qiziltepa",
    "Xatirchi" :"xatirchi",
    "Navbahor" :"navbahor",
    "Nurota" :"nurota",
    "Tomdi" :"tomdi",
    "Uchquduq" :"uchquduq",
    "Chortoq": "chortoq",
    "Chust ": "chust",
    "Kosonsoy ": "kosonsoy",
    "Mingbuloq": "mingbuloq",
    "Namangan ": "namangan shaxar",
    "Norin": "norin",
    "Pop ": "pop",
    "To'raqo'rg'on": "toraqo'rg'on",
    "Uchqo'rg'on": "uchqo'rgo'n",
    "Uychi": "uychi",
    "Yangiqo'rg'on": "yangi qo'rg'on",
    "Davlatobod ": "davlatobod",
    "Yangi Namangan": "yangi namangan",
    "Bekobod": "bekobod",
    "Boʻstonliq": "bostonliq",
    "Boʻka": "boka",
    "Chinoz": "chinoz",
    "Qibray": "qibray",
    "Ohangaron": "ohangaron",
    "Oqqoʻrgʻon": "oqqorgon",
    "Parkent": "parkent",
    "Piskent": "piskent",
    "Quyi Chirchiq": "quyichirchiq",
    "Oʻrta Chirchiq": "ortachirchiq",
    "Yangiyoʻl": "yangiyol",
    "Yuqori Chirchiq": "yuqorichirchiq",
    "Zangiota": "zangiota",
    "Oqoltin" :"oqoltin",
    "Boyovut" :"boyovut" ,
    "Guliston" :"guliston",
    "Xovos" : "xovos",
    "Mirzaobod" : "mirzaobod",
    "Sardoba" :"sardoba",
    "Sayxunobod" :"sayxunobod",
    "Sirdaryo" :"sirdaryo shaxri",
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
    "Bogʻot" :"bog'ot",
    "Gurlan" :"gurlan",
    "Xonqa" :"xonqa",
    "Hazorasp" :"hazorasp",
    "Xiva" :"xiva",
    "Qoʻshkoʻpir" :"qoshko'prik",
    "Shovot" :"shovot",
    "Urganch" :"urganch",
    "Yangiariq" :"yangiariq",
    "Yangibozor" :"yangibozor",
    "Tupproqqalʼa" :"tuproqqal'a",
    "Baxmal" :"baxmal",
    "Doʻstlik" :"do'stlik",
    "Forish" :"forish",
    "Gʻallaorol" :"g'allarol",
    "Sharof Rashidov ":"sharof rashidov",
    'Mirzachoʻl' :'mirzachol',
    "Paxtakor" :"paxtakor",
    "Yangiobod" :"yangi obod",
    'Zomin' :"zomin",
    'Zafarobod' :"zafarobod",
    'Zarbdor' :"zarbdor",
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
    'Samarqand' :"samarqand shahar",
    'Toyloq' :"toyloq",

}

for key,value in ansa.items():
    @dp.callback_query_handler(text=value)
    async def jonatish(call:CallbackQuery, state:FSMContext):
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="page_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="2xc12x1c2xc21xc1x"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="filt_off"))
        orders = await db.select_tayyor_taxi()
        buyurtma = []
        for i in orders:
            if i[0]==call.data:
                if i[1] and [2] is not None:

                    lis=[]
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma)==0:
            await call.message.answer("Bu tumanda ayni paytdda tayyor taxi mavjud emas !")
        else:
            await state.update_data({"buyurtma":buyurtma,"tuman":call.data})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="page_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"page_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="filt_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"axax":buyurtma[curr_page]})


@dp.callback_query_handler(text="2xc12x1c2xc21xc1x")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text="receive")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("axax")
            await call.message.answer(buyurtma[1])





for key,value in viloyat_x.items():
    @dp.callback_query_handler(text=value)
    async def region_filt(call:CallbackQuery,state:FSMContext):
        orders = await db.select_tayyor_taxi()
        markup = aiogram.types.InlineKeyboardMarkup()
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="bet_0"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="receive"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="second_filt_off"))
        buyurtma = []
        data = await state.get_data()
        tuman=data.get("tuman")
        for i in orders:
            if i[3] == call.data and i[0]==tuman:
                if i[1] and [2] is not None:
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
        if len(buyurtma) == 0:
            await call.message.answer("222 Bu tumanda ayni paytdda tayyor taxi mavjud emas !")
        else:
            await state.update_data({"buyurtma_1": buyurtma,"call":call.data,"viloyatga":call.data})
            await call.message.answer(buyurtma[0][0],reply_markup=markup)

@dp.callback_query_handler(text_contains="bet_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_1")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"bet_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="qqaa"))
        markup.add(aiogram.types.InlineKeyboardButton("Filtrlash", callback_data="second_filt_off"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"qqaxax":buyurtma[curr_page]})

@dp.callback_query_handler(text="qqaa")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("qqaxax")
            await call.message.answer(buyurtma[1])
ss={
    "sjduuwgfuwgdkgjda": andijon_x,
    "akilwyiwefsdjksd": namangan_x,
    "kdjhaigdakhdksa": fargona_x,
    "allaskalkdaslkjd": buxoro_x,
    "euywiudhkns":toshkent_x ,
    "jweytfugdiahjash": sirdaryo_x,
    "qdwqwdqwsasxa": surxondaryo_x,
    "asasdsadasd": qashqadaryo_x,
    "dfdsfdsgfdsfgfd": xorazm_x,
    "fghgfjghjgfh": navoiy_x,
    "reggfvdvdvcx": jizzax_x,
    "tyhjyjghfh": samarqand_x,
}
@dp.callback_query_handler(text="second_filt_off")
async def callback_query(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('call')
    for key, value in ss.items():

        if tuman==key:
            await call.message.answer("Qaysi tumanga borasiz ? ", reply_markup=value)
            await state.update_data({'value':value})

@dp.callback_query_handler(text_contains="varaq_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("buyurtma_2")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"varaq_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="sdsdsd"))
        await call.message.answer(text=buyurtma[curr_page][0],reply_markup=markup)
        await state.update_data({"dsdsd":buyurtma[curr_page]})

@dp.callback_query_handler(text="sdsdsd")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("dsdsd")
            await call.message.answer(buyurtma[1])

@dp.callback_query_handler(text="asdascdc")
async def callback_query(call:CallbackQuery,state:FSMContext):
            data = await state.get_data()
            buyurtma = data.get("buyurtma_2")
            await call.message.answer(buyurtma[0][1])

@dp.callback_query_handler(text_contains="x_")
async def ajss(call:CallbackQuery,state:FSMContext):
    orders = await db.select_tayyor_taxi()
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data="varaq_0"))
    markup.add(aiogram.types.InlineKeyboardButton("Qabul qilish", callback_data="asdascdc"))
    buyurtma = []
    data = await state.get_data()
    tuman=data.get("tuman")
    viloyatiga=data.get("viloyatga")
    for i in orders:
        if i[0] == tuman:
            print(i[0])
            if i[3]==viloyatiga:
             print(i[3])
             if i[4]==call.data[2:].capitalize():
                if i[1] and [2] is not None:
                    print(i[4])
                    lis = []
                    lis.append(i[1])
                    lis.append(i[2])
                    buyurtma.append(lis)
    if len(buyurtma) == 0:
        await call.message.answer("333 Bu tumanda ayni paytdda tayyor taxi mavjud emas !")
    else:
        await state.update_data({"buyurtma_2": buyurtma})
        await call.message.answer(buyurtma[0][0],reply_markup=markup)


