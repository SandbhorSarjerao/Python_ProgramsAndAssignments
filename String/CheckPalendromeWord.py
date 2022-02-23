# Check Palendrome word or not
# eg. madam, malayalam

# Method-1
a = "malayalam"
b = ""

for l in a:
    b = l + b

if(a==b):
  print(a + " is Palendrome word")
else:
    print(a + " is NOT Palendrome word")

# Method-2
b = ""
length = len(a)
print("String Length is " + str(length))

for i in range((length-1), -1, -1):
    b = b + a[i]

if(a==b):
  print(a + " is Palendrome word")
else:
    print(a + " is NOT Palendrome word")    
    

