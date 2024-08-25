from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.tariflar.asosiy import first, second, third
from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback,menu_callback
from keyboards.inline.yolovchi.kirish import kirish
from keyboards.inline.yolovchi.viloyatlar import viloyatlar, viloyatlar_eng_birinchi
from loader import dp,db


class SozlamalarStates(StatesGroup):
    kirish=State()
    viloyat_filter=State()
    haydovchi_tur=State()
    my_info=State()
    tarifni_almashtirish=State()
    tarifni_tanlash=State()
class EngBirinchiSozlamaState(StatesGroup):
    kirish=State()
    viloyat_filter=State()
    haydovchi_tur=State()
    my_info=State()
    tarifni_almashtirish=State()
    tarifni_tanlash=State()

haydovchilar_royxati = []
@dp.callback_query_handler(kirish_callback.filter(item_name='haydovchi6656'))
async def haydovchif(call:CallbackQuery):
        haydovchilar_royxati.append(call.from_user.id)
        await db.haydovchi_set(haydovchi=True, telegram_id=call.from_user.id)
        await db.yolovchi_set(yolovchi=False, telegram_id=call.from_user.id)
        await db.add_haydovchi(username=call.from_user.username, telegram_id=call.from_user.id, balans=0)

        await db.add_driver(tashiman_odam=True, tashiman_pochta=True, tashiman_yuk=True,
                            sayohatchi_tashiman=True,
                            telegram_id=call.from_user.id)
        await call.message.answer("O'zingiz faoliyat qiladigan hududingizni va belgilang", reply_markup=viloyatlar_eng_birinchi)
        await EngBirinchiSozlamaState.viloyat_filter.set()
@dp.callback_query_handler(menu_callback.filter(item_name='nastroyki'))
async def sozlamalar(call:CallbackQuery):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ",reply_markup=marrk)
    await call.message.delete()

@dp.callback_query_handler(text="headmenu")
async def ortga_qarab_qoch(call:CallbackQuery,state:FSMContext):
    
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
        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await call.message.delete()
        await state.finish()
@dp.callback_query_handler(text="filtrlash")
async def katta_filtr(call:CallbackQuery,state:FSMContext):
    
        mark=InlineKeyboardMarkup(row_width=2)
        mark.insert(InlineKeyboardButton(text="Haydovchi filter",callback_data="haydovchifilter"))
        mark.insert(InlineKeyboardButton(text="Viloyat filter",callback_data="viloyatfilter"))
        mark.insert(InlineKeyboardButton(text=" Ortga",callback_data="ortga"))
        mark.insert(InlineKeyboardButton(text="Bosh menu",callback_data="headmenu"))
        await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
        await SozlamalarStates.kirish.set()
        await call.message.delete()

@dp.callback_query_handler(text="ortga",state=SozlamalarStates.kirish)
async def ortga(call:CallbackQuery,state:FSMContext):
    
        marrk = InlineKeyboardMarkup(row_width=2)
        marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
        marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
        marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
        marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
        await call.message.answer("Sozlamalar bo'limi ", reply_markup=marrk)
        await state.finish()
        await call.message.delete()

@dp.callback_query_handler(text="headmenu", state=SozlamalarStates.kirish)
async def ortga(call: CallbackQuery, state: FSMContext):
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
    await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
    await call.message.delete()
    await state.finish()

@dp.callback_query_handler(text="haydovchifilter",state=SozlamalarStates.kirish)
async def haydovchi_filter(call:CallbackQuery,state:FSMContext):
    
        driver = await db.select_driver(telegram_id=call.from_user.id)
        tur={}
        if driver[1] == True:
            tur["✅Odam tashiman"] = "odam"
        else:
            tur["Odam tashiman"] = "odam"
        if driver[2] == True:
            tur["✅Yuk tashiman"] = "yuk"
        else:
            tur["Yuk tashiman"] = "yuk"
        if driver[3] == True:
            tur["✅Pochta tashiman"] = "pochta"
        else:
            tur["Pochta tashiman"] = "pochta"
        if driver[5] == True:
            tur["✅Sayohatchi tashiman"] = "sayohat"
        else:
            tur["Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"] = 'ortga'
        tur["Bosh menu"] = 'boshmenu'
        haydovchi_tur=InlineKeyboardMarkup(row_width=2)
        for key,value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key,callback_data=value))
        await call.message.answer("Siz aynan nima tashisiz ?\n✅ - tanlangan\n❌- tanlanmagan",reply_markup=haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()
        await call.message.delete()

@dp.callback_query_handler(state=SozlamalarStates.haydovchi_tur)
async def nimatashiman(call: CallbackQuery, state: FSMContext):
    driver = await db.select_driver(telegram_id=call.from_user.id)

    if call.data == "odam":
        tur = {}
        if driver[1] == True:
            await db.update_odam_tashish(tashiman_odam=False,telegram_id=call.from_user.id)
            tur["Odam tashiman"] = "odam"
        else:
            await db.update_odam_tashish(tashiman_odam=True,telegram_id=call.from_user.id)
            tur["✅Odam tashiman"] = "odam"
        if driver[2] == True:
            tur["✅Yuk tashiman"] = "yuk"
        else:
            tur["Yuk tashiman"] = "yuk"
        if driver[3] == True:
            tur["✅Pochta tashiman"] = "pochta"
        else:
            tur["Pochta tashiman"] = "pochta"
        if driver[5] == True:
            tur["✅Sayohatchi tashiman"] = "sayohat"
        else:
            tur["Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"] = 'ortga'
        tur["Bosh menu"] = 'boshmenu'

        haydovchi_tur = InlineKeyboardMarkup(row_width=2)
        for key, value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.edit_reply_markup(haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()

    if call.data == "yuk":
        tur = {}
        if driver[1] == True:
            tur["✅Odam tashiman"] = "odam"
        else:
            tur["Odam tashiman"] = "odam"
        if driver[2] == True:
            await db.update_tashiman_yuk(tashiman_yuk=False,telegram_id=call.from_user.id)
            tur["Yuk tashiman"] = "yuk"
        else:
            await db.update_tashiman_yuk(tashiman_yuk=True, telegram_id=call.from_user.id)
            tur["✅Yuk tashiman"] = "yuk"
        if driver[3] == True:
            tur["✅Pochta tashiman"] = "pochta"
        else:
            tur["Pochta tashiman"] = "pochta"
        if driver[5] == True:
            tur["✅Sayohatchi tashiman"] = "sayohat"
        else:
            tur["Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"] = 'ortga'
        tur["Bosh menu"] = 'boshmenu'
        haydovchi_tur = InlineKeyboardMarkup(row_width=2)
        for key, value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.edit_reply_markup(haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()

    if call.data == "pochta":

        tur = {}
        if driver[1] == True:
            tur["✅Odam tashiman"] = "odam"
        else:
            tur["Odam tashiman"] = "odam"
        if driver[2] == True:
            tur["✅Yuk tashiman"] = "yuk"
        else:
            tur["Yuk tashiman"] = "yuk"
        if driver[3] == True:
            await db.update_tashiman_pochta(tashiman_pochta=False, telegram_id=call.from_user.id)
            tur["Pochta tashiman"] = "pochta"
        else:
            await db.update_tashiman_pochta(tashiman_pochta=True, telegram_id=call.from_user.id)
            tur["✅Pochta tashiman"] = "pochta"
        if driver[5] == True:
            tur["✅Sayohatchi tashiman"] = "sayohat"
        else:
            tur["Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"] = 'ortga'
        tur["Bosh menu"] = 'boshmenu'
        haydovchi_tur = InlineKeyboardMarkup(row_width=2)
        for key, value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.edit_reply_markup(haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()
    if call.data == "sayohat":
        tur = {}
        if driver[1] == True:
            tur["✅Odam tashiman"] = "odam"
        else:
            tur["Odam tashiman"] = "odam"
        if driver[2] == True:
            tur["✅Yuk tashiman"] = "yuk"
        else:
            tur["Yuk tashiman"] = "yuk"
        if driver[3] == True:
            tur["✅Pochta tashiman"] = "pochta"
        else:
            tur["Pochta tashiman"] = "pochta"
        if driver[5] == True:
            await db.update_odam_sayohat(sayohatchi_tashiman=False, telegram_id=call.from_user.id)
            tur["Sayohatchi tashiman"] = "sayohat"
        else:
            await db.update_odam_sayohat(sayohatchi_tashiman=True, telegram_id=call.from_user.id)
            tur["✅Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"] = 'ortga'
        tur["Bosh menu"] = 'boshmenu'
        haydovchi_tur = InlineKeyboardMarkup(row_width=2)
        for key, value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.edit_reply_markup(haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()


    if call.data == "boshmenu":
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
        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await call.message.delete()
        await state.finish()
    if call.data == "ortga":
        mark = InlineKeyboardMarkup(row_width=2)
        mark.insert(InlineKeyboardButton(text="Haydovchi filter", callback_data="haydovchifilter"))
        mark.insert(InlineKeyboardButton(text="Viloyat filter", callback_data="viloyatfilter"))
        mark.insert(InlineKeyboardButton(text=" Ortga", callback_data="ortga"))
        mark.insert(InlineKeyboardButton(text="Bosh menu", callback_data="headmenu"))
        await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
        await SozlamalarStates.kirish.set()
        await call.message.delete()
@dp.callback_query_handler(text="viloyatfilter",state=SozlamalarStates.kirish)
async def viloyat_filter(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)
        await SozlamalarStates.viloyat_filter.set()
        await call.message.delete()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='nazad'),state=SozlamalarStates.viloyat_filter)
async def katta_filtr(call:CallbackQuery,state:FSMContext):
    
        mark=InlineKeyboardMarkup(row_width=2)
        mark.insert(InlineKeyboardButton(text="Haydovchi filter",callback_data="haydovchifilter"))
        mark.insert(InlineKeyboardButton(text="Viloyat filter",callback_data="viloyatfilter"))
        mark.insert(InlineKeyboardButton(text=" Ortga",callback_data="ortga"))
        mark.insert(InlineKeyboardButton(text="Bosh menu",callback_data="boshmenu"))
        await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
        await call.message.delete()
        await SozlamalarStates.kirish.set()
@dp.callback_query_handler(text="meningmalumotlarim")
async def my_report(call:CallbackQuery,state:FSMContext):
    try:
        driver = await db.select_user(telegram_id=call.from_user.id)
        balans = driver[7]
        msg=(f"<b>Sizning ma'lumotlaringiz </b>\n\n"
             f"Haydovchi nomi :\n{call.from_user.full_name}\n\n"
             f"Haydovchi ID :\n{driver[0]}\n"
             f"Haydovchi telegram ID :\n{driver[3]} \n"
             f"Balans :{balans} \n"
            )
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Balansni to'ldirish", callback_data="balansnitoldirish"))
        markup.insert(InlineKeyboardButton(text="Tarifni almashtirish", callback_data="tarifnialmashtirish"))
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="ortgadasdasda"))
        markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="ortga"))
        await call.message.answer(msg,reply_markup=markup)
        await SozlamalarStates.my_info.set()
        await call.message.delete()
    except TypeError:
        await call.message.answer("Uzr bu bo'lim faqat haydovchilar uchun. Siz haydovchilar ro'yxatida yo'qsiz.")
        await call.message.delete()
@dp.callback_query_handler(state=SozlamalarStates.my_info,text="ortgadasdasda")
async def mening_malumotlarimga_qaytish(call:CallbackQuery,state:FSMContext):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ", reply_markup=marrk)
    await call.message.delete()
    await state.finish()
@dp.callback_query_handler(text="balansnitoldirish",state=SozlamalarStates.my_info)
async def balans_toldirish(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                              f"Telefon : +998 94 100 79 74\n"
                              f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")
    await state.finish()

@dp.callback_query_handler(text="tarifnialmashtirish",state=SozlamalarStates.my_info)
async def balans_toldirish(call:CallbackQuery,state:FSMContext):
    one = await db.select_tarif(tarif_name='first')
    msg_1 = f"Kuniga {one[3]}ta qabul qilish, oyiga - > {one[2]}"
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"Kuniga {two[3]}ta qabul qilish, oyiga - > {two[2]}"
    three = await db.select_tarif(tarif_name='third')
    msg_3 = f"Kuniga {three[3]}ta qabul qilish, oyiga - > {three[2]}"
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="1 - tarif",
                                       callback_data="birinchitarif"))
    markup.insert(InlineKeyboardButton(text="2 - tarif ",
                                       callback_data="ikkinchitarif"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",
                                       callback_data="uchinchitarif"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="backk"))
    await call.message.answer("Qaysi tarifga ulanmoqchisiz\n"
                              f"<b>1 - tarif </b>\n{msg_1}\n"
                              f"<b>2 - tarif </b>\n{msg_2}\n"
                              f"<b>3 - tarif </b>\n{msg_3}\n",
                              reply_markup=markup)
    await call.message.delete()
    await state.finish()

@dp.callback_query_handler(text="backk")
async def birinchiga(call:CallbackQuery,state:FSMContext):
    try:
        driver = await db.select_user(telegram_id=call.from_user.id)
        balans = driver[7]
        msg=(f"<b>Sizning ma'lumotlaringiz </b>\n\n"
             f"Haydovchi nomi :\n{call.from_user.full_name}\n\n"
             f"Haydovchi ID :\n{driver[0]}\n"
             f"Haydovchi telegram ID :\n{driver[3]} \n"
             f"Balans :{balans} \n"
            )
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Balansni to'ldirish", callback_data="balansnitoldirish"))
        markup.insert(InlineKeyboardButton(text="Tarifni almashtirish", callback_data="tarifnialmashtirish"))
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="ortga"))
        await call.message.answer(msg,reply_markup=markup)
        await SozlamalarStates.my_info.set()
        await call.message.delete()
    except TypeError:
        await call.message.answer("Uzr bu bo'lim faqat haydovchilar uchun. Siz haydovchilar ro'yxatida yo'qsiz.")
        await call.message.delete()
        await state.finish()

@dp.callback_query_handler(state=SozlamalarStates.my_info,text="ortga",)
async def ortga_qarab_qoch(call: CallbackQuery,state:FSMContext):
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
    await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
    await call.message.delete()
    await state.finish()

@dp.callback_query_handler(text="birinchitarif",state=SozlamalarStates.tarifni_almashtirish)
async def birinchiga(call:CallbackQuery,state:FSMContext):
    haydovchi = await db.select_user(telegram_id=call.from_user.id)
    haydovchi_balansi = haydovchi[7]
    tarif = await db.select_tarif(tarif_name='first')
    if haydovchi_balansi >= tarif[2]:
        await db.update_balans(balans=haydovchi_balansi - tarif[2], telegram_id=call.from_user.id)
        first.append(call.from_user.id)
        await call.message.answer("Siz birinchi tarifga muvaffaqiyatli qo'shildingiz !")
        await state.finish()
    else:
        await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                                  f"Telefon : +998 94 100 79 74\n"
                                  f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")
        await state.finish()

@dp.callback_query_handler(text="ikkinchitarif",state=SozlamalarStates.tarifni_almashtirish)
async def ikkinchiga(call:CallbackQuery,state:FSMContext):
    haydovchi = await db.select_user(telegram_id=call.from_user.id)
    haydovchi_balansi = haydovchi[7]
    tarif = await db.select_tarif(tarif_name='second')
    if haydovchi_balansi >= tarif[2]:
        await db.update_balans(balans=haydovchi_balansi - tarif[2], telegram_id=call.from_user.id)
        second.append(call.from_user.id)
        await call.message.answer("Siz ikkinchi tarifga muvaffaqiyatli qo'shildingiz !")
        await state.finish()

    else:
        await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                                  f"Telefon : +998 94 100 79 74\n"
                                  f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")
        await state.finish()

@dp.callback_query_handler(text="uchinchitarif",state=SozlamalarStates.tarifni_almashtirish)
async def tariflar_uchun(call:CallbackQuery,state:FSMContext):
    haydovchi = await db.select_user(telegram_id=call.from_user.id)
    haydovchi_balansi = haydovchi[7]
    tarif = await db.select_tarif(tarif_name='third')
    print(tarif[2])
    print(type(tarif[2]))
    if haydovchi_balansi >= tarif[2]:
        await db.update_balans(balans=haydovchi_balansi - tarif[2], telegram_id=call.from_user.id)
        third.append(call.from_user.id)
        await call.message.answer("Siz uchinchi tarifga muvaffaqiyatli qo'shildingiz !")
        await state.finish()

    else:
        await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                                  f"Telefon : +998 94 100 79 74\n"
                                  f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")
        await state.finish()


