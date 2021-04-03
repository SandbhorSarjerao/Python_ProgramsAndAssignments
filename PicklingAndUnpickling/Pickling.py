import PicklingAndUnpickling.Employee as emp
import pickle

f = open("emp.data", "wb")
n = int(input('Enter Number of Employees: '))
for i in range(n):
    eno = int(input('Enter Employee Number: '))
    ename = input('Enter Employee Name: ')
    esal = float(input('Enter Employee Salary: '))
    eaddr = input('Enter Employee Address: ')
    e = emp.Employee(eno, ename, esal, eaddr)
    pickle.dump(f, e)
