import mysql.connector
import mysql.connector.errorcode
from secret import *

def create_request(email,category_double_quote,request_days_off):
    category={}
    category["NormalDaysOff"]='NormalDaysOff'
    category["ParentialDaysOff"]='ParentialDaysOff'
    category["DiseaseDaysOff"]='DiseaseDaysOff'
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    values=email,
    sql_statement="select "+category_double_quote+" from Employee where email=%s"
    cursor.execute(sql_statement,values)
    results=[result for result in list(cursor.fetchall())]
    print(results)
    days_off=int(results[0][0])
    sql_statement="select sum(Requested_Days_Off) from Requests where email=%s and category=%s and accepted=null"
    values=(email,category[category_double_quote])
    cursor.execute(sql_statement,values)
    results=[result for result in list(cursor.fetchall())]
    overall_request_days_off=results[0][0]+request_days_off
    db.commit()
    if(days_off>=request_days_off):
        sql_statement="insert into Request (email,category,RequestedDaysOff) values(%s,%s,%s) "
        values=(email,category[category_double_quote],request_days_off)
        cursor.execute(sql_statement,values)
        db.commit()
        cursor.close()
        db.close()
        return "Your request has been sent"
    else:
        return "You cannot take too many days off.For "+category_double_quote+" check days off "
    
def unseen_answers(email):
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    sql_statement="select count(*) from Decision where reciever=%s"
    values=email,
    cursor.execute(sql_statement,values)
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    cursor.close()
    db.close()
    return int(results[0][0])


def get_left_days_off(email,category_double_quote):
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    sql_statement="select "+category_double_quote+" from Employee where email=%s"
    values=email,
    cursor.execute(sql_statement,values)
    results=[result for result in list(cursor.fetchall())]
    db.commit()
    cursor.close()
    db.close()
    return int(results[0][0])

def results(email):
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    sql_statement="select description from Decision where reciever=%s"
    values=email,
    cursor.execute(sql_statement,values)
    returned_results=[result[0] for result in list(cursor.fetchall())]
    db.commit()
    cursor.close()
    db.close()
    return returned_results


#print(create_request('manosmorf97@gmail.com',"NormalDaysOff",10))
#print(unseen_answers("manosmorf97@gmail.com"))
#print(get_left_days_off('manosmorf97@gmail.com',"ParentialDaysOff"))
#print(results("manosmorf97@gmail.com"))

