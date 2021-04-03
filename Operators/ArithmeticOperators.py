'''
+
-
*
/
//  Floor Division
%
** Exponent/Power
'''

a = 10
b = 2

print("Addition: ", a + b)         # 12
print("Addition: ", '10' + '20')         # '1020'
print("Addition: ", '10' + 20)         # TypeError => Both should be either Digit or String

print('Subtraction: ', a - b)         # 8

print('Multiplicaiton: ', a * b)         # 20
print('Multiplicaiton: ', '10' * 2)         # '1010'
print('Multiplicaiton: ', 2 * '20')         # '2020'
print('Multiplicaiton: ', '10' * '2')         # TypeError => can't multiply sequence by non-int of type 'str'
print('Multiplicaiton: ', 2 * '20' + '20')         # '202020'

print('Divison: ', a / b)            # 5.0 <= Float Value
print('Divison: ', 10.0 / b)         # 5.0 <= Float Value

print('Floor Division: ', a // b)       # 5
print('Floor Division: ', 10.0 // b)    # 5.0

print('Modulus: ', a % b)      # 0
print('Modulus: ', 10.0 % 2)   # 0.0
print('Modulus: ', 10 % 3)     # 1
print('Modulus: ', 10.0 % 3)   # 1.0
print('Modulus: ', 10.5 % 2.0) # 0.5

print('Power: ', a ** b)  # 100
print('Power: ', 10.0 ** 2.0)  # 100.0

