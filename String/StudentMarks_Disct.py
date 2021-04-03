n = int(input("Enter the Number of Students: "))
d = {}
for i in range(n):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))
    d[name] = marks
print(d)

while True:
    name = input("Enter Student Name to get Marks: ")
    marks = d.get(name, -1)
    if marks == -1:
        print("Student Not Found.")
    else:
        print("The Marks of {} :{} ".format(name, marks))
    option = input("Do you want to find another student marks[Yes|No]: ")
    if option == "No":
        break

print("Thanks for using our Application.")