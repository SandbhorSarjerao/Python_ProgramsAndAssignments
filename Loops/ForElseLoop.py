nums = [10, 16, 18, 21, 30, 26]

for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Not Found...")