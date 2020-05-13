'''
Conditional / Ternary
'''

x = b if a else c       # x=(a)?b:c

a = 3
b = 5
minval = a if a < b else b
print('Minimum Value: ', minval)

a = -3
b = -5
minval = a if a < b else b
print('Minimum Value: ', minval)

a = 5
b = 3
c = 7
minval = a if (a < b and a < c) else b if b < c else c
print('Minimum Value: ', minval)
