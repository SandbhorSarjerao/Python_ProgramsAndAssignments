from array import *

intValues = array('i',[5, 7 , 11, 21, 18])
print("Int Values Array: ",intValues)
# print("Int Values Array: ",intValues.append())

for i in intValues:
    print(intValues[i])

print("Buffer Info: ",intValues.buffer_info())
print("Reverse Array: ",intValues.reverse())
print("First Array Element: ",intValues[0])
print("Second Array Element: ",intValues[1])
print("Count Array: ",intValues.count())
print("Insert Element to Array: ",intValues.insert())
print("POP Array: ",intValues.pop())
print("Reverse Array: ",intValues.remove())

signedIntVal = array('i',[5, 7 , -11, 21, 18])
print("Signed Int Values Array: ",signedIntVal)

unSignedIntVal = array('I',[5, 7 , 11, 21, 18])
print("Un-Signed Int Values Array: ",unSignedIntVal)

charVal = array('u',['a','e','i','o','u'])
print("Char Val: ",charVal)

copyArray = array(intValues.typecode,(e for a in intValues))
for e in copyArray:
    print(e)

copySquareArray = array(intValues.typecode,(e*e for a in intValues))
for e in copySquareArray:
    print(e)