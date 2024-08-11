from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, namangan_callback

class NamanganStates(StatesGroup):
    namangan=State()
    namanga_eng_birinchi=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='gann'),state=SozlamalarStates.viloyat_filter)
async def namangan_edit(call: CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Namanganning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_namangan)

        await NamanganStates.namangan.set()
        await call.message.delete()


@dp.callback_query_handler(state=NamanganStates.namangan)
async def namangan_state(call:CallbackQuery,state:FSMContext):

    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Namangan", tuman="chortoq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="chust tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="kosonsoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="mingbuloq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="namangan shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="namangan tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="norin tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="pop tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="toraqo'rg'on tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="uychi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="yangi namangan tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_namangan)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Namangan", tuman="chortoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="chust tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="kosonsoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="mingbuloq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="norin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="pop tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="toraqo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uychi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi namangan tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_namangan)

    if call.data == "qaytish":
        await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)
        await SozlamalarStates.viloyat_filter.set()
        await call.message.delete()

    if call.data == "boshmenu":
        await call.message.answer("Sizga kerakli xizmat turini tanlang !!!", reply_markup=umumiy_menu_1)
        await call.message.delete()
        await state.finish()
    list_1 = []
    jami = await db.select_all_driver_info()
    for i in jami:
        if i[3] == call.from_user.id:
            list_1.append(i[2])
    if call.data in list_1:
        await db.delete_driver_info(telegram_id=call.from_user.id, tuman=call.data)
    else:
        await db.add_driver_info(viloyat="Farg'ona", telegram_id=call.from_user.id, tuman=call.data)
    jamii = await db.select_all_driver_info()
    list = []
    for i in jamii:
        if i[3] == call.from_user.id:
            list.append(i[2])
    namangan = {}
    if "namangan shahar" in list:
        namangan["✅Namangan shaxar"] = 'namangan shahar'
    else:
        namangan["❌Namangan shaxar"] = 'namangan shahar'
    if "namangan tumani" in list:
        namangan["✅Namangan tuman"] = 'namangan tumani'
    else:
        namangan["❌Namangan tuman"] = 'namangan tumani'
    if "chortoq tumani" in list:
        namangan["✅Chortoq"] = "chortoq tumani"
    else:
        namangan["❌Chortoq"] = "chortoq tumani"
    if "chust tumani" in list:
        namangan["✅Chust"] = 'chust tumani'
    else:
        namangan["❌Chust"] = 'chust tumani'
    if "kosonsoy tumani" in list:
        namangan["✅Kosonsoy"] = "kosonsoy tumani"
    else:
        namangan["❌Kosonsoy"] = "kosonsoy tumani"
    if "mingbuloq tumani" in list:
        namangan["✅Mingbuloq"] = 'mingbuloq tumani'
    else:
        namangan["❌Mingbuloq"] = 'mingbuloq tumani'
    if "norin tumani" in list:
        namangan["✅Norin"] = "norin tumani"
    else:
        namangan["❌Norin"] = 'norin tumani'
    if "pop tumani" in list:
        namangan["✅Pop"] = "pop tumani"
    else:
        namangan["❌Pop"] = 'pop tumani'
    if "toraqo'rg'on tumani" in list:
        namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
    else:
        namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
    if "uchqo'rgo'n tumani" in list:
        namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
    else:
        namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
    if "uychi tumani" in list:
        namangan["✅Uychi"] = "uychi tumani"
    else:
        namangan["❌Uychi"] = "uychi tumani"
    if "yangi qo'rg'on tumani" in list:
        namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
    else:
        namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
    if "yangi namangan tumani" in list:
        namangan["✅Yangi Namangan"] = "yangi namangan tumani"
    else:
        namangan["❌Yangi Namangan"] = "yangi namangan tumani"
    shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
    for key, value in namangan.items():
        shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))


    for key, value in namangan.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_namangan)
            await NamanganStates.namangan.set()

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='gann'),state=EngBirinchiSozlamaState.viloyat_filter)
async def namangan_edit(call: CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Namanganning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_namangan)

        await NamanganStates.namanga_eng_birinchi.set()
        await call.message.delete()


@dp.callback_query_handler(state=NamanganStates.namanga_eng_birinchi)
async def namangan_state(call:CallbackQuery,state:FSMContext):

    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Namangan", tuman="chortoq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="chust tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="kosonsoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="mingbuloq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="namangan shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="namangan tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="norin tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="pop tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="toraqo'rg'on tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="uychi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Namangan", tuman="yangi namangan tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_namangan)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Namangan", tuman="chortoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="chust tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="kosonsoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="mingbuloq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="norin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="pop tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="toraqo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uychi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi namangan tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        namangan = {}
        if "namangan shahar" in list:
            namangan["✅Namangan shaxar"] = 'namangan shahar'
        else:
            namangan["❌Namangan shaxar"] = 'namangan shahar'
        if "namangan tumani" in list:
            namangan["✅Namangan tuman"] = 'namangan tumani'
        else:
            namangan["❌Namangan tuman"] = 'namangan tumani'
        if "chortoq tumani" in list:
            namangan["✅Chortoq"] = "chortoq tumani"
        else:
            namangan["❌Chortoq"] = "chortoq tumani"
        if "chust tumani" in list:
            namangan["✅Chust"] = 'chust tumani'
        else:
            namangan["❌Chust"] = 'chust tumani'
        if "kosonsoy tumani" in list:
            namangan["✅Kosonsoy"] = "kosonsoy tumani"
        else:
            namangan["❌Kosonsoy"] = "kosonsoy tumani"
        if "mingbuloq tumani" in list:
            namangan["✅Mingbuloq"] = 'mingbuloq tumani'
        else:
            namangan["❌Mingbuloq"] = 'mingbuloq tumani'
        if "norin tumani" in list:
            namangan["✅Norin"] = "norin tumani"
        else:
            namangan["❌Norin"] = 'norin tumani'
        if "pop tumani" in list:
            namangan["✅Pop"] = "pop tumani"
        else:
            namangan["❌Pop"] = 'pop tumani'
        if "toraqo'rg'on tumani" in list:
            namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
        else:
            namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
        if "uchqo'rgo'n tumani" in list:
            namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        else:
            namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
        if "uychi tumani" in list:
            namangan["✅Uychi"] = "uychi tumani"
        else:
            namangan["❌Uychi"] = "uychi tumani"
        if "yangi qo'rg'on tumani" in list:
            namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        else:
            namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
        if "yangi namangan tumani" in list:
            namangan["✅Yangi Namangan"] = "yangi namangan tumani"
        else:
            namangan["❌Yangi Namangan"] = "yangi namangan tumani"
        shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
        for key, value in namangan.items():
            shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_namangan)

    if call.data == "qaytish":
        await call.message.answer("O'zingiz faoliyat qiladigan hududingizni va belgilang", reply_markup=viloyatlar)
        await EngBirinchiSozlamaState.viloyat_filter.set()
        await call.message.delete()

    if call.data == "boshmenu":
        await call.message.answer("Sizga kerakli xizmat turini tanlang !!!", reply_markup=umumiy_menu_1)
        await call.message.delete()
        await state.finish()
    list_1 = []
    jami = await db.select_all_driver_info()
    for i in jami:
        if i[3] == call.from_user.id:
            list_1.append(i[2])
    if call.data in list_1:
        await db.delete_driver_info(telegram_id=call.from_user.id, tuman=call.data)
    else:
        await db.add_driver_info(viloyat="Farg'ona", telegram_id=call.from_user.id, tuman=call.data)
    jamii = await db.select_all_driver_info()
    list = []
    for i in jamii:
        if i[3] == call.from_user.id:
            list.append(i[2])
    namangan = {}
    if "namangan shahar" in list:
        namangan["✅Namangan shaxar"] = 'namangan shahar'
    else:
        namangan["❌Namangan shaxar"] = 'namangan shahar'
    if "namangan tumani" in list:
        namangan["✅Namangan tuman"] = 'namangan tumani'
    else:
        namangan["❌Namangan tuman"] = 'namangan tumani'
    if "chortoq tumani" in list:
        namangan["✅Chortoq"] = "chortoq tumani"
    else:
        namangan["❌Chortoq"] = "chortoq tumani"
    if "chust tumani" in list:
        namangan["✅Chust"] = 'chust tumani'
    else:
        namangan["❌Chust"] = 'chust tumani'
    if "kosonsoy tumani" in list:
        namangan["✅Kosonsoy"] = "kosonsoy tumani"
    else:
        namangan["❌Kosonsoy"] = "kosonsoy tumani"
    if "mingbuloq tumani" in list:
        namangan["✅Mingbuloq"] = 'mingbuloq tumani'
    else:
        namangan["❌Mingbuloq"] = 'mingbuloq tumani'
    if "norin tumani" in list:
        namangan["✅Norin"] = "norin tumani"
    else:
        namangan["❌Norin"] = 'norin tumani'
    if "pop tumani" in list:
        namangan["✅Pop"] = "pop tumani"
    else:
        namangan["❌Pop"] = 'pop tumani'
    if "toraqo'rg'on tumani" in list:
        namangan["✅To'raqo'rg'on"] = "toraqo'rg'on tumani"
    else:
        namangan["❌To'raqo'rg'on"] = "toraqo'rg'on tumani"
    if "uchqo'rgo'n tumani" in list:
        namangan["✅Uchqo'rg'on"] = "uchqo'rgo'n tumani"
    else:
        namangan["❌Uchqo'rg'on"] = "uchqo'rgo'n tumani"
    if "uychi tumani" in list:
        namangan["✅Uychi"] = "uychi tumani"
    else:
        namangan["❌Uychi"] = "uychi tumani"
    if "yangi qo'rg'on tumani" in list:
        namangan["✅Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
    else:
        namangan["❌Yangiqo'rg'on"] = "yangi qo'rg'on tumani"
    if "yangi namangan tumani" in list:
        namangan["✅Yangi Namangan"] = "yangi namangan tumani"
    else:
        namangan["❌Yangi Namangan"] = "yangi namangan tumani"
    shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
    for key, value in namangan.items():
        shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))


    for key, value in namangan.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_namangan)
            await NamanganStates.namanga_eng_birinchi.set()