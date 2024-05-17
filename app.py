

from aiogram import Bot, Dispatcher, executor, types
from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
        await db.create()
        # await db.drop_qoshimcha_tumanlar()
        # await db.drop_driver()
        await db.drop_admins()
        # await db.drop_last_tarif()
        # await db.drop_yoldan_odam_info()
        # await db.drop_sayohat_info()
        # await db.drop_driver_info()
        # await db.drop_orders()
        # await db.drop_users()
        # await db.drop_yolovchi()
        # await db.drop_haydovchi()
        # await db.drop_last_order()
        # await db.create_qoshimcha_tumanlar()
        # await db.create_sayohat_info()
        # await db.create_yoldan_odam()
        # await db.create_table_tarif()
        # await db.add_tarif(tarif_name="first", tarif_kuni=3, tarif_narxi=30000)
        # await db.add_tarif(tarif_name="second", tarif_kuni=6, tarif_narxi=50000)
        # await db.add_tarif(tarif_name="third", tarif_kuni=12, tarif_narxi=100000)
        # await db.add_tarif(tarif_name="fourth", tarif_kuni=2, tarif_narxi=0)
        # await db.add_tarif(tarif_name="fifth", tarif_kuni=2, tarif_narxi=0)
        # await db.create_table_users()
        # await db.create_table_driver_info()
        # await db.create_table_driver()
        # await db.create_table_orders()
        # await db.create_table_haydovchi()
        # await db.create_table_yolovchi()
        # await db.create_table_count_last_get_orders()
        await db.create_table_admins()
        await db.add_admin(telegram_id=6132434228)
        await db.add_admin(telegram_id=343103355)
        # await on_startup_notify(dispatcher)
        await set_default_commands(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)


