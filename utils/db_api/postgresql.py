import asyncio
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

import loader
from data import config



DATABASE_URL = "postgresql://oojgyaho:m7or8A]:C59rTL@mi3-ss111.a2hosting.com:5432/oojgyaho_taxibot"

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
        telegram_id BIGINT NULL UNIQUE,
        last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        yolovchi BOOLEAN NOT NULL DEFAULT FALSE,
        haydovchi BOOLEAN NOT NULL DEFAULT FALSE,
        balans BIGINT NULL
        
       );
        """
        await self.execute(sql, execute=True)

    async def create_table_admins(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Admins (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NULL UNIQUE
       );
        """
        await self.execute(sql, execute=True)
    async def add_admin(self,telegram_id):
        sql = "INSERT INTO admins (telegram_id) VALUES($1) returning *"
        return await self.execute(sql,  telegram_id, fetchrow=True)
    async def delete_admin(self, **kwargs):
        sql = "DELETE FROM Admins WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_admin(self, **kwargs):
        sql = "SELECT * FROM Admins WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_all_admins(self):
        sql = "SELECT * FROM Admins"
        return await self.execute(sql, fetch=True)
    async def drop_admins(self):
        await self.execute("DROP TABLE Admins", execute=True)

    async def get_users_joined_in_last_day(self):
        sql = """
        SELECT * FROM Users
        WHERE last_interaction >= NOW() - INTERVAL '1 day';
        """
        return await self.execute(sql,fetch=True)

    async def yolovchi_set(self,yolovchi,telegram_id):
        sql = """
           UPDATE Users SET yolovchi=$1 WHERE telegram_id=$2
           """
        return await self.execute(sql, yolovchi, telegram_id, execute=True)
    async def haydovchi_set(self,haydovchi,telegram_id):
        sql = """
           UPDATE Users SET haydovchi=$1 WHERE telegram_id=$2
           """
        return await self.execute(sql, haydovchi, telegram_id, execute=True)

    async def update_balans(self, balans, telegram_id):
        sql = "UPDATE Users SET balans=$1 WHERE telegram_id=$2"
        return await self.execute(sql, balans, telegram_id, execute=True)


    async def create_table_orders(self):
        sql = """
        CREATE TABLE Orders (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NULL,
        tayyor_taxi TEXT NULL,
        tayyor_taxi_full TEXT NULL,
        viloyat TEXT NULL,
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
        tayyor_sayohatchi_full_mashina TEXT NULL,
        last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP ,
        kelishilmoqda BOOLEAN NOT NULL DEFAULT FALSE,
        kelishildi BOOLEAN NOT NULL DEFAULT FALSE,
        rad_etildi BOOLEAN NOT NULL DEFAULT FALSE,
        bormaydi BOOLEAN NOT NULL DEFAULT FALSE,
        aniq_bormaydi BOOLEAN NOT NULL DEFAULT FALSE,
        event_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        bormaydi2 BOOLEAN NOT NULL DEFAULT FALSE,
        kim_tomonidan_qabul_qilindi TEXT NULL,
        sana TEXT NULL,
        phone TEXT
        
        );
        """
        await self.execute(sql, execute=True)

    async def add_order_tayyor_taxi(self,
                                    tayyor_taxi,
                                    tayyor_taxi_full,
                                    viloyat,
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
                                    event_time,
                                    kim_tomonidan_qabul_qilindi,
                                    sana,phone):
        sql = "INSERT INTO orders (" \
              "tayyor_taxi," \
              "tayyor_taxi_full, " \
              "viloyat, " \
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
              "tayyor_sayohatchi_full_mashina," \
              "event_time," \
              "kim_tomonidan_qabul_qilindi,"\
              "sana,phone"\
              ") VALUES(" \
              "$1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12 , $13, $14, $15, $16, $17, $18, $19, $20, $21,$22,$23,$24,$25" \
              ") " \
              "returning *"
        return await self.execute(
            sql, tayyor_taxi,
            tayyor_taxi_full,
            viloyat,
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
            event_time,
            kim_tomonidan_qabul_qilindi,
            sana,phone,
            fetchrow=True
        )

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def get_orders_joined_in_last_day(self):
        sql = """
         SELECT * FROM Orders
         WHERE last_interaction >= NOW() - INTERVAL '1 day';
         """
        return await self.execute(sql, fetch=True)
    async def add_user(self, full_name, username, telegram_id,balans):
        sql = "INSERT INTO users (full_name, username, telegram_id,balans) VALUES($1, $2, $3,$4) returning *"
        return await self.execute(sql, full_name, username, telegram_id,balans, fetchrow=True)
    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_orders(self, **kwargs):
        sql = "SELECT * FROM Orders WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def delete_orders(self, **kwargs):
        sql = "DELETE FROM Orders WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    async def select_all_orders(self):
        sql = "SELECT * FROM Orders"
        return await self.execute(sql, fetch=True)
    async def update_orders_qabul_qilish(self, kim_tomonidan_qabul_qilindi, id):
        sql = "UPDATE Orders SET kim_tomonidan_qabul_qilindi=$1 WHERE id=$2"
        return await self.execute(sql, kim_tomonidan_qabul_qilindi, id, execute=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)
    async def delete_users(self,telegram_id):
        query = "DELETE FROM Users WHERE telegram_id = $1"
        await self.execute(query, telegram_id, execute=True)
    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)


    async def count_orders(self):
        sql = "SELECT COUNT(*) FROM Orders"
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
        sql = "SELECT region,tayyor_sayohatchi_mashina, tayyor_sayohatchi_full_mashina, viloyatga,tumanga,viloyat,id,kelishildi,rad_etildi,event_time FROM Orders "
        return await self.execute(sql, fetch=True)
    async def select_tayyor_taxi(self):
        sql = "SELECT region,tayyor_taxi,tayyor_taxi_full,viloyatga,tumanga,viloyat,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_sayohatchi(self):
        sql = "SELECT region,tayyor_sayohatchi,tayyor_sayohatchi_full,viloyatga,tumanga,viloyat ,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_sayohatchi_mashina(self):
        sql = "SELECT region,tayyor_sayohatchi_mashina,tayyor_sayohatchi_full_mashina,viloyatga,tumanga,viloyat,id,kelishildi,rad_etildi,event_time  FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_pochta_mashina(self):
        sql = "SELECT region,tayyor_pochta_mashina,tayyor_pochta_mashina_full,viloyatga,tumanga,viloyat ,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_pochta(self):
            sql = "SELECT region,tayyor_pochta,tayyor_pochta_full,viloyatga,tumanga,viloyat ,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
            return await self.execute(sql, fetch=True)
    async def select_tayyor_yuk(self):
        sql = "SELECT region,tayyor_yuk,tayyor_yuk_full,viloyatga,tumanga,viloyat ,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_yolovchi(self):
        sql = "SELECT region,tayyor_yolovchi,tayyor_yolovchi_full,viloyatga,tumanga,viloyat ,id,kelishildi,rad_etildi,event_time FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_tayyor_yuk_haydovchi(self):
        sql = "SELECT region,tayyor_yuk_haydovchisi,tayyor_yuk_haydovchisi_full,viloyatga,tumanga,viloyat,id,kelishildi,rad_etildi,event_time,telegram_id  FROM Orders WHERE aniq_bormaydi=False"
        return await self.execute(sql, fetch=True)
    async def select_order(self, **kwargs):
        sql = "SELECT * FROM Orders WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)



    async def count_orders(self):
        sql = "SELECT COUNT(*) FROM Orders"
        return await self.execute(sql, fetchval=True)

    async def deactivate_orders(self,rad_etildi,id):
        sql = """
           UPDATE Orders SET rad_etildi=$1 WHERE id=$2
           """
        return await self.execute(sql, rad_etildi, id, execute=True)
    async def kelishildi_orders(self,kelishildi,id):
        sql = """
           UPDATE Orders SET kelishildi=$1 WHERE id=$2
           """
        return await self.execute(sql, kelishildi, id, execute=True)
    async def kelishilmoqda_orders(self,kelishilmoqda,id):
        sql = """
           UPDATE Orders SET kelishilmoqda=$1 WHERE id=$2
           """
        return await self.execute(sql, kelishilmoqda, id, execute=True)

    async def bormaydi_update(self,bormaydi,id):
        sql = """
           UPDATE Orders SET bormaydi=$1 WHERE id=$2
           """
        return await self.execute(sql, bormaydi, id, execute=True)
    async def bormaydi2_update(self,bormaydi2,id):
        sql = """
           UPDATE Orders SET bormaydi2=$1 WHERE id=$2
           """
        return await self.execute(sql, bormaydi2, id, execute=True)
    async def aniq_bormaydi_update(self,aniq_bormaydi,id):
        sql = """
           UPDATE Orders SET aniq_bormaydi=$1 WHERE id=$2
           """
        return await self.execute(sql, aniq_bormaydi, id, execute=True)

    async def update_user_tayyor_taxi(self, tayyor_taxi, telegram_id):
        sql = "UPDATE Users SET tayyor_taxi=$1 WHERE telegram_id=$2"
        return await self.execute(sql, tayyor_taxi, telegram_id, execute=True)
    async def update_user_region(self,region,telegram_id):
        sql = "UPDATE Users SET region=$1 WHERE telegram_id=$2"
        return await self.execute(sql, region, telegram_id, execute=True)
    async def update_tayyor_yolovchi(self,tayyor_yolovchi_full,id):
        sql = "UPDATE Orders SET tayyor_yolovchi_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_yolovchi_full, id, execute=True)
    async def update_tayyor_taxi(self,tayyor_taxi_full,id):
        sql = "UPDATE Orders SET tayyor_taxi_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_taxi_full, id, execute=True)
    async def update_tayyor_pochta(self,tayyor_pochta_full,id):
        sql = "UPDATE Orders SET tayyor_pochta_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_pochta_full, id, execute=True)
    async def update_tayyor_pochta_mashina(self,tayyor_pochta_mashina_full,id):
        sql = "UPDATE Orders SET tayyor_pochta_mashina_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_pochta_mashina_full, id, execute=True)
    async def update_tayyor_yuk(self,tayyor_yuk_full,id):
        sql = "UPDATE Orders SET tayyor_yuk_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_yuk_full, id, execute=True)
    async def update_tayyor_yuk_mashinasi(self,tayyor_yuk_haydovchisi_full,id):
        sql = "UPDATE Orders SET tayyor_yuk_haydovchisi_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_yuk_haydovchisi_full, id, execute=True)
    async def update_tayyor_sayohatchi(self,tayyor_sayohatchi_full,id):
        sql = "UPDATE Orders SET tayyor_sayohatchi_full=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_sayohatchi_full, id, execute=True)
    async def update_tayyor_sayohatchi_mashina(self,tayyor_sayohatchi_full_mashina,id):
        sql = "UPDATE Orders SET tayyor_sayohatchi_full_mashina=$1 WHERE id=$2"
        return await self.execute(sql, tayyor_sayohatchi_full_mashina, id, execute=True)
    async def drop_orders(self):
        await self.execute("DROP TABLE Orders", execute=True)




    async def create_table_driver(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Driver (
           id SERIAL PRIMARY KEY,
           tashiman_odam TEXT NULL,
           tashiman_yuk TEXT NULL,
           tashiman_pochta TEXT NULL,
           telegram_id BIGINT NULL,
           sayohatchi_tashiman TEXT NULL,
           last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
           
          );
           """
        await self.execute(sql, execute=True)
    async def get_drivers_joined_in_last_day(self):
        sql = """
         SELECT * FROM Driver
         WHERE last_interaction >= NOW() - INTERVAL '1 day';
         """
        return await self.execute(sql, fetch=True)
    async def select_driver(self, **kwargs):
        sql = "SELECT * FROM Driver WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def add_driver(self, tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id,sayohatchi_tashiman):
        sql = "INSERT INTO driver (tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id,sayohatchi_tashiman) VALUES($1, $2, $3, $4,$5) returning *"
        return await self.execute(sql, tashiman_odam, tashiman_yuk,tashiman_pochta, telegram_id,sayohatchi_tashiman, fetchrow=True)

    async def select_all_driver(self):
        sql = "SELECT * FROM Driver"
        return await self.execute(sql, fetch=True)

    async def delete_driver(self, **kwargs):
        sql = "DELETE FROM Driver WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def drop_driver(self):
            await self.execute("DROP TABLE Driver", execute=True)

    async def select_all_drivers(self, limit,offset):
        sql = f"SELECT * FROM Driver LIMIT {limit} OFFSET {offset}"
        return await self.execute(sql, fetch=True)




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


    async def create_sayohat_info(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Travel (
           id SERIAL PRIMARY KEY,
           viloyat TEXT NULL,
           telegram_id BIGINT NULL
          );
           """
        await self.execute(sql, execute=True)

    async def add_sayohat_info(self, viloyat,telegram_id):
        sql = "INSERT INTO Travel (viloyat,telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, viloyat, telegram_id, fetchrow=True)
    async def select_all_sayohat_info(self):
        sql = "SELECT * FROM Travel"
        return await self.execute(sql, fetch=True)
    async def delete_sayohat_info(self, **kwargs):
        sql = "DELETE FROM Travel WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def drop_sayohat_info(self):
        await self.execute("DROP TABLE Travel", execute=True)


    async def create_yoldan_odam(self):
        sql = """
           CREATE TABLE IF NOT EXISTS Yoldan (
           id SERIAL PRIMARY KEY,
           tuman TEXT NULL,
           telegram_id BIGINT NULL
          );
           """
        await self.execute(sql, execute=True)

    async def add_yoldan_odam(self,tuman,telegram_id):
        sql = "INSERT INTO Yoldan (tuman,telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, tuman, telegram_id, fetchrow=True)
    async def select_all_yoldan_odam(self):
        sql = "SELECT * FROM Yoldan"
        return await self.execute(sql, fetch=True)
    async def delete_yoldan_odam(self, **kwargs):
        sql = "DELETE FROM Yoldan WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def drop_yoldan_odam_info(self):
        await self.execute("DROP TABLE Yoldan", execute=True)

    async def create_qoshimcha_tumanlar(self):
        sql = """
              CREATE TABLE IF NOT EXISTS Tumanlar (
              id SERIAL PRIMARY KEY,
              tuman TEXT NULL,
              telegram_id BIGINT NULL
             );
              """
        await self.execute(sql, execute=True)

    async def add_qoshimcha_tumanlar(self, tuman, telegram_id):
        sql = "INSERT INTO Tumanlar (tuman,telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, tuman, telegram_id, fetchrow=True)

    async def select_all_qoshimcha_tumanlar(self):
        sql = "SELECT * FROM Tumanlar"
        return await self.execute(sql, fetch=True)

    async def delete_qoshimcha_tumanlar(self, **kwargs):
        sql = "DELETE FROM Tumanlar WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def drop_qoshimcha_tumanlar(self):
        await self.execute("DROP TABLE Tumanlar", execute=True)

    async def create_table_yolovchi(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Yolovchi (
        id SERIAL PRIMARY KEY,
        username varchar(255) NULL,
        telegram_id BIGINT NULL,
        last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        
       );
        """
        await self.execute(sql, execute=True)

    async def get_yolovchi_joined_in_last_day(self):
        sql = """
            SELECT * FROM Yolovchi
            WHERE last_interaction >= NOW() - INTERVAL '1 day';
            """
        return await self.execute(sql, fetch=True)

    async def add_yolovchi(self,username,telegram_id):
        sql = "INSERT INTO Yolovchi (username,telegram_id) VALUES($1, $2) returning *"
        return await self.execute(sql, username, telegram_id, fetchrow=True)
    async def select_all_yolovchi(self):
        sql = "SELECT * FROM Yolovchi"
        return await self.execute(sql, fetch=True)
    async def delete_yolovchi(self,telegram_id):
        query = "DELETE FROM Yolovchi WHERE telegram_id = $1"
        await self.execute(query, telegram_id, execute=True)
    async def select_yolovchi(self, **kwargs):
        sql = "SELECT * FROM Yolovchi WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def count_yolovchi(self):
        sql = "SELECT COUNT(*) FROM Yolovchi"
        return await self.execute(sql, fetchval=True)
    async def drop_yolovchi(self):
        await self.execute("DROP TABLE Yolovchi", execute=True)

    async def create_table_haydovchi(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Haydovchi (
        id SERIAL PRIMARY KEY,
        username varchar(255) NULL,
        telegram_id BIGINT NULL,
        balans BIGINT NULL
       );
        """
        await self.execute(sql, execute=True)

    async def add_haydovchi(self, username, telegram_id,balans):
        sql = "INSERT INTO Haydovchi (username,telegram_id,balans) VALUES($1, $2,$3) returning *"
        return await self.execute(sql, username, telegram_id,balans, fetchrow=True)


    async def select_haydovchi(self, **kwargs):
        sql = "SELECT * FROM Haydovchi WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def select_all_haydovchi(self):
        sql = "SELECT * FROM Haydovchi"
        return await self.execute(sql, fetch=True)

    async def delete_haydovchi(self, telegram_id):
        query = "DELETE FROM Haydovchi WHERE telegram_id = $1"
        await self.execute(query, telegram_id, execute=True)
    async def count_haydovchi(self):
        sql = "SELECT COUNT(*) FROM Haydovchi"
        return await self.execute(sql, fetchval=True)
    async def drop_haydovchi(self):
        await self.execute("DROP TABLE Haydovchi", execute=True)


    async def create_table_count_last_get_orders(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Last (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NULL ,
        last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
       );
        """
        await self.execute(sql, execute=True)

    async def add_last(self, telegram_id):
        sql = "INSERT INTO Last  (telegram_id) VALUES($1) returning *"
        return await self.execute(sql,  telegram_id, fetchrow=True)

    async def get_order_joined_in_last_day(self):
        sql = """
          SELECT * FROM Last
          WHERE last_interaction >= NOW() - INTERVAL '1 day';
          """
        return await self.execute(sql, fetch=True)
    async def get_order_joined_in_last_day_2(self):
        sql = """
          SELECT * FROM Orders
          WHERE last_interaction >= NOW() - INTERVAL '1 day';
          """
        return await self.execute(sql, fetch=True)
    async def delete_last_order(self,**kwargs):
        sql = "DELETE FROM Last WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)


    async def drop_last_order(self):
        await self.execute("DROP TABLE Last", execute=True)


    async def create_table_tarif(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Tarif (
        id SERIAL PRIMARY KEY,
        tarif_name VARCHAR(255) NOT NULL,
        tarif_narxi BIGINT NULL ,
        tarif_kuni BIGINT NULL ,
        last_interaction TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
       );
        """
        await self.execute(sql, execute=True)
    async def add_tarif(self, tarif_name, tarif_narxi, tarif_kuni):
        sql = "INSERT INTO Tarif (tarif_name, tarif_narxi, tarif_kuni) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, tarif_name, tarif_narxi, tarif_kuni, fetchrow=True)
    async def select_tarif(self, **kwargs):
        sql = "SELECT * FROM Tarif WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    async def drop_last_tarif(self):
        await self.execute("DROP TABLE Tarif", execute=True)

    async def update_tarif_pay(self, tarif_narxi, tarif_name):
        sql = "UPDATE Tarif SET tarif_narxi=$1 WHERE tarif_name=$2"
        return await self.execute(sql, tarif_narxi, tarif_name, execute=True)

    async def update_tarif_day(self, tarif_kuni, tarif_name):
        sql = "UPDATE Tarif SET tarif_kuni=$1 WHERE tarif_name=$2"
        return await self.execute(sql, tarif_kuni, tarif_name, execute=True)