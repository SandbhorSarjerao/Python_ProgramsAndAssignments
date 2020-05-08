l = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(filter(lambda x : x%2 == 0, l))
print("Even Nos: ", l1)
l2 = list(filter(lambda x : x%2!=0, l))
print("Odd Nos: ", l2)

l3 = list(map(lambda x : 2*x, l))
print("Double Nos: ", l3)

l4 = list(map(lambda x : x**2, l))
print("Square Nos: ", l4)