from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db


class Toshkent_shaharStatesGroup(StatesGroup):
    shahar=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='kent shahar'),state=SozlamalarStates.viloyat_filter)
async def fargona_edit(call:CallbackQuery):
    
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        tosh_shahar = {}
        if "Toshkent shahar" in list:
            tosh_shahar["✅Toshkent shahar"] = "Toshkent shahar"
        else:
            tosh_shahar["❌Toshkent shahar"] = "Toshkent shahar"
        if "Bektemir tumani" in list:
            tosh_shahar["✅Bektemir tumani"] = "Bektemir tumani"
        else:
            tosh_shahar["❌Bektemir tumani"] = "Bektemir tumani"
        if "Mirzo Ulug'bek tumani" in list:
            tosh_shahar["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
        else:
            tosh_shahar["❌Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
        if "Mirobod tumani" in list:
            tosh_shahar["✅Mirobod tumani"] = "Mirobod tumani"
        else:
            tosh_shahar["❌Mirobod tumani"] = "Mirobod tumani"
        if "Olmazor tumani" in list:
            tosh_shahar["✅Olmazor tumani"] = 'Olmazor tumani'
        else:
            tosh_shahar["❌Olmazor tumani"] = 'Olmazor tumani'
        if "Sirg'ali tumani" in list:
            tosh_shahar["✅Sirg‘ali tumani"] = "Sirg'ali tumani"
        else:
            tosh_shahar["❌Sirg‘ali tumani"] = "Sirg'ali tumani"
        if "Uchtepa tumani" in list:
            tosh_shahar["✅Uchtepa tumani"] = "Uchtepa tumani"
        else:
            tosh_shahar["❌Uchtepa tumani"] = "Uchtepa tumani"
        if "Chilonzor tumani" in list:
            tosh_shahar["✅Chilonzor tumani"] = "Chilonzor tumani"
        else:
            tosh_shahar["❌Chilonzor tumani"] = 'Chilonzor tumani'
        if "Shayxontohur tumani" in list:
            tosh_shahar["✅Shayxontohur tumani"] = "Shayxontohur tumani"
        else:
            tosh_shahar["❌Shayxontohur tumani"] = "Shayxontohur tumani"
        if "Yunusobod tumani" in list:
            tosh_shahar["✅Yunusobod tumani"] = "Yunusobod tumani"
        else:
            tosh_shahar["❌Yunusobod tumani"] = 'Yunusobod tumani'
        if "Yakkasaroy tumani" in list:
            tosh_shahar["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
        else:
            tosh_shahar["❌Yakkasaroy tumani"] = "Yakkasaroy tumani"
        if "Yashnobod tumani" in list:
            tosh_shahar["✅Yashnobod tumani"] = "Yashnobod tumani"
        else:
            tosh_shahar["❌Yashnobod tumani"] = "Yashnobod tumani"

        shaxsiy_tosh_shahar = InlineKeyboardMarkup(row_width=3)
        for key, value in tosh_shahar.items():
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Toshkent shaharning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                      "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                      "❌ - chiqqan holat\n\n✅- kirgan holat ",reply_markup=shaxsiy_tosh_shahar)

        await Toshkent_shaharStatesGroup.shahar.set()
        await call.message.delete()
@dp.callback_query_handler(state=Toshkent_shaharStatesGroup.shahar)
async def toshkent_shahar_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Toshkent shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Bektemir tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Mirzo Ulug'bek tumani",
                                     telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Mirobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Olmazor tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Sirg'ali tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Uchtepa tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Chilonzor tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Shayxontohur tumani",
                                     telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Yunusobod tumani", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Yakkasaroy tumani",
                                     telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Toshkent shahar", tuman="Yashnobod tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            tosh_shahar = {}
            if "Toshkent shahar" in list:
                tosh_shahar["✅Toshkent shahar"] = "Toshkent shahar"
            else:
                tosh_shahar["❌Toshkent shahar"] = "Toshkent shahar"
            if "Bektemir tumani" in list:
                tosh_shahar["✅Bektemir tumani"] = "Bektemir tumani"
            else:
                tosh_shahar["❌Bektemir tumani"] = "Bektemir tumani"
            if "Mirzo Ulug'bek tumani" in list:
                tosh_shahar["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
            else:
                tosh_shahar["❌Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
            if "Mirobod tumani" in list:
                tosh_shahar["✅Mirobod tumani"] = "Mirobod tumani"
            else:
                tosh_shahar["❌Mirobod tumani"] = "Mirobod tumani"
            if "Olmazor tumani" in list:
                tosh_shahar["✅Olmazor tumani"] = 'Olmazor tumani'
            else:
                tosh_shahar["❌Olmazor tumani"] = 'Olmazor tumani'
            if "Sirg'ali tumani" in list:
                tosh_shahar["✅Sirg‘ali tumani"] = "Sirg'ali tumani"
            else:
                tosh_shahar["❌Sirg‘ali tumani"] = "Sirg'ali tumani"
            if "Uchtepa tumani" in list:
                tosh_shahar["✅Uchtepa tumani"] = "Uchtepa tumani"
            else:
                tosh_shahar["❌Uchtepa tumani"] = "Uchtepa tumani"
            if "Chilonzor tumani" in list:
                tosh_shahar["✅Chilonzor tumani"] = "Chilonzor tumani"
            else:
                tosh_shahar["❌Chilonzor tumani"] = 'Chilonzor tumani'
            if "Shayxontohur tumani" in list:
                tosh_shahar["✅Shayxontohur tumani"] = "Shayxontohur tumani"
            else:
                tosh_shahar["❌Shayxontohur tumani"] = "Shayxontohur tumani"
            if "Yunusobod tumani" in list:
                tosh_shahar["✅Yunusobod tumani"] = "Yunusobod tumani"
            else:
                tosh_shahar["❌Yunusobod tumani"] = 'Yunusobod tumani'
            if "Yakkasaroy tumani" in list:
                tosh_shahar["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
            else:
                tosh_shahar["❌Yakkasaroy tumani"] = "Yakkasaroy tumani"
            if "Yashnobod tumani" in list:
                tosh_shahar["✅Yashnobod tumani"] = "Yashnobod tumani"
            else:
                tosh_shahar["❌Yashnobod tumani"] = "Yashnobod tumani"

            shaxsiy_tosh_shahar = InlineKeyboardMarkup(row_width=3)
            for key, value in tosh_shahar.items():
                shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_tosh_shahar.insert(
                InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_tosh_shahar)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Toshkent shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Bektemir tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Mirzo Ulug'bek tumani",
                                     telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Mirobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Olmazor tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Sirg'ali tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Uchtepa tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Chilonzor tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Shayxontohur tumani",
                                     telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yunusobod tumani", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yakkasaroy tumani",
                                     telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yashnobod tumani", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            tosh_shahar = {}
            if "Toshkent shahar" in list:
                tosh_shahar["✅Toshkent shahar"] = "Toshkent shahar"
            else:
                tosh_shahar["❌Toshkent shahar"] = "Toshkent shahar"
            if "Bektemir tumani" in list:
                tosh_shahar["✅Bektemir tumani"] = "Bektemir tumani"
            else:
                tosh_shahar["❌Bektemir tumani"] = "Bektemir tumani"
            if "Mirzo Ulug'bek tumani" in list:
                tosh_shahar["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
            else:
                tosh_shahar["❌Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
            if "Mirobod tumani" in list:
                tosh_shahar["✅Mirobod tumani"] = "Mirobod tumani"
            else:
                tosh_shahar["❌Mirobod tumani"] = "Mirobod tumani"
            if "Olmazor tumani" in list:
                tosh_shahar["✅Olmazor tumani"] = 'Olmazor tumani'
            else:
                tosh_shahar["❌Olmazor tumani"] = 'Olmazor tumani'
            if "Sirg'ali tumani" in list:
                tosh_shahar["✅Sirg‘ali tumani"] = "Sirg'ali tumani"
            else:
                tosh_shahar["❌Sirg‘ali tumani"] = "Sirg'ali tumani"
            if "Uchtepa tumani" in list:
                tosh_shahar["✅Uchtepa tumani"] = "Uchtepa tumani"
            else:
                tosh_shahar["❌Uchtepa tumani"] = "Uchtepa tumani"
            if "Chilonzor tumani" in list:
                tosh_shahar["✅Chilonzor tumani"] = "Chilonzor tumani"
            else:
                tosh_shahar["❌Chilonzor tumani"] = 'Chilonzor tumani'
            if "Shayxontohur tumani" in list:
                tosh_shahar["✅Shayxontohur tumani"] = "Shayxontohur tumani"
            else:
                tosh_shahar["❌Shayxontohur tumani"] = "Shayxontohur tumani"
            if "Yunusobod tumani" in list:
                tosh_shahar["✅Yunusobod tumani"] = "Yunusobod tumani"
            else:
                tosh_shahar["❌Yunusobod tumani"] = 'Yunusobod tumani'
            if "Yakkasaroy tumani" in list:
                tosh_shahar["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
            else:
                tosh_shahar["❌Yakkasaroy tumani"] = "Yakkasaroy tumani"
            if "Yashnobod tumani" in list:
                tosh_shahar["✅Yashnobod tumani"] = "Yashnobod tumani"
            else:
                tosh_shahar["❌Yashnobod tumani"] = "Yashnobod tumani"

            shaxsiy_tosh_shahar = InlineKeyboardMarkup(row_width=3)
            for key, value in tosh_shahar.items():
                shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_tosh_shahar.insert(
                InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_tosh_shahar)
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
        tosh_shahar = {}
        if "Toshkent shahar" in list:
            tosh_shahar["✅Toshkent shahar"] = "Toshkent shahar"
        else:
            tosh_shahar["❌Toshkent shahar"] = "Toshkent shahar"
        if "Bektemir tumani" in list:
            tosh_shahar["✅Bektemir tumani"] = "Bektemir tumani"
        else:
            tosh_shahar["❌Bektemir tumani"] = "Bektemir tumani"
        if "Mirzo Ulug'bek tumani" in list:
            tosh_shahar["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
        else:
            tosh_shahar["❌Mirzo Ulug‘bek tumani"] = "Mirzo Ulug'bek tumani"
        if "Mirobod tumani" in list:
            tosh_shahar["✅Mirobod tumani"] = "Mirobod tumani"
        else:
            tosh_shahar["❌Mirobod tumani"] = "Mirobod tumani"
        if "Olmazor tumani" in list:
            tosh_shahar["✅Olmazor tumani"] = 'Olmazor tumani'
        else:
            tosh_shahar["❌Olmazor tumani"] = 'Olmazor tumani'
        if "Sirg'ali tumani" in list:
            tosh_shahar["✅Sirg‘ali tumani"] = "Sirg'ali tumani"
        else:
            tosh_shahar["❌Sirg‘ali tumani"] = "Sirg'ali tumani"
        if "Uchtepa tumani" in list:
            tosh_shahar["✅Uchtepa tumani"] = "Uchtepa tumani"
        else:
            tosh_shahar["❌Uchtepa tumani"] = "Uchtepa tumani"
        if "Chilonzor tumani" in list:
            tosh_shahar["✅Chilonzor tumani"] = "Chilonzor tumani"
        else:
            tosh_shahar["❌Chilonzor tumani"] = 'Chilonzor tumani'
        if "Shayxontohur tumani" in list:
            tosh_shahar["✅Shayxontohur tumani"] = "Shayxontohur tumani"
        else:
            tosh_shahar["❌Shayxontohur tumani"] = "Shayxontohur tumani"
        if "Yunusobod tumani" in list:
            tosh_shahar["✅Yunusobod tumani"] = "Yunusobod tumani"
        else:
            tosh_shahar["❌Yunusobod tumani"] = 'Yunusobod tumani'
        if "Yakkasaroy tumani" in list:
            tosh_shahar["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
        else:
            tosh_shahar["❌Yakkasaroy tumani"] = "Yakkasaroy tumani"
        if "Yashnobod tumani" in list:
            tosh_shahar["✅Yashnobod tumani"] = "Yashnobod tumani"
        else:
            tosh_shahar["❌Yashnobod tumani"] = "Yashnobod tumani"

        shaxsiy_tosh_shahar = InlineKeyboardMarkup(row_width=3)
        for key, value in tosh_shahar.items():
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        for key, value in tosh_shahar.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_tosh_shahar)
                await Toshkent_shaharStatesGroup.shahar.set()