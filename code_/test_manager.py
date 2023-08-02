#import sys
#sys.path.insert(0,"../code_")
import pytest
from connection import *
from employee import *
from manager import *
#sys.path.insert(0,"pwd/../code_")


@pytest.fixture
def insert_users():
    db,cursor=connect()
    cursor.execute("Delete from Employee")
    db.commit()
    cursor.execute("Delete from Request")
    db.commit()
    cursor.execute("Delete from Decision")
    db.commit()
    cursor.execute("Insert into  Employee values ('manosmorf97@gmail.com','Manos','Morfiadakis',25,50,90)")
    db.commit()
    cursor.execute("Insert into  Employee values ('johnd97@gmail.com','John','Doe',25,50,90)")
    db.commit()
    cursor.execute("Insert into  Employee values ('billb97@gmail.com','Bill','Bor',25,50,90)")
    db.commit()
    disconnect(db,cursor)

def test_see_Requests():
    db,cursor=connect()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,accepted) values('manosmorf97@gmail.com','NormalDaysOff',7,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,accepted) values('billb@gmail.com','DiseaseDaysOff',8,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,accepted) values('manosmorf97@gmail.com','NormalDaysOff',7,'Accepted') ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,accepted) values('billb@gmail.com','DiseaseDaysOff',8,'Rejected') ")
    db.commit()
    Requests=see_Requests()
    assert len(Requests)==2
    assert len(Requests[0])==len(Requests[1])
    assert len(Requests[0])==5

