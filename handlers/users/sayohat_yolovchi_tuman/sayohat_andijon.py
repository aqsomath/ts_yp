import asyncio
import datetime

import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.location import phone_number, lokatsiya
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa
from keyboards.inline.sayohat_qilish.sayohat_viloyatlar import sayohat_vil
from keyboards.inline.yolovchi.andtuman import andijon_yol, qoraqalpogiston_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import tasdiq_oxir, umumiy_menu, kirish
from keyboards.inline.yolovchi.namtuman import namangan_yol
from keyboards.inline.yolovchi.navoiytuman import navoiy_yol
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_yol
from keyboards.inline.yolovchi.samartuman import samarqand_yol
from keyboards.inline.yolovchi.sirtuman import sirdaryo_yol
from keyboards.inline.yolovchi.soat import time
from keyboards.inline.yolovchi.surtuman import surxondaryo_yol
from keyboards.inline.yolovchi.toshtuman import toshkent_yol
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol_x
from keyboards.inline.yolovchi.xa_yoq import yes_not
from keyboards.inline.yolovchi.xorazmtuman import xorazm_yol
from loader import dp, db, bot, limiter
from states.sayohat_states import Sayohat_andijon
from utils.misc import show_on_gmaps


@dp.callback_query_handler(state=Sayohat_andijon.asosiy,text="Ortga")
async def qaytmoq(call:CallbackQuery,state:FSMContext):
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

@dp.callback_query_handler(state=Sayohat_andijon.asosiy,text="Bosh menu")
async def qaytmoq(call:CallbackQuery,state:FSMContext):
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


viloyat = {
    "Andijon":"dushanba",
    "Namangan":"seshanba",
    "Farg'ona":"chorshanba",
    "Buxoro":"payshanba",
    "Toshkent":"juma",
    "Sirdaryo":"shanba",
    "Surxondaryo":"yakshanba",
    "Qashqadaryo":"iyul",
    "Xorazm":"july",
    "Navoiy":"avgust",
    "Jizzax":"sentabr",
    "Samarqand":"oktabr",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"Ortga",
    "Bosh menu":"Bosh menu",
}
for key,value in viloyat.items():
    @dp.callback_query_handler(state=Sayohat_andijon.asosiy)
    async def andijon(call: CallbackQuery, state: FSMContext):
        
            if call.data=='july':
                await state.update_data({"viloyat": "Xorazm"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='dushanba':
                await state.update_data({"viloyat": "Andijon"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=andijon_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='seshanba':
                await state.update_data({"viloyat": "Namangan"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=namangan_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=="chorshanba":
                await state.update_data({"viloyat": "Farg'ona"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=fargona_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='payshanba':
                await state.update_data({"viloyat": "Buxoro"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=buxoro_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='juma':
                await state.update_data({"viloyat": "Toshkent"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=toshkent_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='shanba':
                await state.update_data({"viloyat": "Sirdaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=sirdaryo_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='yakshanba':
                await state.update_data({"viloyat": "Surxondaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=surxondaryo_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='iyul':
                await state.update_data({"viloyat": "Qashqadaryo"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qashqadaryo_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='avgust':
                await state.update_data({"viloyat": "Navoiy"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=navoiy_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='sentabr':
                await state.update_data({"viloyat": "Jizzax"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=jizzax_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='oktabr':
                await state.update_data({"viloyat": "Samarqand"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=samarqand_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
            if call.data=='qoraqalpoq':
                await state.update_data({"viloyat": "Qoraqalpog'iston"})
                await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qoraqalpogiston_yol)
                await call.message.delete()
                await Sayohat_andijon.tuman.set()
@dp.callback_query_handler(text='ortga', state=Sayohat_andijon.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatdan sayohat mashinasi kerak ? ", reply_markup=sayohat_vil)
    await call.message.delete()
    await Sayohat_andijon.asosiy.set()
    await call.message.delete()


#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Sayohat_andijon.tuman)
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

@dp.callback_query_handler(state=Sayohat_andijon.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    

        await state.update_data({"tuman":call.data})
        list_1 = []
        jami = await db.select_all_sayohat_info()
        for i in jami:
            if i[2] == call.from_user.id:
                list_1.append(i[1])

        jamii = await db.select_all_sayohat_info()
        list = []
        for i in jamii:
            if i[2] == call.from_user.id:
                list.append(i[1])
                if "qaytish" in list:
                    list.remove("qaytish")
                if "yakunlash" in list:
                    list.remove("yakunlash")
                if "homeback" in list:
                    list.remove("homeback")
        await state.update_data({"sayohat":list})
        vil = {}
        if "Andijon" in list:
            vil["✅Andijon"] = "Andijon"
        else:
            vil["Andijon"] = "Andijon"
        if "Namangan" in list:
            vil["✅Namangan"] = "Namangan"
        else:
            vil["Namangan"] = "Namangan"
        if "Farg'ona" in list:
            vil["✅Farg'ona"] = "Farg'ona"
        else:
            vil["Farg'ona"] = "Farg'ona"
        if "Buxoro" in list:
            vil["✅Buxoro"] = "Buxoro"
        else:
            vil["Buxoro"] = "Buxoro"
        if "Toshkent" in list:
            vil["✅Toshkent"] = "Toshkent"
        else:
            vil["Toshkent"] = "Toshkent"
        if "Toshkent shahar" in list:
            vil["✅Toshkent shahar"] = "Toshkent shahar"
        else:
            vil["Toshkent shahar"] = "Toshkent shahar"
        if "Sirdaryo" in list:
            vil["✅Sirdaryo"] = "Sirdaryo"
        else:
            vil["Sirdaryo"] = "Sirdaryo"
        if "Surxondaryo" in list:
            vil["✅Surxondaryo"] = "Surxondaryo"
        else:
            vil["Surxondaryo"] = "Surxondaryo"
        if "Qashqadaryo" in list:
            vil["✅Qashqadaryo"] = "Qashqadaryo"
        else:
            vil["Qashqadaryo"] = "Qashqadaryo"
        if "Xorazm" in list:
            vil["✅Xorazm"] = "Xorazm"
        else:
            vil["Xorazm"] = "Xorazm"
        if "Navoiy" in list:
            vil["✅Navoiy"] = "Navoiy"
        else:
            vil["Navoiy"] = "Navoiy"
        if "Jizzax" in list:
            vil["✅Jizzax"] = "Jizzax"
        else:
            vil["Jizzax"] = "Jizzax"
        if "Samarqand" in list:
            vil["✅Samarqand"] = "Samarqand"
        else:
            vil["Samarqand"] = "Samarqand"
        if "qoraqalpoq" in list:
            vil["✅Qoraqalpog'iston"] = "qoraqalpoq"
        else:
            vil["Qoraqalpog'iston"] = "qoraqalpoq"
        vil["Yakunlash"] = "yakunlash"
        vil["Ortga"] = "homeback"
        vil["Buyurtmani bekor qilish"] = "atmen"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=2)
        for key, value in vil.items():
            shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Qaysi viloyatlarga sayohat qilasiz  ? ", reply_markup=shaxsiy_tugma)
        await Sayohat_andijon.viloyatlarni_belgilash.set()
        await call.message.delete()

@dp.callback_query_handler(state=Sayohat_andijon.viloyatlarni_belgilash)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    
        list_1 = []
        jami = await db.select_all_sayohat_info()
        for i in jami:
            if i[2] == call.from_user.id:
                list_1.append(i[1])
        if call.data in list_1:
            await db.delete_sayohat_info(telegram_id=call.from_user.id, viloyat=call.data)
        else:
            await db.add_sayohat_info(telegram_id=call.from_user.id, viloyat=call.data)
        jamii = await db.select_all_sayohat_info()
        list = []
        for i in jamii:
            if i[2] == call.from_user.id:
                list.append(i[1])
                if "qaytish" in list:
                    list.remove("qaytish")
                if "yakunlash" in list:
                    list.remove("yakunlash")
                if "homeback" in list:
                    list.remove("homeback")
        await state.update_data({"sayohat":list})
        vil = {}
        if "Andijon" in list:
            vil["✅Andijon"] = "Andijon"
        else:
            vil["Andijon"] = "Andijon"
        if "Namangan" in list:
            vil["✅Namangan"] = "Namangan"
        else:
            vil["Namangan"] = "Namangan"
        if "Farg'ona" in list:
            vil["✅Farg'ona"] = "Farg'ona"
        else:
            vil["Farg'ona"] = "Farg'ona"
        if "Buxoro" in list:
            vil["✅Buxoro"] = "Buxoro"
        else:
            vil["Buxoro"] = "Buxoro"
        if "Toshkent" in list:
            vil["✅Toshkent"] = "Toshkent"
        else:
            vil["Toshkent"] = "Toshkent"
        if "Toshkent shahar" in list:
            vil["✅Toshkent shahar"] = "Toshkent shahar"
        else:
            vil["Toshkent shahar"] = "Toshkent shahar"
        if "Sirdaryo" in list:
            vil["✅Sirdaryo"] = "Sirdaryo"
        else:
            vil["Sirdaryo"] = "Sirdaryo"
        if "Surxondaryo" in list:
            vil["✅Surxondaryo"] = "Surxondaryo"
        else:
            vil["Surxondaryo"] = "Surxondaryo"
        if "Qashqadaryo" in list:
            vil["✅Qashqadaryo"] = "Qashqadaryo"
        else:
            vil["Qashqadaryo"] = "Qashqadaryo"
        if "Xorazm" in list:
            vil["✅Xorazm"] = "Xorazm"
        else:
            vil["Xorazm"] = "Xorazm"
        if "Navoiy" in list:
            vil["✅Navoiy"] = "Navoiy"
        else:
            vil["Navoiy"] = "Navoiy"
        if "Jizzax" in list:
            vil["✅Jizzax"] = "Jizzax"
        else:
            vil["Jizzax"] = "Jizzax"
        if "Samarqand" in list:
            vil["✅Samarqand"] = "Samarqand"
        else:
            vil["Samarqand"] = "Samarqand"
        if "qoraqalpoq" in list:
            vil["✅Qoraqalpog'iston"] = "qoraqalpoq"
        else:
            vil["Qoraqalpog'iston"] = "qoraqalpoq"
        vil["Yakunlash"] = "yakunlash"
        vil["Ortga"] = "homeback"
        vil["Buyurtmani bekor qilish"] = "atmen"

        shaxsiy_tugma = InlineKeyboardMarkup(row_width=2)
        for key,value in vil.items():
            shaxsiy_tugma.insert(InlineKeyboardButton(text=key,callback_data=value))
        if call.data=="yakunlash":
            await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
            await Sayohat_andijon.kuni.set()
            await call.message.delete()
        if call.data=="homeback":
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
            await Sayohat_andijon.tuman.set()
            await call.message.delete()

        if call.data=="atmen":
            await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?",reply_markup=umumiy_menu)
            await state.finish()
            await call.message.delete()

        for key,value in vil.items():
            if call.data==value:
                await call.message.edit_reply_markup(shaxsiy_tugma)
                await Sayohat_andijon.viloyatlarni_belgilash.set()

@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    
        list_1 = []
        jami = await db.select_all_sayohat_info()
        for i in jami:
            if i[2] == call.from_user.id:
                list_1.append(i[1])

        jamii = await db.select_all_sayohat_info()
        list = []
        for i in jamii:
            if i[2] == call.from_user.id:
                list.append(i[1])
                if "qaytish" in list:
                    list.remove("qaytish")
                if "yakunlash" in list:
                    list.remove("yakunlash")
                if "homeback" in list:
                    list.remove("homeback")
        await state.update_data({"sayohat":list})
        vil = {}
        if "Andijon" in list:
            vil["✅Andijon"] = "Andijon"
        else:
            vil["Andijon"] = "Andijon"
        if "Namangan" in list:
            vil["✅Namangan"] = "Namangan"
        else:
            vil["Namangan"] = "Namangan"
        if "Farg'ona" in list:
            vil["✅Farg'ona"] = "Farg'ona"
        else:
            vil["Farg'ona"] = "Farg'ona"
        if "Buxoro" in list:
            vil["✅Buxoro"] = "Buxoro"
        else:
            vil["Buxoro"] = "Buxoro"
        if "Toshkent" in list:
            vil["✅Toshkent"] = "Toshkent"
        else:
            vil["Toshkent"] = "Toshkent"
        if "Sirdaryo" in list:
            vil["✅Sirdaryo"] = "Sirdaryo"
        else:
            vil["Sirdaryo"] = "Sirdaryo"
        if "Surxondaryo" in list:
            vil["✅Surxondaryo"] = "Surxondaryo"
        else:
            vil["Surxondaryo"] = "Surxondaryo"
        if "Qashqadaryo" in list:
            vil["✅Qashqadaryo"] = "Qashqadaryo"
        else:
            vil["Qashqadaryo"] = "Qashqadaryo"
        if "Xorazm" in list:
            vil["✅Xorazm"] = "Xorazm"
        else:
            vil["Xorazm"] = "Xorazm"
        if "Navoiy" in list:
            vil["✅Navoiy"] = "Navoiy"
        else:
            vil["Navoiy"] = "Navoiy"
        if "Jizzax" in list:
            vil["✅Jizzax"] = "Jizzax"
        else:
            vil["Jizzax"] = "Jizzax"
        if "Samarqand" in list:
            vil["✅Samarqand"] = "Samarqand"
        else:
            vil["Samarqand"] = "Samarqand"
        if "qoraqalpoq" in list:
            vil["✅Qoraqalpog'iston"] = "qoraqalpoq"
        else:
            vil["Qoraqalpog'iston"] = "qoraqalpoq"
        vil["Yakunlash"] = "yakunlash"
        vil["Ortga"] = "homeback"
        vil["Buyurtmani bekor qilish"] = "atmen"
        shaxsiy_tugma = InlineKeyboardMarkup(row_width=2)
        for key, value in vil.items():
            shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Qaysi viloyatlarga borasiz   ? ", reply_markup=shaxsiy_tugma)
        await Sayohat_andijon.viloyatlarni_belgilash.set()
        await call.message.delete()


@dp.callback_query_handler(text="atmen", state=Sayohat_andijon.kuni)
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
@dp.callback_query_handler(text='Qoldakiritish', state=Sayohat_andijon.kuni)
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
    await Sayohat_andijon.oyini_kiritsh.set()
    await call.message.delete()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.oyini_kiritsh)
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


@dp.callback_query_handler(text="Ortga", state=Sayohat_andijon.oyini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await Sayohat_andijon.kuni.set()
        await call.message.delete()


@dp.callback_query_handler(state=Sayohat_andijon.oyini_kiritsh)
async def oyi(call: CallbackQuery, state: FSMContext):
    await state.update_data({"oyi": call.data})
    if int(call.data) < datetime.datetime.now().month:
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
        await call.message.answer("Kechirasiz siz o'tib ketgan oyni kiritingiz!\nQaytadan oyni kiriting.",
                                  reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.oyini_kiritsh.set()
    else:
        markup = InlineKeyboardMarkup(row_width=6)
        for i in range(1, 32):
            markup.insert(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer(f"Tanlagan oyingizni nechinchi kunida ketasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.kunini_kiritsh)
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


@dp.callback_query_handler(text="Ortga", state=Sayohat_andijon.kunini_kiritsh)
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
    await Sayohat_andijon.oyini_kiritsh.set()
    await call.message.delete()


@dp.callback_query_handler(state=Sayohat_andijon.kunini_kiritsh)
async def kunini(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    oy = data.get("oyi")
    oy = int(oy)
    if oy > datetime.datetime.now().month:
        await state.update_data({"sanasi": call.data})
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await call.message.delete()
        await Sayohat_andijon.soat.set()
    if oy == datetime.datetime.now().month:
        if int(call.data) >= datetime.datetime.now().day:
            await state.update_data({"sanasi": call.data})
            await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
            await call.message.delete()
            await Sayohat_andijon.soat.set()
        else:
            markup = InlineKeyboardMarkup(row_width=6)
            for i in range(1, 32):
                markup.insert(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer(
                f"Kechirasiz siz o'tib ketgan kunni belgilandingiz!\nQaytadan kiriting.\nTanlagan oyingizni nechinchi kunida ketasiz ? ",
                reply_markup=markup)
            await call.message.delete()
            await Sayohat_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text='Bugun', state=Sayohat_andijon.kuni)
@dp.callback_query_handler(text='Ertaga', state=Sayohat_andijon.kuni)
@dp.callback_query_handler(text='Indinga', state=Sayohat_andijon.kuni)
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
    await Sayohat_andijon.soat.set()
    await call.message.delete()


@dp.callback_query_handler(text='qaytish', state=Sayohat_andijon.aniq_kuni)
async def aniq_ku(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await Sayohat_andijon.kuni.set()
        await call.message.delete()


@dp.callback_query_handler(text='bomenyu', state=Sayohat_andijon.aniq_kuni)
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


@dp.callback_query_handler(text='ortga', state=Sayohat_andijon.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga sayohat qilasiz ? ", reply_markup=viloyatlar_yol_x)
        await Sayohat_andijon.viloyatga.set()
        await call.message.delete()


@dp.callback_query_handler(text_contains='atmen', state=Sayohat_andijon.kuni)
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


@dp.callback_query_handler(state=Sayohat_andijon.aniq_kuni)
async def reys_kuni(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kuni": call.data
            }
        )
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await Sayohat_andijon.soat.set()
        await call.message.delete()


@dp.callback_query_handler(text='ortga', state=Sayohat_andijon.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await Sayohat_andijon.kuni.set()
        await call.message.delete()


@dp.callback_query_handler(text_contains='atmen', state=Sayohat_andijon.soat)
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


@dp.callback_query_handler(state=Sayohat_andijon.soat)
@dp.callback_query_handler(state=Sayohat_andijon.soat)
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
            await Sayohat_andijon.phone.set()
        else:
            await call.message.answer("Kechirasiz siz vaqtni noto'g'ri kiritdingiz!\nSoat nechchida yo'lga chiqasiz ? ",
                                      reply_markup=time)
            await call.message.delete()
            await Sayohat_andijon.soat.set()


@dp.callback_query_handler(text='ortga', state=Sayohat_andijon.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id-1)
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await Sayohat_andijon.soat.set()
        await call.message.delete()


@dp.callback_query_handler(text_contains='atmen', state=Sayohat_andijon.phone)
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


@dp.message_handler(content_types=['contact', 'text'], state=Sayohat_andijon.phone)
async def reys_loc(message: Message, state: FSMContext):
    

        await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id-2)
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
        tuman = data.get('tuman')
        sayohat = data.get("sayohat")
        oy = data.get('oyi')
        kuni = data.get('kuni')
        soat = data.get('soat')
        phone = data.get('phone')
        xabar= f"🏢 <b>Qaysi viloyatlarga boriladi :</b>\n" + ",".join(sayohat)+"\nViloyatlariga boruvchi sayohat mashinasi\n"
        if oy is not None:
            m = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
                f"🏤 <b>{tuman} </b> \n" \
                f"📆 <b>Sanasi : {kuni}.{oy}</b>\n" \
                f"⏱ <b>{soat}</b>\n" \
                f"🏢 <b>Qaysi viloyatlarga boriladi :</b>\n" + ",".join(sayohat)+"\nViloyatlariga boruvchi sayohat mashinasi\n"

            msg = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
                  f"🏤<b> {tuman} </b> \n" \
                  f"📆 <b>Qachon yo'lga chiqadi : {kuni}.{oy}</b>\n" \
                  f"⏱ <b>{soat}\n</b>" \
                  f"📞 <b>Tel : {phone}</b>\n"\
                  f"🏢 <b>Qaysi viloyatlarga boriladi :</b>\n" + ",".join(sayohat)+"\nViloyatlariga boruvchi sayohat mashinasi\n"
            await state.update_data(
                {
                    "msg": msg, "m": m
                }
            )
        else:
            m = f"🚕\n🏢 <b>{viloyat} \n</b>" \
                f"🏤 <b>{tuman}  </b>\n" \
                f"{xabar}"\
                f"📆 <b>Sanasi : {kuni}.{oy}</b>\n" \
                f"⏱ <b>{soat}</b>\n"
            msg = f"🚕\n🏢 <b>{viloyat} </b>\n" \
                  f"🏤 <b>{tuman}  \n</b>" \
                  f"{xabar}\n"\
                  f"📆 <b>Qachon yo'lga chiqadi :  {kuni}.{oy}</b>\n" \
                  f"⏱ <b>{soat}\n</b>" \
                  f"📞 <b>Tel : {phone}\n</b>"
            await state.update_data(
                {
                    "msg": msg, "m": m
                }
            )
        await message.answer(f"Ma'lumotlar to'g'rimi?\n{msg}", reply_markup=yes_not)
        await message.delete()
        await Sayohat_andijon.tasdiqlash.set()
        await message.delete()


@dp.callback_query_handler(text='ortga', state=Sayohat_andijon.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
        await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
        await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                                  "Kontakt yuborish ni bosing", reply_markup=markup)
        await Sayohat_andijon.phone.set()
        await call.message.delete()


@dp.callback_query_handler(text='yesss', state=Sayohat_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    

        data = await state.get_data()
        tuman = data.get('tuman')
        viloyat = data.get('viloyat')
        tumaniga = data.get('tumaniga')
        baza = data.get('sayohat')
        print(tuman)
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
        if time_difference_seconds>0:
            await db.add_order_tayyor_taxi(
                tayyor_taxi=None,
                tayyor_taxi_full=None,
                tayyor_yolovchi=None,
                tayyor_yolovchi_full=None,
                viloyat=viloyat,
                region=tuman,
                telegram_id=telegram_id,
                viloyatga=",".join(baza),
                tumanga=tumaniga,
                tayyor_pochta=None,
                tayyor_pochta_full=None,
                tayyor_yuk=None,
                tayyor_yuk_full=None,
                tayyor_yuk_haydovchisi=None,
                tayyor_yuk_haydovchisi_full=None,
                tayyor_pochta_mashina=None,
                tayyor_pochta_mashina_full=None,
                tayyor_sayohatchi=m,
                tayyor_sayohatchi_full=msg,
                tayyor_sayohatchi_mashina=None,
                tayyor_sayohatchi_full_mashina=None,
                event_time=end_time,
                kim_tomonidan_qabul_qilindi=None,
                 sana=f"{datetime.date.today()}"



            )



            await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                  "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                                  )
            list_1 = []
            viloyat_jami = await db.select_all_sayohat_info()
            for i in viloyat_jami:
                if i[2] == call.from_user.id:
                    list_1.append(i[1])
            for b in list_1:
                await db.delete_sayohat_info(telegram_id=call.from_user.id, viloyat=b)
            offset = -28
            limit = 28
            while True:
                offset += limit
                drivers = await db.select_all_drivers(limit=limit, offset=offset)
                await asyncio.sleep(1)
                for driver in drivers:
                    if driver[5] == 'sayohat':
                        if driver[4] != call.from_user.id:
                            async with limiter:
                                markup = InlineKeyboardMarkup(row_width=2)
                                markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data='qabul'))
                                await bot.send_message(chat_id=driver[4], text=m, reply_markup=markup)
                await call.message.delete()
                await state.finish()
        else:
            await call.message.answer(
                "Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
            await state.finish()


@dp.callback_query_handler(text='nott', state=Sayohat_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
    haydovchi = await db.select_haydovchi(telegram_id=call.from_user.id)
    if yolovchi is not None:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()
        await state.finish()

    elif haydovchi is not None:
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
        await call.message.answer(f"Salom, {call.message.from_user.full_name}!", reply_markup=kirish)
        await state.finish()


@dp.callback_query_handler(text='add_information', state=Sayohat_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia - 3', callback_data='Nexia - 3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Cobalt', callback_data='Cobalt'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Lacetti', callback_data='Lacetti'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Malibu', callback_data='Malibu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Equinox', callback_data='Equinox'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Trailblazer', callback_data='Trailblazer'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.xa_yoq.set()


@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.xa_yoq)
async def qaytaman(call: CallbackQuery, state: FSMContext):
    
        data = await state.get_data()
        msg = data.get('msg')
        await call.message.answer(f"Ma'lumotlar to'g'rimi\n{msg}?", reply_markup=yes_not)
        await call.message.delete()

        await Sayohat_andijon.tasdiqlash.set()
        await call.message.delete()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.xa_yoq)
async def qaytaman(call: CallbackQuery, state: FSMContext):
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


@dp.callback_query_handler(text="qoldayozish", state=Sayohat_andijon.xa_yoq)
async def qlda_yoz(call: CallbackQuery, state: FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Sizga kerak mashina turini kiriting :", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.qolda_yoz.set()
        await call.message.delete()


@dp.callback_query_handler(text="Keyingisi", state=Sayohat_andijon.xa_yoq)
async def jeieir(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "mashina_turi": "Kiritilmadi"
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'shmi..? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.pochta_olasizmi.set()
        await call.message.delete()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.qolda_yoz)
async def bmenu(call: CallbackQuery, state: FSMContext):
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


@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.qolda_yoz)
async def qol(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia - 3', callback_data='Nexia - 3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Cobalt', callback_data='Cobalt'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Lacetti', callback_data='Lacetti'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Malibu', callback_data='Malibu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Equinox', callback_data='Equinox'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Trailblazer', callback_data='Trailblazer'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.xa_yoq.set()
        await call.message.delete()

@dp.message_handler(state=Sayohat_andijon.qolda_yoz)
async def kisi(message: Message, state: FSMContext):
    
        await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id-1)
        await state.update_data(
            {
                "mashina_turi": message.text
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await message.answer("Kapot bo'sh bo'lsinmi ? ( xa yoki yo'q )", reply_markup=markup)
        await message.delete()

        await Sayohat_andijon.pochta_olasizmi.set()


@dp.callback_query_handler(state=Sayohat_andijon.xa_yoq)
async def kisi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "mashina_turi": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'sh bo'lsinmi ? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.pochta_olasizmi.set()


@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.pochta_olasizmi)
async def sdljf(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia - 3', callback_data='Nexia - 3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Cobalt', callback_data='Cobalt'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Lacetti', callback_data='Lacetti'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Malibu', callback_data='Malibu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Equinox', callback_data='Equinox'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Trailblazer', callback_data='Trailblazer'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Qanday mashina bo'lsin ? :   ", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.xa_yoq.set()
        await call.message.delete()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.pochta_olasizmi)
async def skahh(call: CallbackQuery, state: FSMContext):
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


@dp.callback_query_handler(text="Keyingisi", state=Sayohat_andijon.pochta_olasizmi)
async def reys_pochta_olasizmi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kapot": 'Kiritilmadi'
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'sh bo'lsinmi ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.yuk_olasizmi.set()
        await call.message.delete()


@dp.callback_query_handler(state=Sayohat_andijon.pochta_olasizmi)
async def reys_pochta_olasizmi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kapot": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'sh bo'lsinmi ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.yuk_olasizmi.set()


@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.yuk_olasizmi)
async def kasla(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'sh bo'lsinmi? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.pochta_olasizmi.set()
        await call.message.delete()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.yuk_olasizmi)
async def jasa(call: CallbackQuery, state: FSMContext):
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

@dp.callback_query_handler(text="Keyingisi", state=Sayohat_andijon.yuk_olasizmi)
async def yuk_olasizmi_reys(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "bagaj": "Kiritilmadi"
            }
        )
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='10', callback_data='10'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha kishisizlar ? ", reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.jami_odam.set()
        await call.message.delete()



@dp.callback_query_handler(state=Sayohat_andijon.yuk_olasizmi)
async def yuk_olasizmi_reys(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "bagaj": call.data
            }
        )
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='10', callback_data='10'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha kishisizlar ? ", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.jami_odam.set()
        await call.message.delete()
@dp.callback_query_handler(text="qoldayozish",state=Sayohat_andijon.jami_odam)
async def qolda_kiritish(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Nechta sayohatchi ekaningizni yozma kiriting .")
        await call.message.delete()

        await Sayohat_andijon.qolda_odam_soni.set()
        await call.message.delete()

@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.jami_odam)
async def ksdhkja(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'sh bo'lsinmi ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.yuk_olasizmi.set()
        await call.message.delete()

@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.jami_odam)
async def aljs(call: CallbackQuery, state: FSMContext):
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


@dp.callback_query_handler(text="Keyingisi",state=Sayohat_andijon.jami_odam)
async def ton(call:CallbackQuery,state:FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=4)
        markup.insert(aiogram.types.InlineKeyboardButton(text='80000', callback_data='80000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='100000', callback_data='100000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='120000', callback_data='120000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='150000', callback_data='150000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='170000', callback_data='170000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='200000', callback_data='200000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='220000', callback_data='220000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='250000', callback_data='250000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='300000', callback_data='300000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Yo'l haqqi uchun qancha berasiz ?",reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.locatsiya.set()
        await call.message.delete()

@dp.callback_query_handler(state=Sayohat_andijon.jami_odam)
async def ton(call:CallbackQuery,state:FSMContext):
    
        await state.update_data({"tonna":call.data})
        markup = aiogram.types.InlineKeyboardMarkup(row_width=4)
        markup.insert(aiogram.types.InlineKeyboardButton(text='80000', callback_data='80000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='100000', callback_data='100000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='120000', callback_data='120000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='150000', callback_data='150000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='170000', callback_data='170000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='200000', callback_data='200000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='220000', callback_data='220000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='250000', callback_data='250000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='300000', callback_data='300000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Yo'l haqqi uchun qancha berasiz ?",reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.locatsiya.set()

@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.locatsiya)
async def bosh_menu(call:CallbackQuery,state:FSMContext):
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

@dp.callback_query_handler(text="ortga", state=Sayohat_andijon.locatsiya)
async def ortga_qaytamian(call:CallbackQuery,state:FSMContext):
    
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='10', callback_data='10'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha kishisizlar ? ", reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.jami_odam.set()

@dp.message_handler(state=Sayohat_andijon.qolda_odam_soni)
async def qolda_odam_soni(message:Message,state:FSMContext):
    
        if message.text.isdigit()==True:
            await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id-1)
            await state.update_data({"tonna":message.text})
            markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
            markup.insert(aiogram.types.InlineKeyboardButton(text='80000', callback_data='80000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='100000', callback_data='100000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='120000', callback_data='120000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='150000', callback_data='150000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='170000', callback_data='170000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='200000', callback_data='200000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='220000', callback_data='220000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='250000', callback_data='250000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='300000', callback_data='300000'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
            markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
            markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
            await message.answer("Yo'l haqqi uchun qancha berasiz ?", reply_markup=markup)
            await message.delete()
            await Sayohat_andijon.locatsiya.set()
            await message.delete()
        else:
            await message.answer("Iltimos son bilan kiriting. Matn bilan emas !!!")
            await message.delete()
            await Sayohat_andijon.qolda_odam_soni.set()


@dp.callback_query_handler(text="ruchnoy", state=Sayohat_andijon.locatsiya)
async def pol_ruchnoy(call: CallbackQuery, state: FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("O'zingizning xizmat narxingizni kiriting : ")
        await call.message.delete()

        await Sayohat_andijon.pul_qol.set()
        await call.message.delete()
@dp.callback_query_handler(state=Sayohat_andijon.locatsiya)
async def y_n(call:CallbackQuery, state:FSMContext):
    
        await state.update_data({"yol_haqqi":call.data})
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="Qaytish"))
        markup.insert(InlineKeyboardButton(text="Boshmenu",callback_data="Boshmenu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi",callback_data="Keyingisi"))
        await call.message.answer("Sizni topib olishimiz oson bo'lishi uchun lokatsiya yuboring ? ",reply_markup=lokatsiya)
        await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ",reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.odam.set()


@dp.callback_query_handler(text="Boshmennu", state=Sayohat_andijon.odam)
async def kasaas(call: CallbackQuery, state: FSMContext):
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
@dp.callback_query_handler(text="Qaytish", state=Sayohat_andijon.odam)
async def kasaas(call: CallbackQuery, state: FSMContext):
    
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
        markup = aiogram.types.InlineKeyboardMarkup(row_width=4)
        markup.insert(aiogram.types.InlineKeyboardButton(text='80000', callback_data='80000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='100000', callback_data='100000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='120000', callback_data='120000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='150000', callback_data='150000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='170000', callback_data='170000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='200000', callback_data='200000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='220000', callback_data='220000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='250000', callback_data='250000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='300000', callback_data='300000'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))

        await call.message.answer("Yo'l haqqi uchun qancha berasiz ? ", reply_markup=markup)
        await call.message.delete()

        await Sayohat_andijon.locatsiya.set()


@dp.callback_query_handler(text="boshmenu", state=Sayohat_andijon.odam_vil)
async def asla(call: CallbackQuery, state: FSMContext):
    
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
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

@dp.message_handler(state=Sayohat_andijon.pul_qol)
async def sjhsdfhs(message:Message,state:FSMContext):
    
        await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id-1)
        await state.update_data({"yol_haqqi": message.text})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytish"))
        markup.insert(InlineKeyboardButton(text="Boshmenu", callback_data="Boshmenu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
        await message.answer("Sizni topib olishimiz oson bo'lishi uchun lokatsiya yuboring ? ", reply_markup=lokatsiya)
        await message.answer("Kerak bo'lmasa keyingisini bosing ? ", reply_markup=markup)
        await message.delete()
        await Sayohat_andijon.odam.set()


@dp.callback_query_handler(state=Sayohat_andijon.odam,text="Keyingisi")
async def sjhsdfhs(call:CallbackQuery,state:FSMContext):
    

        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
        data = await state.get_data()
        msg = data.get("msg")
        mashina_turi = data.get('mashina_turi')
        mashina = f"🚚 <b>Qanaqa mashina kerak : {mashina_turi}</b>\n"
        if mashina_turi == "Kiritilmadi":
            mashina = ""
        yol_haqqi = data.get("yol_haqqi")
        yolkira = f"💲 <b>Yo'l haqqi: {yol_haqqi}</b>\n"
        if yol_haqqi == "Kiritilmadi":
            yolkira = ""
        kapot = data.get("kapot")
        kap = f"⁉️ <b>Kapot bo'sh bo'lsinmi ? - {kapot}</b>\n"
        if kapot == "Kiritilmadi":
            kap = ""
        bagaj = data.get("bagaj")
        bag = f"⁉️ <b>Bagaj bo'sh bo'lsinmi ? - {bagaj}</b>\n"
        if bagaj == "Kiritilmadi":
            bag = ""
        tonna = data.get("tonna")
        ton = f"⁉️ <b>Sayohatchilar soni ? - {tonna}</b>\n"
        if tonna is None:
            ton = ""
        msg_full = msg + f"{mashina}" \
                         f"{kap}" \
                         f"{bag}" \
                         f"{ton}" \
                         f"{yolkira}" \

        await state.update_data(
            {
                "msg_full": msg_full
            }
        )
        await call.message.answer(f"Ma'lumotar to'g'rimi ?\n{msg_full}", reply_markup=tasdiq_oxir)
        await Sayohat_andijon.end.set()
        await call.message.delete()

@dp.message_handler(state=Sayohat_andijon.odam)
async def sjhsdfhs(message:Message,state:FSMContext):
    

        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id - 2)
        lat = message.location.latitude
        lon = message.location.longitude
        place = show_on_gmaps.show(lat=lat, lon=lon)
        await state.update_data(
            {
                "location": place
            }
        )
        data = await state.get_data()
        msg = data.get("msg")
        mashina_turi = data.get('mashina_turi')
        mashina = f"🚚 <b>Qanaqa mashina kerak : {mashina_turi}</b>\n"
        if mashina_turi == "Kiritilmadi":
            mashina = ""
        yol_haqqi = data.get("yol_haqqi")
        yolkira = f"💲 <b>Yo'l haqqi: {yol_haqqi}</b>\n"
        if yol_haqqi == "Kiritilmadi":
            yolkira = ""
        kapot = data.get("kapot")
        kap = f"⁉️ <b>Kapot bo'sh bo'lsinmi ? - {kapot}</b>\n"
        if kapot == "Kiritilmadi":
            kap = ""
        bagaj = data.get("bagaj")
        bag = f"⁉️ <b>Bagaj bo'sh bo'lsinmi ? - {bagaj}</b>\n"
        if bagaj == "Kiritilmadi":
            bag = ""
        tonna = data.get("tonna")
        ton = f"⁉️ <b>Sayohatchilar soni ? - {tonna}</b>\n"
        if tonna is None:
            ton = ""
        msg_full = msg + f"{mashina}" \
                         f"{kap}" \
                         f"{bag}" \
                         f"{ton}" \
                         f"{yolkira}" \
                         f"Sayohatchining lokatsiyasi \n{place}"

        await state.update_data(
            {
                "msg_full": msg_full
            }
        )
        await message.answer(f"Ma'lumotar to'g'rimi ?\n{msg_full}", reply_markup=tasdiq_oxir)
        await Sayohat_andijon.end.set()
        await message.delete()
@dp.callback_query_handler(text='qaytish', state=Sayohat_andijon.end)
async def qayiys(call: CallbackQuery, state: FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Qaytish"))
        markup.insert(InlineKeyboardButton(text="Boshmenu", callback_data="Boshmenu"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="Keyingisi"))
        await call.message.answer("Sizni topib olishimiz oson bo'lishi uchun lokatsiya yuboring ? ", reply_markup=lokatsiya)
        await call.message.answer("Kerak bo'lmasa keyingisini bosing ? ", reply_markup=markup)
        await call.message.delete()
        await Sayohat_andijon.odam.set()


@dp.callback_query_handler(text='glavmenu', state=Sayohat_andijon.end)
async def boshmenuga(call: CallbackQuery, state: FSMContext):
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

@dp.callback_query_handler(text='Confirm', state=Sayohat_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    
        data = await state.get_data()
        tuman = data.get('tuman')
        viloyat = data.get('viloyat')
        tumaniga = data.get('tumaniga')
        baza = data.get('sayohat')
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
                tayyor_pochta=None,
                tayyor_pochta_full=None,
                tayyor_yuk=None,
                tayyor_yuk_full=None,
                tayyor_yuk_haydovchisi=None,
                tayyor_yuk_haydovchisi_full=None,
                tayyor_pochta_mashina=None,
                tayyor_pochta_mashina_full=None,
                tayyor_sayohatchi=m,
                tayyor_sayohatchi_full=msg,
                tayyor_sayohatchi_mashina=None,
                tayyor_sayohatchi_full_mashina=None,
                event_time=end_time,
                kim_tomonidan_qabul_qilindi=None,
                 sana=f"{datetime.date.today()}"



            )

            await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                      "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                                      )
            list_1 = []
            viloyat_jami = await db.select_all_sayohat_info()
            for i in viloyat_jami:
                if i[2] == call.from_user.id:
                    list_1.append(i[1])
            for b in list_1:
                await db.delete_sayohat_info(telegram_id=call.from_user.id, viloyat=b)
            offset = -28
            limit = 28
            while True:
                offset += limit
                drivers = await db.select_all_drivers(limit=limit, offset=offset)
                await asyncio.sleep(1)
                for driver in drivers:
                    if driver[5] == 'sayohat':
                        if driver[4] != call.from_user.id:
                            async with limiter:
                                markup = InlineKeyboardMarkup(row_width=2)
                                markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data='qabul'))
                                await bot.send_message(chat_id=driver[4], text=m, reply_markup=markup)
                await call.message.delete()
                await state.finish()
        else:
            await call.message.answer(
                "Kechirasiz siz o'tib ketgan vaqtni belgiladingiz, vaqt belgilashda xatolikka yo'l qo'yilgan. Tekshirib qaytadan kiriting")
            await state.finish()



@dp.callback_query_handler(text='UnConfirm', state=Sayohat_andijon.end)
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