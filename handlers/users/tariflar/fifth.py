import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.users.tariflar.asosiy import second, third, first, fifth, fourth,hammaga_bepul
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu, kirish
from loader import db, dp



class ConfFifthGroup(StatesGroup):
    pay = State()
    day = State()
@dp.message_handler(state=ConfFifthGroup,commands=['cancel'])
async def back_tarifs(message:Message,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Hamma uchun bepul", callback_data="hammagabepulqilish"))
    markup.insert(InlineKeyboardButton(text="Hamma uchun pullik", callback_data="hammagapullikqilish"))
    markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif",callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif",callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif",callback_data="conffifthsetting"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Adminbolimgaqayt"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="skldjuiuiuiuiererere"))
    await message.answer("Ta'riflar bo'limi",reply_markup=markup)
    await message.delete()
    await state.finish()
@dp.callback_query_handler(text="conffifthsetting")
async def conf_one(call:CallbackQuery):
    if len(fifth) == 0:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"5-tarif\nA'zolar soni - {len(fifth)}\n/start bosilishiga\nKuniga - {five[3]}\n3 -  kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Tarifni yoqish", callback_data="beshinchitarifgaodamqoshish"))
        markup.insert(
            InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="beshinchitarifsozlamalari"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
        await call.message.answer(f"{msg_5}", reply_markup=markup)
        await call.message.delete()

    else:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"5-tarif\nA'zolar soni - {len(fifth)}\n/start bosilishiga :\nKuniga - {five[3]}\n3 -  kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Tarifni o'chirish", callback_data="beshiinchitarifniochirish"))
        markup.insert(
            InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="beshinchitarifsozlamalari"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
        await call.message.answer(f"{msg_5}", reply_markup=markup)
        await call.message.delete()


@dp.callback_query_handler(text="beshinchitarifsozlamalari")
async def conf_one_setting(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfFifthGroup.pay.set()

@dp.message_handler(state=ConfFifthGroup.pay)
async def first_conf_pay(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text), tarif_name="fifth")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfFifthGroup.day.set()
    else:
        await message.answer("Iltimos son kiriting !!!")


@dp.message_handler(state=ConfFifthGroup.day)
async def first_conf_day(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_day(tarif_name="fifth", tarif_kuni=int(message.text))
        await message.answer("Tarif o'zgartirildi")
        await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")


class FifthStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(state=FifthStatesGroup,commands=['cancel'])
async def back_tarifs(message:Message,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Hamma uchun bepul", callback_data="hammagabepulqilish"))
    markup.insert(InlineKeyboardButton(text="Hamma uchun pullik", callback_data="hammagapullikqilish"))
    markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif",callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif",callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif",callback_data="conffifthsetting"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Adminbolimgaqayt"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="skldjuiuiuiuiererere"))
    await message.answer("Ta'riflar bo'limi",reply_markup=markup)
    await message.delete()
    await state.finish()
@dp.callback_query_handler(text="beshinchitarifgaodamqoshish")
async def tarif_5_ga_otkazish(call: CallbackQuery):
    fourth.clear()
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="quququortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="xa"))
    five = await db.select_tarif(tarif_name='fifth')
    msg_5 = f"/start bosilishiga {five[3]} kun bepul holatida ishlaydi "
    await call.message.answer(f"5 - ta'rif yoqildi .{msg_5}", reply_markup=markup)
    await call.message.delete()
    users = await db.select_all_users()
    for user in users:
        fifth.append(user[3])
        five = await db.select_tarif(tarif_name='fifth')
        await asyncio.sleep(five[3] * 24 * 60 * 60)
        for user in users:
            if user[3] in fifth:
                fifth.remove(user[3])


@dp.callback_query_handler(text="beshiinchitarifniochirish")
async def tarif_5_ga_otkazish(call: CallbackQuery, state: FSMContext):
    fifth.clear()
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="quququortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="xa"))
    five = await db.select_tarif(tarif_name='fifth')
    msg_5 = f"5-tarif\nA'zolar soni - {len(fifth)}\n/start bosilishiga\nKuniga - {five[3]}\n3 -  kun bepul"
    await call.message.answer(f"5 - ta'rif o'chirildi .\n{msg_5}",reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(text="quququortga")
async def ortga_qayytish_uchun(call:CallbackQuery):
    if len(fifth)==0:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"5-tarif\nA'zolar soni - {len(fifth)}\n/start bosilishiga\nKuniga - {five[3]}\n3 -  kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Tarifni yoqish", callback_data="beshinchitarifgaodamqoshish"))
        markup.insert(
            InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="beshinchitarifsozlamalari"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
        await call.message.answer(f"{msg_5}", reply_markup=markup)
        await call.message.delete()

    else:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"5-tarif\nA'zolar soni - {len(fifth)}\n/start bosilishiga\nKuniga - {five[3]}\n3 -  kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Tarifni o'chirish", callback_data="beshiinchitarifniochirish"))
        markup.insert(
            InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="beshinchitarifsozlamalari"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
        await call.message.answer(f"{msg_5}", reply_markup=markup)
        await call.message.delete()

@dp.callback_query_handler(text="xa")
async def yakun(call:CallbackQuery,state:FSMContext):
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



