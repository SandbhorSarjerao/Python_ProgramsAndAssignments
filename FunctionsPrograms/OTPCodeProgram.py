from random import randint



# 1st Way
# print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep="")

# 2nd Way
for i in range(3):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep="")

# OTP => A7B6C3
# 1,3,5 => Alphabets
# 2,4,6 => Digits
for i in range(3):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9))

# 3rd Way ==> INVALID WAY
from random import *
for i in range(3):
    print(randint(000000, 999999))

