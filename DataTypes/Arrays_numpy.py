from numpy import *

# 1-D Array
arr1D = array([1,2,3,4,5,6],int)
print("1-D Array: ",arr1D)
print(arr1D.dtype)

arr1D = array([1,2,3,4,5,6],float)
print("1-D Array: ",arr1D)
print(arr1D.dtype)

linArr = linspace(0,15,20)          # 20-Parts - Fixed Size
print("Linspace Array: ", linArr)

logArr = logspace(1,40,10)          # Parts - Not fixed part size
print("Logspace Array: ", logArr)
print('%.2f' %logArr[0])
print('%.2f' %logArr[9])

arngArr = arange(1,15,2)            # Steps 1 3 5 7 etc...
print("arange Array: ", arngArr)

zeroArr = zeros(10)                 # 0's array with 10 elements
print("zeros Array: ", zeroArr)

onesArr = ones(10)                  # 1's array with 10 elements
print("zeros Array: ", onesArr)