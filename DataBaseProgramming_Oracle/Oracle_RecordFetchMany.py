import cx_Oracle
try:
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    query = "select * from employees"
    cursor.execute(query)
    n = int(input('Enter the Number of Records to Fetch'))
    data = cursor.fetchmany(n)
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