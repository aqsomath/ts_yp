from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from handlers.users.edit_district.xorazm_edit import Bogot, Gurlan, Xonqa, Hazorasp, Xiva, Qoshkopir, Shovot, Yangiariq, \
    Urganch, Yangibozor, Tupproqqala
from keyboards.default.location import lokatsiya, phone_number, keyingisi, orqaga_qaytish
from keyboards.inline.yolovchi.andtuman import  andijon_yol
from keyboards.inline.yolovchi.buxtuman import buxoro_yol
from keyboards.inline.yolovchi.callback_data import time_callback
from keyboards.inline.yolovchi.fartuman import fargona_yol
from keyboards.inline.yolovchi.jizztuman import jizzax_yol
from keyboards.inline.yolovchi.kirish import umumiy_menu, necha_kishisizlar, oldi_kerakmi, qanday_avto, tasdiq_oxir
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
from states.yolovchi_reys_states import Yolovchi_xorazm
from keyboards.inline.yolovchi.viloyatlar import  viloyatlar_yol_x
from loader import dp, bot, db
from utils.misc import show_on_gmaps
#  1 - ORTGA
@dp.callback_query_handler(text_contains='atmen',state=None)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text_contains="xorazm",state=None)
async def adnijonyolovchi(call:CallbackQuery,state: FSMContext):
    await state.update_data(
        {"viloyat":"Xorazm"}
    )
    await call.message.answer("Qaysi tumandan ketasiz :",reply_markup=xorazm_yol)
    await Yolovchi_xorazm.viloyatga.set()
# 2 - ORTGA
@dp.callback_query_handler(text='ortga', state=Yolovchi_xorazm.viloyatga)
async def orqaga(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qayerdan yurmoqchisiz ? \n",reply_markup=viloyatlar_yol_x)
    await state.finish()
# 2 -  BEKOR QILISH
@dp.callback_query_handler(text='atmen',state=Yolovchi_xorazm.viloyatga)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(state=Yolovchi_xorazm.viloyatga)
async def tuman_andijon(call:CallbackQuery, state:FSMContext):
    await state.update_data(
        {"tuman":call.data}
    )
    await call.message.answer("Qaysi viloyatga borasiz? ", reply_markup=viloyatlar_yol_x)
    await Yolovchi_xorazm.tumaniga.set()
@dp.callback_query_handler(text='atmen',state=Yolovchi_xorazm.tumaniga)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
#  3 - ORTGA
@dp.callback_query_handler(text='ortga',state=Yolovchi_xorazm.tumaniga)
async def nazad(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi tumandan ketasiz :", reply_markup=xorazm_yol)
    await Yolovchi_xorazm.viloyatga.set()

@dp.callback_query_handler(state=Yolovchi_xorazm.tumaniga)
async def tuman_andijon(call:CallbackQuery, state:FSMContext):
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

    await Yolovchi_xorazm.soat.set()


#  4 - BEKOR QILISH
@dp.callback_query_handler(text='atmen', state=Yolovchi_xorazm.soat)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


# 4 - ORTGA
@dp.callback_query_handler(text='ortga', state=Yolovchi_xorazm.soat)
async def ketish_soati(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga borasiz? ", reply_markup=viloyatlar_yol_x)
    await Yolovchi_xorazm.tumaniga.set()


@dp.callback_query_handler(state=Yolovchi_xorazm.soat)
async def ketish_soati(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"tumaniga": call.data.capitalize()}
    )
    await call.message.answer("Soat nechchida yo'lga chiqmoqchisiz ?", reply_markup=time)
    await Yolovchi_xorazm.phone.set()


#   5 - BEKOR QILISH
@dp.callback_query_handler(text='atmen', state=Yolovchi_xorazm.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


# 5 - ORTGA
@dp.callback_query_handler(time_callback.filter(item_name='ortga'), state=Yolovchi_xorazm.phone)
async def phone(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga borasiz? ", reply_markup=viloyatlar_yol_x)
    await Yolovchi_xorazm.tumaniga.set()


@dp.callback_query_handler(state=Yolovchi_xorazm.phone)
async def phone(call: CallbackQuery, state: FSMContext):
    print(call.data)
    await state.update_data(
        {
            "soat": call.data
        }
    )
    await call.message.answer("Sizga bog'lana oladiga telefon raqamingizni kiriting: ", reply_markup=phone_number)
    await call.message.answer("Na'muna: 994813499 ?", reply_markup=orqaga_qaytish)
    await Yolovchi_xorazm.locatsiya.set()


#  6 - BEKOR QILISH
@dp.callback_query_handler(text='atmen', state=Yolovchi_xorazm.locatsiya)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


#  6 - ORTGA
@dp.callback_query_handler(text='ortga', state=Yolovchi_xorazm.locatsiya)
async def phone(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Soat nechchida yo'lga chiqmoqchisiz ?", reply_markup=time)
    await Yolovchi_xorazm.phone.set()


@dp.message_handler(content_types=['contact', 'text'], state=Yolovchi_xorazm.locatsiya)
async def location(message: Message, state: FSMContext):
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
    await Yolovchi_xorazm.tasdiqlash.set()


#     7 - BEKOR QILISH
@dp.callback_query_handler(text='atmen', state=Yolovchi_xorazm.tasdiqlash)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


#     7 - ORTGA
@dp.callback_query_handler(text='ortga', state=Yolovchi_xorazm.tasdiqlash)
async def orqatomon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Sizga bog'lana oladiga telefon raqamingizni kiriting: ", reply_markup=phone_number)
    await call.message.answer("Na'muna: 994813499 ?", reply_markup=orqaga_qaytish)
    await Yolovchi_xorazm.locatsiya.set()


@dp.message_handler(content_types=['location'], state=Yolovchi_xorazm.tasdiqlash)
async def location(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    place = show_on_gmaps.show(lat=lat, lon=lon)
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
          f"<b>{ketish_tumani} tumaniga {soat} da  boruvchi yo'lovchi bor</b>\n" \
          f"<i><b>Telefon raqam</b></i> : {phone}\n" \
          f"<b>Lokatsiya :</b>\n" \
          f"{place}"
    await state.update_data(
        {
            "msg": msg
        }
    )
    m = f"<b>{turgan_viloyati} viloyati,\n</b>" \
        f"<b>{turgan_tumani} tumanidan</b>\n" \
        f"<b>{ketish_viloyati} viloyati</b>\n" \
        f"<b>{ketish_tumani} tumaniga {soat} da  boruvchi yo'lovchi bor</b>\n"
    await state.update_data(
        {
            "m": m
        }
    )

    await message.answer(msg)
    await message.answer("Malumotlaringiz to'g'rimi ?", reply_markup=yes_not)
    await Yolovchi_xorazm.xa_yoq.set()


#     8 - BEKOR QILISH
@dp.callback_query_handler(text='atmen', state=Yolovchi_xorazm.xa_yoq)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


#     8 - ORTGA
@dp.callback_query_handler(text="ortga", state=Yolovchi_xorazm.xa_yoq)
async def keyin(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Sizni topib borish uchun lokatsiyangizni yuboring. ", reply_markup=lokatsiya)
    await call.message.answer("Agar istamasangiz 'Keyingisi' ni bosing.", reply_markup=keyingisi)
    await Yolovchi_xorazm.tasdiqlash.set()


@dp.callback_query_handler(text="yingisi", state=Yolovchi_xorazm.tasdiqlash)
async def keyin(call: CallbackQuery, state: FSMContext):
    place = "Lokatsiya yuborilmadi"
    data = await state.get_data()
    turgan_viloyati = data.get('viloyat')
    turgan_tumani = data.get('tuman')
    ketish_viloyati = data.get('viloyatiga')
    ketish_tumani = data.get('tumaniga')
    soat = data.get('soat')
    phone = data.get('phone')
    m = f"{turgan_viloyati} viloyati\n" \
        f"{turgan_tumani} tumanidan \n" \
        f"{ketish_viloyati} viloyati\n" \
        f"<b>{ketish_tumani} tumaniga {soat} da  boruvchi yo'lovchi bor</b>\n" \
        f"{soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    msg = f"<b>{turgan_viloyati} viloyati,\n</b>" \
          f"<b>{turgan_tumani} tumanidan</b>\n" \
          f"<b>{ketish_viloyati} viloyati</b>\n" \
          f"<b>{ketish_tumani} tumaniga {soat} da  boruvchi yo'lovchi bor</b>\n" \
          f"<i><b>Telefon raqam</b></i> : {phone}\n" \
          f"<b>Lokatsiya :</b>\n" \
          f"{place}"
    await state.update_data(
        {
            "msg": msg
        }
    )
    await call.message.answer(msg)
    await call.message.answer("Malumotlaringiz to'g'rimi ?", reply_markup=yes_not)
    await Yolovchi_xorazm.xa_yoq.set()


@dp.callback_query_handler(text='yesss', state=Yolovchi_xorazm.xa_yoq)
async def y_n(call: CallbackQuery, state: FSMContext):
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
                                   tayyor_yolovchi=m,
                                   tayyor_yolovchi_full=msg,
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
    print("qo'shildi")
    order = await db.select_tayyor_yolovchi()
    print(order)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n"
                              )
    await state.finish()


@dp.callback_query_handler(text='nott', state=Yolovchi_xorazm.xa_yoq)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(text='add_information', state=Yolovchi_xorazm.xa_yoq)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Necha kishisizlar ? ", reply_markup=necha_kishisizlar)
    await Yolovchi_xorazm.necha_kishi.set()


@dp.callback_query_handler(state=Yolovchi_xorazm.necha_kishi)
async def kisi(call: CallbackQuery, state: FSMContext):
    print(call.data)
    await state.update_data(
        {
            "odam_soni": call.data
        }
    )
    await call.message.answer("Oldi o'rindiq kerakmi ?", reply_markup=oldi_kerakmi)
    await Yolovchi_xorazm.oldi_kerakmi.set()


@dp.callback_query_handler(state=Yolovchi_xorazm.oldi_kerakmi)
async def kisi(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "oldi_joy": call.data
        }
    )
    await call.message.answer("Avtomobil qanday bo'lsin ?", reply_markup=qanday_avto)
    await Yolovchi_xorazm.qanday_moshina.set()


@dp.callback_query_handler(state=Yolovchi_xorazm.qanday_moshina)
async def kisi(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "Avto_turi": call.data
        }
    )
    data = await state.get_data()
    msg = data.get("msg")
    odam_soni = data.get("odam_soni")
    oldi_orin = data.get("oldi_joy")
    avto_turi = data.get("Avto_turi")
    msg_full = msg + f"\nYo'lovchilar soni :{odam_soni}\n{oldi_orin}\nAvtomobil turi: {avto_turi}"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await call.message.answer(msg_full)
    await call.message.answer("Ma'lumotlaringiz to'g'rimi ? ", reply_markup=tasdiq_oxir)
    await Yolovchi_xorazm.end.set()


@dp.callback_query_handler(text='Confirm', state=Yolovchi_xorazm.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
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
                                   tayyor_yolovchi=m,
                                   tayyor_yolovchi_full=msg,
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
    print("qo'shildi")
    order = await db.select_tayyor_yolovchi()
    print(order)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    await state.finish()


@dp.callback_query_handler(text='UnConfirm', state=Yolovchi_xorazm.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()
