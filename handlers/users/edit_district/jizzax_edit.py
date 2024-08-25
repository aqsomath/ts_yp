from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup,State

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,jizzax_callback
from keyboards.inline.yolovchi.jizztuman import jizzax_tumanlari

class JizzaxStates(StatesGroup):
    jizzax=State()
    jizzax_eng_birinchi=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='zzax'),state=SozlamalarStates.viloyat_filter)
async def jizzax_edit(call: CallbackQuery):
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Jizzaxning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ",reply_markup=shaxsiy_jizzax)
        await JizzaxStates.jizzax.set()
        await call.message.delete()
@dp.callback_query_handler(state=JizzaxStates.jizzax)
async def jizzax_state(call:CallbackQuery,state:FSMContext):

    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Jizzax", tuman="jizzax shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="arnasoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="baxmal tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="do'stlik tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="forish tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="g'allarol tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="sharof rashidov tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="mirzachol tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="paxtakor tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="yangi obod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zomin tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zafarobod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zarbdor tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_jizzax)

    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Jizzax", tuman="jizzax shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="arnasoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="baxmal tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="do'stlik tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="forish tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="g'allarol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="sharof rashidov tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="mirzachol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="paxtakor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="yangi obod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zomin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zafarobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zarbdor tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_jizzax)

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
    jizzax={}
    if "jizzax shahar" in list:
        jizzax["✅Jizzax shahri"] = "jizzax shahar"
    else:
        jizzax["❌Jizzax shahri"] = "jizzax shahar"
    if "arnasoy tumani" in list:
        jizzax["✅Arnasoy"] = "arnasoy tumani"
    else:
        jizzax["❌Arnasoy"] = "arnasoy tumani"
    if "baxmal tumani" in list:
        jizzax["✅Baxmal"] = "baxmal tumani"
    else:
        jizzax["❌Baxmal"] = "baxmal tumani"
    if "do'stlik tumani" in list:
        jizzax["✅Doʻstlik"] = "do'stlik tumani"
    else:
        jizzax["❌Doʻstlik"] = "do'stlik tumani"
    if "forish tumani" in list:
        jizzax["✅Forish"] = 'forish tumani'
    else:
        jizzax["❌Forish"] = 'forish tumani'
    if "g'allarol tumani" in list:
        jizzax["✅Gʻallaorol"] = "g'allarol tumani"
    else:
        jizzax["❌Gʻallaorol"] = "g'allarol tumani"
    if "sharof rashidov tumani" in list:
        jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
    else:
        jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
    if "mirzachol tumani" in list:
        jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
    else:
        jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
    if "paxtakor tumani" in list:
        jizzax["✅Paxtakor"] = "paxtakor tumani"
    else:
        jizzax["❌Paxtakor"] = "paxtakor tumani"
    if "yangi obod tumani" in list:
        jizzax["✅Yangiobod"] = "yangi obod tumani"
    else:
        jizzax["❌Yangiobod"] = 'yangi obod tumani'
    if "zomin tumani" in list:
        jizzax["✅Zomin"] = "zomin tumani"
    else:
        jizzax["❌Zomin"] = "zomin tumani"
    if "zafarobod tumani" in list:
        jizzax["✅Zafarobod"] = "zafarobod tumani"
    else:
        jizzax["❌Zafarobod"] = "zafarobod tumani"
    if "zarbdor tumani" in list:
        jizzax["✅Zarbdor"] = "zarbdor tumani"
    else:
        jizzax["❌Zarbdor"] = "zarbdor tumani"
    shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
    for key, value in jizzax.items():
        shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in jizzax.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_jizzax)
            await JizzaxStates.jizzax.set()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='zzax'),state=EngBirinchiSozlamaState.viloyat_filter)
async def jizzax_edit(call: CallbackQuery):
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Jizzaxning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ",reply_markup=shaxsiy_jizzax)
        await JizzaxStates.jizzax_eng_birinchi.set()
        await call.message.delete()
@dp.callback_query_handler(state=JizzaxStates.jizzax_eng_birinchi)
async def jizzax_state(call:CallbackQuery,state:FSMContext):

    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Jizzax", tuman="jizzax shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="arnasoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="baxmal tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="do'stlik tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="forish tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="g'allarol tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="sharof rashidov tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="mirzachol tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="paxtakor tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="yangi obod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zomin tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zafarobod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Jizzax", tuman="zarbdor tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_jizzax)

    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Jizzax", tuman="jizzax shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="arnasoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="baxmal tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="do'stlik tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="forish tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="g'allarol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="sharof rashidov tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="mirzachol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="paxtakor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="yangi obod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zomin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zafarobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zarbdor tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        jizzax = {}
        if "jizzax shahar" in list:
            jizzax["✅Jizzax shahri"] = "jizzax shahar"
        else:
            jizzax["❌Jizzax shahri"] = "jizzax shahar"
        if "arnasoy tumani" in list:
            jizzax["✅Arnasoy"] = "arnasoy tumani"
        else:
            jizzax["❌Arnasoy"] = "arnasoy tumani"
        if "baxmal tumani" in list:
            jizzax["✅Baxmal"] = "baxmal tumani"
        else:
            jizzax["❌Baxmal"] = "baxmal tumani"
        if "do'stlik tumani" in list:
            jizzax["✅Doʻstlik"] = "do'stlik tumani"
        else:
            jizzax["❌Doʻstlik"] = "do'stlik tumani"
        if "forish tumani" in list:
            jizzax["✅Forish"] = 'forish tumani'
        else:
            jizzax["❌Forish"] = 'forish tumani'
        if "g'allarol tumani" in list:
            jizzax["✅Gʻallaorol"] = "g'allarol tumani"
        else:
            jizzax["❌Gʻallaorol"] = "g'allarol tumani"
        if "sharof rashidov tumani" in list:
            jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
        else:
            jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
        if "mirzachol tumani" in list:
            jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
        else:
            jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
        if "paxtakor tumani" in list:
            jizzax["✅Paxtakor"] = "paxtakor tumani"
        else:
            jizzax["❌Paxtakor"] = "paxtakor tumani"
        if "yangi obod tumani" in list:
            jizzax["✅Yangiobod"] = "yangi obod tumani"
        else:
            jizzax["❌Yangiobod"] = 'yangi obod tumani'
        if "zomin tumani" in list:
            jizzax["✅Zomin"] = "zomin tumani"
        else:
            jizzax["❌Zomin"] = "zomin tumani"
        if "zafarobod tumani" in list:
            jizzax["✅Zafarobod"] = "zafarobod tumani"
        else:
            jizzax["❌Zafarobod"] = "zafarobod tumani"
        if "zarbdor tumani" in list:
            jizzax["✅Zarbdor"] = "zarbdor tumani"
        else:
            jizzax["❌Zarbdor"] = "zarbdor tumani"
        shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
        for key, value in jizzax.items():
            shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_jizzax)

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
    jizzax={}
    if "jizzax shahar" in list:
        jizzax["✅Jizzax shahri"] = "jizzax shahar"
    else:
        jizzax["❌Jizzax shahri"] = "jizzax shahar"
    if "arnasoy tumani" in list:
        jizzax["✅Arnasoy"] = "arnasoy tumani"
    else:
        jizzax["❌Arnasoy"] = "arnasoy tumani"
    if "baxmal tumani" in list:
        jizzax["✅Baxmal"] = "baxmal tumani"
    else:
        jizzax["❌Baxmal"] = "baxmal tumani"
    if "do'stlik tumani" in list:
        jizzax["✅Doʻstlik"] = "do'stlik tumani"
    else:
        jizzax["❌Doʻstlik"] = "do'stlik tumani"
    if "forish tumani" in list:
        jizzax["✅Forish"] = 'forish tumani'
    else:
        jizzax["❌Forish"] = 'forish tumani'
    if "g'allarol tumani" in list:
        jizzax["✅Gʻallaorol"] = "g'allarol tumani"
    else:
        jizzax["❌Gʻallaorol"] = "g'allarol tumani"
    if "sharof rashidov tumani" in list:
        jizzax["✅Sharof Rashidov"] = "sharof rashidov tumani"
    else:
        jizzax["❌Sharof Rashidov"] = 'sharof rashidov tumani'
    if "mirzachol tumani" in list:
        jizzax["✅Mirzachoʻl"] = "mirzachol tumani"
    else:
        jizzax["❌Mirzachoʻl"] = 'mirzachol tumani'
    if "paxtakor tumani" in list:
        jizzax["✅Paxtakor"] = "paxtakor tumani"
    else:
        jizzax["❌Paxtakor"] = "paxtakor tumani"
    if "yangi obod tumani" in list:
        jizzax["✅Yangiobod"] = "yangi obod tumani"
    else:
        jizzax["❌Yangiobod"] = 'yangi obod tumani'
    if "zomin tumani" in list:
        jizzax["✅Zomin"] = "zomin tumani"
    else:
        jizzax["❌Zomin"] = "zomin tumani"
    if "zafarobod tumani" in list:
        jizzax["✅Zafarobod"] = "zafarobod tumani"
    else:
        jizzax["❌Zafarobod"] = "zafarobod tumani"
    if "zarbdor tumani" in list:
        jizzax["✅Zarbdor"] = "zarbdor tumani"
    else:
        jizzax["❌Zarbdor"] = "zarbdor tumani"
    shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
    for key, value in jizzax.items():
        shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in jizzax.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_jizzax)
            await JizzaxStates.jizzax_eng_birinchi.set()

