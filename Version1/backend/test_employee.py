#import sys
#sys.path.insert(0,"../code_")
import pytest
from .connection import *
from .employee import *
from .manager import *
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

def test_max_request_with_rejections(insert_users):
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","NormalDaysOff",20)
    assert "Your request has been sent"==create_request("billb97@gmail.com","NormalDaysOff",20)
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","NormalDaysOff",5)
    assert "Your request has been sent"==create_request("billb97@gmail.com","NormalDaysOff",5)
    db,cursor=connect()
    cursor.execute("Update Request set approval='Rejected' where email='manosmorf97@gmail.com' and RequestedDaysOff=5")
    db.commit()
    disconnect(db,cursor)
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","NormalDaysOff",5)
    assert "You cannot take too many days off.For NormalDaysOff check days off "==create_request("billb97@gmail.com","NormalDaysOff",5)
    assert "Your request has been sent"==create_request("manosmorf97@gmail.com","ParentialDaysOff",50)
    assert "Your request has been sent"==create_request("billb97@gmail.com","ParentialDaysOff",50)


def test_left_days_off(insert_users):
    assert 25==get_left_days_off('manosmorf97@gmail.com','NormalDaysOff')
    assert 90==get_left_days_off('billb97@gmail.com','DiseaseDaysOff')
    assert 90==get_left_days_off('manosmorf97@gmail.com','DiseaseDaysOff')
    assert 25==get_left_days_off('billb97@gmail.com','NormalDaysOff')

def test_unseen_answers(insert_users):
    db,cursor=connect()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_it','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_it2','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB2','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB3','no','billb97@gmail.com')")
    db.commit()
    assert 2==unseen_answers('manosmof97@gmail.com')
    assert 3==unseen_answers('billb97@gmail.com')
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itT','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB2','no','billb97@gmail.com')")
    db.commit()
    #viewed=yes
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTe','yes','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB','yes','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB2','yes','billb97@gmail.com')")
    db.commit()
    assert 3==unseen_answers('manosmof97@gmail.com')
    assert 5==unseen_answers('billb97@gmail.com')
    disconnect(db,cursor)

def test_results(insert_users):
    db,cursor=connect()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_it','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_it2','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB2','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itB3','no','billb97@gmail.com')")
    db.commit()
    resm=results('manosmof97@gmail.com')
    resb=results('billb97@gmail.com')
    assert(len(resm))==2
    assert 'Got_it'==resm[0]
    assert 'Got_it2'==resm[1]
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itT','no','manosmof97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB','no','billb97@gmail.com')")
    db.commit()
    cursor.execute("Insert into Decision (description,viewed,reciever) values ('Got_itTB2','no','billb97@gmail.com')")
    db.commit()
    resm2=results('manosmof97@gmail.com')
    assert(len(resm2))==1
    assert 'Got_itT'==resm2[0]
    resb2=results('billb97@gmail.com')
    assert len(resb2)==2
    assert 'Got_itTB'==resb2[0]
    assert 'Got_itTB2'==resb2[1]




