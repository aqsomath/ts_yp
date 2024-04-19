import asyncio

import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.location import lokatsiya, phone_number
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa
from keyboards.inline.yolovchi.andtuman import andijon_yol, qoraqalpogiston_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import umumiy_menu, tasdiq_oxir, kirish
from keyboards.inline.yolovchi.namtuman import namangan_yol
from keyboards.inline.yolovchi.navoiytuman import navoiy_yol
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_yol
from keyboards.inline.yolovchi.samartuman import samarqand_yol
from keyboards.inline.yolovchi.sirtuman import sirdaryo_yol
from keyboards.inline.yolovchi.soat import time
from keyboards.inline.yolovchi.surtuman import surxondaryo_yol
from keyboards.inline.yolovchi.toshtuman import toshkent_yol
from keyboards.inline.yolovchi.xa_yoq import yes_not
from keyboards.inline.yolovchi.xorazmtuman import xorazm_yol
from states.yolovchi_reys_states import Yolovchi_andijon
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol, viloyatlar_yol_x
from loader import dp, bot, db, limiter
from utils.misc import show_on_gmaps
import datetime

#  1 - ORTGA
@dp.callback_query_handler(text_contains='Bosh menu', state=Yolovchi_andijon.asosiy)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()

@dp.callback_query_handler(text_contains='ortga', state=Yolovchi_andijon.asosiy)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()

@dp.callback_query_handler(state=Yolovchi_andijon.asosiy)
async def andijon(call: CallbackQuery, state: FSMContext):
    if call.data == 'xorazm':
        await state.update_data({"viloyat": "Xorazm"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'andijon':
        await state.update_data({"viloyat": "Andijon"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=andijon_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'namangan':
        await state.update_data({"viloyat": "Namangan"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=namangan_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == "farg'ona":
        await state.update_data({"viloyat": "Farg'ona"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=fargona_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'buxoro':
        await state.update_data({"viloyat": "Buxoro"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=buxoro_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'toshkent':
        await state.update_data({"viloyat": "Toshkent"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=toshkent_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'sirdaryo':
        await state.update_data({"viloyat": "Sirdaryo"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=sirdaryo_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'surxondaryo':
        await state.update_data({"viloyat": "Surxondaryo"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=surxondaryo_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'qashqadaryo':
        await state.update_data({"viloyat": "Qashqadaryo"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qashqadaryo_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'navoiy':
        await state.update_data({"viloyat": "Navoiy"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=navoiy_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'jizzax':
        await state.update_data({"viloyat": "Jizzax"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=jizzax_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'samarqand':
        await state.update_data({"viloyat": "Samarqand"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=samarqand_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()
    if call.data == 'qoraqalpoq':
        await state.update_data({"viloyat": "Qoraqalpog'iston"})
        await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qoraqalpogiston_yol)
        await call.message.delete()
        await Yolovchi_andijon.tuman.set()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatdan taxi kerak ? ", reply_markup=viloyatlar_yol)
    await call.message.delete()
    await Yolovchi_andijon.asosiy.set()


#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.tuman)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "tuman": call.data
        }
    )
    await call.message.answer("Qaysi viloyatga  borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Yolovchi_andijon.viloyatga.set()


@dp.callback_query_handler(text='homeback', state=Yolovchi_andijon.viloyatga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    viloyat = data.get("viloyat")
    if viloyat == "Andijon":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=andijon_yol)
    if viloyat == "Namangan":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=namangan_yol)
    if viloyat == "Farg'ona":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=fargona_yol)
    if viloyat == "Buxoro":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=buxoro_yol)
    if viloyat == "Toshkent":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=toshkent_yol)
    if viloyat == "Sirdaryo":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=sirdaryo_yol)
    if viloyat == "Surxondaryo":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=surxondaryo_yol)
    if viloyat == "Qashqadaryo":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=qashqadaryo_yol)
    if viloyat == "Xorazm":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=xorazm_yol)
    if viloyat == "Navoiy":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=navoiy_yol)
    if viloyat == "Jizzax":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=jizzax_yol)
    if viloyat == "Samarqand":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=samarqand_yol)
    if viloyat == "Qoraqalpog'iston":
        await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=qoraqalpogiston_yol)
    await call.message.delete()
    await Yolovchi_andijon.tuman.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.viloyatga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.viloyatga)
async def reys_viloyatga(call: CallbackQuery, state: FSMContext):
    data = call.data
    print(data)
    if data == 'qoraqalpoq':
        await state.update_data(
            {"viloyatiga": "Qoraqalpog'iston"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=qoraqalpogiston_yol)

    if data == 'sjduuwgfuwgdkgjda':
        await state.update_data(
            {"viloyatiga": "Andijon"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=andijon_yol)

    if data == "kdjhaigdakhdksa":
        await state.update_data(
            {"viloyatiga": "Farg'ona"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=fargona_yol)
    if data == "akilwyiwefsdjksd":
        await state.update_data(
            {"viloyatiga": "Namangan"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=namangan_yol)
    if data == "allaskalkdaslkjd":
        await state.update_data(
            {"viloyatiga": "Buxoro"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=buxoro_yol)
    if data == "euywiudhkns":
        await state.update_data(
            {"viloyatiga": "Toshkent"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=toshkent_yol)
    if data == "jweytfugdiahjash":
        await state.update_data(
            {"viloyatiga": "Sirdaryo"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=sirdaryo_yol)
    if data == "qdwqwdqwsasxa":
        await state.update_data(
            {"viloyatiga": "Surxondaryo"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=surxondaryo_yol)
    if data == "asasdsadasd":
        await state.update_data(
            {"viloyatiga": "Qashqadaryo"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=qashqadaryo_yol)
    if data == "dfdsfdsgfdsfgfd":
        await state.update_data(
            {"viloyatiga": "Xorazm"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=xorazm_yol)
    if data == "fghgfjghjgfh":
        await state.update_data(
            {"viloyatiga": "Navoiy"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=navoiy_yol)
    if data == "reggfvdvdvcx":
        await state.update_data(
            {"viloyatiga": "Jizzax"}
        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=jizzax_yol)
    if data == "tyhjyjghfh":
        await state.update_data(
            {"viloyatiga": "Samarqand"}

        )
        await call.message.answer("Qaysi tumaniga borasiz", reply_markup=samarqand_yol)
    dt = await state.get_data()
    viloyatiga = dt.get("viloyatiga")
    await state.update_data({"baza": viloyatiga})
    await call.message.delete()
    await Yolovchi_andijon.tumaniga.set()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.tumaniga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Yolovchi_andijon.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.tumaniga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()

@dp.callback_query_handler(state=Yolovchi_andijon.tumaniga)
async def reys_tumaniga(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "tumaniga": call.data.capitalize()
        }
    )
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Yolovchi_andijon.kuni.set()


@dp.callback_query_handler(text="ortga", state=Yolovchi_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Yolovchi_andijon.viloyatga.set()


@dp.callback_query_handler(text="atmen", state=Yolovchi_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()

@dp.callback_query_handler(text='Qoldakiritish', state=Yolovchi_andijon.kuni)
async def qolda_yozing(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=6)
    markup.insert(InlineKeyboardButton(text="Yanvar", callback_data="1"))
    markup.insert(InlineKeyboardButton(text="Fevral", callback_data="2"))
    markup.insert(InlineKeyboardButton(text="Mart", callback_data="3"))
    markup.insert(InlineKeyboardButton(text="Aprel", callback_data="4"))
    markup.insert(InlineKeyboardButton(text="May", callback_data="5"))
    markup.insert(InlineKeyboardButton(text="Iyun", callback_data="6"))
    markup.insert(InlineKeyboardButton(text="Iyul", callback_data="7"))
    markup.insert(InlineKeyboardButton(text="Avgust", callback_data="8"))
    markup.insert(InlineKeyboardButton(text="Sentabr", callback_data="9"))
    markup.insert(InlineKeyboardButton(text="Oktabr", callback_data="10"))
    markup.insert(InlineKeyboardButton(text="Noyabr", callback_data="11"))
    markup.insert(InlineKeyboardButton(text="Dekabr", callback_data="12"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer("Qaysi oyda yo'lga chiqasiz ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yolovchi_andijon.oyini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(text="Ortga", state=Yolovchi_andijon.oyini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Yolovchi_andijon.kuni.set()


@dp.callback_query_handler(state=Yolovchi_andijon.oyini_kiritsh)
async def oyi(call: CallbackQuery, state: FSMContext):
    await state.update_data({"oyi": call.data})
    markup = InlineKeyboardMarkup(row_width=6)
    for i in range(1, 32):
        markup.insert(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer(f"Tanlagan oyingizni nechinchi kunida ketasiz ? ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yolovchi_andijon.kunini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(text="Ortga", state=Yolovchi_andijon.kunini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=6)
    markup.insert(InlineKeyboardButton(text="Yanvar", callback_data="1"))
    markup.insert(InlineKeyboardButton(text="Fevral", callback_data="2"))
    markup.insert(InlineKeyboardButton(text="Mart", callback_data="3"))
    markup.insert(InlineKeyboardButton(text="Aprel", callback_data="4"))
    markup.insert(InlineKeyboardButton(text="May", callback_data="5"))
    markup.insert(InlineKeyboardButton(text="Iyun", callback_data="6"))
    markup.insert(InlineKeyboardButton(text="Iyul", callback_data="7"))
    markup.insert(InlineKeyboardButton(text="Avgust", callback_data="8"))
    markup.insert(InlineKeyboardButton(text="Sentabr", callback_data="9"))
    markup.insert(InlineKeyboardButton(text="Oktabr", callback_data="10"))
    markup.insert(InlineKeyboardButton(text="Noyabr", callback_data="11"))
    markup.insert(InlineKeyboardButton(text="Dekabr", callback_data="12"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer("Qaysi oyda yo'lga chiqasiz ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(state=Yolovchi_andijon.kunini_kiritsh)
async def kunini(call: CallbackQuery, state: FSMContext):
    await state.update_data({"kuni": call.data})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text='Bugun', state=Yolovchi_andijon.kuni)
@dp.callback_query_handler(text='Ertaga', state=Yolovchi_andijon.kuni)
@dp.callback_query_handler(text='Indinga', state=Yolovchi_andijon.kuni)
async def oy(call: CallbackQuery, state: FSMContext):
    if call.data == 'Bugun':
        today = datetime.date.today().day
        oyi = datetime.date.today().month
        await state.update_data({"oyi": oyi})
        await state.update_data({"kuni": today})
    if call.data == 'Ertaga':
        today = datetime.date.today() + datetime.timedelta(days=1)
        await state.update_data({"kuni": today.day})
        oyi = datetime.date.today().month
        await state.update_data({"oyi": oyi})
    if call.data == 'Indinga':
        today = datetime.date.today() + datetime.timedelta(days=2)
        await state.update_data({"kuni": today.day})
        oyi = datetime.date.today().month
        await state.update_data({"oyi": oyi})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text='qaytish', state=Yolovchi_andijon.aniq_kuni)
async def aniq_ku(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Yolovchi_andijon.kuni.set()


@dp.callback_query_handler(text='bomenyu', state=Yolovchi_andijon.aniq_kuni)
async def menu_bosh(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga pochta olib borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Yolovchi_andijon.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.kuni)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.aniq_kuni)
async def reys_kuni(call: CallbackQuery, state: FSMContext):
    await state.update_data({"kuni":call.data})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Yolovchi_andijon.kuni.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.soat)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.soat)
async def reys_soat(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "soat": call.data
        }
    )
    data = await state.get_data()
    now = datetime.datetime.now()
    oy = int(data.get('oyi'))
    kuni = int(data.get('kuni'))
    soat = int(data.get('soat'))
    year = datetime.datetime.now().year
    start_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    end_time = datetime.datetime(year, oy, kuni, soat, 0, 0)
    time_difference = end_time - start_time
    time_difference_seconds = time_difference.total_seconds()
    if time_difference_seconds > 0:

        markup = aiogram.types.InlineKeyboardMarkup(row_width=3, )
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
        await call.message.answer("Sizga bog'lanishimiz uchun", reply_markup=phone_number)
        await call.message.answer("Telefon raqamingizni kiriting ..\nMana shu raqamni ishlatayotgan bo'lsangiz\n"
                                  "Kontakt yuborish ni bosing", reply_markup=markup)
        await call.message.delete()
        await Yolovchi_andijon.phone.set()
    else:
        await call.message.answer("Kechirasiz siz vaqtni noto'g'ri kiritdingiz?")
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Yolovchi_andijon.kuni.set()


@dp.callback_query_handler(text='tortga', state=Yolovchi_andijon.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.message_handler(content_types=['contact', 'text'], state=Yolovchi_andijon.phone)
async def reys_loc(message: Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 1)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 2)

    if message.contact:
        await state.update_data(
            {
                "phone": message.contact.phone_number
            }
        )
    else:
        await state.update_data(
            {
                "phone": message.text
            }
        )

    data = await state.get_data()
    viloyat = data.get('viloyat')
    tuman = data.get('tuman').capitalize()
    viloyatiga = data.get('viloyatiga')
    tumaniga = data.get('tumaniga')
    oy = data.get('oyi')
    kuni = data.get('kuni')
    soat = data.get('soat')
    phone = data.get('phone')
    if oy is not None:
        m = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
            f"🏤 <b>{tuman}dan </b> \n" \
            f"🏢 <b>{viloyatiga} \n</b>" \
            f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi</b>\n" \
            f"📆 <b>Sanasi : {kuni}.{oy}</b>\n" \
            f"⏱ <b>{soat}</b>\n"
        msg = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
              f"🏤<b> {tuman} dan </b> \n" \
              f"🏢<b> {viloyatiga} </b>\n" \
              f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi </b>\n" \
              f"📆 <b>Qachon yo'lga chiqadi : {kuni}.{oy}</b>\n" \
              f"⏱ <b>{soat}</b>\n" \
              f"📞 <b>Tel : {phone}</b>\n"
        await state.update_data(
            {
                "msg": msg, "m": m
            }
        )
    else:
        m = f"🚕\n🏢 <b>{viloyat} \n</b>" \
            f"🏤 <b>{tuman}dan  </b>\n" \
            f"🏢 <b>{viloyatiga} </b>\n" \
            f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi </b>\n" \
            f"📆 <b>Sanasi : {kuni}.{oy}</b>\n" \
            f"⏱ <b>{soat}</b>\n"
        msg = f"🚕\n🏢 <b>{viloyat}  </b>\n" \
              f"🏤 <b>{tuman}dan \n</b>" \
              f"🏢 <b>{viloyatiga} \n</b>" \
              f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi</b>\n" \
              f"📆 <b>Qachon yo'lga chiqadi :  {kuni}.{oy}</b>\n" \
              f"⏱ <b>{soat}\n</b>\n" \
              f"📞 <b>Tel : {phone}\n</b>"
        await state.update_data(
            {
                "msg": msg, "m": m
            }
        )
    await message.answer(f"Ma'lumotlar to'g'rimi {msg}?", reply_markup=yes_not)
    await Yolovchi_andijon.tasdiqlash.set()
    await message.delete()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.phone.set()


@dp.callback_query_handler(text='yesss', state=Yolovchi_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    viloyat = data.get('viloyat')
    tumaniga = data.get('tumaniga')
    baza = data.get('viloyatiga')
    msg = data.get("msg")
    m = data.get("m")
    telegram_id = call.from_user.id
    now = datetime.datetime.now()
    oy = int(data.get('oyi'))
    kuni = int(data.get('kuni'))
    soat = int(data.get('soat'))
    year = datetime.datetime.now().year
    start_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    end_time = datetime.datetime(year, oy, kuni, soat, 0, 0)
    time_difference = end_time - start_time
    time_difference_seconds = time_difference.total_seconds()
    if time_difference_seconds > 0:
        await db.add_order_tayyor_taxi(
            tayyor_taxi=None,
            tayyor_taxi_full=None,
            tayyor_yolovchi=m,
            tayyor_yolovchi_full=msg,
            viloyat=viloyat,
            region=tuman,
            telegram_id=telegram_id,
            viloyatga=baza,
            tumanga=tumaniga,
            tayyor_pochta=None,
            tayyor_pochta_full=None,
            tayyor_yuk=None,
            tayyor_yuk_full=None,
            tayyor_yuk_haydovchisi=None,
            tayyor_yuk_haydovchisi_full=None,
            tayyor_pochta_mashina=None,
            tayyor_pochta_mashina_full=None,
            tayyor_sayohatchi=None,
            tayyor_sayohatchi_full=None,
            tayyor_sayohatchi_mashina=None,
            tayyor_sayohatchi_full_mashina=None,
            event_time=end_time

        )

        await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                  "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                                  )

        order = await db.select_order(tayyor_yolovchi_full=msg)
        offset = -28
        limit = 28
        while True:
            offset += limit
            drivers = await db.select_all_drivers(limit=limit, offset=offset)
            await asyncio.sleep(1)
            for driver in drivers:
                if driver[1] == 'odam':
                    if driver[4]!=call.from_user.id:
                        async with limiter:
                            markup = InlineKeyboardMarkup(row_width=2)
                            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data=f'qabul_flkk_{order[0]}'))
                            await bot.send_message(chat_id=driver[4], text=m, reply_markup=markup,parse_mode="HTML")
            await state.update_data({"msg":msg})
            await call.message.delete()
            await state.finish()
    else:
        await call.message.answer("Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
        await state.finish()


@dp.callback_query_handler(text='nott', state=Yolovchi_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()

@dp.callback_query_handler(text='add_information', state=Yolovchi_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytish"))
    markup.insert(InlineKeyboardButton(text="Boshmenu", callback_data="Boshmenu"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Lokatsiya yuboring  ? ", reply_markup=lokatsiya)
    await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.locatsiya.set()


@dp.callback_query_handler(state=Yolovchi_andijon.locatsiya, text="Boshmenu")
async def Boshmenuga(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.locatsiya, text="Qaytish")
async def qaytaman(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg")
    await call.message.answer(f"Malumotlaringiz to'g'rimi ?\n{msg}", reply_markup=yes_not)
    await call.message.delete()
    await Yolovchi_andijon.tasdiqlash.set()


@dp.callback_query_handler(state=Yolovchi_andijon.locatsiya, text="Keyingisi")
async def keyingisio(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
    markup = InlineKeyboardMarkup(row_width=3)
    markup.insert(InlineKeyboardButton(text="1", callback_data="bir"))
    markup.insert(InlineKeyboardButton(text="2", callback_data="ikki"))
    markup.insert(InlineKeyboardButton(text="3", callback_data="uch"))
    markup.insert(InlineKeyboardButton(text="4", callback_data="to'rt"))
    markup.insert(InlineKeyboardButton(text="5", callback_data="besh"))
    markup.insert(InlineKeyboardButton(text="Kiritish", callback_data="Kiritish"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Necha kishi ketasizlar ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.necha_kishi.set()


@dp.message_handler(content_types=['location'], state=Yolovchi_andijon.locatsiya)
async def location(message: Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 1)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 2)
    lat = message.location.latitude
    lon = message.location.longitude
    place = show_on_gmaps.show(lat=lat, lon=lon)
    await state.update_data(
        {
            "lat": lat,
            "lon": lon
        }
    )
    markup = InlineKeyboardMarkup(row_width=3)
    markup.insert(InlineKeyboardButton(text="1", callback_data="bir"))
    markup.insert(InlineKeyboardButton(text="2", callback_data="ikki"))
    markup.insert(InlineKeyboardButton(text="3", callback_data="uch"))
    markup.insert(InlineKeyboardButton(text="4", callback_data="to'rt"))
    markup.insert(InlineKeyboardButton(text="5", callback_data="besh"))
    markup.insert(InlineKeyboardButton(text="Kiritish", callback_data="Kiritish"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await message.answer("Necha kishi ketasizlar ?", reply_markup=markup)
    await message.delete()
    await Yolovchi_andijon.necha_kishi.set()


@dp.callback_query_handler(state=Yolovchi_andijon.necha_kishi, text="Bosh menu")
async def qayatdsdsaa(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.necha_kishi, text="Ortga")
async def qayataa(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytish"))
    markup.insert(InlineKeyboardButton(text="Boshmenu", callback_data="Boshmenu"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Lokatsiya yuboring  ? ", reply_markup=lokatsiya)
    await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.locatsiya.set()


@dp.callback_query_handler(state=Yolovchi_andijon.necha_kishi, text="Keyingisi")
async def kisi(call: CallbackQuery, state: FSMContext):
    oldi_kerakmi = InlineKeyboardMarkup(row_width=2)
    oldi_kerakmi.insert(InlineKeyboardButton(text="Xa kerak", callback_data="Oldi o'rindiq kerak"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Yo'q kerak emas", callback_data="Oldi o'rindiq kerak emas"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Oldi o'rindiq kerakmi ?", reply_markup=oldi_kerakmi)
    await call.message.delete()
    await Yolovchi_andijon.oldi_kerakmi.set()


@dp.callback_query_handler(state=Yolovchi_andijon.necha_kishi, text="Kiritish")
async def kisi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Necha kishi ketishingizni son orqali ifodalang")
    await Yolovchi_andijon.qolda_yozish.set()
    await call.message.delete()


@dp.message_handler(state=Yolovchi_andijon.qolda_yozish)
async def neckakishi(msg: Message, state: FSMContext):
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)
    if msg.text.isdigit() == True:
        await state.update_data(
            {
                "odam_soni": msg.text
            }
        )
        oldi_kerakmi = InlineKeyboardMarkup(row_width=2)
        oldi_kerakmi.insert(InlineKeyboardButton(text="Xa kerak", callback_data="Oldi o'rindiq kerak"))
        oldi_kerakmi.insert(InlineKeyboardButton(text="Yo'q kerak emas", callback_data="Oldi o'rindiq kerak emas"))
        oldi_kerakmi.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
        oldi_kerakmi.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
        oldi_kerakmi.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
        await msg.answer("Oldi o'rindiq kerakmi ?", reply_markup=oldi_kerakmi)
        await msg.delete()
        await Yolovchi_andijon.oldi_kerakmi.set()
    else:
        await msg.answer("Iltimos Son orqali kiriting . Matn kiritmang !!!")
        await msg.delete()
        await Yolovchi_andijon.qolda_yozish.set()


@dp.callback_query_handler(state=Yolovchi_andijon.necha_kishi)
async def kisi(call: CallbackQuery, state: FSMContext):
    print(call.data)
    await state.update_data(
        {
            "odam_soni": call.data
        }
    )
    oldi_kerakmi = InlineKeyboardMarkup(row_width=2)
    oldi_kerakmi.insert(InlineKeyboardButton(text="Xa kerak", callback_data="Oldi o'rindiq kerak"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Yo'q kerak emas", callback_data="Oldi o'rindiq kerak emas"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Oldi o'rindiq kerakmi ?", reply_markup=oldi_kerakmi)
    await call.message.delete()
    await Yolovchi_andijon.oldi_kerakmi.set()


@dp.callback_query_handler(state=Yolovchi_andijon.oldi_kerakmi, text="Ortga")
async def kisi(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=3)
    markup.insert(InlineKeyboardButton(text="1", callback_data="bir"))
    markup.insert(InlineKeyboardButton(text="2", callback_data="ikki"))
    markup.insert(InlineKeyboardButton(text="3", callback_data="uch"))
    markup.insert(InlineKeyboardButton(text="4", callback_data="to'rt"))
    markup.insert(InlineKeyboardButton(text="5", callback_data="besh"))
    markup.insert(InlineKeyboardButton(text="Kiritish", callback_data="Kiritish"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Necha kishi ketasizlar ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.necha_kishi.set()


@dp.callback_query_handler(state=Yolovchi_andijon.oldi_kerakmi, text="Bosh menu")
async def kisi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.oldi_kerakmi, text="Keyingisi")
async def kisi(call: CallbackQuery, state: FSMContext):
    qanday_avto = InlineKeyboardMarkup(row_width=3)
    qanday_avto.insert(InlineKeyboardButton(text='Ekonom', callback_data="Ekonom", ))
    qanday_avto.insert(InlineKeyboardButton(text='Komfort', callback_data="Komfort"))
    qanday_avto.insert(InlineKeyboardButton(text='Biznez klass', callback_data="Biznes klass"))
    qanday_avto.insert(InlineKeyboardButton(text="Farqi yo'q", callback_data="Farqi yo'q"))
    qanday_avto.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    qanday_avto.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    qanday_avto.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Avtomobil qanday bo'lsin ?", reply_markup=qanday_avto)
    await call.message.delete()
    await Yolovchi_andijon.qanday_moshina.set()


@dp.callback_query_handler(state=Yolovchi_andijon.oldi_kerakmi)
async def kisi(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "oldi_joy": call.data
        }
    )
    qanday_avto = InlineKeyboardMarkup(row_width=3)
    qanday_avto.insert(InlineKeyboardButton(text='Ekonom', callback_data="Ekonom", ))
    qanday_avto.insert(InlineKeyboardButton(text='Komfort', callback_data="Komfort"))
    qanday_avto.insert(InlineKeyboardButton(text='Biznez klass', callback_data="Biznes klass"))
    qanday_avto.insert(InlineKeyboardButton(text="Farqi yo'q", callback_data="Farqi yo'q"))
    qanday_avto.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    qanday_avto.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    qanday_avto.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Avtomobil qanday bo'lsin ?", reply_markup=qanday_avto)
    await call.message.delete()
    await Yolovchi_andijon.qanday_moshina.set()


@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina, text="Ortga")
async def kisi(call: CallbackQuery, state: FSMContext):
    oldi_kerakmi = InlineKeyboardMarkup(row_width=2)
    oldi_kerakmi.insert(InlineKeyboardButton(text="Xa kerak", callback_data="Oldi o'rindiq kerak"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Yo'q kerak emas", callback_data="Oldi o'rindiq kerak emas"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    oldi_kerakmi.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Oldi o'rindiq kerakmi ?", reply_markup=oldi_kerakmi)
    await call.message.delete()
    await Yolovchi_andijon.oldi_kerakmi.set()


@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina, text="Bosh menu")
async def kisi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina, text="Keyingisi")
async def mashina_turi(call:CallbackQuery,state:FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia', callback_data='Nexia'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Kobalt', callback_data='Kobalt'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Damas', callback_data='Damas'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Gentra', callback_data='Gentra'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Onix', callback_data='Onix'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Monza', callback_data='Monza'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.mashina.set()

@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina)
async def mashina_turi(call:CallbackQuery,state:FSMContext):
    await state.update_data({"tarif_avto":call.data})
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia', callback_data='Nexia'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Kobalt', callback_data='Kobalt'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Damas', callback_data='Damas'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Gentra', callback_data='Gentra'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Onix', callback_data='Onix'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Monza', callback_data='Monza'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.mashina.set()

@dp.callback_query_handler(state=Yolovchi_andijon.mashina,text='boshmenu')
async def qanday_mashina(call:CallbackQuery,state:FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()
@dp.callback_query_handler(state=Yolovchi_andijon.mashina,text='ortga')
async def qanday_mashina(call:CallbackQuery,state:FSMContext):
    qanday_avto = InlineKeyboardMarkup(row_width=3)
    qanday_avto.insert(InlineKeyboardButton(text='Ekonom', callback_data="Ekonom", ))
    qanday_avto.insert(InlineKeyboardButton(text='Komfort', callback_data="Komfort"))
    qanday_avto.insert(InlineKeyboardButton(text='Biznez klass', callback_data="Biznes klass"))
    qanday_avto.insert(InlineKeyboardButton(text="Farqi yo'q", callback_data="Farqi yo'q"))
    qanday_avto.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    qanday_avto.insert(InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu"))
    qanday_avto.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
    await call.message.answer("Avtomobil qanday bo'lsin ?", reply_markup=qanday_avto)
    await call.message.delete()
    await Yolovchi_andijon.qanday_moshina.set()
@dp.callback_query_handler(state=Yolovchi_andijon.mashina,text='qoldayozish')
async def mashina_turi(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sizga qanday mashina rusumi kerak ?(Qo'lda kiriting)")
    await Yolovchi_andijon.mashina_qolda_turi.set()
@dp.message_handler(state=Yolovchi_andijon.mashina_qolda_turi)
async def mashina_turi(message:Message,state:FSMContext):
    await state.update_data({"Avto_turi":message.text})
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='10-20', callback_data='10-20'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='20-30', callback_data='20-30'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='30-40', callback_data='30-40'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='40-50', callback_data='40-50'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='50-60', callback_data='50-60'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='60-70', callback_data='60-70'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='70-80', callback_data='70-80'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='80-90', callback_data='80-90'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='90-100', callback_data='90+100'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='100+', callback_data='100+'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    await message.answer("Yo'l haqqi uchun qancha bermoqchisiz ?", reply_markup=markup)
    await Yolovchi_andijon.kira_haqqi.set()
    await message.delete()
@dp.callback_query_handler(state=Yolovchi_andijon.mashina)
async def mashina_turi(call:CallbackQuery,state:FSMContext):
    await state.update_data({"Avto_turi":call.data})
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='10-20', callback_data='10-20'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='20-30', callback_data='20-30'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='30-40', callback_data='30-40'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='40-50', callback_data='40-50'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='50-60', callback_data='50-60'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='60-70', callback_data='60-70'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='70-80', callback_data='70-80'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='80-90', callback_data='80-90'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='90-100', callback_data='90+100'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='100+', callback_data='100+'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    await call.message.answer("Yo'l haqqi uchun qancha bermoqchisiz ?", reply_markup=markup)
    await Yolovchi_andijon.kira_haqqi.set()
    await call.message.delete()

@dp.callback_query_handler(state=Yolovchi_andijon.mashina,text='Keyingisi')
async def mashina_turi(call:CallbackQuery,state:FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='10-20', callback_data='10-20'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='20-30', callback_data='20-30'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='30-40', callback_data='30-40'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='40-50', callback_data='40-50'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='50-60', callback_data='50-60'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='60-70', callback_data='60-70'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='70-80', callback_data='70-80'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='80-90', callback_data='80-90'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='90-100', callback_data='90+100'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='100+', callback_data='100+'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    await call.message.answer("Yo'l haqqi uchun qancha bermoqchisiz ?", reply_markup=markup)
    await Yolovchi_andijon.kira_haqqi.set()
    await call.message.delete()

@dp.callback_query_handler(state=Yolovchi_andijon.kira_haqqi,text='boshmenu')
async def kira_keyingisi(call:CallbackQuery,state:FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()
@dp.callback_query_handler(state=Yolovchi_andijon.kira_haqqi,text='ortga')
async def kira_keyingisi(call:CallbackQuery,state:FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia', callback_data='Nexia'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Kobalt', callback_data='Kobalt'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Damas', callback_data='Damas'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Gentra', callback_data='Gentra'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Onix', callback_data='Onix'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Monza', callback_data='Monza'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.mashina.set()

@dp.callback_query_handler(state=Yolovchi_andijon.kira_haqqi,text="ruchnoy")
async def kira_uchun(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qancha bermoqchisiz ? (Qo'lda kiriting)")
    await Yolovchi_andijon.kira_haqqi_2.set()

@dp.message_handler(state=Yolovchi_andijon.kira_haqqi_2)
async def kisi(message: Message, state: FSMContext):
    await state.update_data({"yol_haqqi":message.text})
    data = await state.get_data()
    msg = data.get("msg")
    yol_haqqi = data.get("yol_haqqi")
    yol_kira_uchun = f"Yo'l haqqi uchun qancha to'lamoqchi : {yol_haqqi} so'm"
    m = data.get("m")
    lat = data.get("lat")
    lon = data.get("lon")
    lokatsiya = f"<a href='https://www.google.com/maps?q={lat},{lon}'>Yo'lovchi turgan joy lokatsiyasi</a>"
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    tarif  = data.get("tarif_avto")
    tarif_avto = f"Qanday ta'rifdagi taxi kerak : {tarif}"
    avto_turi = data.get("Avto_turi")
    odam_soni = f"Necha kishi ketadi: {odam_soni}"
    avto_turi = f"Qanday avto kerak : {avto_turi}"
    if lat == None:
        lokatsiya = ""

    if odam_soni == None:
        odam_soni = ""
    if oldi_orin == None:
        oldi_orin = ""
    if avto_turi == None:
        avto_turi = ""
    if tarif == None:
        tarif_avto = ""
    msg_full = msg + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{yol_kira_uchun}\n{tarif_avto}\n{lokatsiya}"
    m_full = m + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{yol_kira_uchun}\n{tarif_avto}\n{lokatsiya}"
    await state.update_data(
        {
            "msg_full": msg_full,
            "m_full": m_full,
        }
    )
    await message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
    await message.delete()
    await Yolovchi_andijon.end.set()

@dp.callback_query_handler(state=Yolovchi_andijon.kira_haqqi,text='Keyingisi')
async def kira_keyingisi(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    msg = data.get("msg")
    m = data.get("m")
    lat = data.get("lat")
    lon = data.get("lon")
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    tarif = data.get("tarif_avto")
    tarif_avto = f"Qanday ta'rifdagi taxi kerak : {tarif}"
    avto_turi = data.get("Avto_turi")
    odam_soni = f"Necha kishi ketadi: {odam_soni}"
    avto_turi = f"Qanday avto kerak : {avto_turi}"
    if lat == None:
        lokatsiya = ""
    else:
        lokatsiya = f"<a href='https://www.google.com/maps?q={lat},{lon}'>Yo'lovchi turgan joy lokatsiyasi</a>"
    if odam_soni == None:
        odam_soni = ""
    if oldi_orin == None:
        oldi_orin = ""
    if avto_turi == None:
        avto_turi = ""
    if tarif == None:
        tarif_avto = ""
    msg_full = msg + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{tarif_avto}\n{lokatsiya}"
    m_full = m + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{tarif_avto}\n{lokatsiya}"
    await state.update_data(
        {
            "msg_full": msg_full,
            "m_full": m_full,
        }
    )
    await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir, parse_mode="HTML")
    await call.message.delete()
    await Yolovchi_andijon.end.set()
@dp.callback_query_handler(state=Yolovchi_andijon.kira_haqqi)
async def kisi(call: CallbackQuery, state: FSMContext):
    await state.update_data({"yol_haqqi":call.data})
    data = await state.get_data()
    msg = data.get("msg")
    tarif = data.get("tarif_avto")
    tarif_avto = f"Qanday ta'rifdagi taxi kerak : {tarif}"
    yol_haqqi = data.get("yol_haqqi")
    yol_kira_uchun = f"Yo'l haqqi uchun qancha to'lamoqchi : {yol_haqqi} so'm"
    m = data.get("m")
    lat = data.get("lat")
    lon = data.get("lon")
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    avto_turi = data.get("Avto_turi")
    odam_soni = f"Necha kishi ketadi: {odam_soni}"
    avto_turi = f"Qanday avto kerak : {avto_turi}"
    if lat == None:
        lokatsiya = ""
    else:
        lokatsiya = f"<a href='https://www.google.com/maps?q={lat},{lon}'>Yo'lovchi turgan joy lokatsiyasi</a>"
    if odam_soni == None:
        odam_soni = ""
    if oldi_orin == None:
        oldi_orin = ""
    if avto_turi == None:
        avto_turi = ""
    if tarif == None:
        tarif_avto = ""
    msg_full = msg + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{yol_kira_uchun}\n{tarif_avto}\n{lokatsiya}"
    m_full = m + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{yol_kira_uchun}\n{tarif_avto}\n{lokatsiya}"
    await state.update_data(
        {
            "msg_full": msg_full,
            "m_full": m_full,
        }
    )
    await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir,parse_mode="HTML")
    await call.message.delete()
    await Yolovchi_andijon.end.set()


@dp.callback_query_handler(text='qaytish', state=Yolovchi_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='10-20', callback_data='10-20'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='20-30', callback_data='20-30'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='30-40', callback_data='30-40'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='40-50', callback_data='40-50'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='50-60', callback_data='50-60'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='60-70', callback_data='60-70'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='70-80', callback_data='70-80'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='80-90', callback_data='80-90'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='90-100', callback_data='90+100'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='100+', callback_data='100+'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
    await call.message.answer("Yo'l haqqi uchun qancha bermoqchisiz ?", reply_markup=markup)
    await Yolovchi_andijon.kira_haqqi.set()


@dp.callback_query_handler(text='glavmenu', state=Yolovchi_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()


@dp.callback_query_handler(text='Confirm', state=Yolovchi_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    viloyat = data.get('viloyat')
    tumaniga = data.get('tumaniga')
    baza = data.get('viloyat')
    print(tuman)
    msg = data.get("msg_full")
    m_full = data.get("m_full")
    telegram_id = call.from_user.id
    now = datetime.datetime.now()
    oy = int(data.get('oyi'))
    kuni = int(data.get('kuni'))
    soat = int(data.get('soat'))
    year = datetime.datetime.now().year
    start_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    end_time = datetime.datetime(year, oy, kuni, soat, 0, 0)
    time_difference = end_time - start_time
    time_difference_seconds = time_difference.total_seconds()
    if time_difference_seconds > 0:
        await db.add_order_tayyor_taxi(
            tayyor_taxi=None,
            tayyor_taxi_full=None,
            tayyor_yolovchi=m_full,
            tayyor_yolovchi_full=msg,
            viloyat=viloyat,
            region=tuman,
            telegram_id=telegram_id,
            viloyatga=baza,
            tumanga=tumaniga,
            tayyor_pochta=None,
            tayyor_pochta_full=None,
            tayyor_yuk=None,
            tayyor_yuk_full=None,
            tayyor_yuk_haydovchisi=None,
            tayyor_yuk_haydovchisi_full=None,
            tayyor_pochta_mashina=None,
            tayyor_pochta_mashina_full=None,
            tayyor_sayohatchi=None,
            tayyor_sayohatchi_full=None,
            tayyor_sayohatchi_mashina=None,
            tayyor_sayohatchi_full_mashina=None,
            event_time=end_time

        )

        await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                  "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                                  )

        order = await db.select_order(tayyor_yolovchi_full=msg)
        offset = -28
        limit = 28
        while True:
            offset += limit
            drivers = await db.select_all_drivers(limit=limit, offset=offset)
            await asyncio.sleep(1)
            for driver in drivers:
                if driver[1] == 'odam':
                    if driver[4]!=call.from_user.id:
                        async with limiter:
                            markup = InlineKeyboardMarkup(row_width=2)
                            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data=f'qabul_flkk_{order[0]}'))
                            await bot.send_message(chat_id=driver[4], text=m_full, reply_markup=markup, parse_mode="HTML")
            await state.update_data({"msg": msg})
            await call.message.delete()
            await state.finish()
    else:
        await call.message.answer(
            "Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
        await state.finish()


@dp.callback_query_handler(text='UnConfirm', state=Yolovchi_andijon.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
            await state.finish()
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
            await state.finish()
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
            await state.finish()
