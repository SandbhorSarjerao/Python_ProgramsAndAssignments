
a = '5'
b = '6'
c = 'Hello World'

result = a + b
# result = a + b + c
print(result)

p = 5
q = 6

int_add = int.__add__(p, q)     # Magic Methods
int_sub = int.__sub__(p, q)
int_mul = int.__mul__(p, q)

str_add = str.__add__(a, c)

print('int_add: ', int_add)
print('int_sub: ', int_sub)
print('int_mul: ', int_mul)

print('str_add: ', str_add)