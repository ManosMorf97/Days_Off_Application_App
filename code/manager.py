import mysql.connector
import mysql.connector.errorcode
from secret import *

def reduce_days_off(true_or_false,results,db,cursor):
    if(true_or_false=="false") :
        return
    for accepted_result in results:
        sql_statement="select email,"+accepted_result[2]+" from Employee where email=%s"
        values=tuple(accepted_result[1])
        cursor.execute(sql_statement,values)
        inner_results=[result for result in list(cursor.fetchall())]
        email_=inner_results[0][0]
        days_to_reduce=accepted_result[3]
        left_days_off=inner_results[0][1]
        left_days_off=left_days_off-days_to_reduce
        sql_statement="update Employee set "+accepted_result[2]+"=%s where email=%s"
        values=(left_days_off,email_)
        cursor.execute(sql_statement,values)
        db.commit()


def process_Request(requests_ids,true_or_false,Accepted_or_Rejected):
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    sql_statement="Update Request set accepted="+true_or_false+" where RequestId in %s"
    values=tuple(requests_ids)
    cursor.execute(sql_statement,values)
    db.commit()
    sql_statement="select id,email,category,RequestedDaysOff from Request where accepted="+true_or_false
    cursor.execute(sql_statement)
    db.commit()
    results=[result for result in list(cursor.fetchall())]
    for result in results:
        description="The request with id: "+result[0]+" where you asked"+str(result[3])+" "+result[2]+" has been "+Accepted_or_Rejected
        sql_statement="Insert into Decision values(%s,false,%s)"
        values=(description,result[1])
        cursor.execute(sql_statement,values)
        db.commit()
    reduce_days_off(true_or_false,results,db,cursor)

def Accept_Reject(accepted_requests_ids):
    db=mysql.connector.connect(user='manos',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    cursor.execute("select id from requests")
    results=[result for result in list(cursor.fetchall())]
    ids=list(map(lambda result:result[0],results))
    rejected_requests_ids=list(set(ids)-set(accepted_requests_ids))
    process_Request(rejected_requests_ids,"false","Rejected")
    process_Request(accepted_requests_ids,"true","Accepted")
    


