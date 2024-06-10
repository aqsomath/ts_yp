from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.statics.buyurtmalar_bolimi import get_paginated_keyboard
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu, kirish
from loader import dp, db, bot


def get_paginated_keyboard_2(items, current_page, items_per_page):
    total_items = len(items)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    # Create inline keyboard
    keyboard = InlineKeyboardMarkup()
    ortga = InlineKeyboardButton(text="Ortga", callback_data="sdlkjsdjs")


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
        prev_button = InlineKeyboardButton("🔙Oldingisi", callback_data=f"varaq_{current_page - 1}")
        navigation_buttons.append(prev_button)

    if current_page < total_pages - 1:
        next_button = InlineKeyboardButton("Keyingisi 🔜", callback_data=f"varaq_{current_page + 1}")
        navigation_buttons.append(next_button)

    if navigation_buttons:
        keyboard.row(*navigation_buttons)
    keyboard.add(ortga)
    return keyboard



@dp.callback_query_handler(lambda c: c.data.startswith("varaq_"))
async def page_handler(callback_query: CallbackQuery):
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

    keyboard = get_paginated_keyboard_2(items, current_page, items_per_page)

    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=keyboard)

@dp.callback_query_handler(text="sdlkjsdjs")
async def ortga_boramiz(call:CallbackQuery):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user is not None:
        if user[5] == True:
            await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?",
                                      reply_markup=umumiy_menu)
            await call.message.delete()
        elif user[6] == True:
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
        else:
            await call.message.answer(f"Salom, {call.from_user.full_name}!", reply_markup=kirish)
@dp.callback_query_handler(menu_callback.filter(item_name="meningbuyurtmalarim"))
async def my_orders_head(call:CallbackQuery):
    items = []
    orders = await db.select_all_orders()
    for order in orders:
        if order[1]==call.from_user.id:
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

    keyboard = get_paginated_keyboard_2(items, current_page, items_per_page)

    await call.message.answer("Sizning buyurtmalaringiz ro'yxati :", reply_markup=keyboard)
    await call.message.delete()
