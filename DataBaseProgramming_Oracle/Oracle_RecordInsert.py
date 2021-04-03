import cx_Oracle
try:
    query = "insert into employees values(100,'Sarjerao',100000,'Pune')"
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    print('Record Inserted Successfully.')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()