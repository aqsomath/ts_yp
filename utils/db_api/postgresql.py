from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )
        # !/usr/bin/python

    # import psycopg2
    #
    # conn = psycopg2.connect(
    #     host="176.57.214.12",
    #     database="default_db",
    #     user="gen_user",
    #     password="Akmaljon2001"
    # )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result


    #  USERS TABLE

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id INTEGER NULL
       );
        """
        await self.execute(sql, execute=True)

    async def create_table_orders(self):
        sql = """
        CREATE TABLE Orders (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NULL,
        tayyor_taxi TEXT NULL,
        tayyor_taxi_full TEXT NULL,
        region TEXT NULL,
        viloyatga TEXT NULL,
        tumanga TEXT NULL,
        tayyor_pochta TEXT NULL,
        tayyor_pochta_full TEXT NULL,
        tayyor_yuk TEXT NULL,
        tayyor_yuk_full TEXT NULL,
        tayyor_yuk_haydovchisi TEXT NULL,
        tayyor_yuk_haydovchisi_full TEXT NULL,
        tayyor_yolovchi TEXT NULL,
        tayyor_yolovchi_full TEXT NULL,
        tayyor_pochta_mashina TEXT NULL,
        tayyor_pochta_mashina_full TEXT NULL,
        tayyor_sayohatchi TEXT NULL,
        tayyor_sayohatchi_full TEXT NULL,
        tayyor_sayohatchi_mashina TEXT NULL,
        tayyor_sayohatchi_full_mashina TEXT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_order_tayyor_taxi(self,
                                    tayyor_taxi,
                                    tayyor_taxi_full,
                                    region,
                                    tumanga,
                                    viloyatga,
                                    telegram_id,
                                    tayyor_pochta,
                                    tayyor_pochta_full,
                                    tayyor_yuk,
                                    tayyor_yuk_full,
                                    tayyor_yuk_haydovchisi,
                                    tayyor_yuk_haydovchisi_full,
                                    tayyor_yolovchi,
                                    tayyor_yolovchi_full,
                                    tayyor_pochta_mashina,
                                    tayyor_pochta_mashina_full,
                                    tayyor_sayohatchi,
                                    tayyor_sayohatchi_full,
                                    tayyor_sayohatchi_mashina,
                                    tayyor_sayohatchi_full_mashina):
        sql = "INSERT INTO orders (" \
              "tayyor_taxi," \
              "tayyor_taxi_full, " \
              "region," \
              "tumanga," \
              "viloyatga," \
              " telegram_id," \
              "tayyor_pochta," \
              "tayyor_pochta_full," \
              "tayyor_yuk," \
              " tayyor_yuk_full," \
              "tayyor_yuk_haydovchisi," \
              "tayyor_yuk_haydovchisi_full," \
              "tayyor_yolovchi,"\
              "tayyor_yolovchi_full ," \
              "tayyor_pochta_mashina," \
              "tayyor_pochta_mashina_full," \
              "tayyor_sayohatchi," \
              "tayyor_sayohatchi_full," \
              "tayyor_sayohatchi_mashina,"\
              "tayyor_sayohatchi_full_mashina" \
              ") VALUES(" \
              "$1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12 , $13, $14, $15, $16, $17, $18, $19, $20" \
              ") " \
              "returning *"
        return await self.execute(
            sql, tayyor_taxi,
            tayyor_taxi_full,
            region,
            tumanga,
            viloyatga,
            telegram_id,
            tayyor_pochta,
            tayyor_pochta_full,
            tayyor_yuk,
            tayyor_yuk_full,
            tayyor_yuk_haydovchisi,
            tayyor_yuk_haydovchisi_full,
            tayyor_yolovchi,
            tayyor_yolovchi_full,
            tayyor_pochta_mashina,
            tayyor_pochta_mashina_full,
            tayyor_sayohatchi,
            tayyor_sayohatchi_full,
            tayyor_sayohatchi_mashina,
            tayyor_sayohatchi_full_mashina,
            fetchrow=True
        )

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)
    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)
    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)



    async def select_taxi_orders(self):
        sql = "SELECT tayyor_taxi_full, telegram_id FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_pochta_haydovchi(self):
        sql = "SELECT tayyor_pochta_mashina_full, telegram_id FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_yuk_avto_orders(self):
        sql = "SELECT tayyor_yuk_haydovchisi_full, telegram_id FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_sayohatchi_mashina(self):
        sql = "SELECT tayyor_sayohatchi_full_mashina, telegram_id FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_taxi(self):
        sql = "SELECT region,tayyor_taxi,tayyor_taxi_full,viloyatga,tumanga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_sayohatchi(self):
        sql = "SELECT region,tayyor_sayohatchi,tayyor_sayohatchi_full,viloyatga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_sayohatchi_mashina(self):
        sql = "SELECT region,tayyor_sayohatchi_mashina,tayyor_sayohatchi_full_mashina,viloyatga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_pochta_mashina(self):
        sql = "SELECT region,tayyor_pochta_mashina,tayyor_pochta_mashina_full,viloyatga,tumanga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_pochta(self):
            sql = "SELECT region,tayyor_pochta,tayyor_pochta_full,viloyatga,tumanga FROM Orders"
            return await self.execute(sql, fetch=True)
    async def select_tayyor_yuk(self):
        sql = "SELECT region,tayyor_yuk,tayyor_yuk_full,viloyatga,tumanga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_yolovchi(self):
        sql = "SELECT region,tayyor_yolovchi,tayyor_yolovchi_full,viloyatga,tumanga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_yuk_haydovchi(self):
        sql = "SELECT region,tayyor_yuk_haydovchisi,tayyor_yuk_haydovchisi_full,viloyatga,tumanga FROM Orders"
        return await self.execute(sql, fetch=True)
    async def select_order(self, **kwargs):
        sql = "SELECT * FROM Orders WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def count_orders(self):
        sql = "SELECT COUNT(*) FROM Orders"
        return await self.execute(sql, fetchval=True)
    async def update_user_tayyor_taxi(self, tayyor_taxi, telegram_id):
        sql = "UPDATE Users SET tayyor_taxi=$1 WHERE telegram_id=$2"
        return await self.execute(sql, tayyor_taxi, telegram_id, execute=True)
    async def update_user_region(self,region,telegram_id):
        sql = "UPDATE Users SET region=$1 WHERE telegram_id=$2"
        return await self.execute(sql, region, telegram_id, execute=True)

    async def drop_orders(self):
        await self.execute("DROP TABLE Orders", execute=True)




    async def create_table_driver(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Driver (
           id SERIAL PRIMARY KEY,
           tashiman_odam TEXT NULL,
           tashiman_yuk TEXT NULL,
           tashiman_pochta TEXT NULL,
           telegram_id BIGINT NULL
          );
           """
        await self.execute(sql, execute=True)

    async def add_driver(self, tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id):
        sql = "INSERT INTO driver (tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id, fetchrow=True)

    async def select_all_driver(self):
        sql = "SELECT * FROM Driver"
        return await self.execute(sql, fetch=True)

    async def delete_driver(self, **kwargs):
        sql = "DELETE FROM Driver WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def drop_driver(self):
        await self.execute("DROP TABLE Driver", execute=True)
    async def create_table_driver_info(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Info (
           id SERIAL PRIMARY KEY,
           viloyat TEXT NULL,
           tuman TEXT NULL,
           telegram_id BIGINT NULL
          );
           """
        await self.execute(sql, execute=True)

    async def add_driver_info(self, viloyat, tuman, telegram_id):
        sql = "INSERT INTO info (viloyat, tuman, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, viloyat, tuman, telegram_id, fetchrow=True)

    async def select_all_driver_info(self):
        sql = "SELECT * FROM Info"
        return await self.execute(sql, fetch=True)
    async def drop_driver_info(self):
        await self.execute("DROP TABLE Info", execute=True)

    async def delete_driver_info(self, **kwargs):
        sql = "DELETE FROM Info WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
