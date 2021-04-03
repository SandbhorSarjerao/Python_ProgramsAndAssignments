from csv import *

with open('emp.csv', 'w',newline='') as f:
    w = writer(f) # returns writer object to write data
    print(type(w))
    w.writerow(['EmpNo','EmpName','EmpSal','EmpAddr'])
    while True:
        EmpNo = int(input('Enter Employee Number: '))
        EmpName = input('Enter Employee Name: ')
        EmpSal = float(input('Enter Employee Salary: '))
        EmpAddr = input('Enter Employee Address: ')
        w.writerow([EmpNo,EmpName,EmpSal,EmpAddr])
        option = input('Do you want to insert one more record: [Yes|No] ')
        if option.lower() == 'no':
            break
print('Employee Data successfully to csv file.')
f.close()

with open('emp.csv', 'r') as f:
    r = reader(f)  # returns csv reader object
    data = list(r)
    # print(data)
    for row in data:
        for column in row:
            print(column, '\t', end='')
            print()
f.close()