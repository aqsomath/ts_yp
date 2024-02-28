from aiogram import types,filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import kirish, umumiy_menu
from loader import dp, db, bot, message_semaphore

admin_ids = [6132434228,343103355]

@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    if message.from_user.id not in admin_ids:
        one = await db.select_tarif(tarif_name='first')
        msg_1 = f"Kuniga {one[3]}ta qabul qilish, oyiga - > {one[2]}"
        two = await db.select_tarif(tarif_name='second')
        msg_2 = f"Kuniga {two[3]}ta qabul qilish, oyiga - > {two[2]}"
        three = await db.select_tarif(tarif_name='third')
        msg_3 = f"Kuniga {three[3]}ta qabul qilish, oyiga - > {three[2]}"
        four = await db.select_tarif(tarif_name='fourth')
        msg_4 = f"Kuniga {four[3]}ta qabul qilish, oyiga - > {four[2]} "
        five = await db.select_tarif(tarif_name='fifth')
        msg_5 = f"/start bosilishiga {five[3]} kun bepul qilish "

        await dp.bot.set_my_commands(
            [
                types.BotCommand("start", "Botni ishga tushurish"),
                types.BotCommand("help", "Yordam"),
                types.BotCommand("statics", "Statistika"),
                types.BotCommand("ban", "Foydalanuvchini blok qilish"),
                types.BotCommand("unban", "Foydalanuvchini blokdan chiqarish"),
                types.BotCommand("first_type", msg_1),
                types.BotCommand("second_type", msg_2),
                types.BotCommand("third_type", msg_3),
                types.BotCommand("fourth_type", msg_4),
                types.BotCommand("fifth_type", msg_5),
                types.BotCommand("tarif_sozlamalari", "Tarif summasi va limitini o'zgartirish"),
                types.BotCommand("filter", "Sozlamalar bo'limi"),
                types.BotCommand("balans_toldirish", "Haydovchi balansini to'ldirish")
            ]
        )
    else:
        await dp.bot.set_my_commands(
            [
                types.BotCommand("start", "Botni ishga tushurish"),
                types.BotCommand("help", "Yordam"),])
    existing_user = await db.select_user(telegram_id=message.from_user.id)
    if existing_user:
        pass
    else:
        await db.add_user(full_name=message.from_user.full_name, username=message.from_user.username,
                          telegram_id=message.from_user.id)
    all_yolovchi=await db.select_all_yolovchi()
    all_haydovchi=await db.select_all_haydovchi()

    yolovchilar=[]
    for i in all_yolovchi:
        yolovchilar.append(i[2])
    haydovchilar=[]
    for m in all_haydovchi:
        haydovchilar.append(m[2])
    if message.from_user.id in yolovchilar:
        await message.answer("Salom yo'lovchi\nSizga kerakli hizmat turini belgilang ?", reply_markup=umumiy_menu)
        await message.delete()


    elif message.from_user.id in haydovchilar:
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
        await message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await message.delete()
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=kirish)
        # if message.from_user.id not in first:
        #     if message.from_user.id not in second:
        #         if message.from_user.id not in third:
        #             if message.from_user.id not in fifth:
        #                 fourth.append(message.from_user.id)
        #                 print("4 - ta'rifga avtomatik qo'shildi")
        #                 await asyncio.sleep(60*60*24*3)
        #                 fourth.remove(message.from_user.id)
        # else:
        #     print("Boshqa ta'rifga oldin qo'shilgan")




