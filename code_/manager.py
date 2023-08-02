from connection import *

def reduce_days_off(Accepted_or_Rejected,results,db,cursor):
    if(Accepted_or_Rejected=="Rejected") :
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
        

def process_Request(requests_ids,Accepted_or_Rejected,db,cursor):
    sql_statement="Update Request set accepted="+Accepted_or_Rejected+" where RequestId in %s"
    values=tuple(requests_ids)
    cursor.execute(sql_statement,values)
    db.commit()
    values=Accepted_or_Rejected,
    sql_statement="select id,email,category,RequestedDaysOff from Request where accepted=%s"
    cursor.execute(sql_statement,values)
    db.commit()
    results=[result for result in list(cursor.fetchall())]
    for result in results:
        request_id=result[0]
        email_=result[1]
        category=result[2]
        days_off=result[3]
        description="The request with id: "+request_id+" where you asked"+str(days_off)+" "+category+" has been "+Accepted_or_Rejected
        sql_statement="Insert into Decision values(%s,no,%s)"
        values=(description,email_)
        cursor.execute(sql_statement,values)
        db.commit()
    reduce_days_off(Accepted_or_Rejected,results,db,cursor)

def Accept_Reject(accepted_requests_ids):
    db,cursor=connect()
    results=[result for result in list(cursor.fetchall())]
    ids=list(map(lambda result:result[0],results))
    rejected_requests_ids=list(set(ids)-set(accepted_requests_ids))
    process_Request(rejected_requests_ids,"Rejected",db,cursor)
    process_Request(accepted_requests_ids,"Accepted",db,cursor)
    disconnect(db,cursor)
    
def see_Requests():
    db,cursor=connect()
    cursor.execute("select * from Request where accepted is NULL")
    results=[result for result in list(cursor.fetchall())]
    return results

