from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup,State

from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback, sirdaryo_callback
from keyboards.inline.yolovchi.sirtuman import sirdaryo_viloyati_tumanlari

class SirdaryoStatesGroup(StatesGroup):
    sirdaryo=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='ryoo'),state=SozlamalarStates.viloyat_filter)
async def namangan_edit(call: CallbackQuery):


        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        sirdaryo = {}
        if "sirdaryo shahar" in list:
            sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
        else:
            sirdaryo["❌Sirdaryo shahar"] = "sirdaryo shahar"
        if "sirdaryo tumani" in list:
            sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tumani"
        else:
            sirdaryo["❌Sirdaryo tuman"] = "sirdaryo tumani"
        if "oqoltin tumani" in list:
            sirdaryo["✅Oqoltin"] = "oqoltin tumani"
        else:
            sirdaryo["❌Oqoltin"] = "oqoltin tumani"
        if "shirin shahar" in list:
            sirdaryo["✅Shirin shahri"] = "shirin shahar"
        else:
            sirdaryo["❌Shirin shahri"] = "shirin shahar"
        if "yangiyer shahar" in list:
            sirdaryo["✅Yangiyer shahri"] = "yangiyer shahar"
        else:
            sirdaryo["❌Yangiyer shahri"] = "yangiyer shahar"
        if "oqoltin tumani" in list:
            sirdaryo["✅Oqoltin"] = "oqoltin tumani"
        else:
            sirdaryo["❌Oqoltin"] = "oqoltin tumani"
        if "boyovut tumani" in list:
            sirdaryo["✅Boyovut"] = 'boyovut tumani'
        else:
            sirdaryo["❌Boyovut"] = 'boyovut tumani'
        if "guliston shahar" in list:
            sirdaryo["✅Guliston shahar"] = "guliston shahar"
        else:
            sirdaryo["❌Guliston shahar"] = "guliston shahar"
        if "guliston tumani" in list:
            sirdaryo["✅Guliston tuman"] = "guliston tumani"
        else:
            sirdaryo["❌Guliston tuman"] = "guliston tumani"
        if "xovos tumani" in list:
            sirdaryo["✅Xovos"] = 'xovos tumani'
        else:
            sirdaryo["❌Xovos"] = 'xovos tumani'
        if "mirzaobod tumani" in list:
            sirdaryo["✅Mirzaobod"] = 'mirzaobod tumani'
        else:
            sirdaryo["❌Mirzaobod"] = 'mirzaobod tumani'
        if "sayxunobod tumani" in list:
            sirdaryo["✅Sayxunobod"] = "sayxunobod tumani"
        else:
            sirdaryo["❌Sayxunobod"] = 'sayxunobod tumani'
        if "sardoba tumani" in list:
            sirdaryo["✅Sardoba"] = "sardoba tumani"
        else:
            sirdaryo["❌Sardoba"] = 'sardoba tumani'

        shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in sirdaryo.items():
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Sirdaryoning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_sirdaryo)

        await SirdaryoStatesGroup.sirdaryo.set()
        await call.message.delete()
@dp.callback_query_handler(state=SirdaryoStatesGroup.sirdaryo)
async def sirdaryo_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="oqoltin tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="boyovut tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="guliston shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="guliston tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="shirin shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="yangiyer shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="xovos tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="mirzaobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="sardoba tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="sayxunobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="sirdaryo shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Sirdaryo", tuman="sirdaryo tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            sirdaryo = {}
            if "sirdaryo shahar" in list:
                sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
            else:
                sirdaryo["❌Sirdaryo shahar"] = "sirdaryo shahar"
            if "sirdaryo tumani" in list:
                sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tumani"
            else:
                sirdaryo["❌Sirdaryo tuman"] = "sirdaryo tumani"
            if "oqoltin tumani" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin tumani"
            else:
                sirdaryo["❌Oqoltin"] = "oqoltin tumani"
            if "shirin shahar" in list:
                sirdaryo["✅Shirin shahri"] = "shirin shahar"
            else:
                sirdaryo["❌Shirin shahri"] = "shirin shahar"
            if "yangiyer shahar" in list:
                sirdaryo["✅Yangiyer shahri"] = "yangiyer shahar"
            else:
                sirdaryo["❌Yangiyer shahri"] = "yangiyer shahar"
            if "oqoltin tumani" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin tumani"
            else:
                sirdaryo["❌Oqoltin"] = "oqoltin tumani"
            if "boyovut tumani" in list:
                sirdaryo["✅Boyovut"] = 'boyovut tumani'
            else:
                sirdaryo["❌Boyovut"] = 'boyovut tumani'
            if "guliston shahar" in list:
                sirdaryo["✅Guliston shahar"] = "guliston shahar"
            else:
                sirdaryo["❌Guliston shahar"] = "guliston shahar"
            if "guliston tumani" in list:
                sirdaryo["✅Guliston tuman"] = "guliston tumani"
            else:
                sirdaryo["❌Guliston tuman"] = "guliston tumani"
            if "xovos tumani" in list:
                sirdaryo["✅Xovos"] = 'xovos tumani'
            else:
                sirdaryo["❌Xovos"] = 'xovos tumani'
            if "mirzaobod tumani" in list:
                sirdaryo["✅Mirzaobod"] = 'mirzaobod tumani'
            else:
                sirdaryo["❌Mirzaobod"] = 'mirzaobod tumani'
            if "sayxunobod tumani" in list:
                sirdaryo["✅Sayxunobod"] = "sayxunobod tumani"
            else:
                sirdaryo["❌Sayxunobod"] = 'sayxunobod tumani'
            if "sardoba tumani" in list:
                sirdaryo["✅Sardoba"] = "sardoba tumani"
            else:
                sirdaryo["❌Sardoba"] = 'sardoba tumani'

            shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in sirdaryo.items():
                shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_sirdaryo)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Sirdaryo", tuman="oqoltin tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="boyovut tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="shirin shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="yangiyer shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="xovos tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="mirzaobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="sardoba tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="sayxunobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            sirdaryo = {}
            if "sirdaryo shahar" in list:
                sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
            else:
                sirdaryo["❌Sirdaryo shahar"] = "sirdaryo shahar"
            if "sirdaryo tumani" in list:
                sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tumani"
            else:
                sirdaryo["❌Sirdaryo tuman"] = "sirdaryo tumani"
            if "oqoltin tumani" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin tumani"
            else:
                sirdaryo["❌Oqoltin"] = "oqoltin tumani"
            if "shirin shahar" in list:
                sirdaryo["✅Shirin shahri"] = "shirin shahar"
            else:
                sirdaryo["❌Shirin shahri"] = "shirin shahar"
            if "yangiyer shahar" in list:
                sirdaryo["✅Yangiyer shahri"] = "yangiyer shahar"
            else:
                sirdaryo["❌Yangiyer shahri"] = "yangiyer shahar"
            if "oqoltin tumani" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin tumani"
            else:
                sirdaryo["❌Oqoltin"] = "oqoltin tumani"
            if "boyovut tumani" in list:
                sirdaryo["✅Boyovut"] = 'boyovut tumani'
            else:
                sirdaryo["❌Boyovut"] = 'boyovut tumani'
            if "guliston shahar" in list:
                sirdaryo["✅Guliston shahar"] = "guliston shahar"
            else:
                sirdaryo["❌Guliston shahar"] = "guliston shahar"
            if "guliston tumani" in list:
                sirdaryo["✅Guliston tuman"] = "guliston tumani"
            else:
                sirdaryo["❌Guliston tuman"] = "guliston tumani"
            if "xovos tumani" in list:
                sirdaryo["✅Xovos"] = 'xovos tumani'
            else:
                sirdaryo["❌Xovos"] = 'xovos tumani'
            if "mirzaobod tumani" in list:
                sirdaryo["✅Mirzaobod"] = 'mirzaobod tumani'
            else:
                sirdaryo["❌Mirzaobod"] = 'mirzaobod tumani'
            if "sayxunobod tumani" in list:
                sirdaryo["✅Sayxunobod"] = "sayxunobod tumani"
            else:
                sirdaryo["❌Sayxunobod"] = 'sayxunobod tumani'
            if "sardoba tumani" in list:
                sirdaryo["✅Sardoba"] = "sardoba tumani"
            else:
                sirdaryo["❌Sardoba"] = 'sardoba tumani'

            shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in sirdaryo.items():
                shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_sirdaryo)

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
        sirdaryo = {}
        if "sirdaryo shahar" in list:
            sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
        else:
            sirdaryo["❌Sirdaryo shahar"] = "sirdaryo shahar"
        if "sirdaryo tumani" in list:
            sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tumani"
        else:
            sirdaryo["❌Sirdaryo tuman"] = "sirdaryo tumani"
        if "oqoltin tumani" in list:
            sirdaryo["✅Oqoltin"] = "oqoltin tumani"
        else:
            sirdaryo["❌Oqoltin"] = "oqoltin tumani"
        if "shirin shahar" in list:
            sirdaryo["✅Shirin shahri"] = "shirin shahar"
        else:
            sirdaryo["❌Shirin shahri"] = "shirin shahar"
        if "yangiyer shahar" in list:
            sirdaryo["✅Yangiyer shahri"] = "yangiyer shahar"
        else:
            sirdaryo["❌Yangiyer shahri"] = "yangiyer shahar"
        if "oqoltin tumani" in list:
            sirdaryo["✅Oqoltin"] = "oqoltin tumani"
        else:
            sirdaryo["❌Oqoltin"] = "oqoltin tumani"
        if "boyovut tumani" in list:
            sirdaryo["✅Boyovut"] = 'boyovut tumani'
        else:
            sirdaryo["❌Boyovut"] = 'boyovut tumani'
        if "guliston shahar" in list:
            sirdaryo["✅Guliston shahar"] = "guliston shahar"
        else:
            sirdaryo["❌Guliston shahar"] = "guliston shahar"
        if "guliston tumani" in list:
            sirdaryo["✅Guliston tuman"] = "guliston tumani"
        else:
            sirdaryo["❌Guliston tuman"] = "guliston tumani"
        if "xovos tumani" in list:
            sirdaryo["✅Xovos"] = 'xovos tumani'
        else:
            sirdaryo["❌Xovos"] = 'xovos tumani'
        if "mirzaobod tumani" in list:
            sirdaryo["✅Mirzaobod"] = 'mirzaobod tumani'
        else:
            sirdaryo["❌Mirzaobod"] = 'mirzaobod tumani'
        if "sayxunobod tumani" in list:
            sirdaryo["✅Sayxunobod"] = "sayxunobod tumani"
        else:
            sirdaryo["❌Sayxunobod"] = 'sayxunobod tumani'
        if "sardoba tumani" in list:
            sirdaryo["✅Sardoba"] = "sardoba tumani"
        else:
            sirdaryo["❌Sardoba"] = 'sardoba tumani'

        shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in sirdaryo.items():
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        for key, value in sirdaryo.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_sirdaryo)
                await SirdaryoStatesGroup.sirdaryo.set()





