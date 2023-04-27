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
        log.database.info(f"Valid connection")
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(error)
    finally:
        if conn is not None:
            conn.close()
            return True
        else:
            return False

def insert_price(brand_name: str, 
                 model_name: str, 
                 body_type: str, 
                 fuel_type: str, 
                 transmission: str, 
                 power: float, 
                 mileage: int, 
                 year: int, 
                 engine_displacement: float, 
                 price: float):
    sql = """INSERT INTO results 
            (brandName, modelName, bodyType, fuelType, transmission, power, mileage, year, engineDisplacement, price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    conn = None
    try:
        conn =  generate_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (brand_name,
                            model_name, 
                            body_type, 
                            fuel_type, 
                            transmission, 
                            power, 
                            mileage, 
                            year, 
                            engine_displacement, 
                            price))
        conn.commit()
        cursor.close()
        log.database.info(f"Data inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        log.database.error(error)
    finally:
        if conn is not None:
            conn.close()