# String Reverse:
s1 = "This is a String."
new_str = ""

for l in s1:
    # print(l)
    new_str = l + new_str

print(new_str)

length = len(s1)
print("String Length is " + str(length))

for i in range((length-length), -1, -1):
    new_str = new_str + s1[i]
print(new_str) 
