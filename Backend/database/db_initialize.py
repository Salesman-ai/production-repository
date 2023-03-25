from database.db_conn import generate_connection
from database.db_query import check_connection

import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import sys
sys.path.append('../')
from logger.log import log

config_path = Path('../config.cfg')
load_dotenv(dotenv_path=config_path)


def is_database_exist():
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
    
    sql_create = f"""
                    CREATE TABLE IF NOT EXISTS public.{os.environ.get('POSTGRES_TABLE')}
                    (
                        id SERIAL NOT NULL,
                        user_ip text COLLATE pg_catalog."default",
                        car_name text COLLATE pg_catalog."default",
                        car_type text COLLATE pg_catalog."default",
                        car_price numeric,
                        CONSTRAINT results_pkey PRIMARY KEY (id)
                    )

                    TABLESPACE pg_default;

                    ALTER TABLE IF EXISTS public.results
                        OWNER to {os.environ.get('POSTGRES_USER')};"""
    
    conn = None
    try:
        conn =  generate_connection("salesman")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql_init)
        log.database.info(f"database { str(os.environ.get('POSTGRES_DB')) } created.")
        cursor.execute(sql_create)
        log.database.info(f"table 'name' created.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(f"Database was not created correctly. Error - {error}")
    finally:
        if conn is not None:
            conn.close()
