from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import EngBirinchiSozlamaState, EngBirinchiSozlamaState
from handlers.users.tariflar.asosiy import first, second, third
from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback,menu_callback
from keyboards.inline.yolovchi.kirish import kirish
from keyboards.inline.yolovchi.viloyatlar import viloyatlar, viloyatlar_eng_birinchi
from loader import dp,db


@dp.callback_query_handler(viloyatlar_callback.filter(item_name='nazad'),state=EngBirinchiSozlamaState.viloyat_filter)
async def eng_birinchi(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
    await state.finish()

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='yakunlash'),state=EngBirinchiSozlamaState.viloyat_filter)
async def eng_birinchi_next(call:CallbackQuery,state:FSMContext):
    driver = await db.select_driver(telegram_id=call.from_user.id)
    tur = {}
    if driver[1]==True:
        tur["✅Odam tashiman"] = "odam"
    else:
        tur["Odam tashiman"] = "odam"
    if driver[2]==True:
        tur["✅Yuk tashiman"] = "yuk"
    else:
        tur["Yuk tashiman"] = "yuk"
    if driver[3]==True:
        tur["✅Pochta tashiman"] = "pochta"
    else:
        tur["Pochta tashiman"] = "pochta"
    if driver[5]==True:
        tur["✅Sayohatchi tashiman"] = "sayohat"
    else:
        tur["Sayohatchi tashiman"] = "sayohat"
    tur["Ortga"] = 'ortga'
    tur["Bosh menu"] = 'boshmenu'
    haydovchi_tur = InlineKeyboardMarkup(row_width=2)
    for key, value in tur.items():
        haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
    await call.message.answer("Siz aynan nima tashisiz ?\n✅ - tanlangan\n❌- tanlanmagan", reply_markup=haydovchi_tur)
    await EngBirinchiSozlamaState.haydovchi_tur.set()
    await call.message.delete()


@dp.callback_query_handler(state=EngBirinchiSozlamaState.haydovchi_tur)
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
        await EngBirinchiSozlamaState.haydovchi_tur.set()

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
        await EngBirinchiSozlamaState.haydovchi_tur.set()

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
        await EngBirinchiSozlamaState.haydovchi_tur.set()
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
        await EngBirinchiSozlamaState.haydovchi_tur.set()


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
        await call.message.answer("O'zingiz faoliyat qiladigan hududingizni va belgilang",
                                  reply_markup=viloyatlar_eng_birinchi)
        await EngBirinchiSozlamaState.viloyat_filter.set()
        await call.message.delete()