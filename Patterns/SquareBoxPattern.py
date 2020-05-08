"""
* * * *
* * * *
* * * *
* * * *
"""

n = int(input("Enter Number of Rows: "))
for i in range(n):      # Row Number
    for j in range(n):  # Number of *
        print("*", end=" ")
    print()

# 2nd Way
n = int(input("Enter Number of Rows: "))
for i in range(n):
    print("* "*n)
