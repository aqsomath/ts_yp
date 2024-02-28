from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,navoiy_callback
from keyboards.inline.yolovchi.navoiytuman import navoiy_tumanlari
class NavoiyStates(StatesGroup):
    navoiy=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='voyy'),state=SozlamalarStates.viloyat_filter)
async def xorazm_edit(call: CallbackQuery):


        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        navoiy = {}
        if "navoiy shahar" in list:
            navoiy["✅Navoiy shahri"] = "navoiy shahar"
        else:
            navoiy["❌Navoiy shahri"] = "navoiy shahar"
        if "zarafshon shahar" in list:
            navoiy["✅Zarafshon shahri"] = "zarafshon shahar"
        else:
            navoiy["❌Zarafshon shahri"] = "zarafshon shahar"
        if "konimex tumani" in list:
            navoiy["✅Konimex"] = "konimex tumani"
        else:
            navoiy["❌Konimex"] = "konimex tumani"
        if "karmana tumani" in list:
            navoiy["✅Karmana"] = "karmana tumani"
        else:
            navoiy["❌Karmana"] = "karmana tumani"
        if "qiziltepa tumani" in list:
            navoiy["✅Qiziltepa"] = "qiziltepa tumani"
        else:
            navoiy["❌Qiziltepa"] = "qiziltepa tumani"
        if "xatirchi tumani" in list:
            navoiy["✅Xatirchi"] = 'xatirchi tumani'
        else:
            navoiy["❌Xatirchi"] = 'xatirchi tumani'
        if "navbahor tumani" in list:
            navoiy["✅Navbahor"] = 'navbahor tumani'
        else:
            navoiy["❌Navbahor"] = 'navbahor tumani'
        if "nurota tumani" in list:
            navoiy["✅Nurota"] = "nurota tumani"
        else:
            navoiy["❌Nurota"] = "nurota tumani"
        if "tomdi tumani" in list:
            navoiy["✅Tomdi"] = "tomdi tumani"
        else:
            navoiy["❌Tomdi"] = 'tomdi tumani'
        if "uchquduq tumani" in list:
            navoiy["✅Uchquduq"] = "uchquduq tumani"
        else:
            navoiy["❌Uchquduq"] = "uchquduq tumani"

        shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
        for key, value in navoiy.items():
            shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Navoiyning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_navoiy)

        await NavoiyStates.navoiy.set()
        await call.message.delete()
@dp.callback_query_handler(state=NavoiyStates.navoiy)
async def navoiy_state(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Navoiy", tuman="navoiy shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="zarafshon shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="konimex tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="karmana tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="qiziltepa tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="xatirchi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="navbahor tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="nurota tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="tomdi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Navoiy", tuman="uchquduq tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        navoiy = {}
        if "navoiy shahar" in list:
            navoiy["✅Navoiy shahri"] = "navoiy shahar"
        else:
            navoiy["❌Navoiy shahri"] = "navoiy shahar"
        if "zarafshon shahar" in list:
            navoiy["✅Zarafshon shahri"] = "zarafshon shahar"
        else:
            navoiy["❌Zarafshon shahri"] = "zarafshon shahar"
        if "konimex tumani" in list:
            navoiy["✅Konimex"] = "konimex tumani"
        else:
            navoiy["❌Konimex"] = "konimex tumani"
        if "karmana tumani" in list:
            navoiy["✅Karmana"] = "karmana tumani"
        else:
            navoiy["❌Karmana"] = "karmana tumani"
        if "qiziltepa tumani" in list:
            navoiy["✅Qiziltepa"] = "qiziltepa tumani"
        else:
            navoiy["❌Qiziltepa"] = "qiziltepa tumani"
        if "xatirchi tumani" in list:
            navoiy["✅Xatirchi"] = 'xatirchi tumani'
        else:
            navoiy["❌Xatirchi"] = 'xatirchi tumani'
        if "navbahor tumani" in list:
            navoiy["✅Navbahor"] = 'navbahor tumani'
        else:
            navoiy["❌Navbahor"] = 'navbahor tumani'
        if "nurota tumani" in list:
            navoiy["✅Nurota"] = "nurota tumani"
        else:
            navoiy["❌Nurota"] = "nurota tumani"
        if "tomdi tumani" in list:
            navoiy["✅Tomdi"] = "tomdi tumani"
        else:
            navoiy["❌Tomdi"] = 'tomdi tumani'
        if "uchquduq tumani" in list:
            navoiy["✅Uchquduq"] = "uchquduq tumani"
        else:
            navoiy["❌Uchquduq"] = "uchquduq tumani"

        shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
        for key, value in navoiy.items():
            shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_navoiy)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Navoiy", tuman="navoiy shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="zarafshon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="konimex tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="karmana tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="qiziltepa tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="xatirchi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="navbahor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="nurota tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="tomdi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="uchquduq tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        navoiy = {}
        if "navoiy shahar" in list:
            navoiy["✅Navoiy shahri"] = "navoiy shahar"
        else:
            navoiy["❌Navoiy shahri"] = "navoiy shahar"
        if "zarafshon shahar" in list:
            navoiy["✅Zarafshon shahri"] = "zarafshon shahar"
        else:
            navoiy["❌Zarafshon shahri"] = "zarafshon shahar"
        if "konimex tumani" in list:
            navoiy["✅Konimex"] = "konimex tumani"
        else:
            navoiy["❌Konimex"] = "konimex tumani"
        if "karmana tumani" in list:
            navoiy["✅Karmana"] = "karmana tumani"
        else:
            navoiy["❌Karmana"] = "karmana tumani"
        if "qiziltepa tumani" in list:
            navoiy["✅Qiziltepa"] = "qiziltepa tumani"
        else:
            navoiy["❌Qiziltepa"] = "qiziltepa tumani"
        if "xatirchi tumani" in list:
            navoiy["✅Xatirchi"] = 'xatirchi tumani'
        else:
            navoiy["❌Xatirchi"] = 'xatirchi tumani'
        if "navbahor tumani" in list:
            navoiy["✅Navbahor"] = 'navbahor tumani'
        else:
            navoiy["❌Navbahor"] = 'navbahor tumani'
        if "nurota tumani" in list:
            navoiy["✅Nurota"] = "nurota tumani"
        else:
            navoiy["❌Nurota"] = "nurota tumani"
        if "tomdi tumani" in list:
            navoiy["✅Tomdi"] = "tomdi tumani"
        else:
            navoiy["❌Tomdi"] = 'tomdi tumani'
        if "uchquduq tumani" in list:
            navoiy["✅Uchquduq"] = "uchquduq tumani"
        else:
            navoiy["❌Uchquduq"] = "uchquduq tumani"

        shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
        for key, value in navoiy.items():
            shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_navoiy)

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
    navoiy = {}
    if "navoiy shahar" in list:
        navoiy["✅Navoiy shahri"] = "navoiy shahar"
    else:
        navoiy["❌Navoiy shahri"] = "navoiy shahar"
    if "zarafshon shahar" in list:
        navoiy["✅Zarafshon shahri"] = "zarafshon shahar"
    else:
        navoiy["❌Zarafshon shahri"] = "zarafshon shahar"
    if "konimex tumani" in list:
        navoiy["✅Konimex"] = "konimex tumani"
    else:
        navoiy["❌Konimex"] = "konimex tumani"
    if "karmana tumani" in list:
        navoiy["✅Karmana"] = "karmana tumani"
    else:
        navoiy["❌Karmana"] = "karmana tumani"
    if "qiziltepa tumani" in list:
        navoiy["✅Qiziltepa"] = "qiziltepa tumani"
    else:
        navoiy["❌Qiziltepa"] = "qiziltepa tumani"
    if "xatirchi tumani" in list:
        navoiy["✅Xatirchi"] = 'xatirchi tumani'
    else:
        navoiy["❌Xatirchi"] = 'xatirchi tumani'
    if "navbahor tumani" in list:
        navoiy["✅Navbahor"] = 'navbahor tumani'
    else:
        navoiy["❌Navbahor"] = 'navbahor tumani'
    if "nurota tumani" in list:
        navoiy["✅Nurota"] = "nurota tumani"
    else:
        navoiy["❌Nurota"] = "nurota tumani"
    if "tomdi tumani" in list:
        navoiy["✅Tomdi"] = "tomdi tumani"
    else:
        navoiy["❌Tomdi"] = 'tomdi tumani'
    if "uchquduq tumani" in list:
        navoiy["✅Uchquduq"] = "uchquduq tumani"
    else:
        navoiy["❌Uchquduq"] = "uchquduq tumani"

    shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
    for key, value in navoiy.items():
        shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    for key, value in navoiy.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_navoiy)
            await NavoiyStates.navoiy.set()
