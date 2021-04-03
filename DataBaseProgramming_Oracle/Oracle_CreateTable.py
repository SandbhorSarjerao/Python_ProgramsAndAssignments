import cx_Oracle
try:
    query = "create table employees(eno number, ename varchar2(10), esal number(10,2), eaddress varchar2(20))"
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    cursor.execute(query)
    print('Employee Table Created Successfully.')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()