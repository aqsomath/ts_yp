import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.statics.royxatlar import admin_ids, balans_toldirish, balans_ayrish, user_of_banned, ban_qilish, \
    bandan_chiqarish
from loader import dp, db, bot


class BanStatesGroup(StatesGroup):
    id = State()
    day = State()
class UnBanStatesGroup(StatesGroup):
    id = State()
class BalansToldirish(StatesGroup):
    id = State()
    money = State()

class BalansAyirish(StatesGroup):
    id = State()
    money = State()


@dp.message_handler(commands=["admin"])
async def admin_panel_commands(message:Message,state:FSMContext):
    one = await db.select_tarif(tarif_name='first')
    msg_1 = f"Kuniga {one[3]} ta qabul qilish, oyiga - > {one[2]}"
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"Kuniga {two[3]} ta qabul qilish, oyiga - > {two[2]}"
    three = await db.select_tarif(tarif_name='third')
    msg_3 = f"Kuniga {three[3]} ta qabul qilish, oyiga - > {three[2]}"
    four = await db.select_tarif(tarif_name='fourth')
    msg_4 = f"Kuniga {four[3]} ta qabul qilish, oyiga - > {four[2]} "
    five = await db.select_tarif(tarif_name='fifth')
    msg_5 = f"/start bosilishiga {five[3]} kun bepul qilish "
    admin = await db.select_admin(telegram_id = message.from_user.id)
    if admin:
        list_of_commands = (f"/start --> Botni ishga tushirish\n"
                            f"/help --> Yordam\n"
                            f"/statics --> Statistika\n"
                            f"/ban --> Foydalanuvchini blok qilish\n"
                            f"/unban --> Foydalanuvchini blokdan chiqarish\n"
                            f"/first_type --> {msg_1}\n"
                            f"/second_type --> {msg_2}\n"
                            f"/third_type --> {msg_3}\n"
                            f"/hammaga_bepul_qilish --> {msg_4}\n"
                            f"/fifth_type --> {msg_5}\n"
                            f"/tarif_sozlamalari --> Tarif summasi va limitini o'zgartirish\n"
                            f"/filter --> Sozlamalar bo'limi\n"
                            f"/balans_toldirish --> Haydovchi balansini to'ldirish\n"
                            f"/balans_ayirish --> Haydovchi balansini ayirish\n"
                            f"/hammaga_pullik_qilish -- > Hamma uchun pullik qilish")
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Statistika",callback_data="umumiystatistika"))
        markup.insert(InlineKeyboardButton(text="Foydalanuvchilar",callback_data="foydalanuvchilarniqidirish"))
        markup.insert(InlineKeyboardButton(text="Adminlar",callback_data="adminlarroyxati"))
        markup.insert(InlineKeyboardButton(text="Buyurtmalar",callback_data="baribuyurtmalar"))
        markup.insert(InlineKeyboardButton(text="Ban qilish",callback_data="banqilish"))
        markup.insert(InlineKeyboardButton(text="Bandan chiqarish",callback_data="bandanchiqarish"))
        markup.insert(InlineKeyboardButton(text="Tariflar",callback_data='barchatariflar'))
        markup.insert(InlineKeyboardButton(text="Balans to'ldirish",callback_data="Balanstoldirish"))
        markup.insert(InlineKeyboardButton(text="Balans ayirish",callback_data="Balansayrish"))
        button = InlineKeyboardButton(text="Foydalanuvchilarga xabar jo'natish",callback_data="foydalanuvchilargaxabarjonatish")
        markup.add(button)
        await message.answer(reply_markup=markup,text="Admin bo'lim")

@dp.callback_query_handler(text="Balanstoldirish")
async def pay_balans(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in balans_toldirish:
        await call.message.answer("Foydalanuvchining ID sini kiriting :")
        await BalansToldirish.id.set()
    else:
        await call.message.answer("Kechirasiz sizga balans to'ldirish uchun ruxsat yo'q")
        await state.finish()
@dp.message_handler(state=BalansToldirish , commands=['cancel'])
@dp.message_handler(state=BalansAyirish , commands=['cancel'])
@dp.message_handler(state=BanStatesGroup , commands=['cancel'])
@dp.message_handler(state=UnBanStatesGroup , commands=['cancel'])
async def cancel_com(message:Message,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Statistika", callback_data="umumiystatistika"))
    markup.insert(InlineKeyboardButton(text="Foydalanuvchilar", callback_data="foydalanuvchilarniqidirish"))
    markup.insert(InlineKeyboardButton(text="Adminlar", callback_data="adminlarroyxati"))
    markup.insert(InlineKeyboardButton(text="Buyurtmalar", callback_data="baribuyurtmalar"))
    markup.insert(InlineKeyboardButton(text="Ban qilish", callback_data="banqilish"))
    markup.insert(InlineKeyboardButton(text="Bandan chiqarish", callback_data="bandanchiqarish"))
    markup.insert(InlineKeyboardButton(text="Tariflar", callback_data='barchatariflar'))
    markup.insert(InlineKeyboardButton(text="Balans to'ldirish", callback_data="Balanstoldirish"))
    markup.insert(InlineKeyboardButton(text="Balans ayirish", callback_data="Balansayrish"))
    await message.answer(reply_markup=markup, text="Admin bo'lim")
    await message.delete()
    await state.finish()
@dp.message_handler(state=BalansToldirish.id)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        id = int(message.text)
        await state.update_data({"id":id})
        await message.answer("Qanchaga to'ldirasiz. Son bilan to'liq kirgizing.")
        await message.delete()
        await BalansToldirish.money.set()
@dp.message_handler(state=BalansToldirish.money)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        id=data.get("id")
        d = await db.select_user(telegram_id=id)
        if d is not None:
            await db.update_balans(telegram_id=d[3],balans=d[7]+int(message.text))
            d = await db.select_user(telegram_id=id)
            await message.answer(f"Balans to'ldirildi\nHaydovchi\nusername:{d[1]}\nID:{id}\nBalans:{d[7]} ")
            await bot.send_message(chat_id=d[3], text=f"Balansingiz {message.text} ga to'ldirildi")
            await message.delete()
            await state.finish()
        else:
            await message.answer("Kechirasiz bunday foydalanuvchi mavjud emas !")
            await state.finish()


@dp.callback_query_handler(text="Balansayrish")
async def pay_balans(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in balans_ayrish:
        await call.message.answer("Foydalanuvchining ID sini kiriting :")
        await BalansAyirish.id.set()
    else:
        await call.message.answer("Kechirasiz sizga balans kamaytirish uchun ruxsat yo'q")

@dp.message_handler(state=BalansAyirish.id)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        id = int(message.text)
        await state.update_data({"id":id})
        await message.answer("Qanchaga kamaytirilisin. Son bilan to'liq kirgizing.")
        await message.delete()
        await BalansAyirish.money.set()
@dp.message_handler(state=BalansAyirish.money)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        id=data.get("id")
        d = await db.select_user(telegram_id=id)
        if d is not None:
            await db.update_balans(telegram_id=d[3],balans=d[7]-int(message.text))
            d = await db.select_user(telegram_id=id)
            await message.answer(f"Balans ayrildi\nHaydovchi\nusername: {d[1]}\nID:{id}\nBalans:{d[7]} ")
            await bot.send_message(chat_id=d[3], text=f"Balansingiz {message.text} ga kamaytirildi")
            await message.delete()
            await state.finish()
        else:
            await message.answer("Kechirasiz bunday foydalanuvchi mavjud emas !")
            await state.finish()

@dp.callback_query_handler(text="banqilish")
async def ban_user(call: types.CallbackQuery,state:FSMContext):
    if call.from_user.id in ban_qilish:
        await call.message.answer("Foydalanuvchi ID sini kiriting :")
        await call.message.delete()
        await BanStatesGroup.id.set()
    else:
        await call.message.answer("Kechirasiz sizga ban qilish uchun ruxsat yo'q")
        await state.finish()
@dp.message_handler(state=BanStatesGroup.id)
async def id_get(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        user = await db.select_user(telegram_id=id)
        if user is not None:
            await state.update_data({"id":user[3]})
            user_of_banned.append(user[3])
            await message.answer("Necha kunga ban bo'lsin")
            await BanStatesGroup.day.set()
        else:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")
            await state.finish()
@dp.message_handler(state=BanStatesGroup.day)
async def how_many_day(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    data = await state.get_data()
    id = data.get("id")
    try:
        if message.text.isdigit():
            day = int(message.text)
            await message.answer(f"Foydalanuvchi {day} kun ichida bloklangan holatda bo'ladi")
            await message.delete()
            await state.finish()
            await asyncio.sleep(60*60*24*day)
            user_of_banned.remove(id)
    except TypeError:
        await message.answer("Bu ID da foydalanuvchi mavjud emas .")



@dp.callback_query_handler(text='bandanchiqarish')
async def unban_user(call: types.CallbackQuery,state:FSMContext):
    if call.from_user.id in bandan_chiqarish:
        await call.message.answer("Foydalanuvchi ID sini kiriting :")
        await call.message.delete()
        await UnBanStatesGroup.id.set()
    else:
        await call.message.answer("Kechirasiz sizga foydalanuvchilarni bandan chiqarish uchun ruxsat yo'q")
        await state.finish()
@dp.message_handler(state=UnBanStatesGroup.id)
async def id_get_ban_user(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(telegram_id=id)
            if user[3] in user_of_banned:
                user_of_banned.remove(user[3])
                await message.answer("Foydalanuvchi blokdan chiqarildi")
                await message.delete()
                await state.finish()
            else:
                await message.answer("Bu foydalanuvchi bloklanmagan !")
                await message.delete()
                await state.finish()

        except TypeError :
            await message.answer("Bu ID da foydalanuvchi mavjud emas .")



