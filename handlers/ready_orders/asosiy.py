from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup,InlineKeyboardButton
from handlers.ready_orders.dictionary import all_district, tumanlar_all, andijon_yol_1, viloyatlar_yol_2, andijon_yol_2, \
    namangan_yol_2, fargona_yol_2, buxoro_yol_2, toshkent_yol_2, sirdaryo_yol_2, surxondaryo_yol_2, qashqadaryo_yol_2, \
    xorazm_yol_2, navoiy_yol_2, jizzax_yol_2, samarqand_yol_2, tosh_shsha_2, qoraqalpogiston_yol_2, namangan_yol_1, \
    fargona_yol_1, buxoro_yol_1, toshkent_yol_1, sirdaryo_yol_1, surxondaryo_yol_1, qashqadaryo_yol_1, xorazm_yol_1, \
    navoiy_yol_1, jizzax_yol_1, samarqand_yol_1, qoraqalpogiston_yol_1, tosh_shsha_1
from handlers.users.edit_district.sozlamalar import haydovchilar_royxati
from handlers.users.yolovchi_tuman.yolovchimisiz import yolovchilar_royxati
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1, umumiy_menu
from loader import dp, db


@dp.callback_query_handler(menu_callback.filter() )
async def ready_orders(call:CallbackQuery,state:FSMContext):
    await state.update_data({"First_data":call.data})
    tayyor=[]
    orders=[]
    if call.data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if call.data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if call.data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if call.data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if call.data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if call.data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if call.data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if call.data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[1] is not None:
            if order[2] is not None:
                if order[7] ==False:
                    if order[8] ==False:
                        tayyor.append(order)
    if len(tayyor) == 0:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer("Tayyor yo'lovchilar hozirda mavjud emas 🙅🏻‍♂️ ", reply_markup=markup)
        await call.message.delete()
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(tayyor[0][1], reply_markup=markup)
        await state.update_data({"id":tayyor[0][6]})
        await call.message.delete()

@dp.callback_query_handler(text="ogirilish")
async def boshi_uchun(call:CallbackQuery):
    if call.message.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.message.from_user.id in haydovchilar_royxati:
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
@dp.callback_query_handler(text="osjdndi")
async def boshi_uchun(call:CallbackQuery):
    if call.message.from_user.id in yolovchilar_royxati:
        await call.message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await call.message.delete()


    elif call.message.from_user.id in haydovchilar_royxati:
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
@dp.callback_query_handler(lambda c: c.data.startswith('next_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page=int(call.data.split("_")[1])
    data=await state.get_data()
    first_data=data.get("First_data")
    tayyor=[]
    orders=[]
    if first_data=="course:tayyoryolovchi":
        orders=await db.select_tayyor_yolovchi()
    if first_data=="course:tayyorpochta":
        orders=await db.select_tayyor_pochta()
    if first_data=="course:tayyorpochtamashinasi":
        orders=await db.select_tayyor_pochta_mashina()
    if first_data=="course:tayyoryuk":
        orders=await db.select_tayyor_yuk()
    if first_data=="course:tayyoryukmashinasi":
        orders=await db.select_tayyor_yuk_haydovchi()
    if first_data=="course:tayyortaksi":
        orders=await db.select_tayyor_taxi()
    if first_data=="course:tayyorsayohatchi":
        orders=await db.select_tayyor_sayohatchi()
    if first_data=="course:tayyorsayohatgamashina":
        orders=await db.select_tayyor_sayohatchi_mashina()

    for order in orders:
        if order[1] is not None:
            if order[2] is not None:
                if order[7] == False:
                    if order[8] == False:
                        tayyor.append(order)
    if current_page < len(tayyor) - 1:
        current_page += 1
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(tayyor[current_page][1], reply_markup=markup)
        await state.update_data({"id": tayyor[current_page][6]})
        await call.message.delete()
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{tayyor[current_page][1]}",
                                  reply_markup=markup)
        await state.update_data({"id": tayyor[current_page][6]})
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('prev_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page = int(call.data.split("_")[1])
    data = await state.get_data()
    first_data = data.get("First_data")
    tayyor = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[1] is not None:
            if order[2] is not None:
                if order[7] == False:
                    if order[8] == False:
                        tayyor.append(order)
    if current_page > 0:
        current_page -= 1
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(tayyor[current_page][1], reply_markup=markup)
        await state.update_data({"id": tayyor[current_page][6]})
        await call.message.delete()
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu birinchi buyurtma . Bundan oldingisi yo'q 🤷🏻‍♂️\n{tayyor[current_page][1]}",
                                  reply_markup=markup)
        await state.update_data({"id": tayyor[current_page][6]})
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="filtrlash_1" or c.data=="kjdhshlksajdkajskuu")
async def first_filtr(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ",reply_markup=viloyatlar_yol_2)
    await call.message.delete()
@dp.callback_query_handler(text="askskhdkshdkfhs")
async def orttt(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    first_data=data.get("First_data")
    tayyor = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[1] is not None:
            if order[2] is not None:
                if order[7] == False:
                    if order[8] == False:
                        tayyor.append(order)
    if len(tayyor) == 0:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer("Tayyor yo'lovchilar hozirda mavjud emas 🙅🏻‍♂️ ", reply_markup=markup)
        await call.message.delete()
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash_1"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="osjdndi"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(tayyor[0][1], reply_markup=markup)
        await state.update_data({"id": tayyor[0][6]})
        await call.message.delete()
@dp.callback_query_handler(text="Bosh menu")
async def boshi_uchun(call:CallbackQuery):
    await call.message.answer("Hurmatli haydovchi !\nSizga kerakli bo'limni tanlang. ",reply_markup=umumiy_menu_1)
    await call.message.delete()
viloyat = {
    "Andijon":"andijon",
    "Namangan":"namangan",
    "Farg'ona":"farg'ona",
    "Buxoro":"buxoro",
    "Toshkent":"toshkent",
    "Sirdaryo":"sirdaryo",
    "Surxondaryo":"surxondaryo",
    "Qashqadaryo":"qashqadaryo",
    "Xorazm":"xorazm",
    "Navoiy":"navoiy",
    "Jizzax":"jizzax",
    "Samarqand":"samarqand",
    "Toshkent shahar":"kent shahar",
    "Qoraqalpog'iston":"qoraqalpoq",
}
@dp.callback_query_handler(lambda c: c.data in viloyat.keys() )
async def filter(call:CallbackQuery,state:FSMContext):
    print(call.data)
    data = await state.get_data()
    first_data = data.get("First_data")
    tayyor = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[5] == call.data:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            tayyor.append(order)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="dnckdhs01_0"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="ieweedkjee01_0"))
    markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash01_1"))
    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshlksajdkajskuu"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
    await call.message.answer(tayyor[0][1], reply_markup=markup)
    await state.update_data({"id": tayyor[0][6]})
    await call.message.delete()
    await state.update_data({"vil": call.data})
@dp.callback_query_handler(lambda c:c.data.startswith("ieweedkjee01_"))
async def viloyat_filter_1(call:CallbackQuery,state:FSMContext):
    current_page=int(call.data.split("_")[1])
    data=await state.get_data()
    first_data=data.get("First_data")
    viloyat = data.get("vil")
    list=[]
    orders=[]
    if first_data=="course:tayyoryolovchi":
        orders=await db.select_tayyor_yolovchi()
    if first_data=="course:tayyorpochta":
        orders=await db.select_tayyor_pochta()
    if first_data=="course:tayyorpochtamashinasi":
        orders=await db.select_tayyor_pochta_mashina()
    if first_data=="course:tayyoryuk":
        orders=await db.select_tayyor_yuk()
    if first_data=="course:tayyoryukmashinasi":
        orders=await db.select_tayyor_yuk_haydovchi()
    if first_data=="course:tayyortaksi":
        orders=await db.select_tayyor_taxi()
    if first_data=="course:tayyorsayohatchi":
        orders=await db.select_tayyor_sayohatchi()
    if first_data=="course:tayyorsayohatgamashina":
        orders=await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[5]==viloyat:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            list.append(order)
    if current_page <len(list)-1:
        current_page += 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"dnckdhs01_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"ieweedkjee01_0{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash01_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshlksajdkajskuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"dnckdhs01_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"ieweedkjee01_0{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash01_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshlksajdkajskuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}", reply_markup=markup)
        await call.message.delete()
@dp.callback_query_handler(lambda c:c.data.startswith("dnckdhs01_"))
async def viloyat_filter_1(call:CallbackQuery,state:FSMContext):
    current_page=int(call.data.split("_")[1])
    data=await state.get_data()
    first_data=data.get("First_data")
    viloyat = data.get("vil")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[5]==viloyat:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            list.append(order)
    if current_page >0:
        current_page -= 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"dnckdhs01_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"ieweedkjee01_0{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash01_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshlksajdkajskuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"dnckdhs01_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"ieweedkjee01_0{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash01_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshlksajdkajskuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu birinchi buyurtma . Bundan oldingisi yo'q 🤷🏻‍♂️\n{list[current_page][1]}", reply_markup=markup)
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="filtrlash01_1")
async def filtr_of_one(call:CallbackQuery,state:FSMContext):
    data=await state.get_data()
    first_data=data.get("First_data")
    viloyat=data.get("vil")
    if viloyat == 'Andijon':
        await call.message.answer("Andijonning qaysi tumanidan yo'lovchi kerak ?", reply_markup=andijon_yol_2)
    if viloyat == 'Namangan':
        await call.message.answer("Namanganning qaysi tumanidan yo'lovchi kerak ?", reply_markup=namangan_yol_2)
    if viloyat == "Farg'ona":
        await call.message.answer("Farg'onaning qaysi tumanidan yo'lovchi kerak ?", reply_markup=fargona_yol_2)
    if viloyat == "Buxoro":
        await call.message.answer("Buxoroning qaysi tumanidan yo'lovchi kerak ?", reply_markup=buxoro_yol_2)
    if viloyat == "Toshkent":
        await call.message.answer("Toshkentning qaysi tumanidan yo'lovchi kerak ?", reply_markup=toshkent_yol_2)
    if viloyat == "Sirdaryo":
        await call.message.answer("Sirdaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=sirdaryo_yol_2)
    if viloyat == "Surxondaryo":
        await call.message.answer("Surxondaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=surxondaryo_yol_2)
    if viloyat == "Qashqadaryo":
        await call.message.answer("Qashqadaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=qashqadaryo_yol_2)
    if viloyat == "Xorazm":
        await call.message.answer("Xorazmning qaysi tumanidan yo'lovchi kerak ?", reply_markup=xorazm_yol_2)
    if viloyat == "Navoiy":
        await call.message.answer("Navoiyning qaysi tumanidan yo'lovchi kerak ?", reply_markup=navoiy_yol_2)
    if viloyat == "Jizzax":
        await call.message.answer("Jizzaxning qaysi tumanidan yo'lovchi kerak ?", reply_markup=jizzax_yol_2)
    if viloyat == "Samarqand":
        await call.message.answer("Samarqandning qaysi tumanidan yo'lovchi kerak ?", reply_markup=samarqand_yol_2)
    if viloyat == "Toshkent shahar":
        await call.message.answer("Toshkent shaharning qaysi tumanidan yo'lovchi kerak ?", reply_markup=tosh_shsha_2)
    if viloyat == "Qoraqalpog'oston":
        await call.message.answer("Qorqalpog'istonning qaysi tumanidan yo'lovchi kerak ?",
                                  reply_markup=qoraqalpogiston_yol_2)
@dp.callback_query_handler(text="ksjhfksdhfkshfk")
async def qaytib_olamiz(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ", reply_markup=viloyatlar_yol_2)
    await call.message.delete()
    #BU YERDA###################
@dp.callback_query_handler(lambda c: c.data in all_district.values() )
async def filter_region(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    first_data = data.get("First_data")
    tayyor = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[0] == call.data:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            tayyor.append(order)
    await state.update_data({"id": tayyor[0][6]})
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev1_0"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next1_0"))
    markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
    await call.message.answer(tayyor[0][1], reply_markup=markup)
    await call.message.delete()
    await state.update_data({"tuman":call.data})
@dp.callback_query_handler(text="kjdhshkuu")
async def ortga_q(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    vil=data.get("vil")
    if vil=='andijon':
        await call.message.answer("Andijonning qaysi tumanidan yo'lovchi kerak ?",reply_markup=andijon_yol_2)
    if vil=='namangan':
        await call.message.answer("Namanganning qaysi tumanidan yo'lovchi kerak ?",reply_markup=namangan_yol_2)
    if vil=="farg'ona":
        await call.message.answer("Farg'onaning qaysi tumanidan yo'lovchi kerak ?",reply_markup=fargona_yol_2)
    if vil == "buxoro":
        await call.message.answer("Buxoroning qaysi tumanidan yo'lovchi kerak ?", reply_markup=buxoro_yol_2)
    if vil == "toshkent":
        await call.message.answer("Toshkentning qaysi tumanidan yo'lovchi kerak ?", reply_markup=toshkent_yol_2)
    if vil == "sirdaryo":
        await call.message.answer("Sirdaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=sirdaryo_yol_2)
    if vil == "surxondaryo":
        await call.message.answer("Surxondaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=surxondaryo_yol_2)
    if vil == "qashqadaryo":
        await call.message.answer("Qashqadaryoning qaysi tumanidan yo'lovchi kerak ?", reply_markup=qashqadaryo_yol_2)
    if vil == "xorazm":
        await call.message.answer("Xorazmning qaysi tumanidan yo'lovchi kerak ?", reply_markup=xorazm_yol_2)
    if vil == "navoiy":
        await call.message.answer("Navoiyning qaysi tumanidan yo'lovchi kerak ?", reply_markup=navoiy_yol_2)
    if vil == "jizzax":
        await call.message.answer("Jizzaxning qaysi tumanidan yo'lovchi kerak ?", reply_markup=jizzax_yol_2)
    if vil == "samarqand":
        await call.message.answer("Samarqandning qaysi tumanidan yo'lovchi kerak ?", reply_markup=samarqand_yol_2)
    if vil == "kent shahar":
        await call.message.answer("Toshkent shaharning qaysi tumanidan yo'lovchi kerak ?", reply_markup=tosh_shsha_2)
    if vil == "qoraqalpoq":
        await call.message.answer("Qorqalpog'istonning qaysi tumanidan yo'lovchi kerak ?", reply_markup=qoraqalpogiston_yol_2)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('next1_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page = int(call.data.split("_")[1])
    data = await state.get_data()
    tuman = data.get("tuman")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[0] == tuman:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            list.append(order)
    if current_page < len(list) - 1:
        current_page += 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:

        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                  reply_markup=markup)
        await state.update_data({"id": list[current_page][6]})
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('prev1_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page = int(call.data.split("_")[1])
    data = await state.get_data()
    tuman = data.get("tuman")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[0] == tuman:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            list.append(order)
    if current_page >0:
        current_page -= 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next1_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu birinchi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                  reply_markup=markup)
        await state.update_data({"id": list[current_page][6]})
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="filtrlash1_1" or c.data=="usdids")
async def first_filtr(call:CallbackQuery):
    viloyat_1 = {
        "1Andijon": "1Andijon",
        "1Namangan": "1Namangan",
        "1Farg'ona": "1Farg'ona",
        "1Buxoro": "1Buxoro",
        "1Toshkent": "1Toshkent",
        "1Sirdaryo": "1Sirdaryo",
        "1Surxondaryo": "1Surxondaryo",
        "1Qashqadaryo": "1Qashqadaryo",
        "1Xorazm": "1Xorazm",
        "1Navoiy": "1Navoiy",
        "1Jizzax": "1Jizzax",
        "1Samarqand": "1Samarqand",
        "1Toshkent shahar": "1Toshkent shahar",
        "1Qoraqalpog'iston": "1Qoraqalpog'iston",
        "1Ortga": "kjdjksdeu",
        "1Bosh menu": "ogirilish",
    }
    markup=InlineKeyboardMarkup(row_width=2)
    for key,value in viloyat_1.items():
        markup.insert(InlineKeyboardButton(text=key[1:],callback_data=value))
    await call.message.answer("Qaysi viloyatga boradigan yo'lovchi kerak ? ",reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="kjdjksdeu")
async def qayt_fil(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get("tuman")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
    for order in orders:
        if order[0] == tuman:
            if order[1] is not None:
                if order[2] is not None:
                    if order[7] == False:
                        if order[8] == False:
                            list.append(order)
    await state.update_data({"id": list[0][6]})
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev1_0"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next1_0"))
    markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash1_1"))
    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="kjdhshkuu"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
    await call.message.answer(list[0][1], reply_markup=markup)
    await call.message.delete()
viloyat_1 = {
    "1Andijon":"andijon",
    "1Namangan":"namangan",
    "1Farg'ona":"farg'ona",
    "1Buxoro":"buxoro",
    "1Toshkent":"toshkent",
    "1Sirdaryo":"sirdaryo",
    "1Surxondaryo":"surxondaryo",
    "1Qashqadaryo":"qashqadaryo",
    "1Xorazm":"xorazm",
    "1Navoiy":"navoiy",
    "1Jizzax":"jizzax",
    "1Samarqand":"samarqand",
    "1Toshkent shahar":"kent shahar",
    "1Qoraqalpog'iston":"qoraqalpoq",

}
@dp.callback_query_handler(lambda c: c.data in viloyat_1.keys() )
async def filter(call:CallbackQuery,state:FSMContext):
    print(call.data)
    data = await state.get_data()
    tuman = data.get("tuman")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
        for order in orders:
            if order[0] == tuman:
                if call.data[1:] in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await state.update_data({"id": list[0][6]})
        await call.message.delete()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
        for order in orders:
            if order[0] == tuman:
                if call.data[1:] in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await state.update_data({"id": list[0][6]})
        await call.message.delete()
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == call.data[1:]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    await state.update_data({"viloyatga":call.data[1:]})
@dp.callback_query_handler(text="usdids")
async def qaytmoq(call:CallbackQuery,state:FSMContext):
    viloyat_1 = {
        "Andijon": "andijon",
        "Namangan": "namangan",
        "Farg'ona": "farg'ona",
        "Buxoro": "buxoro",
        "Toshkent": "toshkent",
        "Sirdaryo": "sirdaryo",
        "Surxondaryo": "surxondaryo",
        "Qashqadaryo": "qashqadaryo",
        "Xorazm": "xorazm",
        "Navoiy": "navoiy",
        "Jizzax": "jizzax",
        "Samarqand": "samarqand",
        "Toshkent shahar": "kent shahar",
        "Qoraqalpog'iston": "qoraqalpoq",
        "Ortga": "kjdjksdeu",
        "Bosh menu": "ogirilish",
    }
    markup = InlineKeyboardMarkup(row_width=2)
    for key, value in viloyat_1.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=key))
    await call.message.answer("Qaysi viloyatga boradigan yo'lovchi kerak ? ", reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('next2_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page=int(call.data.split("_")[1])
    data=await state.get_data()
    tuman=data.get("tuman")
    viloyatiga=data.get("viloyatga")
    first_data=data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                     list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page <len(list)-1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}", reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page < len(list) - 1:
            current_page += 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('prev2_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page = int(call.data.split("_")[1])
    data = await state.get_data()
    tuman = data.get("tuman")
    viloyatiga = data.get("viloyatga")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        if current_page > 0:
            current_page -= 1
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(list[current_page][1], reply_markup=markup)
            await call.message.delete()
        else:
            await state.update_data({"id": list[current_page][6]})
            markup = InlineKeyboardMarkup(row_width=2)
            markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next2_{current_page}"))
            markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
            markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
            markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
            await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                      reply_markup=markup)
            await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="filtrlash2_2")
async def first_filtr(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    viloyatiga = data.get("viloyatga")
    if viloyatiga=="Andijon":
        await call.message.answer("Andijonning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=andijon_yol_1)
    if viloyatiga=="Namangan":
        await call.message.answer("Namanganning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=namangan_yol_1)
    if viloyatiga=="Farg'ona":
        await call.message.answer("Farg'onaning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=fargona_yol_1)
    if viloyatiga=="Buxoro":
        await call.message.answer("Buxoroning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=buxoro_yol_1)
    if viloyatiga=="Toshkent":
        await call.message.answer("Toshkentning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=toshkent_yol_1)
    if viloyatiga=="Sirdaryo":
        await call.message.answer("Sirdaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=sirdaryo_yol_1)
    if viloyatiga=="Surxondaryo":
        await call.message.answer("Surxondaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=surxondaryo_yol_1)
    if viloyatiga == "Qashqadaryo":
        await call.message.answer("Qashqadaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=qashqadaryo_yol_1)
    if viloyatiga == "Xorazm":
        await call.message.answer("Xorazmning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=xorazm_yol_1)
    if viloyatiga == "Navoiy":
        await call.message.answer("Navoiyning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=navoiy_yol_1)
    if viloyatiga == "Jizzax":
        await call.message.answer("Jizzaxning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=jizzax_yol_1)
    if viloyatiga == "Samarqand":
        await call.message.answer("Samarqandning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=samarqand_yol_1)
    if viloyatiga == "Toshkent shahar":
        await call.message.answer("Toshkent shaharning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=tosh_shsha_1)
    if viloyatiga == "Qoraqalpog'iston":
        await call.message.answer("Qoraqalpog'istonning qaysi tumaniga boruvchi yo'lovchi kerak ? ", reply_markup=qoraqalpogiston_yol_1)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="kshkfheiiisuyruy")
async def qayta(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get("tuman")
    viloyatiga = data.get("viloyatga")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    if order[7] == False:
                                        if order[8] == False:
                                                list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
        for order in orders:
            if order[0] == tuman:
                if order[3] == viloyatiga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Filtrlash", callback_data="filtrlash2_2"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorsayohatchi":
        orders = await db.select_tayyor_sayohatchi()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
    if first_data == "course:tayyorsayohatgamashina":
        orders = await db.select_tayyor_sayohatchi_mashina()
        for order in orders:
            if order[0] == tuman:
                if viloyatiga in order[3]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
        await state.update_data({"id": list[0][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev2_0"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next2_0"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="usdids"))
        await call.message.answer(list[0][1], reply_markup=markup)
        await call.message.delete()
@dp.callback_query_handler(lambda c:c.data in tumanlar_all.values())
async def filter_oxir(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    tuman = data.get("tuman")
    viloyatiga = data.get("viloyatga")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    for order in orders:
        if order[0] == tuman:
            if order[3] == viloyatiga:
                if order[4]==call.data.capitalize()[:-1]:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                     list.append(order)
    await state.update_data({"id": list[0][6]})
    await state.update_data({"tumanga":call.data.capitalize()[:-1]})
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data="prev3_0"))
    markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data="next3_0"))
    markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
    markup.insert(InlineKeyboardButton(text="Ortga", callback_data="psodoe"))
    markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
    await call.message.answer(list[0][1], reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('next3_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page=int(call.data.split("_")[1])
    data=await state.get_data()
    tuman=data.get("tuman")
    viloyatiga=data.get("viloyatga")
    tumaniga=data.get("tumanga")
    first_data=data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()
    for order in orders:
        if order[0] == tuman:
            if order[3] == viloyatiga:
                if order[4] == tumaniga:
                    if order[1] is not None:
                        if order[2] is not None:
                            if order[7] == False:
                                if order[8] == False:
                                        list.append(order)
    if current_page <len(list)-1:
        current_page += 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="psodoe"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="psodoe"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}", reply_markup=markup)
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith('prev3_'))
async def keyingi_list_item(call:CallbackQuery,state:FSMContext):
    current_page = int(call.data.split("_")[1])
    data = await state.get_data()
    tuman = data.get("tuman")
    viloyatiga = data.get("viloyatga")
    tumaniga = data.get("tumanga")
    first_data = data.get("First_data")
    list = []
    orders = []
    if first_data == "course:tayyoryolovchi":
        orders = await db.select_tayyor_yolovchi()
    if first_data == "course:tayyorpochta":
        orders = await db.select_tayyor_pochta()
    if first_data == "course:tayyorpochtamashinasi":
        orders = await db.select_tayyor_pochta_mashina()
    if first_data == "course:tayyoryuk":
        orders = await db.select_tayyor_yuk()
    if first_data == "course:tayyoryukmashinasi":
        orders = await db.select_tayyor_yuk_haydovchi()
    if first_data == "course:tayyortaksi":
        orders = await db.select_tayyor_taxi()

    for order in orders:
        if order[0] == tuman:
            if order[1] is not None:
                if order[2] is not None:
                    if order[3] == viloyatiga:
                        if order[4] == tumaniga:
                            if order[7] == False:
                                if order[8] == False:
                                    list.append(order)
    if current_page > 0:
        current_page -= 1
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="psodoe"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(list[current_page][1], reply_markup=markup)
        await call.message.delete()
    else:
        await state.update_data({"id": list[current_page][6]})
        markup = InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Oldingisi", callback_data=f"prev3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Keyingisi", callback_data=f"next3_{current_page}"))
        markup.insert(InlineKeyboardButton(text="Qabul qilish", callback_data="qabul"))
        markup.insert(InlineKeyboardButton(text="Ortga", callback_data="psodoe"))
        markup.insert(InlineKeyboardButton(text="Bosh menu", callback_data="ogirilish"))
        await call.message.answer(f"Bu oxirgi buyurtma . Boshqa qolmadi 🤷🏻‍♂️\n{list[current_page][1]}",
                                  reply_markup=markup)
        await call.message.delete()
@dp.callback_query_handler(lambda c: c.data=="psodoe")
async def first_filtr(call:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    viloyatiga = data.get("viloyatga")
    if viloyatiga=="Andijon":
        await call.message.answer("Andijonning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=andijon_yol_1)
    if viloyatiga=="Namangan":
        await call.message.answer("Namanganning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=namangan_yol_1)
    if viloyatiga=="Farg'ona":
        await call.message.answer("Farg'onaning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=fargona_yol_1)
    if viloyatiga=="Buxoro":
        await call.message.answer("Buxoroning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=buxoro_yol_1)
    if viloyatiga=="Toshkent":
        await call.message.answer("Toshkentning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=toshkent_yol_1)
    if viloyatiga=="Sirdaryo":
        await call.message.answer("Sirdaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=sirdaryo_yol_1)
    if viloyatiga=="Surxondaryo":
        await call.message.answer("Surxondaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=surxondaryo_yol_1)
    if viloyatiga == "Qashqadaryo":
        await call.message.answer("Qashqadaryoning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=qashqadaryo_yol_1)
    if viloyatiga == "Xorazm":
        await call.message.answer("Xorazmning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=xorazm_yol_1)
    if viloyatiga == "Navoiy":
        await call.message.answer("Navoiyning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=navoiy_yol_1)
    if viloyatiga == "Jizzax":
        await call.message.answer("Jizzaxning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=jizzax_yol_1)
    if viloyatiga == "Samarqand":
        await call.message.answer("Samarqandning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=samarqand_yol_1)
    if viloyatiga == "Toshkent shahar":
        await call.message.answer("Toshkent shaharning qaysi tumaniga boruvchi yo'lovchi kerak ? ",reply_markup=tosh_shsha_1)
    if viloyatiga == "Qoraqalpog'iston":
        await call.message.answer("Qoraqalpog'istonning qaysi tumaniga boruvchi yo'lovchi kerak ? ", reply_markup=qoraqalpogiston_yol_1)
    await call.message.delete()