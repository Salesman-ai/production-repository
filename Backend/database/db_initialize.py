from database.db_conn import generate_connection
from database.db_query import check_connection

import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import sys
sys.path.append('../')
from logger.log import log

config_path = Path(os.path.abspath(__file__)).parent / '../config.cfg'
load_dotenv(dotenv_path=config_path)


def is_database_exist():
    table_create()
    if "not exist" in str(generate_connection()):
        log.database.warning(f"{ str(os.environ.get('POSTGRES_DB')) } not exist. Database will be created.")
        database_initialization()
    elif check_connection() is True:
        log.database.info(f"Table: { str(os.environ.get('POSTGRES_DB')) } exist. Skipping...")

def database_initialization():

    sql_init = f"""
                CREATE DATABASE {os.environ.get('POSTGRES_DB')}
                WITH
                OWNER = {os.environ.get('POSTGRES_USER')}
                ENCODING = 'UTF8'
                LC_COLLATE = 'en_US.utf8'
                LC_CTYPE = 'en_US.utf8'
                TABLESPACE = pg_default
                CONNECTION LIMIT = -1
                IS_TEMPLATE = False;"""

    
    conn = None
    try:
        conn =  generate_connection("salesman")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql_init)
        log.database.info(f"database { str(os.environ.get('POSTGRES_DB')) } created.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(f"Database was not created correctly. Error - {error}")
    finally:
        if conn is not None:
            conn.close()

def table_create():
    sql_create = f"""
                CREATE TABLE IF NOT EXISTS public.{os.environ.get('POSTGRES_TABLE')}
                (
                    id SERIAL NOT NULL,
                    brandName text COLLATE pg_catalog."default",
                    modelName text COLLATE pg_catalog."default",
                    bodyType text COLLATE pg_catalog."default",
                    fuelType text COLLATE pg_catalog."default",
                    transmission text COLLATE pg_catalog."default",
                    power numeric,
                    mileage numeric,
                    year numeric,
                    engineDisplacement numeric,
                    price numeric,
                    CONSTRAINT results_pkey PRIMARY KEY (id)
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.results
                    OWNER to salesman;"""
    conn = None
    try:
        conn =  generate_connection("salesman")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql_create)
        log.database.info(f"table 'name' created.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(f"Database was not created correctly. Error - {error}")
    finally:
        if conn is not None:
            conn.close()