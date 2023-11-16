import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.drop_driver()
    await db.create_table_driver()
    await db.add_driver("odam","yuk","pochta",565454)
    await db.add_driver("odam","yuk","pochta",56565656)
    await db.add_driver("odam","yuk","pochta",784512)
    await db.add_driver("odam","yuk","pochta",124587)
    await db.add_driver("odam","yuk","pochta",236598)
    await db.add_driver_info("dsdsd","asasasas",25454545)
    x=await db.select_all_driver()
    for i in x:
        print(i[1])




asyncio.run(test())