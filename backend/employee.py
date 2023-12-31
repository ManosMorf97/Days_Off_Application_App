from connection import *

def create_request(email,category_double_quote,request_days_off):
    category={}
    category["NormalDaysOff"]='NormalDaysOff'
    category["ParentialDaysOff"]='ParentialDaysOff'
    category["DiseaseDaysOff"]='DiseaseDaysOff'
    db,cursor=connect()
    try:
        values=(email,)
        sql_statement="select "+category_double_quote+" from Employee where email=%s"
        cursor.execute(sql_statement,values)
        results=[result for result in list(cursor.fetchall())]
        db.commit()
        days_off=int(results[0][0])
        sql_statement="select sum(RequestedDaysOff) from Request where email=%s and category=%s and approval is NULL "
        values=(email,category[category_double_quote])
        cursor.execute(sql_statement,values)
        results=[result for result in list(cursor.fetchall())]
        db.commit()
        past_requested_days_off=0
        if not(results[0][0] is None):
            past_requested_days_off=int(results[0][0])
        overall_requested_days_off=past_requested_days_off+request_days_off
        if(days_off<overall_requested_days_off):
            return "You cannot take too many days off.For "+category_double_quote+" check days off "
        sql_statement="insert into Request (email,category,RequestedDaysOff) values(%s,%s,%s) "
        values=(email,category[category_double_quote],request_days_off)
        cursor.execute(sql_statement,values)
        db.commit()
    except mysql.connector.Error as err:
        print(err)
        return "There is something wrong.Try again"
    disconnect(db,cursor)
    return "Your request has been sent"
    
def unseen_answers(email):
    db,cursor=connect()
    try:
        sql_statement="select count(*) from Decision where reciever=%s and viewed='no'"
        values=email,
        cursor.execute(sql_statement,values)
        results=[result for result in list(cursor.fetchall())]
        db.commit()
    except mysql.connector.Error as err:
        print(err)
    disconnect(db,cursor)
    return int(results[0][0])


def get_left_days_off(email,category_double_quote):
    db,cursor=connect()
    try:
        sql_statement="select "+category_double_quote+" from Employee where email=%s"
        values=email,
        cursor.execute(sql_statement,values)
        results=[result for result in list(cursor.fetchall())]
        db.commit()
    except mysql.connector.Error as err:
        print(err)
    disconnect(db,cursor)
    return int(results[0][0])

def results(email):
    db,cursor=connect()
    try:
        sql_statement="select description from Decision where reciever=%s and viewed='no'"
        values=email,
        cursor.execute(sql_statement,values)
        returned_results=[result[0] for result in list(cursor.fetchall())]
        db.commit()
        sql_statement="delete from Decision where reciever=%s"
        cursor.execute(sql_statement,values)
        db.commit()
    except  mysql.connector.Error as err:
        print(err)
    disconnect(db,cursor)
    return returned_results





#print(create_request('manosmorf97@gmail.com',"NormalDaysOff",10))
#print(unseen_answers("manosmorf97@gmail.com"))
#print(get_left_days_off('manosmorf97@gmail.com',"ParentialDaysOff"))
#print(results("manosmorf97@gmail.com"))

