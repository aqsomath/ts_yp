from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db

class QoraqalpoqStatesGroup(StatesGroup):
    qoraqalpoq=State()
    qoraqalpoq_eng_birinchi=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='qoraqalpoq'),state=SozlamalarStates.viloyat_filter)
async def fargona_edit(call:CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Qoraqalpog'istonning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_qoraqalpoq)

        await QoraqalpoqStatesGroup.qoraqalpoq.set()
        await call.message.delete()
@dp.callback_query_handler(state=QoraqalpoqStatesGroup.qoraqalpoq)
async def qoraqalpoq_state(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Amudaryo tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Beruniy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Kegeyli tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qanliko'l tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qorao'zak tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qo'ng'irot tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Mo'ynoq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxiatosh tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxtako'pir tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="To'rtko'l tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Xo'jayli tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Chimboy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Sho'manoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Ellikqal'a tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Amudaryo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Beruniy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Kegeyli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qanliko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qorao'zak tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qo'ng'irot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Mo'ynoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxiatosh tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxtako'pir tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="To'rtko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Xo'jayli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Chimboy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Sho'manoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Ellikqal'a tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)

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

    qoraqalpoq = {}
    if "Nukus shahar" in list:
        qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
    else:
        qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
    if "Amudaryo tumani" in list:
        qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
    else:
        qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
    if "Beruniy tumani" in list:
        qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
    else:
        qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
    if "Kegeyli tumani" in list:
        qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
    else:
        qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
    if "Qanliko'l tumani" in list:
        qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
    else:
        qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
    if "Qorao'zak tumani" in list:
        qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
    else:
        qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
    if "Qo'ng'irot tumani" in list:
        qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
    else:
        qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
    if "Mo'ynoq tumani" in list:
        qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
    else:
        qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
    if "Nukus tumani" in list:
        qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
    else:
        qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
    if "Taxiatosh tumani" in list:
        qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
    else:
        qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
    if "Taxtako'pir tumani" in list:
        qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
    else:
        qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
    if "To'rtko'l tumani" in list:
        qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
    else:
        qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
    if "Xo'jayli tumani" in list:
        qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
    else:
        qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
    if "Chimboy tumani" in list:
        qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
    else:
        qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
    if "Sho'manoy tumani" in list:
        qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
    else:
        qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
    if "Ellikqal'a tumani" in list:
        qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
    else:
        qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

    shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
    for key, value in qoraqalpoq.items():
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in qoraqalpoq.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)
            await QoraqalpoqStatesGroup.qoraqalpoq.set()

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='qoraqalpoq'),state=EngBirinchiSozlamaState.viloyat_filter)
async def fargona_edit(call:CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Qoraqalpog'istonning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_qoraqalpoq)

        await QoraqalpoqStatesGroup.qoraqalpoq_eng_birinchi.set()
        await call.message.delete()
@dp.callback_query_handler(state=QoraqalpoqStatesGroup.qoraqalpoq_eng_birinchi)
async def qoraqalpoq_state(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Amudaryo tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Beruniy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Kegeyli tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qanliko'l tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qorao'zak tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Qo'ng'irot tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Mo'ynoq tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxiatosh tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxtako'pir tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="To'rtko'l tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Xo'jayli tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Chimboy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Sho'manoy tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qoraqalpog'iston", tuman="Ellikqal'a tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)
    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Amudaryo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Beruniy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Kegeyli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qanliko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qorao'zak tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qo'ng'irot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Mo'ynoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxiatosh tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxtako'pir tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="To'rtko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Xo'jayli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Chimboy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Sho'manoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Ellikqal'a tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qoraqalpoq = {}
        if "Nukus shahar" in list:
            qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
        else:
            qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
        if "Amudaryo tumani" in list:
            qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
        else:
            qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
        if "Beruniy tumani" in list:
            qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
        else:
            qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
        if "Kegeyli tumani" in list:
            qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
        else:
            qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
        if "Qanliko'l tumani" in list:
            qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
        else:
            qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
        if "Qorao'zak tumani" in list:
            qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
        else:
            qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
        if "Qo'ng'irot tumani" in list:
            qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        else:
            qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
        if "Mo'ynoq tumani" in list:
            qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
        else:
            qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
        if "Nukus tumani" in list:
            qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
        else:
            qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
        if "Taxiatosh tumani" in list:
            qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
        else:
            qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
        if "Taxtako'pir tumani" in list:
            qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
        else:
            qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
        if "To'rtko'l tumani" in list:
            qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
        else:
            qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
        if "Xo'jayli tumani" in list:
            qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
        else:
            qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
        if "Chimboy tumani" in list:
            qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
        else:
            qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
        if "Sho'manoy tumani" in list:
            qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
        else:
            qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
        if "Ellikqal'a tumani" in list:
            qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
        else:
            qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

        shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
        for key, value in qoraqalpoq.items():
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)

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

    qoraqalpoq = {}
    if "Nukus shahar" in list:
        qoraqalpoq["✅Nukus shahri"] = "Nukus shahar"
    else:
        qoraqalpoq["❌Nukus shahri"] = "Nukus shahar"
    if "Amudaryo tumani" in list:
        qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
    else:
        qoraqalpoq["❌Amudaryo tumani"] = 'Amudaryo tumani'
    if "Beruniy tumani" in list:
        qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
    else:
        qoraqalpoq["❌Beruniy tumani"] = "Beruniy tumani"
    if "Kegeyli tumani" in list:
        qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
    else:
        qoraqalpoq["❌Kegeyli tumani"] = 'Kegeyli tumani'
    if "Qanliko'l tumani" in list:
        qoraqalpoq["✅Qanliko'l tumani"] = "Qanliko'l tumani"
    else:
        qoraqalpoq["❌Qanliko'l tumani"] = "Qanliko'l tumani"
    if "Qorao'zak tumani" in list:
        qoraqalpoq["✅Qorao'zak tumani"] = "Qorao'zak tumani"
    else:
        qoraqalpoq["❌Qorao'zak tumani"] = "Qorao'zak tumani"
    if "Qo'ng'irot tumani" in list:
        qoraqalpoq["✅Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
    else:
        qoraqalpoq["❌Qo'ng'irot tumani"] = "Qo'ng'irot tumani"
    if "Mo'ynoq tumani" in list:
        qoraqalpoq["✅Mo'ynoq tumani"] = "Mo'ynoq tumani"
    else:
        qoraqalpoq["❌Mo'ynoq tumani"] = "Mo'ynoq tumani"
    if "Nukus tumani" in list:
        qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
    else:
        qoraqalpoq["❌Nukus tumani"] = 'Nukus tumani'
    if "Taxiatosh tumani" in list:
        qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
    else:
        qoraqalpoq["❌Taxiatosh tumani"] = 'Taxiatosh tumani'
    if "Taxtako'pir tumani" in list:
        qoraqalpoq["✅Taxtako'pir tumani"] = "Taxtako'pir tumani"
    else:
        qoraqalpoq["❌Taxtako'pir tumani"] = "Taxtako'pir tumani"
    if "To'rtko'l tumani" in list:
        qoraqalpoq["✅To'rtko'l tumani"] = "To'rtko'l tumani"
    else:
        qoraqalpoq["❌To'rtko'l tumani"] = "To'rtko'l tumani"
    if "Xo'jayli tumani" in list:
        qoraqalpoq["✅Xo'jayli tumani"] = "Xo'jayli tumani"
    else:
        qoraqalpoq["❌Xo'jayli tumani"] = "Xo'jayli tumani"
    if "Chimboy tumani" in list:
        qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
    else:
        qoraqalpoq["❌Chimboy tumani"] = "Chimboy tumani"
    if "Sho'manoy tumani" in list:
        qoraqalpoq["✅Sho'manoy tumani"] = "Sho'manoy tumani"
    else:
        qoraqalpoq["❌Sho'manoy tumani"] = "Sho'manoy tumani"
    if "Ellikqal'a tumani" in list:
        qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal'a tumani"
    else:
        qoraqalpoq["❌Ellikqal’a tumani"] = "Ellikqal'a tumani"

    shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
    for key, value in qoraqalpoq.items():
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in qoraqalpoq.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)
            await QoraqalpoqStatesGroup.qoraqalpoq_eng_birinchi.set()