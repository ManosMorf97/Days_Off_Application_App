import mysql.connector
import mysql.connector.errorcode
from  secretP import *

def connect():
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='company',host="10.152.183.121",port=3306)
    cursor=db.cursor(buffered=True)
    return db,cursor

def disconnect(db,cursor):
    cursor.close()
    db.close()

