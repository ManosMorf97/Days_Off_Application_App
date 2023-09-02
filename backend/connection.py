import mysql.connector
import mysql.connector.errorcode

def connect():
    db=mysql.connector.connect(user='manos',password='x#9kQL4X',database='company',host="localhost",port=31001)
    cursor=db.cursor(buffered=True)
    return db,cursor

def disconnect(db,cursor):
    cursor.close()
    db.close()

