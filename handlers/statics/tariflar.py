import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp,db

first = []
second = []
third = []
fourth = []
fifth = []


@dp.message_handler(commands=['tarif_sozlamalari'])
async def tarif_conf(message:Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif",callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif",callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif",callback_data="conffifthsetting"))
    await message.answer("Qaysi tarifni o'zgartirmoqchisiz ?",reply_markup=markup)
    await message.delete()

class ConfFirstGroup(StatesGroup):
    pay = State()
    day = State()
@dp.callback_query_handler(text="confonesetting")
async def conf_one(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfFirstGroup.pay.set()
@dp.message_handler(state=ConfFirstGroup.pay)
async def first_conf_pay(message:Message,state:FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text),tarif_name="first")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfFirstGroup.day.set()
    else:
        await message.answer("Iltimos son kiriting !!!")
@dp.message_handler(state=ConfFirstGroup.day)
async def first_conf_day(message:Message,state:FSMContext):
    if message.text.isdigit():
        await db.update_tarif_day(tarif_name="first",tarif_kuni=int(message.text))
        await message.answer("Tarif o'zgartirildi")
        await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")

    tarif = await db.select_tarif(tarif_name="first")
    print(tarif)
class ConfSecondGroup(StatesGroup):
    pay = State()
    day = State()
@dp.callback_query_handler(text="confsecondsetting")
async def conf_one(call:CallbackQuery):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfSecondGroup.pay.set()
@dp.message_handler(state=ConfSecondGroup.pay)
async def first_conf_pay(message:Message,state:FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text),tarif_name="second")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfFirstGroup.day.set()
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


class ConfThirdGroup(StatesGroup):
    pay = State()
    day = State()

@dp.callback_query_handler(text="confthirdsetting")
async def conf_one(call:CallbackQuery):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfThirdGroup.pay.set()


@dp.message_handler(state=ConfThirdGroup.pay)
async def first_conf_pay(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text), tarif_name="third")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfFirstGroup.day.set()
    else:
        await message.answer("Iltimos son kiriting !!!")


@dp.message_handler(state=ConfThirdGroup.day)
async def first_conf_day(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_day(tarif_name="third", tarif_kuni=int(message.text))
        await message.answer("Tarif o'zgartirildi")
        await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")



class ConfFourthGroup(StatesGroup):
    pay = State()
    day = State()

@dp.callback_query_handler(text="conffourthsetting")
async def conf_one(call:CallbackQuery):
    await call.message.answer("Yangi oylik to'lov miqdorini kiriting :")
    await ConfFourthGroup.pay.set()


@dp.message_handler(state=ConfFourthGroup.pay)
async def first_conf_pay(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_pay(tarif_narxi=int(message.text), tarif_name="fourth")
        await message.answer("Kuniga qancha mijoz qabul qilsin  ? ")
        await ConfFourthGroup.day.set()
    else:
        await message.answer("Iltimos son kiriting !!!")


@dp.message_handler(state=ConfFourthGroup.day)
async def first_conf_day(message: Message, state: FSMContext):
    if message.text.isdigit():
        await db.update_tarif_day(tarif_name="fourth", tarif_kuni=int(message.text))
        await message.answer("Tarif o'zgartirildi")
        await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")



class ConfFifthGroup(StatesGroup):
    pay = State()
    day = State()

@dp.callback_query_handler(text="conffifthsetting")
async def conf_one(call:CallbackQuery):
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



class FirstStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(commands=['first_type'])
async def tarif_1_ga_otkazish(message: Message, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yakunlash",callback_data="xa"))
    await message.answer("1 - ta'rif. Kimnidur bu tarifga o'tkazmoqchi bo'lsangiz Foydalanuvchi ID raqamini kiriting , aks holda yakunlashni bosing",reply_markup=markup)
    await FirstStatesGroup.id.set()
    await message.delete()
@dp.callback_query_handler(text="xa",state=FirstStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Salom Admin ",reply_markup=umumiy_menu)
    await state.finish()
@dp.message_handler(state=FirstStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            await state.update_data({"id": user[3]})
            if user[3] in second:
                for i in second:
                    if i==user[3]:
                        second.remove(i)
            if user[3] in third:
                for i in third:
                    if i==user[3]:
                        third.remove(i)
            first.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 1- tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class SecondStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(commands=['second_type'])
async def tarif_2_ga_otkazish(message: Message, state: FSMContext):
    await message.answer("2 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yakunlash", callback_data="xa"))
    await message.answer(
        "2 - ta'rif yoqildi . Kimnidur bu tarifga o'tkazmoqchi bo'lsangiz Foydalanuvchi ID raqamini kiriting , aks holda yakunlashni bosing",
        reply_markup=markup)
    await message.delete()
    await SecondStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=SecondStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Salom Admin ",reply_markup=umumiy_menu)
    await state.finish()
@dp.message_handler(state=SecondStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            await state.update_data({"id": user[3]})
            if user[3] in first:
                for i in first:
                    if i==user[3]:
                        first.remove(i)
            if user[3] in third:
                for i in third:
                    if i==user[3]:
                        third.remove(i)
            second.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 2 - tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class ThirdStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(commands=['third_type'])
async def tarif_3_ga_otkazish(message: Message, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yakunlash", callback_data="xa"))
    await message.answer(
        "3 - ta'rif yoqildi . Kimnidur bu tarifga o'tkazmoqchi bo'lsangiz Foydalanuvchi ID raqamini kiriting , aks holda yakunlashni bosing",
        reply_markup=markup)
    await message.delete()
    await ThirdStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=ThirdStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Salom Admin ",reply_markup=umumiy_menu)
    await state.finish()
@dp.message_handler(state=ThirdStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            await state.update_data({"id": user[3]})
            if user[3] in second:
                for i in second:
                    if i==user[3]:
                        second.remove(i)
            if user[3] in first:
                for i in first:
                    if i==user[3]:
                        first.remove(i)
            third.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 3 - tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class FouthStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(commands=['fourth_type'])
async def tarif_4_ga_otkazish(message: Message, state: FSMContext):
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        fourth.append(user[3])
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yakunlash", callback_data="xa"))
    await message.answer(
        "4 - ta'rif yoqildi . Kimnidur bu tarifga o'tkazmoqchi bo'lsangiz Foydalanuvchi ID raqamini kiriting , aks holda yakunlashni bosing",
        reply_markup=markup)
    await message.delete()
    await FouthStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=FouthStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Salom Admin ",reply_markup=umumiy_menu)
    await state.finish()
@dp.message_handler(state=FouthStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            await state.update_data({"id": user[3]})
            if user[3] in second:
                for i in second:
                    if i==user[3]:
                        second.remove(i)
            if user[3] in third:
                for i in third:
                    if i==user[3]:
                        third.remove(i)
            if user[3] in first:
                for i in first:
                    if i==user[3]:
                        first.remove(i)
            if user[3] in fifth:
                for i in fifth:
                    if i==user[3]:
                        fifth.remove(i)
            fourth.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 4 - tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class FifthStatesGroup(StatesGroup):
    id = State()
@dp.message_handler(commands=['fifth_type'])
async def tarif_5_ga_otkazish(message: Message, state: FSMContext):
    for i in fourth:
        fourth.remove(i)
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        fifth.append(user[3])
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Yakunlash", callback_data="xa"))
    await message.answer(
        "5 - ta'rif yoqildi . Kimnidur bu tarifga o'tkazmoqchi bo'lsangiz Foydalanuvchi ID raqamini kiriting , aks holda yakunlashni bosing",
        reply_markup=markup)
    await message.delete()
    await FifthStatesGroup.id.set()

@dp.callback_query_handler(text="xa",state=FifthStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Salom Admin ",reply_markup=umumiy_menu)
    await state.finish()
@dp.message_handler(state=FifthStatesGroup.id)
async def tarif_1_id(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            await state.update_data({"id": user[3]})
            if user[3] in second:
                for i in second:
                    if i==user[3]:
                        second.remove(i)
            if user[3] in third:
                for i in third:
                    if i==user[3]:
                        third.remove(i)
            if user[3] in fourth:
                for i in fourth:
                    if i==user[3]:
                        fourth.remove(i)
            if user[3] in first:
                for i in first:
                    if i==user[3]:
                        first.remove(i)
            fifth.append(user[3])
            await message.answer(f"{id} - raqamli foydalanuvchi 5 - tarifga o'tkazildi .")
            await state.finish()
            await asyncio.sleep(30*24*60*60)
            second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")


@dp.message_handler(commands="hammaga_pullik_qilish")
async def hammaga_pullik(message:Message):
    for i in fourth:
        fourth.remove(i)
    for i in fifth:
        fifth.remove(i)
    await message.answer("Hamma uchun pullik bo'ldi !!!")