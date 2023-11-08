from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from handlers.users.edit_district.navoiy_edit import Konimex, Karmana, Qiziltepa, Xatirchi, Navbahor, Nurota, Tomdi, \
    Uchquduq
from keyboards.default.location import phone_number
from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import reys_ortgaa
from keyboards.inline.haydovchi_reys.haydovchi_sayohatchi_reys import taxi_sayohat_callback, tax_say_vil
from keyboards.inline.yolovchi.kirish import umumiy_menu, tasdiq_oxir
from keyboards.inline.yolovchi.navoiytuman import navoiy_yol
from keyboards.inline.yolovchi.soat import time
from keyboards.inline.yolovchi.xa_yoq import yes_not
from loader import dp, bot, db
from states.haydovchi_sayohat_reys_states import Hay_say_navoiy


@dp.callback_query_handler(taxi_sayohat_callback.filter(item_name='sod'))
async def reys(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "viloyat": "Navoiy"
        }
    )
    await call.message.answer("Sayohatchilarni qaysi tumandan olasiz ? ", reply_markup=navoiy_yol)
    await Hay_say_navoiy.tuman.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.tuman)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatdan sayohatchi kerak ? ", reply_markup=tax_say_vil)
    await state.finish()


#     2 -  BEKOR QILISH
@dp.callback_query_handler(text_contains='atmen', state=Hay_say_navoiy.tuman)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Hay_say_navoiy.tuman)
async def reys_tuman(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "tuman": call.data
        }
    )
    await call.message.answer("Qaysi viloyatlarga borasiz ? ( Yozma shaklda kiriting ) ",reply_markup=reys_ortgaa)
    await Hay_say_navoiy.viloyatga.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.viloyatga)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Sayohatchilarni qaysi tumandan olasiz ? ", reply_markup=navoiy_yol)
    await Hay_say_navoiy.tuman.set()


@dp.callback_query_handler(text_contains='atmen', state=Hay_say_navoiy.viloyatga)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()

@dp.message_handler(state=Hay_say_navoiy.viloyatga)
async def reys_tumaniga(message: Message, state: FSMContext):
    await state.update_data(
        {
            "manzillar": message.text
        }
    )
    await message.answer("Yo'lga chiqadigan sanangizni yozing. ( M-n : 11.07.2023 )", reply_markup=reys_ortgaa)
    await Hay_say_navoiy.kuni.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.kuni)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi viloyatlarga borasiz ? ( Yozma shaklda kiriting ) ",reply_markup=reys_ortgaa)
    await Hay_say_navoiy.viloyatga.set()


@dp.callback_query_handler(text_contains='atmen', state=Hay_say_navoiy.kuni)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.message_handler(state=Hay_say_navoiy.kuni)
async def reys_kuni(message: Message, state: FSMContext):
    await state.update_data(
        {
            "kuni": message.text
        }
    )
    await message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await Hay_say_navoiy.soat.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.soat)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Yo'lga chiqadigan sanangizni yozing. ( M-n : 11.07.2023 )", reply_markup=reys_ortgaa)
    await Hay_say_navoiy.kuni.set()


@dp.callback_query_handler(text_contains='atmen', state=Hay_say_navoiy.soat)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\n"
                              "Sizga kerakli hizmat turini belgilang ?",
                              reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(state=Hay_say_navoiy.soat)
async def reys_soat(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "soat": call.data
        }
    )
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=reys_ortgaa)
    await Hay_say_navoiy.phone.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.phone)
async def andi_jon(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Soat nechchida yo'lga chiqasiz ? ", reply_markup=time)
    await Hay_say_navoiy.soat.set()


@dp.callback_query_handler(text_contains='atmen', state=Hay_say_navoiy.phone)
async def haydovchi(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()


@dp.message_handler(content_types=['contact', 'text'], state=Hay_say_navoiy.phone)
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
    manzillar = data.get("manzillar")
    kuni = data.get('kuni')
    soat = data.get('soat')
    phone = data.get('phone')

    msg = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan \n" \
          f"{manzillar} ga boruvchi sayohat mashinasi bor \n" \
          f"Sanasi : {kuni}\n" \
          f"{soat}\n" \
          f"Tel : {phone}\n"
    await state.update_data(
        {
            "msg": msg
        }
    )
    m = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan \n" \
          f"{manzillar} ga boruvchi sayohat mashinasi bor \n" \
          f"Sanasi : {kuni}\n" \
          f"{soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    await message.answer(msg)
    await message.answer("Ma'lumotlar to'g'rimi?", reply_markup=yes_not)
    await Hay_say_navoiy.tasdiqlash.set()


@dp.callback_query_handler(text='ortga', state=Hay_say_navoiy.tasdiqlash)
async def reys_ortga(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Telefon raqamingizni kiriting ..", reply_markup=phone_number)
    await call.message.answer("Mana shu raqamni ishlatayotgan bo'lsangiz\n"
                              "Kontakt yuborish ni bosing", reply_markup=reys_ortgaa)
    await Hay_say_navoiy.phone.set()


@dp.callback_query_handler(text='yesss', state=Hay_say_navoiy.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    tumaniga = data.get('tumaniga')
    manzillar = data.get('manzillar')
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
                                   viloyatga=manzillar,
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
                                   tayyor_sayohatchi_mashina=m,
                                   tayyor_sayohatchi_full_mashina=msg)
    print("Qo'shildi")
    order = await db.select_tayyor_sayohatchi()
    print(order)

    await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    await state.finish()


@dp.callback_query_handler(text='nott', state=Hay_say_navoiy.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()


@dp.callback_query_handler(text='add_information', state=Hay_say_navoiy.tasdiqlash)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Mahsinangiz qanday ? :   ")
    await Hay_say_navoiy.xa_yoq.set()


@dp.message_handler(state=Hay_say_navoiy.xa_yoq)
async def kisi(message: Message, state: FSMContext):
    await state.update_data(
        {
            "mashina_turi": message.text
        }
    )
    await message.answer("Yo'l haqqi uchun qancha olasiz ? ")
    await Hay_say_navoiy.pochta_olasizmi.set()


@dp.message_handler(state=Hay_say_navoiy.pochta_olasizmi)
async def reys_pochta_olasizmi(message: Message, state: FSMContext):
    await state.update_data(
        {
            "yolkira": message.text
        }
    )
    await message.answer("Jami nechta odam olasiz ?")
    await Hay_say_navoiy.odam.set()



@dp.message_handler(state=Hay_say_navoiy.odam)
async def reys_odam(message: Message, state: FSMContext):
    await state.update_data(
        {
            "jami_odam": message.text
        }
    )
    data = await state.get_data()
    msg = data.get("msg")
    mashina_turi = data.get('mashina_turi')
    yol_haqqi = data.get("yolkira")
    odam_soni = data.get("jami_odam")
    msg_full = msg + f"Mashina turi : {mashina_turi}\n" \
                     f"Yo'l haqqi ? - {yol_haqqi} \n" \
                     f"Jami olinadigan yo'lovchilar soni : {odam_soni}\n"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await message.answer(msg_full)
    await message.answer("Ma'lumotar to'g'rimi ?", reply_markup=tasdiq_oxir)
    await Hay_say_navoiy.end.set()


@dp.callback_query_handler(text='Confirm', state=Hay_say_navoiy.end)
async def oxirgi(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    tuman = data.get('tuman')
    tumaniga = data.get('tumaniga')
    manzillar = data.get('manzillar')
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
                                   viloyatga=manzillar,
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
                                   tayyor_sayohatchi_mashina=m,
                                   tayyor_sayohatchi_full_mashina=msg)
    print("Qo'shildi")
    order = await db.select_tayyor_sayohatchi()
    print(order)

    await call.message.answer("Sizning buyurtmangiz tumaningiz yo'lovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )

    await state.finish()


@dp.callback_query_handler(text='UnConfirm', state=Hay_say_navoiy.end)
async def y_n(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()

