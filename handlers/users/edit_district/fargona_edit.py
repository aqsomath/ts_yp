from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db


class FargonaStatesGroup(StatesGroup):
    fargona=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='onaa'),state=SozlamalarStates.viloyat_filter)
async def fargona_edit(call:CallbackQuery):
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        fargona = {}
        if "farg'ona shahar" in list:
            fargona["✅Fargʻona shahri"] = "farg'ona shahar"
        else:
            fargona["❌Fargʻona shahri"] = "farg'ona shahar"
        if "farg'ona tuman" in list:
            fargona["✅Fargʻona tuman"] = "farg'ona tuman"
        else:
            fargona["❌Fargʻona tuman"] = "farg'ona tuman"
        if "oltiariq tuman" in list:
            fargona["✅Oltiariq"] = "oltiariq tuman"
        else:
            fargona["❌Oltiariq"] = "oltiariq tuman"
        if "bog'dod tuman" in list:
            fargona["✅Bagʻdod"] = "bog'dod tuman"
        else:
            fargona["❌Bagʻdod"] = "bog'dod tuman"
        if "beshariq tuman" in list:
            fargona["✅Beshariq"] = "beshariq tuman"
        else:
            fargona["❌Beshariq"] = "beshariq tuman"
        if "buvayda tuman" in list:
            fargona["✅Buvayda"] = 'buvayda tuman'
        else:
            fargona["❌Buvayda"] = 'buvayda tuman'
        if "dangara tuman" in list:
            fargona["✅Dangʻara"] = 'dangara tuman'
        else:
            fargona["❌Dangʻara"] = 'dangara tuman'
        if "furqat tuman" in list:
            fargona["✅Furqat"] = "furqat tuman"
        else:
            fargona["❌Furqat"] = 'furqat tuman'
        if "qo'shtepa tuman" in list:
            fargona["✅Qoʻshtepa"] = "qo'shtepa tuman"
        else:
            fargona["❌Qoʻshtepa"] = "qo'shtepa tuman"
        if "quva tuman" in list:
            fargona["✅Quva"] = "quva tuman"
        else:
            fargona["❌Quva"] = 'quva tuman'
        if "rishton tuman" in list:
            fargona["✅Rishton"] = "rishton tuman"
        else:
            fargona["❌Rishton"] = "rishton tuman"
        if "sox tuman" in list:
            fargona["✅Soʻx"] = "sox tuman"
        else:
            fargona["❌Soʻx"] = "sox tuman"
        if "toshloq tuman" in list:
            fargona["✅Toshloq"] = "toshloq tuman"
        else:
            fargona["❌Toshloq"] = "toshloq tuman"
        if "o'zbekiston tuman" in list:
            fargona["✅Oʻzbekiston"] = "o'zbekiston tuman"
        else:
            fargona["❌Oʻzbekiston"] = "o'zbekiston tuman"
        if "uchko'prik tuman" in list:
            fargona["✅Uchkoʻprik"] = "uchko'prik tuman"
        else:
            fargona["❌Uchkoʻprik"] = "uchko'prik tuman"
        if "yozyovon tuman" in list:
            fargona["✅Yozyovon"] = "yozyovon tuman"
        else:
            fargona["❌Yozyovon"] = "yozyovon tuman"
        if "quvasoy shahar" in list:
            fargona["✅Quvasoy shahri"] = "quvasoy shahar"
        else:
            fargona["❌Quvasoy shahri"] = "quvasoy shahar"
        if "marg'ilon shahar" in list:
            fargona["✅Marg'ilon shahri"] = "marg'ilon shahar"
        else:
            fargona["❌Marg'ilon shahri"] = "marg'ilon shahar"
        if "qo'qon shahar" in list:
            fargona["✅Qo'qon shahri"] = "qo'qon shahar"
        else:
            fargona["❌Qo'qon shahri"] = "qo'qon shahar"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
        for key, value in fargona.items():
            shaxsiy_tugma.insert(
                InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Farg'onaning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ",reply_markup=shaxsiy_tugma)

        await FargonaStatesGroup.fargona.set()
        await call.message.delete()


@dp.callback_query_handler(state=FargonaStatesGroup.fargona)
async def oltiariq_edit(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Farg'ona", tuman="o'zbekiston tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="uchko'prik tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="yozyovon tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="toshloq tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="sox tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="rishton tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="quva tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="oltiariq tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="farg'ona tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="furqat tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="qo'shtepa tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="dangara tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="buvayda tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="beshariq tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="bog'dod tuman", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="qo'qon shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="quvasoy shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="marg'ilon shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Farg'ona", tuman="farg'ona shahar", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        fargona = {}
        if "farg'ona shahar" in list:
            fargona["✅Fargʻona shahri"] = "farg'ona shahar"
        else:
            fargona["❌Fargʻona shahri"] = "farg'ona shahar"
        if "farg'ona tuman" in list:
            fargona["✅Fargʻona tuman"] = "farg'ona tuman"
        else:
            fargona["❌Fargʻona tuman"] = "farg'ona tuman"
        if "oltiariq tuman" in list:
            fargona["✅Oltiariq"] = "oltiariq tuman"
        else:
            fargona["❌Oltiariq"] = "oltiariq tuman"
        if "bog'dod tuman" in list:
            fargona["✅Bagʻdod"] = "bog'dod tuman"
        else:
            fargona["❌Bagʻdod"] = "bog'dod tuman"
        if "beshariq tuman" in list:
            fargona["✅Beshariq"] = "beshariq tuman"
        else:
            fargona["❌Beshariq"] = "beshariq tuman"
        if "buvayda tuman" in list:
            fargona["✅Buvayda"] = 'buvayda tuman'
        else:
            fargona["❌Buvayda"] = 'buvayda tuman'
        if "dangara tuman" in list:
            fargona["✅Dangʻara"] = 'dangara tuman'
        else:
            fargona["❌Dangʻara"] = 'dangara tuman'
        if "furqat tuman" in list:
            fargona["✅Furqat"] = "furqat tuman"
        else:
            fargona["❌Furqat"] = 'furqat tuman'
        if "qo'shtepa tuman" in list:
            fargona["✅Qoʻshtepa"] = "qo'shtepa tuman"
        else:
            fargona["❌Qoʻshtepa"] = "qo'shtepa tuman"
        if "quva tuman" in list:
            fargona["✅Quva"] = "quva tuman"
        else:
            fargona["❌Quva"] = 'quva tuman'
        if "rishton tuman" in list:
            fargona["✅Rishton"] = "rishton tuman"
        else:
            fargona["❌Rishton"] = "rishton tuman"
        if "sox tuman" in list:
            fargona["✅Soʻx"] = "sox tuman"
        else:
            fargona["❌Soʻx"] = "sox tuman"
        if "toshloq tuman" in list:
            fargona["✅Toshloq"] = "toshloq tuman"
        else:
            fargona["❌Toshloq"] = "toshloq tuman"
        if "o'zbekiston tuman" in list:
            fargona["✅Oʻzbekiston"] = "o'zbekiston tuman"
        else:
            fargona["❌Oʻzbekiston"] = "o'zbekiston tuman"
        if "uchko'prik tuman" in list:
            fargona["✅Uchkoʻprik"] = "uchko'prik tuman"
        else:
            fargona["❌Uchkoʻprik"] = "uchko'prik tuman"
        if "yozyovon tuman" in list:
            fargona["✅Yozyovon"] = "yozyovon tuman"
        else:
            fargona["❌Yozyovon"] = "yozyovon tuman"
        if "quvasoy shahar" in list:
            fargona["✅Quvasoy shahri"] = "quvasoy shahar"
        else:
            fargona["❌Quvasoy shahri"] = "quvasoy shahar"
        if "marg'ilon shahar" in list:
            fargona["✅Marg'ilon shahri"] = "marg'ilon shahar"
        else:
            fargona["❌Marg'ilon shahri"] = "marg'ilon shahar"
        if "qo'qon shahar" in list:
            fargona["✅Qo'qon shahri"] = "qo'qon shahar"
        else:
            fargona["❌Qo'qon shahri"] = "qo'qon shahar"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
        for key, value in fargona.items():
            shaxsiy_tugma.insert(
                InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_tugma)

    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Farg'ona", tuman="o'zbekiston tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="uchko'prik tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="yozyovon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="toshloq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="sox tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="rishton tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="quva tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="oltiariq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="farg'ona tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="furqat tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="qo'shtepa tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="dangara tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="buvayda tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="beshariq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="bog'dod tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="qo'qon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="quvasoy shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="marg'ilon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="farg'ona shahar", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        fargona = {}
        if "farg'ona shahar" in list:
            fargona["✅Fargʻona shahri"] = "farg'ona shahar"
        else:
            fargona["❌Fargʻona shahri"] = "farg'ona shahar"
        if "farg'ona tuman" in list:
            fargona["✅Fargʻona tuman"] = "farg'ona tuman"
        else:
            fargona["❌Fargʻona tuman"] = "farg'ona tuman"
        if "oltiariq tuman" in list:
            fargona["✅Oltiariq"] = "oltiariq tuman"
        else:
            fargona["❌Oltiariq"] = "oltiariq tuman"
        if "bog'dod tuman" in list:
            fargona["✅Bagʻdod"] = "bog'dod tuman"
        else:
            fargona["❌Bagʻdod"] = "bog'dod tuman"
        if "beshariq tuman" in list:
            fargona["✅Beshariq"] = "beshariq tuman"
        else:
            fargona["❌Beshariq"] = "beshariq tuman"
        if "buvayda tuman" in list:
            fargona["✅Buvayda"] = 'buvayda tuman'
        else:
            fargona["❌Buvayda"] = 'buvayda tuman'
        if "dangara tuman" in list:
            fargona["✅Dangʻara"] = 'dangara tuman'
        else:
            fargona["❌Dangʻara"] = 'dangara tuman'
        if "furqat tuman" in list:
            fargona["✅Furqat"] = "furqat tuman"
        else:
            fargona["❌Furqat"] = 'furqat tuman'
        if "qo'shtepa tuman" in list:
            fargona["✅Qoʻshtepa"] = "qo'shtepa tuman"
        else:
            fargona["❌Qoʻshtepa"] = "qo'shtepa tuman"
        if "quva tuman" in list:
            fargona["✅Quva"] = "quva tuman"
        else:
            fargona["❌Quva"] = 'quva tuman'
        if "rishton tuman" in list:
            fargona["✅Rishton"] = "rishton tuman"
        else:
            fargona["❌Rishton"] = "rishton tuman"
        if "sox tuman" in list:
            fargona["✅Soʻx"] = "sox tuman"
        else:
            fargona["❌Soʻx"] = "sox tuman"
        if "toshloq tuman" in list:
            fargona["✅Toshloq"] = "toshloq tuman"
        else:
            fargona["❌Toshloq"] = "toshloq tuman"
        if "o'zbekiston tuman" in list:
            fargona["✅Oʻzbekiston"] = "o'zbekiston tuman"
        else:
            fargona["❌Oʻzbekiston"] = "o'zbekiston tuman"
        if "uchko'prik tuman" in list:
            fargona["✅Uchkoʻprik"] = "uchko'prik tuman"
        else:
            fargona["❌Uchkoʻprik"] = "uchko'prik tuman"
        if "yozyovon tuman" in list:
            fargona["✅Yozyovon"] = "yozyovon tuman"
        else:
            fargona["❌Yozyovon"] = "yozyovon tuman"
        if "quvasoy shahar" in list:
            fargona["✅Quvasoy shahri"] = "quvasoy shahar"
        else:
            fargona["❌Quvasoy shahri"] = "quvasoy shahar"
        if "marg'ilon shahar" in list:
            fargona["✅Marg'ilon shahri"] = "marg'ilon shahar"
        else:
            fargona["❌Marg'ilon shahri"] = "marg'ilon shahar"
        if "qo'qon shahar" in list:
            fargona["✅Qo'qon shahri"] = "qo'qon shahar"
        else:
            fargona["❌Qo'qon shahri"] = "qo'qon shahar"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
        for key, value in fargona.items():
            shaxsiy_tugma.insert(
                InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_tugma)
        
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
        await db.add_driver_info(viloyat="Farg'ona",telegram_id=call.from_user.id, tuman=call.data)
    jamii = await db.select_all_driver_info()
    list = []
    for i in jamii:
        if i[3] == call.from_user.id:
            list.append(i[2])
    fargona = {}
    if "farg'ona shahar" in list:
        fargona["✅Fargʻona shahri"] = "farg'ona shahar"
    else:
        fargona["❌Fargʻona shahri"] = "farg'ona shahar"
    if "farg'ona tuman" in list:
        fargona["✅Fargʻona tuman"] = "farg'ona tuman"
    else:
        fargona["❌Fargʻona tuman"] = "farg'ona tuman"
    if "oltiariq tuman" in list:
        fargona["✅Oltiariq"] = "oltiariq tuman"
    else:
        fargona["❌Oltiariq"] = "oltiariq tuman"
    if "bog'dod tuman" in list:
        fargona["✅Bagʻdod"] = "bog'dod tuman"
    else:
        fargona["❌Bagʻdod"] = "bog'dod tuman"
    if "beshariq tuman" in list:
        fargona["✅Beshariq"] = "beshariq tuman"
    else:
        fargona["❌Beshariq"] = "beshariq tuman"
    if "buvayda tuman" in list:
        fargona["✅Buvayda"] = 'buvayda tuman'
    else:
        fargona["❌Buvayda"] = 'buvayda tuman'
    if "dangara tuman" in list:
        fargona["✅Dangʻara"] = 'dangara tuman'
    else:
        fargona["❌Dangʻara"] = 'dangara tuman'
    if "furqat tuman" in list:
        fargona["✅Furqat"] = "furqat tuman"
    else:
        fargona["❌Furqat"] = 'furqat tuman'
    if "qo'shtepa tuman" in list:
        fargona["✅Qoʻshtepa"] = "qo'shtepa tuman"
    else:
        fargona["❌Qoʻshtepa"] = "qo'shtepa tuman"
    if "quva tuman" in list:
        fargona["✅Quva"] = "quva tuman"
    else:
        fargona["❌Quva"] = 'quva tuman'
    if "rishton tuman" in list:
        fargona["✅Rishton"] = "rishton tuman"
    else:
        fargona["❌Rishton"] = "rishton tuman"
    if "sox tuman" in list:
        fargona["✅Soʻx"] = "sox tuman"
    else:
        fargona["❌Soʻx"] = "sox tuman"
    if "toshloq tuman" in list:
        fargona["✅Toshloq"] = "toshloq tuman"
    else:
        fargona["❌Toshloq"] = "toshloq tuman"
    if "o'zbekiston tuman" in list:
        fargona["✅Oʻzbekiston"] = "o'zbekiston tuman"
    else:
        fargona["❌Oʻzbekiston"] = "o'zbekiston tuman"
    if "uchko'prik tuman" in list:
        fargona["✅Uchkoʻprik"] = "uchko'prik tuman"
    else:
        fargona["❌Uchkoʻprik"] = "uchko'prik tuman"
    if "yozyovon tuman" in list:
        fargona["✅Yozyovon"] = "yozyovon tuman"
    else:
        fargona["❌Yozyovon"] = "yozyovon tuman"
    if "quvasoy shahar" in list:
        fargona["✅Quvasoy shahri"] = "quvasoy shahar"
    else:
        fargona["❌Quvasoy shahri"] = "quvasoy shahar"
    if "marg'ilon shahar" in list:
        fargona["✅Marg'ilon shahri"] = "marg'ilon shahar"
    else:
        fargona["❌Marg'ilon shahri"] = "marg'ilon shahar"
    if "qo'qon shahar" in list:
        fargona["✅Qo'qon shahri"] = "qo'qon shahar"
    else:
        fargona["❌Qo'qon shahri"] = "qo'qon shahar"

    shaxsiy_fargona = InlineKeyboardMarkup(row_width=3)
    for key, value in fargona.items():
        shaxsiy_fargona.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_fargona.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_fargona.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))


    for key, value in fargona.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_fargona)
            await FargonaStatesGroup.fargona.set()









