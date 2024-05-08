from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, bot, db


def get_paginated_keyboard(items, current_page, items_per_page):
    total_items = len(items)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    # Create inline keyboard
    keyboard = InlineKeyboardMarkup()
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
    keyboard.add(ortga)
    return keyboard

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
