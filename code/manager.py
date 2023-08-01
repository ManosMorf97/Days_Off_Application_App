from connection import *

def reduce_days_off(true_or_false,results,db,cursor):
    if(true_or_false=="false") :
        return
    for accepted_result in results:
        request_id=accepted_result[0]
        email_=accepted_result[1]
        category=accepted_result[2]
        days_off=accepted_result[3]
        sql_statement="Update Employee set "+category+"="+category+"-"+days_off+" where email=%s"
        values=tuple(email_)
        cursor.execute(sql_statement,values)
        db.commit()
        

def process_Request(requests_ids,true_or_false,Accepted_or_Rejected,db,cursor):
    sql_statement="Update Request set accepted="+true_or_false+" where RequestId in %s"
    values=tuple(requests_ids)
    cursor.execute(sql_statement,values)
    db.commit()
    sql_statement="select id,email,category,RequestedDaysOff from Request where accepted="+true_or_false
    cursor.execute(sql_statement)
    db.commit()
    results=[result for result in list(cursor.fetchall())]
    for result in results:
        request_id=result[0]
        email_=result[1]
        category=result[2]
        days_off=result[3]
        description="The request with id: "+request_id+" where you asked"+str(days_off)+" "+category+" has been "+Accepted_or_Rejected
        sql_statement="Insert into Decision values(%s,false,%s)"
        values=(description,email_)
        cursor.execute(sql_statement,values)
        db.commit()
    reduce_days_off(true_or_false,results,db,cursor)

def Accept_Reject(accepted_requests_ids):
    db,cursor=connect()
    results=[result for result in list(cursor.fetchall())]
    ids=list(map(lambda result:result[0],results))
    rejected_requests_ids=list(set(ids)-set(accepted_requests_ids))
    process_Request(rejected_requests_ids,"false","Rejected")
    process_Request(accepted_requests_ids,"true","Accepted")
    disconnect(db,cursor)
    


