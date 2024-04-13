import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.statics.admin_panel import user_of_banned
from handlers.users.tariflar import first,fifth,fourth,second,third
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp, db, bot


@dp.callback_query_handler(lambda c: c.data.startswith("qabul"))
async def first_qabul(call:CallbackQuery,state:FSMContext):
    await db.add_last(telegram_id=call.from_user.id)
    last_get_orders =await db.get_order_joined_in_last_day()
    if call.from_user.id not in user_of_banned:
        if call.from_user.id in fourth:
            count = []
            for i in last_get_orders:
                if i[1]==call.from_user.id:
                    count.append(i)
            tarif = await db.select_tarif(tarif_name="fourth")
            tarif1 = await db.select_tarif(tarif_name="first")
            tarif2= await db.select_tarif(tarif_name="second")
            tarif3 = await db.select_tarif(tarif_name="third")
            limit = tarif[3]
            if call.from_user.id in first:
                limit+=tarif1[3]
            if call.from_user.id in second:
                limit+=tarif2[3]
            if call.from_user.id in third:
                limit+=tarif3[3]
            if len(count)<limit+1:
                if call.data.startswith("qabul_flkk_"):
                    ord_id = int(call.data.split("_")[2])
                    await state.update_data({"ord_id":ord_id})
                    msg = await db.select_orders(id=ord_id)
                    list = [3, 9, 11, 13, 15, 17, 19, 21]
                    for i in list:
                        if msg[i] is not None:
                            if msg[23] == False:
                                if msg[25] == False:
                                    if msg[24] == False:
                                        try:
                                            markup_1 = InlineKeyboardMarkup(row_width=2)
                                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                                 callback_data=f"kelishaoldik_{ord_id}"))
                                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik",
                                                                                 callback_data=f"kelisholmadik_{ord_id}"))
                                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                                 callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                            markup_1.insert(
                                                InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))

                                            markup_12 = InlineKeyboardMarkup(row_width=2)
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                     callback_data=f"kelishaoldik_{ord_id}"))
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Kelisha olmadik",
                                                                     callback_data=f"kelisholmadik_{ord_id}"))
                                            markup_12.insert(InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                                                  callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
                                            driver = await db.select_user(telegram_id=call.from_user.id)
                                            driver_id = driver[0]
                                            await bot.send_message(
                                                text=f"Sizning buyurtmangizni {driver_id} - raqamli foydalanuvchi qabul qildi",
                                                chat_id=msg[1], reply_markup=markup_1)
                                            await call.message.answer(msg[i], reply_markup=markup_12)
                                            await db.kelishilmoqda_orders(kelishilmoqda=True, id=ord_id)
                                        except TypeError:
                                            await call.message.answer(
                                                "Kechirasiz , bu buyurtmani qabul qilishigniz uchun siz haydovchi bo'lishingiz kerak !")
                                    else:
                                        await call.message.answer(
                                            "Afsus kech qoldingiz . Bu buyurtma qabul boshqa talabgor tomonidan qabul qilinib bo'ldi")
                                else:
                                    await call.message.answer("Bu buyurtma buyurtmachi tomonidan bekor qilindi ")
                            else:
                                await call.message.answer("Bu buyurtma ayni paytda kelishilmoqda !")

        else:

            if call.from_user.id in fifth:
                count = []
                for i in last_get_orders:
                    if i[1] == call.from_user.id:
                        count.append(i)
                tarif = await db.select_tarif(tarif_name="fifth")
                if len(count) < tarif[3]+1:
                    if call.data.startswith("qabul_flkk_"):
                        ord_id = int(call.data.split("_")[2])
                        await state.update_data({"ord_id": ord_id})
                        msg = await db.select_orders(id=ord_id)
                        list = [3, 9, 11, 13, 15, 17, 19, 21]
                        for i in list:
                         if msg[i] is not None:
                            if msg[23] == False:
                                if msg[25]==False:
                                    if msg[24]==False:
                                        try:
                                            markup_1 = InlineKeyboardMarkup(row_width=2)
                                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                                 callback_data=f"kelishaoldik_{ord_id}"))
                                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik",
                                                                                 callback_data=f"kelisholmadik_{ord_id}"))
                                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                                 callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                            markup_1.insert(
                                                InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))

                                            markup_12 = InlineKeyboardMarkup(row_width=2)
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                     callback_data=f"kelishaoldik_{ord_id}"))
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Kelisha olmadik",
                                                                     callback_data=f"kelisholmadik_{ord_id}"))
                                            markup_12.insert(InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                                                  callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                            markup_12.insert(
                                                InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
                                            driver = await db.select_user(telegram_id=call.from_user.id)
                                            driver_id = driver[0]
                                            await bot.send_message(
                                                text=f"Sizning buyurtmangizni {driver_id} - raqamli foydalanuvchi qabul qildi",
                                                chat_id=msg[1], reply_markup=markup_1)
                                            await call.message.answer(msg[i], reply_markup=markup_12)
                                            await db.kelishilmoqda_orders(kelishilmoqda=True, id=ord_id)
                                        except TypeError:
                                            await call.message.answer(
                                                "Kechirasiz , bu buyurtmani qabul qilishigniz uchun siz haydovchi bo'lishingiz kerak !")
                                    else:
                                        await call.message.answer("Afsus kech qoldingiz . Bu buyurtma qabul boshqa talabgor tomonidan qabul qilinib bo'ldi")
                                else:
                                    await call.message.answer("Bu buyurtma buyurtmachi tomonidan bekor qilindi ")
                            else:
                                await call.message.answer("Bu buyurtma ayni paytda kelishilmoqda !")

            if call.from_user.id in first:
                count = []
                for i in last_get_orders:
                    if i[1] == call.from_user.id:
                        count.append(i)
                tarif =await db.select_tarif(tarif_name="first")
                if call.from_user.id in fourth:
                    tarif_4= await db.select_tarif(tarif_name="fourth")
                    if len(count) < tarif[3] + 1+tarif_4[3]:

                        if call.data.startswith("qabul_flkk_"):
                            ord_id = int(call.data.split("_")[2])
                            await state.update_data({"ord_id": ord_id})
                            msg = await db.select_orders(id=ord_id)
                            list = [3, 9, 11, 13, 15, 17, 19, 21]
                            for i in list:
                                if msg[i] is not None:
                                    if msg[23] == False:
                                        if msg[25] == False:
                                            if msg[24] == False:
                                                try:
                                                    markup_1 = InlineKeyboardMarkup(row_width=2)
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                                         callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik",
                                                                                         callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                                         callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_1.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))

                                                    markup_12 = InlineKeyboardMarkup(row_width=2)
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                             callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha olmadik",
                                                                             callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                                             callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))
                                                    driver = await db.select_user(telegram_id=call.from_user.id)
                                                    driver_id = driver[0]
                                                    await bot.send_message(
                                                        text=f"Sizning buyurtmangizni {driver_id} - raqamli foydalanuvchi qabul qildi",
                                                        chat_id=msg[1], reply_markup=markup_1)
                                                    await call.message.answer(msg[i], reply_markup=markup_12)
                                                    await db.kelishilmoqda_orders(kelishilmoqda=True, id=ord_id)
                                                except TypeError:
                                                    await call.message.answer(
                                                        "Kechirasiz , bu buyurtmani qabul qilishigniz uchun siz haydovchi bo'lishingiz kerak !")
                                            else:
                                                await call.message.answer(
                                                    "Afsus kech qoldingiz . Bu buyurtma qabul boshqa talabgor tomonidan qabul qilinib bo'ldi")
                                        else:
                                            await call.message.answer(
                                                "Bu buyurtma buyurtmachi tomonidan bekor qilindi ")
                                    else:
                                        await call.message.answer("Bu buyurtma ayni paytda kelishilmoqda !")

            if call.from_user.id in second:
                count = []
                for i in last_get_orders:
                    if i[1] == call.from_user.id:
                        count.append(i)
                tarif = await db.select_tarif(tarif_name="second")
                if call.from_user.id in fourth:
                    tarif_4= await db.select_tarif(tarif_name="fourth")
                    if len(count) < tarif[3] + 1+tarif_4[3]:

                        if call.data.startswith("qabul_flkk_"):
                            ord_id = int(call.data.split("_")[2])
                            await state.update_data({"ord_id": ord_id})
                            msg = await db.select_orders(id=ord_id)
                            list = [3, 9, 11, 13, 15, 17, 19, 21]
                            for i in list:
                                if msg[i] is not None:
                                    if msg[23] == False:
                                        if msg[25] == False:
                                            if msg[24] == False:
                                                try:
                                                    markup_1 = InlineKeyboardMarkup(row_width=2)
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                                         callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik",
                                                                                         callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                                         callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_1.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))

                                                    markup_12 = InlineKeyboardMarkup(row_width=2)
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                             callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha olmadik",
                                                                             callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                                             callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))
                                                    driver = await db.select_user(telegram_id=call.from_user.id)
                                                    driver_id = driver[0]
                                                    await bot.send_message(
                                                        text=f"Sizning buyurtmangizni {driver_id} - raqamli foydalanuvchi qabul qildi",
                                                        chat_id=msg[1], reply_markup=markup_1)
                                                    await call.message.answer(msg[i], reply_markup=markup_12)
                                                    await db.kelishilmoqda_orders(kelishilmoqda=True, id=ord_id)
                                                except TypeError:
                                                    await call.message.answer(
                                                        "Kechirasiz , bu buyurtmani qabul qilishigniz uchun siz haydovchi bo'lishingiz kerak !")
                                            else:
                                                await call.message.answer(
                                                    "Afsus kech qoldingiz . Bu buyurtma qabul boshqa talabgor tomonidan qabul qilinib bo'ldi")
                                        else:
                                            await call.message.answer(
                                                "Bu buyurtma buyurtmachi tomonidan bekor qilindi ")
                                    else:
                                        await call.message.answer("Bu buyurtma ayni paytda kelishilmoqda !")
            if call.from_user.id in third:
                count = []
                for i in last_get_orders:
                    if i[1] == call.from_user.id:
                        count.append(i)
                tarif = await db.select_tarif(tarif_name="third")
                if call.from_user.id in fourth:
                    tarif_4 = await db.select_tarif(tarif_name="fourth")
                    if len(count) < tarif[3] + 1 + tarif_4[3]:

                        if call.data.startswith("qabul_flkk_"):
                            ord_id = int(call.data.split("_")[2])
                            await state.update_data({"ord_id": ord_id})
                            msg = await db.select_orders(id=ord_id)
                            list = [3, 9, 11, 13, 15, 17, 19, 21]
                            for i in list:
                                if msg[i] is not None:
                                    if msg[23] == False:
                                        if msg[25] == False:
                                            if msg[24] == False:
                                                try:
                                                    markup_1 = InlineKeyboardMarkup(row_width=2)
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                                         callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik",
                                                                                         callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                                         callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_1.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))

                                                    markup_12 = InlineKeyboardMarkup(row_width=2)
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha oldik 🤝 ",
                                                                             callback_data=f"kelishaoldik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Kelisha olmadik",
                                                                             callback_data=f"kelisholmadik_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                                             callback_data=f"Mijozbormaydiganbolibdi_{ord_id}"))
                                                    markup_12.insert(
                                                        InlineKeyboardButton(text="Bosh menu",
                                                                             callback_data="qaytvoramiz"))
                                                    driver = await db.select_user(telegram_id=call.from_user.id)
                                                    driver_id = driver[0]
                                                    await bot.send_message(
                                                        text=f"Sizning buyurtmangizni {driver_id} - raqamli foydalanuvchi qabul qildi",
                                                        chat_id=msg[1], reply_markup=markup_1)
                                                    await call.message.answer(msg[i], reply_markup=markup_12)
                                                    await db.kelishilmoqda_orders(kelishilmoqda=True, id=ord_id)
                                                except TypeError:
                                                    await call.message.answer(
                                                        "Kechirasiz , bu buyurtmani qabul qilishigniz uchun siz haydovchi bo'lishingiz kerak !")
                                            else:
                                                await call.message.answer(
                                                    "Afsus kech qoldingiz . Bu buyurtma qabul boshqa talabgor tomonidan qabul qilinib bo'ldi")
                                        else:
                                            await call.message.answer(
                                                "Bu buyurtma buyurtmachi tomonidan bekor qilindi ")
                                    else:
                                        await call.message.answer("Bu buyurtma ayni paytda kelishilmoqda !")

            if call.from_user.id not in fourth:
                if call.from_user.id not in fifth:
                    if call.from_user.id not in third:
                        if call.from_user.id not in second:
                            if call.from_user.id not in first:
                                markup = InlineKeyboardMarkup(row_width=2)
                                markup.insert(InlineKeyboardButton(text="1 - tarif",callback_data="birinchitarif"))
                                markup.insert(InlineKeyboardButton(text="2 - tarif ",callback_data="ikkinchitarif"))
                                markup.insert(InlineKeyboardButton(text="3 - tarif",callback_data="uchinchitarif"))
                                await call.message.answer("Siz hech qaysi ta'rifda emassiz !\nQuyidagi tariflardan biriga ulaning:\n"
                                                          "<b>1 - tarif </b>\nKunlik 3 ta mijozni qabul qilish, oyiga 30000 so'm\n"
                                                          "<b>2 - tarif </b>\nKunlik 6 ta mijozni qabul qilish, oyiga 50000 so'm\n"
                                                          "<b>3 - tarif </b>\nKunlik 12 ta mijozni qabul qilish, oyiga 100000 so'm\n",reply_markup=markup)
    else:
        await call.message.answer("Kechirasiz !!!\nSiz vaqtinchalik qora ro'yxatdasiz")

@dp.callback_query_handler(text="birinchitarif")
@dp.callback_query_handler(text="ikkinchitarif")
@dp.callback_query_handler(text="uchinchitarif")
async def tariflar_uchun(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                              f"Telefon : +998 94 100 79 74\n"
                              f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")

@dp.callback_query_handler(lambda c: c.data.startswith("kelisholmadik_"))
async def kelisha_olmadik(call:CallbackQuery,state:FSMContext):
    ord_id = int(call.data.split("_")[1])
    order = await db.select_order(id=ord_id)
    await db.kelishilmoqda_orders(kelishilmoqda=False, id=ord_id)
    await db.kelishildi_orders(kelishildi=False, id=ord_id)
    markup_1 = InlineKeyboardMarkup(row_width=2)
    markup_1.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
    await call.message.answer("Afsus 😞, menda siz uchun takliflar bor. Bosh menu ga o'ting",reply_markup=markup_1)
    await call.message.delete()




@dp.callback_query_handler(lambda c: c.data=="qaytvoramiz")
async def qyatvoramiz(call:CallbackQuery,state:FSMContext):
    yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
    haydovchi = await db.select_haydovchi(telegram_id=call.from_user.id)
    if yolovchi is not None:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()

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

@dp.callback_query_handler(lambda c: c.data.startswith("kelishaoldik"))
async def kelisha_oldik(call:CallbackQuery,state:FSMContext):
   ord_id = int(call.data.split("_")[1])
   order = await db.select_order(id=ord_id)
   if ord_id is not None:
       if len(order)==0:
           markup = InlineKeyboardMarkup(row_width=2)
           markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
           await db.kelishildi_orders(kelishildi=True, id=ord_id)
           await db.kelishilmoqda_orders(kelishilmoqda=False, id=ord_id)
           await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
           await call.message.delete()
       else:
           markup = InlineKeyboardMarkup(row_width=2)
           markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
           await db.kelishildi_orders(kelishildi=True,id=ord_id)
           await db.kelishilmoqda_orders(kelishilmoqda=False, id=ord_id)
           await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
           await call.message.delete()

@dp.callback_query_handler(lambda c:  c.data.startswith(f"Mijozbormaydiganbolibdi_"))
async def bormaydigan_bolish(call:CallbackQuery,state:FSMContext):
    ord_id =int(call.data.split("_")[1])
    if ord_id is not None:
        order = await db.select_order(id=ord_id)
        text=f"Rostdan ham bormaydigan bo'ldingizmi ?"
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Xa", callback_data=f"bormidiganboldim_{ord_id}"))
        markup.insert(InlineKeyboardButton(text="Yo'q", callback_data=f"yoqboraman_{ord_id}"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
        await bot.send_message(text=text,chat_id=order[1],reply_markup=markup)
        if order[26]==False:
            await db.bormaydi_update(bormaydi=True,id=ord_id)
            await db.kelishilmoqda_orders(kelishilmoqda=False,id=ord_id)
        else:
            await db.delete_orders(id=ord_id)
    await call.message.delete()
@dp.callback_query_handler(lambda c:  c.data.startswith("bormidiganboldim_"))
async def bormaydigan_bolish_1(call:CallbackQuery,state:FSMContext):
    id = int(call.data.split("_")[1])
    if id is not None:
        await db.delete_orders(id=id)
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
        await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
        await call.message.delete()


@dp.callback_query_handler(lambda c:  c.data.startswith("yoqboraman_"))
async def yoqboraman(call:CallbackQuery):
    id = int(call.data.split("_")[1])
    if id is not None:
        await db.kelishilmoqda_orders(kelishilmoqda=False, id=id)
        await db.kelishildi_orders(kelishildi=False, id=id)
        await db.bormaydi_update(bormaydi=False, id=id)
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="qaytvoramiz"))
        await call.message.answer("Juda yaxshi , haydovchilarimiz siz bilan bo'g'lanishini kuting ", reply_markup=markup)
        await call.message.delete()