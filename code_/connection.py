import mysql.connector
import mysql.connector.errorcode
from secret import *

def connect():
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor(buffered=True)
    return db,cursor

def disconnect(db,cursor):
    cursor.close()
    db.close()

