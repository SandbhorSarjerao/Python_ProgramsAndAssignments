s1 = 'Hello World !'
s2 = "Learn Python"

print(s1)
print(s2)

print(s1+s2)
print(s1, s2)

print("Hello \n World !")
print("Hello \t World !")
print("Test"*3)
print(s1[0:5])

print("My Name is %s and my Age is %d " %("Sarjerao", 39))

s3 = '''hello I am Sarjerao.
I am learning Python
And API Test Automation
'''
print(s3)

s4 = """Hello I am ShivajiRao.
Learning Python is very interesting.
"""
print(s4)

print('Hi I\'m ShivajiRao. \n Learning Python is very interesting.')
print("Hi I\'m ShivajiRao. \\n Learning \"Python\" is very interesting.")

print(len(s3))
print(s4.count("ShivajiRao"))
print(s3.count("Python"))
print(s3.lstrip())
print(s3.rstrip())
print(max(s4))
print(min(s3))
print(s4.lower())
print(s4.upper())
print(s4.find("ShivajiRao"))
print(s3.capitalize())
print(s4.replace("Hello","Bye"))
str1 = "ShivajiRao Hello Java Hello Python Hello JavaScript"
str2 = str1.split("Hello")
print(str2)

for obj in str2:
    print(obj)

a = "Sarjerao"
b = "ShivajiRao"
print(a is b)
print(a==b)
print(str1.__contains__(b))

