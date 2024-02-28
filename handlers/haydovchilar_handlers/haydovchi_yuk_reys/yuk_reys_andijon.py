import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.location import phone_number
from keyboards.inline.haydovchi_reys.haydovchi_pochta_reys import taxi_pochta_callback, tax_pochta_vil
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa, tax_resy_vil
from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import taxi_yuk_callback, tax_yuk_vil
from keyboards.inline.yolovchi.andtuman import andijon_yol, tosh_shsha,qoraqalpogiston_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import tasdiq_oxir, umumiy_menu_1
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
from loader import dp, db, bot
from states.yuk_reys_states import Yuk_reys_andijon


@dp.callback_query_handler(state=Yuk_reys_andijon.asosiy)
async def andijon_yuk(call: CallbackQuery, state: FSMContext):
    
        if call.data == 'february':
            await state.update_data({"viloyat": "Xorazm"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'monday':
            await state.update_data({"viloyat": "Andijon"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=andijon_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'tuesday':
            await state.update_data({"viloyat": "Namangan"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=namangan_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'wenesday':
            await state.update_data({"viloyat": "Farg'ona"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=fargona_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'thursday':
            await state.update_data({"viloyat": "Buxoro"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=buxoro_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'friday':
            await state.update_data({"viloyat": "Toshkent"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=toshkent_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'kent shahar':
            await state.update_data({"viloyat": "Toshkent shahar"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=tosh_shsha)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'saturday':
            await state.update_data({"viloyat": "Sirdaryo"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=sirdaryo_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'sunday':
            await state.update_data({"viloyat": "Surxondaryo"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=surxondaryo_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'january':
            await state.update_data({"viloyat": "Qashqadaryo"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qashqadaryo_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'february':
            await state.update_data({"viloyat": "Xorazm"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=xorazm_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'march':
            await state.update_data({"viloyat": "Navoiy"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=navoiy_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'june':
            await state.update_data({"viloyat": "Jizzax"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=jizzax_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'july':
            await state.update_data({"viloyat": "Samarqand"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=samarqand_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()
        if call.data == 'qoraqalpoq':
            await state.update_data({"viloyat": "Qoraqalpog'iston"})
            await call.message.answer("Qaysi tumandan yuk yuborasiz ? ", reply_markup=qoraqalpogiston_yol)
            await call.message.delete()
            await Yuk_reys_andijon.tuman.set()

@dp.callback_query_handler(text='ortga', state=Yuk_reys_andijon.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatlardan yuk olasiz ? ", reply_markup=tax_yuk_vil)
        await Yuk_reys_andijon.asosiy.set()
        await call.message.delete()

#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.tuman)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "tuman": call.data
            }
        )
        await call.message.answer("Qaysi viloyatga  borasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Yuk_reys_andijon.viloyatga.set()


@dp.callback_query_handler(text='homeback', state=Yuk_reys_andijon.viloyatga)
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
        if viloyat == "Toshkent shahar":
            await call.message.answer("Qaysi tumanidan yuk yuborasiz ? ", reply_markup=tosh_shsha)
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
        await Yuk_reys_andijon.tuman.set()


@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.viloyatga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.viloyatga)
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
        if data == 'kent shahar':
            await state.update_data(
                {"viloyatiga": "Toshkent shahar"}
            )
            await call.message.answer("Qaysi tumaniga borasiz", reply_markup=tosh_shsha)
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
        await state.update_data({"baza": data})
        await call.message.delete()
        await Yuk_reys_andijon.tumaniga.set()
@dp.callback_query_handler(text='ortga', state=Yuk_reys_andijon.tumaniga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga borasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Yuk_reys_andijon.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.tumaniga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.tumaniga)
async def reys_tumaniga(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "tumaniga": call.data.capitalize()
            }
        )
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Yuk_reys_andijon.kuni.set()


@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga borasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Yuk_reys_andijon.viloyatga.set()


@dp.callback_query_handler(text="atmen", state=Yuk_reys_andijon.kuni)
async def taqas(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text='Qoldakiritish', state=Yuk_reys_andijon.kuni)
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
        await Yuk_reys_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.oyini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text="Ortga", state=Yuk_reys_andijon.oyini_kiritsh)
async def qayyt(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Yuk_reys_andijon.kuni.set()


@dp.callback_query_handler(state=Yuk_reys_andijon.oyini_kiritsh)
async def oyi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data({"oyi": call.data})
        markup = InlineKeyboardMarkup(row_width=6)
        for i in range(1, 32):
            markup.insert(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="Ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer(f"{call.data} oyining qaysi kunida ketasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.kunini_kiritsh.set()


@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.kunini_kiritsh)
async def bosh(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text="Ortga", state=Yuk_reys_andijon.kunini_kiritsh)
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
        await Yuk_reys_andijon.oyini_kiritsh.set()


@dp.callback_query_handler(state=Yuk_reys_andijon.kunini_kiritsh)
async def kunini(call: CallbackQuery, state: FSMContext):
    
        await state.update_data({"sanasi": call.data})
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await call.message.delete()
        await Yuk_reys_andijon.soat.set()


@dp.callback_query_handler(text='Bugun', state=Yuk_reys_andijon.kuni)
@dp.callback_query_handler(text='Ertaga', state=Yuk_reys_andijon.kuni)
@dp.callback_query_handler(text='Indinga', state=Yuk_reys_andijon.kuni)
async def oy(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kuni": call.data
            }
        )
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await call.message.delete()
        await Yuk_reys_andijon.soat.set()


@dp.callback_query_handler(text='qaytish', state=Yuk_reys_andijon.aniq_kuni)
async def aniq_ku(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
    await call.message.delete()
    await Yuk_reys_andijon.kuni.set()


@dp.callback_query_handler(text='bomenyu', state=Yuk_reys_andijon.aniq_kuni)
async def menu_bosh(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text='ortga', state=Yuk_reys_andijon.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qaysi viloyatga yuk olib borasiz ? ", reply_markup=viloyatlar_yol_x)
        await call.message.delete()
        await Yuk_reys_andijon.viloyatga.set()

@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.kuni)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.aniq_kuni)
async def reys_kuni(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kuni": call.data
            }
        )
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await call.message.delete()
        await Yuk_reys_andijon.soat.set()


@dp.callback_query_handler(text='ortga', state=Yuk_reys_andijon.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Qachon yo'lga chiqasiz ?", reply_markup=reys_ortgaa)
        await call.message.delete()
        await Yuk_reys_andijon.kuni.set()


@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.soat)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom yo'lovchi\n"
                                  "Sizga kerakli hizmat turini belgilang ?",
                                  reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.soat)
async def reys_soat(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "soat": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3,)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
        await call.message.answer("Sizga bog'lanishimiz uchun", reply_markup=phone_number)
        await call.message.answer("Telefon raqamingizni kiriting ..\nMana shu raqamni ishlatayotgan bo'lsangiz\n"
                                       "Kontakt yuborish ni bosing", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.phone.set()


@dp.callback_query_handler(text='tortga', state=Yuk_reys_andijon.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
        await call.message.delete()
        await Yuk_reys_andijon.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Yuk_reys_andijon.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.message_handler(content_types=['contact', 'text'], state=Yuk_reys_andijon.phone)
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
                f"🏪 <b>{tumaniga} ga boruvchi yuk mashina</b>\n" \
                f"📆 <b>Sanasi : {sanasi}-{oy}</b>\n" \
                f"⏱ <b>{soat}</b>\n"
            msg = f"🚕\n<b> 🏢 {viloyat} </b>\n" \
                  f"🏤<b> {tuman} dan </b> \n" \
                  f"🏢<b> {viloyatiga} </b>\n" \
                  f"🏪 <b>{tumaniga} ga boruvchi yuk mashina </b>\n" \
                  f"📆 <b>Qachon yo'lga chiqadi : {sanasi}-{oy}</b>\n" \
                  f"⏱ <b>{soat}\n</b>" \
                  f"📞 <b>Tel : {phone}</b>\n"
            await state.update_data(
                {
                    "msg": msg, "m": m
                }
            )
        else:
            m = f"🚕🏢 <b>{viloyat} \n</b>" \
                f"🏤 <b>{tuman}dan  </b>\n" \
                f"🏢 <b>{viloyatiga} </b>\n" \
                f"🏪 <b>{tumaniga} ga boruvchi yuk mashina </b>\n" \
                f"📆 <b>Sanasi : {kuni}</b>\n" \
                f"⏱ <b>{soat}</b>\n"
            msg = f"🚕\n🏢 <b>{viloyat}  </b>\n" \
                  f"🏤 <b>{tuman}dan \n</b>" \
                  f"🏢 <b>{viloyatiga} \n</b>" \
                  f"🏪 <b>{tumaniga} ga boruvchi yuk mashina</b>\n" \
                  f"📆 <b>Qachon yo'lga chiqadi :  {kuni}</b>\n" \
                  f"⏱ <b>{soat}\n</b>" \
                  f"📞 <b>Tel : {phone}\n</b>"
            await state.update_data(
                {
                    "msg": msg, "m": m
                }
            )
        await bot.delete_message(chat_id=message.from_user.id,message_id=message.message_id)
        await message.answer(f"Ma'lumotlar to'g'rimi {msg}?", reply_markup=yes_not)
        await Yuk_reys_andijon.tasdiqlash.set()
        await message.delete()

@dp.callback_query_handler(text='ortga', state=Yuk_reys_andijon.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='tortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='atmen'))
        await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
        await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                                  "Kontakt yuborish ni bosing", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.phone.set()


@dp.callback_query_handler(text='yesss', state=Yuk_reys_andijon.tasdiqlash)
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
            tayyor_yuk_haydovchisi=m,
            tayyor_yuk_haydovchisi_full=msg,
            tayyor_pochta_mashina=None,
            tayyor_pochta_mashina_full=None,
            tayyor_sayohatchi=None,
            tayyor_sayohatchi_full=None,
            tayyor_sayohatchi_mashina=None,
            tayyor_sayohatchi_full_mashina=None

        )
        print("Qo'shildi")
        order = await db.select_tayyor_pochta_mashina()
        print(order)
        await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                  "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu_1
                                  )
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text='nott', state=Yuk_reys_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text='add_information', state=Yuk_reys_andijon.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil', callback_data='Zil'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kamaz', callback_data='Kamaz'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil 53', callback_data='Zil 53'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='HOVO', callback_data='HOVO'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='CHACKMAN', callback_data='CHACKMAN'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Labo', callback_data='Labo'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='KIA', callback_data='KIA'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Mashinangiz qanday ? :   ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.xa_yoq.set()
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.xa_yoq)
async def qaytaman(call: CallbackQuery, state: FSMContext):
    
        data = await state.get_data()
        msg = data.get('msg')
        await call.message.answer(f"Ma'lumotlar to'g'rimi?\n{msg}", reply_markup=yes_not)
        await call.message.delete()
        await Yuk_reys_andijon.tasdiqlash.set()
@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.xa_yoq)
async def qaytaman(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text="qoldayozish", state=Yuk_reys_andijon.xa_yoq)
async def qlda_yoz(call: CallbackQuery, state: FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=3)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("Mashinangiz Turini kiriting :", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.qolda_yoz.set()
@dp.callback_query_handler(text="Keyingisi", state=Yuk_reys_andijon.xa_yoq)
async def jeieir(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "mashina_turi": "Kiritilmadi"
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'shmi..? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.pochta_olasizmi.set()


@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.qolda_yoz)
async def bmenu(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.qolda_yoz)
async def qol(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil', callback_data='Zil'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kamaz', callback_data='Kamaz'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil 53', callback_data='Zil 53'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='HOVO', callback_data='HOVO'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='CHACKMAN', callback_data='CHACKMAN'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Labo', callback_data='Labo'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='KIA', callback_data='KIA'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Mashinangiz qanday ? :   ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.xa_yoq.set()

@dp.message_handler(state=Yuk_reys_andijon.qolda_yoz)
async def kisi(message: Message, state: FSMContext):
    
        await state.update_data(
            {
                "mashina_turi": message.text
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await message.answer("Kapot bo'shmi..? ( xa yoki yo'q )", reply_markup=markup)
        await message.delete()
        await Yuk_reys_andijon.pochta_olasizmi.set()
@dp.callback_query_handler(state=Yuk_reys_andijon.xa_yoq)
async def kisi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "mashina_turi": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'shmi..? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.pochta_olasizmi.set()
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.pochta_olasizmi)
async def sdljf(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil', callback_data='Zil'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kamaz', callback_data='Kamaz'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Zil 53', callback_data='Zil 53'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='HOVO', callback_data='HOVO'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='CHACKMAN', callback_data='CHACKMAN'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Labo', callback_data='Labo'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='KIA', callback_data='KIA'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Mashinangiz qanday ? :   ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.xa_yoq.set()


@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.pochta_olasizmi)
async def skahh(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(text="Keyingisi", state=Yuk_reys_andijon.pochta_olasizmi)
async def reys_pochta_olasizmi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kapot": 'Kiritilmadi'
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'shmi.. ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.yuk_olasizmi.set()


@dp.callback_query_handler(state=Yuk_reys_andijon.pochta_olasizmi)
async def reys_pochta_olasizmi(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "kapot": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'shmi.. ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.yuk_olasizmi.set()
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.yuk_olasizmi)
async def kasla(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Kapot bo'shmi..? ( xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.pochta_olasizmi.set()
@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.yuk_olasizmi)
async def jasa(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text="Keyingisi", state=Yuk_reys_andijon.yuk_olasizmi)
async def yuk_olasizmi_reys(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "bagaj": "Kiritilmadi"
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='10', callback_data='10'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha tonnagacha yuk olasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.jami_odam.set()
@dp.callback_query_handler(state=Yuk_reys_andijon.yuk_olasizmi)
async def yuk_olasizmi_reys(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "bagaj": call.data
            }
        )
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='10', callback_data='10'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha tonnagacha yuk olasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.jami_odam.set()
@dp.callback_query_handler(text="qoldayozish",state=Yuk_reys_andijon.jami_odam)
async def qolda_kiritish(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Nechta tonna olishingizni yozma kiriting .")
        await call.message.delete()
        await Yuk_reys_andijon.qolda_odam_soni.set()
@dp.message_handler(state=Yuk_reys_andijon.qolda_odam_soni)
async def qolda_odam_soni(message:Message,state:FSMContext):
    

        if message.text.isdigit()==True:
            await state.update_data({"tonna":message.text})
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
            await message.answer("Yo'l haqqi uchun qancha olasiz ?", reply_markup=markup)
            await message.delete()
            await Yuk_reys_andijon.locatsiya.set()
        else:
            await message.answer("Iltimos son kiritib ifodalang. Matn bilan emas !!!")
            await Yuk_reys_andijon.qolda_odam_soni.set()
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.jami_odam)
async def ksdhkja(call: CallbackQuery, state: FSMContext):
    
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Xa', callback_data='xa'))
        markup.insert(aiogram.types.InlineKeyboardButton(text="'Yo'q", callback_data="yo'q"))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Bagaj bo'shmi.. ? (xa yoki yo'q )", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.yuk_olasizmi.set()
@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.jami_odam)
async def aljs(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text="Keyingisi",state=Yuk_reys_andijon.jami_odam)
async def ton(call:CallbackQuery,state:FSMContext):
    
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
        await call.message.answer("Yo'l haqqi uchun qancha olasiz ?",reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.locatsiya.set()
@dp.callback_query_handler(state=Yuk_reys_andijon.jami_odam)
async def ton(call:CallbackQuery,state:FSMContext):
    
        await state.update_data({"tonna":call.data})
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
        markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Yo'l haqqi uchun qancha olasiz ?",reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.locatsiya.set()
@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.locatsiya)
async def bosh_menu(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.locatsiya)
async def ortga_qaytamian(call:CallbackQuery,state:FSMContext):
    
        markup=InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='1', callback_data='1'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='3', callback_data='3'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='5', callback_data='5'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='7', callback_data='7'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        await call.message.answer("Necha tonnagacha yuk olasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.jami_odam.set()
@dp.callback_query_handler(text="ruchnoy", state=Yuk_reys_andijon.locatsiya)
async def pol_ruchnoy(call: CallbackQuery, state: FSMContext):
    
        markup = InlineKeyboardMarkup(row_width=3)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
        await call.message.answer("O'zingizning xizmat narxingizni kiriting : ")
        await call.message.delete()
        await Yuk_reys_andijon.pul_qol.set()
@dp.message_handler(state=Yuk_reys_andijon.pul_qol)
async def qolda_pul(message: Message, state: FSMContext):
    
        await state.update_data(
            {
                "yol_haqqi": message.text
            }
        )
        viloyat = {
            "Andijon": "andijon",
            "Namangan": "namangan",
            "Farg'ona": "farg'ona",
            "Buxoro": "buxoro",
            "Toshkent": "toshkent",
            "Toshkent shahri": "kent shahar",
            "Sirdaryo": "sirdaryo",
            "Surxondaryo": "surxondaryo",
            "Qashqadaryo": "qashqadaryo",
            "Xorazm": "xorazm",
            "Navoiy": "navoiy",
            "Jizzax": "jizzax",
            "Samarqand": "samarqand",
            "Qoraqalpog'iston": "qoraqalpoq",
            "Keyingisi": "Olinmaydi",
            "Tanlab bo'ldim": "tanladim",
            "Ortga": "ortga",
            "Bosh menu": "boshmenu",
        }
        viloyatlar_yol = InlineKeyboardMarkup(row_width=3)
        for key, value in viloyat.items():
            viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
        await message.answer("Yo'lingizdagi qaysi tumanlardan qo'shimcha yuk olasiz ? ",
                             reply_markup=viloyatlar_yol)
        await message.delete()
        await Yuk_reys_andijon.odam_vil.set()
@dp.callback_query_handler(text="Keyingisi", state=Yuk_reys_andijon.locatsiya)
async def jami_odam(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "yol_haqqi": 'Kiritilmadi'
            }
        )
        viloyat = {
            "Andijon": "andijon",
            "Namangan": "namangan",
            "Farg'ona": "farg'ona",
            "Buxoro": "buxoro",
            "Toshkent": "toshkent",
            "Toshkent shahri": "kent shahar",
            "Sirdaryo": "sirdaryo",
            "Surxondaryo": "surxondaryo",
            "Qashqadaryo": "qashqadaryo",
            "Xorazm": "xorazm",
            "Navoiy": "navoiy",
            "Jizzax": "jizzax",
            "Samarqand": "samarqand",
            "Qoraqalpog'iston": "qoraqalpoq",
            "Keyingisi": "Olinmaydi",
            "Tanlab bo'ldim": "tanladim",
            "Ortga": "ortga",
            "Bosh menu": "boshmenu",
        }
        viloyatlar_yol = InlineKeyboardMarkup(row_width=3)
        for key, value in viloyat.items():
            viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Yo'lingizdagi qaysi tumanlardan qo'shimcha yuk olasiz ? ",
                                  reply_markup=viloyatlar_yol)
        await call.message.delete()
        await Yuk_reys_andijon.odam_vil.set()
@dp.callback_query_handler(state=Yuk_reys_andijon.locatsiya)
async def jami_odam(call: CallbackQuery, state: FSMContext):
    
        await state.update_data(
            {
                "yol_haqqi": call.data
            }
        )
        viloyat = {
            "Andijon": "andijon",
            "Namangan": "namangan",
            "Farg'ona": "farg'ona",
            "Buxoro": "buxoro",
            "Toshkent viloyati": "toshkent",
            "Toshkent shahri": "kent shahar",
            "Sirdaryo": "sirdaryo",
            "Surxondaryo": "surxondaryo",
            "Qashqadaryo": "qashqadaryo",
            "Xorazm": "xorazm",
            "Navoiy": "navoiy",
            "Jizzax": "jizzax",
            "Samarqand": "samarqand",
            "Qoraqalpog'iston": "qoraqalpoq",
            "Keyingisi": "Olinmaydi",
            "Tanlab bo'ldim": "tanladim",
            "Ortga": "ortga",
            "Bosh menu": "boshmenu",
        }
        viloyatlar_yol = InlineKeyboardMarkup(row_width=3)
        for key, value in viloyat.items():
            viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Yo'lingizdagi qaysi tumanlardan qo'shimcha yuk olasiz ? ",
                                  reply_markup=viloyatlar_yol)
        await call.message.delete()
        await Yuk_reys_andijon.odam_vil.set()
@dp.callback_query_handler(text="ortga", state=Yuk_reys_andijon.odam_vil)
async def kasaas(call: CallbackQuery, state: FSMContext):
    
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
        markup.insert(aiogram.types.InlineKeyboardButton(text="Qo'lda kiritish", callback_data='ruchnoy'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))

        await call.message.answer("Yo'l haqqi uchun qancha olasiz ? ", reply_markup=markup)
        await call.message.delete()
        await Yuk_reys_andijon.locatsiya.set()


@dp.callback_query_handler(text="boshmenu", state=Yuk_reys_andijon.odam_vil)
async def asla(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Salom haydovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")


@dp.callback_query_handler(state=Yuk_reys_andijon.odam_vil)
async def odam_viloyat(call: CallbackQuery, state: FSMContext):
    

        list = []
        jamii = await db.select_all_yoldan_odam()
        for i in jamii:
            if i[2] == call.from_user.id:
                list.append(i[1])
        if call.data == 'andijon':
            andijon = {}
            if "andijon shaxar" in list:
                andijon["✅Andijon shaxar"] = 'andijon shaxar'
            else:
                andijon["Andijon shaxar"] = 'andijon shaxar'
            if "Andijon" in list:
                andijon["✅Andijon tuman"] = "Andijon"
            else:
                andijon["Andijon tuman"] = 'Andijon'
            if "ulug'nor" in list:
                andijon["✅Ulug'nor"] = "ulug'nor"
            else:
                andijon["Ulug'nor"] = "ulug'nor"
            if "asaka" in list:
                andijon["✅Asaka"] = "asaka"
            else:
                andijon["Asaka"] = "asaka"
            if "paxtaobod" in list:

                andijon["✅Paxtaobod"] = 'paxtaobod'
            else:
                andijon["Paxtaobod"] = 'paxtaobod'
            if "shaxrixon" in list:

                andijon["✅Shaxrixon"] = 'shaxrixon'
            else:
                andijon["Shaxrixon"] = 'shaxrixon'
            if "marhamat" in list:

                andijon["✅Marhamat"] = "marhamat"
            else:
                andijon["Marhamat"] = 'marhamat'
            if "xonabod shahar" in list:
                andijon["✅Xonabod shahar"] = "xonabod shahar"
            else:
                andijon["Xonabod shahar"] = 'xonabod shahar'
            if "xonabod" in list:
                andijon["✅Xonabod"] = "xonabod"
            else:
                andijon["Xonabod"] = 'xonabod'
            if "oltinko'l" in list:

                andijon["✅Oltinko'l"] = "oltinko'l"
            else:
                andijon["Oltinko'l"] = "oltinko'l"
            if "baliqchi" in list:

                andijon["✅Baliqchi"] = "baliqchi"
            else:
                andijon["Baliqchi"] = 'baliqchi'
            if "bo'ston" in list:

                andijon["✅Bo'ston"] = "bo'ston"
            else:
                andijon["Bo'ston"] = "bo'ston"
            if "buloqboshi" in list:

                andijon["✅Buloqboshi"] = "buloqboshi"
            else:
                andijon["Buloqboshi"] = "buloqboshi"
            if "izboskan" in list:

                andijon["✅Izboskan"] = "izboskan"
            else:
                andijon["Izboskan"] = "izboskan"
            if "jalaquduq" in list:

                andijon["✅Jalaquduq"] = "jalaquduq"
            else:
                andijon["Jalaquduq"] = "jalaquduq"
            if "xo'jabod" in list:

                andijon["✅Xo'jabod"] = "xo'jabod"
            else:
                andijon["Xo'jabod"] = "xo'jabod"
            if "qo'rg'ontepa" in list:

                andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa"
            else:
                andijon["Qo'rg'ontepa"] = "qo'rg'ontepa"
            shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
            for key, value in andijon.items():
                shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Andijonning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_tugma)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'namangan':
            namangan = {}
            if "namangan shaxar" in list:
                namangan["✅Namangan shaxar"] = 'namangan shaxar'
            else:
                namangan["Namangan shaxar"] = 'namangan shaxar'
            if "namangan tuman" in list:
                namangan["✅Namangan tuman"] = 'namangan tuman'
            else:
                namangan["Namangan tuman"] = 'namangan tuman'
            if "chortoq" in list:
                namangan["✅Chortoq"] = "chortoq"
            else:
                namangan["Chortoq"] = "chortoq"
            if "chust" in list:
                namangan["✅Chust"] = 'chust'
            else:
                namangan["Chust"] = 'chust'
            if "kosonsoy" in list:
                namangan["✅Kosonsoy"] = "kosonsoy"
            else:
                namangan["Kosonsoy"] = "kosonsoy"
            if "mingbuloq" in list:
                namangan["✅Mingbuloq"] = 'mingbuloq'
            else:
                namangan["Mingbuloq"] = 'mingbuloq'
            if "norin" in list:
                namangan["✅Norin"] = "norin"
            else:
                namangan["Norin"] = 'norin'
            if "pop" in list:
                namangan["✅Pop"] = "pop"
            else:
                namangan["Pop"] = 'pop'
            if "toraqorgon" in list:
                namangan["✅To'raqo'rg'on"] = "toraqorgon"
            else:
                namangan["To'raqo'rg'on"] = "toraqorgon"
            if "uchqorgon" in list:
                namangan["✅Uchqo'rg'on"] = "uchqorgon"
            else:
                namangan["Uchqo'rg'on"] = 'uchqorgon'
            if "uychi" in list:
                namangan["✅Uychi"] = "uychi"
            else:
                namangan["Uychi"] = "uychi"
            if "yangi qorgon" in list:
                namangan["✅Yangiqo'rg'on"] = "yangi qorgon"
            else:
                namangan["Yangiqo'rg'on"] = "yangi qorgon"
            if "yangi namangan" in list:
                namangan["✅Yangi Namangan"] = "yangi namangan"
            else:
                namangan["Yangi Namangan"] = "yangi namangan"

            shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
            for key, value in namangan.items():
                shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_namangan.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Namanganning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_namangan)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == "farg'ona":
            fargona = {}
            if "fergana city" in list:
                fargona["✅Fargʻona shahri"] = "fergana city"
            else:
                fargona["Fargʻona shahri"] = 'fergana city'
            if "fergana" in list:
                fargona["✅Fargʻona tuman"] = "fergana"
            else:
                fargona["Fargʻona tuman"] = 'fergana'
            if "oltiariq" in list:
                fargona["✅Oltiariq"] = "oltiariq"
            else:
                fargona["Oltiariq"] = "oltiariq"
            if "bog'dod" in list:
                fargona["✅Bagʻdod"] = "bog'dod"
            else:
                fargona["Bagʻdod"] = "bog'dod"
            if "beshariq" in list:
                fargona["✅Beshariq"] = "beshariq"
            else:
                fargona["Beshariq"] = "beshariq"
            if "buvayda" in list:
                fargona["✅Buvayda"] = 'buvayda'
            else:
                fargona["Buvayda"] = 'buvayda'
            if "dangara" in list:
                fargona["✅Dangʻara"] = 'dangara'
            else:
                fargona["Dangʻara"] = 'dangara'
            if "furqat" in list:
                fargona["✅Furqat"] = "furqat"
            else:
                fargona["Furqat"] = 'furqat'
            if "qo'shtepa" in list:
                fargona["✅Qoʻshtepa"] = "qo'shtepa"
            else:
                fargona["Qoʻshtepa"] = "qo'shtepa"
            if "quva" in list:
                fargona["✅Quva"] = "quva"
            else:
                fargona["Quva"] = 'quva'
            if "rishton" in list:
                fargona["✅Rishton"] = "rishton"
            else:
                fargona["Rishton"] = "rishton"
            if "sox" in list:
                fargona["✅Soʻx"] = "sox"
            else:
                fargona["Soʻx"] = "sox"
            if "toshloq" in list:
                fargona["✅Toshloq"] = "toshloq"
            else:
                fargona["Toshloq"] = "toshloq"
            if "o'zbekiston" in list:
                fargona["✅Oʻzbekiston"] = "o'zbekiston"
            else:
                fargona["Oʻzbekiston"] = "o'zbekiston"
            if "uchko'prik" in list:
                fargona["✅Uchkoʻprik"] = "uchko'prik"
            else:
                fargona["Uchkoʻprik"] = "uchko'prik"
            if "yozyovon" in list:
                fargona["✅Yozyovon"] = "yozyovon"
            else:
                fargona["Yozyovon"] = "yozyovon"
            if "quvasoy shahri" in list:
                fargona["✅Quvasoy shahri"] = "quvasoy shahri"
            else:
                fargona["Quvasoy shahri"] = "quvasoy shahri"
            if "margilon shahri" in list:
                fargona["✅Marg'ilon shahri"] = "margilon shahri"
            else:
                fargona["Marg'ilon shahri"] = "margilon shahri"
            if "qoqon" in list:
                fargona["✅Qo'qon shahri"] = "qoqon"
            else:
                fargona["Qo'qon shahri"] = "qoqon"
            shaxsiy_fargona = InlineKeyboardMarkup(row_width=3)
            for key, value in fargona.items():
                shaxsiy_fargona.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_fargona.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_fargona.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_fargona.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Farg'onaning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_fargona)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'buxoro':
            buxoro = {}
            if "buxoro shaxar" in list:
                buxoro["✅Buxoro shahar"] = "buxoro shaxar"
            else:
                buxoro["Buxoro shahar"] = "buxoro shaxar"
            if "Buxoro tuman" in list:
                buxoro["✅Buxoro tuman"] = "Buxoro tuman"
            else:
                buxoro["Buxoro tuman"] = "Buxoro tuman"
            if "olot" in list:
                buxoro["✅Olot"] = "olot"
            else:
                buxoro["Olot"] = "olot"
            if "g'ijduvon" in list:
                buxoro["✅Gʻijduvon"] = "g'ijduvon"
            else:
                buxoro["Gʻijduvon"] = "g'ijduvon"
            if "jondor" in list:
                buxoro["✅Jondor"] = 'jondor'
            else:
                buxoro["Jondor"] = 'jondor'
            if "kogon shahar" in list:
                buxoro["✅Kogon shahar"] = 'kogon shahar'
            else:
                buxoro["Kogon shahar"] = 'kogon shahar'
            if "kogon" in list:
                buxoro["✅Kogon tuman"] = 'kogon tuman'
            else:
                buxoro["Kogon tuman"] = 'kogon tuman'
            if "qorako'l" in list:
                buxoro["✅Qorakoʻl"] = "qorako'l"
            else:
                buxoro["Qorakoʻl"] = 'qorako\'l'
            if "qorovulbozor" in list:
                buxoro["✅Qorovulbozor"] = "qorovulbozor"
            else:
                buxoro["Qorovulbozor"] = 'qorovulbozor'
            if "peshku" in list:
                buxoro["✅Peshku"] = "peshku"
            else:
                buxoro["Peshku"] = "peshku"
            if "romitan" in list:
                buxoro["✅Romitan"] = "romitan"
            else:
                buxoro["Romitan"] = 'romitan'
            if "shofirkon" in list:
                buxoro["✅Shofirkon"] = "shofirkon"
            else:
                buxoro["Shofirkon"] = "shofirkon"
            if "vobkent" in list:
                buxoro["✅Vobkent"] = "vobkent"
            else:
                buxoro["Vobkent"] = "vobkent"
            shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
            for key, value in buxoro.items():
                shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Buxoroning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_buxoro)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'toshkent':
            toshkent = {}
            if "Toshkent tuman" in list:
                toshkent["✅Toshkent tuman"] = "Toshkent"
            else:
                toshkent["Toshkent tuman"] = "Toshkent"
            if "bekobod" in list:
                toshkent["✅Bekobod tuman"] = "bekobod"
            else:
                toshkent["Bekobod tuman"] = "bekobod"
            if "bekobod_shahar" in list:
                toshkent["✅Bekobod shahar"] = "bekobod_shahar"
            else:
                toshkent["Bekobod shahar"] = "bekobod_shahar"
            if "bostonliq" in list:
                toshkent["✅Boʻstonliq tuman"] = 'bostonliq'
            else:
                toshkent["Boʻstonliq tuman"] = 'bostonliq'
            if "boka" in list:
                toshkent["✅Boʻka"] = "boka"
            else:
                toshkent["Boʻka"] = "boka"
            if "chinoz" in list:
                toshkent["✅Chinoz"] = 'chinoz'
            else:
                toshkent["Chinoz"] = 'chinoz'
            if "qibray" in list:
                toshkent["✅Qibray"] = 'qibray'
            else:
                toshkent["Qibray"] = 'qibray'
            if "ohangaron" in list:
                toshkent["✅Ohangaron tuman"] = "ohangaron"
            else:
                toshkent["Ohangaron tuman"] = 'ohangaron'
            if "ohangaron shahar" in list:
                toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
            else:
                toshkent["Ohangaron shahri"] = 'ohangaron shahar'
            if "oqqorgon" in list:
                toshkent["✅Oqqoʻrgʻon"] = "oqqorgon"
            else:
                toshkent["Oqqoʻrgʻon"] = 'oqqorgon'
            if "parkent" in list:
                toshkent["✅Parkent"] = "parkent"
            else:
                toshkent["Parkent"] = "parkent"
            if "piskent" in list:
                toshkent["✅Piskent"] = "piskent"
            else:
                toshkent["Piskent"] = 'piskent'
            if "quyichirchiq" in list:
                toshkent["✅Quyi Chirchiq"] = "quyichirchiq"
            else:
                toshkent["Quyi Chirchiq"] = "quyichirchiq"
            if "ortachirchiq" in list:
                toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq"
            else:
                toshkent["Oʻrta Chirchiq"] = "ortachirchiq"
            if "yangiyol" in list:
                toshkent["✅Yangiyoʻl"] = "yangiyol"
            else:
                toshkent["Yangiyoʻl"] = "yangiyol"
            if "yangiyol shahri" in list:
                toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahri"
            else:
                toshkent["Yangiyoʻl shahri"] = "yangiyol shahri"
            if "yuqorichirchiq" in list:
                toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq"
            else:
                toshkent["Yuqori Chirchiq"] = "yuqorichirchiq"
            if "zangiota" in list:
                toshkent["✅Zangiota"] = "zangiota"
            else:
                toshkent["Zangiota"] = "zangiota"
            if "olmaliq" in list:
                toshkent["✅Olmaliq shahri"] = "olmaliq "
            else:
                toshkent["Olmaliq shahri"] = "olmaliq"
            if "nurafshon" in list:
                toshkent["✅Nurafshon shahri"] = "nurafshon "
            else:
                toshkent["Nurafshon shahri"] = "nurafshon"
            if "angren" in list:
                toshkent["✅Angren shahar"] = "angren "
            else:
                toshkent["Angren shahr"] = "angren"
            if "angren" in list:
                toshkent["✅Angren"] = "angren "
            else:
                toshkent["Angren"] = "angren"
            if "chirchiq shahri" in list:
                toshkent["✅Chirchiq shahri"] = "chirchiq shahri"
            else:
                toshkent["Chirchiq shahri"] = "chirchiq shahri"
            if "qoyliq" in list:
                toshkent["✅Qo'yliq"] = "qoyliq"
            else:
                toshkent["Qo'yliq"] = "qoyliq"
            shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
            for key, value in toshkent.items():
                shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Toshkentning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_toshkent)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'sirdaryo':
            sirdaryo = {}
            if "sirdaryo shahar" in list:
                sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
            else:
                sirdaryo["Sirdaryo shahar"] = "sirdaryo shahar"
            if "sirdaryo tuman" in list:
                sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tuman"
            else:
                sirdaryo["Sirdaryo tuman"] = "sirdaryo tuman"
            if "oqoltin" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin"
            else:
                sirdaryo["Oqoltin"] = "oqoltin"
            if "Shirin shahri" in list:
                sirdaryo["✅Shirin shahri"] = "Shirin shahri"
            else:
                sirdaryo["Shirin shahri"] = "Shirin shahri"
            if "Yangiyer shahri" in list:
                sirdaryo["✅Yangiyer shahri"] = "Yangiyer shahri"
            else:
                sirdaryo["Yangiyer shahri"] = "Yangiyer shahri"
            if "oqoltin" in list:
                sirdaryo["✅Oqoltin"] = "oqoltin"
            else:
                sirdaryo["Oqoltin"] = "oqoltin"
            if "boyovut" in list:
                sirdaryo["✅Boyovut"] = 'boyovut'
            else:
                sirdaryo["Boyovut"] = 'boyovut'
            if "guliston tuman" in list:
                sirdaryo["✅Guliston tuman"] = "guliston tuman"
            else:
                sirdaryo["Guliston tuman"] = "guliston tuman"
            if "guliston shahar" in list:
                sirdaryo["✅Guliston shahar"] = "guliston shahar"
            else:
                sirdaryo["Guliston shahar"] = "guliston shahar"
            if "xovos" in list:
                sirdaryo["✅Xovos"] = 'xovos'
            else:
                sirdaryo["Xovos"] = 'xovos'
            if "mirzaobod" in list:
                sirdaryo["✅Mirzaobod"] = 'mirzaobod'
            else:
                sirdaryo["Mirzaobod"] = 'mirzaobod'
            if "sayxunobod" in list:
                sirdaryo["✅Sayxunobod"] = "sayxunobod"
            else:
                sirdaryo["Sayxunobod"] = 'sayxunobod'
            if "sardoba" in list:
                sirdaryo["✅Sardoba"] = "sardoba"
            else:
                sirdaryo["Sardoba"] = 'sardoba'

            shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in sirdaryo.items():
                shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Sirdaryoning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_sirdaryo)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'surxondaryo':
            surxondaryo = {}
            if "termiz shahar" in list:
                surxondaryo["✅Termiz shahar"] = "termiz shahar"
            else:
                surxondaryo["Termiz shahar"] = "termiz shahar"
            if "angor" in list:
                surxondaryo["✅Angor"] = "angor"
            else:
                surxondaryo["Angor"] = "angor"
            if "boysun" in list:
                surxondaryo["✅Boysun"] = "boysun"
            else:
                 surxondaryo["Boysun"] = "boysun"
            if "denov" in list:
                surxondaryo["✅Denov"] = 'denov'
            else:
                surxondaryo["Denov"] = 'denov'
            if "jarqorgon" in list:
                surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon"
            else:
                surxondaryo["Jarqoʻrgʻon"] = 'jarqorgon'
            if "furqat" in list:
                surxondaryo["✅Furqat"] = "furqat"
            else:
                surxondaryo["Furqat"] = 'furqat'
            if "qiziriq" in list:
                surxondaryo["✅Qiziriq"] = "qiziriq"
            else:
                surxondaryo["Qiziriq"] = "qiziriq"
            if "qumqorgon" in list:
                surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon"
            else:
                surxondaryo["Qumqoʻrgʻon"] = 'qumqorgon'
            if "muzrabod" in list:
                surxondaryo["✅Muzrabod"] = "muzrabod"
            else:
                surxondaryo["Muzrabod"] = "muzrabod"
            if "oltinsoy" in list:
                surxondaryo["✅Oltinsoy"] = "oltinsoy"
            else:
                surxondaryo["Oltinsoy"] = "oltinsoy"
            if "sariosiyo" in list:
                surxondaryo["✅Sariosiyo"] = "sariosiyo"
            else:
                surxondaryo["Sariosiyo"] = "sariosiyo"
            if "sherobod" in list:
                surxondaryo["✅Sherobod"] = "sherobod"
            else:
                surxondaryo["Sherobod"] = "sherobod"
            if "shorchi" in list:
                surxondaryo["✅Shoʻrchi"] = "shorchi"
            else:
                surxondaryo["Shoʻrchi"] = "shorchi"
            if "termiz tuman" in list:
                surxondaryo["✅Termiz tuman"] = "termiz tuman"
            else:
                surxondaryo["Termiz tuman"] = "termiz tuman"
            if "uzun" in list:
                surxondaryo["✅Uzun"] = "uzun"
            else:
                surxondaryo["Uzun"] = "uzun"
            shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in surxondaryo.items():
                shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Surxondaryoning qaysi tumanlaridan yuk olasiz ?",
                                      reply_markup=shaxsiy_surxondaryo)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'qashqadaryo':
            qashqadaryo = {}
            if "qarshi shahar" in list:
                qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
            else:
                qashqadaryo["Qarshi shahar"] = "qarshi shahar"
            if "dehqonobod" in list:
                qashqadaryo["✅Dehqonobod"] = "dehqonobod"
            else:
                qashqadaryo["Dehqonobod"] = "dehqonobod"
            if "kasbi" in list:
                qashqadaryo["✅Kasbi"] = "kasbi"
            else:
                qashqadaryo["Kasbi"] = "kasbi"
            if "kitob" in list:
                qashqadaryo["✅Kitob"] = "kitob"
            else:
                qashqadaryo["Kitob"] = "kitob"
            if "koson" in list:
                qashqadaryo["✅Koson"] = 'koson'
            else:
                qashqadaryo["Koson"] = 'koson'
            if "kokdala" in list:
                qashqadaryo["✅Koʻkdala"] = 'kokdala'
            else:
                qashqadaryo["Koʻkdala"] = 'kokdala'
            if "mirishkor" in list:
                qashqadaryo["✅Mirishkor"] = "mirishkor"
            else:
                qashqadaryo["Mirishkor"] = 'mirishkor'
            if "muborak" in list:
                qashqadaryo["✅Muborak"] = "muborak"
            else:
                qashqadaryo["Muborak"] = 'muborak'
            if "nishon" in list:
                qashqadaryo["✅Nishon"] = "nishon"
            else:
                qashqadaryo["Nishon"] = "nishon"
            if "qamashi" in list:
                qashqadaryo["✅Qamashi"] = "qamashi"
            else:
                qashqadaryo["Qamashi"] = 'qamashi'
            if "qarshi" in list:
                qashqadaryo["✅Qarshi"] = "qarshi"
            else:
                qashqadaryo["Qarshi"] = "qarshi"
            if "yakkabog" in list:
                qashqadaryo["✅Yakkabogʻ"] = "yakkabog"
            else:
                qashqadaryo["Yakkabogʻ"] = "yakkabog"
            if "guzor" in list:
                qashqadaryo["✅Gʻuzor"] = "guzor"
            else:
                qashqadaryo["Gʻuzor"] = "guzor"
            if "shahrisabz" in list:
                qashqadaryo["✅Shahrisabz"] = "shahrisabz"
            else:
                qashqadaryo["Shahrisabz"] = "shahrisabz"
            if "shahrisabz shahar" in list:
                qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
            else:
                qashqadaryo["Shahrisabz shahar"] = "shahrisabz shahar"
            if "chiroqchi" in list:
                qashqadaryo["✅Chiroqchi"] = "chiroqchi"
            else:
                qashqadaryo["Chiroqchi"] = "chiroqchi"

            shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
            for key, value in qashqadaryo.items():
                shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Qashqadaryoning qaysi tumanlaridan yuk olasiz ?",
                                      reply_markup=shaxsiy_qashqadaryo)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'xorazm':
            xorazm = {}
            if "urganch shahar" in list:
                xorazm["✅Urganch shahar"] = "urganch shahar"
            else:
                xorazm["Urganch shahar"] = "urganch shahar"
            if "bog'ot" in list:
                xorazm["✅Bogʻot"] = "bog'ot"
            else:
                xorazm["Bogʻot"] = "bog'ot"
            if "gurlan" in list:
                xorazm["✅Gurlan"] = "gurlan"
            else:
                xorazm["Gurlan"] = "gurlan"
            if "xonqa" in list:
                xorazm["✅Xonqa"] = "xonqa"
            else:
                xorazm["Xonqa"] = "xonqa"
            if "hazorasp" in list:
                xorazm["✅Hazorasp"] = 'hazorasp'
            else:
                xorazm["Hazorasp"] = 'hazorasp'
            if "xiva" in list:
                xorazm["✅Xiva"] = 'xiva'
            else:
                xorazm["Xiva"] = 'xiva'
            if "xiva shahar" in list:
                xorazm["✅Xiva shahar"] = 'xiva shahar'
            else:
                xorazm["Xiva shahar"] = 'xiva shahar'
            if "qoshko'prik" in list:
                xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik"
            else:
                xorazm["Qoʻshkoʻpir"] = "qoshko'prik"
            if "shovot" in list:
                xorazm["✅Shovot"] = "shovot"
            else:
                xorazm["Shovot"] = 'shovot'
            if "urganch" in list:
                xorazm["✅Urganch tuman"] = "urganch"
            else:
                xorazm["Urganch tuman"] = "urganch"
            if "yangiariq" in list:
                xorazm["✅Yangiariq"] = "yangiariq"
            else:
                xorazm["Yangiariq"] = 'yangiariq'
            if "yangibozor" in list:
                xorazm["✅Yangibozor"] = "yangibozor"
            else:
                xorazm["Yangibozor"] = "yangibozor"
            if "tuproqqal'a" in list:
                xorazm["✅Tupproqqalʼa"] = "tuproqqal'a"
            else:
                xorazm["Tupproqqalʼa"] = "tuproqqal'a"

            shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
            for key, value in xorazm.items():
                shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Xorazmning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_xorazm)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'navoiy':
            navoiy = {}
            if "Navoiy shahri" in list:
                navoiy["✅Navoiy shahri"] = "Navoiy shahri"
            else:
                navoiy["Navoiy shahri"] = "Navoiy shahri"
            if "Zarafshon shahri" in list:
                navoiy["✅Zarafshon shahri"] = "Zarafshon shahri"
            else:
                navoiy["Zarafshon shahri"] = "Zarafshon shahri"
            if "konimex" in list:
                navoiy["✅Konimex"] = "konimex"
            else:
                navoiy["Konimex"] = "konimex"
            if "karmana" in list:
                navoiy["✅Karmana"] = "karmana"
            else:
                navoiy["Karmana"] = "karmana"
            if "qiziltepa" in list:
                navoiy["✅Qiziltepa"] = "qiziltepa"
            else:
                navoiy["Qiziltepa"] = "qiziltepa"
            if "xatirchi" in list:
                navoiy["✅Xatirchi"] = 'xatirchi'
            else:
                navoiy["Xatirchi"] = 'xatirchi'
            if "navbahor" in list:
                navoiy["✅Navbahor"] = 'navbahor'
            else:
                navoiy["Navbahor"] = 'navbahor'
            if "nurota" in list:
                navoiy["✅Nurota"] = "nurota"
            else:
                navoiy["Nurota"] = "nurota"
            if "tomdi" in list:
                navoiy["✅Tomdi"] = "tomdi"
            else:
                navoiy["Tomdi"] = 'tomdi'
            if "uchquduq" in list:
                navoiy["✅Uchquduq"] = "uchquduq"
            else:
                navoiy["Uchquduq"] = "uchquduq"

            shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
            for key, value in navoiy.items():
                shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_navoiy.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Navoiyning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_navoiy)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'jizzax':

            jizzax = {}
            if "Jizzax shahri" in list:
                jizzax["✅Jizzax shahri"] = "Jizzax shahri"
            else:
                jizzax["Jizzax shahri"] = "Jizzax shahri"
            if "arnasoy" in list:
                jizzax["✅Arnasoy"] = "arnasoy"
            else:
                jizzax["Arnasoy"] = "arnasoy"
            if "baxmal" in list:
                jizzax["✅Baxmal"] = "baxmal"
            else:
                jizzax["Baxmal"] = "baxmal"
            if "do'stlik" in list:
                jizzax["✅Doʻstlik"] = "do'stlik"
            else:
                jizzax["Doʻstlik"] = "do'stlik"
            if "forish" in list:
                jizzax["✅Forish"] = 'forish'
            else:
                jizzax["Forish"] = 'forish'
            if "g'allarol" in list:
                jizzax["✅Koʻkdala"] = "g'allarol"
            else:
                jizzax["Koʻkdala"] = "g'allarol"
            if "sharof rashidov" in list:
                jizzax["✅Sharof Rashidov"] = "sharof rashidov"
            else:
                jizzax["Sharof Rashidov"] = 'sharof rashidov'
            if "mirzachol" in list:
                jizzax["✅Mirzachoʻl"] = "mirzachol"
            else:
                jizzax["Mirzachoʻl"] = 'mirzachol'
            if "paxtakor" in list:
                jizzax["✅Paxtakor"] = "paxtakor"
            else:
                jizzax["Paxtakor"] = "paxtakor"
            if "yangi obod" in list:
                jizzax["✅Yangiobod"] = "yangi obod"
            else:
                jizzax["Yangiobod"] = 'yangi obod'
            if "zomin" in list:
                jizzax["✅Zomin"] = "zomin"
            else:
                jizzax["Zomin"] = "zomin"
            if "zafarobod" in list:
                jizzax["✅Zafarobod"] = "zafarobod"
            else:
                jizzax["Zafarobod"] = "zafarobod"
            if "zarbdor" in list:
                jizzax["✅Zarbdor"] = "zarbdor"
            else:
                jizzax["Zarbdor"] = "zarbdor"
            shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
            for key, value in jizzax.items():
                shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_jizzax.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("JIzzaxning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_jizzax)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'samarqand':
            samarqand = {}
            if "samarqand shahar" in list:
                samarqand["✅Samarqand shahar"] = "samarqand shahar"
            else:
                samarqand["Samarqand shahar"] = "samarqand shahar"
            if "samarqand tuman" in list:
                samarqand["✅Samarqand tuman"] = "samarqand tuman"
            else:
                samarqand["Samarqand tuman"] = "samarqand tuman"
            if "bulungur" in list:
                samarqand["✅Bulungʻur"] = "bulungur"
            else:
                samarqand["Bulungʻur"] = "bulungur"
            if "ishtixon" in list:
                samarqand["✅Ishtixon"] = "ishtixon"
            else:
                samarqand["Ishtixon"] = "ishtixon"
            if "jomboy" in list:
                samarqand["✅Jomboy"] = "jomboy"
            else:
                samarqand["Jomboy"] = "jomboy"
            if "kattaqorgon" in list:
                samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon'
            else:
                samarqand["Kattaqoʻrgʻon"] = 'kattaqorgon'
            if "Kattaqoʻrgʻon shahar" in list:
                samarqand["✅Kattaqoʻrgʻon shahar"] = 'Kattaqoʻrgʻon shahar '
            else:
                samarqand["Kattaqoʻrgʻon shahar"] = 'Kattaqoʻrgʻon shahar'
            if "qoshrabot" in list:
                samarqand["✅Qoʻshrabot"] = "qoshrabot"
            else:
                samarqand["Qoʻshrabot"] = "qoshrabot"
            if "narpay" in list:
                samarqand["✅Narpay"] = "narpay"
            else:
                samarqand["Narpay"] = 'narpay'
            if "nurobod" in list:
                samarqand["✅Nurobod"] = "nurobod"
            else:
                samarqand["Nurobod"] = 'nurobod'
            if "oqdaryo" in list:
                samarqand["✅Oqdaryo"] = "oqdaryo"
            else:
                samarqand["Oqdaryo"] = "oqdaryo"
            if "paxtachi" in list:
                samarqand["✅Paxtachi"] = "paxtachi"
            else:
                samarqand["Paxtachi"] = 'paxtachi'
            if "payariq" in list:
                samarqand["✅Payariq"] = "payariq"
            else:
                samarqand["Payariq"] = "payariq"
            if "pastdargom" in list:
                samarqand["✅Pastdargʻom"] = "pastdargom"
            else:
                samarqand["Pastdargʻom"] = "pastdargom"
            if "toyloq" in list:
                samarqand["✅Toyloq"] = "toyloq"
            else:
                samarqand["Toyloq"] = "toyloq"
            shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
            for key, value in samarqand.items():
                shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_samarqand.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Samarqandning qaysi tumanlaridan yuk olasiz ?",
                                      reply_markup=shaxsiy_samarqand)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'kent shahar':
            tosh_shahar = {}
            if "Toshkent shahar" in list:
                tosh_shahar["✅Toshkent shahar"] = "Toshkent shahar"
            else:
                tosh_shahar["Toshkent shahar"] = "Toshkent shahar"
            if "Bektemir" in list:
                tosh_shahar["✅Bektemir tumani"] = "Bektemir"
            else:
                tosh_shahar["Bektemir tumani"] = "Bektemir"
            if "Mirzo Ulug‘bek tumani" in list:
                tosh_shahar["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug‘bek tumani"
            else:
                tosh_shahar["Mirzo Ulug‘bek tumani"] = "Mirzo Ulug‘bek tumani"
            if "Mirobod tumani" in list:
                tosh_shahar["✅Mirobod tumani"] = "Mirobod tumani"
            else:
                tosh_shahar["Mirobod tumani"] = "Mirobod tumani"
            if "Olmazor tumani" in list:
                tosh_shahar["✅Olmazor tumani"] = 'Olmazor tumani'
            else:
                tosh_shahar["Olmazor tumani"] = 'Olmazor tumani'
            if "Sirg‘ali tumani" in list:
                tosh_shahar["✅Sirg‘ali tumani"] = 'Sirg‘ali tumani'
            else:
                tosh_shahar["Sirg‘ali tumani"] = 'Sirg‘ali tumani'
            if "Uchtepa tumani" in list:
                tosh_shahar["✅Uchtepa tumani"] = "Uchtepa tumani"
            else:
                tosh_shahar["Uchtepa tumani"] = "Uchtepa tumani"
            if "Chilonzor tumani" in list:
                tosh_shahar["✅Chilonzor tumani"] = "Chilonzor tumani"
            else:
                tosh_shahar["Chilonzor tumani"] = 'Chilonzor tumani'
            if "Shayxontohur tumani" in list:
                tosh_shahar["✅Shayxontohur tumani"] = "Shayxontohur tumani"
            else:
                tosh_shahar["Shayxontohur tumani"] = "Shayxontohur tumani"
            if "Yunusobod tumani" in list:
                tosh_shahar["✅Yunusobod tumani"] = "Yunusobod tumani"
            else:
                tosh_shahar["Yunusobod tumani"] = 'Yunusobod tumani'
            if "Yakkasaroy tumani" in list:
                tosh_shahar["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
            else:
                tosh_shahar["Yakkasaroy tumani"] = "Yakkasaroy tumani"
            if "Yashnobod tumani" in list:
                tosh_shahar["✅Yashnobod tumani"] = "Yashnobod tumani"
            else:
                tosh_shahar["Yashnobod tumani"] = "Yashnobod tumani"

            shaxsiy_tosh_shahar = InlineKeyboardMarkup(row_width=3)
            for key, value in tosh_shahar.items():
                shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_tosh_shahar.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("tosh_shaharning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_tosh_shahar)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()

        if call.data == 'qoraqalpoq':
            qoraqalpoq = {}
            if "Nukus shahri" in list:
                qoraqalpoq["✅Nukus shahri"] = "Nukus shahri"
            else:
                qoraqalpoq["Nukus shahri"] = "Nukus shahri"
            if "Amudaryo tumani" in list:
                qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
            else:
                qoraqalpoq["Amudaryo tumani"] = 'Amudaryo tumani'
            if "Beruniy tumani" in list:
                qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
            else:
                qoraqalpoq["Beruniy tumani"] = "Beruniy tumani"
            if "Kegeyli tumani" in list:
                qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
            else:
                qoraqalpoq["Kegeyli tumani"] = 'Kegeyli tumani'
            if "Qanliko‘l tumani" in list:
                qoraqalpoq["✅Qanliko‘l tumani"] = 'Qanliko‘l tumani'
            else:
                qoraqalpoq["Qanliko‘l tumani"] = 'Qanliko‘l tumani'
            if "Qorao‘zak tumani" in list:
                qoraqalpoq["✅Qorao‘zak tumani"] = "Qorao‘zak tumani"
            else:
                qoraqalpoq["Qorao‘zak tumani"] = 'Qorao‘zak tumani'
            if "Qo‘ng‘irot tumani" in list:
                qoraqalpoq["✅Qo‘ng‘irot tumani"] = "Qo‘ng‘irot tumani"
            else:
                qoraqalpoq["Qo‘ng‘irot tumani"] = 'Qo‘ng‘irot tumani'
            if "Mo‘ynoq tumani" in list:
                qoraqalpoq["✅Mo‘ynoq tumani"] = "Mo‘ynoq tumani"
            else:
                qoraqalpoq["Mo‘ynoq tumani"] = "Mo‘ynoq tumani"
            if "Nukus tumani" in list:
                qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
            else:
                qoraqalpoq["Nukus tumani"] = 'Nukus tumani'
            if "Taxiatosh tumani" in list:
                qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
            else:
                qoraqalpoq["Taxiatosh tumani"] = 'Taxiatosh tumani'
            if "Taxtako‘pir tumani" in list:
                qoraqalpoq["✅Taxtako‘pir tumani"] = "Taxtako‘pir tumani"
            else:
                qoraqalpoq["Taxtako‘pir tumani"] = 'Taxtako‘pir tumani'
            if "To‘rtko‘l tumani" in list:
                qoraqalpoq["✅To‘rtko‘l tumani"] = "To‘rtko‘l tumani"
            else:
                qoraqalpoq["To‘rtko‘l tumani"] = "To‘rtko‘l tumani"
            if "Xo‘jayli tumani" in list:
                qoraqalpoq["✅Xo‘jayli tumani"] = "Xo‘jayli tumani"
            else:
                qoraqalpoq["Xo‘jayli tumani"] = "Xo‘jayli tumani"
            if "Chimboy tumani" in list:
                qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
            else:
                qoraqalpoq["Chimboy tumani"] = "Chimboy tumani"
            if "Sho‘manoy tumani" in list:
                qoraqalpoq["✅Sho‘manoy tumani"] = "Sho‘manoy tumani"
            else:
                qoraqalpoq["Sho‘manoy tumani"] = "Sho‘manoy tumani"
            if "Ellikqal’a tumani" in list:
                qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal’a tumani"
            else:
                qoraqalpoq["Ellikqal’a tumani"] = "Ellikqal’a tumani"

            shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
            for key, value in qoraqalpoq.items():
                shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
            shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
            await call.message.answer("Qoraqalpog'istonning qaysi tumanlaridan yuk olasiz ?", reply_markup=shaxsiy_qoraqalpoq)
            await Yuk_reys_andijon.tuman_yol.set()
            await call.message.delete()
        if call.data == "Olinmaydi":
            data = await state.get_data()
            msg = data.get("msg")
            mashina_turi = data.get('mashina_turi')
            mashina = f"🚗 <b>Mashina turi : {mashina_turi}</b>\n"
            if mashina_turi == "Kiritilmadi":
                mashina = ""
            yol_haqqi = data.get("yol_haqqi")
            yolkira = f"💲 <b>Yo'l haqqi: {yol_haqqi}</b>\n"
            if yol_haqqi == "Kiritilmadi":
                yolkira = ""
            kapot = data.get("kapot")
            kap = f"⁉️ <b>Kapot bo'shmi ? - {kapot}</b>\n"
            if kapot == "Kiritilmadi":
                kap = ""
            bagaj = data.get("bagaj")
            bag = f"⁉️ <b>Bagaj bo'shmi ? - {bagaj}</b>\n"
            if bagaj == "Kiritilmadi":
                bag = ""
            tonna=data.get("tonna")
            ton = f"⁉️ <b>Necha tonnagacha yuk olinadi ? - {tonna}</b>"

            if tonna is None:
                ton=""

            msg_full = msg + f"{mashina}" \
                             f"{kap}" \
                             f"{bag}" \
                             f"{ton}"\
                             f"{yolkira}"
            jamii = await db.select_all_yoldan_odam()
            list = []
            for i in jamii:
                if i[2] == call.from_user.id:
                    list.append(i[1])
            for a in list:
                await db.delete_yoldan_odam(telegram_id=call.from_user.id, tuman=a)
            list_1 = []
            viloyat_jami = await db.select_all_sayohat_info()
            for i in viloyat_jami:
                if i[2] == call.from_user.id:
                    list_1.append(i[1])
            for b in list_1:
                await db.delete_sayohat_info(telegram_id=call.from_user.id, viloyat=b)
            await state.update_data(
                {
                    "msg_full": msg_full
                }
            )
            await call.message.answer(f"Ma'lumotar to'g'rimi ?\n{msg_full}", reply_markup=tasdiq_oxir)
            await Yuk_reys_andijon.end.set()
            await call.message.delete()
        if call.data == 'tanladim':
            tartib = ""
            data = await state.get_data()
            yolda = data.get("yo'ldagilar")
            if yolda is not None:

                for i in yolda:
                    if i == "boshqaviloyat":
                        yolda.remove(i)
                    if i == "qaytamiz":
                        yolda.remove(i)
                    if i == "glavmenu":
                        yolda.remove(i)
                tartib = f"⁉️ <b>Yo'ldagi qaysi tumanlardan yuk olinadi ?</b>\n" + ",".join(yolda)
            await state.update_data(
                {
                    "yo'ldagilar": yolda
                }
            )
            # @dp.callback_query_handler(state=Yuk_reys_andijon.odam)
            # async def reys_odam(call:CallbackQuery,state:FSMContext):

            data = await state.get_data()
            msg = data.get("msg")

            mashina_turi = data.get('mashina_turi')
            mashina = f"🚚 <b>Mashina turi : {mashina_turi}</b>\n"
            if mashina_turi == "Kiritilmadi":
                mashina = ""
            yol_haqqi = data.get("yol_haqqi")
            yolkira = f"💲 <b>Yo'l haqqi: {yol_haqqi}</b>\n"
            if yol_haqqi == "Kiritilmadi":
                yolkira = ""
            kapot = data.get("kapot")
            kap = f"⁉️ <b>Kapot bo'shmi ? - {kapot}</b>\n"
            if kapot == "Kiritilmadi":
                kap = ""
            bagaj = data.get("bagaj")
            bag = f"⁉️ <b>Bagaj bo'shmi ? - {bagaj}</b>\n"
            if bagaj == "Kiritilmadi":
                bag = ""
            tonna = data.get("tonna")
            ton = f"⁉️ <b>Necha tonnagacha yuk olinadi ? - {tonna}</b>\n"
            if tonna is None:
                ton = ""
            msg_full = msg + f"{mashina}" \
                             f"{kap}" \
                             f"{bag}" \
                             f"{ton}" \
                             f"{yolkira}" \
                             f"{tartib}"
            jamii = await db.select_all_yoldan_odam()
            list = []
            for i in jamii:
                if i[2] == call.from_user.id:
                    list.append(i[1])
            for a in list:
                await db.delete_yoldan_odam(telegram_id=call.from_user.id, tuman=a)
            list_1 = []
            viloyat_jami = await db.select_all_sayohat_info()
            for i in viloyat_jami:
                if i[2] == call.from_user.id:
                    list_1.append(i[1])
            for b in list_1:
                await db.delete_sayohat_info(telegram_id=call.from_user.id, viloyat=b)
            await state.update_data(
                {
                    "msg_full": msg_full
                }
            )
            await call.message.answer(f"Ma'lumotar to'g'rimi ?\n{msg_full}", reply_markup=tasdiq_oxir)
            await call.message.delete()
            await Yuk_reys_andijon.end.set()
@dp.callback_query_handler(text='boshmenu', state=Yuk_reys_andijon.end)
async def boshmenuga(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text='qaytish', state=Yuk_reys_andijon.end)
async def qayiys(call: CallbackQuery, state: FSMContext):
    
        viloyat = {
            "Andijon": "andijon",
            "Namangan": "namangan",
            "Farg'ona": "farg'ona",
            "Buxoro": "buxoro",
            "Toshkent": "toshkent",
            "Toshkent shahri": "kent shahar",
            "Sirdaryo": "sirdaryo",
            "Surxondaryo": "surxondaryo",
            "Qashqadaryo": "qashqadaryo",
            "Xorazm": "xorazm",
            "Navoiy": "navoiy",
            "Jizzax": "jizzax",
            "Samarqand": "samarqand",
            "Keyingisi": "Olinmaydi",
            "Tanlab bo'ldim": "tanladim",
            "Ortga": "ortga",
            "Bosh menu": "boshmenu",
        }
        viloyatlar_yol = InlineKeyboardMarkup(row_width=3)
        for key, value in viloyat.items():
            viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Yo'lingizdagi qaysi tumanlardan qo'shimcha yuk olasiz ? ",
                                  reply_markup=viloyatlar_yol)
        await Yuk_reys_andijon.odam_vil.set()
        await call.message.delete()

@dp.callback_query_handler(text='glavmenu', state=Yuk_reys_andijon.end)
async def boshmenuga(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text='Confirm', state=Yuk_reys_andijon.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    
        data = await state.get_data()
        tuman = data.get('tuman')
        viloyat = data.get('viloyat')
        tumaniga = data.get('tumaniga')
        baza = data.get('baza')
        print(tuman)
        msg = data.get("msg_full")
        m = data.get("m")
        telegram_id = call.from_user.id
        print(telegram_id)
        await db.add_order_tayyor_taxi(tayyor_taxi=None,
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
            tayyor_yuk_haydovchisi=m,
            tayyor_yuk_haydovchisi_full=msg,
            tayyor_pochta_mashina=None,
            tayyor_pochta_mashina_full=None,
            tayyor_sayohatchi=None,
            tayyor_sayohatchi_full=None,
            tayyor_sayohatchi_mashina=None,
            tayyor_sayohatchi_full_mashina=None
                                       )
        print("Qo'shildi")
        await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                                  "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu_1
                                  )
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
@dp.callback_query_handler(text='UnConfirm', state=Yuk_reys_andijon.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    
        await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu_1)
        await call.message.delete()
        try:
            await state.finish()
        except KeyError as e:
            print(f"KeyError: {e}")
