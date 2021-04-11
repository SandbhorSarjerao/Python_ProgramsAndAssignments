from array import *

arr = array('i',[])

size = int(input("Enter Size of the Array: "))

for i in range(size):
    e = int(input("Enter Array Element Value: "))
    arr.append(e)

print("Array Elements: ",arr)

# Search an Element in Array

x = int(input("Enter element to Search in Array: "))
flag = False
pos = 0
for i in range(size):
    if arr[i]==x:
        flag = True
        pos = i
        break
    else:
        flag = False

if flag:
    print(x, " Found in Array at ",pos , " Index Position")
else:
    print(x, " Not Found in Array")

print("Using index function ",arr.index(x))