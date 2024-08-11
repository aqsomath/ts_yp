from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,xorazm_callback
from keyboards.inline.yolovchi.xorazmtuman import xorazm_tumanlari



class XorazmStatesGroup(StatesGroup):
    xorazm=State()
    xorazm_en=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='azmm'),state=SozlamalarStates.viloyat_filter)
async def xorazm_edit(call: CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        xorazm = {}
        if "urganch shahar" in list:
            xorazm["✅Urganch shahar"] = "urganch shahar"
        else:
            xorazm["❌Urganch shahar"] = "urganch shahar"
        if "bog'ot tumani" in list:
            xorazm["✅Bogʻot"] = "bog'ot tumani"
        else:
            xorazm["❌Bogʻot"] = "bog'ot tumani"
        if "gurlan tumani" in list:
            xorazm["✅Gurlan"] = "gurlan tumani"
        else:
            xorazm["❌Gurlan"] = "gurlan tumani"
        if "xonqa tumani" in list:
            xorazm["✅Xonqa"] = "xonqa tumani"
        else:
            xorazm["❌Xonqa"] = "xonqa tumani"
        if "hazorasp tumani" in list:
            xorazm["✅Hazorasp"] = 'hazorasp tumani'
        else:
            xorazm["❌Hazorasp"] = 'hazorasp tumani'
        if "xiva tumani" in list:
            xorazm["✅Xiva"] = 'xiva tumani'
        else:
            xorazm["❌Xiva"] = 'xiva tumani'
        if "xiva shahar" in list:
            xorazm["✅Xiva shahar"] = 'xiva shahar'
        else:
            xorazm["❌Xiva shahar"] = 'xiva shahar'
        if "qoshko'prik tumani" in list:
            xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
        else:
            xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
        if "shovot tumani" in list:
            xorazm["✅Shovot"] = "shovot tumani"
        else:
            xorazm["❌Shovot"] = 'shovot tumani'
        if "urganch tumani" in list:
            xorazm["✅Urganch tuman"] = "urganch tumani"
        else:
            xorazm["❌Urganch tuman"] = "urganch tumani"
        if "yangiariq tumani" in list:
            xorazm["✅Yangiariq"] = "yangiariq tumani"
        else:
            xorazm["❌Yangiariq"] = 'yangiariq tumani'
        if "yangibozor tumani" in list:
            xorazm["✅Yangibozor"] = "yangibozor tumani"
        else:
            xorazm["❌Yangibozor"] = "yangibozor tumani"
        if "tuproqqal'a tumani" in list:
            xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
        else:
            xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

        shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
        for key, value in xorazm.items():
            shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Xorazmning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_xorazm)

        await XorazmStatesGroup.xorazm.set()
        await call.message.delete()
@dp.callback_query_handler(state=XorazmStatesGroup.xorazm)
async def xorazm_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Xorazm", tuman="bog'ot tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="gurlan tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xonqa tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="hazorasp tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xiva tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xiva shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="qoshko'prik tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="shovot tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="urganch tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="urganch shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="yangiariq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="yangibozor tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="tuproqqal'a tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            xorazm = {}
            if "urganch shahar" in list:
                xorazm["✅Urganch shahar"] = "urganch shahar"
            else:
                xorazm["❌Urganch shahar"] = "urganch shahar"
            if "bog'ot tumani" in list:
                xorazm["✅Bogʻot"] = "bog'ot tumani"
            else:
                xorazm["❌Bogʻot"] = "bog'ot tumani"
            if "gurlan tumani" in list:
                xorazm["✅Gurlan"] = "gurlan tumani"
            else:
                xorazm["❌Gurlan"] = "gurlan tumani"
            if "xonqa tumani" in list:
                xorazm["✅Xonqa"] = "xonqa tumani"
            else:
                xorazm["❌Xonqa"] = "xonqa tumani"
            if "hazorasp tumani" in list:
                xorazm["✅Hazorasp"] = 'hazorasp tumani'
            else:
                xorazm["❌Hazorasp"] = 'hazorasp tumani'
            if "xiva tumani" in list:
                xorazm["✅Xiva"] = 'xiva tumani'
            else:
                xorazm["❌Xiva"] = 'xiva tumani'
            if "xiva shahar" in list:
                xorazm["✅Xiva shahar"] = 'xiva shahar'
            else:
                xorazm["❌Xiva shahar"] = 'xiva shahar'
            if "qoshko'prik tumani" in list:
                xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
            else:
                xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
            if "shovot tumani" in list:
                xorazm["✅Shovot"] = "shovot tumani"
            else:
                xorazm["❌Shovot"] = 'shovot tumani'
            if "urganch tumani" in list:
                xorazm["✅Urganch tuman"] = "urganch tumani"
            else:
                xorazm["❌Urganch tuman"] = "urganch tumani"
            if "yangiariq tumani" in list:
                xorazm["✅Yangiariq"] = "yangiariq tumani"
            else:
                xorazm["❌Yangiariq"] = 'yangiariq tumani'
            if "yangibozor tumani" in list:
                xorazm["✅Yangibozor"] = "yangibozor tumani"
            else:
                xorazm["❌Yangibozor"] = "yangibozor tumani"
            if "tuproqqal'a tumani" in list:
                xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
            else:
                xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

            shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
            for key, value in xorazm.items():
                shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_xorazm)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Xorazm", tuman="bog'ot tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="gurlan tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xonqa tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="hazorasp tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xiva tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xiva shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="qoshko'prik tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="shovot tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="urganch tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="urganch shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="yangiariq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="yangibozor tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="tuproqqal'a tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            xorazm = {}
            if "urganch shahar" in list:
                xorazm["✅Urganch shahar"] = "urganch shahar"
            else:
                xorazm["❌Urganch shahar"] = "urganch shahar"
            if "bog'ot tumani" in list:
                xorazm["✅Bogʻot"] = "bog'ot tumani"
            else:
                xorazm["❌Bogʻot"] = "bog'ot tumani"
            if "gurlan tumani" in list:
                xorazm["✅Gurlan"] = "gurlan tumani"
            else:
                xorazm["❌Gurlan"] = "gurlan tumani"
            if "xonqa tumani" in list:
                xorazm["✅Xonqa"] = "xonqa tumani"
            else:
                xorazm["❌Xonqa"] = "xonqa tumani"
            if "hazorasp tumani" in list:
                xorazm["✅Hazorasp"] = 'hazorasp tumani'
            else:
                xorazm["❌Hazorasp"] = 'hazorasp tumani'
            if "xiva tumani" in list:
                xorazm["✅Xiva"] = 'xiva tumani'
            else:
                xorazm["❌Xiva"] = 'xiva tumani'
            if "xiva shahar" in list:
                xorazm["✅Xiva shahar"] = 'xiva shahar'
            else:
                xorazm["❌Xiva shahar"] = 'xiva shahar'
            if "qoshko'prik tumani" in list:
                xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
            else:
                xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
            if "shovot tumani" in list:
                xorazm["✅Shovot"] = "shovot tumani"
            else:
                xorazm["❌Shovot"] = 'shovot tumani'
            if "urganch tumani" in list:
                xorazm["✅Urganch tuman"] = "urganch tumani"
            else:
                xorazm["❌Urganch tuman"] = "urganch tumani"
            if "yangiariq tumani" in list:
                xorazm["✅Yangiariq"] = "yangiariq tumani"
            else:
                xorazm["❌Yangiariq"] = 'yangiariq tumani'
            if "yangibozor tumani" in list:
                xorazm["✅Yangibozor"] = "yangibozor tumani"
            else:
                xorazm["❌Yangibozor"] = "yangibozor tumani"
            if "tuproqqal'a tumani" in list:
                xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
            else:
                xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

            shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
            for key, value in xorazm.items():
                shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_xorazm)


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
        xorazm = {}
        if "urganch shahar" in list:
            xorazm["✅Urganch shahar"] = "urganch shahar"
        else:
            xorazm["❌Urganch shahar"] = "urganch shahar"
        if "bog'ot tumani" in list:
            xorazm["✅Bogʻot"] = "bog'ot tumani"
        else:
            xorazm["❌Bogʻot"] = "bog'ot tumani"
        if "gurlan tumani" in list:
            xorazm["✅Gurlan"] = "gurlan tumani"
        else:
            xorazm["❌Gurlan"] = "gurlan tumani"
        if "xonqa tumani" in list:
            xorazm["✅Xonqa"] = "xonqa tumani"
        else:
            xorazm["❌Xonqa"] = "xonqa tumani"
        if "hazorasp tumani" in list:
            xorazm["✅Hazorasp"] = 'hazorasp tumani'
        else:
            xorazm["❌Hazorasp"] = 'hazorasp tumani'
        if "xiva tumani" in list:
            xorazm["✅Xiva"] = 'xiva tumani'
        else:
            xorazm["❌Xiva"] = 'xiva tumani'
        if "xiva shahar" in list:
            xorazm["✅Xiva shahar"] = 'xiva shahar'
        else:
            xorazm["❌Xiva shahar"] = 'xiva shahar'
        if "qoshko'prik tumani" in list:
            xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
        else:
            xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
        if "shovot tumani" in list:
            xorazm["✅Shovot"] = "shovot tumani"
        else:
            xorazm["❌Shovot"] = 'shovot tumani'
        if "urganch tumani" in list:
            xorazm["✅Urganch tuman"] = "urganch tumani"
        else:
            xorazm["❌Urganch tuman"] = "urganch tumani"
        if "yangiariq tumani" in list:
            xorazm["✅Yangiariq"] = "yangiariq tumani"
        else:
            xorazm["❌Yangiariq"] = 'yangiariq tumani'
        if "yangibozor tumani" in list:
            xorazm["✅Yangibozor"] = "yangibozor tumani"
        else:
            xorazm["❌Yangibozor"] = "yangibozor tumani"
        if "tuproqqal'a tumani" in list:
            xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
        else:
            xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"
        shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
        for key, value in xorazm.items():
            shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

        for key, value in xorazm.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_xorazm)
                await XorazmStatesGroup.xorazm.set()


@dp.callback_query_handler(viloyatlar_callback.filter(item_name='azmm'),state=EngBirinchiSozlamaState.viloyat_filter)
async def xorazm_edit(call: CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        xorazm = {}
        if "urganch shahar" in list:
            xorazm["✅Urganch shahar"] = "urganch shahar"
        else:
            xorazm["❌Urganch shahar"] = "urganch shahar"
        if "bog'ot tumani" in list:
            xorazm["✅Bogʻot"] = "bog'ot tumani"
        else:
            xorazm["❌Bogʻot"] = "bog'ot tumani"
        if "gurlan tumani" in list:
            xorazm["✅Gurlan"] = "gurlan tumani"
        else:
            xorazm["❌Gurlan"] = "gurlan tumani"
        if "xonqa tumani" in list:
            xorazm["✅Xonqa"] = "xonqa tumani"
        else:
            xorazm["❌Xonqa"] = "xonqa tumani"
        if "hazorasp tumani" in list:
            xorazm["✅Hazorasp"] = 'hazorasp tumani'
        else:
            xorazm["❌Hazorasp"] = 'hazorasp tumani'
        if "xiva tumani" in list:
            xorazm["✅Xiva"] = 'xiva tumani'
        else:
            xorazm["❌Xiva"] = 'xiva tumani'
        if "xiva shahar" in list:
            xorazm["✅Xiva shahar"] = 'xiva shahar'
        else:
            xorazm["❌Xiva shahar"] = 'xiva shahar'
        if "qoshko'prik tumani" in list:
            xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
        else:
            xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
        if "shovot tumani" in list:
            xorazm["✅Shovot"] = "shovot tumani"
        else:
            xorazm["❌Shovot"] = 'shovot tumani'
        if "urganch tumani" in list:
            xorazm["✅Urganch tuman"] = "urganch tumani"
        else:
            xorazm["❌Urganch tuman"] = "urganch tumani"
        if "yangiariq tumani" in list:
            xorazm["✅Yangiariq"] = "yangiariq tumani"
        else:
            xorazm["❌Yangiariq"] = 'yangiariq tumani'
        if "yangibozor tumani" in list:
            xorazm["✅Yangibozor"] = "yangibozor tumani"
        else:
            xorazm["❌Yangibozor"] = "yangibozor tumani"
        if "tuproqqal'a tumani" in list:
            xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
        else:
            xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

        shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
        for key, value in xorazm.items():
            shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Xorazmning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_xorazm)

        await XorazmStatesGroup.xorazm_en.set()
        await call.message.delete()
@dp.callback_query_handler(state=XorazmStatesGroup.xorazm_en)
async def xorazm_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Xorazm", tuman="bog'ot tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="gurlan tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xonqa tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="hazorasp tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xiva tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="xiva shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="qoshko'prik tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="shovot tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="urganch tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="urganch shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="yangiariq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="yangibozor tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Xorazm", tuman="tuproqqal'a tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            xorazm = {}
            if "urganch shahar" in list:
                xorazm["✅Urganch shahar"] = "urganch shahar"
            else:
                xorazm["❌Urganch shahar"] = "urganch shahar"
            if "bog'ot tumani" in list:
                xorazm["✅Bogʻot"] = "bog'ot tumani"
            else:
                xorazm["❌Bogʻot"] = "bog'ot tumani"
            if "gurlan tumani" in list:
                xorazm["✅Gurlan"] = "gurlan tumani"
            else:
                xorazm["❌Gurlan"] = "gurlan tumani"
            if "xonqa tumani" in list:
                xorazm["✅Xonqa"] = "xonqa tumani"
            else:
                xorazm["❌Xonqa"] = "xonqa tumani"
            if "hazorasp tumani" in list:
                xorazm["✅Hazorasp"] = 'hazorasp tumani'
            else:
                xorazm["❌Hazorasp"] = 'hazorasp tumani'
            if "xiva tumani" in list:
                xorazm["✅Xiva"] = 'xiva tumani'
            else:
                xorazm["❌Xiva"] = 'xiva tumani'
            if "xiva shahar" in list:
                xorazm["✅Xiva shahar"] = 'xiva shahar'
            else:
                xorazm["❌Xiva shahar"] = 'xiva shahar'
            if "qoshko'prik tumani" in list:
                xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
            else:
                xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
            if "shovot tumani" in list:
                xorazm["✅Shovot"] = "shovot tumani"
            else:
                xorazm["❌Shovot"] = 'shovot tumani'
            if "urganch tumani" in list:
                xorazm["✅Urganch tuman"] = "urganch tumani"
            else:
                xorazm["❌Urganch tuman"] = "urganch tumani"
            if "yangiariq tumani" in list:
                xorazm["✅Yangiariq"] = "yangiariq tumani"
            else:
                xorazm["❌Yangiariq"] = 'yangiariq tumani'
            if "yangibozor tumani" in list:
                xorazm["✅Yangibozor"] = "yangibozor tumani"
            else:
                xorazm["❌Yangibozor"] = "yangibozor tumani"
            if "tuproqqal'a tumani" in list:
                xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
            else:
                xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

            shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
            for key, value in xorazm.items():
                shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_xorazm)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Xorazm", tuman="bog'ot tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="gurlan tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xonqa tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="hazorasp tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xiva tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="xiva shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="qoshko'prik tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="shovot tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="urganch tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="urganch shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="yangiariq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="yangibozor tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Xorazm", tuman="tuproqqal'a tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            xorazm = {}
            if "urganch shahar" in list:
                xorazm["✅Urganch shahar"] = "urganch shahar"
            else:
                xorazm["❌Urganch shahar"] = "urganch shahar"
            if "bog'ot tumani" in list:
                xorazm["✅Bogʻot"] = "bog'ot tumani"
            else:
                xorazm["❌Bogʻot"] = "bog'ot tumani"
            if "gurlan tumani" in list:
                xorazm["✅Gurlan"] = "gurlan tumani"
            else:
                xorazm["❌Gurlan"] = "gurlan tumani"
            if "xonqa tumani" in list:
                xorazm["✅Xonqa"] = "xonqa tumani"
            else:
                xorazm["❌Xonqa"] = "xonqa tumani"
            if "hazorasp tumani" in list:
                xorazm["✅Hazorasp"] = 'hazorasp tumani'
            else:
                xorazm["❌Hazorasp"] = 'hazorasp tumani'
            if "xiva tumani" in list:
                xorazm["✅Xiva"] = 'xiva tumani'
            else:
                xorazm["❌Xiva"] = 'xiva tumani'
            if "xiva shahar" in list:
                xorazm["✅Xiva shahar"] = 'xiva shahar'
            else:
                xorazm["❌Xiva shahar"] = 'xiva shahar'
            if "qoshko'prik tumani" in list:
                xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
            else:
                xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
            if "shovot tumani" in list:
                xorazm["✅Shovot"] = "shovot tumani"
            else:
                xorazm["❌Shovot"] = 'shovot tumani'
            if "urganch tumani" in list:
                xorazm["✅Urganch tuman"] = "urganch tumani"
            else:
                xorazm["❌Urganch tuman"] = "urganch tumani"
            if "yangiariq tumani" in list:
                xorazm["✅Yangiariq"] = "yangiariq tumani"
            else:
                xorazm["❌Yangiariq"] = 'yangiariq tumani'
            if "yangibozor tumani" in list:
                xorazm["✅Yangibozor"] = "yangibozor tumani"
            else:
                xorazm["❌Yangibozor"] = "yangibozor tumani"
            if "tuproqqal'a tumani" in list:
                xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
            else:
                xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"

            shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
            for key, value in xorazm.items():
                shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_xorazm)


        if call.data == "qaytish":
            await call.message.answer("O'zingizga kerakli hududlarni tanlang", reply_markup=viloyatlar)
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
        xorazm = {}
        if "urganch shahar" in list:
            xorazm["✅Urganch shahar"] = "urganch shahar"
        else:
            xorazm["❌Urganch shahar"] = "urganch shahar"
        if "bog'ot tumani" in list:
            xorazm["✅Bogʻot"] = "bog'ot tumani"
        else:
            xorazm["❌Bogʻot"] = "bog'ot tumani"
        if "gurlan tumani" in list:
            xorazm["✅Gurlan"] = "gurlan tumani"
        else:
            xorazm["❌Gurlan"] = "gurlan tumani"
        if "xonqa tumani" in list:
            xorazm["✅Xonqa"] = "xonqa tumani"
        else:
            xorazm["❌Xonqa"] = "xonqa tumani"
        if "hazorasp tumani" in list:
            xorazm["✅Hazorasp"] = 'hazorasp tumani'
        else:
            xorazm["❌Hazorasp"] = 'hazorasp tumani'
        if "xiva tumani" in list:
            xorazm["✅Xiva"] = 'xiva tumani'
        else:
            xorazm["❌Xiva"] = 'xiva tumani'
        if "xiva shahar" in list:
            xorazm["✅Xiva shahar"] = 'xiva shahar'
        else:
            xorazm["❌Xiva shahar"] = 'xiva shahar'
        if "qoshko'prik tumani" in list:
            xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik tumani"
        else:
            xorazm["❌Qoʻshkoʻpir"] = "qoshko'prik tumani"
        if "shovot tumani" in list:
            xorazm["✅Shovot"] = "shovot tumani"
        else:
            xorazm["❌Shovot"] = 'shovot tumani'
        if "urganch tumani" in list:
            xorazm["✅Urganch tuman"] = "urganch tumani"
        else:
            xorazm["❌Urganch tuman"] = "urganch tumani"
        if "yangiariq tumani" in list:
            xorazm["✅Yangiariq"] = "yangiariq tumani"
        else:
            xorazm["❌Yangiariq"] = 'yangiariq tumani'
        if "yangibozor tumani" in list:
            xorazm["✅Yangibozor"] = "yangibozor tumani"
        else:
            xorazm["❌Yangibozor"] = "yangibozor tumani"
        if "tuproqqal'a tumani" in list:
            xorazm["✅Tupproqqalʼa"] = "tuproqqal'a tumani"
        else:
            xorazm["❌Tupproqqalʼa"] = "tuproqqal'a tumani"
        shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
        for key, value in xorazm.items():
            shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

        for key, value in xorazm.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_xorazm)
                await XorazmStatesGroup.xorazm_en.set()