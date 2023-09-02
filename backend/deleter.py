from connection import *

def delete_():
    db,cursor=connect()
    cursor.execute("drop table Request")
    db.commit()
    cursor.execute("drop table Decision")
    db.commit()
    cursor.execute("drop table Employee")
    db.commit()
    disconnect(db,cursor)

#delete_()

db,cursor=connect()
cursor.execute("show tables")
print(cursor.fetchall())
disconnect(db,cursor)