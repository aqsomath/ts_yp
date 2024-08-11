from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup,State

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback


class SamarqandStatesGroup(StatesGroup):
    samarqand=State()
    samarqand_eng_birinchi=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='marqa'),state=EngBirinchiSozlamaState.viloyat_filter)
async def jizzax_edit(call: CallbackQuery):


        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        samarqand = {}
        if "samarqand shahar" in list:
            samarqand["✅Samarqand shahar"] = "samarqand shahar"
        else:
            samarqand["❌Samarqand shahar"] = "samarqand shahar"
        if "samarqand tumani" in list:
            samarqand["✅Samarqand tuman"] = "samarqand tumani"
        else:
            samarqand["❌Samarqand tuman"] = "samarqand tumani"
        if "bulungur tumani" in list:
            samarqand["✅Bulungʻur"] = "bulungur tumani"
        else:
            samarqand["❌Bulungʻur"] = "bulungur tumani"
        if "ishtixon tumani" in list:
            samarqand["✅Ishtixon"] = "ishtixon tumani"
        else:
            samarqand["❌Ishtixon"] = "ishtixon tumani"
        if "jomboy tumani" in list:
            samarqand["✅Jomboy"] = "jomboy tumani"
        else:
            samarqand["❌Jomboy"] = "jomboy tumani"
        if "kattaqorgon tumani" in list:
            samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        else:
            samarqand["❌Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        if "kattaqorgon shahar" in list:
            samarqand["✅Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        else:
            samarqand["❌Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        if "qoshrabot tumani" in list:
            samarqand["✅Qoʻshrabot"] = "qoshrabot tumani"
        else:
            samarqand["❌Qoʻshrabot"] = "qoshrabot tumani"
        if "narpay tumani" in list:
            samarqand["✅Narpay"] = "narpay tumani"
        else:
            samarqand["❌Narpay"] = 'narpay tumani'
        if "nurobod tumani" in list:
            samarqand["✅Nurobod"] = "nurobod tumani"
        else:
            samarqand["❌Nurobod"] = 'nurobod tumani'
        if "oqdaryo tumani" in list:
            samarqand["✅Oqdaryo"] = "oqdaryo tumani"
        else:
            samarqand["❌Oqdaryo"] = "oqdaryo tumani"
        if "paxtachi tumani" in list:
            samarqand["✅Paxtachi"] = "paxtachi tumani"
        else:
            samarqand["❌Paxtachi"] = 'paxtachi tumani'
        if "payariq tumani" in list:
            samarqand["✅Payariq"] = "payariq tumani"
        else:
            samarqand["❌Payariq"] = "payariq tumani"
        if "pastdargom tumani" in list:
            samarqand["✅Pastdargʻom"] = "pastdargom tumani"
        else:
            samarqand["❌Pastdargʻom"] = "pastdargom tumani"
        if "toyloq tumani" in list:
            samarqand["✅Toyloq"] = "toyloq tumani"
        else:
            samarqand["❌Toyloq"] = "toyloq tumani"
        shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
        for key, value in samarqand.items():
            shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Samarqandning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_samarqand)
        await SamarqandStatesGroup.samarqand_eng_birinchi.set()
        await call.message.delete()

@dp.callback_query_handler(state=SamarqandStatesGroup.samarqand_eng_birinchi)
async def samarqand_state(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Samarqand", tuman="bulungur tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="ishtixon tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="jomboy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="kattaqorgon shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="kattaqorgon tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="qoshrabot tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="narpay tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="nurobod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="oqdaryo tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="paxtachi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="payariq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="pastdargom tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="samarqand shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="samarqand tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Samarqand", tuman="toyloq tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        samarqand = {}
        if "samarqand shahar" in list:
            samarqand["✅Samarqand shahar"] = "samarqand shahar"
        else:
            samarqand["❌Samarqand shahar"] = "samarqand shahar"
        if "samarqand tumani" in list:
            samarqand["✅Samarqand tuman"] = "samarqand tumani"
        else:
            samarqand["❌Samarqand tuman"] = "samarqand tumani"
        if "bulungur tumani" in list:
            samarqand["✅Bulungʻur"] = "bulungur tumani"
        else:
            samarqand["❌Bulungʻur"] = "bulungur tumani"
        if "ishtixon tumani" in list:
            samarqand["✅Ishtixon"] = "ishtixon tumani"
        else:
            samarqand["❌Ishtixon"] = "ishtixon tumani"
        if "jomboy tumani" in list:
            samarqand["✅Jomboy"] = "jomboy tumani"
        else:
            samarqand["❌Jomboy"] = "jomboy tumani"
        if "kattaqorgon tumani" in list:
            samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        else:
            samarqand["❌Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        if "kattaqorgon shahar" in list:
            samarqand["✅Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        else:
            samarqand["❌Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        if "qoshrabot tumani" in list:
            samarqand["✅Qoʻshrabot"] = "qoshrabot tumani"
        else:
            samarqand["❌Qoʻshrabot"] = "qoshrabot tumani"
        if "narpay tumani" in list:
            samarqand["✅Narpay"] = "narpay tumani"
        else:
            samarqand["❌Narpay"] = 'narpay tumani'
        if "nurobod tumani" in list:
            samarqand["✅Nurobod"] = "nurobod tumani"
        else:
            samarqand["❌Nurobod"] = 'nurobod tumani'
        if "oqdaryo tumani" in list:
            samarqand["✅Oqdaryo"] = "oqdaryo tumani"
        else:
            samarqand["❌Oqdaryo"] = "oqdaryo tumani"
        if "paxtachi tumani" in list:
            samarqand["✅Paxtachi"] = "paxtachi tumani"
        else:
            samarqand["❌Paxtachi"] = 'paxtachi tumani'
        if "payariq tumani" in list:
            samarqand["✅Payariq"] = "payariq tumani"
        else:
            samarqand["❌Payariq"] = "payariq tumani"
        if "pastdargom tumani" in list:
            samarqand["✅Pastdargʻom"] = "pastdargom tumani"
        else:
            samarqand["❌Pastdargʻom"] = "pastdargom tumani"
        if "toyloq tumani" in list:
            samarqand["✅Toyloq"] = "toyloq tumani"
        else:
            samarqand["❌Toyloq"] = "toyloq tumani"
        shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
        for key, value in samarqand.items():
            shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_samarqand)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Samarqand", tuman="bulungur tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="ishtixon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="jomboy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="qoshrabot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="narpay tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="nurobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="oqdaryo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="paxtachi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="payariq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="pastdargom tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="samarqand shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="samarqand tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="toyloq tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        samarqand = {}
        if "samarqand shahar" in list:
            samarqand["✅Samarqand shahar"] = "samarqand shahar"
        else:
            samarqand["❌Samarqand shahar"] = "samarqand shahar"
        if "samarqand tumani" in list:
            samarqand["✅Samarqand tuman"] = "samarqand tumani"
        else:
            samarqand["❌Samarqand tuman"] = "samarqand tumani"
        if "bulungur tumani" in list:
            samarqand["✅Bulungʻur"] = "bulungur tumani"
        else:
            samarqand["❌Bulungʻur"] = "bulungur tumani"
        if "ishtixon tumani" in list:
            samarqand["✅Ishtixon"] = "ishtixon tumani"
        else:
            samarqand["❌Ishtixon"] = "ishtixon tumani"
        if "jomboy tumani" in list:
            samarqand["✅Jomboy"] = "jomboy tumani"
        else:
            samarqand["❌Jomboy"] = "jomboy tumani"
        if "kattaqorgon tumani" in list:
            samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        else:
            samarqand["❌Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
        if "kattaqorgon shahar" in list:
            samarqand["✅Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        else:
            samarqand["❌Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
        if "qoshrabot tumani" in list:
            samarqand["✅Qoʻshrabot"] = "qoshrabot tumani"
        else:
            samarqand["❌Qoʻshrabot"] = "qoshrabot tumani"
        if "narpay tumani" in list:
            samarqand["✅Narpay"] = "narpay tumani"
        else:
            samarqand["❌Narpay"] = 'narpay tumani'
        if "nurobod tumani" in list:
            samarqand["✅Nurobod"] = "nurobod tumani"
        else:
            samarqand["❌Nurobod"] = 'nurobod tumani'
        if "oqdaryo tumani" in list:
            samarqand["✅Oqdaryo"] = "oqdaryo tumani"
        else:
            samarqand["❌Oqdaryo"] = "oqdaryo tumani"
        if "paxtachi tumani" in list:
            samarqand["✅Paxtachi"] = "paxtachi tumani"
        else:
            samarqand["❌Paxtachi"] = 'paxtachi tumani'
        if "payariq tumani" in list:
            samarqand["✅Payariq"] = "payariq tumani"
        else:
            samarqand["❌Payariq"] = "payariq tumani"
        if "pastdargom tumani" in list:
            samarqand["✅Pastdargʻom"] = "pastdargom tumani"
        else:
            samarqand["❌Pastdargʻom"] = "pastdargom tumani"
        if "toyloq tumani" in list:
            samarqand["✅Toyloq"] = "toyloq tumani"
        else:
            samarqand["❌Toyloq"] = "toyloq tumani"
        shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
        for key, value in samarqand.items():
            shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_samarqand)

    if call.data == "qaytish":
        await call.message.answer("O'zingizga kerakli hududlarni tanlang", reply_markup=viloyatlar)
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
    samarqand = {}
    if "samarqand shahar" in list:
        samarqand["✅Samarqand shahar"] = "samarqand shahar"
    else:
        samarqand["❌Samarqand shahar"] = "samarqand shahar"
    if "samarqand tumani" in list:
        samarqand["✅Samarqand tuman"] = "samarqand tumani"
    else:
        samarqand["❌Samarqand tuman"] = "samarqand tumani"
    if "bulungur tumani" in list:
        samarqand["✅Bulungʻur"] = "bulungur tumani"
    else:
        samarqand["❌Bulungʻur"] = "bulungur tumani"
    if "ishtixon tumani" in list:
        samarqand["✅Ishtixon"] = "ishtixon tumani"
    else:
        samarqand["❌Ishtixon"] = "ishtixon tumani"
    if "jomboy tumani" in list:
        samarqand["✅Jomboy"] = "jomboy tumani"
    else:
        samarqand["❌Jomboy"] = "jomboy tumani"
    if "kattaqorgon tumani" in list:
        samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
    else:
        samarqand["❌Kattaqoʻrgʻon"] = 'kattaqorgon tumani'
    if "kattaqorgon shahar" in list:
        samarqand["✅Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
    else:
        samarqand["❌Kattaqoʻrgʻon shahar"] = 'kattaqorgon shahar'
    if "qoshrabot tumani" in list:
        samarqand["✅Qoʻshrabot"] = "qoshrabot tumani"
    else:
        samarqand["❌Qoʻshrabot"] = "qoshrabot tumani"
    if "narpay tumani" in list:
        samarqand["✅Narpay"] = "narpay tumani"
    else:
        samarqand["❌Narpay"] = 'narpay tumani'
    if "nurobod tumani" in list:
        samarqand["✅Nurobod"] = "nurobod tumani"
    else:
        samarqand["❌Nurobod"] = 'nurobod tumani'
    if "oqdaryo tumani" in list:
        samarqand["✅Oqdaryo"] = "oqdaryo tumani"
    else:
        samarqand["❌Oqdaryo"] = "oqdaryo tumani"
    if "paxtachi tumani" in list:
        samarqand["✅Paxtachi"] = "paxtachi tumani"
    else:
        samarqand["❌Paxtachi"] = 'paxtachi tumani'
    if "payariq tumani" in list:
        samarqand["✅Payariq"] = "payariq tumani"
    else:
        samarqand["❌Payariq"] = "payariq tumani"
    if "pastdargom tumani" in list:
        samarqand["✅Pastdargʻom"] = "pastdargom tumani"
    else:
        samarqand["❌Pastdargʻom"] = "pastdargom tumani"
    if "toyloq tumani" in list:
        samarqand["✅Toyloq"] = "toyloq tumani"
    else:
        samarqand["❌Toyloq"] = "toyloq tumani"
    shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
    for key, value in samarqand.items():
        shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in samarqand.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_samarqand)
            await SamarqandStatesGroup.samarqand_eng_birinchi.set()

