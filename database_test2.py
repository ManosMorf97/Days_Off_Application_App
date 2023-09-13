from connection import *
import time

def clean():
    db,cursor=connect()
    cursor.execute("DROP TABLE IF EXISTS Request")
    db.commit()
    time.sleep(1)
    cursor.execute("DROP TABLE IF EXISTS Decision")
    db.commit()
    time.sleep(1)
    cursor.execute("DROP TABLE IF EXISTS Employee")
    db.commit()
    time.sleep(1)
    disconnect(db,cursor)

def delete1():
    db,cursor=connect()
    cursor.execute("delete from Employee")
    db.commit()
    disconnect(db,cursor)

def activate_tables():
    
    db,cursor=connect()
    sql_statement=("create table IF NOT EXISTS Request (RequestId int not null auto_increment"
    ",email varchar(30) not null,category varchar(20) not null,RequestedDaysOff int not null"
    ",approval varchar(15),primary key(RequestId),constraint CHECK_CATEGORY check "
    "(category  in  ('NormalDaysOff','ParentialDaysOff','DiseaseDaysOff')))ENGINE=InnoDB;")
    cursor.execute(sql_statement)
    db.commit()
    time.sleep(1)
    sql_statement=("create table IF NOT EXISTS Decision (DecisionId int not null auto_increment"
    ",description varchar(200) not null,viewed varchar(4) not null,reciever varchar(30) not null"
    ",primary key(DecisionId))ENGINE=InnoDB;")
    cursor.execute(sql_statement)
    db.commit()
    time.sleep(1)
    sql_statement=("create table IF NOT EXISTS Employee(email varchar(30) not null"
    ",Name varchar(20) not null,Surname varchar(20) not null"
    ",NormalDaysOff int not null,ParentialDaysOff int not null"
    ",DiseaseDaysOff int not null,primary key(email))ENGINE=InnoDB;")
    cursor.execute(sql_statement)
    db.commit()

    disconnect(db,cursor)
    
    return "tables are created"

#activate_tables()

delete1()
db,cursor=connect()
cursor.execute("select * from Employee")
print(cursor.fetchall())
db.commit()
disconnect(db,cursor)

