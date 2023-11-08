import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.drop_orders()

    await db.create_table_orders()

    print("Yaratildi")
    msg = "sdjsjkdhskdjh"
    msg_full = "sdjsjkdhskdjh_jdhjasgjhgdjgsdgsd"
    await db.add_order_tayyor_taxi(msg,msg_full,"ulug'nor",'5654645654654654',"dsdsdsd",987987987987987,"adasdasdas","asdasdakshdasjdg","asdsdsdsd","sdsdsdsd","shah0","alksdjlasldajsdk","a;lsdjlksjdajk","alshjdkahsdha","alshdkahska", "12121","12121","12121","12121","12121")
    print("qo'shildi")
    print("qo'shildi")
    x=await db.count_orders()
    print(x)
    order= await db.select_tayyor_pochta()
    print(order)
    # print("Users jadvalini yaratamiz...")
    # await db.drop_users()
    # await db.create_table_users()
    # print("Yaratildi")
    #
    # print("Foydalanuvchilarni qo'shamiz")
    # await db.add_user("anvar", "sariqdev", 85656565 )
    # print("Qo'shildi")
    #
    # await db.update_user_tayyor_taxi("Andijon viloyati\nUlug'nor tumani\nadasasdasa\nasasasdsassaasn\nsdsd\n",  85656565 )
    # await db.update_user_region("Ulug'nor", 85656565)
    # print("Qo'shildi")
    #
    # users = await db.select_all_users()
    # print(f"Barcha foydalanuvchilar: {users}")
    #
    # user = await db.select_user(id=1)
    # print(f"Foydalanuvchi: {user}")


asyncio.run(test())