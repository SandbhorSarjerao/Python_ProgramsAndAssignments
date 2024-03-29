
'''
List ==>
1) Insertion order preserved
2) Duplicates are Allowed
3) Represent []
4) Slicing & Indexing Allowed
5) Mutable - Can be updated
6) Heterogeneous Elements Allowed
'''

# Example-1
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("List Values: ", List1)

List1.append(10)
print("List Values after appending value: ", List1)

List1.insert(2, 11)
print("List values after inserting 11 at index 2: ", List1)

List1.remove(List1[2])
print("List Values after removing Index value at 2 : ", List1)

List1.remove(3)
print("List values after removing value 3: ", List1)

List1.pop()
print("POP Last Element Removed: ", List1)

List1.pop(1)
print("POP - 2nd Element Removed: ", List1)

del List1[5:]
print("After Deleting multiple elements: ", List1)

print("Minimum Number from List: ", min(List1))
print("Maximum Number from List: ", max(List1))
print("Sum of List: ", sum(List1))
print("Sorted List: ", sorted(List1))
print("Sort List: ", List1.sort())




# Example-2
my_list = [“Jan”,”Feb”,”Mar”,”April”,”May”,”June”,”July”]
print(my_list)
print(my_list[3])
my_list.append(”Aug”)
print(my_list)
print(my_list[7])
my_list.remove(“Jan”)
print(my_list)
