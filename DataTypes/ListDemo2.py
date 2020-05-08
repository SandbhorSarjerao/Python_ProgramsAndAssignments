my_list = ['a', 'b', 'c', 'd', 'f']
print("Print List: ", my_list)

print("Print List starting from 0 and till 3: ", my_list[0:3])

Length = len(my_list)
print("Length of List: ", Length)

my_list.append('g')
print(my_list)

my_list.pop()
print(my_list)

my_first_item = my_list.pop(0)
print(my_list)
print("First Item of List: ", my_first_item)

print(my_list.reverse())
