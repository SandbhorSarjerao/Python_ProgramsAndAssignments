import cx_Oracle
try:
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    cutoff = float('Enter Cutoff Salary: ')
    query = "delete from employees where esal > %f"
    cursor.execute(query %cutoff)
    con.commit()
    print('Record Deleted Successfully.')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()