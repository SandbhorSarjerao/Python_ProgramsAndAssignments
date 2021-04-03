'''
in
not in
'''

print('r' in 'Durga')   # True
print('z' in 'Durga')   # False

l1 = ['sunny', 'bunny', 'vinny', 'chiny']
l2 = ['sunny', 'bunny', 'vinny', 'chiny']
print("l1 in l2 : ", l1 in l2)              # False => Address Comparison
print("l1 not in l2 : ", l1 not in l2)      # True => Address Comparison

print("sun in l2 : ", 'sun' in l2)              # False => Address Comparison
print("sun not in l2 : ", 'sun' not in l2)      # True

print("bunny in l2 : ", 'bunny' in l2)              # True => Address Comparison
print("bunny not in l2 : ", 'bunny' not in l2)      # False => Address Comparison

l1 = l2
print("l1 = l2 => l1 in l2 : ", l1 in l2)              # False => Address Comparison
print("l1 = l2 => l1 not in l2 : ", l1 not in l2)      # True => Address Comparison

print("l1 = l2 => bunny in l2 : ", 'bunny' in l2)          # True => Address Comparison
print("l1 = l2 => bunny not in l2 : ", 'bunny' not in l2)  # False => Address Comparison
