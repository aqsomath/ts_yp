import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.create_table_orders()
    await db.add_order_tayyor_taxi(
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        54654654654,
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
        "asdasda",
    )
    orders = await db.select_all_orders()
    print(orders)
asyncio.run(test())