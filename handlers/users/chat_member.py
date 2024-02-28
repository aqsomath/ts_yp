from aiogram import types

from loader import bot, dp, db


@dp.my_chat_member_handler()
async def update(update:types.ChatMemberUpdated):
 if update.new_chat_member.status == "kicked":
    await bot.send_message(chat_id=6132434228, text=f"Botni kimdir blocklab qo'ydi! <a href='tg://user?id={update.from_user.id}'>inline mention of a user</a>")
    await db.delete_users(telegram_id = update.from_user.id)
    all_yolovchi = await db.select_all_yolovchi()
    all_haydovchi = await db.select_all_haydovchi()

    yolovchilar = []
    for i in all_yolovchi:
        yolovchilar.append(i[2])
    haydovchilar = []
    for m in all_haydovchi:
        haydovchilar.append(m[2])
    if update.from_user.id in haydovchilar:
        await db.delete_haydovchi(update.from_user.id)
    if update.from_user.id in yolovchilar:
        await db.delete_yolovchi(update.from_user.id)
 else:
     count = update.chat.id
     await bot.send_message(chat_id=6132434228, text=f"Botga yangi foydalanuvchi qo'shildi! ")