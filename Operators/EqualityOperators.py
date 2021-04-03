'''
Assignment Operator   =>
=

Value / Content Comparison =>
==
!=

is      => Address/Reference Comparison
is not
'''

print("10 == 10 : ", 10 == 10)  # True
print("10 != 10 : ", 10 != 10)

print("Durga == Durga : ", 'Durga' == 'Durga')  # Ture
print("Durga != Durga : ", 'Durga' != 'Durga')

print("10 == Durga : ", 10 == 'Durga')  # False
print("10 != Durga : ", 10 != 'Durga')  #

l1 = ['sunny', 'bunny', 'vinny', 'chiny']
l2 = ['sunny', 'bunny', 'vinny', 'chiny']
print("l1 == l2 : ", l1 == l2)  # True => Value/Content Comparison
print("l1 != l2 : ", l1 != l2)  #

print("l1 is l2 : ", l1 is l2)  # False => Address Comparison
print("l1 is not l2 : ", l1 is not l2)  # True => Address Comparison

l1 = l2
print("l1 == l2 : ", l1 == l2)  # True => Value/Content Comparison
print("l1 != l2 : ", l1 != l2)  #

print("l1 is l2 : ", l1 is l2)  # True => Address Comparison
print("l1 is not l2 : ", l1 is not l2)  # False => Address Comparison

d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
if 'C' in d:                # Not Available => Always seach in Keys only, Not in Value
    print('Available')
else:
    print('Not Available')

if 3 in d:
    print('Available')
else:
    print('Not Available')
