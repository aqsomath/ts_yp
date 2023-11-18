import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message


from keyboards.default.location import phone_number, lokatsiya, keyingisi
from keyboards.inline.sayohat_qilish.sayohat_viloyatlar import sayohat_callback, sayohat_vil
from keyboards.inline.yolovchi.andtuman import andijon_yol
from keyboards.inline.yolovchi.kirish import umumiy_menu, tasdiq_oxir
from keyboards.inline.yolovchi.navoiytuman import navoiy_yol
from keyboards.inline.yolovchi.soat import time
from keyboards.inline.yolovchi.xa_yoq import yes_not
from loader import dp, bot, db
from states.sayohat_states import Sayohat_navoiy
from utils.misc import show_on_gmaps


@dp.callback_query_handler(sayohat_callback.filter(item_name='avgust'))
async def andijon_sayohat(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "viloyat":"Navoiy"
        }
    )
    await call.message.answer("Navoiyning qaysi tumanidan yo'lga sayohatga yo'l olasiz ?", reply_markup=navoiy_yol)
    await Sayohat_navoiy.tuman.set()
@dp.callback_query_handler(text='atmen',state=Sayohat_navoiy.tuman)
async def haydovchi(call:CallbackQuery,state: FSMContext):
    await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='ortga',state=Sayohat_navoiy.tuman)
async def sayohat_asosiy(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan sayohatga chiqmoqchisiz ? ", reply_markup=sayohat_vil)
    await state.finish()


@dp.callback_query_handler(state=Sayohat_navoiy.tuman)
async def sayohat_tuman(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "tuman":call.data
        }
    )
    await call.message.answer("Sayohat qilmoqchi bo'lgan joylaringizni yozma shaklda kiriting ?",)
    await Sayohat_navoiy.sayohat_manzillari.set()


@dp.message_handler(state=Sayohat_navoiy.sayohat_manzillari)
async def manzillar(message:Message,state:FSMContext):
    await state.update_data(
        {
            "manzillar":message.text
        }
    )
    await message.answer("Sayohat qiladigan sanangizni kiriting :")
    await Sayohat_navoiy.sana.set()

@dp.message_handler(state=Sayohat_navoiy.sana)
async def manzillar(message:Message,state:FSMContext):
    await state.update_data(
        {
            "sana":message.text
        }
    )
    await message.answer("Soat nechchida sayohatga chiqasiz ?", reply_markup=time)
    await Sayohat_navoiy.soat.set()
@dp.callback_query_handler(text='atmen',state=Sayohat_navoiy.soat)
async def times(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sizga kerakli xizmat turini tanlang", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='ortga',state=Sayohat_navoiy.soat)
async def comeback(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sayohat qiladigan sanangizni kiriting :")
    await Sayohat_navoiy.sana.set()

@dp.callback_query_handler(state=Sayohat_navoiy.soat)
async def sayohat_soati(call:CallbackQuery,state:FSMContext):
    await state.update_data(
        {
            "soat":call.data
        }
    )
    await call.message.answer("Siz bilan bog'lana oladigan telefon raqammingizni kiriting\n"
                              "Agar mana shu raqamni ishlatsangiz ~Kontakt yuborish~ ni bosing",
                              reply_markup=phone_number)
    await Sayohat_navoiy.phone.set()
@dp.message_handler(content_types=['contact','text'],state=Sayohat_navoiy.phone)
async def kont(message:Message,state:FSMContext):
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
    await message.answer("Joylashgan joyingizni lokatsiyasini yuboring.",reply_markup=lokatsiya)
    await message.answer("Agar kerak bo'lmasa ~Keyingisi~ ni bosing",reply_markup=keyingisi)
    await Sayohat_navoiy.tasdiqlash.set()
@dp.callback_query_handler(text='atmen',state=Sayohat_navoiy.tasdiqlash)
async def ett(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Sizga kerakli xizmat turini tanlang", reply_markup=umumiy_menu)
    await state.finish()
@dp.callback_query_handler(text='ortga',state=Sayohat_navoiy.tasdiqlash)
async def tett(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Siz bilan bog'lana oladigan telefon raqammingizni kiriting\n"
                              "Agar mana shu raqamni ishlatsangiz ~Kontakt yuborish~ ni bosing",
                              reply_markup=phone_number)
    await Sayohat_navoiy.phone.set()

@dp.message_handler(content_types='location',state=Sayohat_navoiy.tasdiqlash)
async def lokatsiya_sayohat(message:Message,state:FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    place = show_on_gmaps.show(lat=lat, lon=lon)
    data = await state.get_data()
    viloyat = data.get('viloyat')
    tuman = data.get('tuman')
    manzil = data.get('manzillar')
    sana = data.get('sana')
    soat = data.get('soat')
    tel = data.get('phone')
    msg = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan " \
          f"Sayohat qilmoqchi bo'lgan sayohatchi bor.\n" \
          f"Sayohat manzillari : {manzil}\n" \
          f"Sayohatga chiqish vaqti: {sana} kuni {soat}\n" \
          f"Tel : {tel}\n" \
          f"Lokatsiya : {place}"
    await state.update_data(
        {
            "msg":msg
        }
    )
    m = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan " \
          f"Sayohat qilmoqchi bo'lgan sayohatchi bor.\n" \
          f"Sayohat manzillari : {manzil}\n" \
          f"Sayohatga chiqish vaqti: {sana} kuni {soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    await message.answer(msg)
    await message.answer("Malumotlaringiz to'g'rimi ?", reply_markup=yes_not)
    await Sayohat_navoiy.xa_yoq.set()

@dp.callback_query_handler(text='yingisi',state=Sayohat_navoiy.tasdiqlash)
async def lokatsiya_sayohat(call:CallbackQuery,state:FSMContext):

    place = "Lokatsiya yuborilmadi"
    data = await state.get_data()
    viloyat = data.get('viloyat')
    tuman = data.get('tuman')
    manzil = data.get('manzillar')
    sana = data.get('sana')
    soat = data.get('soat')
    tel = data.get('phone')
    msg = f"{viloyat} viloyati\n" \
          f"{tuman} tumanidan " \
          f"Sayohat qilmoqchi bo'lgan sayohatchi bor.\n" \
          f"Sayohat manzillari : {manzil}\n" \
          f"Sayohatga chiqish vaqti: {sana} kuni {soat}\n" \
          f"Tel : {tel}\n" \
          f"Lokatsiya : {place}"
    await state.update_data(
        {
            "msg":msg
        }
    )
    m = f"{viloyat} viloyati\n" \
        f"{tuman} tumanidan " \
        f"Sayohat qilmoqchi bo'lgan sayohatchi bor.\n" \
        f"Sayohat manzillari : {manzil}\n" \
        f"Sayohatga chiqish vaqti: {sana} kuni {soat}\n"
    await state.update_data(
        {
            "m": m
        }
    )
    await call.message.answer(msg)
    await call.message.answer("Malumotlaringiz to'g'rimi ?", reply_markup=yes_not)
    await Sayohat_navoiy.xa_yoq.set()

@dp.callback_query_handler(text='yesss', state=Sayohat_navoiy.xa_yoq)
async def y_n(call:CallbackQuery, state:FSMContext):
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
                                   tayyor_sayohatchi=m,
                                   tayyor_sayohatchi_full=msg,
                                   tayyor_sayohatchi_full_mashina=None,
                                   tayyor_sayohatchi_mashina=None)
    drivers = await db.select_all_driver()
    drivers_info = await db.select_all_driver_info()
    for i in drivers:
        if i[5] == 'ok':
            for k in drivers_info:
                if k[2] == tuman and i[4] == k[3]:
                    markup = aiogram.types.InlineKeyboardMarkup()
                    markup.insert(
                        aiogram.types.InlineKeyboardButton(text="Qabul qilish", callback_data='xshdjodopdsppp'))
                    await bot.send_message(text=m, chat_id=k[3], reply_markup=markup)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n"
                              )
    await state.reset_state(with_data=False)


@dp.callback_query_handler(text="xshdjodopdsppp")
async def qabul_qilish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg")
    await bot.send_message(text=msg, chat_id=call.from_user.id)
@dp.callback_query_handler(text='nott', state=Sayohat_navoiy.xa_yoq)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()

@dp.callback_query_handler(text='add_information', state=Sayohat_navoiy.xa_yoq)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Necha kunlik sayohat qilmoqchisiz ? ")
    await Sayohat_navoiy.necha_kun.set()
@dp.message_handler(state=Sayohat_navoiy.necha_kun)
async def kuns(message:Message,state:FSMContext):
    await state.update_data(
        {
            "sayohat_kuni":message.text
        }
    )
    await message.answer("Necha kishisizlar ?")
    await Sayohat_navoiy.necha_kishi.set()

@dp.message_handler(state=Sayohat_navoiy.necha_kishi)
async def necha_sayyoh(message:Message,state:FSMContext):
    await state.update_data(
        {
            "sayyoh_soni": message.text
        }
    )
    await message.answer("Qancha to'lamoqchisiz ? ")
    await Sayohat_navoiy.qancha_narx.set()
@dp.message_handler(state=Sayohat_navoiy.qancha_narx)
async def narx_qancha(message:Message,state:FSMContext):
    await state.update_data(
        {
            "narx":message.text
        }
    )
    data = await state.get_data()
    kun = data.get('sayohat_kuni')
    soni = data.get('sayyoh_soni')
    narx = data.get('narx')
    msg = data.get('msg')
    msg_full = msg+f"\nOdam soni : {soni}\nSayohat davomiyligi: {kun}\nHaydovchi uchun narx: {narx}"
    await state.update_data(
        {
            "msg_full": msg_full
        }
    )
    await message.answer(msg_full)
    await message.answer("Ma'lumotlar to'g'rimi ? ",reply_markup=tasdiq_oxir)
    await Sayohat_navoiy.end.set()
@dp.callback_query_handler(text='Confirm',state=Sayohat_navoiy.end)
async def oxirgi(call:CallbackQuery,state:FSMContext):
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
                                   tayyor_sayohatchi=m,
                                   tayyor_sayohatchi_full=msg,
                                   tayyor_sayohatchi_full_mashina=None,
                                   tayyor_sayohatchi_mashina=None)
    drivers = await db.select_all_driver()
    drivers_info = await db.select_all_driver_info()
    for i in drivers:
        if i[5] == 'ok':
            for k in drivers_info:
                if k[2] == tuman and i[4] == k[3]:
                    markup = aiogram.types.InlineKeyboardMarkup()
                    markup.insert(
                        aiogram.types.InlineKeyboardButton(text="Qabul qilish",
                                                           callback_data='sdsds3d465s4d65s'))
                    await bot.send_message(text=m, chat_id=k[3], reply_markup=markup)
    await call.message.answer("Sizning buyurtmangiz tumaningiz haydovchilariga yuborildi.\n"
                              "Ularning bog'lanishini kuting !\n", reply_markup=umumiy_menu
                              )
    await state.reset_state(with_data=False)


@dp.callback_query_handler(text="sdsds3d465s4d65s")
async def qabul_qilish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("msg_full")
    await bot.send_message(text=msg, chat_id=call.from_user.id)



@dp.callback_query_handler(text='UnConfirm', state=Sayohat_navoiy.end)
async def y_n(call:CallbackQuery, state:FSMContext):
    await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu)
    await state.finish()
