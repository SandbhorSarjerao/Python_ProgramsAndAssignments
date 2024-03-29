import cx_Oracle
try:
    query = "drop table employees"
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    cursor.execute(query)
    print('Employee Table Dropped Successfully.')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()