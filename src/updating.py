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


def get_database_connection(
        host=HOST_DB,
        database=DATABASE,
        user=USER_DB,
        password=PASSWD_DB
    ):
    validate()
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    except Error as err:
        print(err_msg('An error has occured. ' + repr(err)))
    return connection


def testing_func():
    try:
        conn = get_database_connection()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            query = """select * from `net_records`;"""
            cursor.execute(query)
            print(cursor.fetchall())
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
