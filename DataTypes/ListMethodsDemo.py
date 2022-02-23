my_list = [5,2,6,1,0,9,8,4,3,7]
print(my_list)

# Length of List
print(len(my_list))

my_list.append(10)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

my_list.insert(0,11)
print(my_list)

print(my_list.sort())

print(my_list.reverse())

print(my_list + my_list)

print("Minimum Number from List: ", min(my_list))
print("Maximum Number from List: ", max(my_list))
print("Sum of List: ", sum(my_list))
print("Sorted List: ", sorted(my_list))
print("Sort List: ", my_list.sort())
