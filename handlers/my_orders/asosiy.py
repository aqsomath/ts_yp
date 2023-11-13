import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp,db


@dp.callback_query_handler(menu_callback.filter(item_name='meningbuyurtmalarim'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    markup=aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton(text="Yo'lovchi olish", callback_data="jsegukwsgfsgjkfsdgs"))
    markup.add(aiogram.types.InlineKeyboardButton(text="Yuk olish ", callback_data="yukavtochaqirish"))
    markup.add(aiogram.types.InlineKeyboardButton(text="Sayohatchi olish ", callback_data="sayohattaxichaqirish"))
    markup.add(aiogram.types.InlineKeyboardButton(text="Pochta olish", callback_data="pochtayuborishbuyurtmalari"))
    await call.message.answer("Sizning buyurtmalaringiz ro'yxati :  ",reply_markup=markup)


@dp.callback_query_handler(text="jsegukwsgfsgjkfsdgs")
async def taxi_buyurtmalarim(call:CallbackQuery,state:FSMContext):
    markup_taxi = aiogram.types.InlineKeyboardMarkup()
    markup_taxi.add(aiogram.types.InlineKeyboardButton(text="Keyingisi", callback_data="ketaxi_0"))
    orders = await db.select_taxi_orders()
    orders_taxi_list = []
    print("Nega ishlamayapti")
    if len(orders)==0:
        await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q")
    else:
        for i in orders:
            if i[1]==call.message.from_user.id:
                if i[0] is not None:
                    orders_taxi_list.append(i[0])
        await call.message.answer(f"Siz da yo'ovchi olish uchun jami {len(orders_taxi_list)} ta buyurtma qilgansiz.\n\n1-buyurtrma")
        await call.message.answer(orders_taxi_list[0],reply_markup=markup_taxi)
        await state.update_data({"taxi_list":orders_taxi_list})
        if len(orders_taxi_list)==0:
            await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q !")


@dp.callback_query_handler(text_contains="ketaxi_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("taxi_list")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"ketaxi_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton(text="Ortga", callback_data="orqaga_0"))
        await call.message.answer(f"{curr_page+1}-buyurtma")
        await call.message.answer(text=buyurtma[curr_page],reply_markup=markup)
        await state.update_data({"curr":curr_page})





@dp.callback_query_handler(text="yukavtochaqirish")
async def taxi_buyurtmalarim(call:CallbackQuery,state:FSMContext):
    markup_taxi = aiogram.types.InlineKeyboardMarkup()
    markup_taxi.add(aiogram.types.InlineKeyboardButton(text="Keyingisi", callback_data="sjdgjsgd_0"))
    orders = await db.select_yuk_avto_orders()
    orders_yuk_avto_list = []
    print("Nega ishlamayapti")
    if len(orders)==0:
        await call.message.answer("Yuk olish uchun buyurtmalaringiz yo'q")
    else:
        for i in orders:
            if i[1]==call.message.from_user.id:
                if i[0] is not None:
                    orders_yuk_avto_list.append(i[0])
        await call.message.answer(f"Sizda yuk olish uchun jami {len(orders_yuk_avto_list)} ta buyurtma qilgansiz.\n\n1-buyurtrma")
        await call.message.answer(orders_yuk_avto_list[0],reply_markup=markup_taxi)
        await state.update_data({"taxi_yuk_list":orders_yuk_avto_list})
        if len(orders_yuk_avto_list)==0:
            await call.message.answer("Siz yuk olish buyurtma qilmagansiz !")


@dp.callback_query_handler(text_contains="sjdgjsgd_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("taxi_yuk_list")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sjdgjsgd_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton(text="Ortga", callback_data="orqaga_0"))
        await call.message.answer(f"{curr_page+1}-buyurtma")
        await call.message.answer(text=buyurtma[curr_page],reply_markup=markup)
        await state.update_data({"curr":curr_page})



@dp.callback_query_handler(text="sayohattaxichaqirish")
async def taxi_buyurtmalarim(call:CallbackQuery,state:FSMContext):
    markup_taxi = aiogram.types.InlineKeyboardMarkup()
    markup_taxi.add(aiogram.types.InlineKeyboardButton(text="Keyingisi", callback_data="sxaxas_0"))
    orders = await db.select_sayohatchi_mashina()
    orders_sayohat_taxi_list = []
    print("Nega ishlamayapti")
    if len(orders)==0:
        await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q")
    else:
        for i in orders:
            if i[1]==call.message.from_user.id:
                if i[0] is not None:
                    orders_sayohat_taxi_list.append(i[0])
        await call.message.answer(f"Siz da yo'ovchi olish uchun jami {len(orders_sayohat_taxi_list)} ta buyurtma qilgansiz.\n")
        await call.message.answer(orders_sayohat_taxi_list[0],reply_markup=markup_taxi)
        await state.update_data({"taxi_sayohat_list":orders_sayohat_taxi_list})
        if len(orders_sayohat_taxi_list)==0:
            await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q !")


@dp.callback_query_handler(text_contains="sxaxas_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("taxi_sayohat_list")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"sxaxas_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton(text="Ortga", callback_data="orqaga_0"))
        await call.message.answer(f"{curr_page+1}-buyurtma")
        await call.message.answer(text=buyurtma[curr_page],reply_markup=markup)
        await state.update_data({"curr":curr_page})


@dp.callback_query_handler(text="pochtayuborishbuyurtmalari")
async def taxi_buyurtmalarim(call:CallbackQuery,state:FSMContext):
    markup_taxi = aiogram.types.InlineKeyboardMarkup()
    markup_taxi.add(aiogram.types.InlineKeyboardButton(text="Keyingisi", callback_data="d4s5d4_0"))
    orders = await db.select_pochta_haydovchi()
    orders_pochta_taxi_list = []
    print("Nega ishlamayapti")
    if len(orders)==0:
        await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q")
    else:
        for i in orders:
            if i[1]==call.message.from_user.id:
                if i[0] is not None:
                    orders_pochta_taxi_list.append(i[0])
        await call.message.answer(f"Siz da yo'ovchi olish uchun jami {len(orders_pochta_taxi_list)} ta buyurtma qilgansiz.\n")
        await call.message.answer(orders_pochta_taxi_list[0],reply_markup=markup_taxi)
        await state.update_data({"taxi_pochta_list":orders_pochta_taxi_list})
        if len(orders_pochta_taxi_list)==0:
            await call.message.answer("Yo'lovchi olish uchun buyurtmalaringiz yo'q !")


@dp.callback_query_handler(text_contains="d4s5d4_")
async def callback_query(call:CallbackQuery,state:FSMContext):
        data = await state.get_data()
        buyurtma=data.get("taxi_pochta_list")
        markup = aiogram.types.InlineKeyboardMarkup()
        curr_page = int(call.data.split("_")[1])
        curr_page = 0 if (curr_page+1) >= len(buyurtma) else curr_page + 1
        markup.add(aiogram.types.InlineKeyboardButton("Keyingisi", callback_data=f"d4s5d4_{curr_page}"))
        markup.add(aiogram.types.InlineKeyboardButton(text="Ortga", callback_data="orqaga_0"))
        await call.message.answer(f"{curr_page+1}-buyurtma")
        await call.message.answer(text=buyurtma[curr_page],reply_markup=markup)
        await state.update_data({"curr":curr_page})
