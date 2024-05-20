import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import haydovchilar_royxati, SozlamalarStates
from handlers.users.yolovchi_tuman.yolovchimisiz import yolovchilar_royxati
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu, kirish
from loader import dp,db

first = []
second = []
third = []
fourth = []
fifth = []




























@dp.callback_query_handler(state=SozlamalarStates.tarifni_almashtirish)
async def change_tarif(call: CallbackQuery, state: FSMContext):
    if call.data == 'changebirinchitarif':
        tarif_first = await db.select_tarif(tarif_name="first")
        driver = await db.select_haydovchi(telegram_id=call.from_user.id)
        balans = driver[3]
        if balans >= tarif_first[2]:
            await db.update_balans(balans=balans - tarif_first[3], telegram_id=call.from_user.id)
            if call.from_user.id in fourth:
                fourth.remove(call.from_user.id)
            if call.from_user.id in fifth:
                fifth.remove(call.from_user.id)
            if call.from_user.id in third:
                third.remove(call.from_user.id)
            if call.from_user.id in second:
                second.remove(call.from_user.id)
            first.append(call.from_user.id)
            await call.message.answer("Tarif muvofaqqiyatli o'zgartirildi .")
            await call.message.delete()
            await state.finish()

        else:
            await call.message.answer("Balansda pul yetarli emas !!!\nIltimos hisobingizni to'ldiring.")
            await call.message.delete()
            await state.finish()

    if call.data == "changeikkinchitarif":
        tarif_second = await db.select_tarif(tarif_name="second")
        driver = await db.select_haydovchi(telegram_id=call.from_user.id)

        balans = driver[3]
        if balans >= tarif_second[2]:
            await db.update_balans(balans=balans - tarif_second[3], telegram_id=call.from_user.id)
            if call.from_user.id in fourth:
                fourth.remove(call.from_user.id)
            if call.from_user.id in fifth:
                fifth.remove(call.from_user.id)
            if call.from_user.id in third:
                third.remove(call.from_user.id)
            if call.from_user.id in first:
                first.remove(call.from_user.id)
            second.append(call.from_user.id)
            await call.message.answer("Tarif muvofaqqiyatli o'zgartirildi .")
            await call.message.delete()
            await state.finish()

        else:
            await call.message.answer("Balansda pul yetarli emas !!!\nIltimos hisobingizni to'ldiring.")
            await call.message.delete()
            await state.finish()

    if call.data == "changeuchinchitarif":
        tarif_third = await db.select_tarif(tarif_name="third")
        driver = await db.select_haydovchi(telegram_id=call.from_user.id)

        balans = driver[3]
        if balans >= tarif_third[2]:
            await db.update_balans(balans=balans - tarif_third[3], telegram_id=call.from_user.id)
            if call.from_user.id in fourth:
                fourth.remove(call.from_user.id)
            if call.from_user.id in fifth:
                fifth.remove(call.from_user.id)
            if call.from_user.id in second:
                second.remove(call.from_user.id)
            if call.from_user.id in first:
                first.remove(call.from_user.id)
            third.append(call.from_user.id)
            await call.message.answer("Tarif muvofaqqiyatli o'zgartirildi .")
            await call.message.delete()
            await state.finish()
        else:
            await call.message.answer("Balansda pul yetarli emas !!!\nIltimos hisobingizni to'ldiring.")
            await call.message.delete()
            await state.finish()


@dp.callback_query_handler(text="boshmenu", state=SozlamalarStates.my_info)
async def nazad_and_headmenu(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()

        elif user[6] == True:
            driver = {
                "Haydovchi reys belgilash": 'yolovchikerak',
                "Tayyor yo'lovchi": 'tayyoryolovchi',
                "Yuk kerak": 'yukkerak',
                "Tayyor yuk": "tayyoryuk",
                "Pochta kerak": 'pochtakerak',
                "Tayyor pochta": "tayyorpochta",
                "Sayohatchilar kerak": 'sayohatgayolovchi',
                "Tayyor sayohatchi": "tayyorsayohatchi",
                "Mening buyurtmalarim": "meningbuyurtmalarim",
                "Admin bilan bog'lanish": "adminbilanboglanish",
                "Sozlamalar": "nastroyki",
                "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"
            }
            markup = InlineKeyboardMarkup(row_width=2)
            for key, value in driver.items():
                markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
            await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
            await call.message.delete()
        else:
            await call.message.answer(f"Salom, {call.message.from_user.full_name}!", reply_markup=kirish)
    await state.finish()


@dp.callback_query_handler(text="ortga", state=SozlamalarStates.my_info)
async def nazad_and_headmenu(call: CallbackQuery, state: FSMContext):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ", reply_markup=marrk)
    await SozlamalarStates.kirish.set()
    await call.message.delete()


