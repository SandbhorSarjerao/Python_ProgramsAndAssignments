number = int(input("Please Enter Number: "))
if number<0:
    print(number," is Negative")
elif number>0:
    print(number," is Positive")
elif number==0:
    print(number," is Zero")
else:
    print("Not Defined")

a = 500
b = 200
c = 300
if a>b and a>c:
    print("a is greatest number")
elif b>c and b>a:
    print("b is greatest number")
else:
    print("c is greatest number")