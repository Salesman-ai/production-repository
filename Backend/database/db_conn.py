import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import sys
sys.path.append('../')
from logger.log import log

config_path = Path('../config.cfg')
load_dotenv(dotenv_path=config_path)

def generate_connection(database_name=os.environ.get("POSTGRES_DB")):
    try:
        conn = psycopg2.connect(
            dbname=database_name,
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASS"),
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT")
        )
        return conn
    except Exception as error:
        log.database.error(f"Not connected to the database. Cause: {error}")
        return error