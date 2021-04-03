a = 5
b = 6

print("Before Swapping : ", a, b)

a,b = b,a       # ROT_TWO() ==> Swap the two topmost stack items
print("After Swapping-Assignment Operator : ", a, b)

temp = a
a = b
b = temp

print("After Swapping-Temp : ", a, b)

a = a + b
b = a - b
a = a - b
print("After Swapping-Add & Sub : ", a, b)

a = a * b
b = a / b
a = a / b
print("After Swapping-Mul & Div : ", a, b)

a = a ^ b
b = a ^ b
a = a ^ b
print("After Swapping-XOR : ", a, b)

