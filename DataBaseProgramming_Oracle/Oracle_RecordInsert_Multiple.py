import cx_Oracle
try:
    query = "insert into employees values(:eno, :ename, :esal, :eaddr)"
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    records = [(200, 'Sunny', 2000, 'Mumbai'),
               (300, 'Bunny', 3000, 'Hyderabad'),
               (400, 'Chinny', 4000, 'Banglore')]
    cursor.executemany(query, records)
    con.commit()
    print('Multiple Records Inserted Successfully.')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()