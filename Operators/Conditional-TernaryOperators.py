'''
Conditional / Ternary
x = b if a else c       # x=(a)?b:c
'''

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

min1 = a if a < b < c else b if b < a < c else c
print('Minimum Value: ', min1)

a = 5
b = 35
c = 30
min2 = a if a < b < c else b if b < a < c else c    # Wrong Answer, Not working
print('Minimum Value: ', min2)

min3 = a if a < b < c else b if b < c else c        # Wrong Answer, Not working
print('Minimum Value: ', min3)

