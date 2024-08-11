from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.edit_district.sozlamalar import SozlamalarStates,EngBirinchiSozlamaState
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, toshkent_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.toshtuman import toshkent_viloyati_tumanlari
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db


class ToshkentStatesGroup(StatesGroup):
    toshkent=State()
    toshkent_eng_birinchi=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='kentt'),state=EngBirinchiSozlamaState.viloyat_filter)
async def toshkenttuman(call:CallbackQuery):
    

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        toshkent = {}
        if "toshkent tuman" in list:
            toshkent["✅Toshkent tuman"] = "toshkent tuman"
        else:
            toshkent["❌Toshkent tuman"] = "toshkent tuman"
        if "bekobod tumani" in list:
            toshkent["✅Bekobod tuman"] = "bekobod tumani"
        else:
            toshkent["❌Bekobod tuman"] = "bekobod tumani"
        if "bekobod shahar" in list:
            toshkent["✅Bekobod shahar"] = "bekobod shahar"
        else:
            toshkent["❌Bekobod shahar"] = "bekobod shahar"
        if "bostonliq tumani" in list:
            toshkent["✅Boʻstonliq tuman"] = 'bostonliq tumani'
        else:
            toshkent["❌Boʻstonliq tuman"] = 'bostonliq tumani'
        if "boka tumani" in list:
            toshkent["✅Boʻka"] = "boka tumani"
        else:
            toshkent["❌Boʻka"] = "boka tumani"
        if "chinoz tumani" in list:
            toshkent["✅Chinoz"] = 'chinoz tumani'
        else:
            toshkent["❌Chinoz"] = 'chinoz tumani'
        if "qibray tumani" in list:
            toshkent["✅Qibray"] = 'qibray tumani'
        else:
            toshkent["❌Qibray"] = 'qibray tumani'
        if "ohangaron tumani" in list:
            toshkent["✅Ohangaron tuman"] = "ohangaron tumani"
        else:
            toshkent["❌Ohangaron tuman"] = 'ohangaron tumani'
        if "ohangaron shahar" in list:
            toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
        else:
            toshkent["❌Ohangaron shahri"] = 'ohangaron shahar'
        if "oqqorgon tumani" in list:
            toshkent["✅Oqqoʻrgʻon"] = "oqqorgon tumani"
        else:
            toshkent["❌Oqqoʻrgʻon"] = 'oqqorgon tumani'
        if "parkent tumani" in list:
            toshkent["✅Parkent"] = "parkent tumani"
        else:
            toshkent["❌Parkent"] = "parkent tumani"
        if "piskent tumani" in list:
            toshkent["✅Piskent"] = "piskent tumani"
        else:
            toshkent["❌Piskent"] = 'piskent tumani'
        if "quyichirchiq tumani" in list:
            toshkent["✅Quyi Chirchiq"] = "quyichirchiq tumani"
        else:
            toshkent["❌Quyi Chirchiq"] = "quyichirchiq tumani"
        if "ortachirchiq tumani" in list:
            toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq tumani"
        else:
            toshkent["❌Oʻrta Chirchiq"] = "ortachirchiq tumani"
        if "yangiyol tumani" in list:
            toshkent["✅Yangiyoʻl"] = "yangiyol tumani"
        else:
            toshkent["❌Yangiyoʻl"] = "yangiyol tumani"
        if "yangiyol shahar" in list:
            toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahar"
        else:
            toshkent["❌Yangiyoʻl shahri"] = "yangiyol shahar"
        if "yuqorichirchiq tumani" in list:
            toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq tumani"
        else:
            toshkent["❌Yuqori Chirchiq"] = "yuqorichirchiq tumani"
        if "zangiota tumani" in list:
            toshkent["✅Zangiota"] = "zangiota tumani"
        else:
            toshkent["❌Zangiota"] = "zangiota tumani"
        if "olmaliq shahar" in list:
            toshkent["✅Olmaliq shahri"] = "olmaliq shahar"
        else:
            toshkent["❌Olmaliq shahri"] = "olmaliq shahar"
        if "nurafshon shahar" in list:
            toshkent["✅Nurafshon shahri"] = "nurafshon shahar"
        else:
            toshkent["❌Nurafshon shahri"] = "nurafshon shahar"
        if "angren shahar" in list:
            toshkent["✅Angren shahar"] = "angren shahar"
        else:
            toshkent["❌Angren shahr"] = "angren shahar"
        if "chirchiq shahar" in list:
            toshkent["✅Chirchiq shahri"] = "chirchiq shahar"
        else:
            toshkent["❌Chirchiq shahri"] = "chirchiq shahar"
        if "qoyliq" in list:
            toshkent["✅Qo'yliq"] = "qoyliq"
        else:
            toshkent["❌Qo'yliq"] = "qoyliq"
        shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
        for key, value in toshkent.items():
            shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_toshkent.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Toshkentning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_toshkent)

        await ToshkentStatesGroup.toshkent_eng_birinchi.set()
        await call.message.delete()
@dp.callback_query_handler(state=ToshkentStatesGroup.toshkent_eng_birinchi)
async def toshkent_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Toshkent", tuman="toshkent tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="angren shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="nurafshon shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="bekobod shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="olmaliq shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="chirchiq shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="bekobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="bostonliq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="boka tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="chinoz tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="qibray tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="ohangaron shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="ohangaron tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="oqqorgon tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="parkent tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="piskent tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="quyichirchiq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="ortachirchiq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="yangiyol shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="yangiyol tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="yuqorichirchiq tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="zangiota tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent", tuman="qoyliq", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            toshkent = {}
            if "toshkent tuman" in list:
                toshkent["✅Toshkent tuman"] = "toshkent tuman"
            else:
                toshkent["❌Toshkent tuman"] = "toshkent tuman"
            if "bekobod tumani" in list:
                toshkent["✅Bekobod tuman"] = "bekobod tumani"
            else:
                toshkent["❌Bekobod tuman"] = "bekobod tumani"
            if "bekobod shahar" in list:
                toshkent["✅Bekobod shahar"] = "bekobod shahar"
            else:
                toshkent["❌Bekobod shahar"] = "bekobod shahar"
            if "bostonliq tumani" in list:
                toshkent["✅Boʻstonliq tuman"] = 'bostonliq tumani'
            else:
                toshkent["❌Boʻstonliq tuman"] = 'bostonliq tumani'
            if "boka tumani" in list:
                toshkent["✅Boʻka"] = "boka tumani"
            else:
                toshkent["❌Boʻka"] = "boka tumani"
            if "chinoz tumani" in list:
                toshkent["✅Chinoz"] = 'chinoz tumani'
            else:
                toshkent["❌Chinoz"] = 'chinoz tumani'
            if "qibray tumani" in list:
                toshkent["✅Qibray"] = 'qibray tumani'
            else:
                toshkent["❌Qibray"] = 'qibray tumani'
            if "ohangaron tumani" in list:
                toshkent["✅Ohangaron tuman"] = "ohangaron tumani"
            else:
                toshkent["❌Ohangaron tuman"] = 'ohangaron tumani'
            if "ohangaron shahar" in list:
                toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
            else:
                toshkent["❌Ohangaron shahri"] = 'ohangaron shahar'
            if "oqqorgon tumani" in list:
                toshkent["✅Oqqoʻrgʻon"] = "oqqorgon tumani"
            else:
                toshkent["❌Oqqoʻrgʻon"] = 'oqqorgon tumani'
            if "parkent tumani" in list:
                toshkent["✅Parkent"] = "parkent tumani"
            else:
                toshkent["❌Parkent"] = "parkent tumani"
            if "piskent tumani" in list:
                toshkent["✅Piskent"] = "piskent tumani"
            else:
                toshkent["❌Piskent"] = 'piskent tumani'
            if "quyichirchiq tumani" in list:
                toshkent["✅Quyi Chirchiq"] = "quyichirchiq tumani"
            else:
                toshkent["❌Quyi Chirchiq"] = "quyichirchiq tumani"
            if "ortachirchiq tumani" in list:
                toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq tumani"
            else:
                toshkent["❌Oʻrta Chirchiq"] = "ortachirchiq tumani"
            if "yangiyol tumani" in list:
                toshkent["✅Yangiyoʻl"] = "yangiyol tumani"
            else:
                toshkent["❌Yangiyoʻl"] = "yangiyol tumani"
            if "yangiyol shahar" in list:
                toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahar"
            else:
                toshkent["❌Yangiyoʻl shahri"] = "yangiyol shahar"
            if "yuqorichirchiq tumani" in list:
                toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq tumani"
            else:
                toshkent["❌Yuqori Chirchiq"] = "yuqorichirchiq tumani"
            if "zangiota tumani" in list:
                toshkent["✅Zangiota"] = "zangiota tumani"
            else:
                toshkent["❌Zangiota"] = "zangiota tumani"
            if "olmaliq shahar" in list:
                toshkent["✅Olmaliq shahri"] = "olmaliq shahar"
            else:
                toshkent["❌Olmaliq shahri"] = "olmaliq shahar"
            if "nurafshon shahar" in list:
                toshkent["✅Nurafshon shahri"] = "nurafshon shahar"
            else:
                toshkent["❌Nurafshon shahri"] = "nurafshon shahar"
            if "angren shahar" in list:
                toshkent["✅Angren shahar"] = "angren shahar"
            else:
                toshkent["❌Angren shahr"] = "angren shahar"
            if "chirchiq shahar" in list:
                toshkent["✅Chirchiq shahri"] = "chirchiq shahar"
            else:
                toshkent["❌Chirchiq shahri"] = "chirchiq shahar"
            if "qoyliq" in list:
                toshkent["✅Qo'yliq"] = "qoyliq"
            else:
                toshkent["❌Qo'yliq"] = "qoyliq"
            shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
            for key, value in toshkent.items():
                shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_toshkent)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Toshkent", tuman="toshkent tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="angren shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="nurafshon shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="bekobod shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="olmaliq shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="chirchiq shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="bekobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="bostonliq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="boka tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="chinoz tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="qibray tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="ohangaron shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="ohangaron tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="oqqorgon tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="parkent tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="piskent tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="quyichirchiq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="ortachirchiq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="yangiyol shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="yangiyol tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="yuqorichirchiq tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="zangiota tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent", tuman="qoyliq", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            toshkent = {}
            if "toshkent tuman" in list:
                toshkent["✅Toshkent tuman"] = "toshkent tuman"
            else:
                toshkent["❌Toshkent tuman"] = "toshkent tuman"
            if "bekobod tumani" in list:
                toshkent["✅Bekobod tuman"] = "bekobod tumani"
            else:
                toshkent["❌Bekobod tuman"] = "bekobod tumani"
            if "bekobod shahar" in list:
                toshkent["✅Bekobod shahar"] = "bekobod shahar"
            else:
                toshkent["❌Bekobod shahar"] = "bekobod shahar"
            if "bostonliq tumani" in list:
                toshkent["✅Boʻstonliq tuman"] = 'bostonliq tumani'
            else:
                toshkent["❌Boʻstonliq tuman"] = 'bostonliq tumani'
            if "boka tumani" in list:
                toshkent["✅Boʻka"] = "boka tumani"
            else:
                toshkent["❌Boʻka"] = "boka tumani"
            if "chinoz tumani" in list:
                toshkent["✅Chinoz"] = 'chinoz tumani'
            else:
                toshkent["❌Chinoz"] = 'chinoz tumani'
            if "qibray tumani" in list:
                toshkent["✅Qibray"] = 'qibray tumani'
            else:
                toshkent["❌Qibray"] = 'qibray tumani'
            if "ohangaron tumani" in list:
                toshkent["✅Ohangaron tuman"] = "ohangaron tumani"
            else:
                toshkent["❌Ohangaron tuman"] = 'ohangaron tumani'
            if "ohangaron shahar" in list:
                toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
            else:
                toshkent["❌Ohangaron shahri"] = 'ohangaron shahar'
            if "oqqorgon tumani" in list:
                toshkent["✅Oqqoʻrgʻon"] = "oqqorgon tumani"
            else:
                toshkent["❌Oqqoʻrgʻon"] = 'oqqorgon tumani'
            if "parkent tumani" in list:
                toshkent["✅Parkent"] = "parkent tumani"
            else:
                toshkent["❌Parkent"] = "parkent tumani"
            if "piskent tumani" in list:
                toshkent["✅Piskent"] = "piskent tumani"
            else:
                toshkent["❌Piskent"] = 'piskent tumani'
            if "quyichirchiq tumani" in list:
                toshkent["✅Quyi Chirchiq"] = "quyichirchiq tumani"
            else:
                toshkent["❌Quyi Chirchiq"] = "quyichirchiq tumani"
            if "ortachirchiq tumani" in list:
                toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq tumani"
            else:
                toshkent["❌Oʻrta Chirchiq"] = "ortachirchiq tumani"
            if "yangiyol tumani" in list:
                toshkent["✅Yangiyoʻl"] = "yangiyol tumani"
            else:
                toshkent["❌Yangiyoʻl"] = "yangiyol tumani"
            if "yangiyol shahar" in list:
                toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahar"
            else:
                toshkent["❌Yangiyoʻl shahri"] = "yangiyol shahar"
            if "yuqorichirchiq tumani" in list:
                toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq tumani"
            else:
                toshkent["❌Yuqori Chirchiq"] = "yuqorichirchiq tumani"
            if "zangiota tumani" in list:
                toshkent["✅Zangiota"] = "zangiota tumani"
            else:
                toshkent["❌Zangiota"] = "zangiota tumani"
            if "olmaliq shahar" in list:
                toshkent["✅Olmaliq shahri"] = "olmaliq shahar"
            else:
                toshkent["❌Olmaliq shahri"] = "olmaliq shahar"
            if "nurafshon shahar" in list:
                toshkent["✅Nurafshon shahri"] = "nurafshon shahar"
            else:
                toshkent["❌Nurafshon shahri"] = "nurafshon shahar"
            if "angren shahar" in list:
                toshkent["✅Angren shahar"] = "angren shahar"
            else:
                toshkent["❌Angren shahr"] = "angren shahar"
            if "chirchiq shahar" in list:
                toshkent["✅Chirchiq shahri"] = "chirchiq shahar"
            else:
                toshkent["❌Chirchiq shahri"] = "chirchiq shahar"
            if "qoyliq" in list:
                toshkent["✅Qo'yliq"] = "qoyliq"
            else:
                toshkent["❌Qo'yliq"] = "qoyliq"
            shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
            for key, value in toshkent.items():
                shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_toshkent)

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
        toshkent = {}
        if "toshkent tuman" in list:
            toshkent["✅Toshkent tuman"] = "toshkent tuman"
        else:
            toshkent["❌Toshkent tuman"] = "toshkent tuman"
        if "bekobod tumani" in list:
            toshkent["✅Bekobod tuman"] = "bekobod tumani"
        else:
            toshkent["❌Bekobod tuman"] = "bekobod tumani"
        if "bekobod shahar" in list:
            toshkent["✅Bekobod shahar"] = "bekobod shahar"
        else:
            toshkent["❌Bekobod shahar"] = "bekobod shahar"
        if "bostonliq tumani" in list:
            toshkent["✅Boʻstonliq tuman"] = 'bostonliq tumani'
        else:
            toshkent["❌Boʻstonliq tuman"] = 'bostonliq'
        if "boka tumani" in list:
            toshkent["✅Boʻka"] = "boka tumani"
        else:
            toshkent["❌Boʻka"] = "boka tumani"
        if "chinoz tumani" in list:
            toshkent["✅Chinoz"] = 'chinoz tumani'
        else:
            toshkent["❌Chinoz"] = 'chinoz tumani'
        if "qibray tumani" in list:
            toshkent["✅Qibray"] = 'qibray tumani'
        else:
            toshkent["❌Qibray"] = 'qibray tumani'
        if "ohangaron tumani" in list:
            toshkent["✅Ohangaron tuman"] = "ohangaron tumani"
        else:
            toshkent["❌Ohangaron tuman"] = 'ohangaron tumani'
        if "ohangaron shahar" in list:
            toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
        else:
            toshkent["❌Ohangaron shahri"] = 'ohangaron shahar'
        if "oqqorgon tumani" in list:
            toshkent["✅Oqqoʻrgʻon"] = "oqqorgon tumani"
        else:
            toshkent["❌Oqqoʻrgʻon"] = 'oqqorgon tumani'
        if "parkent tumani" in list:
            toshkent["✅Parkent"] = "parkent tumani"
        else:
            toshkent["❌Parkent"] = "parkent tumani"
        if "piskent tumani" in list:
            toshkent["✅Piskent"] = "piskent tumani"
        else:
            toshkent["❌Piskent"] = 'piskent tumani'
        if "quyichirchiq tumani" in list:
            toshkent["✅Quyi Chirchiq"] = "quyichirchiq tumani"
        else:
            toshkent["❌Quyi Chirchiq"] = "quyichirchiq tumani"
        if "ortachirchiq tumani" in list:
            toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq tumani"
        else:
            toshkent["❌Oʻrta Chirchiq"] = "ortachirchiq tumani"
        if "yangiyol tumani" in list:
            toshkent["✅Yangiyoʻl"] = "yangiyol tumani"
        else:
            toshkent["❌Yangiyoʻl"] = "yangiyol tumani"
        if "yangiyol shahar" in list:
            toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahar"
        else:
            toshkent["❌Yangiyoʻl shahri"] = "yangiyol shahar"
        if "yuqorichirchiq tumani" in list:
            toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq tumani"
        else:
            toshkent["❌Yuqori Chirchiq"] = "yuqorichirchiq tumani"
        if "zangiota tumani" in list:
            toshkent["✅Zangiota"] = "zangiota tumani"
        else:
            toshkent["❌Zangiota"] = "zangiota tumani"
        if "olmaliq shahar" in list:
            toshkent["✅Olmaliq shahri"] = "olmaliq shahar"
        else:
            toshkent["❌Olmaliq shahri"] = "olmaliq shahar"
        if "nurafshon shahar" in list:
            toshkent["✅Nurafshon shahri"] = "nurafshon shahar"
        else:
            toshkent["❌Nurafshon shahri"] = "nurafshon shahar"
        if "angren shahar" in list:
            toshkent["✅Angren shahar"] = "angren shahar"
        else:
            toshkent["❌Angren shahr"] = "angren shahar"
        if "chirchiq shahar" in list:
            toshkent["✅Chirchiq shahri"] = "chirchiq shahar"
        else:
            toshkent["❌Chirchiq shahri"] = "chirchiq shahar"
        if "qoyliq" in list:
            toshkent["✅Qo'yliq"] = "qoyliq"
        else:
            toshkent["❌Qo'yliq"] = "qoyliq"
        shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
        for key, value in toshkent.items():
            shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        for key, value in toshkent.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_toshkent)
                await ToshkentStatesGroup.toshkent_eng_birinchi.set()
