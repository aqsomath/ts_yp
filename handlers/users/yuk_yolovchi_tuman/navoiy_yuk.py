import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.default.location import phone_number, orqaga_qaytish, phone_ortga, lokatsiya, keyingisi
from keyboards.inline.yolovchi.andtuman import andijon_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import umumiy_menu, tasdiq_oxir
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol, viloyatlar_yol_x
from keyboards.inline.yuk_yuborish.yuk_tugmalari import yuk_callback, andijon_yuk, yuk_viloyatlar, qanaqa_avto
from loader import dp, bot, db
from states.yuk_states import Yuk_navoiy
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
from utils.misc import show_on_gmaps


@dp.callback_query_handler(yuk_callback.filter(item_name='101010'),state=None)
async def andi_jon(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "viloyat":"Navoiy"
        }
    )
    await call.message.answer("Qaysi tumanidan yuborasiz ? ",reply_markup=navoiy_yol)
    await Yuk_navoiy.tuman.set()
# 1 - ORTGA
@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.tuman)
async def andi_jon(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Yukni qaysi viloyatdan yuborasiz ?", reply_markup=yuk_viloyatlar)
    await state.finish()
#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.tuman)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(state=Yuk_navoiy.tuman)
async def tumanx(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "tuman":call.data
        }
    )
    print(call.data)
    await call.message.answer("Qaysi viloyatga yuk yubormoqchisiz ? ", reply_markup=viloyatlar_yol_x)
    await Yuk_navoiy.viloyatga.set()
@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.viloyatga)
async def ztumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi tumanidan yuborasiz ? ", reply_markup=navoiy_yol)### --->> MANA SHU O'ZGARISHI KERAK
    await Yuk_navoiy.tuman.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.viloyatga)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()

@dp.callback_query_handler(state=Yuk_navoiy.viloyatga)
async def viloyatga(call:CallbackQuery,state:FSMContext):
    data = call.data
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
    await state.update_data({"baza": data})
    await Yuk_navoiy.tumaniga.set()

@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.tumaniga)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatga yuk yubormoqchisiz ? ", reply_markup=viloyatlar_yol_x)
    await Yuk_navoiy.viloyatga.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.tumaniga)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()

@dp.callback_query_handler(state=Yuk_navoiy.tumaniga)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {"tumaniga": call.data.capitalize()}
    )
    await call.message.answer("Soat nechchilarda yubormoqchisiz ?",reply_markup=time)
    await Yuk_navoiy.soat.set()
@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.soat)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatga yuk yubormoqchisiz ? ", reply_markup=viloyatlar_yol_x)
    await Yuk_navoiy.viloyatga.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.soat)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Yuk_navoiy.soat)
async def soat(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "soat": call.data
        }
    )

    await call.message.answer("Sizga bog'lana oladiga telefon raqamingizni kiriting: ", reply_markup=phone_number)
    await call.message.answer("Na'muna: 994813499 ?", reply_markup=phone_ortga)
    await Yuk_navoiy.phone.set()
@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.phone)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Soat nechchilarda yubormoqchisiz ?", reply_markup=time)
    await Yuk_navoiy.soat.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.phone)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.message_handler(content_types=['contact', 'text'],state=Yuk_navoiy.phone)
async def message(message:Message,state:FSMContext):

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
        await message.answer("Sizni topib borish uchun lokatsiyangizni yuboring. ", reply_markup=lokatsiya)
        await message.answer("Agar istamasangiz 'Keyingisi' ni bosing.", reply_markup=keyingisi)
        await Yuk_navoiy.locatsiya.set()
@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.locatsiya)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sizga bog'lana oladiga telefon raqamingizni kiriting: ", reply_markup=phone_number)
    await call.message.answer("Na'muna: 994813499 ?", reply_markup=phone_ortga)
    await Yuk_navoiy.phone.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.locatsiya)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()

@dp.callback_query_handler(text="yingisi",state=Yuk_navoiy.locatsiya)
async def keyin_gisi(call:CallbackQuery,state:FSMContext):

    place = "Lokatsiya yuborilmadi"
    data = await state.get_data()
    turgan_viloyati = data.get('viloyat')
    turgan_tumani = data.get('tuman')
    ketish_viloyati = data.get('viloyatiga')
    ketish_tumani = data.get('tumaniga')
    soat = data.get('soat')
    phone = data.get('phone')
    msg = f"<b>{turgan_viloyati} viloyati,\n</b>" \
          f"<b>{turgan_tumani} tumanidan</b>\n" \
          f"<b>{ketish_viloyati} viloyati</b>\n" \
          f"<b>{ketish_tumani} tumaniga {soat} da yuborilishi kerak yuk</b>\n" \
          f"<b>Telefon raqam :</b>\n {phone}\n" \
          f"<b>Lokatsiya :</b>\n" \
          f"{place}"
    await state.update_data(
        {
            "msg": msg
        }
    )
    m = f"{turgan_viloyati} viloyati\n" \
        f"{turgan_tumani} tumanidan \n" \
        f"{ketish_viloyati} viloyati\n" \
        f"{ketish_tumani} tumaniga boruvchi haydovchi\n" \
        f"{soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    await call.message.answer(msg)
    await call.message.answer("Malumotlaringiz to'g'rimi ?", reply_markup=yes_not)
    await Yuk_navoiy.tasdiqlash.set()


@dp.message_handler(content_types=['location'],state=Yuk_navoiy.locatsiya)
async def location(message:Message, state:FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    place = show_on_gmaps.show(lat=lat, lon=lon)
    data =await state.get_data()
    turgan_viloyati = data.get('viloyat')
    turgan_tumani = data.get('tuman')
    ketish_viloyati = data.get('viloyatiga')
    ketish_tumani = data.get('tumaniga')
    soat = data.get('soat')
    yuk = data.get('yuk')
    phone = data.get('phone')
    msg = f"<b>{turgan_viloyati} viloyati,\n</b>" \
          f"<b>{turgan_tumani} tumanidan</b>\n" \
          f"<b>{ketish_viloyati} viloyati</b>\n" \
          f"<b>{ketish_tumani} tumaniga {soat} da  yuborilishi kerak yuk bor</b>\n" \
          f"<b>Yuk turi : {yuk}</b>\n"\
          f"<b>Telefon raqam :</b>\n {phone}\n" \
          f"<b>Lokatsiya :</b>\n" \
          f"{place}"
    await state.update_data(
        {
            "msg":msg
        }
    )
    m = f"<b>{turgan_viloyati} viloyati,\n</b>" \
          f"<b>{turgan_tumani} tumanidan</b>\n" \
          f"<b>{ketish_viloyati} viloyati</b>\n" \
          f"<b>{ketish_tumani} tumaniga {soat} da  yuborilishi kerak yuk bor</b>\n" \
          f"<b>Yuk turi : {yuk}</b>\n"
    await state.update_data(
        {
            "m": m
        }
    )
    await message.answer(msg)
    await message.answer("Malumotlaringiz to'g'rimi ?",reply_markup=yes_not)
    await Yuk_navoiy.tasdiqlash.set()

@dp.callback_query_handler(text='ortga',state=Yuk_navoiy.tasdiqlash)
async def tumaniga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sizni topib borish uchun lokatsiyangizni yuboring. ", reply_markup=lokatsiya)
    await call.message.answer("Agar istamasangiz 'Keyingisi' ni bosing.", reply_markup=keyingisi)
    await Yuk_navoiy.locatsiya.set()
@dp.callback_query_handler(text_contains='atmen',state=Yuk_navoiy.tasdiqlash)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='nott', state=Yuk_navoiy.tasdiqlash)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(text='yesss', state=Yuk_navoiy.tasdiqlash)
async def y_n(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    tumaniga = data.get('tumaniga')
    baza = data.get('baza')
    print(tuman)
    msg = data.get("msg")
    m = data.get("m")
    telegram_id = call.message.from_user.id
    print(telegram_id)
    await db.add_order_tayyor_taxi(tayyor_taxi=None,
                                   tayyor_taxi_full=None,
                                   tayyor_yolovchi=None,
                                   tayyor_yolovchi_full=None,
                                   region=tuman,
                                   telegram_id=telegram_id,
                                   viloyatga=baza,
                                   tumanga=tumaniga,
                                   tayyor_pochta=None,
                                   tayyor_pochta_full=None,
                                   tayyor_yuk=m,
                                   tayyor_yuk_full=msg,
                                   tayyor_yuk_haydovchisi=None,
                                   tayyor_yuk_haydovchisi_full=None,
                                   tayyor_pochta_mashina=None,
                                   tayyor_pochta_mashina_full=None,
                                   tayyor_sayohatchi=None,
                                   tayyor_sayohatchi_full=None,
                                   tayyor_sayohatchi_full_mashina=None,
                                   tayyor_sayohatchi_mashina=None)
    drivers = await db.select_all_driver()
    drivers_info = await db.select_all_driver_info()
    for i in drivers:
        if i[2] == 'ok':
            for k in drivers_info:
                if k[2] == tuman and i[4] == k[3]:
                    markup = aiogram.types.InlineKeyboardMarkup()
                    markup.insert(
                        aiogram.types.InlineKeyboardButton(text="Qabul qilish", callback_data='8D85S5S5D5'))
                    await bot.send_message(text=m, chat_id=k[3], reply_markup=markup)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n"
                              )
    await state.reset_state(with_data=False)


@dp.callback_query_handler(text="8D85S5S5D5")
async def qabul_qilish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg")
    await bot.send_message(text=msg, chat_id=call.from_user.id)
@dp.callback_query_handler(text='add_information', state=Yuk_navoiy.tasdiqlash)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Qanday yuk mashinasi kerak ? ",reply_markup= qanaqa_avto)
    await Yuk_navoiy.xa_yoq.set()
@dp.callback_query_handler(state=Yuk_navoiy.xa_yoq)
async def kisi(call:CallbackQuery,state:FSMContext):
    print(call.data)
    await state.update_data(
        {
            "Avto_turi":call.data
        }
    )
    await call.message.answer("Yuk turi qanday ? ( yozma shaklda kiriting ) ")
    await Yuk_navoiy.turi.set()
@dp.message_handler(state=Yuk_navoiy.turi)
async def yuk_turi(message:Message,state:FSMContext):
    await state.update_data(
        {
            "yuk_turi":message.text
        }
    )
    await message.answer("Yuk tashish uchun haydovchiga qancha bermoqchisiz ? ")
    await Yuk_navoiy.narx.set()
@dp.message_handler(state=Yuk_navoiy.narx)
async def yuk_narx(message:Message,state:FSMContext):
    await state.update_data(
        {
            "narxi":message.text
        }
    )
    data = await state.get_data()
    yuk_turi=data.get("yuk_turi")
    narxi=data.get("narxi")
    msg = data.get("msg")
    yuk_mashina = data.get("Avto_turi")
    msg_full = msg+f"\nYuk mashinasi : {yuk_mashina} yoki shunga o'xshash hajmli yuk mashinasi bo'lishi kerak.\n" \
                   f"Yuk turi: {yuk_turi}\n" \
                   f"Haydovchiga belgilangan narx : {narxi}"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await message.answer(msg_full)
    await message.answer("Ma'lumotar to'g'rimi ?", reply_markup=tasdiq_oxir)
    await Yuk_navoiy.end.set()
@dp.callback_query_handler(text='Confirm',state=Yuk_navoiy.end)
async def oxirgi(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    tumaniga = data.get('tumaniga')
    baza = data.get('baza')
    print(tuman)
    msg = data.get("msg_full")
    m = data.get("m")
    telegram_id = call.message.from_user.id
    print(telegram_id)
    await db.add_order_tayyor_taxi(tayyor_taxi=None,
                                   tayyor_taxi_full=None,
                                   tayyor_yolovchi=None,
                                   tayyor_yolovchi_full=None,
                                   region=tuman,
                                   telegram_id=telegram_id,
                                   viloyatga=baza,
                                   tumanga=tumaniga,
                                   tayyor_pochta=None,
                                   tayyor_pochta_full=None,
                                   tayyor_yuk=m,
                                   tayyor_yuk_full=msg,
                                   tayyor_yuk_haydovchisi=None,
                                   tayyor_yuk_haydovchisi_full=None,
                                   tayyor_pochta_mashina=None,
                                   tayyor_pochta_mashina_full=None,
                                   tayyor_sayohatchi=None,
                                   tayyor_sayohatchi_full=None,
                                   tayyor_sayohatchi_full_mashina=None,
                                   tayyor_sayohatchi_mashina=None)
    drivers = await db.select_all_driver()
    drivers_info = await db.select_all_driver_info()
    for i in drivers:
        if i[2] == 'ok':
            for k in drivers_info:
                if k[2] == tuman and i[4] == k[3]:
                    markup = aiogram.types.InlineKeyboardMarkup()
                    markup.insert(
                        aiogram.types.InlineKeyboardButton(text="Qabul qilish",
                                                           callback_data='8A7S8989S'))
                    await bot.send_message(text=m, chat_id=k[3], reply_markup=markup)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    await state.reset_state(with_data=False)


@dp.callback_query_handler(text="8A7S8989S")
async def qabul_qilish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg_full")
    await bot.send_message(text=msg, chat_id=call.from_user.id)


@dp.callback_query_handler(text='UnConfirm', state=Yuk_navoiy.end)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()