import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.drop_orders()
    await db.drop_driver()

    await db.create_table_orders()
    await db.create_table_driver()

    print("dsdsd")
asyncio.run(test())