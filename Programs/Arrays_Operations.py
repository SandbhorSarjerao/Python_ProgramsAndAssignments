from numpy import *

arr = array([1,2,3,4,5])
print(arr)

# Add 5 to each element
arr = arr + 5
print(arr)

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

print("Sin Value of Array: ",sin(arr1))
print("Cos Value of Array: ",cos(arr1))

print("Log Value of Array: ",log(arr1))

print("Square Value of Array: ",square(arr1))
print("Square-root Value of Array: ",sqrt(arr1))

print("Sum Value of Array: ",sum(arr1))

print("MIN Value of Array: ",min(arr1))
print("MAX Value of Array: ",max(arr1))

print("Sort Value of Array: ",sort(arr1))

# print("Reverse Value of Array: ",reverse(arr1))

arr3 = arr1 + arr2
print("Addition of 2 arrays: ", arr3)

print("Concatenation of 2 Arrays: ", concatenate([arr1,arr2]))

print("Address of Array: ",id(arr1))

# Aliasing of  Array
array1 = array([2,6,8,1,3])
array2 = array1
print("array1: ",array1)            # SAME Values
print("array2: ",array2)            # SAME Values
print("array1: ",id(array1))        # SAME Address
print("array2: ",id(array2))        # SAME Address

# Copy - Shallow(both will interlilnk) & Deep(new array)
arr4 = arr1.view()      # Shallow Copy - Linked with each other
print("Array-1: ",arr1)
print("Array-4: ",arr4)
print("Array-1: ",id(arr1))
print("Array-4: ",id(arr4))

arr5 = arr1.copy()      # Deep Copy - Not linked with each other
print("Array-1: ",arr1)
print("Array-5: ",arr5)
print("Array-1: ",id(arr1))
print("Array-4: ",id(arr5))

