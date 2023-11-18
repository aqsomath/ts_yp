from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback, andijon_callback, \
    menu_callback
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, bot,db


@dp.callback_query_handler(menu_callback.filter(item_name='nastroyki'))
async def sozlamalar(call:CallbackQuery):
    marrk=InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='fioprwoepwo'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='sdeif0003d'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ",reply_markup=marrk)


@dp.callback_query_handler(text="fioprwoepwo")
async def katta_filtr(call:CallbackQuery):
    mark=InlineKeyboardMarkup(row_width=2)
    mark.insert(InlineKeyboardButton(text="Haydovchi filter",callback_data="akjdie"))
    mark.insert(InlineKeyboardButton(text="Viloyat filter",callback_data="ewfsdddfs"))
    mark.insert(InlineKeyboardButton(text=" Ortga",callback_data="89d5dw"))
    mark.insert(InlineKeyboardButton(text="Bosh menu",callback_data="w699d3ww2"))
    await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
@dp.callback_query_handler(text="sdeif0003d")
async def my_report(call:CallbackQuery):
    await call.message.answer("Mening malumotlarim")

@dp.callback_query_handler(text=["w699d3ww2",'headmenu'])
async def back_home(call:CallbackQuery):
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
        "Sozlamalar": "nastroyki",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Sozlamalar bo'limi ",reply_markup=markup)
@dp.callback_query_handler(text="89d5dw")
async def my_report(call:CallbackQuery):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='fioprwoepwo'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='sdeif0003d'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='ddeff55g566'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ",reply_markup=marrk)

nima_tashisan=InlineKeyboardMarkup(row_width=2)
nima_tashisan.insert(InlineKeyboardButton(text="Yo'lovchi tashiman", callback_data="odamtashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Pochta tashiman", callback_data="pochtatashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Yuk tashiman", callback_data="yuktashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Sayohatchi tashiman", callback_data="sayohatchitashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Barchasi", callback_data="hammasinitashimantashiman"))
nima_tashisan.insert(InlineKeyboardButton(text="Yakunlash", callback_data="tugatish"))
nima_tashisan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaopoioo"))
nima_tashisan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="headmenu"))


@dp.callback_query_handler(text='qaopoioo')
async def sozla(call:CallbackQuery):
    mark = InlineKeyboardMarkup(row_width=2)
    mark.insert(InlineKeyboardButton(text="Haydovchi filter", callback_data="akjdie"))
    mark.insert(InlineKeyboardButton(text="Viloyat filter", callback_data="ewfsdddfs"))
    mark.insert(InlineKeyboardButton(text=" Ortga", callback_data="89d5dw"))
    mark.insert(InlineKeyboardButton(text="Bosh menu", callback_data="w699d3ww2"))
    await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
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
        "Sozlamalar": "nastroyki",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in driver.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
    await call.message.answer("Haydovchi!\nSiz tanlagan hizmat turi bo'yicha butun "
                              "O'zbekiston bo'yicha mijozlarning buyurtmalari sizga kelib turadi."
                              "O'zingizga mos hududlarni tanlash uchun 'Viloyalarni  filtrlashni' bosing.",reply_markup=markup)
@dp.callback_query_handler(text="akjdie")
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
@dp.callback_query_handler(text="ewfsdddfs")
async def select_hudud(call:CallbackQuery):
    await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='nazad'))
async def nazad(call:CallbackQuery):
    mark = InlineKeyboardMarkup(row_width=2)
    mark.insert(InlineKeyboardButton(text="Haydovchi filter", callback_data="akjdie"))
    mark.insert(InlineKeyboardButton(text="Viloyat filter", callback_data="ewfsdddfs"))
    mark.insert(InlineKeyboardButton(text=" Ortga", callback_data="89d5dw"))
    mark.insert(InlineKeyboardButton(text="Bosh menu", callback_data="w699d3ww2"))
    await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
