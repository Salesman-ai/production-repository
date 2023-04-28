import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import sys
sys.path.append('../')
from logger.log import log
import time

config_path = Path(os.path.abspath(__file__)).parent / '../config.cfg'
load_dotenv(dotenv_path=config_path)

def generate_connection(database_name=os.environ.get("POSTGRES_DB")):
    time.sleep(15)
    try:
        conn = psycopg2.connect(f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASS')}@{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}")
        return conn
    except Exception as error:
        log.database.error(f"Not connected to the database. Cause: {error}")
        return error