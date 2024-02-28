import asyncio
import datetime
from datetime import timedelta

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ChatMemberUpdated
from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import dp,db,bot

admin_ids = [6132434228,343103355]

user_of_banned = []
class BanStatesGroup(StatesGroup):
    id = State()
    day = State()
class UnBanStatesGroup(StatesGroup):
    id = State()
class BalansToldirish(StatesGroup):
    id = State()
    money = State()
@dp.message_handler(commands=['balans_toldirish'])
async def pay_balans(message:Message,state:FSMContext):
    await message.answer("Foydalanuvchining ID sini kiriting :")
    await BalansToldirish.id.set()

@dp.message_handler(state=BalansToldirish.id)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        id = int(message.text)
        await state.update_data({"id":id})
        await message.answer("Qanchaga to'ldirasiz. Son bilan to'liq kirgizing.")
        await message.delete()
        await BalansToldirish.money.set()
@dp.message_handler(state=BalansToldirish.money)
async def balans_id(message:Message,state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        id=data.get("id")
        d=await db.select_driver(id=id)
        await db.update_balans(telegram_id=d[2],balans=int(message.text))
        print(d)
        await message.answer("Balans to'ldirildi")
        await message.delete()
        await state.finish()
@dp.message_handler(commands=['ban'])
async def ban_user(message: types.Message,state:FSMContext):
    await message.answer("Foydalanuvchi ID sini kiriting :")
    await message.delete()
    await BanStatesGroup.id.set()
@dp.message_handler(state=BanStatesGroup.id)
async def id_get(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:

            user = await db.select_user(id=id)
            await state.update_data({"id":user[3]})
            user_of_banned.append(user[3])
            await message.answer("Necha kunga ban bo'lsin")
            await BanStatesGroup.day.set()
        except TypeError:
            await message.answer("Bu ID da foydalanuvchi mavjud emas . ")
@dp.message_handler(state=BanStatesGroup.day)
async def how_many_day(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    data = await state.get_data()
    id = data.get("id")
    try:
        if message.text.isdigit():
            day = int(message.text)
            await message.answer(f"Foydalanuvchi {day} kun ichida bloklangan holatda bo'ladi")
            await message.delete()
            await state.finish()
            # await asyncio.sleep(15)
            await asyncio.sleep(60*60*24*day)
            user_of_banned.remove(id)
    except TypeError:
        await message.answer("Bu ID da foydalanuvchi mavjud emas .")



@dp.message_handler(commands=['unban'])
async def unban_user(message: types.Message):
    await message.answer("Foydalanuvchi ID sini kiriting :")
    await message.delete()
    await UnBanStatesGroup.id.set()
@dp.message_handler(state=UnBanStatesGroup.id)
async def id_get_ban_user(message:Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer("Iltimos son kiriting 🙅‍♂️🙅‍♂️🙅‍♂️")
    if message.text.isdigit():
        id = int(message.text)
        try:
            user = await db.select_user(id=id)
            if user[3] in user_of_banned:
                user_of_banned.remove(user[3])
                await message.answer("Foydalanuvchi blokdan chiqarildi")
                await message.delete()
                await state.finish()
            else:
                await message.answer("Bu foydalanuvchi bloklanmagan !")
                await message.delete()
        except TypeError :
            await message.answer("Bu ID da foydalanuvchi mavjud emas .")


@dp.message_handler(commands=['statics'])
async def umumiy_statistika(message:Message,state:FSMContext):
    data = await state.get_data()
    users = data.get("users")
    drivers = data.get("drivers")
    yolovchi = data.get("yolovchi")
    plus_user = ""
    minus_user = ""
    plus_yolovchi = ""
    minus_yolovchi = ""
    plus_haydovchi = ""
    minus_haydovchi = ""
    all_users = await db.count_users()
    await state.update_data({"users":all_users})
    count_haydovchi = await db.count_haydovchi()
    await state.update_data({"drivers": count_haydovchi})
    count_yolovchi = await db.count_yolovchi()
    await state.update_data({"yolovchi": count_yolovchi})

    bugun_taxi = []
    bugun_yolovchi = []
    bugun_pochta = []
    bugun_pochta_mashina = []
    bugun_yuk = []
    bugun_yuk_mashina = []
    bugun_sayohatchi = []
    bugun_sayohatchi_mashina = []
    users_last = await db.get_users_joined_in_last_day()
    orders_last = await db.get_orders_joined_in_last_day()

    bugun_driver = await db.get_drivers_joined_in_last_day()
    bugun_yolovchi = await db.get_yolovchi_joined_in_last_day()
    for i in orders_last:
        if i[15] is not None:
            bugun_yolovchi.append(i)
        if i[9] is not None:
            bugun_pochta.append(i)
        if i[17] is not None:
            bugun_pochta_mashina.append(i)
        if i[11] is not None:
            bugun_yuk.append(i)
        if i[13] is not None:
            bugun_yuk_mashina.append(i)
        if i[3] is not None:
            bugun_taxi.append(i)
        if i[19] is not None:
            bugun_sayohatchi.append(i)
        if i[21] is not None:
            bugun_sayohatchi_mashina.append(i)
    if users is not None:
        change_users = all_users - users
        if change_users>0:
            plus_user =change_users
            minus_user = 0
        if change_users<0:
            plus_user =0
            minus_user =change_users*(-1)
        if change_users==0:
            plus_user =0
            minus_user = 0

        change_haydovchi = count_haydovchi - drivers
        if change_haydovchi > 0:
            plus_haydovchi = change_haydovchi
            minus_haydovchi = 0
        if change_haydovchi < 0:
            plus_haydovchi = 0
            minus_haydovchi = change_haydovchi*(-1)
        if change_haydovchi == 0:
            plus_haydovchi = 0
            minus_haydovchi = 0

        change_yolovchi = count_yolovchi - yolovchi

        if change_yolovchi > 0:
            plus_yolovchi = change_yolovchi
            minus_yolovchi = 0
        if change_yolovchi < 0:
            plus_yolovchi = 0
            minus_yolovchi = change_yolovchi*(-1)
        if change_yolovchi == 0:
            plus_yolovchi = 0
            minus_yolovchi = 0


    all_orders = await db.count_orders()
    taxi =[]
    taxi_kelishildi =[]
    taxi_kelishilmoqda =[]
    taxi_rad =[]
    tayyor_taxi =await db.select_tayyor_taxi()
    for a in tayyor_taxi:
        if a[2] is not None:
            taxi.append(a)
            if a[2] == "Kelishildi":
                taxi_kelishildi.append(a)
            if a[2] == "Kelishilmoqda":
                taxi_kelishilmoqda.append(a)
            if a[2] == "Rad etildi":
                taxi_rad.append(a)
    yolovchi = []
    yolovchi_kelishildi = []
    yolovchi_kelishilmoqda = []
    yolovchi_rad = []
    tayyor_yolovchi=await db.select_tayyor_yolovchi()
    for b in tayyor_yolovchi:
        if b[2] is not None:
            yolovchi.append(b)
            if b[2] == "Kelishildi":
                yolovchi_kelishildi.append(b)
            if b[2] == "Kelishilmoqda...!":
                yolovchi_kelishilmoqda.append(b)
            if b[2] == "Rad etildi":
                yolovchi_rad.append(b)
    tayyor_pochta= await db.select_tayyor_pochta()
    pochta = []
    pochta_kelishildi = []
    pochta_kelishilmoqda = []
    pochta_rad = []
    for c in tayyor_pochta:
        if c[2] is not None:
            pochta.append(c)
            if c[2] == "Kelishildi":
                pochta_kelishildi.append(c)
            if c[2] == "Kelishilmoqda...!":
                pochta_kelishilmoqda.append(c)
            if c[2] == "Rad etildi":
                pochta_rad.append(c)
    tayyor_pochta_mashina= await db.select_tayyor_pochta_mashina()
    pochta_mashina = []
    pochta_mashina_kelishildi = []
    pochta_mashina_kelishilmoqda = []
    pochta_mashina_rad = []
    for d in tayyor_pochta_mashina:
        if d[2] is not None:
            pochta_mashina.append(d)
            if d[2] == "Kelishildi":
                pochta_mashina_kelishildi.append(d)
            if d[2] == "Kelishilmoqda...!":
                pochta_mashina_kelishilmoqda.append(d)
            if d[2] == "Rad etildi":
                pochta_mashina_rad.append(d)
    tayyor_yuk= await db.select_tayyor_yuk()
    yuk = []
    yuk_kelishildi = []
    yuk_kelishilmoqda = []
    yuk_rad = []
    for i in tayyor_yuk:
        if i[2] is not None:
            yuk.append(i)
            if i[2] == "Kelishildi":
                yuk_kelishildi.append(i)
            if i[2] == "Kelishilmoqda...!":
                yuk_kelishilmoqda.append(i)
            if i[2] == "Rad etildi":
                yuk_rad.append(i)
    tayyor_yuk_mashina=await db.select_tayyor_yuk_haydovchi()
    yuk_mashina=[]
    yuk_mashina_kelishildi = []
    yuk_mashina_kelishilmoqda = []
    yuk_mashina_rad = []
    for f in tayyor_yuk_mashina:
        if f[2] is not None:
            yuk_mashina.append(f)
            if f[2] == "Kelishildi":
                yuk_mashina_kelishildi.append(f)
            if f[2] == "Kelishilmoqda...!":
                yuk_mashina_kelishilmoqda.append(f)
            if f[2] == "Rad etildi":
                yuk_mashina_rad.append(f)
    tayyor_sayohatchi=await db.select_tayyor_sayohatchi()
    sayohatchi = []
    sayohatchi_kelishildi = []
    sayohatchi_kelishilmoqda = []
    sayohatchi_rad = []
    for j in tayyor_sayohatchi:
        if j[2] is not None:
            sayohatchi.append(j)
            if j[2] == "Kelishildi":
                sayohatchi_kelishildi.append(j)
            if j[2] == "Kelishilmoqda...!":
                sayohatchi_kelishilmoqda.append(j)
            if j[2] == "Rad etildi":
                sayohatchi_rad.append(j)
    tayyor_sayohatchi_mashina= await db.select_tayyor_sayohatchi_mashina()
    sayohatchi_mashina = []
    sayohatchi_mashina_kelishildi = []
    sayohatchi_mashina_kelishilmoqda = []
    sayohatchi_mashina_rad = []
    for k in tayyor_sayohatchi_mashina:
        if k[2]  is not None:
            sayohatchi_mashina.append(k)
            if k[2] == "Kelishildi":
                sayohatchi_mashina_kelishildi.append(k)
            if k[2] == "Kelishilmoqda...!":
                sayohatchi_mashina_kelishilmoqda.append(k)
            if k[2] == "Rad etildi":
                sayohatchi_mashina_rad.append(k)

    await message.answer(f"<b>Jami foydalanuvchilar - {all_users}</b>\n"
                         f"<code>Qo'shildi - {plus_user}</code>\n"
                         f"<code>Tark etdi - {minus_user}</code>\n"
                         f"<code>Bugun qo'shildi - {len(users_last)}</code>\n"
                         f"<b>Jami yo'lovchi - {count_yolovchi}</b>\n"
                         f"<code>Qo'shildi - {plus_yolovchi}</code>\n"
                         f"<code>Tark etdi - {minus_yolovchi}</code>\n"
                         f"<code>Bugun qo'shildi - {len(bugun_yolovchi)}</code>\n"
                         f"<b>Jami haydovchilar - {count_haydovchi}</b>\n"
                         f"<code>Qo'shildi - {plus_haydovchi}</code>\n"
                         f"<code>Tark etdi - {minus_haydovchi}</code>\n"
                         f"<code>Bugun qo'shildi - {len(bugun_driver)}</code>\n"
                         f"<b>Jami buyurtmalar - {all_orders}</b>\n"
                         f"<code>Bugungi jami buyurtmalar - {len(orders_last)}</code>\n"
                         f"<b>Tayyor taxi- {len(taxi)}</b>\n"
                         f"<code>    Kelishilgan- {len(taxi_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(taxi_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(taxi_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi - {len(bugun_taxi)}</code>\n"
                         f"<b>Tayyor yo'lovchi- {len(yolovchi)}</b>\n"
                          f"<code>    Kelishilgan- {len(yolovchi_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(yolovchi_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(yolovchi_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_yolovchi)}</code>\n"
                         f"<b>Tayyor pochta- {len(pochta)}</b>\n"
                         f"<code>    Kelishilgan- {len(pochta_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(pochta_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(pochta_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_pochta)}</code>\n"
                         f"<b>Tayyor pochta mashina- {len(pochta_mashina)}</b>\n"
                         f"<code>    Kelishilgan- {len(pochta_mashina_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(pochta_mashina_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(pochta_mashina_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_pochta_mashina)}</code>\n"
                         f"<b>Tayyor yuk - {len(yuk)}</b>\n"
                         f"<code>    Kelishilgan- {len(yuk_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(yuk_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(yuk_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_yuk)}</code>\n"
                         f"<b>Tayyor yuk  mashina- {len(yuk_mashina)}</b>\n"
                         f"<code>    Kelishilgan- {len(yuk_mashina_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(yuk_mashina_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(yuk_mashina_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_yuk_mashina)}</code>\n"
                         f"<b>Tayyor sayohatchi- {len(sayohatchi)}</b>\n"
                         f"<code>    Kelishilgan- {len(sayohatchi_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(sayohatchi_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(sayohatchi_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_sayohatchi)}</code>\n"
                         f"<b>Tayyor sayohatchi mashina- {len(sayohatchi_mashina)}</b>\n"
                         f"<code>    Kelishilgan- {len(sayohatchi_mashina_kelishildi)}</code>\n"
                         f"<code>    Rad etildi- {len(sayohatchi_mashina_rad)}</code>\n"
                         f"<code>    Jarayonda- {len(sayohatchi_mashina_kelishilmoqda)}</code>\n"
                         f"<code>    Bugungi- {len(bugun_sayohatchi_mashina)}</code>\n"
                         )

@dp.message_handler(commands=['tarif_1'])
async def tarif_1_ga_otkazish(message:Message,state:FSMContext):
    await message.answer("1 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")

@dp.message_handler(commands=['tarif_2'])
async def tarif_1_ga_otkazish(message:Message,state:FSMContext):
    await message.answer("1 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")

@dp.message_handler(commands=['tarif_3'])
async def tarif_1_ga_otkazish(message:Message,state:FSMContext):
    await message.answer("1 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")

@dp.message_handler(commands=['tarif_4'])
async def tarif_1_ga_otkazish(message:Message,state:FSMContext):
    await message.answer("1 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")

@dp.message_handler(commands=['tarif_5'])
async def tarif_1_ga_otkazish(message:Message,state:FSMContext):
    await message.answer("1 - ta'rifga o'tkaziladigan haydovchi ID sini kiriting")


