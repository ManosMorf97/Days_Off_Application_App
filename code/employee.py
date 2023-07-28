from secret import *

def create_request(email,category,request_days_off):
    db=mysql.connector.connect(user='root',password=mysql_pwd,database='permisions',host="localhost")
    cursor=db.cursor()
    values=(category,email)
    sql_statement="select %s from employee where email=%s"
    cursor.execute(sql_statement,values)
    results=[result for result in list(cursor.fetchall())]
    days_off=int(results[0][0])
    db.commit()
    if(days_off>=request_days_off):
        sql_statement="insert into table Request (email,category,request_days_off) values(%s,%s,%s) "
        values=(email,category,request_days_off)
        cursor.execute(sql_statement,values)
        db.commit()
        sql_statement="update Employee set %s=%s where email=%s "
        values=(category,str(int(days_off-request_days_off)),email)
        cursor.execute(sql_statement,values)
        db.commit()
        cursor.close()
        db.close()
        return "Your request has been sent"
    else:
        return "You cannot take too many days off for "+category+" check days off "

