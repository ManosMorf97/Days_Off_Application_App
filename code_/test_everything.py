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

def test_max_requests(insert_users):
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","NormalDaysOff",20)
    assert "Your request has been sent"==create_request("billb97@gmail.com","NormalDaysOff",20)
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","NormalDaysOff",5)
    assert "Your request has been sent"==create_request("billb97@gmail.com","NormalDaysOff",5)
    assert "You cannot take too many days off.For NormalDaysOff check days off "==create_request("manosmorf97@gmail.com","NormalDaysOff",5)
    assert "You cannot take too many days off.For NormalDaysOff check days off "==create_request("billb97@gmail.com","NormalDaysOff",5)
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","ParentialDaysOff",50)
    assert "Your request has been sent"==create_request("billb97@gmail.com","ParentialDaysOff",50)


