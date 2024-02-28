from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, andijon_callback, \
    menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, bot, db


class HaydovchiEdit(StatesGroup):
    andijon=State()


# A N D I J O N   V I L O Y T I

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='jonn'),state=SozlamalarStates.viloyat_filter)
async def andijontuman(call:CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        andijon = {}
        if "andijon shaxar" in list:
            andijon["✅Andijon shaxar"] = 'andijon shaxar'
        else:
            andijon["❌Andijon shaxar"] = 'andijon shaxar'
        if "andijon tuman" in list:
            andijon["✅Andijon tuman"] = "andijon tuman"
        else:
            andijon["❌Andijon tuman"] = 'andijon tuman'
        if "ulug'nor tuman" in list:
            andijon["✅Ulug'nor"] = "ulug'nor tuman"
        else:
            andijon["❌Ulug'nor"] = "ulug'nor tuman"
        if "asaka tuman" in list:
            andijon["✅Asaka"] = "asaka tuman"
        else:
            andijon["❌Asaka"] = "asaka tuman"
        if "paxtaobod tuman" in list:
            andijon["✅Paxtaobod"] = 'paxtaobod tuman'
        else:
            andijon["❌Paxtaobod"] = 'paxtaobod tuman'
        if "shaxrixon tuman" in list:
            andijon["✅Shaxrixon"] = 'shaxrixon tuman'
        else:
            andijon["❌Shaxrixon"] = 'shaxrixon tuman'
        if "marhamat tuman" in list:
            andijon["✅Marhamat"] = "marhamat tuman"
        else:
            andijon["❌Marhamat"] = 'marhamat tuman'
        if "xonabod shahar" in list:
            andijon["✅Xonabod shahar"] = "xonabod shahar"
        else:
            andijon["❌Xonabod shahar"] = 'xonabod shahar'
        if "oltinko'l tuman" in list:
            andijon["✅Oltinko'l"] = "oltinko'l tuman"
        else:
            andijon["❌Oltinko'l"] = "oltinko'l tuman"
        if "baliqchi tuman" in list:
            andijon["✅Baliqchi"] = "baliqchi tuman"
        else:
            andijon["❌Baliqchi"] = 'baliqchi tuman'
        if "bo'ston tuman" in list:
            andijon["✅Bo'ston"] = "bo'ston tuman"
        else:
            andijon["❌Bo'ston"] = "bo'ston tuman"
        if "buloqboshi tuman" in list:
            andijon["✅Buloqboshi"] = "buloqboshi tuman"
        else:
            andijon["❌Buloqboshi"] = "buloqboshi tuman"
        if "izboskan tuman" in list:
            andijon["✅Izboskan"] = "izboskan tuman"
        else:
            andijon["❌Izboskan"] = "izboskan tuman"
        if "jalaquduq tuman" in list:
            andijon["✅Jalaquduq"] = "jalaquduq tuman"
        else:
            andijon["❌Jalaquduq"] = "jalaquduq tuman"
        if "xo'jabod tuman" in list:
            andijon["✅Xo'jabod"] = "xo'jabod tuman"
        else:
            andijon["❌Xo'jabod"] = "xo'jabod tuman"
        if "qo'rg'ontepa tuman" in list:

            andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
        else:
            andijon["❌Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
        for key, value in andijon.items():
            shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Andijonning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_tugma)

        await HaydovchiEdit.andijon.set()
        await call.message.delete()


@dp.callback_query_handler(state=HaydovchiEdit.andijon)
async def andijon_state(call:CallbackQuery,state:FSMContext):
        if call.data == "hammasiniradetish":
            await db.delete_driver_info(viloyat="Andijon", tuman="ulug'nor tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="andijon tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="asaka tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="paxtaobod tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="shaxrixon tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="marhamat tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="xonabod shahar", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="oltinko'l tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="baliqchi tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="bo'ston tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="buloqboshi tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="izboskan tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="jalaquduq tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="xo'jabod tuman", telegram_id=call.from_user.id)
            await db.delete_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa tuman", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            andijon = {}
            if "andijon shaxar" in list:
                andijon["✅Andijon shaxar"] = 'andijon shaxar'
            else:
                andijon["❌Andijon shaxar"] = 'andijon shaxar'
            if "andijon tuman" in list:
                andijon["✅Andijon tuman"] = "andijon tuman"
            else:
                andijon["❌Andijon tuman"] = 'andijon tuman'
            if "ulug'nor tuman" in list:
                andijon["✅Ulug'nor"] = "ulug'nor tuman"
            else:
                andijon["❌Ulug'nor"] = "ulug'nor tuman"
            if "asaka tuman" in list:
                andijon["✅Asaka"] = "asaka tuman"
            else:
                andijon["❌Asaka"] = "asaka tuman"
            if "paxtaobod tuman" in list:
                andijon["✅Paxtaobod"] = 'paxtaobod tuman'
            else:
                andijon["❌Paxtaobod"] = 'paxtaobod tuman'
            if "shaxrixon tuman" in list:
                andijon["✅Shaxrixon"] = 'shaxrixon tuman'
            else:
                andijon["❌Shaxrixon"] = 'shaxrixon tuman'
            if "marhamat tuman" in list:
                andijon["✅Marhamat"] = "marhamat tuman"
            else:
                andijon["❌Marhamat"] = 'marhamat tuman'
            if "xonabod shahar" in list:
                andijon["✅Xonabod shahar"] = "xonabod shahar"
            else:
                andijon["❌Xonabod shahar"] = 'xonabod shahar'
            if "oltinko'l tuman" in list:
                andijon["✅Oltinko'l"] = "oltinko'l tuman"
            else:
                andijon["❌Oltinko'l"] = "oltinko'l tuman"
            if "baliqchi tuman" in list:
                andijon["✅Baliqchi"] = "baliqchi tuman"
            else:
                andijon["❌Baliqchi"] = 'baliqchi tuman'
            if "bo'ston tuman" in list:
                andijon["✅Bo'ston"] = "bo'ston tuman"
            else:
                andijon["❌Bo'ston"] = "bo'ston tuman"
            if "buloqboshi tuman" in list:
                andijon["✅Buloqboshi"] = "buloqboshi tuman"
            else:
                andijon["❌Buloqboshi"] = "buloqboshi tuman"
            if "izboskan tuman" in list:
                andijon["✅Izboskan"] = "izboskan tuman"
            else:
                andijon["❌Izboskan"] = "izboskan tuman"
            if "jalaquduq tuman" in list:
                andijon["✅Jalaquduq"] = "jalaquduq tuman"
            else:
                andijon["❌Jalaquduq"] = "jalaquduq tuman"
            if "xo'jabod tuman" in list:
                andijon["✅Xo'jabod"] = "xo'jabod tuman"
            else:
                andijon["❌Xo'jabod"] = "xo'jabod tuman"
            if "qo'rg'ontepa tuman" in list:

                andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
            else:
                andijon["❌Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
            shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
            for key, value in andijon.items():
                shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.edit_reply_markup(shaxsiy_tugma)
        if call.data == "hammasinibelgilash":
            await db.add_driver_info(viloyat="Andijon", tuman="ulug'nor tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="andijon tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="asaka tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="paxtaobod tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="shaxrixon tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="marhamat tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="xonabod shahar", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="oltinko'l tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="baliqchi tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="bo'ston tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="buloqboshi tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="izboskan tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="jalaquduq tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="xo'jabod tuman", telegram_id=call.from_user.id)
            await db.add_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa tuman", telegram_id=call.from_user.id)
            jamii = await db.select_all_driver_info()
            list = []
            for i in jamii:
                if i[3] == call.from_user.id:
                    list.append(i[2])
            andijon = {}
            if "andijon shaxar" in list:
                andijon["✅Andijon shaxar"] = 'andijon shaxar'
            else:
                andijon["❌Andijon shaxar"] = 'andijon shaxar'
            if "andijon tuman" in list:
                andijon["✅Andijon tuman"] = "andijon tuman"
            else:
                andijon["❌Andijon tuman"] = 'andijon tuman'
            if "ulug'nor tuman" in list:
                andijon["✅Ulug'nor"] = "ulug'nor tuman"
            else:
                andijon["❌Ulug'nor"] = "ulug'nor tuman"
            if "asaka tuman" in list:
                andijon["✅Asaka"] = "asaka tuman"
            else:
                andijon["❌Asaka"] = "asaka tuman"
            if "paxtaobod tuman" in list:
                andijon["✅Paxtaobod"] = 'paxtaobod tuman'
            else:
                andijon["❌Paxtaobod"] = 'paxtaobod tuman'
            if "shaxrixon tuman" in list:
                andijon["✅Shaxrixon"] = 'shaxrixon tuman'
            else:
                andijon["❌Shaxrixon"] = 'shaxrixon tuman'
            if "marhamat tuman" in list:
                andijon["✅Marhamat"] = "marhamat tuman"
            else:
                andijon["❌Marhamat"] = 'marhamat tuman'
            if "xonabod shahar" in list:
                andijon["✅Xonabod shahar"] = "xonabod shahar"
            else:
                andijon["❌Xonabod shahar"] = 'xonabod shahar'
            if "oltinko'l tuman" in list:
                andijon["✅Oltinko'l"] = "oltinko'l tuman"
            else:
                andijon["❌Oltinko'l"] = "oltinko'l tuman"
            if "baliqchi tuman" in list:
                andijon["✅Baliqchi"] = "baliqchi tuman"
            else:
                andijon["❌Baliqchi"] = 'baliqchi tuman'
            if "bo'ston tuman" in list:
                andijon["✅Bo'ston"] = "bo'ston tuman"
            else:
                andijon["❌Bo'ston"] = "bo'ston tuman"
            if "buloqboshi tuman" in list:
                andijon["✅Buloqboshi"] = "buloqboshi tuman"
            else:
                andijon["❌Buloqboshi"] = "buloqboshi tuman"
            if "izboskan tuman" in list:
                andijon["✅Izboskan"] = "izboskan tuman"
            else:
                andijon["❌Izboskan"] = "izboskan tuman"
            if "jalaquduq tuman" in list:
                andijon["✅Jalaquduq"] = "jalaquduq tuman"
            else:
                andijon["❌Jalaquduq"] = "jalaquduq tuman"
            if "xo'jabod tuman" in list:
                andijon["✅Xo'jabod"] = "xo'jabod tuman"
            else:
                andijon["❌Xo'jabod"] = "xo'jabod tuman"
            if "qo'rg'ontepa tuman" in list:

                andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
            else:
                andijon["❌Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
            shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
            for key, value in andijon.items():
                shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
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
            await db.add_driver_info(viloyat="Farg'ona", telegram_id=call.from_user.id, tuman=call.data)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        andijon = {}
        if "andijon shaxar" in list:
            andijon["✅Andijon shaxar"] = 'andijon shaxar'
        else:
            andijon["❌Andijon shaxar"] = 'andijon shaxar'
        if "andijon tuman" in list:
            andijon["✅Andijon tuman"] = "andijon tuman"
        else:
            andijon["❌Andijon tuman"] = 'andijon tuman'
        if "ulug'nor tuman" in list:
            andijon["✅Ulug'nor"] = "ulug'nor tuman"
        else:
            andijon["❌Ulug'nor"] = "ulug'nor tuman"
        if "asaka tuman" in list:
            andijon["✅Asaka"] = "asaka tuman"
        else:
            andijon["❌Asaka"] = "asaka tuman"
        if "paxtaobod tuman" in list:
            andijon["✅Paxtaobod"] = 'paxtaobod tuman'
        else:
            andijon["❌Paxtaobod"] = 'paxtaobod tuman'
        if "shaxrixon tuman" in list:
            andijon["✅Shaxrixon"] = 'shaxrixon tuman'
        else:
            andijon["❌Shaxrixon"] = 'shaxrixon tuman'
        if "marhamat tuman" in list:
            andijon["✅Marhamat"] = "marhamat tuman"
        else:
            andijon["❌Marhamat"] = 'marhamat tuman'
        if "xonabod shahar" in list:
            andijon["✅Xonabod shahar"] = "xonabod shahar"
        else:
            andijon["❌Xonabod shahar"] = 'xonabod shahar'
        if "oltinko'l tuman" in list:
            andijon["✅Oltinko'l"] = "oltinko'l tuman"
        else:
            andijon["❌Oltinko'l"] = "oltinko'l tuman"
        if "baliqchi tuman" in list:
            andijon["✅Baliqchi"] = "baliqchi tuman"
        else:
            andijon["❌Baliqchi"] = 'baliqchi tuman'
        if "bo'ston tuman" in list:
            andijon["✅Bo'ston"] = "bo'ston tuman"
        else:
            andijon["❌Bo'ston"] = "bo'ston tuman"
        if "buloqboshi tuman" in list:
            andijon["✅Buloqboshi"] = "buloqboshi tuman"
        else:
            andijon["❌Buloqboshi"] = "buloqboshi tuman"
        if "izboskan tuman" in list:
            andijon["✅Izboskan"] = "izboskan tuman"
        else:
            andijon["❌Izboskan"] = "izboskan tuman"
        if "jalaquduq tuman" in list:
            andijon["✅Jalaquduq"] = "jalaquduq tuman"
        else:
            andijon["❌Jalaquduq"] = "jalaquduq tuman"
        if "xo'jabod tuman" in list:
            andijon["✅Xo'jabod"] = "xo'jabod tuman"
        else:
            andijon["❌Xo'jabod"] = "xo'jabod tuman"
        if "qo'rg'ontepa tuman" in list:

            andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
        else:
            andijon["❌Qo'rg'ontepa"] = "qo'rg'ontepa tuman"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
        for key, value in andijon.items():
            shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

        for key, value in andijon.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_tugma)
                await HaydovchiEdit.andijon.set()
