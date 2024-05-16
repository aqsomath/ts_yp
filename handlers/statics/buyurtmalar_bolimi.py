from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from loader import dp, bot, db
from aiogram.dispatcher.filters.state import StatesGroup, State


def get_paginated_keyboard(items, current_page, items_per_page):
    total_items = len(items)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    # Create inline keyboard
    keyboard = InlineKeyboardMarkup()
    qidirish = InlineKeyboardButton(text="Qidirish 🔍", callback_data="searchorderbyid")
    ortga = InlineKeyboardButton(text="Ortga", callback_data="back")


    # Add items for the current page
    start = current_page * items_per_page
    end = min(start + items_per_page, total_items)
    current_items = items[start:end]

    # Add items to the keyboard
    for item in current_items:
        # For this example, buttons just show item text
        button = InlineKeyboardButton(text=item[0], callback_data=item[1])
        keyboard.add(button)


    # Add navigation buttons
    navigation_buttons = []
    if current_page > 0:
        prev_button = InlineKeyboardButton("🔙Oldingis", callback_data=f"page_{current_page - 1}")
        navigation_buttons.append(prev_button)

    if current_page < total_pages - 1:
        next_button = InlineKeyboardButton("Keyingisi 🔜", callback_data=f"page_{current_page + 1}")
        navigation_buttons.append(next_button)

    if navigation_buttons:
        keyboard.row(*navigation_buttons)
    keyboard.add(ortga,qidirish)
    return keyboard


class SearchOrderState(StatesGroup):
    id = State()
@dp.callback_query_handler(text="searchorderbyid")
async def qidirish_order(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer("Buyurtma ID sini kiriting : ")
    await SearchOrderState.id.set()
    await call.message.delete()
@dp.message_handler(state=SearchOrderState.id,commands=['cancel'])
async def come_back(message:Message,state:FSMContext):
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
    current_page = 0
    items_per_page = 3

    keyboard = get_paginated_keyboard(items, current_page, items_per_page)

    await message.answer("Buyurtmalar ro'yxati :", reply_markup=keyboard)
    await message.delete()
    await state.finish()
@dp.message_handler(state=SearchOrderState.id)
async def idiruv_id(message:types.Message,state:FSMContext):
    if message.text.isdigit():
        order = await db.select_orders(id=int(message.text))
        if order is not None:
            if order[2] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              3] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()
                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              3] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      3] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()

                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(InlineKeyboardButton(text="Buyurtmani o'chirish",callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[3] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[8] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()

                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[9] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
                    await state.finish()

            if order[10] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()


                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[11] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[12] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()


                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[13] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[14] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()


                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[15] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[16] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()


                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[17] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[18] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()


                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[19] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()

            if order[20] != None:
                if order[30] != None:
                    if order[23] == False:
                        if order[24] == True:
                            if order[27] == True:
                                await message.answer(order[
                                                              21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                                await state.finish()

                        else:
                            if order[27] == True:
                                await message.answer(order[
                                                              21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
                                await state.finish()

                    else:
                        await message.answer(order[
                                                      21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")
                        await state.finish()
                else:
                    markup = InlineKeyboardMarkup()
                    markup.insert(
                        InlineKeyboardButton(text="Buyurtmani o'chirish", callback_data=f"buyurtmani_ochir_{order[0]}"))
                    await message.answer(
                        order[21] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}",reply_markup=markup)
                    await state.finish()
    await message.delete()


@dp.callback_query_handler(lambda c: c.data.startswith("buyurtmani_ochir_"))
async def buyurtmalarni_ochirish(call:CallbackQuery):
    id  = int(call.data.split("_")[2])
    await db.aniq_bormaydi_update(aniq_bormaydi=True,id=id)
    await db.update_orders_qabul_qilish(kim_tomonidan_qabul_qilindi=f"<a href='tg://user?id={call.from_user.id}'>Admin</a> tomonidan o'chirilgan",id=id)
    await call.message.answer("Buyurtma o'chirildi")
    await call.message.delete()


@dp.callback_query_handler(text="back")
async def admin_bolimga_qaytish(call:types.CallbackQuery):
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
@dp.callback_query_handler(text="baribuyurtmalar")
async def start_handler(call: types.CallbackQuery):
    items = []
    orders = await db.select_all_orders()
    for order in orders:
        if order[2] != None:
            items.append([f"Taxi reys: ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[8] != None:
            items.append([f"Tayyor pochta : ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[10] != None:
            items.append([f"Tayyor yuk: ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[12] != None:
            items.append([f"Tayyor yuk mashinasi : ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[14] != None:
            items.append([f"Tayyor yo'lovchi : ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[16] != None:
            items.append([f"Tayyor pochta mashinasi : ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[18] != None:
            items.append([f"Tayyor sayohatchi : ID - {order[0]}",f"id_of_order_{order[0]}"])
        if order[20] != None:
            items.append([f"Tayyor sayohat mashinasi : ID - {order[0]}",f"id_of_order_{order[0]}"])
    current_page = 0
    items_per_page = 3

    keyboard = get_paginated_keyboard(items, current_page, items_per_page)

    await call.message.answer("Buyurtmalar ro'yxati :", reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data.startswith("page_"))
async def page_handler(callback_query: types.CallbackQuery):
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

@dp.callback_query_handler(lambda c: c.data.startswith("id_of_order_"))
async def get_order_statics(call:types.CallbackQuery):
    id = int(call.data.split("_")[3])
    order = await db.select_orders(id=id)
    if order[2] != None:
        if order[30] != None:
            if order[23]==False:
                if order[24] == True:
                    if order[27]==True:
                        await call.message.answer(order[3]+f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27]==True:
                        await call.message.answer(order[3]+f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[3] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[3]+f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[8] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              9] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[9] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[10] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              11] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[11] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[12] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              13] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[13] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[14] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              15] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[15] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[16] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              17] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[17] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[18] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              19] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[19] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
    if order[20] != None:
        if order[30] != None:
            if order[23] == False:
                if order[24] == True:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishildi</b>")
                else:
                    if order[27] == True:
                        await call.message.answer(order[
                                                      21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma rad etildi</b>")
            else:
                await call.message.answer(order[
                                              21] + f"\nQabul qildi : \n{order[30]}\nBuyurtma berilgan sana: \n{order[31]}\n<b>Buyurtma kelishilmoqda</b>")

        else:
            await call.message.answer(order[21] + f"\nQabul qildi : Hech kim\nBuyurtma berilgan sana: \n{order[31]}")
