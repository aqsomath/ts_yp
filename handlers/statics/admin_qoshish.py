from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from handlers.users.start import admin_ids
from loader import dp,db,bot
from aiogram.dispatcher.filters.state import StatesGroup, State

admin_qoshish = []
admin_chiqarish = []
balans_toldirish = []
balans_ayrish = []
@dp.callback_query_handler(text="adminlarroyxati")
async def adminlar_qatori(call:CallbackQuery):
    users = await db.select_all_users()
    markup = InlineKeyboardMarkup(row_width=2)
    admins ={}
    for i in admin_ids:
        for user in users:
            if user[3]==i:
                admins[user[1]]=i
    for key,value in admins.items():
        markup.insert(InlineKeyboardButton(text=key,callback_data=f"adminlar_{value}"))
    markup.insert(InlineKeyboardButton(text="Admin qo'shish",callback_data="asosiyqoshish"))
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="adminpanel"))
    await call.message.answer("Adminlar", reply_markup=markup)
    await call.message.delete()

class AdminkopaytirishState(StatesGroup):
    admin_id = State()
@dp.callback_query_handler(text="asosiyqoshish")
async def admin_qosh(call:CallbackQuery):
    await call.message.answer("Yangi admin telegram id sini kiriting :")
    await call.message.delete()
    await AdminkopaytirishState.admin_id.set()
@dp.message_handler(state=AdminkopaytirishState.admin_id)
async def admin_add(message:Message,state:FSMContext):
    if message.text.isdigit():
        id = int(message.text)
        user = await db.select_user(telegram_id=id)
        if user is not None:
            admin_ids.append(id)
            users = await db.select_all_users()
            markup = InlineKeyboardMarkup(row_width=2)
            admins = {}
            for i in admin_ids:
                for user in users:
                    if user[3] == i:
                        admins[user[1]] = i
            for key, value in admins.items():
                markup.insert(InlineKeyboardButton(text=key, callback_data=f"adminlar_{value}"))
            markup.insert(InlineKeyboardButton(text="Admin qo'shish", callback_data="asosiyqoshish"))
            markup.insert(InlineKeyboardButton(text="Ortga", callback_data="adminpanel"))
            await message.answer(f"Adminlar ro'yxatiga {user[1]} qo'shildi", reply_markup=markup)
            await message.delete()
            await state.finish()
        else:
            await message.answer("Bunday ID bot foydalanuvchilari orasidan topilmadi !")
            await state.finish()
    else:
        await message.answer("Iltimos son kiriting !!!")
        await AdminkopaytirishState.admin_id.set()
@dp.callback_query_handler(text="adminpanel")
async def admin_panelga_qaytish(call:CallbackQuery):
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
    await call.message.answer(reply_markup=markup, text="Admin bo'lim")
    await call.message.delete()

@dp.callback_query_handler(lambda c: c.data.startswith("adminlar_"))
async def admin_haqida(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[1])
    markup = InlineKeyboardMarkup()
    delete = InlineKeyboardButton(text="O'chirish",callback_data=f"delete_{telegram_id}")
    permission = InlineKeyboardButton(text="Ruxsatlar",callback_data=f"permission_{telegram_id}")
    ortga = InlineKeyboardButton(text="Ortga",callback_data=f"adminlarroyxati")
    markup.add(delete,permission)
    markup.add(ortga)
    admin = await db.select_user(telegram_id=telegram_id)
    await call.message.answer(f"{admin[1]}",reply_markup=markup)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data.startswith("delete_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[1])
    admin_ids.remove(telegram_id)
    users = await db.select_all_users()
    markup = InlineKeyboardMarkup(row_width=2)
    admins = {}
    for i in admin_ids:
        for user in users:
            if user[3] == i:
                admins[user[1]] = i
    for key, value in admins.items():
        markup.insert(InlineKeyboardButton(text=key, callback_data=f"adminlar_{value}"))
    markup.insert(InlineKeyboardButton(text="Admin qo'shish", callback_data="asosiyqoshish"))
    markup.insert(InlineKeyboardButton(text="Ortga",callback_data="adminpanel"))
    await call.message.answer("Adminlar", reply_markup=markup)
    await call.message.delete()

@dp.callback_query_handler(lambda c: c.data.startswith("permission_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[1])
    markup = InlineKeyboardMarkup()
    if telegram_id in admin_qoshish:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish✅ ", callback_data=f"add_admin_{telegram_id}")
    else:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish ", callback_data=f"add_admin_{telegram_id}")
    if telegram_id in admin_chiqarish:
        admin_ochir = InlineKeyboardButton(text="Admin o'chirish✅", callback_data=f"remove_admin_{telegram_id}")
    else:
        admin_ochir = InlineKeyboardButton(text="Admin o'chirish", callback_data=f"remove_admin_{telegram_id}")
    if telegram_id in balans_toldirish:
        balans_toldir = InlineKeyboardButton(text="Balans to'ldirish✅", callback_data=f"add_balans_{telegram_id}")
    else:
        balans_toldir = InlineKeyboardButton(text="Balans to'ldirish", callback_data=f"add_balans_{telegram_id}")
    if telegram_id in balans_ayrish:
        balans_ayr = InlineKeyboardButton(text="Balans ayirish✅", callback_data=f"frac_balans_{telegram_id}")
    else:
        balans_ayr = InlineKeyboardButton(text="Balans ayirish", callback_data=f"frac_balans_{telegram_id}")
    ortga= InlineKeyboardButton(text="Ortga",callback_data=f"adminlar_{telegram_id}")
    markup.add(admin_qosh, admin_ochir)
    markup.add(balans_toldir, balans_ayr)
    markup.add(ortga)
    await call.message.answer("Admin ruxsatlari",reply_markup=markup)
    await call.message.delete()
@dp.callback_query_handler(lambda c: c.data.startswith("add_admin_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[2])
    markup = InlineKeyboardMarkup()
    if telegram_id in admin_qoshish:
        admin_qoshish.remove(telegram_id)
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish ",callback_data=f"add_admin_{telegram_id}")
    else:
        admin_qoshish.append(telegram_id)
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish✅ ", callback_data=f"add_admin_{telegram_id}")
    if telegram_id in admin_chiqarish:
        admin_ochir = InlineKeyboardButton(text="Admin o'chirish✅", callback_data=f"remove_admin_{telegram_id}")
    else:
        admin_ochir = InlineKeyboardButton(text="Admin o'chirish", callback_data=f"remove_admin_{telegram_id}")
    if telegram_id in balans_toldirish:
        balans_toldir = InlineKeyboardButton(text="Balans to'ldirish✅", callback_data=f"add_balans_{telegram_id}")
    else:
        balans_toldir = InlineKeyboardButton(text="Balans to'ldirish", callback_data=f"add_balans_{telegram_id}")
    if telegram_id in balans_ayrish:
        balans_ayr = InlineKeyboardButton(text="Balans ayirish✅", callback_data=f"frac_balans_{telegram_id}")
    else:
        balans_ayr = InlineKeyboardButton(text="Balans ayirish", callback_data=f"frac_balans_{telegram_id}")
    ortga= InlineKeyboardButton(text="Ortga",callback_data=f"adminlar_{telegram_id}")
    markup.add(admin_qosh,admin_ochir)
    markup.add(balans_toldir,balans_ayr)
    markup.add(ortga)
    await call.message.edit_reply_markup(markup)

@dp.callback_query_handler(lambda c: c.data.startswith("remove_admin_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[2])
    markup = InlineKeyboardMarkup()
    if telegram_id in admin_qoshish:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish ✅",callback_data=f"add_admin_{telegram_id}")
    else:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish", callback_data=f"add_admin_{telegram_id}")
    if telegram_id in admin_chiqarish:
        admin_chiqarish.remove(telegram_id)
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish",callback_data=f"remove_admin_{telegram_id}")
    else:
        admin_chiqarish.append(telegram_id)
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish✅",callback_data=f"remove_admin_{telegram_id}")
    if telegram_id in balans_toldirish:
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish✅",callback_data=f"add_balans_{telegram_id}")
    else:
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish",callback_data=f"add_balans_{telegram_id}")
    if telegram_id in balans_ayrish:
        balans_ayr= InlineKeyboardButton(text="Balans ayirish✅",callback_data=f"frac_balans_{telegram_id}")
    else:
        balans_ayr= InlineKeyboardButton(text="Balans ayirish",callback_data=f"frac_balans_{telegram_id}")
    ortga= InlineKeyboardButton(text="Ortga",callback_data=f"adminlar_{telegram_id}")
    markup.add(admin_qosh,admin_ochir)
    markup.add(balans_toldir,balans_ayr)
    markup.add(ortga)
    await call.message.edit_reply_markup(markup)

@dp.callback_query_handler(lambda c: c.data.startswith("add_balans_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[2])
    markup = InlineKeyboardMarkup()
    if telegram_id in admin_qoshish:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish ✅",callback_data=f"add_admin_{telegram_id}")
    else:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish", callback_data=f"add_admin_{telegram_id}")
    if telegram_id in admin_chiqarish:
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish✅",callback_data=f"remove_admin_{telegram_id}")
    else:
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish",callback_data=f"remove_admin_{telegram_id}")
    if telegram_id in balans_toldirish:
        balans_toldirish.remove(telegram_id)
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish",callback_data=f"add_balans_{telegram_id}")
    else:
        balans_toldirish.append(telegram_id)
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish✅",callback_data=f"add_balans_{telegram_id}")
    if telegram_id in balans_ayrish:
        balans_ayr= InlineKeyboardButton(text="Balans ayirish✅",callback_data=f"frac_balans_{telegram_id}")
    else:
        balans_ayr= InlineKeyboardButton(text="Balans ayirish",callback_data=f"frac_balans_{telegram_id}")
    ortga= InlineKeyboardButton(text="Ortga",callback_data=f"adminlar_{telegram_id}")
    markup.add(admin_qosh,admin_ochir)
    markup.add(balans_toldir,balans_ayr)
    markup.add(ortga)
    await call.message.edit_reply_markup(markup)


@dp.callback_query_handler(lambda c: c.data.startswith("frac_balans_"))
async def adminni_chiqarish(call:CallbackQuery):
    telegram_id = int(call.data.split("_")[2])
    markup = InlineKeyboardMarkup()
    if telegram_id in admin_qoshish:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish ✅",callback_data=f"add_admin_{telegram_id}")
    else:
        admin_qosh = InlineKeyboardButton(text="Admin qo'shish", callback_data=f"add_admin_{telegram_id}")
    if telegram_id in admin_chiqarish:
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish✅",callback_data=f"remove_admin_{telegram_id}")
    else:
        admin_ochir= InlineKeyboardButton(text="Admin o'chirish",callback_data=f"remove_admin_{telegram_id}")
    if telegram_id in balans_toldirish:
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish✅",callback_data=f"add_balans_{telegram_id}")
    else:
        balans_toldir= InlineKeyboardButton(text="Balans to'ldirish",callback_data=f"add_balans_{telegram_id}")
    if telegram_id in balans_ayrish:
        balans_ayrish.remove(telegram_id)
        balans_ayr= InlineKeyboardButton(text="Balans ayirish",callback_data=f"frac_balans_{telegram_id}")
    else:
        balans_ayrish.append(telegram_id)
        balans_ayr= InlineKeyboardButton(text="Balans ayirish✅",callback_data=f"frac_balans_{telegram_id}")
    ortga= InlineKeyboardButton(text="Ortga",callback_data=f"adminlar_{telegram_id}")
    markup.add(admin_qosh,admin_ochir)
    markup.add(balans_toldir,balans_ayr)
    markup.add(ortga)
    await call.message.edit_reply_markup(markup)