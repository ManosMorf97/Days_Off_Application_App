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

def test_see_Requests(insert_users):
    db,cursor=connect()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('manosmorf97@gmail.com','NormalDaysOff',7,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('billb97@gmail.com','DiseaseDaysOff',8,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('manosmorf97@gmail.com','NormalDaysOff',7,'Accepted') ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('billb97@gmail.com','DiseaseDaysOff',8,'Rejected') ")
    db.commit()
    Requests=see_Requests()
    assert len(Requests)==2
    assert len(Requests[0])==len(Requests[1])
    assert len(Requests[0])==5
    disconnect(db,cursor)

def test_Accept_Reject(insert_users):
    db,cursor=connect()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('manosmorf97@gmail.com','NormalDaysOff',7,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('billb97@gmail.com','DiseaseDaysOff',5,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('manosmorf97@gmail.com','NormalDaysOff',10,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('johnd97@gmail.com','ParentialDaysOff',27,NULL) ")
    db.commit()
    cursor.execute("insert into Request (email,category,RequestedDaysOff,approval) values('billb97@gmail.com','DiseaseDaysOff',8,NULL) ")
    db.commit()
    cursor.execute("Select RequestId from Request")
    ids=[result[0] for result in list(cursor.fetchall())]
    accepted_ids=[ids[1],ids[2],ids[3]]
    Accept_Reject(accepted_ids)
    cursor.execute("select count(*) from Request where approval='Accepted'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_accepted=results[0][0]
    cursor.execute("select count(*) from Request where approval='Rejected'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_rejected=results[0][0]
    assert 2==count_rejected
    assert 3==count_accepted
    cursor.execute("select count(*) from Decision where description like '%Rejected%'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_decisions_rejected=results[0][0]
    cursor.execute("select count(*) from Decision where description like '%Accepted%'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_decisions_accepted=results[0][0]
    assert 3==count_decisions_accepted
    assert count_rejected==count_decisions_rejected
    cursor.execute("select count(*) from Decision where description like '%NormalDaysOff%'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_decisions_NormalDaysOff=results[0][0]
    cursor.execute("select count(*) from Decision where description like '%DiseaseDaysOff%'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_decisions_DiseaseDaysOff=results[0][0]
    cursor.execute("select count(*) from Decision where description like '%ParentialDaysOff%'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    count_decisions_ParentialDaysOff=results[0][0]
    assert count_decisions_NormalDaysOff==2
    assert count_decisions_DiseaseDaysOff==2
    assert count_decisions_ParentialDaysOff==1
    cursor.execute("select NormalDaysoff from Employee where email='manosmorf97@gmail.com'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    manos_days_off_normal=results[0][0]
    cursor.execute("select DiseaseDaysoff from Employee where email='billb97@gmail.com'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    bill_days_off_disease=results[0][0]
    cursor.execute("select ParentialDaysoff from Employee where email='johnd97@gmail.com'")
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    john_days_off_parential=results[0][0]
    assert manos_days_off_normal==15
    assert bill_days_off_disease==85
    assert john_days_off_parential==23





