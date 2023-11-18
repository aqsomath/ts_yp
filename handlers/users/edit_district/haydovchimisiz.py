from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.andtuman import andijon_old
from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback, andijon_callback, \
    menu_callback
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, bot,db


@dp.callback_query_handler(kirish_callback.filter(item_name='haydovchi'))
async def haydovchi(call:CallbackQuery):
    driver={
    "Haydovchi reys belgilash":'yolovchikerak',
    "Tayyor yo'lovchi": 'tayyoryolovchi',
    "Yuk kerak":'yukkerak',
    "Tayyor yuk": "tayyoryuk",
    "Pochta kerak":'pochtakerak',
    "Tayyor pochta": "tayyorpochta",
    "Sayohatchilar kerak":'sayohatgayolovchi',
    "Tayyor sayohatchi":"tayyorsayohatchi",
    "Mening buyurtmalarim": "meningbuyurtmalarim",
    "Admin bilan bog'lanish": "adminbilanboglanish",
    "Filtrlash":"filtrlash_1",
    "Viloyatlarni filtrlash":"viloyalarnifiltrlash",
    "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key,value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
#
nima_tashisan=InlineKeyboardMarkup(row_width=2)
nima_tashisan.insert(InlineKeyboardButton(text="Yo'lovchi tashiman", callback_data="odamtashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Pochta tashiman", callback_data="pochtatashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Yuk tashiman", callback_data="yuktashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Sayohatchi tashiman", callback_data="sayohatchitashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Barchasi", callback_data="hammasinitashimantashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Yakunlash", callback_data="tugatish"))


@dp.callback_query_handler(text='tugatish')
async def tugatish(call:CallbackQuery):
    driver = {
        "Haydovchi reys belgilash": 'yolovchikerak',
        "Tayyor yo'lovchi": 'tayyoryolovchi',
        "Yuk kerak": 'yukkerak',
        "Tayyor yuk": "tayyoryuk",
        "Pochta kerak": 'pochtakerak',
        "Tayyor pochta": "tayyorpochta",
        "Sayohatchilar kerak": 'sayohatgayolovchi',
        "Tayyor sayohatchi": "tayyorsayohatchi",
        "Mening buyurtmalarim": "meningbuyurtmalarim",
        "Admin bilan bog'lanish": "adminbilanboglanish",
        "Filtrlash": "filtrlash_1",
        "Viloyatlarni filtrlash": "viloyalarnifiltrlash",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"
    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Haydovchi!\nSiz tanlagan hizmat turi bo'yicha butun "
                              "O'zbekiston bo'yicha mijozlarning buyurtmalari sizga kelib turadi."
                              "O'zingizga mos hududlarni tanlash uchun 'Viloyalarni  filtrlashni' bosing.",reply_markup=markup)
@dp.callback_query_handler(menu_callback.filter(item_name='filtrlash_1'))
async def haydovchi(call:CallbackQuery):

    await call.message.answer("Salom haydovchi\nSiz nima tashisiz ?", reply_markup=nima_tashisan)

@dp.callback_query_handler(text='odamtashiman')
async def edit(call:CallbackQuery):
    nima_tashisan['inline_keyboard'][0][0]['text'] = "✅ Yo'lovchi tashiman"
    nima_tashisan['inline_keyboard'][0][0]['callback_data'] = "odam_tashimayman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await db.add_driver(tashiman_odam='ok',tashiman_pochta=None,tashiman_yuk=None,telegram_id=call.from_user.id,sayohatchi_tashiman=None)
    await call.message.edit_reply_markup(nima_tashisan)

@dp.callback_query_handler(text='odam_tashimayman')
async def edit(call:CallbackQuery):
    await db.delete_driver(tashiman_odam='ok',  telegram_id=call.from_user.id)
    nima_tashisan['inline_keyboard'][0][0]['text'] = "Yo'lovchi tashiman"
    nima_tashisan['inline_keyboard'][0][0]['callback_data'] = "odamtashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='pochtatashiman')
async def edit(call:CallbackQuery):
    await db.add_driver(tashiman_odam=None,tashiman_pochta='ok',tashiman_yuk=None,telegram_id=call.from_user.id,sayohatchi_tashiman=None)
    nima_tashisan['inline_keyboard'][0][1]['text'] = "✅ Pochta tashiman"
    nima_tashisan['inline_keyboard'][0][1]['callback_data'] = "pochtatashimayman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='pochtatashimayman')
async def edit(call:CallbackQuery):
    await db.delete_driver(tashiman_pochta='ok',  telegram_id=call.from_user.id)
    nima_tashisan['inline_keyboard'][0][1]['text'] = "Pochta tashiman"
    nima_tashisan['inline_keyboard'][0][1]['callback_data'] = "pochtatashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='yuktashiman')
async def edit(call:CallbackQuery):
    await db.add_driver(tashiman_odam=None,tashiman_pochta=None,tashiman_yuk='ok',telegram_id=call.from_user.id,sayohatchi_tashiman=None)
    nima_tashisan['inline_keyboard'][1][0]['text'] = "✅ Yuk tashiman"
    nima_tashisan['inline_keyboard'][1][0]['callback_data'] = "yuk_tashimayman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='yuk_tashimayman')
async def edit(call:CallbackQuery):
    await db.delete_driver(tashiman_yuk='ok',  telegram_id=call.from_user.id)
    nima_tashisan['inline_keyboard'][1][0]['text'] = "Yuk tashiman"
    nima_tashisan['inline_keyboard'][1][0]['callback_data'] = "yuktashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)


@dp.callback_query_handler(text='sayohatchitashiman')
async def edit(call:CallbackQuery):
    await db.add_driver(tashiman_odam=None,tashiman_pochta=None,tashiman_yuk=None,telegram_id=call.from_user.id,sayohatchi_tashiman='ok')
    nima_tashisan['inline_keyboard'][1][1]['text'] = "✅ Sayohatchi tashiman"
    nima_tashisan['inline_keyboard'][1][1]['callback_data'] = "sayohatchi_tashimayman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='sayohatchi_tashimayman')
async def edit(call:CallbackQuery):
    await db.delete_driver(sayohatchi_tashiman='ok',  telegram_id=call.from_user.id)
    nima_tashisan['inline_keyboard'][1][1]['text'] = "Sayohatchi tashiman"
    nima_tashisan['inline_keyboard'][1][1]['callback_data'] = "sayohatchitashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await call.message.edit_reply_markup(nima_tashisan)

#      B A R C H A S I N I     B E L G I L A S H
@dp.callback_query_handler(text='hammasinitashimantashiman')
async def edit(call:CallbackQuery):
    await db.delete_driver(tashiman_yuk='ok',  telegram_id=call.from_user.id)
    await db.delete_driver(tashiman_pochta='ok',  telegram_id=call.from_user.id)
    await db.delete_driver(tashiman_odam='ok',  telegram_id=call.from_user.id)
    await db.delete_driver(sayohatchi_tashiman='ok',  telegram_id=call.from_user.id)
    await db.add_driver(tashiman_odam='ok',tashiman_pochta='ok',tashiman_yuk='ok',telegram_id=call.from_user.id,sayohatchi_tashiman='ok')
    nima_tashisan['inline_keyboard'][1][0]['text'] = "Yuk tashiman"
    nima_tashisan['inline_keyboard'][1][0]['callback_data'] = "yuktashiman"
    nima_tashisan['inline_keyboard'][0][1]['text'] = "Pochta tashiman"
    nima_tashisan['inline_keyboard'][0][1]['callback_data'] = "pochtatashiman"
    nima_tashisan['inline_keyboard'][0][0]['text'] = "Yo'lovchi tashiman"
    nima_tashisan['inline_keyboard'][0][0]['callback_data'] = "odamtashiman"
    nima_tashisan['inline_keyboard'][1][1]['text'] = "Sayohatchi tashiman"
    nima_tashisan['inline_keyboard'][1][1]['callback_data'] = "sayohatchitashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "✅ Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasini_tashimayman"
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(text='hammasini_tashimayman')
async def edit(call:CallbackQuery):

    nima_tashisan['inline_keyboard'][1][0]['text'] = "Yuk tashiman"
    nima_tashisan['inline_keyboard'][1][0]['callback_data'] = "yuktashiman"
    nima_tashisan['inline_keyboard'][0][1]['text'] = "Pochta tashiman"
    nima_tashisan['inline_keyboard'][0][1]['callback_data'] = "pochtatashiman"
    nima_tashisan['inline_keyboard'][0][0]['text'] = "Yo'lovchi tashiman"
    nima_tashisan['inline_keyboard'][0][0]['callback_data'] = "odamtashiman"
    nima_tashisan['inline_keyboard'][1][1]['text'] = "Sayohatchi tashiman"
    nima_tashisan['inline_keyboard'][1][1]['callback_data'] = "sayohatchitashiman"
    nima_tashisan['inline_keyboard'][2][0]['text'] = "Barchasi"
    nima_tashisan['inline_keyboard'][2][0]['callback_data'] = "hammasinitashimantashiman"
    await db.delete_driver(tashiman_yuk='ok', telegram_id=call.from_user.id)
    await db.delete_driver(tashiman_pochta='ok', telegram_id=call.from_user.id)
    await db.delete_driver(tashiman_odam='ok', telegram_id=call.from_user.id)
    await call.message.edit_reply_markup(nima_tashisan)
@dp.callback_query_handler(menu_callback.filter(item_name="viloyalarnifiltrlash"))
async def select_hudud(call:CallbackQuery):
    await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='nazad'))
async def nazad(call:CallbackQuery):
    driver = {
        "Haydovchi reys belgilash": 'yolovchikerak',
        "Tayyor yo'lovchi": 'tayyoryolovchi',
        "Yuk kerak": 'yukkerak',
        "Tayyor yuk": "tayyoryuk",
        "Pochta kerak": 'pochtakerak',
        "Tayyor pochta": "tayyorpochta",
        "Sayohatchilar kerak": 'sayohatgayolovchi',
        "Tayyor sayohatchi": "tayyorsayohatchi",
        "Mening buyurtmalarim": "meningbuyurtmalarim",
        "Admin bilan bog'lanish": "adminbilanboglanish",
        "Filtrlash": "filtrlash_1",
        "Viloyatlarni filtrlash": "viloyalarnifiltrlash",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"
    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Sizga kerakli bo'limni tanlang",reply_markup=markup)


x=["Ulug'nor","Andijon shahar",
   "Asaka","Baliqchi","Bo'ston",
   "Buloqbosh","Izboskan","Jalaquduq",
   "Xoʻjaobod","Qoʻrgʻontepa","Marhamat",
   "Oltinkoʻl","Paxtaobod","Shahrixon","Xonabod"
   ]


# A N D I J O N   V I L O Y T I

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='jonn'))
async def andijontuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="ulug'nor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="asaka", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="paxtaobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="shaxrixon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="marhamat", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="xonabod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="oltinko'l", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="baliqchi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="bo'ston", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="buloqboshi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="izboskan", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="jalaquduq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="xo'jabod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa", telegram_id=call.from_user.id)
    await call.message.answer("Hurmatli haydovchi siz Andijonni barcha tumanlaridan mijozlarni qabul qilasiz. "
                              "Sziga keraksiz hududlardan chiqib keting."
                              "\n\n❌ - chiqqan holat"
                              "\n\n✅- kirgan holat ")
    await call.message.answer("Andijon tumanlari", reply_markup=andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='qaytamiz'))
async def qaytish_ortga(call:CallbackQuery):
    await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)
@dp.callback_query_handler(andijon_callback.filter(item_name='glavmenu'))
async def qaytish_ortga(call:CallbackQuery):
    driver = {
        "Haydovchi reys belgilash": 'yolovchikerak',
        "Tayyor yo'lovchi": 'tayyoryolovchi',
        "Yuk kerak": 'yukkerak',
        "Tayyor yuk": "tayyoryuk",
        "Pochta kerak": 'pochtakerak',
        "Tayyor pochta": "tayyorpochta",
        "Sayohatchilar kerak": 'sayohatgayolovchi',
        "Tayyor sayohatchi": "tayyorsayohatchi",
        "Mening buyurtmalarim": "meningbuyurtmalarim",
        "Admin bilan bog'lanish": "adminbilanboglanish",
        "Filtrlash": "filtrlash_1",
        "Viloyatlarni filtrlash": "viloyalarnifiltrlash",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Sizga kerakli xizmat turini tanlang ?", reply_markup=markup)
@dp.callback_query_handler(andijon_callback.filter(item_name='Xahh'))
async def hammasini_rad_qilish(call:CallbackQuery):
    andijon_old['inline_keyboard'][0][0]['text'] = "❌ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulug"
    await db.delete_driver_info(tuman="ulug'nor", telegram_id=call.from_user.id)
    await db.delete_driver_info(tuman="andijon shaxar", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][1]['text'] = "❌ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shahar"
    await db.delete_driver_info(tuman="asaka", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][2]['text'] = "❌ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asak"
    await db.delete_driver_info(tuman="baliqchi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][0]['text'] = "❌ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliq"
    await db.delete_driver_info(tuman="bo'ston", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][1]['text'] = "❌ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boston"
    await db.delete_driver_info(tuman="buloqboshi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][2]['text'] = "❌ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloq"
    await db.delete_driver_info(tuman="izboskan", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][0]['text'] = "❌ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izbos"
    await db.delete_driver_info(tuman="jalaquduq", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][1]['text'] = "❌ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jala"
    await db.delete_driver_info(tuman="xo'jabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][2]['text'] = "❌ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xoja"
    await db.delete_driver_info(tuman="qo'rg'ontepa", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][0]['text'] = "❌ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgon"
    await db.delete_driver_info(tuman="marhamat", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][1]['text'] = "❌ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marham"
    await db.delete_driver_info(tuman="oltinko'l", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][2]['text'] = "❌ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltin"
    await db.delete_driver_info(tuman="paxtaobod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][0]['text'] = "❌ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxta"
    await db.delete_driver_info(tuman="shaxrixon", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][1]['text'] = "❌ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxri"
    await db.delete_driver_info(tuman="xonabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][2]['text'] = "❌ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xona"
    andijon_old['inline_keyboard'][5][0]['text'] = "Hammasini belgilash"
    andijon_old['inline_keyboard'][5][0]['callback_data'] = "course:lkajslj"
    await call.message.edit_reply_markup(andijon_old)





@dp.callback_query_handler(andijon_callback.filter(item_name='lkajslj'))
async def hammasini_belgilash(call:CallbackQuery):
    andijon_old['inline_keyboard'][5][0]['text'] = "Hammasini rad etish"
    andijon_old['inline_keyboard'][5][0]['callback_data'] = "course:Xahh"
    andijon_old['inline_keyboard'][0][0]['text'] = "✅ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulugnor"
    andijon_old['inline_keyboard'][0][1]['text'] = "✅ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shaxar"
    andijon_old['inline_keyboard'][0][2]['text'] = "✅ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asaka"
    andijon_old['inline_keyboard'][1][0]['text'] = "✅ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliqchi"
    andijon_old['inline_keyboard'][1][1]['text'] = "✅ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boz"
    andijon_old['inline_keyboard'][1][2]['text'] = "✅ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloqboshi"
    andijon_old['inline_keyboard'][2][0]['text'] = "✅ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izboskan"
    andijon_old['inline_keyboard'][2][1]['text'] = "✅ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jalaquduq"
    andijon_old['inline_keyboard'][2][2]['text'] = "✅ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xojabod"
    andijon_old['inline_keyboard'][3][0]['text'] = "✅ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgontepa"
    andijon_old['inline_keyboard'][3][1]['text'] = "✅ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marhamat"
    andijon_old['inline_keyboard'][3][2]['text'] = "✅ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltinkol"
    andijon_old['inline_keyboard'][4][0]['text'] = "✅ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxtaobod"
    andijon_old['inline_keyboard'][4][1]['text'] = "✅ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxrixon"
    andijon_old['inline_keyboard'][4][2]['text'] = "✅ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xonabod"
    await db.add_driver_info(viloyat="Andijon", tuman="ulug'nor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="asaka", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="paxtaobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="shaxrixon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="marhamat", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="xonabod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="oltinko'l", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="baliqchi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="bo'ston", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="buloqboshi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="izboskan", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="jalaquduq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="xo'jabod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa", telegram_id=call.from_user.id)
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='ulugnor'))
async def edit(call:CallbackQuery):
    andijon_old['inline_keyboard'][0][0]['text'] = "❌ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulug"

    await db.delete_driver_info(tuman="ulug'nor", telegram_id=call.from_user.id)
    await call.message.edit_reply_markup(andijon_old)




@dp.callback_query_handler(andijon_callback.filter(item_name='ulug'))
async def edit(call:CallbackQuery):
    andijon_old['inline_keyboard'][0][0]['text'] = "✅ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulugnor"
    await db.add_driver_info(viloyat="Andijon", tuman="ulug'nor", telegram_id=call.from_user.id)
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shaxar'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="andijon shaxar", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][1]['text'] = "❌ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shahar"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shahar'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][1]['text'] = "✅ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shaxar"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='asaka'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="asaka", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][2]['text'] = "❌ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asak"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='asak'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="asaka", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][0][2]['text'] = "✅ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asaka"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='baliqchi'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="baliqchi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][0]['text'] = "❌ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliq"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='baliq'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="baliqchi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][0]['text'] = "✅ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliqchi"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='boz'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="bo'ston", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][1]['text'] = "❌ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boston"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='boston'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="bo'ston", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][1]['text'] = "✅ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boz"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='buloqboshi'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="buloqboshi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][2]['text'] = "❌ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloq"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='buloq'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="buloqboshi", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][1][2]['text'] = "✅ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloqboshi"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='izboskan'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="izboskan", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][0]['text'] = "❌ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izbos"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='izbos'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="izboskan", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][0]['text'] = "✅ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izboskan"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='jalaquduq'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="jalaquduq", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][1]['text'] = "❌ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jala"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='jala'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="jalaquduq", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][1]['text'] = "✅ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jalaquduq"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xojabod'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="xo'jabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][2]['text'] = "❌ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xoja"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xoja'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="xo'jabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][2][2]['text'] = "✅ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xojabod"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='qorgontepa'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="qo'rg'ontepa", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][0]['text'] = "❌ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgon"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='qorgon'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][0]['text'] = "✅ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgontepa"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='marhamat'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="marhamat", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][1]['text'] = "❌ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marham"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='marham'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="marhamat", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][1]['text'] = "✅ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marhamat"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='oltinkol'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="oltinko'l", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][2]['text'] = "❌ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltin"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='oltin'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="oltinko'l", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][3][2]['text'] = "✅ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltinkol"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='paxtaobod'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="paxtaobod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][0]['text'] = "❌ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxta"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='paxta'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="paxtaobod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][0]['text'] = "✅ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxtaobod"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='shaxrixon'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="shaxrixon", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][1]['text'] = "❌ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxri"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shaxri'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="shaxrixon", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][1]['text'] = "✅ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxrixon"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='xonabod'))
async def edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="xonabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][2]['text'] = "❌ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xona"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xona'))
async def edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Andijon", tuman="xonabod", telegram_id=call.from_user.id)
    andijon_old['inline_keyboard'][4][2]['text'] = "✅ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xonabod"
    a=await db.select_all_driver_info()
    print(a)
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(menu_callback.filter(item_name='yolovchibolibdavometish'))
async def yolovchi_bolish(call:CallbackQuery):
    menu = {
        "Yo'lovchi reys belgilash": 'texikerak',
        "Tayyor taksi": 'tayyortaksi',
        "Yuk yuborish kerak": 'yukyuborishkerak',
        "Tayyor yuk mashinasi": "tayyoryukmashinasi",
        "Pochta yuborish kerak": 'pochtayuborishkerak',
        "Tayyor pochta mashinasi": "tayyorpochtamashinasi",
        "Sayohatga mashina kerak": 'sayohatgamashina',
        "Tayyor sayohatga mashina": 'tayyorsayohatgamashina',
        "Mening buyurtmalarim": "meningbuyurtmalarim",
        "Admin bilan bog'lanish": "adminbilanboglanish",
        "Haydovchi bo'lib davom etish": "haydovchibolibdavometish"

    }
    umumiy_menu = InlineKeyboardMarkup(row_width=2)
    for key, value in menu.items():
        umumiy_menu.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Salom Yo'lovchi !!\nSizga kerakli Xizmat turini tanlang.",reply_markup=umumiy_menu)