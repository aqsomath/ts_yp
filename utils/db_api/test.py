import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()

    await db.create()
    await db.drop_orders()
    await db.create_table_orders()
    await db.create_table_driver()
    await db.create_table_haydovchi()
    await db.add_driver("odam",
                                   "sdsjskjdkjshdf",
                                   "200000",
                                   200000,
                                   "kjhdkjsds",


                             )
    await db.add_driver("odam",
                        "sdsjskjdkjshdf",
                        "200000",
                        6546465,
                        "kjhdkjsds",

                      )
    offset = -28
    limit = 28
    while True:
        offset+=limit
        drivers = await db.select_all_drivers(limit=limit,offset=offset)
        print(drivers)

asyncio.run(test())