from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.statics.admin_qoshish import balans_toldirish, balans_ayrish
from handlers.statics.buyurtmalar_bolimi import get_paginated_keyboard
from loader import dp, db, bot
from aiogram.dispatcher.filters.state import StatesGroup, State

@dp.callback_query_handler(lambda c:c.data=="foydalanuvchilarniqidirish")
async def hamma_foydalanuvchilar(call:CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="ID orqali qidirish",callback_data="idorqalitopish"))
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="back"))
    await call.message.answer("Foydalanuvchilar haqida ma'lumot olish bo'limi",reply_markup=markup)
    await call.message.delete()


@dp.callback_query_handler(lambda c:c.data=="back")
async def admin_qisimga_qaytish(call:CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Statistika", callback_data="/"))
    markup.insert(InlineKeyboardButton(text="Foydalanuvchilar", callback_data="foydalanuvchilarniqidirish"))
    markup.insert(InlineKeyboardButton(text="Adminlar", callback_data="adminlarroyxati"))
    markup.insert(InlineKeyboardButton(text="Buyurtmalar", callback_data="baribuyurtmalar"))
    markup.insert(InlineKeyboardButton(text="Ban qilish", callback_data="banqilish"))
    markup.insert(InlineKeyboardButton(text="Bandan chiqarish", callback_data="bandanchiqarish"))
    markup.insert(InlineKeyboardButton(text="Tariflar", callback_data='barchatariflar'))
    markup.insert(InlineKeyboardButton(text="Balans to'ldirish", callback_data="Balanstoldirish"))
    markup.insert(InlineKeyboardButton(text="Balans ayirish", callback_data="Balansayrish"))
    await call.message.answer(text="Admin bo'lim",reply_markup=markup)
    await call.message.delete()


class SelectUserState(StatesGroup):
    id = State()
    keyingi = State()
    hisob_toldirish = State()
    hisob_ayirish = State()
    send_message = State()
    pagination = State()

@dp.callback_query_handler(lambda c:c.data=="idorqalitopish")
async def id_orqali_foydalanuvchi(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Foydalanuvchi ID sini kiriting : ")
    await SelectUserState.id.set()
    await call.message.delete()
@dp.message_handler(state=SelectUserState , commands=['cancel'])
async def cancel_com(message:Message,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Statistika", callback_data="/"))
    markup.insert(InlineKeyboardButton(text="Foydalanuvchilar", callback_data="foydalanuvchilarniqidirish"))
    markup.insert(InlineKeyboardButton(text="Adminlar", callback_data="adminlarroyxati"))
    markup.insert(InlineKeyboardButton(text="Buyurtmalar", callback_data="baribuyurtmalar"))
    markup.insert(InlineKeyboardButton(text="Ban qilish", callback_data="banqilish"))
    markup.insert(InlineKeyboardButton(text="Bandan chiqarish", callback_data="bandanchiqarish"))
    markup.insert(InlineKeyboardButton(text="Tariflar", callback_data='barchatariflar'))
    markup.insert(InlineKeyboardButton(text="Balans to'ldirish", callback_data="Balanstoldirish"))
    markup.insert(InlineKeyboardButton(text="Balans ayirish", callback_data="Balansayrish"))
    await message.answer(text="Admin bo'lim", reply_markup=markup)
    await message.delete()
    await state.finish()
@dp.message_handler(state=SelectUserState.id)
async def id_kiritish(message:Message,state:FSMContext):
    if message.text.isdigit():
        id = int(message.text)
        await state.update_data({"id":id})
        user = await db.select_user(telegram_id=id)
        if user is not None:
            username  = user[2]
            full_name  = user[1]
            telegram_id = user[3]
            balans = user[7]
            kim = ""
            if user[5]==True:
                kim = "Yo'lovchi"
            if user[6]==True:
                kim="Haydovchi"
            text = (f"Foydalanuvchi : {full_name}\n"
                    f"{kim}\n"
                    f"Foydalanuvchi ID : {user[0]}\n"
                    f"Telegram ID: {telegram_id}\n"
                    f"Username : {username}\n"
                    f"Balans : {balans}"
                    )
            markup = InlineKeyboardMarkup()
            button1=InlineKeyboardButton(text="Balans to'ldirish",callback_data="hisobnitoldirish")
            button2=InlineKeyboardButton(text="Balans ayirish",callback_data="hisobnikamaytirish")
            button3=InlineKeyboardButton(text="Xabar yuborish",callback_data="Sendmessage")
            button4=InlineKeyboardButton(text="Foydalanuvchi buyurtmalari",callback_data="foydalanuvchiningbuyurtmalari")
            button5=InlineKeyboardButton(text="Ortga",callback_data="back")
            markup.add(button1,button2)
            markup.add(button4)
            markup.add(button3,button5)
            await message.answer(text,reply_markup=markup)
            await SelectUserState.keyingi.set()
        else:
            await message.answer("Bunday foydalanuvchi mavjud emas !")
            await state.finish()

    else:
        await message.answer("Iltimos son kiriting !")
        await SelectUserState.id.set()

@dp.callback_query_handler(lambda c:c.data=="hisobnitoldirish",state=SelectUserState.keyingi)
async def hisobni_toldirish(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in balans_toldirish:
        await call.message.answer("Qanchaga to'ldirasiz ? ( Son bilan kiriting ) :")
        await SelectUserState.hisob_toldirish.set()
    else:
        await call.message.answer("Kechirasiz sizga hisobni to'ldirish uchun ruxsat yo'q")
        await state.finish()


@dp.message_handler(state=SelectUserState.hisob_toldirish)
async def hisobga_qosh(message:Message,state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        id = data.get("id")
        d = await db.select_user(telegram_id=id)
        await db.update_balans(telegram_id=d[3], balans=d[7] + int(message.text))
        user = await db.select_user(telegram_id=id)
        if user is not None:
            username = user[2]
            full_name = user[1]
            telegram_id = user[3]
            balans = user[7]
            kim = ""
            if user[5] == True:
                kim = "Yo'lovchi"
            if user[6] == True:
                kim = "Haydovchi"
            text = (f"Foydalanuvchi : {full_name}\n"
                    f"{kim}\n"
                    f"Foydalanuvchi ID : {user[0]}\n"
                    f"Telegram ID: {telegram_id}\n"
                    f"Username : {username}\n"
                    f"Balans : {balans}"
                    )
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text="Balans to'ldirish", callback_data="hisobnitoldirish")
            button2 = InlineKeyboardButton(text="Balans ayirish", callback_data="hisobnikamaytirish")
            button3 = InlineKeyboardButton(text="Xabar yuborish", callback_data="Sendmessage")
            button4 = InlineKeyboardButton(text="Foydalanuvchi buyurtmalari", callback_data="foydalanuvchiningbuyurtmalari")
            button5 = InlineKeyboardButton(text="Ortga", callback_data="back")
            markup.add(button1, button2)
            markup.add(button4)
            markup.add(button3, button5)
            await message.answer(text, reply_markup=markup)
            await SelectUserState.keyingi.set()


@dp.callback_query_handler(lambda c:c.data=="hisobnikamaytirish",state=SelectUserState.keyingi)
async def hisobni_toldirish(call:CallbackQuery,state:FSMContext):
    if call.from_user.id in balans_ayrish:
        await call.message.answer("Qanchaga kamaytirmoqchisiz ? ( Son bilan kiriting ) :")
        await SelectUserState.hisob_ayirish.set()
    else:
        await call.message.answer("Kechirasiz sizga hisobni kamaytirish uchun ruxsat yo'q")
        await state.finish()

@dp.message_handler(state=SelectUserState.hisob_ayirish)
async def hisobga_qosh(message:Message,state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        id = data.get("id")
        d = await db.select_user(telegram_id=id)
        await db.update_balans(telegram_id=d[3], balans=d[7] - int(message.text))
        user = await db.select_user(telegram_id=id)
        if user is not None:
            username = user[2]
            full_name = user[1]
            telegram_id = user[3]
            balans = user[7]
            kim = ""
            if user[5] == True:
                kim = "Yo'lovchi"
            if user[6] == True:
                kim = "Haydovchi"
            text = (f"Foydalanuvchi : {full_name}\n"
                    f"{kim}\n"
                    f"Foydalanuvchi ID : {user[0]}\n"
                    f"Telegram ID: {telegram_id}\n"
                    f"Username : {username}\n"
                    f"Balans : {balans}"
                    )
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text="Balans to'ldirish", callback_data="hisobnitoldirish")
            button2 = InlineKeyboardButton(text="Balans ayirish", callback_data="hisobnikamaytirish")
            button3 = InlineKeyboardButton(text="Xabar yuborish", callback_data="Sendmessage")
            button4 = InlineKeyboardButton(text="Foydalanuvchi buyurtmalari", callback_data="foydalanuvchiningbuyurtmalari")
            button5 = InlineKeyboardButton(text="Ortga", callback_data="back")
            markup.add(button1, button2)
            markup.add(button4)
            markup.add(button3, button5)
            await message.answer(text, reply_markup=markup)
            await SelectUserState.keyingi.set()

@dp.callback_query_handler(lambda c:c.data=="Sendmessage",state=SelectUserState.keyingi)
async def foydalanuvchiga_xabar(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Foydalanuvchiga yubormoqchi bo'lgan xabarni kiriting : ")
    await SelectUserState.send_message.set()


@dp.message_handler(state=SelectUserState.send_message)
async def xabarni_yuborish(message:Message,state:FSMContext):
    text = message.text
    data = await state.get_data()
    id = data.get("id")
    await bot.send_message(chat_id=id,text=text)
    await message.answer("Xabar yuborildi ✅")
    await state.finish()

@dp.callback_query_handler(lambda c:c.data=="foydalanuvchiningbuyurtmalari",state=SelectUserState.keyingi)
async def fouydalanuvchi_buyurtmalari(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    id = data.get("id")
    orders = await db.select_all_orders()
    items = []
    for order in orders:
        if order[1]==id:
            if order[2] != None:
                items.append([f"Taxi reys: ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[8] != None:
                items.append([f"Tayyor pochta : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[10] != None:
                items.append([f"Tayyor yuk: ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[12] != None:
                items.append([f"Tayyor yuk mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[14] != None:
                items.append([f"Tayyor yo'lovchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[16] != None:
                items.append([f"Tayyor pochta mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[18] != None:
                items.append([f"Tayyor sayohatchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[20] != None:
                items.append([f"Tayyor sayohat mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
    if len(items)!=0:
        current_page = 0
        items_per_page = 3
        keyboard = get_paginated_keyboard(items, current_page, items_per_page)
        await call.message.answer("Buyurtmalar ro'yxati :", reply_markup=keyboard)
        await SelectUserState.pagination.set()
    else:
        await call.message.answer("Buyurtmalar mavjud emas 🤷🏼‍♂️")
        await SelectUserState.keyingi.set()
@dp.callback_query_handler(lambda c: c.data.startswith("page_"),state=SelectUserState.pagination)
async def page_handler(callback_query: types.CallbackQuery,state:FSMContext):
    # Extract page number from callback data
    current_page = int(callback_query.data.split("_")[1])
    items = []
    orders = await db.select_all_orders()
    for order in orders:
        if order[2] != None:
            items.append([f"Taxi reys: ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[8] != None:
            items.append([f"Tayyor pochta : ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[10] != None:
            items.append([f"Tayyor yuk: ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[12] != None:
            items.append([f"Tayyor yuk mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[14] != None:
            items.append([f"Tayyor yo'lovchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[16] != None:
            items.append([f"Tayyor pochta mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[18] != None:
            items.append([f"Tayyor sayohatchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
        if order[20] != None:
            items.append([f"Tayyor sayohat mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
    items_per_page = 3

    keyboard = get_paginated_keyboard(items, current_page, items_per_page)

    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    reply_markup=keyboard)
    await SelectUserState.pagination.set()


@dp.callback_query_handler(lambda c: c.data=="back",state=SelectUserState.pagination)
async def hisobga_qosh(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        id = data.get("id")
        user = await db.select_user(telegram_id=id)
        if user is not None:
            username = user[2]
            full_name = user[1]
            telegram_id = user[3]
            balans = user[7]
            kim = ""
            if user[5] == True:
                kim = "Yo'lovchi"
            if user[6] == True:
                kim = "Haydovchi"
            text = (f"Foydalanuvchi : {full_name}\n"
                    f"{kim}\n"
                    f"Foydalanuvchi ID : {user[0]}\n"
                    f"Telegram ID: {telegram_id}\n"
                    f"Username : {username}\n"
                    f"Balans : {balans}"
                    )
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text="Balans to'ldirish", callback_data="hisobnitoldirish")
            button2 = InlineKeyboardButton(text="Balans ayirish", callback_data="hisobnikamaytirish")
            button3 = InlineKeyboardButton(text="Xabar yuborish", callback_data="Sendmessage")
            button4 = InlineKeyboardButton(text="Foydalanuvchi buyurtmalari", callback_data="foydalanuvchiningbuyurtmalari")
            button5 = InlineKeyboardButton(text="Ortga", callback_data="back")
            markup.add(button1, button2)
            markup.add(button4)
            markup.add(button3, button5)
            await call.message.answer(text, reply_markup=markup)
            await SelectUserState.keyingi.set()
            await call.message.delete()


@dp.callback_query_handler(lambda c: c.data=="back",state=SelectUserState.keyingi)
async def hisobga_qosh(call:CallbackQuery,state:FSMContext):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Statistika", callback_data="/"))
    markup.insert(InlineKeyboardButton(text="Foydalanuvchilar", callback_data="foydalanuvchilarniqidirish"))
    markup.insert(InlineKeyboardButton(text="Adminlar", callback_data="adminlarroyxati"))
    markup.insert(InlineKeyboardButton(text="Buyurtmalar", callback_data="baribuyurtmalar"))
    markup.insert(InlineKeyboardButton(text="Ban qilish", callback_data="banqilish"))
    markup.insert(InlineKeyboardButton(text="Bandan chiqarish", callback_data="bandanchiqarish"))
    markup.insert(InlineKeyboardButton(text="Tariflar", callback_data='barchatariflar'))
    markup.insert(InlineKeyboardButton(text="Balans to'ldirish", callback_data="Balanstoldirish"))
    markup.insert(InlineKeyboardButton(text="Balans ayirish", callback_data="Balansayrish"))
    await call.message.answer("Admin bo'lim", reply_markup=markup)
    await call.message.delete()
    await state.finish()

@dp.callback_query_handler(lambda c: c.data.startswith("id_of_order_"),state=SelectUserState.pagination)
async def get_order_statics(call:types.CallbackQuery,state:FSMContext):
    id = int(call.data.split("_")[3])
    order = await db.select_orders(id=id)
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="orqaga"))
    if order[2] != None:
        if order[30] != None:
            if order[23]==False:
                if order[24] == True:
                    if order[27]==True:
                        await call.message.answer(order[3]+f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27]==True:
                        await call.message.answer(order[3]+f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[3] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[3]+f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)

    if order[8] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[9] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[10] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[11] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[12] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[13] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[14] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[15] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[16] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[17] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[18] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[19] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
    if order[20] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>",reply_markup=markup)
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>",reply_markup=markup)
            else:
                await call.message.answer(order[
                                              21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>",reply_markup=markup)

        else:
            await call.message.answer(order[21] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)


@dp.callback_query_handler(lambda c:c.data=="orqaga",state=SelectUserState.pagination)
async def fouydalanuvchi_buyurtmalari(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    id = data.get("id")
    orders = await db.select_all_orders()
    items = []
    for order in orders:
        if order[1]==id:
            if order[2] != None:
                items.append([f"Taxi reys: ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[8] != None:
                items.append([f"Tayyor pochta : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[10] != None:
                items.append([f"Tayyor yuk: ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[12] != None:
                items.append([f"Tayyor yuk mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[14] != None:
                items.append([f"Tayyor yo'lovchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[16] != None:
                items.append([f"Tayyor pochta mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[18] != None:
                items.append([f"Tayyor sayohatchi : ID - {order[0]}", f"id_of_order_{order[0]}"])
            if order[20] != None:
                items.append([f"Tayyor sayohat mashinasi : ID - {order[0]}", f"id_of_order_{order[0]}"])
    if len(items)!=0:
        current_page = 0
        items_per_page = 3
        keyboard = get_paginated_keyboard(items, current_page, items_per_page)
        await call.message.answer("Buyurtmalar ro'yxati :", reply_markup=keyboard)
        await SelectUserState.pagination.set()
    else:
        await call.message.answer("Buyurtmalar mavjud emas 🤷🏼‍♂️")
        await state.finish()