'''
range() ==>
Example => r = range(10)
1) Order NOT preserved
2) Duplicates are NOT Allowed
3) Represent ()
4) Slicing & Indexing Allowed
5) Immutable - Can NOT be updated
6) NOT Heterogeneous Elements Allowed
7) Not Dynamic - Can Not Add & Delete Elements - Can NOT chage the size
'''


r = range(10)
r[0] = 777  # Error - As per Declaration allowed values are from 0-9

range(10)
range(10, 100)
range(0, 101, 5)

list1 = list(range(1, 11))
