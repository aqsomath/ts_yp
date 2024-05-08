import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.edit_district.sozlamalar import haydovchilar_royxati, SozlamalarStates
from handlers.users.yolovchi_tuman.yolovchimisiz import yolovchilar_royxati
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp,db

first = []
second = []
third = []
fourth = []
fifth = []


@dp.callback_query_handler(text='barchatariflar')
async def tarif_conf(call:CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="confonesetting"))
    markup.insert(InlineKeyboardButton(text="2 - tarif",callback_data="confsecondsetting"))
    markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="confthirdsetting"))
    markup.insert(InlineKeyboardButton(text="4 - tarif",callback_data="conffourthsetting"))
    markup.insert(InlineKeyboardButton(text="5 - tarif",callback_data="conffifthsetting"))
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="skldjuiuiuiuiererere"))
    await call.message.answer("Ta'riflar bo'limi",reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(text="skldjuiuiuiuiererere")
async def menuu(call:CallbackQuery):
    yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
    if yolovchi is not None:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    else:
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
class ConfFirstGroup(StatesGroup):
    pay = State()
    day = State()
@dp.callback_query_handler(text="confonesetting")
async def conf_one(call:CallbackQuery,state:FSMContext):
    one = await db.select_tarif(tarif_name='first')
    msg_1 = f"1-ta'rif\nA'zolar {len(first)}\nKuniga {one[3]} ta qabul qilish, oyiga - > {one[2]}"
    markup=InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Tarifga odam qo'shish",callback_data="birinchitarigaodamqoshish"))
    markup.insert(InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish",callback_data="birinchitarifsozlamalari"))
    await call.message.answer(msg_1,reply_markup=markup)
@dp.callback_query_handler(text="birinchitarifsozlamalari")
async def conf_one_setting(call:CallbackQuery,state:FSMContext):
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
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"Kuniga {two[3]} ta qabul qilish, oyiga - > {two[2]}"
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Tarifga odam qo'shish", callback_data="ikkinchitarigaodamqoshish"))
    markup.insert(InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="ikkinchitarifsozlamalari"))
    await call.message.answer(msg_2, reply_markup=markup)
@dp.callback_query_handler(text="ikkinchitarigaodamqoshish")
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
    three = await db.select_tarif(tarif_name='third')
    msg_3 = f"Kuniga {three[3]} ta qabul qilish, oyiga - > {three[2]}"
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Tarifga odam qo'shish", callback_data="uchinchitarigaodamqoshish"))
    markup.insert(InlineKeyboardButton(text="Tarif sozlamalarini o'zgartirish", callback_data="uchinchitarifsozlamalari"))
    await call.message.answer(msg_3, reply_markup=markup)
@dp.callback_query_handler(text="uchinchitarifsozlamalari")
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
    if len(fourth)==0:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Yoqish",callback_data="Hammagauchunbepulqilish"))
        await call.message.answer("Hamma uchun bepul tarif.Bu tarif hozirda o'chiq.\nYoqishni istaysizmi ?",reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="xa"))
        await call.message.answer(f"Barcha uchun bepul tarif \nA'zolar soni -{len(fourth)} ",
                                  reply_markup=markup)

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
    if len(fifth)==0:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"/start bosilishiga {five[3]} kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Yoqish", callback_data="Beshinchitarifniyoqish"))
        await call.message.answer(f"Beshinchi ta'rif .\n{msg_5}\n Bu tarif hozircha o'chiq. Yoqishni istaysizmi ? ",reply_markup=markup)
    else:
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"/start bosilishiga {five[3]} kun bepul"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="xa"))
        await call.message.answer(f"{msg_5} tarif \nA'zolar soni -{len(fifth)} ",
                                  reply_markup=markup)

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
@dp.callback_query_handler(text="birinchitarigaodamqoshish")
async def tarif_1_ga_otkazish(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="xa"))
    await call.message.answer("Foydalanuvchi ID sini kiriting",reply_markup=markup)
    await FirstStatesGroup.id.set()
    await call.message.delete()
@dp.callback_query_handler(text="xa",state=FirstStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
            if user[3] in first:
                haydovchi = await db.select_haydovchi(telegram_id=user[3])
                haydovchi_balansi = haydovchi[3]
                tarif = await db.select_tarif(tarif_name='first')
                if haydovchi_balansi>=tarif[3]:
                    await db.update_balans(balans=haydovchi_balansi-tarif[3],telegram_id=user[3])
                first.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class SecondStatesGroup(StatesGroup):
    id = State()
@dp.callback_query_handler(text="ikkinchitarigaodamqoshish")
async def tarif_1_ga_otkazish(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="xa"))
    await call.message.answer("Foydalanuvchi ID sini kiriting",reply_markup=markup)
    await call.message.delete()
    await SecondStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=SecondStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
            if user[3] in second:
                second.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class ThirdStatesGroup(StatesGroup):
    id = State()
@dp.callback_query_handler(text="uchinchitarigaodamqoshish")
async def tarif_1_ga_otkazish(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="xa"))
    await call.message.answer("Foydalanuvchi ID sini kiriting",reply_markup=markup)
    await call.message.delete()
    await ThirdStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=ThirdStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
    await state.finish()
@dp.callback_query_handler(text="xa")
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
            if user[3] in third:
                third.remove(user[3])
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")

class FouthStatesGroup(StatesGroup):
    id = State()
@dp.callback_query_handler(text="Hammagauchunbepulqilish")
async def tarif_4_ga_otkazish(call: CallbackQuery, state: FSMContext):
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        fourth.append(user[3])
    for i in first:
        first.remove(i)
    for j in second:
        second.remove(j)
    for k in third:
        third.remove(k)
    for l in fifth:
        fifth.remove(l)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu ", callback_data="xa"))
    await call.message.answer(
        "4 - ta'rif - > Barcha uchun bepul bo'ldi",
        reply_markup=markup)
    await call.message.delete()
    await FouthStatesGroup.id.set()
@dp.callback_query_handler(text="xa",state=FouthStatesGroup.id)
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
    await state.finish()


class FifthStatesGroup(StatesGroup):
    id = State()
@dp.callback_query_handler(text="Beshinchitarifniyoqish")
async def tarif_5_ga_otkazish(call: CallbackQuery, state: FSMContext):
    for i in fourth:
        fourth.remove(i)
    users = await db.select_all_users()
    for user in users:
        print(user[3])
        fifth.append(user[3])
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="xa"))
    five = await db.select_tarif(tarif_name='fifth')
    msg_5 = f"/start bosilishiga {five[3]} kun bepul holatida ishlaydi "
    await call.message.answer(
        f"5 - ta'rif yoqildi .{msg_5}",
        reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(text="xa")
async def yakun(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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
    await state.finish()



@dp.message_handler(commands="hammaga_pullik_qilish")
async def hammaga_pullik(message:Message):
    for i in fourth:
        fourth.remove(i)
    for i in fifth:
        fifth.remove(i)
    await message.answer("Hamma uchun pullik bo'ldi !!!")


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
    if call.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.from_user.id in haydovchilar_royxati:
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


