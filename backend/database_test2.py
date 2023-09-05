from connection import *

def delete1():
    db,cursor=connect()
    cursor.execute("DROP TABLE IF EXISTS Request")
    db.commit()
    cursor.execute("DROP TABLE IF EXISTS Decision")
    db.commit()
    cursor.execute("DROP TABLE IF EXISTS Employee")
    db.commit()
    disconnect(db,cursor)

def statement():
    delete1()
    db,cursor=connect()
    cursor.execute("create table Employee(email varchar(30) not null,Name varchar(20) not null,Surname varchar(20) not null,NormalDaysOff int not null,ParentialDaysOff int not null,DiseaseDaysOff int not null,primary key(email))ENGINE=InnoDB;")
    db.commit()
    cursor.execute("insert into  Employee values ('johnd97@gmail.com','John','Doe',25,50,90)")
    db.commit()
    disconnect(db,cursor)

#statement()
db,cursor=connect()
cursor.execute("show tables")
print(cursor.fetchall())
db.commit()
disconnect(db,cursor)

