# This programe checks a word how many times found in a string

str1 = "This is test to test how many times test found in this string"
list1= str1.split(" ")

cnt = 0
for i in list1:
  if(i == 'test'):
    cnt += 1

print("Number of times word 'test' found in string is " + str(cnt))   


# Check whether a string exist in a string
str2 = test
print(str1.find(str2))
