
import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.users.tariflar.asosiy import second, third, first
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu, kirish
from loader import db, dp


class ConfSecondGroup(StatesGroup):
    pay = State()
    day = State()
@dp.message_handler(state=ConfSecondGroup,commands=['cancel'])
async def back_tarifs(message:Message,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Hamma uchun bepul", callback_data="hammagabepulqilish"))
    markup.insert(InlineKeyboardButton(text="Hamma uchun pullik", callback_data="hammagapullikqilish"))
    markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif",callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif",callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif",callback_data="conffifthsetting"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="skldjuiuiuiuiererere"))
    await message.answer("Ta'riflar bo'limi",reply_markup=markup)
    await message.delete()
    await state.finish()
@dp.callback_query_handler(text="confsecondsetting")
async def conf_one(call:CallbackQuery):
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"2-ta'rif\nA'zolar {len(second)}\nKuniga {two[3]} ta qabul qilish, oyiga - > {two[2]}"
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="Tarifga odam qo'shish", callback_data="ikkinchitarigaodamqoshish"))
    markup.insert(InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="ikkinchitarifsozlamalari"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
    await call.message.answer(msg_2, reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(text="ikkinchitarifsozlamalari")
async def conf_one(call:CallbackQuery):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfSecondGroup.pay.set()
@dp.message_handler(state=ConfSecondGroup.pay)
async def first_conf_pay(message:Message,state:FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text),tarif_name="second")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfSecondGroup.day.set()
    else:
        await message.answer("Iltimos son kiriting !!!")
@dp.message_handler(state=ConfSecondGroup.day)
async def first_conf_day(message:Message,state:FSMContext):

    if message.text.isdigit():
        await db.update_tarif_day(tarif_name="second",tarif_kuni=int(message.text))
        await message.answer("Tarif o'zgartirildi")
        await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")

class SecondStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(state=SecondStatesGroup,commands=['cancel'])
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
@dp.callback_query_handler(text="ikkinchitarigaodamqoshish")
async def tarif_1_ga_otkazish(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="xa"))
    await call.message.answer("Foydalanuvchi telegram ID sini kiriting",reply_markup=markup)
    await call.message.delete()
    await SecondStatesGroup.id.set()

@dp.callback_query_handler(text="ortga",state=SecondStatesGroup.id)
async def birinchi_tarifg_odam(call:CallbackQuery,state:FSMContext):
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"2-ta'rif\nA'zolar {len(second)}\nKuniga {two[3]} ta qabul qilish, oyiga - > {two[2]}"
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="Tarifga odam qo'shish", callback_data="ikkinchitarigaodamqoshish"))
    markup.insert(
        InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="ikkinchitarifsozlamalari"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="qayt"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="menuga"))
    await call.message.answer(msg_2, reply_markup=markup)
    await call.message.delete()
    await state.finish()
@dp.callback_query_handler(text="xa",state=SecondStatesGroup.id)
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
@dp.message_handler(state=SecondStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(telegram_id=id)
            await state.update_data({"id": user[3]})
            second.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 2 - tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            if user[3] in second:
                second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")
