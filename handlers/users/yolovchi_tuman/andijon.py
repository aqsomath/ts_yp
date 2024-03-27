import asyncio

import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.location import lokatsiya, phone_number
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa
from keyboards.inline.yolovchi.andtuman import andijon_yol, qoraqalpogiston_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import umumiy_menu, tasdiq_oxir
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


#  1 - ORTGA
@dp.callback_query_handler(text_contains='Bosh menu', state=Yolovchi_andijon.asosiy)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(text_contains='ortga', state=Yolovchi_andijon.asosiy)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(text='Qoldakiritish', state=Yolovchi_andijon.kuni)
async def qolda_yozing(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=6)
    markup.insert(InlineKeyboardButton(text="Yanvar", callback_data="Yanvar"))
    markup.insert(InlineKeyboardButton(text="Fevral", callback_data="Fevral"))
    markup.insert(InlineKeyboardButton(text="Mart", callback_data="Mart"))
    markup.insert(InlineKeyboardButton(text="Aprel", callback_data="Aprel"))
    markup.insert(InlineKeyboardButton(text="May", callback_data="May"))
    markup.insert(InlineKeyboardButton(text="Iyun", callback_data="Iyun"))
    markup.insert(InlineKeyboardButton(text="Iyul", callback_data="Iyul"))
    markup.insert(InlineKeyboardButton(text="Avgust", callback_data="Avgust"))
    markup.insert(InlineKeyboardButton(text="Sentabr", callback_data="Sentabr"))
    markup.insert(InlineKeyboardButton(text="Oktabr", callback_data="Oktabr"))
    markup.insert(InlineKeyboardButton(text="Noyabr", callback_data="Noyabr"))
    markup.insert(InlineKeyboardButton(text="Dekabr", callback_data="Dekabr"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer("Qaysi oyda yo'lga chiqasiz ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yolovchi_andijon.oyini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer(f"{call.data} oyining qaysi kunida ketasiz ? ", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yolovchi_andijon.kunini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(text="Ortga", state=Yolovchi_andijon.kunini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup(row_width=6)
    markup.insert(InlineKeyboardButton(text="Yanvar", callback_data="Yanvar"))
    markup.insert(InlineKeyboardButton(text="Fevral", callback_data="Qoldakiritish"))
    markup.insert(InlineKeyboardButton(text="Mart", callback_data="Mart"))
    markup.insert(InlineKeyboardButton(text="Aprel", callback_data="Aprel"))
    markup.insert(InlineKeyboardButton(text="May", callback_data="May"))
    markup.insert(InlineKeyboardButton(text="Iyun", callback_data="Iyun"))
    markup.insert(InlineKeyboardButton(text="Iyul", callback_data="Iyul"))
    markup.insert(InlineKeyboardButton(text="Avgust", callback_data="Avgust"))
    markup.insert(InlineKeyboardButton(text="Sentabr", callback_data="Sentabr"))
    markup.insert(InlineKeyboardButton(text="Oktabr", callback_data="Oktabr"))
    markup.insert(InlineKeyboardButton(text="Noyabr", callback_data="Noyabr"))
    markup.insert(InlineKeyboardButton(text="Dekabr", callback_data="Dekabr"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    await call.message.answer("Qaysi oyda yo'lga chiqasiz ?", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(state=Yolovchi_andijon.kunini_kiritsh)
async def kunini(call: CallbackQuery, state: FSMContext):
    await state.update_data({"sanasi": call.data})
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text='Bugun', state=Yolovchi_andijon.kuni)
@dp.callback_query_handler(text='Ertaga', state=Yolovchi_andijon.kuni)
@dp.callback_query_handler(text='Indinga', state=Yolovchi_andijon.kuni)
async def oy(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "kuni": call.data
        }
    )
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
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(text='ortga', state=Yolovchi_andijon.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga pochta olib borasiz ? ", reply_markup=viloyatlar_yol_x)
    await call.message.delete()
    await Yolovchi_andijon.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.kuni)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.aniq_kuni)
async def reys_kuni(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "kuni": call.data
        }
    )
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
    await call.message.answer("Salom yo'lovchi\n"
                              "Sizga kerakli hizmat turini belgilang ?",
                              reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.soat)
async def reys_soat(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "soat": call.data
        }
    )
    markup = aiogram.types.InlineKeyboardMarkup(row_width=3, )
    markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
    markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
    await call.message.answer("Sizga bog'lanishimiz uchun", reply_markup=phone_number)
    await call.message.answer("Telefon raqamingizni kiriting ..\nMana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=markup)
    await call.message.delete()
    await Yolovchi_andijon.phone.set()


@dp.callback_query_handler(text='tortga', state=Yolovchi_andijon.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await call.message.delete()
    await Yolovchi_andijon.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Yolovchi_andijon.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
    sanasi = data.get('sanasi')
    soat = data.get('soat')
    phone = data.get('phone')
    if oy is not None:
        m = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
            f"🏤 <b>{tuman}dan </b> \n" \
            f"🏢 <b>{viloyatiga} \n" \
            f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi</b>\n" \
            f"📆 <b>Sanasi : {sanasi}-{oy}</b>\n" \
            f"⏱ <b>{soat}</b>\n"
        msg = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
              f"🏤<b> {tuman} dan </b> \n" \
              f"🏢<b> {viloyatiga} </b>\n" \
              f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi </b>\n" \
              f"📆 <b>Qachon yo'lga chiqadi : {sanasi}-{oy}</b>\n" \
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
            f"📆 <b>Sanasi : {kuni}</b>\n" \
            f"⏱ <b>{soat}</b>\n"
        msg = f"🚕\n🏢 <b>{viloyat}  </b>\n" \
              f"🏤 <b>{tuman}dan \n</b>" \
              f"🏢 <b>{viloyatiga} \n</b>" \
              f"🏪 <b>{tumaniga} ga boruvchi yo'lovchi</b>\n" \
              f"📆 <b>Qachon yo'lga chiqadi :  {kuni}</b>\n" \
              f"⏱ <b>{soat}\n</b>" \
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
    print(tuman)
    msg = data.get("msg")
    m = data.get("m")
    telegram_id = call.from_user.id
    print(telegram_id)
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
        tayyor_sayohatchi_full_mashina=None

    )

    await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    order = await db.select_order(tayyor_yolovchi_full=msg)
    print(order)
    offset = -28
    limit = 28
    while True:
        offset += limit
        drivers = await db.select_all_drivers(limit=limit, offset=offset)
        await asyncio.sleep(1)
        for driver in drivers:
            if driver[1] == 'odam':
                async with limiter:
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data=f'qabul_flkk_{order[0]}'))
                    await bot.send_message(chat_id=driver[4], text=m, reply_markup=markup)
        await state.update_data({"msg":msg})
        await call.message.delete()
        await state.reset_state(with_data=True)


@dp.callback_query_handler(text='nott', state=Yolovchi_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await call.message.delete()
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
            "location": place
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
    await call.message.answer("Salom yo'lovchi sizga kerakli hizmat turini tanlang !", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom yo'lovchi sizga kerakli hizmat turini tanlang !", reply_markup=umumiy_menu)
    await call.message.delete()
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
    await call.message.answer("Salom yo'lovchi sizga kerakli hizmat turini tanlang !", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()


@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina, text="Keyingisi")
async def kisi(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg")
    lokatsiya = data.get("location")
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    odam_soni = f"Necha kishi ketadi: {odam_soni}"
    if lokatsiya == None:
        lokatsiya = ""
    if odam_soni == None:
        odam_soni = ""
    if oldi_orin == None:
        oldi_orin = ""
    msg_full = msg + f"\n{odam_soni}\n{oldi_orin}\n{lokatsiya}"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
    await call.message.delete()
    await Yolovchi_andijon.end.set()


@dp.callback_query_handler(state=Yolovchi_andijon.qanday_moshina)
async def kisi(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "Avto_turi": call.data
        }
    )
    data = await state.get_data()
    msg = data.get("msg")
    lokatsiya = data.get("location")
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    avto_turi = data.get("Avto_turi")
    odam_soni = f"Necha kishi ketadi: {odam_soni}"
    avto_turi = f"Qanday avto kerak : {avto_turi}"
    if lokatsiya == None:
        lokatsiya = ""
    if odam_soni == None:
        odam_soni = ""
    if oldi_orin == None:
        oldi_orin = ""
    if avto_turi == None:
        avto_turi = ""
    msg_full = msg + f"\n{odam_soni}\n{oldi_orin}\n{avto_turi}\n{lokatsiya}"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await call.message.answer(f"Ma'lumotlaringiz to'g'rimi ?\n{msg_full} ", reply_markup=tasdiq_oxir)
    await call.message.delete()
    await Yolovchi_andijon.end.set()


@dp.callback_query_handler(text='qaytish', state=Yolovchi_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
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


@dp.callback_query_handler(text='glavmenu', state=Yolovchi_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi sizga kerakli hizmat turini tanlang !", reply_markup=umumiy_menu)
    await call.message.delete()
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
    m = data.get("m")
    telegram_id = call.message.from_user.id
    print(telegram_id)
    await db.add_order_tayyor_taxi(tayyor_taxi=None,
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
                                   tayyor_sayohatchi_full_mashina=None,
                                   tayyor_sayohatchi_mashina=None)

    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )

    offset = -28
    limit = 28
    while True:
        offset += limit
        drivers = await db.select_all_drivers(limit=limit, offset=offset)
        await asyncio.sleep(1)
        for driver in drivers:
            if driver[1] == 'odam':
                async with limiter:
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data='qabul'))
                    await bot.send_message(chat_id=driver[4], text=msg, reply_markup=markup)
        await call.message.delete()
        await state.finish()


@dp.callback_query_handler(text='UnConfirm', state=Yolovchi_andijon.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await call.message.delete()
    await state.finish()
