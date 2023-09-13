import mysql.connector
import mysql.connector.errorcode
from secretP import *

def connect():
    try_con=True
    while try_con:
        try:
            try_con=False
            db=mysql.connector.connect(user='manos',password=mysql_pwd,database='company',host="10.152.183.121",port=3306)
        except mysql.connector.Error as err:
            try_con=True

    cursor=db.cursor(buffered=True)
    return db,cursor

def disconnect(db,cursor):
    cursor.close()
    db.close()


