import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.drop_orders()
    await db.create_table_orders()
    await db.create_table_driver()
    await db.create_table_haydovchi()
    await db.add_haydovchi("odam",
                                   87456656565,
                                   200000,


                             )



    driver = await db.select_driver(id=1)
    print(driver)
    print(driver[3])
    await db.update_balans(5,87456656565)
    driver = await db.select_driver(id=1)
    print(driver)
    print(driver[3])
asyncio.run(test())