from os import getenv
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from utils.text import err_msg
from config import validate
from utils.date_and_time import format_datetime_to_pt_br_standard

load_dotenv()
HOST_DB=getenv('HOST_DB')
DATABASE=getenv('DATABASE')
USER_DB=getenv('USER_DB')
PASSWD_DB=getenv('PASSWD_DB')


def fetch_net_records(
        host=HOST_DB,
        database=DATABASE,
        user=USER_DB,
        password=PASSWD_DB
    ) -> list:
    validate()
    try:
        conn = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            query = """
            select
                uuid,
                name,
                (select type from `net_device_type` where id = device_id) as device,
                (select name from `net_operating_system` where id = os_id) as os,
                mac_address,
                created_at,
                updated_at
            from
                `net_records`;
            """
            
            cursor.execute(query)
            
            records = cursor.fetchall()
            for record in records:
                record['created_at'] = format_datetime_to_pt_br_standard(
                    record['created_at']
                )
                record['updated_at'] = format_datetime_to_pt_br_standard(
                    record['updated_at']
                )
            
            return records
    except Error as err:
        print(err_msg(f'Error while connecting to database: \n{err}'))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

