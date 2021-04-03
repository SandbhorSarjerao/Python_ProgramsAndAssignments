'''
is      => Address/Reference Comparison
is not
'''



l1 = ['sunny', 'bunny', 'vinny', 'chiny']
l2 = ['sunny', 'bunny', 'vinny', 'chiny']
print("l1 is l2 : ", l1 is l2)  # False => Address Comparison
print("l1 is not l2 : ", l1 is not l2)  # True => Address Comparison

l1 = l2
print("l1 is l2 : ", l1 is l2)  # True => Address Comparison
print("l1 is not l2 : ", l1 is not l2)  # False => Address Comparison