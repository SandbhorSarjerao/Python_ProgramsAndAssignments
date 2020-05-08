import cx_Oracle
try:
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    query = "select * from employees"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row, end='')
        print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()