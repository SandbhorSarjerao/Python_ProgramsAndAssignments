nums = [25, 12, 36, 95, 14]
names = ['Sarjerao', 'Amit', 'Girish', 'Navin']
bolVales = [True, False]

print("List of Numbers: ", nums)
print("List of Strings: ", names)
print("List of Boolean Vales: ", bolVales)

heteroList = [nums, names]
print("List of Heterogeneous Elements: ", heteroList)

nums1 = [25, 36, 95, 14, 12, 26]
print("List of Numbers: ", nums1)

# del nums1(95, 14, 12)
del nums1[2:4]
print("List of Numbers: ", nums1)