import mysql.connector
import mysql.connector.errorcode

def connect():
    db=mysql.connector.connect(user='manos',password='x#9kQL4X',database='company',host="localhost",port=31001)
    cursor=db.cursor(buffered=True)
    return db,cursor

def disconnect(db,cursor):
    cursor.close()
    db.close()


db,cursor=connect()
sql_statement=("create table IF NOT EXISTS Employee(email varchar(30) not null"
    ",Name varchar(20) not null,Surname varchar(20) not null"
    ",NormalDaysOff int not null,ParentialDaysOff int not null"
    ",DiseaseDaysOff int not null,primary key(email))ENGINE=InnoDB;")
cursor.execute(sql_statement)
db.commit()

cursor.execute("Insert into  Employee values ('manosmorf97@gmail.com','Manos','Morfiadakis',25,50,90)")
db.commit()

cursor.execute("select name from Employee where email='manosmorf97@gmail.com'")
result=cursor.fetchall()
db.commit()

print(result[0][0])

cursor.execute("Delete from Employee")
db.commit()

disconnect(db,cursor)