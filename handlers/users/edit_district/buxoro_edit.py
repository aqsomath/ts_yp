from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, buxoro_callback
from keyboards.inline.yolovchi.buxtuman import buxoro_viloyati_tumanlari
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.dispatcher.filters.state import StatesGroup, State

class BuxoroStatesGroup(StatesGroup):
    buxoro=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='oroo'),state=SozlamalarStates.viloyat_filter)
async def toshkenttuman(call:CallbackQuery):
    
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        buxoro = {}
        if "buxoro shaxar" in list:
            buxoro["✅Buxoro shahar"] = "buxoro shaxar"
        else:
            buxoro["❌Buxoro shahar"] = "buxoro shaxar"
        if "buxoro tuman" in list:
            buxoro["✅Buxoro tuman"] = "buxoro tuman"
        else:
            buxoro["❌Buxoro tuman"] = "buxoro tuman"
        if "olot tuman" in list:
            buxoro["✅Olot"] = "olot tuman"
        else:
            buxoro["❌Olot"] = "olot tuman"
        if "g'ijduvon tuman" in list:
            buxoro["✅Gʻijduvon"] = "g'ijduvon tuman"
        else:
            buxoro["❌Gʻijduvon"] = "g'ijduvon tuman"
        if "jondor tuman" in list:
            buxoro["✅Jondor"] = 'jondor tuman'
        else:
            buxoro["❌Jondor"] = 'jondor tuman'
        if "kogon shahar" in list:
            buxoro["✅Kogon shahar"] = 'kogon shahar'
        else:
            buxoro["❌Kogon shahar"] = 'kogon shahar'
        if "kogon tuman" in list:
            buxoro["✅Kogon tuman"] = 'kogon tuman'
        else:
            buxoro["❌Kogon tuman"] = 'kogon tuman'
        if "qorako'l tuman" in list:
            buxoro["✅Qorakoʻl"] = "qorako'l tuman"
        else:
            buxoro["❌Qorakoʻl"] = 'qorako\'l tuman'
        if "qorovulbozor tuman" in list:
            buxoro["✅Qorovulbozor"] = "qorovulbozor tuman"
        else:
            buxoro["❌Qorovulbozor"] = 'qorovulbozor tuman'
        if "peshku tuman" in list:
            buxoro["✅Peshku"] = "peshku tuman"
        else:
            buxoro["❌Peshku"] = "peshku tuman"
        if "romitan tuman" in list:
            buxoro["✅Romitan"] = "romitan tuman"
        else:
            buxoro["❌Romitan"] = 'romitan tuman'
        if "shofirkon tuman" in list:
            buxoro["✅Shofirkon"] = "shofirkon tuman"
        else:
            buxoro["❌Shofirkon"] = "shofirkon tuman"
        if "vobkent tuman" in list:
            buxoro["✅Vobkent"] = "vobkent tuman"
        else:
            buxoro["❌Vobkent"] = "vobkent tuman"

        shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
        for key, value in buxoro.items():
            shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_buxoro.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Buxoroning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ",reply_markup=shaxsiy_buxoro)
        await BuxoroStatesGroup.buxoro.set()
        await call.message.delete()


@dp.callback_query_handler(state=BuxoroStatesGroup.buxoro)
async def oltiariq_edit(call:CallbackQuery,state:FSMContext):
            if call.data == "hammasiniradetish":
                await db.delete_driver_info(tuman="olot tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="buxoro shaxar", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="buxoro tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="g'ijduvon tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="jondor tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="kogon tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="kogon shahar", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="qorako'l tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="qorovulbozor tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="peshku tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="romitan tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="shofirkon tuman", telegram_id=call.from_user.id)
                await db.delete_driver_info(tuman="vobkent tuman", telegram_id=call.from_user.id)
                jamii = await db.select_all_driver_info()
                list = []
                for i in jamii:
                    if i[3] == call.from_user.id:
                        list.append(i[2])
                buxoro = {}
                if "buxoro shaxar" in list:
                    buxoro["✅Buxoro shahar"] = "buxoro shaxar"
                else:
                    buxoro["❌Buxoro shahar"] = "buxoro shaxar"
                if "buxoro tuman" in list:
                    buxoro["✅Buxoro tuman"] = "buxoro tuman"
                else:
                    buxoro["❌Buxoro tuman"] = "buxoro tuman"
                if "olot tuman" in list:
                    buxoro["✅Olot"] = "olot tuman"
                else:
                    buxoro["❌Olot"] = "olot tuman"
                if "g'ijduvon tuman" in list:
                    buxoro["✅Gʻijduvon"] = "g'ijduvon tuman"
                else:
                    buxoro["❌Gʻijduvon"] = "g'ijduvon tuman"
                if "jondor tuman" in list:
                    buxoro["✅Jondor"] = 'jondor tuman'
                else:
                    buxoro["❌Jondor"] = 'jondor tuman'
                if "kogon shahar" in list:
                    buxoro["✅Kogon shahar"] = 'kogon shahar'
                else:
                    buxoro["❌Kogon shahar"] = 'kogon shahar'
                if "kogon tuman" in list:
                    buxoro["✅Kogon tuman"] = 'kogon tuman'
                else:
                    buxoro["❌Kogon tuman"] = 'kogon tuman'
                if "qorako'l tuman" in list:
                    buxoro["✅Qorakoʻl"] = "qorako'l tuman"
                else:
                    buxoro["❌Qorakoʻl"] = 'qorako\'l tuman'
                if "qorovulbozor tuman" in list:
                    buxoro["✅Qorovulbozor"] = "qorovulbozor tuman"
                else:
                    buxoro["❌Qorovulbozor"] = 'qorovulbozor tuman'
                if "peshku tuman" in list:
                    buxoro["✅Peshku"] = "peshku tuman"
                else:
                    buxoro["❌Peshku"] = "peshku tuman"
                if "romitan tuman" in list:
                    buxoro["✅Romitan"] = "romitan tuman"
                else:
                    buxoro["❌Romitan"] = 'romitan tuman'
                if "shofirkon tuman" in list:
                    buxoro["✅Shofirkon"] = "shofirkon tuman"
                else:
                    buxoro["❌Shofirkon"] = "shofirkon tuman"
                if "vobkent tuman" in list:
                    buxoro["✅Vobkent"] = "vobkent tuman"
                else:
                    buxoro["❌Vobkent"] = "vobkent tuman"

                shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
                for key, value in buxoro.items():
                    shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
                shaxsiy_buxoro.insert(
                    InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
                shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
                shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
                await call.message.edit_reply_markup( reply_markup=shaxsiy_buxoro)
            if call.data == "hammasinibelgilash":
                await db.add_driver_info(viloyat="Buxoro", tuman="olot tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="buxoro shaxar", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="buxoro tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="g'ijduvon tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="jondor tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="kogon tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="kogon shahar", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="qorako'l tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="qorovulbozor tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="peshku tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="romitan tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="shofirkon tuman", telegram_id=call.from_user.id)
                await db.add_driver_info(viloyat="Buxoro", tuman="vobkent tuman", telegram_id=call.from_user.id)
                jamii = await db.select_all_driver_info()
                list = []
                for i in jamii:
                    if i[3] == call.from_user.id:
                        list.append(i[2])
                buxoro = {}
                if "buxoro shaxar" in list:
                    buxoro["✅Buxoro shahar"] = "buxoro shaxar"
                else:
                    buxoro["❌Buxoro shahar"] = "buxoro shaxar"
                if "buxoro tuman" in list:
                    buxoro["✅Buxoro tuman"] = "buxoro tuman"
                else:
                    buxoro["❌Buxoro tuman"] = "buxoro tuman"
                if "olot tuman" in list:
                    buxoro["✅Olot"] = "olot tuman"
                else:
                    buxoro["❌Olot"] = "olot tuman"
                if "g'ijduvon tuman" in list:
                    buxoro["✅Gʻijduvon"] = "g'ijduvon tuman"
                else:
                    buxoro["❌Gʻijduvon"] = "g'ijduvon tuman"
                if "jondor tuman" in list:
                    buxoro["✅Jondor"] = 'jondor tuman'
                else:
                    buxoro["❌Jondor"] = 'jondor tuman'
                if "kogon shahar" in list:
                    buxoro["✅Kogon shahar"] = 'kogon shahar'
                else:
                    buxoro["❌Kogon shahar"] = 'kogon shahar'
                if "kogon tuman" in list:
                    buxoro["✅Kogon tuman"] = 'kogon tuman'
                else:
                    buxoro["❌Kogon tuman"] = 'kogon tuman'
                if "qorako'l tuman" in list:
                    buxoro["✅Qorakoʻl"] = "qorako'l tuman"
                else:
                    buxoro["❌Qorakoʻl"] = 'qorako\'l tuman'
                if "qorovulbozor tuman" in list:
                    buxoro["✅Qorovulbozor"] = "qorovulbozor tuman"
                else:
                    buxoro["❌Qorovulbozor"] = 'qorovulbozor tuman'
                if "peshku tuman" in list:
                    buxoro["✅Peshku"] = "peshku tuman"
                else:
                    buxoro["❌Peshku"] = "peshku tuman"
                if "romitan tuman" in list:
                    buxoro["✅Romitan"] = "romitan tuman"
                else:
                    buxoro["❌Romitan"] = 'romitan tuman'
                if "shofirkon tuman" in list:
                    buxoro["✅Shofirkon"] = "shofirkon tuman"
                else:
                    buxoro["❌Shofirkon"] = "shofirkon tuman"
                if "vobkent tuman" in list:
                    buxoro["✅Vobkent"] = "vobkent tuman"
                else:
                    buxoro["❌Vobkent"] = "vobkent tuman"

                shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
                for key, value in buxoro.items():
                    shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
                shaxsiy_buxoro.insert(
                    InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
                shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
                shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
                await call.message.edit_reply_markup(reply_markup=shaxsiy_buxoro)
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
                await db.add_driver_info(viloyat="Buxoro", telegram_id=call.from_user.id, tuman=call.data)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            buxoro = {}
            if "buxoro shaxar" in list:
                buxoro["✅Buxoro shahar"] = "buxoro shaxar"
            else:
                buxoro["❌Buxoro shahar"] = "buxoro shaxar"
            if "buxoro tuman" in list:
                buxoro["✅Buxoro tuman"] = "buxoro tuman"
            else:
                buxoro["❌Buxoro tuman"] = "buxoro tuman"
            if "olot tuman" in list:
                buxoro["✅Olot"] = "olot tuman"
            else:
                buxoro["❌Olot"] = "olot tuman"
            if "g'ijduvon tuman" in list:
                buxoro["✅Gʻijduvon"] = "g'ijduvon tuman"
            else:
                buxoro["❌Gʻijduvon"] = "g'ijduvon tuman"
            if "jondor tuman" in list:
                buxoro["✅Jondor"] = 'jondor tuman'
            else:
                buxoro["❌Jondor"] = 'jondor tuman'
            if "kogon shahar" in list:
                buxoro["✅Kogon shahar"] = 'kogon shahar'
            else:
                buxoro["❌Kogon shahar"] = 'kogon shahar'
            if "kogon tuman" in list:
                buxoro["✅Kogon tuman"] = 'kogon tuman'
            else:
                buxoro["❌Kogon tuman"] = 'kogon tuman'
            if "qorako'l tuman" in list:
                buxoro["✅Qorakoʻl"] = "qorako'l tuman"
            else:
                buxoro["❌Qorakoʻl"] = 'qorako\'l tuman'
            if "qorovulbozor tuman" in list:
                buxoro["✅Qorovulbozor"] = "qorovulbozor tuman"
            else:
                buxoro["❌Qorovulbozor"] = 'qorovulbozor tuman'
            if "peshku tuman" in list:
                buxoro["✅Peshku"] = "peshku tuman"
            else:
                buxoro["❌Peshku"] = "peshku tuman"
            if "romitan tuman" in list:
                buxoro["✅Romitan"] = "romitan tuman"
            else:
                buxoro["❌Romitan"] = 'romitan tuman'
            if "shofirkon tuman" in list:
                buxoro["✅Shofirkon"] = "shofirkon tuman"
            else:
                buxoro["❌Shofirkon"] = "shofirkon tuman"
            if "vobkent tuman" in list:
                buxoro["✅Vobkent"] = "vobkent tuman"
            else:
                buxoro["❌Vobkent"] = "vobkent tuman"

            shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
            for key, value in buxoro.items():
                shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            for key, value in buxoro.items():
                if call.data == value:
                    await call.message.edit_reply_markup(shaxsiy_buxoro)
                    await BuxoroStatesGroup.buxoro.set()
