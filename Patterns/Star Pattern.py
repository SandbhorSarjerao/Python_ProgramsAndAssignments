# Pattern of *
"""
*
* *
* * *
* * * *
"""

n = int(input("Enter the Number of Rows: "))
for i in range(1, n+1):  # i is for Row Number
	for j in range(i):   # j is for the number of * to print
		print("*", end=" ")
	print()

# 2nd Way
n = int(input("Enter the Number of Rows: "))
for i in range(1, n+1):  # i is for Row Number
	print("* "*i)
