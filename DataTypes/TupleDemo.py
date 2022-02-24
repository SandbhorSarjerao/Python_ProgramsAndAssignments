'''
Tuple ==>
1) Insertion order preserved
2) Duplicates are Allowed
3) Represent ()
4) Slicing & Indexing Allowed
5) Immutable - Can NOT be updated
6) Heterogeneous Elements Allowed
7) Size Can NOT chage
'''

tuple1 = (45, 'Automation', 'Testing', True, 12.05, 45, 45)
tuple2 = (45, 99)

print(tuple1.count(45))                                         # 3

print(tuple1.index('Testing'))                                  # 3

tuple3 = tuple1 + tuple2              # Merge 2 tuples
print(tuple3) 

for i in tuple3:
  print(i)
  
for i in range(0, len(tuple3)):
  print(tuple3[i])  
