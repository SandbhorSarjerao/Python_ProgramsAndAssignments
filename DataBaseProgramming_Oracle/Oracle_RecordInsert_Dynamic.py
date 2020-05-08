import cx_Oracle
try:
    con = cx_Oracle('scott/tiger@localhost')
    cursor = con.cursor()
    while True:
        eno = int(input('Enter Employee Number: '))
        ename = input('Enter Employee Name: ')
        esal = float(input('Enter Employee Salary: '))
        eaddr = input('Enter Employee Address: ')
        query = "insert int employees values(%d, '%s', %f, '%s')"
        cursor.execute(query %(eno, ename, esal, eaddr))
        con.commit()
        print('Record Inserted Successfully.')
        option = input('Do you want to insert one more record [Yes|No]: ')
        if option.lower() == 'no':
            break
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()