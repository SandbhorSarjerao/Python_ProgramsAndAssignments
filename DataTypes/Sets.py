'''
Set ==>
Example => s = set()
1) Insertion Order NOT preserved
2) Duplicates are NOT Allowed
3) Represent {}
4) Slicing & Indexing NOT Allowed
5) Mutable - Can be updated
6) Heterogeneous Elements Allowed
7) Dynamic - Can Add & Delete Elements - Can chage the size
'''

x = set()
x.add(1)
x.add(2)
x.add(3)

print(x)

x.remove(3)
print(x)

x.pop()
print(x)
type(x)

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5]
y = set(my_list)
type(my_list)
print(y)

myset = {1,2,3,4,5,1,6,2,4,3,7,8,9}
type(myset)
print(myset)




