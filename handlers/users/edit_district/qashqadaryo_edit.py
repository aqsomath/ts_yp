from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import SozlamalarStates
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp, db
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,qashqadaryo_callback
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_tumanlari


class QashqadaryoStatesGroup(StatesGroup):
    qashqadaryo=State()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='qadaryyy'),state=SozlamalarStates.viloyat_filter)
async def qashqadaryo_edit(call: CallbackQuery):

        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qashqadaryo = {}
        if "qarshi shahar" in list:
            qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
        else:
            qashqadaryo["❌Qarshi shahar"] = "qarshi shahar"
        if "dehqonobod tumani" in list:
            qashqadaryo["✅Dehqonobod"] = "dehqonobod tumani"
        else:
            qashqadaryo["❌Dehqonobod"] = "dehqonobod tumani"
        if "kasbi tumani" in list:
            qashqadaryo["✅Kasbi"] = "kasbi tumani"
        else:
            qashqadaryo["❌Kasbi"] = "kasbi tumani"
        if "kitob tumani" in list:
            qashqadaryo["✅Kitob"] = "kitob tumani"
        else:
            qashqadaryo["❌Kitob"] = "kitob tumani"
        if "koson tumani" in list:
            qashqadaryo["✅Koson"] = 'koson tumani'
        else:
            qashqadaryo["❌Koson"] = 'koson tumani'
        if "kokdala tumani" in list:
            qashqadaryo["✅Koʻkdala"] = 'kokdala tumani'
        else:
            qashqadaryo["❌Koʻkdala"] = 'kokdala tumani'
        if "mirishkor tumani" in list:
            qashqadaryo["✅Mirishkor"] = "mirishkor tumani"
        else:
            qashqadaryo["❌Mirishkor"] = 'mirishkor tumani'
        if "muborak tumani" in list:
            qashqadaryo["✅Muborak"] = "muborak tumani"
        else:
            qashqadaryo["❌Muborak"] = 'muborak tumani'
        if "nishon tumani" in list:
            qashqadaryo["✅Nishon"] = "nishon tumani"
        else:
            qashqadaryo["❌Nishon"] = "nishon tumani"
        if "qamashi tumani" in list:
            qashqadaryo["✅Qamashi"] = "qamashi tumani"
        else:
            qashqadaryo["❌Qamashi"] = 'qamashi tumani'
        if "qarshi tumani" in list:
            qashqadaryo["✅Qarshi"] = "qarshi tumani"
        else:
            qashqadaryo["❌Qarshi"] = "qarshi tumani"
        if "yakkabog tumani" in list:
            qashqadaryo["✅Yakkabogʻ"] = "yakkabog tumani"
        else:
            qashqadaryo["❌Yakkabogʻ"] = "yakkabog tumani"
        if "guzor tumani" in list:
            qashqadaryo["✅Gʻuzor"] = "guzor tumani"
        else:
            qashqadaryo["❌Gʻuzor"] = "guzor tumani"
        if "shahrisabz tumani" in list:
            qashqadaryo["✅Shahrisabz"] = "shahrisabz tumani"
        else:
            qashqadaryo["❌Shahrisabz"] = "shahrisabz tumani"
        if "shahrisabz shahar" in list:
            qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
        else:
            qashqadaryo["❌Shahrisabz shahar"] = "shahrisabz shahar"
        if "chiroqchi tumani" in list:
            qashqadaryo["✅Chiroqchi"] = "chiroqchi tumani"
        else:
            qashqadaryo["❌Chiroqchi"] = "chiroqchi tumani"

        shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in qashqadaryo.items():
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Hurmatli haydovchi siz Qashqadaryoning barcha tumanlaridan mijozlarni qabul qilasiz.\n"
                                  "Sziga keraksiz hududlardan chiqib keting.\n\n"
                                  "❌ - chiqqan holat\n\n✅- kirgan holat ", reply_markup=shaxsiy_qashqadaryo)

        await QashqadaryoStatesGroup.qashqadaryo.set()
        await call.message.delete()

@dp.callback_query_handler(state=QashqadaryoStatesGroup.qashqadaryo)
async def qashqadaryo_state(call:CallbackQuery,state:FSMContext):
    if call.data == "hammasiniradetish":
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="dehqonobod tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="kasbi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="kitob tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="koson tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="kokdala tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="mirishkor tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="muborak tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="nishon tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="qamashi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="qarshi shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="qarshi tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="yakkabog tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="guzor tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz tumani", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz shahar", telegram_id=call.from_user.id)
        await db.delete_driver_info(viloyat="Qashqadaryo", tuman="chiroqchi tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qashqadaryo = {}
        if "qarshi shahar" in list:
            qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
        else:
            qashqadaryo["❌Qarshi shahar"] = "qarshi shahar"
        if "dehqonobod tumani" in list:
            qashqadaryo["✅Dehqonobod"] = "dehqonobod tumani"
        else:
            qashqadaryo["❌Dehqonobod"] = "dehqonobod tumani"
        if "kasbi tumani" in list:
            qashqadaryo["✅Kasbi"] = "kasbi tumani"
        else:
            qashqadaryo["❌Kasbi"] = "kasbi tumani"
        if "kitob tumani" in list:
            qashqadaryo["✅Kitob"] = "kitob tumani"
        else:
            qashqadaryo["❌Kitob"] = "kitob tumani"
        if "koson tumani" in list:
            qashqadaryo["✅Koson"] = 'koson tumani'
        else:
            qashqadaryo["❌Koson"] = 'koson tumani'
        if "kokdala tumani" in list:
            qashqadaryo["✅Koʻkdala"] = 'kokdala tumani'
        else:
            qashqadaryo["❌Koʻkdala"] = 'kokdala tumani'
        if "mirishkor tumani" in list:
            qashqadaryo["✅Mirishkor"] = "mirishkor tumani"
        else:
            qashqadaryo["❌Mirishkor"] = 'mirishkor tumani'
        if "muborak tumani" in list:
            qashqadaryo["✅Muborak"] = "muborak tumani"
        else:
            qashqadaryo["❌Muborak"] = 'muborak tumani'
        if "nishon tumani" in list:
            qashqadaryo["✅Nishon"] = "nishon tumani"
        else:
            qashqadaryo["❌Nishon"] = "nishon tumani"
        if "qamashi tumani" in list:
            qashqadaryo["✅Qamashi"] = "qamashi tumani"
        else:
            qashqadaryo["❌Qamashi"] = 'qamashi tumani'
        if "qarshi tumani" in list:
            qashqadaryo["✅Qarshi"] = "qarshi tumani"
        else:
            qashqadaryo["❌Qarshi"] = "qarshi tumani"
        if "yakkabog tumani" in list:
            qashqadaryo["✅Yakkabogʻ"] = "yakkabog tumani"
        else:
            qashqadaryo["❌Yakkabogʻ"] = "yakkabog tumani"
        if "guzor tumani" in list:
            qashqadaryo["✅Gʻuzor"] = "guzor tumani"
        else:
            qashqadaryo["❌Gʻuzor"] = "guzor tumani"
        if "shahrisabz tumani" in list:
            qashqadaryo["✅Shahrisabz"] = "shahrisabz tumani"
        else:
            qashqadaryo["❌Shahrisabz"] = "shahrisabz tumani"
        if "shahrisabz shahar" in list:
            qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
        else:
            qashqadaryo["❌Shahrisabz shahar"] = "shahrisabz shahar"
        if "chiroqchi tumani" in list:
            qashqadaryo["✅Chiroqchi"] = "chiroqchi tumani"
        else:
            qashqadaryo["❌Chiroqchi"] = "chiroqchi tumani"

        shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in qashqadaryo.items():
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Hammasini belgilash", callback_data="hammasinibelgilash"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qashqadaryo)

    if call.data == "hammasinibelgilash":
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="dehqonobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kasbi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kitob tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="koson tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kokdala tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="mirishkor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="muborak tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="nishon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qamashi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="yakkabog tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="guzor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="chiroqchi tumani", telegram_id=call.from_user.id)
        jamii = await db.select_all_driver_info()
        list = []
        for i in jamii:
            if i[3] == call.from_user.id:
                list.append(i[2])
        qashqadaryo = {}
        if "qarshi shahar" in list:
            qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
        else:
            qashqadaryo["❌Qarshi shahar"] = "qarshi shahar"
        if "dehqonobod tumani" in list:
            qashqadaryo["✅Dehqonobod"] = "dehqonobod tumani"
        else:
            qashqadaryo["❌Dehqonobod"] = "dehqonobod tumani"
        if "kasbi tumani" in list:
            qashqadaryo["✅Kasbi"] = "kasbi tumani"
        else:
            qashqadaryo["❌Kasbi"] = "kasbi tumani"
        if "kitob tumani" in list:
            qashqadaryo["✅Kitob"] = "kitob tumani"
        else:
            qashqadaryo["❌Kitob"] = "kitob tumani"
        if "koson tumani" in list:
            qashqadaryo["✅Koson"] = 'koson tumani'
        else:
            qashqadaryo["❌Koson"] = 'koson tumani'
        if "kokdala tumani" in list:
            qashqadaryo["✅Koʻkdala"] = 'kokdala tumani'
        else:
            qashqadaryo["❌Koʻkdala"] = 'kokdala tumani'
        if "mirishkor tumani" in list:
            qashqadaryo["✅Mirishkor"] = "mirishkor tumani"
        else:
            qashqadaryo["❌Mirishkor"] = 'mirishkor tumani'
        if "muborak tumani" in list:
            qashqadaryo["✅Muborak"] = "muborak tumani"
        else:
            qashqadaryo["❌Muborak"] = 'muborak tumani'
        if "nishon tumani" in list:
            qashqadaryo["✅Nishon"] = "nishon tumani"
        else:
            qashqadaryo["❌Nishon"] = "nishon tumani"
        if "qamashi tumani" in list:
            qashqadaryo["✅Qamashi"] = "qamashi tumani"
        else:
            qashqadaryo["❌Qamashi"] = 'qamashi tumani'
        if "qarshi tumani" in list:
            qashqadaryo["✅Qarshi"] = "qarshi tumani"
        else:
            qashqadaryo["❌Qarshi"] = "qarshi tumani"
        if "yakkabog tumani" in list:
            qashqadaryo["✅Yakkabogʻ"] = "yakkabog tumani"
        else:
            qashqadaryo["❌Yakkabogʻ"] = "yakkabog tumani"
        if "guzor tumani" in list:
            qashqadaryo["✅Gʻuzor"] = "guzor tumani"
        else:
            qashqadaryo["❌Gʻuzor"] = "guzor tumani"
        if "shahrisabz tumani" in list:
            qashqadaryo["✅Shahrisabz"] = "shahrisabz tumani"
        else:
            qashqadaryo["❌Shahrisabz"] = "shahrisabz tumani"
        if "shahrisabz shahar" in list:
            qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
        else:
            qashqadaryo["❌Shahrisabz shahar"] = "shahrisabz shahar"
        if "chiroqchi tumani" in list:
            qashqadaryo["✅Chiroqchi"] = "chiroqchi tumani"
        else:
            qashqadaryo["❌Chiroqchi"] = "chiroqchi tumani"

        shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
        for key, value in qashqadaryo.items():
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Hammasini rad etish", callback_data="hammasiniradetish"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.edit_reply_markup(shaxsiy_qashqadaryo)


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
    qashqadaryo = {}
    if "qarshi shahar" in list:
        qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
    else:
        qashqadaryo["❌Qarshi shahar"] = "qarshi shahar"
    if "dehqonobod tumani" in list:
        qashqadaryo["✅Dehqonobod"] = "dehqonobod tumani"
    else:
        qashqadaryo["❌Dehqonobod"] = "dehqonobod tumani"
    if "kasbi tumani" in list:
        qashqadaryo["✅Kasbi"] = "kasbi tumani"
    else:
        qashqadaryo["❌Kasbi"] = "kasbi tumani"
    if "kitob tumani" in list:
        qashqadaryo["✅Kitob"] = "kitob tumani"
    else:
        qashqadaryo["❌Kitob"] = "kitob tumani"
    if "koson tumani" in list:
        qashqadaryo["✅Koson"] = 'koson tumani'
    else:
        qashqadaryo["❌Koson"] = 'koson tumani'
    if "kokdala tumani" in list:
        qashqadaryo["✅Koʻkdala"] = 'kokdala tumani'
    else:
        qashqadaryo["❌Koʻkdala"] = 'kokdala tumani'
    if "mirishkor tumani" in list:
        qashqadaryo["✅Mirishkor"] = "mirishkor tumani"
    else:
        qashqadaryo["❌Mirishkor"] = 'mirishkor tumani'
    if "muborak tumani" in list:
        qashqadaryo["✅Muborak"] = "muborak tumani"
    else:
        qashqadaryo["❌Muborak"] = 'muborak tumani'
    if "nishon tumani" in list:
        qashqadaryo["✅Nishon"] = "nishon tumani"
    else:
        qashqadaryo["❌Nishon"] = "nishon tumani"
    if "qamashi tumani" in list:
        qashqadaryo["✅Qamashi"] = "qamashi tumani"
    else:
        qashqadaryo["❌Qamashi"] = 'qamashi tumani'
    if "qarshi tumani" in list:
        qashqadaryo["✅Qarshi"] = "qarshi tumani"
    else:
        qashqadaryo["❌Qarshi"] = "qarshi tumani"
    if "yakkabog tumani" in list:
        qashqadaryo["✅Yakkabogʻ"] = "yakkabog tumani"
    else:
        qashqadaryo["❌Yakkabogʻ"] = "yakkabog tumani"
    if "guzor tumani" in list:
        qashqadaryo["✅Gʻuzor"] = "guzor tumani"
    else:
        qashqadaryo["❌Gʻuzor"] = "guzor tumani"
    if "shahrisabz tumani" in list:
        qashqadaryo["✅Shahrisabz"] = "shahrisabz tumani"
    else:
        qashqadaryo["❌Shahrisabz"] = "shahrisabz tumani"
    if "shahrisabz shahar" in list:
        qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
    else:
        qashqadaryo["❌Shahrisabz shahar"] = "shahrisabz shahar"
    if "chiroqchi tumani" in list:
        qashqadaryo["✅Chiroqchi"] = "chiroqchi tumani"
    else:
        qashqadaryo["❌Chiroqchi"] = "chiroqchi tumani"

    shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
    for key, value in qashqadaryo.items():
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    for key, value in qashqadaryo.items():
      if call.data == value:
        await call.message.edit_reply_markup(shaxsiy_qashqadaryo)
        await QashqadaryoStatesGroup.qashqadaryo.set()