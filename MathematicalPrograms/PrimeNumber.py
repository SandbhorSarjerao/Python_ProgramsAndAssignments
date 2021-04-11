# Prime Number => Number Divisible by 1 and Number itself
#  1, 3 , 5, 7, 11, 13, 17, 19, 23, 29, 31 ... etc

num = 7

for i in range(2, num):
    if num % i == 0:
        print(num," Not Prime Number")
        break
else:
    print(num," is Prime Number")
    