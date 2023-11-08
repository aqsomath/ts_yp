from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from handlers.users.edit_district.namangan_edit import Chortoq, Chust, Kosonsoy, Mingbuloq, Namanganshaxar, Pop, Norin, \
    Toraqorgon, Uchqorgon, Uychi, Yangiqorgon, Davlatobod, YangiNamangan
from keyboards.default.location import phone_number, lokatsiya
from keyboards.inline.haydovchi_reys.haydovchi_pochta_reys import taxi_pochta_callback
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import taxi_reys_callback, tax_resy_vil, reys_ortgaa
from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import taxi_yuk_callback
from keyboards.inline.yolovchi import xa_yoq
from keyboards.inline.yolovchi.andtuman import andijon_yol
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
from keyboards.inline.yolovchi.viloyatlar import viloyatlar_yol_x
from keyboards.inline.yolovchi.xa_yoq import yes_not
from keyboards.inline.yolovchi.xorazmtuman import xorazm_yol
from loader import dp, bot, db
from states.haydovchi_pochta_states import Reys_pochta_namangan


@dp.callback_query_handler(taxi_pochta_callback.filter(item_name='dva'))
async def reys(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "viloyat": "Namangan"
        }
    )
    await call.message.answer("Yukni qaysi tumandan olasiz ? ", reply_markup=namangan_yol)
    await Reys_pochta_namangan.tuman.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatdan yuk kerak ? ", reply_markup=tax_resy_vil)
    await state.finish()


#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.tuman)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Reys_pochta_namangan.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "tuman": call.data
        }
    )
    await call.message.answer("Qaysi viloyatga yuk olib borasiz ? ", reply_markup=viloyatlar_yol_x)
    await Reys_pochta_namangan.viloyatga.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.viloyatga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi tumanidan ketasiz ? ", reply_markup=namangan_yol)  #############
    await Reys_pochta_namangan.tuman.set()


@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.viloyatga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Reys_pochta_namangan.viloyatga)
async def reys_viloyatga(call: CallbackQuery, state: FSMContext):
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
    await Reys_pochta_namangan.tumaniga.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.tumaniga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga borasiz ? ", reply_markup=viloyatlar_yol_x)
    await Reys_pochta_namangan.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.tumaniga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Reys_pochta_namangan.tumaniga)
async def reys_tumaniga(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "tumaniga": call.data.capitalize()
        }
    )
    await call.message.answer("Yo'lga chiqadigan sanangizni yozing. ( M-n : 11.07.2023 )", reply_markup=reys_ortgaa)
    await Reys_pochta_namangan.kuni.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatga yuk olib borasiz ? ", reply_markup=viloyatlar_yol_x)
    await Reys_pochta_namangan.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.kuni)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.message_handler(state=Reys_pochta_namangan.kuni)
async def reys_kuni(message: Message, state: FSMContext):
    await state.update_data(
        {
            "kuni": message.text
        }
    )
    await message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await Reys_pochta_namangan.soat.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Yo'lga chiqadigan sanangizni yozing. ( M-n : 11.07.2023 )", reply_markup=reys_ortgaa)
    await Reys_pochta_namangan.kuni.set()


@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.soat)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\n"
                              "Sizga kerakli hizmat turini belgilang ?",
                              reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Reys_pochta_namangan.soat)
async def reys_soat(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "soat": call.data
        }
    )
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=reys_ortgaa)
    await Reys_pochta_namangan.phone.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await Reys_pochta_namangan.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Reys_pochta_namangan.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.message_handler(content_types=['contact', 'text'], state=Reys_pochta_namangan.phone)
async def reys_loc(message: Message, state: FSMContext):
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
    viloyatiga = data.get('viloyatiga')
    tumaniga = data.get('tumaniga')
    kuni = data.get('kuni')
    soat = data.get('soat')
    phone = data.get('phone')
    m = f"{viloyat} viloyati\n" \
        f"{tuman} tumanidan \n" \
        f"{viloyatiga} viloyati\n" \
        f"{tumaniga} tumaniga boruvchi pochta haydovchi bor\n" \
        f"Sanasi : {kuni}\n" \
        f"{soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    msg = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan \n" \
          f"{viloyatiga} viloyati\n" \
          f"{tumaniga} tumaniga boruvchi pochta haydovchi bor\n" \
          f"Sanasi : {kuni}\n" \
          f"{soat}\n" \
          f"Tel : {phone}\n"
    await state.update_data(
        {
            "msg": msg
        }
    )
    await message.answer(msg)
    await message.answer("Ma'lumotlar to'g'rimi?", reply_markup=yes_not)
    await Reys_pochta_namangan.tasdiqlash.set()


@dp.callback_query_handler(text='ortga', state=Reys_pochta_namangan.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=reys_ortgaa)
    await Reys_pochta_namangan.phone.set()


@dp.callback_query_handler(text='yesss', state=Reys_pochta_namangan.tasdiqlash)
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
    await db.add_order_tayyor_taxi(
        tayyor_taxi=None,
        tayyor_taxi_full=None,
        tayyor_yolovchi=None,
        tayyor_yolovchi_full=None,
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
        tayyor_pochta_mashina=m,
        tayyor_pochta_mashina_full=msg,
        tayyor_sayohatchi=None,
        tayyor_sayohatchi_full=None,
        tayyor_sayohatchi_mashina=None,
        tayyor_sayohatchi_full_mashina=None

                                   )
    print("Qo'shildi")
    order = await db.select_tayyor_pochta()
    print(order)
    await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    await state.finish()


@dp.callback_query_handler(text='nott', state=Reys_pochta_namangan.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(text='add_information', state=Reys_pochta_namangan.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Mahsinangiz qanday ? :   ")
    await Reys_pochta_namangan.xa_yoq.set()


@dp.message_handler(state=Reys_pochta_namangan.xa_yoq)
async def kisi(message: Message, state: FSMContext):
    await state.update_data(
        {
            "mashina_turi": message.text
        }
    )
    await message.answer("Kapot bo'shmi..? ( xa yoki yo'q )")
    await Reys_pochta_namangan.pochta_olasizmi.set()


@dp.message_handler(state=Reys_pochta_namangan.pochta_olasizmi)
async def reys_pochta_olasizmi(message: Message, state: FSMContext):
    await state.update_data(
        {
            "kapot": message.text
        }
    )
    await message.answer("Bagaj bo'shmi.. ? (xa yoki yo'q )")
    await Reys_pochta_namangan.yuk_olasizmi.set()


@dp.message_handler(state=Reys_pochta_namangan.yuk_olasizmi)
async def yuk_olasizmi_reys(message: Message, state: FSMContext):
    await state.update_data(
        {
            "bagaj": message.text
        }
    )
    await message.answer("Yo'l haqqi uchun qancha olasiz ? ")
    await Reys_pochta_namangan.jami_odam.set()


@dp.message_handler(state=Reys_pochta_namangan.jami_odam)
async def jami_odam(message: Message, state: FSMContext):
    await state.update_data(
        {
            "yol_haqqi": message.text
        }
    )
    await message.answer("Yo'lingizdagi qaysi tumanlardan qo'shimcha pochta olasiz ? ")
    await Reys_pochta_namangan.odam.set()


@dp.message_handler(state=Reys_pochta_namangan.odam)
async def reys_odam(message: Message, state: FSMContext):
    await state.update_data(
        {
            "qoshimcha_yuk": message.text
        }
    )
    data = await state.get_data()
    msg = data.get("msg")

    mashina_turi = data.get('mashina_turi')
    yol_haqqi = data.get("yol_haqqi")
    kapot = data.get("kapot")
    bagaj = data.get("bagaj")
    qoshimcha_yuk = data.get("qoshimcha_yuk")
    msg_full = msg + f"Mashina turi : {mashina_turi}\n" \
                     f"Kapot bo'shmi ? - {kapot} \n" \
                     f"Bagaj bo'shmi ? - {bagaj} \n" \
                     f"Yo'ldagi qaysi \ntumanlardan qo'shimcha \npochta olinadi : {qoshimcha_yuk}\n" \
                     f"Yo'l haqqi : {yol_haqqi}\n"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await message.answer(msg_full)
    await message.answer("Ma'lumotar to'g'rimi ?", reply_markup=tasdiq_oxir)
    await Reys_pochta_namangan.end.set()


@dp.callback_query_handler(text='Confirm', state=Reys_pochta_namangan.end)
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
    await db.add_order_tayyor_taxi(
        tayyor_taxi=None,
        tayyor_taxi_full=None,
        tayyor_yolovchi=None,
        tayyor_yolovchi_full=None,
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
        tayyor_pochta_mashina=m,
        tayyor_pochta_mashina_full=msg,
        tayyor_sayohatchi=None,
        tayyor_sayohatchi_full=None,
        tayyor_sayohatchi_mashina=None,
        tayyor_sayohatchi_full_mashina=None
    )
    print("Qo'shildi")
    await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )

    await state.finish()


@dp.callback_query_handler(text='UnConfirm', state=Reys_pochta_namangan.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()

