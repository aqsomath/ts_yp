import asyncio
import datetime

import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.location import lokatsiya, phone_number
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa
from keyboards.inline.pochta_yuborish.pochta_yuborish_tugmalari import pochta_viloyatlar
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
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol_x
from loader import dp, bot, db, limiter
from states.yolovchi_pochta_statet import Pochta_andijon
from utils.misc import show_on_gmaps

#  1 - ORTGA
@dp.callback_query_handler(state=Pochta_andijon.asosiy,text="Ortga")
async def haydovchi(call:CallbackQuery,state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
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
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)


@dp.callback_query_handler(state=Pochta_andijon.asosiy,text="Bosh menu")
async def haydovchi(call:CallbackQuery,state: FSMContext):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",reply_markup=umumiy_menu)
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
@dp.callback_query_handler(state=Pochta_andijon.asosiy)
async def andijon(call: CallbackQuery, state: FSMContext):
        
            if call.data=='9999':
                await state.update_data({"viloyat": "Xorazm"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='111':
                await state.update_data({"viloyat": "Andijon"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=andijon_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='222':
                await state.update_data({"viloyat": "Namangan"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=namangan_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='333':
                await state.update_data({"viloyat": "Farg'ona"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=fargona_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='4444':
                await state.update_data({"viloyat": "Buxoro"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=buxoro_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='5555':
                await state.update_data({"viloyat": "Toshkent"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=toshkent_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='6666':
                await state.update_data({"viloyat": "Sirdaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=sirdaryo_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='7777':
                await state.update_data({"viloyat": "Surxondaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=surxondaryo_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='8888':
                await state.update_data({"viloyat": "Qashqadaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qashqadaryo_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='9999':
                await state.update_data({"viloyat": "Xorazm"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='101010':
                await state.update_data({"viloyat": "Navoiy"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=navoiy_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='121212':
                await state.update_data({"viloyat": "Jizzax"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=jizzax_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='131313':
                await state.update_data({"viloyat": "Samarqand"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=samarqand_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()
            if call.data=='qoraqalpoq':
                await state.update_data({"viloyat": "Qoraqalpog'iston"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qoraqalpogiston_yol)
                await call.message.delete()
                await Pochta_andijon.tuman.set()

@dp.callback_query_handler(text='ortga', state=Pochta_andijon.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatdan pochta yuborasiz ? ", reply_markup=pochta_viloyatlar)
        await Pochta_andijon.asosiy.set()
        await call.message.delete()

#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.tuman)
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

@dp.callback_query_handler(state=Pochta_andijon.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "tuman": call.data
            }
        )
        await call.message.answer("Qaysi viloyatga pochta yuborasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Pochta_andijon.viloyatga.set()


@dp.callback_query_handler(text='homeback', state=Pochta_andijon.viloyatga)
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
        await Pochta_andijon.tuman.set()


@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.viloyatga)
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
@dp.callback_query_handler(state=Pochta_andijon.viloyatga)
async def reys_viloyatga(call: CallbackQuery, state: FSMContext):
    

        data = call.data
        print(data)
        if data == 'qoraqalpoq':
            await state.update_data(
                {"viloyatiga": "Qoraqalpog'iston"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=qoraqalpogiston_yol)

        if data == 'sjduuwgfuwgdkgjda':
            await state.update_data(
                {"viloyatiga": "Andijon"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=andijon_yol)

        if data == "kdjhaigdakhdksa":
            await state.update_data(
                {"viloyatiga": "Farg'ona"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=fargona_yol)
        if data == "akilwyiwefsdjksd":
            await state.update_data(
                {"viloyatiga": "Namangan"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=namangan_yol)
        if data == "allaskalkdaslkjd":
            await state.update_data(
                {"viloyatiga": "Buxoro"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=buxoro_yol)
        if data == "euywiudhkns":
            await state.update_data(
                {"viloyatiga": "Toshkent"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=toshkent_yol)
        if data == "jweytfugdiahjash":
            await state.update_data(
                {"viloyatiga": "Sirdaryo"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=sirdaryo_yol)
        if data == "qdwqwdqwsasxa":
            await state.update_data(
                {"viloyatiga": "Surxondaryo"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=surxondaryo_yol)
        if data == "asasdsadasd":
            await state.update_data(
                {"viloyatiga": "Qashqadaryo"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=qashqadaryo_yol)
        if data == "dfdsfdsgfdsfgfd":
            await state.update_data(
                {"viloyatiga": "Xorazm"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=xorazm_yol)
        if data == "fghgfjghjgfh":
            await state.update_data(
                {"viloyatiga": "Navoiy"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=navoiy_yol)
        if data == "reggfvdvdvcx":
            await state.update_data(
                {"viloyatiga": "Jizzax"}
            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=jizzax_yol)
        if data == "tyhjyjghfh":
            await state.update_data(
                {"viloyatiga": "Samarqand"}

            )
            await call.message.answer("Qaysi tumaniga pochta yuborasiz", reply_markup=samarqand_yol)
        await state.update_data({"baza": data})
        await call.message.delete()
        await Pochta_andijon.tumaniga.set()
@dp.callback_query_handler(text='ortga', state=Pochta_andijon.tumaniga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga pochta yuborasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Pochta_andijon.viloyatga.set()

@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.tumaniga)
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

@dp.callback_query_handler(state=Pochta_andijon.tumaniga)
async def reys_tumaniga(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "tumaniga": call.data.capitalize()
            }
        )
        await call.message.answer("Qachon yo'lga chiqarasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Pochta_andijon.kuni.set()


@dp.callback_query_handler(text="ortga", state=Pochta_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga pochta yuborasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Pochta_andijon.viloyatga.set()


@dp.callback_query_handler(text="atmen", state=Pochta_andijon.kuni)
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


@dp.callback_query_handler(text='Qoldakiritish', state=Pochta_andijon.kuni)
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
    await Pochta_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Pochta_andijon.oyini_kiritsh)
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


@dp.callback_query_handler(text="Ortga", state=Pochta_andijon.oyini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Pochta_andijon.kuni.set()


@dp.callback_query_handler(state=Pochta_andijon.oyini_kiritsh)
async def oyi(call: CallbackQuery, state: FSMContext):
    await state.update_data({"oyi": call.data})
    markup = InlineKeyboardMarkup(row_width=6)
    for i in range(1, 32):
        markup.insert(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer(f"Tanlagan oyingizni nechinchi kunida ketasiz ? ", reply_markup=markup)
    await call.message.delete()
    await Pochta_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Pochta_andijon.kunini_kiritsh)
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


@dp.callback_query_handler(text="Ortga", state=Pochta_andijon.kunini_kiritsh)
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
    await Pochta_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(state=Pochta_andijon.kunini_kiritsh)
async def kunini(call: CallbackQuery, state: FSMContext):
    await state.update_data({"kuni": call.data})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Pochta_andijon.soat.set()


@dp.callback_query_handler(text='Bugun', state=Pochta_andijon.kuni)
@dp.callback_query_handler(text='Ertaga', state=Pochta_andijon.kuni)
@dp.callback_query_handler(text='Indinga', state=Pochta_andijon.kuni)
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
    await Pochta_andijon.soat.set()


@dp.callback_query_handler(text='qaytish', state=Pochta_andijon.aniq_kuni)
async def aniq_ku(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Pochta_andijon.kuni.set()


@dp.callback_query_handler(text='bomenyu', state=Pochta_andijon.aniq_kuni)
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


@dp.callback_query_handler(text='ortga', state=Pochta_andijon.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga pochta olib borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Pochta_andijon.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.kuni)
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


@dp.callback_query_handler(state=Pochta_andijon.aniq_kuni)
async def reys_kuni(call: CallbackQuery, state: FSMContext):
    await state.update_data({"kuni":call.data})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Pochta_andijon.soat.set()


@dp.callback_query_handler(text='ortga', state=Pochta_andijon.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Pochta_andijon.kuni.set()


@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.soat)
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


@dp.callback_query_handler(state=Pochta_andijon.soat)
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
        await Pochta_andijon.phone.set()
    else:
        await call.message.answer("Kechirasiz siz vaqtni noto'g'ri kiritdingiz?")
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Pochta_andijon.kuni.set()


@dp.callback_query_handler(text='tortga', state=Pochta_andijon.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Pochta_andijon.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Pochta_andijon.phone)
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

@dp.message_handler(content_types=['contact', 'text'], state=Pochta_andijon.phone)
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
              f"⏱ <b>{soat}\n</b>" \
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
              f"📆 <b>Qachon yo'lga chiqadi : {kuni}.{oy}</b>\n" \
              f"⏱ <b>{soat}\n</b>\n" \
              f"📞 <b>Tel : {phone}\n</b>"
        await state.update_data(
            {
                "msg": msg, "m": m
            }
        )
    await message.answer(f"Ma'lumotlar to'g'rimi {msg}?", reply_markup=yes_not)
    await Pochta_andijon.tasdiqlash.set()
    await message.delete()


@dp.callback_query_handler(text='ortga', state=Pochta_andijon.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=markup)
    await call.message.delete()
    await Pochta_andijon.phone.set()


@dp.callback_query_handler(text='yesss', state=Pochta_andijon.tasdiqlash)
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
            tayyor_yolovchi=None,
            tayyor_yolovchi_full=None,
            viloyat=viloyat,
            region=tuman,
            telegram_id=telegram_id,
            viloyatga=baza,
            tumanga=tumaniga,
            tayyor_pochta=m,
            tayyor_pochta_full=msg,
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

        offset = -28
        limit = 28
        while True:
            offset += limit
            drivers = await db.select_all_drivers(limit=limit, offset=offset)
            await asyncio.sleep(1)
            for driver in drivers:
                if driver[3] == 'pochta':
                    if driver[4]!=call.from_user.id:
                        async with limiter:
                            markup = InlineKeyboardMarkup(row_width=2)
                            markup.insert(InlineKeyboardButton(text="Qabul qilish",callback_data='qabul'))
                            await bot.send_message(chat_id=driver[4], text=m,reply_markup=markup)
            await call.message.delete()
            await state.finish()
    else:
        await call.message.answer("Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
        await state.finish()

@dp.callback_query_handler(text='nott', state=Pochta_andijon.tasdiqlash)
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


@dp.callback_query_handler(text='add_information', state=Pochta_andijon.tasdiqlash)
async def y_n(call:CallbackQuery, state:FSMContext):
    
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="Qaytish"))
        markup.insert(InlineKeyboardButton(text="Boshmenu",callback_data="Boshmenu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi",callback_data="Keyingisi"))
        await call.message.answer("Sizni topib olishimiz oson bo'lishi uchun lokatsiya yuboring ? ",reply_markup=lokatsiya)
        await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ",reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.locatsiya.set()

@dp.callback_query_handler(state=Pochta_andijon.locatsiya,text="Boshmenu")
async def Boshmenuga(call:CallbackQuery,state:FSMContext):
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


@dp.callback_query_handler(state=Pochta_andijon.locatsiya,text="Qaytish")
async def qaytaman(call:CallbackQuery,state:FSMContext):
    
        await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id-1)
        data=await state.get_data()
        msg=data.get("msg")
        await call.message.answer(f"Malumotlaringiz to'g'rimi ?\n{msg}", reply_markup=yes_not)
        await call.message.delete()
        await Pochta_andijon.tasdiqlash.set()
@dp.callback_query_handler(state=Pochta_andijon.locatsiya,text="Keyingisi")
async def keyingisio(call:CallbackQuery,state:FSMContext):
    
        await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id-1)
        markup=InlineKeyboardMarkup(row_width=3)
        markup.insert(InlineKeyboardButton(text="1",callback_data="bir"))
        markup.insert(InlineKeyboardButton(text="2",callback_data="ikki"))
        markup.insert(InlineKeyboardButton(text="3",callback_data="uch"))
        markup.insert(InlineKeyboardButton(text="4",callback_data="to'rt"))
        markup.insert(InlineKeyboardButton(text="5",callback_data="besh"))
        markup.insert(InlineKeyboardButton(text="Kiritish",callback_data="Kiritish"))
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="Kiritish"))
        markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="Bosh menu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi",callback_data="Keyingisi"))
        await call.message.answer("Nechta pochta yuborasiz ?",reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.necha_kishi.set()
@dp.message_handler(content_types=['location'],state=Pochta_andijon.locatsiya)
async def location(message:Message, state:FSMContext):
    
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 2)
        lat = message.location.latitude
        lon = message.location.longitude
        place = show_on_gmaps.show(lat=lat, lon=lon)
        await state.update_data(
            {
                "location":place
            }
        )
        markup=InlineKeyboardMarkup(row_width=3)
        markup.insert(InlineKeyboardButton(text="1",callback_data="bir"))
        markup.insert(InlineKeyboardButton(text="2",callback_data="ikki"))
        markup.insert(InlineKeyboardButton(text="3",callback_data="uch"))
        markup.insert(InlineKeyboardButton(text="4",callback_data="to'rt"))
        markup.insert(InlineKeyboardButton(text="5",callback_data="besh"))
        markup.insert(InlineKeyboardButton(text="Kiritish",callback_data="Kiritish"))
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="Ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="Bosh menu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi",callback_data="Keyingisi"))
        await message.answer("Nechta pochta yuborasiz ?",reply_markup=markup)
        await message.delete()
        await Pochta_andijon.necha_kishi.set()

@dp.callback_query_handler(state=Pochta_andijon.necha_kishi,text="Bosh menu")
async def qayatdsdsaa(call:CallbackQuery,state:FSMContext):
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

@dp.callback_query_handler(state=Pochta_andijon.necha_kishi,text="Ortga")
async def qayataa(call:CallbackQuery,state:FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytish"))
        markup.insert(InlineKeyboardButton(text="Boshmenu", callback_data="Boshmenu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
        await call.message.answer("Sizni topish oson bo'lishi uchun lokatsiya yuboring !", reply_markup=lokatsiya)
        await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ", reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.locatsiya.set()

@dp.callback_query_handler(state=Pochta_andijon.necha_kishi,text="Keyingisi")
async def kisi(call:CallbackQuery,state:FSMContext):
    
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
        await call.message.answer("Yo'l haqqi uchun qancha olasiz ?", reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.oldi_kerakmi.set()


@dp.callback_query_handler(state=Pochta_andijon.necha_kishi,text="Kiritish")
async def kisi(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Nechta pochta yuborishingizni son orqali ifodalang")
        await call.message.delete()
        await Pochta_andijon.qolda_yozish.set()
@dp.message_handler(state=Pochta_andijon.qolda_yozish)
async def neckakishi(msg:Message,state:FSMContext):
    

        if msg.text.isdigit()==True:
            await state.update_data(
                {
                    "odam_soni": msg.text
                }
            )
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
            await msg.answer("Yo'l haqqi uchun qancha olasiz ?", reply_markup=markup)
            await msg.delete()
            await Pochta_andijon.oldi_kerakmi.set()
        else:
            await msg.answer("Iltimos Son orqali kiriting . Matn kiritmang !!!")
            await msg.delete()
            if msg.message_id - 1:
                await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id - 1)
            await Pochta_andijon.qolda_yozish.set()
@dp.callback_query_handler(state=Pochta_andijon.oldi_kerakmi,text="ortga")
async def kisi(call:CallbackQuery,state:FSMContext):
    
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
        await call.message.answer("Nechta pochta yuborasiz ?", reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.necha_kishi.set()
@dp.callback_query_handler(state=Pochta_andijon.oldi_kerakmi,text="ruchnoy")
async def grjrjfjkj(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Qancha haq bermoqchisiz ")
        await Pochta_andijon.pul_qol.set()
@dp.callback_query_handler(state=Pochta_andijon.necha_kishi)
async def kisi(call:CallbackQuery,state:FSMContext):
    
        print(call.data)
        await state.update_data(
            {
                "odam_soni":call.data
            }
        )
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
        await call.message.answer("Yo'l haqqi uchun qancha berasiz ?", reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.oldi_kerakmi.set()
@dp.callback_query_handler(state=Pochta_andijon.oldi_kerakmi,text="Bosh menu")
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


@dp.callback_query_handler(state=Pochta_andijon.oldi_kerakmi, text="Keyingisi")
async def kisi(call: CallbackQuery, state: FSMContext):
    

        data = await state.get_data()
        msg = data.get("msg")
        lokatsiya = data.get("location")
        odam_soni = data.get("odam_soni")
        if lokatsiya == None:
            lokatsiya = ""
        if odam_soni == None:
            odam_soni = ""
        odam_soni = f"Nechta po'chta yuboradi: {odam_soni}"
        msg_full = msg + f"\n{odam_soni}\n{lokatsiya}"
        await state.update_data(
            {
                "msg_full": msg_full
            }
        )
        await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
        await call.message.delete()
        await Pochta_andijon.end.set()


@dp.callback_query_handler(state=Pochta_andijon.oldi_kerakmi)
async def kisi(call:CallbackQuery,state:FSMContext):
    

        data = await state.get_data()
        msg = data.get("msg")
        lokatsiya = data.get("location")
        odam_soni = data.get("odam_soni")
        yolkira=call.data
        if lokatsiya == None:
            lokatsiya = ""
        if odam_soni == None:
            odam_soni = ""
        odam_soni = f"Nechta po'chta yuboradi: {odam_soni}"
        msg_full = msg + f"\n{odam_soni}\n{lokatsiya}\nHaydovchiga {yolkira} ming so'm bermoqchi"
        await state.update_data(
            {
                "msg_full": msg_full
            }
        )
        await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
        await call.message.delete()
        await Pochta_andijon.end.set()

@dp.message_handler(state=Pochta_andijon.pul_qol)
async def grjrjfjkj(message:Message,state:FSMContext):
    

        data = await state.get_data()
        msg = data.get("msg")
        lokatsiya = data.get("location")
        odam_soni = data.get("odam_soni")
        yolkira = message.text
        if lokatsiya == None:
            lokatsiya = ""
        if odam_soni == None:
            odam_soni = ""
        odam_soni = f"Nechta po'chta yuboradi: {odam_soni}"
        msg_full = msg + f"\n{odam_soni}\n{lokatsiya}\nHaydovchiga {yolkira} ming so'm bermoqchi"
        await state.update_data(
            {
                "msg_full": msg_full
            }
        )
        await message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
        await message.delete()
        await Pochta_andijon.end.set()
@dp.callback_query_handler(text='qaytish',state=Pochta_andijon.end)
async def oxirgi(call:CallbackQuery,state:FSMContext):
    
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
        await call.message.answer("Yo'l haqqi uchun qancha berasiz ?", reply_markup=markup)
        await call.message.delete()
        await Pochta_andijon.oldi_kerakmi.set()
@dp.callback_query_handler(text='glavmenu', state=Pochta_andijon.end)
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

@dp.callback_query_handler(text='Confirm',state=Pochta_andijon.end)
async def oxirgi(call:CallbackQuery,state:FSMContext):
    
        data = await state.get_data()
        tuman = data.get('tuman')
        viloyat = data.get('viloyat')
        tumaniga = data.get('tumaniga')
        baza = data.get('baza')
        print(tuman)
        msg = data.get("msg_full")
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
                tayyor_yolovchi=None,
                tayyor_yolovchi_full=None,
                viloyat=viloyat,
                region=tuman,
                telegram_id=telegram_id,
                viloyatga=baza,
                tumanga=tumaniga,
                tayyor_pochta=m,
                tayyor_pochta_full=msg,
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

            offset = -28
            limit = 28
            while True:
                offset += limit
                drivers = await db.select_all_drivers(limit=limit, offset=offset)
                await asyncio.sleep(1)
                for driver in drivers:
                    if driver[3] == 'pochta':
                        if driver[4] != call.from_user.id:
                            async with limiter:
                                markup = InlineKeyboardMarkup(row_width=2)
                                markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data='qabul'))
                                await bot.send_message(chat_id=driver[4], text=msg, reply_markup=markup)
                await call.message.delete()
                await state.finish()
        else:
            await call.message.answer(
                "Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
            await state.finish()



@dp.callback_query_handler(text='UnConfirm', state=Pochta_andijon.end)
async def y_n(call:CallbackQuery, state:FSMContext):
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

