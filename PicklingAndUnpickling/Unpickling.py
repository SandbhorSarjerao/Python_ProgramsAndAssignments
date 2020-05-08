import PicklingAndUnpickling.Employee as emp
import pickle

f = open("emp.dat", "rb")
print("Employees Data ==>")
while True:
    try:
        obj = pickle.load(f)
        # if obj.eno == 100:   # To display only particular record
        obj.display()
        # break
    except EOFError:
        print("All Records are Completed")
        break
f.close()