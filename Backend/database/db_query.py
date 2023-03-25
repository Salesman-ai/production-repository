from database.db_conn import generate_connection
import psycopg2
import sys
sys.path.append('../')
from logger.log import log

def check_connection():
    conn = None
    try:
        conn =  generate_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        log.database.info(f"Valid connection")
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(error)
    finally:
        if conn is not None:
            conn.close()

def insert_price(id, ip, car_name, car_type, car_price):
    sql = """INSERT INTO results (id, user_ip, car_name, car_type, car_price) VALUES (%s, %s, %s, %s, %s)"""
    conn = None
    try:
        conn =  generate_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id, str(ip), str(car_name), str(car_type), car_price,))
        conn.commit()
        cursor.close()
        log.database.info(f"Data inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(error)
    finally:
        if conn is not None:
            conn.close()