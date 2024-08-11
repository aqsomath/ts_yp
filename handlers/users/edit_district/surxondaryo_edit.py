from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback,surxon_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.surtuman import surxondaryo_tuman
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db


class SurxondaryoStatesGroup(StatesGroup):
    surxondaryo=State()
    surxondaryo_eng_birinchi=State()

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='xonn'),state=EngBirinchiSozlamaState.viloyat_filter)
async def surxontuman(call:CallbackQuery):
    

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        surxondaryo = {}
        if "termiz shahar" in list:
            surxondaryo["✅Termiz shahar"] = "termiz shahar"
        else:
            surxondaryo["❌Termiz shahar"] = "termiz shahar"
        if "angor tumani" in list:
            surxondaryo["✅Angor"] = "angor tumani"
        else:
            surxondaryo["❌Angor"] = "angor tumani"
        if "boysun tumani" in list:
            surxondaryo["✅Boysun"] = "boysun tumani"
        else:
            surxondaryo["❌Boysun"] = "boysun tumani"
        if "denov tumani" in list:
            surxondaryo["✅Denov"] = 'denov tumani'
        else:
            surxondaryo["❌Denov"] = 'denov tumani'
        if "jarqorgon tumani" in list:
            surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon tumani"
        else:
            surxondaryo["❌Jarqoʻrgʻon"] = 'jarqorgon tumani'

        if "qiziriq tumani" in list:
            surxondaryo["✅Qiziriq"] = "qiziriq tumani"
        else:
            surxondaryo["❌Qiziriq"] = "qiziriq tumani"
        if "qumqorgon tumani" in list:
            surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon tumani"
        else:
            surxondaryo["❌Qumqoʻrgʻon"] = 'qumqorgon tumani'
        if "muzrabod tumani" in list:
            surxondaryo["✅Muzrabod"] = "muzrabod tumani"
        else:
            surxondaryo["❌Muzrabod"] = "muzrabod tumani"
        if "oltinsoy tumani" in list:
            surxondaryo["✅Oltinsoy"] = "oltinsoy tumani"
        else:
            surxondaryo["❌Oltinsoy"] = "oltinsoy tumani"
        if "sariosiyo tumani" in list:
            surxondaryo["✅Sariosiyo"] = "sariosiyo tumani"
        else:
            surxondaryo["❌Sariosiyo"] = "sariosiyo tumani"
        if "sherobod tumani" in list:
            surxondaryo["✅Sherobod"] = "sherobod tumani"
        else:
            surxondaryo["❌Sherobod"] = "sherobod tumani"
        if "shorchi tumani" in list:
            surxondaryo["✅Shoʻrchi"] = "shorchi tumani"
        else:
            surxondaryo["❌Shoʻrchi"] = "shorchi tumani"
        if "termiz tumani" in list:
            surxondaryo["✅Termiz tuman"] = "termiz tumani"
        else:
            surxondaryo["❌Termiz tuman"] = "termiz tumani"
        if "uzun tumani" in list:
            surxondaryo["✅Uzun"] = "uzun tumani"
        else:
            surxondaryo["❌Uzun"] = "uzun tumani"
        shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in surxondaryo.items():
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Surxondaryoning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_surxondaryo)

        await SurxondaryoStatesGroup.surxondaryo_eng_birinchi.set()
        await call.message.delete()


@dp.callback_query_handler(state=SurxondaryoStatesGroup.surxondaryo_eng_birinchi)
async def surxondaryo_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="angor tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="bandixon tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="boysun tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="denov tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="jarqorgon tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="qiziriq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="qumqorgon tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="muzrabod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="oltinsoy tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="sariosiyo tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="sherobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="shorchi tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="termiz tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="termiz shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Surxondaryo", tuman="uzun tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            surxondaryo = {}
            if "termiz shahar" in list:
                surxondaryo["✅Termiz shahar"] = "termiz shahar"
            else:
                surxondaryo["❌Termiz shahar"] = "termiz shahar"
            if "angor tumani" in list:
                surxondaryo["✅Angor"] = "angor tumani"
            else:
                surxondaryo["❌Angor"] = "angor tumani"
            if "boysun tumani" in list:
                surxondaryo["✅Boysun"] = "boysun tumani"
            else:
                surxondaryo["❌Boysun"] = "boysun tumani"
            if "denov tumani" in list:
                surxondaryo["✅Denov"] = 'denov tumani'
            else:
                surxondaryo["❌Denov"] = 'denov tumani'
            if "jarqorgon tumani" in list:
                surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon tumani"
            else:
                surxondaryo["❌Jarqoʻrgʻon"] = 'jarqorgon tumani'

            if "qiziriq tumani" in list:
                surxondaryo["✅Qiziriq"] = "qiziriq tumani"
            else:
                surxondaryo["❌Qiziriq"] = "qiziriq tumani"
            if "qumqorgon tumani" in list:
                surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon tumani"
            else:
                surxondaryo["❌Qumqoʻrgʻon"] = 'qumqorgon tumani'
            if "muzrabod tumani" in list:
                surxondaryo["✅Muzrabod"] = "muzrabod tumani"
            else:
                surxondaryo["❌Muzrabod"] = "muzrabod tumani"
            if "oltinsoy tumani" in list:
                surxondaryo["✅Oltinsoy"] = "oltinsoy tumani"
            else:
                surxondaryo["❌Oltinsoy"] = "oltinsoy tumani"
            if "sariosiyo tumani" in list:
                surxondaryo["✅Sariosiyo"] = "sariosiyo tumani"
            else:
                surxondaryo["❌Sariosiyo"] = "sariosiyo tumani"
            if "sherobod tumani" in list:
                surxondaryo["✅Sherobod"] = "sherobod tumani"
            else:
                surxondaryo["❌Sherobod"] = "sherobod tumani"
            if "shorchi tumani" in list:
                surxondaryo["✅Shoʻrchi"] = "shorchi tumani"
            else:
                surxondaryo["❌Shoʻrchi"] = "shorchi tumani"
            if "termiz tumani" in list:
                surxondaryo["✅Termiz tuman"] = "termiz tumani"
            else:
                surxondaryo["❌Termiz tuman"] = "termiz tumani"
            if "uzun tumani" in list:
                surxondaryo["✅Uzun"] = "uzun tumani"
            else:
                surxondaryo["❌Uzun"] = "uzun tumani"
            shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in surxondaryo.items():
                shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_surxondaryo.insert(
                InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_surxondaryo)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Surxondaryo", tuman="angor tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="bandixon tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="boysun tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="denov tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="jarqorgon tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="qiziriq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="qumqorgon tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="muzrabod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="oltinsoy tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="sariosiyo tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="sherobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="shorchi tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Surxondaryo", tuman="uzun tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            surxondaryo = {}
            if "termiz shahar" in list:
                surxondaryo["✅Termiz shahar"] = "termiz shahar"
            else:
                surxondaryo["❌Termiz shahar"] = "termiz shahar"
            if "angor tumani" in list:
                surxondaryo["✅Angor"] = "angor tumani"
            else:
                surxondaryo["❌Angor"] = "angor tumani"
            if "boysun tumani" in list:
                surxondaryo["✅Boysun"] = "boysun tumani"
            else:
                surxondaryo["❌Boysun"] = "boysun tumani"
            if "denov tumani" in list:
                surxondaryo["✅Denov"] = 'denov tumani'
            else:
                surxondaryo["❌Denov"] = 'denov tumani'
            if "jarqorgon tumani" in list:
                surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon tumani"
            else:
                surxondaryo["❌Jarqoʻrgʻon"] = 'jarqorgon tumani'

            if "qiziriq tumani" in list:
                surxondaryo["✅Qiziriq"] = "qiziriq tumani"
            else:
                surxondaryo["❌Qiziriq"] = "qiziriq tumani"
            if "qumqorgon tumani" in list:
                surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon tumani"
            else:
                surxondaryo["❌Qumqoʻrgʻon"] = 'qumqorgon tumani'
            if "muzrabod tumani" in list:
                surxondaryo["✅Muzrabod"] = "muzrabod tumani"
            else:
                surxondaryo["❌Muzrabod"] = "muzrabod tumani"
            if "oltinsoy tumani" in list:
                surxondaryo["✅Oltinsoy"] = "oltinsoy tumani"
            else:
                surxondaryo["❌Oltinsoy"] = "oltinsoy tumani"
            if "sariosiyo tumani" in list:
                surxondaryo["✅Sariosiyo"] = "sariosiyo tumani"
            else:
                surxondaryo["❌Sariosiyo"] = "sariosiyo tumani"
            if "sherobod tumani" in list:
                surxondaryo["✅Sherobod"] = "sherobod tumani"
            else:
                surxondaryo["❌Sherobod"] = "sherobod tumani"
            if "shorchi tumani" in list:
                surxondaryo["✅Shoʻrchi"] = "shorchi tumani"
            else:
                surxondaryo["❌Shoʻrchi"] = "shorchi tumani"
            if "termiz tumani" in list:
                surxondaryo["✅Termiz tuman"] = "termiz tumani"
            else:
                surxondaryo["❌Termiz tuman"] = "termiz tumani"
            if "uzun tumani" in list:
                surxondaryo["✅Uzun"] = "uzun tumani"
            else:
                surxondaryo["❌Uzun"] = "uzun tumani"
            shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in surxondaryo.items():
                shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_surxondaryo.insert(
                InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_surxondaryo)
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
        surxondaryo = {}
        if "termiz shahar" in list:
            surxondaryo["✅Termiz shahar"] = "termiz shahar"
        else:
            surxondaryo["❌Termiz shahar"] = "termiz shahar"
        if "angor tumani" in list:
            surxondaryo["✅Angor"] = "angor tumani"
        else:
            surxondaryo["❌Angor"] = "angor tumani"
        if "boysun tumani" in list:
            surxondaryo["✅Boysun"] = "boysun tumani"
        else:
            surxondaryo["❌Boysun"] = "boysun tumani"
        if "denov tumani" in list:
            surxondaryo["✅Denov"] = 'denov tumani'
        else:
            surxondaryo["❌Denov"] = 'denov tumani'
        if "jarqorgon tumani" in list:
            surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon tumani"
        else:
            surxondaryo["❌Jarqoʻrgʻon"] = 'jarqorgon tumani'
        if "qiziriq tumani" in list:
            surxondaryo["✅Qiziriq"] = "qiziriq tumani"
        else:
            surxondaryo["❌Qiziriq"] = "qiziriq tumani"
        if "qumqorgon tumani" in list:
            surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon tumani"
        else:
            surxondaryo["❌Qumqoʻrgʻon"] = 'qumqorgon tumani'
        if "muzrabod tumani" in list:
            surxondaryo["✅Muzrabod"] = "muzrabod tumani"
        else:
            surxondaryo["❌Muzrabod"] = "muzrabod tumani"
        if "oltinsoy tumani" in list:
            surxondaryo["✅Oltinsoy"] = "oltinsoy tumani"
        else:
            surxondaryo["❌Oltinsoy"] = "oltinsoy tumani"
        if "sariosiyo tumani" in list:
            surxondaryo["✅Sariosiyo"] = "sariosiyo tumani"
        else:
            surxondaryo["❌Sariosiyo"] = "sariosiyo tumani"
        if "sherobod tumani" in list:
            surxondaryo["✅Sherobod"] = "sherobod tumani"
        else:
            surxondaryo["❌Sherobod"] = "sherobod tumani"
        if "shorchi tumani" in list:
            surxondaryo["✅Shoʻrchi"] = "shorchi tumani"
        else:
            surxondaryo["❌Shoʻrchi"] = "shorchi tumani"
        if "termiz tumani" in list:
            surxondaryo["✅Termiz tuman"] = "termiz tumani"
        else:
            surxondaryo["❌Termiz tuman"] = "termiz tumani"
        if "uzun tumani" in list:
            surxondaryo["✅Uzun"] = "uzun tumani"
        else:
            surxondaryo["❌Uzun"] = "uzun tumani"
        shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in surxondaryo.items():
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        for key, value in surxondaryo.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_surxondaryo)
                await SurxondaryoStatesGroup.surxondaryo_eng_birinchi.set()
