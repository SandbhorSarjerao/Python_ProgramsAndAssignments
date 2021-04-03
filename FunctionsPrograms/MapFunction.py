l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

def sum(a,b):
    return a+b

l_sum = map(sum(a, b), l1, l2)
print(l_sum)

l_sum = map(lambda a,b:a+b, l1, l2)
print(l_sum)