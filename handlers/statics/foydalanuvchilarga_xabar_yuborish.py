import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.statics.royxatlar import admin_ids, balans_toldirish, balans_ayrish, user_of_banned, ban_qilish, \
    bandan_chiqarish
from loader import dp, db, bot


@dp.callback_query_handler(text="foydalanuvchilargaxabarjonatish")
async def foydalanuvchilarga_xabar(call:CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Hamma haydovchilarga",callback_data="hammahaydovchilarga"))
    markup.insert(InlineKeyboardButton(text="Hamma yo'lovchilarga",callback_data="hammayolovchilarga"))
    markup.insert(InlineKeyboardButton(text="Barcha foydalanuvchilarga",callback_data="barchafoydalanuvchilarga"))
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="akhjsdkajhdkhskdhjajdhskahdskjahsdkjahdasdha"))
    await call.message.answer("Xabar jo'natish",reply_markup=markup)
    await call.message.delete()



class Haydovchi(StatesGroup):
    text = State()
@dp.callback_query_handler(text="hammahaydovchilarga")
async def hamma_haydovchilarga(call:CallbackQuery):
    await call.message.answer("Xabarni kiriting :")
    await Haydovchi.text.set()
@dp.message_handler(state=Haydovchi.text)
async def haydovchi_text(message:Message,state:FSMContext):
    text = message.text
    users = await db.select_all_users()
    drivers = []
    for user in users:
        if user[6]==True:
            drivers.append(user)
    print(drivers)
    if len(drivers)==0:
        for driver in drivers:
            if driver[3]!=message.from_user.id:
                await bot.send_message(chat_id=driver[3],text=text)
        await state.finish()
    else:
        await message.answer("Hozircha haydovchilar yo'q")
        await state.finish()
class Yolovchi(StatesGroup):
    text = State()

@dp.callback_query_handler(text="hammayolovchilarga")
async def hamma_haydovchilarga(call:CallbackQuery):
    await call.message.answer("Xabarni kiriting :")
    await Yolovchi.text.set()

@dp.message_handler(state=Yolovchi.text)
async def haydovchi_text(message:Message,state:FSMContext):
    text = message.text
    users = await db.select_all_users()
    yolovchilar = []
    for user in users:
        if user[5]==True:
            yolovchilar.append(user)
    print(yolovchilar)
    if len(yolovchilar)!=0:
        for yolovchi in yolovchilar:
            if yolovchi[3]!=message.from_user.id:
                await bot.send_message(chat_id=yolovchi[3],text=text)
            await state.finish()
    else:
        await message.answer("Hozircha yo'lovchilar yo'q")
        await state.finish()

class Foydalanuvchilar(StatesGroup):
    text = State()
@dp.callback_query_handler(text="barchafoydalanuvchilarga")
async def hamma_haydovchilarga(call:CallbackQuery):
    await call.message.answer("Xabarni kiriting")
    await Foydalanuvchilar.text.set()

@dp.message_handler(state=Foydalanuvchilar.text)
async def haydovchi_text(message:Message,state:FSMContext):
    text = message.text
    foydalanuvchilar = await db.select_all_users()
    for foydalanuvchi in foydalanuvchilar:
        if foydalanuvchi[3]!=message.from_user.id:
            await bot.send_message(chat_id=foydalanuvchi[3],text=text)
    await state.finish()
@dp.callback_query_handler(text="akhjsdkajhdkhskdhjajdhskahdskjahsdkjahdasdha")
async def hamma_haydovchilarga(call:CallbackQuery):
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
    button = InlineKeyboardButton(text="Foydalanuvchilarga xabar jo'natish",
                                  callback_data="foydalanuvchilargaxabarjonatish")
    markup.add(button)
    await call.message.answer(reply_markup=markup, text="Admin bo'lim")