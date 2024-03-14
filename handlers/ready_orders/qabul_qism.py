import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.statics.admin_panel import user_of_banned
from handlers.statics.tariflar import first,fifth,fourth,second,third
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
            if len(count)<tarif[3]+1 :
                data=await state.get_data()
                first_data=data.get("First_data")
                id = data.get("id")
                order = await db.select_order(id=id)
                if first_data == "course:tayyoryolovchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full":order[15]})
                    chat_id = order[1]
                    if order[15] != "Kelishilmoqda...!":
                        if order[15] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[15], reply_markup=markup)
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                            ord = await db.select_order(id=id)
                            print(ord[15])
                    else:
                        ortga=InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu",callback_data="ogirilish"))
                        await call.message.answer(order[15], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[15] == "Kelishilmoqda...!":
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi" , id=id)
                    await call.message.delete()
                if first_data == "course:tayyorpochta":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi", callback_data="Pochtayuborilmaydiganbolibdi'"))
                    await call.message.answer(order[9], reply_markup=markup)
                    await state.update_data({"msg_full":order[9]})
                    chat_id = order[1]
                    if order[9] != "Kelishilmoqda...!":
                        if order[9] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[9], reply_markup=markup)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[9] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi",id=id)
                if first_data == "course:tayyorpochtamashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[17]})
                    chat_id = order[1]
                    if order[17] != "Kelishilmoqda . . . . .!":
                        if order[17] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!",id=id)
                            await call.message.answer(order[17],reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[17],reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[17] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi",id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryuk":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[11]})
                    chat_id = order[1]
                    if order[11] != "Kelishilmoqda...!":
                        if order[11] !="Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[11], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[11],reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[11] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi",id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryukmashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[13]})
                    chat_id = order[1]
                    if order[13] != "Kelishilmoqda . . . . .!":
                        if order[13] !="Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!",id=id)
                            await call.message.answer(order[13],reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[13], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[13] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyortaksi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[3]})
                    chat_id = order[1]
                    if order[3] != "Kelishilmoqda . . . . .!":
                        if order[3] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!",id=id)
                            await call.message.answer(order[3],reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[3], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[3] == "Kelishilmoqda...!":
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi",id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[19]})
                    chat_id = order[1]
                    if order[19] != "Kelishilmoqda...!":
                        if order[19] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[19],reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[19], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[19] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi",id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatgamashina":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[21]})
                    chat_id = order[1]
                    if order[21]!="Kelishilmoqda...!":
                        if order[21]!="Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                                   chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!",id=id)
                            await call.message.answer(order[21], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[21], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[21] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",id=id)
                    await call.message.delete()
                await call.message.delete()
            else:
                await call.message.answer("Sizning tanlagan ta'rif rejangiz bo'yicha bugungi limitingiz tugadi !!!")
        if call.from_user.id in fifth:
            count = []
            for i in last_get_orders:
                if i[1] == call.from_user.id:
                    count.append(i)
            tarif = await db.select_tarif(tarif_name="fifth")
            if len(count) < tarif[3]+1:
                data = await state.get_data()
                first_data = data.get("First_data")
                id = data.get("id")
                order = await db.select_order(id=id)
                if first_data == "course:tayyoryolovchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[15]})
                    chat_id = order[1]
                    if order[15] != "Kelishilmoqda...!":
                        if order[15] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[15], reply_markup=markup)
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                            ord = await db.select_order(id=id)
                            print(ord[15])
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[15], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[15] == "Kelishilmoqda...!":
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorpochta":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                       callback_data="Pochtayuborilmaydiganbolibdi'"))
                    await call.message.answer(order[9], reply_markup=markup)
                    await state.update_data({"msg_full": order[9]})
                    chat_id = order[1]
                    if order[9] != "Kelishilmoqda...!":
                        if order[9] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[9], reply_markup=markup)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[9] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                if first_data == "course:tayyorpochtamashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[17]})
                    chat_id = order[1]
                    if order[17] != "Kelishilmoqda . . . . .!":
                        if order[17] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[17], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[17], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[17] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryuk":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[11]})
                    chat_id = order[1]
                    if order[11] != "Kelishilmoqda...!":
                        if order[11] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[11], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[11], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[11] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryukmashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[13]})
                    chat_id = order[1]
                    if order[13] != "Kelishilmoqda . . . . .!":
                        if order[13] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[13], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[13], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[13] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyortaksi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[3]})
                    chat_id = order[1]
                    if order[3] != "Kelishilmoqda . . . . .!":
                        if order[3] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[3], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[3], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[3] == "Kelishilmoqda...!":
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                       callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[19]})
                    chat_id = order[1]
                    if order[19] != "Kelishilmoqda...!":
                        if order[19] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[19], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[19], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[19] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatgamashina":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[21]})
                    chat_id = order[1]
                    if order[21] != "Kelishilmoqda...!":
                        if order[21] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                 callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_sayohatchi_mashina(
                                tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                            await call.message.answer(order[21], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[21], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[21] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi", id=id)
                    await call.message.delete()
                await call.message.delete()
        if call.from_user.id in first:
            count = []
            for i in last_get_orders:
                if i[1] == call.from_user.id:
                    count.append(i)
            tarif =await db.select_tarif(tarif_name="first")
            if call.from_user.id in fourth:
                tarif_4= await db.select_tarif(tarif_name="fourth")
                if len(count) < tarif[3] + 1+tarif_4[3]:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!",
                                                                      id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!",
                                                                     id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",
                                                                          id=id)
                        await call.message.delete()
                    await call.message.delete()
            else:
                if len(count) < tarif[3]+1:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi", id=id)
                        await call.message.delete()
                    await call.message.delete()
                else:
                    await call.message.answer("Sizning kunlik ta'rif rejangiz nihoyasiga yetdi")
        if call.from_user.id in second:
            count = []
            for i in last_get_orders:
                if i[1] == call.from_user.id:
                    count.append(i)
            tarif = await db.select_tarif(tarif_name="second")
            if call.from_user.id in fourth:
                tarif_4= await db.select_tarif(tarif_name="fourth")
                if len(count) < tarif[3] + 1+tarif_4[3]:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!",
                                                                      id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!",
                                                                     id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",
                                                                          id=id)
                        await call.message.delete()
                    await call.message.delete()
            else:
                if len(count) < tarif[3]+1:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi", id=id)
                        await call.message.delete()
                    await call.message.delete()
                else:
                    await call.message.answer("Sizning kunlik ta'rif rejangiz nihoyasiga yetdi")
            if len(count) < tarif[3] + 1:

                data = await state.get_data()
                first_data = data.get("First_data")
                id = data.get("id")
                order = await db.select_order(id=id)
                if first_data == "course:tayyoryolovchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                             callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[15]})
                    chat_id = order[1]
                    if order[15] != "Kelishilmoqda...!":
                        if order[15] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[15], reply_markup=markup)
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                            ord = await db.select_order(id=id)
                            print(ord[15])
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[15], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[15] == "Kelishilmoqda...!":
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorpochta":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                       callback_data="Pochtayuborilmaydiganbolibdi'"))
                    await call.message.answer(order[9], reply_markup=markup)
                    await state.update_data({"msg_full": order[9]})
                    chat_id = order[1]
                    if order[9] != "Kelishilmoqda...!":
                        if order[9] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yubormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[9], reply_markup=markup)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[9] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                if first_data == "course:tayyorpochtamashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                             callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[17]})
                    chat_id = order[1]
                    if order[17] != "Kelishilmoqda . . . . .!":
                        if order[17] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[17], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[17], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[17] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryuk":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi",
                                             callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[11]})
                    chat_id = order[1]
                    if order[11] != "Kelishilmoqda...!":
                        if order[11] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[11], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[11], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[11] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryukmashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                             callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[13]})
                    chat_id = order[1]
                    if order[13] != "Kelishilmoqda . . . . .!":
                        if order[13] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[13], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[13], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[13] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyortaksi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[3]})
                    chat_id = order[1]
                    if order[3] != "Kelishilmoqda . . . . .!":
                        if order[3] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[3], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[3], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[3] == "Kelishilmoqda...!":
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                       callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[19]})
                    chat_id = order[1]
                    if order[19] != "Kelishilmoqda...!":
                        if order[19] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[19], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[19], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[19] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatgamashina":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                             callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[21]})
                    chat_id = order[1]
                    if order[21] != "Kelishilmoqda...!":
                        if order[21] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                 callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_sayohatchi_mashina(
                                tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                            await call.message.answer(order[21], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[21], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[21] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",
                                                                      id=id)
                    await call.message.delete()
                await call.message.delete()
                data = await state.get_data()
                first_data = data.get("First_data")
                id = data.get("id")
                order = await db.select_order(id=id)
                if first_data == "course:tayyoryolovchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[15]})
                    chat_id = order[1]
                    if order[15] != "Kelishilmoqda...!":
                        if order[15] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[15], reply_markup=markup)
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                            ord = await db.select_order(id=id)
                            print(ord[15])
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[15], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[15] == "Kelishilmoqda...!":
                            await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorpochta":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                       callback_data="Pochtayuborilmaydiganbolibdi'"))
                    await call.message.answer(order[9], reply_markup=markup)
                    await state.update_data({"msg_full": order[9]})
                    chat_id = order[1]
                    if order[9] != "Kelishilmoqda...!":
                        if order[9] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yubormaydigan bo'ldim", callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await call.message.answer(order[9], reply_markup=markup)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await asyncio.sleep(600)
                        if order[9] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                if first_data == "course:tayyorpochtamashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[17]})
                    chat_id = order[1]
                    if order[17] != "Kelishilmoqda . . . . .!":
                        if order[17] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[17], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[17], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[17] == "Kelishilmoqda...!":
                            await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryuk":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[11]})
                    chat_id = order[1]
                    if order[11] != "Kelishilmoqda...!":
                        if order[11] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[11], reply_markup=markup)
                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[11], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[11] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyoryukmashinasi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[13]})
                    chat_id = order[1]
                    if order[13] != "Kelishilmoqda . . . . .!":
                        if order[13] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[13], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[13], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[13] == "Kelishilmoqda...!":
                            await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyortaksi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Taxi bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[3]})
                    chat_id = order[1]
                    if order[3] != "Kelishilmoqda . . . . .!":
                        if order[3] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[3], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[3], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[3] == "Kelishilmoqda...!":
                            await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatchi":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                       callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[19]})
                    chat_id = order[1]
                    if order[19] != "Kelishilmoqda...!":
                        if order[19] != "Rad etildi":
                            driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                            driver_id = driver[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(
                                InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                     callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                            await call.message.answer(order[19], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[19], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[19] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                    await call.message.delete()
                if first_data == "course:tayyorsayohatgamashina":
                    markup = InlineKeyboardMarkup(row_width=2)
                    markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                    markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                    markup.insert(
                        InlineKeyboardButton(text="Mashina bormaydigan bo'libdi", callback_data="Mijozbormaydiganbolibdi"))
                    await state.update_data({"msg_full": order[21]})
                    chat_id = order[1]
                    if order[21] != "Kelishilmoqda...!":
                        if order[21] != "Rad etildi":
                            yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                            yolovchi_id = yolovchi[0]
                            markup_1 = InlineKeyboardMarkup(row_width=2)
                            markup_1.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                            markup_1.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                            markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                 callback_data="Mijozbormaydiganbolibdi"))
                            await bot.send_message(
                                text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                chat_id=chat_id, reply_markup=markup_1)
                            await db.update_tayyor_sayohatchi_mashina(
                                tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                            await call.message.answer(order[21], reply_markup=markup)

                    else:
                        ortga = InlineKeyboardMarkup()
                        ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                        await call.message.answer(order[21], reply_markup=ortga)
                        await asyncio.sleep(600)
                        if order[21] == "Kelishilmoqda...!":
                            await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi", id=id)
                    await call.message.delete()
                await call.message.delete()
        if call.from_user.id in third:
            count = []
            for i in last_get_orders:
                if i[1] == call.from_user.id:
                    count.append(i)
            tarif = await db.select_tarif(tarif_name="third")
            if call.from_user.id in fourth:
                tarif_4 = await db.select_tarif(tarif_name="fourth")
                if len(count) < tarif[3] + 1 + tarif_4[3]:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!",
                                                                      id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!",
                                                                     id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",
                                                                          id=id)
                        await call.message.delete()
                    await call.message.delete()
            else:
                if len(count) < tarif[3] + 1:

                    data = await state.get_data()
                    first_data = data.get("First_data")
                    id = data.get("id")
                    order = await db.select_order(id=id)
                    if first_data == "course:tayyoryolovchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mijoz bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[15]})
                        chat_id = order[1]
                        if order[15] != "Kelishilmoqda...!":
                            if order[15] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[15], reply_markup=markup)
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishilmoqda...!", id=id)
                                ord = await db.select_order(id=id)
                                print(ord[15])
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[15], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[15] == "Kelishilmoqda...!":
                                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorpochta":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Pochta yuborilmaydigan bo'libdi",
                                                           callback_data="Pochtayuborilmaydiganbolibdi'"))
                        await call.message.answer(order[9], reply_markup=markup)
                        await state.update_data({"msg_full": order[9]})
                        chat_id = order[1]
                        if order[9] != "Kelishilmoqda...!":
                            if order[9] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await call.message.answer(order[9], reply_markup=markup)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[9], reply_markup=markup)
                            await asyncio.sleep(600)
                            if order[9] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
                    if first_data == "course:tayyorpochtamashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[17]})
                        chat_id = order[1]
                        if order[17] != "Kelishilmoqda . . . . .!":
                            if order[17] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishilmoqda...!",
                                                                      id=id)
                                await call.message.answer(order[17], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[17], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[17] == "Kelishilmoqda...!":
                                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryuk":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Yuk yuborilmaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[11]})
                        chat_id = order[1]
                        if order[11] != "Kelishilmoqda...!":
                            if order[11] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Yuk  yubormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[11], reply_markup=markup)
                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[11], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[11] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyoryukmashinasi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik  🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[13]})
                        chat_id = order[1]
                        if order[13] != "Kelishilmoqda . . . . .!":
                            if order[13] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishilmoqda...!",
                                                                     id=id)
                                await call.message.answer(order[13], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[13], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[13] == "Kelishilmoqda...!":
                                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyortaksi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Taxi bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[3]})
                        chat_id = order[1]
                        if order[3] != "Kelishilmoqda . . . . .!":
                            if order[3] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[3], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[3], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[3] == "Kelishilmoqda...!":
                                await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatchi":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(InlineKeyboardButton(text="Sayohatchi bormaydigan bo'libdi",
                                                           callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[19]})
                        chat_id = order[1]
                        if order[19] != "Kelishilmoqda...!":
                            if order[19] != "Rad etildi":
                                driver = await db.select_haydovchi(telegram_id=call.from_user.id)
                                driver_id = driver[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                         callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {driver_id} - raqamli haydovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_pochta(tayyor_pochta_full="Kelishilmoqda...!", id=id)
                                await call.message.answer(order[19], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[19], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[19] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
                        await call.message.delete()
                    if first_data == "course:tayyorsayohatgamashina":
                        markup = InlineKeyboardMarkup(row_width=2)
                        markup.insert(InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                        markup.insert(InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                        markup.insert(
                            InlineKeyboardButton(text="Mashina bormaydigan bo'libdi",
                                                 callback_data="Mijozbormaydiganbolibdi"))
                        await state.update_data({"msg_full": order[21]})
                        chat_id = order[1]
                        if order[21] != "Kelishilmoqda...!":
                            if order[21] != "Rad etildi":
                                yolovchi = await db.select_yolovchi(telegram_id=call.from_user.id)
                                yolovchi_id = yolovchi[0]
                                markup_1 = InlineKeyboardMarkup(row_width=2)
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha oldik 🤝 ", callback_data="kelishaoldik"))
                                markup_1.insert(
                                    InlineKeyboardButton(text="Kelisha olmadik", callback_data="kelisholmadik"))
                                markup_1.insert(InlineKeyboardButton(text="Men bormaydigan bo'ldim",
                                                                     callback_data="Mijozbormaydiganbolibdi"))
                                await bot.send_message(
                                    text=f"Sizning buyurtmangizni {yolovchi_id} - raqamli yo'lovchi qabul qildi",
                                    chat_id=chat_id, reply_markup=markup_1)
                                await db.update_tayyor_sayohatchi_mashina(
                                    tayyor_sayohatchi_full_mashina="Kelishilmoqda . . . . .!", id=id)
                                await call.message.answer(order[21], reply_markup=markup)

                        else:
                            ortga = InlineKeyboardMarkup()
                            ortga.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
                            await call.message.answer(order[21], reply_markup=ortga)
                            await asyncio.sleep(600)
                            if order[21] == "Kelishilmoqda...!":
                                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina="Kellishildi",
                                                                          id=id)
                        await call.message.delete()
                    await call.message.delete()
                else:
                    await call.message.answer("Sizning kunlik ta'rif rejangiz nihoyasiga yetdi")
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

@dp.callback_query_handler(lambda c: c.data=="kelisholmadik" or c.data=="yoqboraman")
async def kelisha_olmadik(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    first_data = data.get("First_data")
    id = data.get("id")
    msg_fulll = data.get("msg_fulll")
    if first_data == "course:tayyoryolovchi":
        await db.update_tayyor_yolovchi(tayyor_yolovchi_full=msg_fulll, id=id)
    if first_data == "course:tayyorpochta":
        await db.update_tayyor_pochta(tayyor_pochta_full=msg_fulll, id=id)
    if first_data == "course:tayyorpochtamashinasi":
        await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full=msg_fulll, id=id)
    if first_data == "course:tayyoryuk":
        await db.update_tayyor_yuk(tayyor_yuk_full=msg_fulll,id=id)
    if first_data == "course:tayyoryukmashinasi":
        await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full=msg_fulll, id=id)
    if first_data == "course:tayyortaksi":
        await db.update_tayyor_taxi(tayyor_taxi_full=msg_fulll, id=id)
    if first_data == "course:tayyorsayohatchi":
        await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full=msg_fulll, id=id)
    if first_data == "course:tayyorsayohatgamashina":
        await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina=msg_fulll,id=id)
    markup=InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="ogirilish"))
    await call.message.answer("Buyurtma kelishilmadi .  ",reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(lambda c: c.data=="kelishaoldik")
async def kelisha_oldik(call:CallbackQuery,state:FSMContext):
   data = await state.get_data()
   first_data = data.get("First_data")
   id = data.get("id")
   order = await db.select_order(id=id)
   print(len(order))
   if len(order)==0:
       markup = InlineKeyboardMarkup(row_width=2)
       markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
       await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
       await call.message.delete()
   else:
       markup = InlineKeyboardMarkup(row_width=2)
       markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
       if first_data == "course:tayyoryolovchi":
           await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Kelishildi", id=id)
       if first_data == "course:tayyorpochta":
           await db.update_tayyor_pochta(tayyor_pochta_full="Kelishildi", id=id)
       if first_data == "course:tayyorpochtamashinasi":
           await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Kelishildi", id=id)
       if first_data == "course:tayyoryuk":
           await db.update_tayyor_yuk(tayyor_yuk_full="Kelishildi", id=id)
       if first_data == "course:tayyoryukmashinasi":
           await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Kelishildi", id=id)
       if first_data == "course:tayyortaksi":
           await db.update_tayyor_taxi(tayyor_taxi_full="Kelishildi", id=id)
       if first_data == "course:tayyorsayohatchi":
           await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Kelishildi", id=id)
       if first_data == "course:tayyorsayohatgamashina":
           await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina='Kelishildi', id=id)
       await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
       await call.message.delete()

@dp.callback_query_handler(lambda c:  c.data=="Mijozbormaydiganbolibdi")
async def bormaydigan_bolish(call:CallbackQuery,state:FSMContext):
    list=[]
    data = await state.get_data()
    first_data = data.get("First_data")
    id = data.get("id")
    order = await db.select_order(id=id)
    text=f"Rostdan ham bormaydigan bo'ldingizmi ?"
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Xa", callback_data="bormidiganboldim"))
    markup.insert(InlineKeyboardButton(text="Yo'q", callback_data="yoqboraman"))
    while len(list)<2:
        await bot.send_message(text=text,chat_id=order[1],reply_markup=markup)
        await asyncio.sleep(300)
        list.append(1)
        if len(list)==2:
            if first_data == "course:tayyoryolovchi":
                await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Rad etildi", id=id)
            if first_data == "course:tayyorpochta":
                await db.update_tayyor_pochta(tayyor_pochta_full="Rad etildi", id=id)
            if first_data == "course:tayyorpochtamashinasi":
                await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Rad etildi", id=id)
            if first_data == "course:tayyoryuk":
                await db.update_tayyor_yuk(tayyor_yuk_full="Rad etildi", id=id)
            if first_data == "course:tayyoryukmashinasi":
                await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Rad etildi", id=id)
            if first_data == "course:tayyortaksi":
                await db.update_tayyor_taxi(tayyor_taxi_full="Rad etildi", id=id)
            if first_data == "course:tayyorsayohatchi":
                await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Rad etildi", id=id)
            if first_data == "course:tayyorsayohatgamashina":
                await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina='Rad etildi', id=id)
            break
    await call.message.delete()
@dp.callback_query_handler(lambda c:  c.data=="bormidiganboldim")
async def bormaydigan_bolish_1(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    first_data = data.get("First_data")
    id = data.get("id")
    if first_data == "course:tayyoryolovchi":
        await db.update_tayyor_yolovchi(tayyor_yolovchi_full="Rad etildi", id=id)
    if first_data == "course:tayyorpochta":
        await db.update_tayyor_pochta(tayyor_pochta_full="Rad etildi", id=id)
    if first_data == "course:tayyorpochtamashinasi":
        await db.update_tayyor_pochta_mashina(tayyor_pochta_mashina_full="Rad etildi", id=id)
    if first_data == "course:tayyoryuk":
        await db.update_tayyor_yuk(tayyor_yuk_full="Rad etildi", id=id)
    if first_data == "course:tayyoryukmashinasi":
        await db.update_tayyor_yuk_mashinasi(tayyor_yuk_haydovchisi_full="Rad etildi", id=id)
    if first_data == "course:tayyortaksi":
        await db.update_tayyor_taxi(tayyor_taxi_full="Rad etildi", id=id)
    if first_data == "course:tayyorsayohatchi":
        await db.update_tayyor_sayohatchi(tayyor_sayohatchi_full="Rad etildi", id=id)
    if first_data == "course:tayyorsayohatgamashina":
        await db.update_tayyor_sayohatchi_mashina(tayyor_sayohatchi_full_mashina='Rad etildi', id=id)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
    await call.message.answer("Sizga hizmat etganimizdan xursandmiz. ", reply_markup=markup)
    await call.message.delete()


