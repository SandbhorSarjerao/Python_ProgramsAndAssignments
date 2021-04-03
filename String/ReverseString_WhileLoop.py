s = input("Enter String to Reverse: ")
ReversedString = ""
i = len(s) - 1

while i >= 0:
    ReversedString = ReversedString + s[i]
    i = i - 1

print("Reversed String is: ", ReversedString)

# 2nd Way
s = input("Enter String to Reverse: ")
ReversedString = ""
n = len(s) - 1
i = 0
print("String in Forward Direction: ")
while i<n:
    print(s[i], end='')
    i = i + 1

print("String in Backwoard Direction: ")
i = n - 1
while i > 0:
    print(s[i], end='')
    i = i - 1
