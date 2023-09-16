from connection import *
import time

def insert_new_user(email,firstname,lastname):
    db,cursor=connect()
    sql_statement="Insert into Employee values(%s,%s,%s,25,25,120)"
    details=(email,firstname,lastname)
    cursor.execute(sql_statement,details)
    db.commit()
    disconnect(db,cursor)
    return "New Employee "

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