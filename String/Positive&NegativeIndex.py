s = input("Enter Some String: ")
i = 0
for ch in s:
    print("The Character present at Positive Index: {} & at Negative Index: {} is : {}".format(i, i - len(s), ch))
    i = i + 1
