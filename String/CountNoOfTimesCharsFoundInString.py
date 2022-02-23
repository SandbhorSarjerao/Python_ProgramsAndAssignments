# Find how many times a letter exist in a string

email = test.test@test.com

# Method-1

x = len(email)
y = len(email.replace("t",""))
t = x - y
print("Number of times Letter 't' found " + str(t))

# Method - 2
cnt = 0
for i in email:
  if(i=='t'):
    cnt += 1
    
print("Number of times Letter 't' found " + str(cnt))    
    
