'''
<
<=
>
>=
'''

print("10 < 20 : ", 10 < 20)        # True
print("10 <= 20 : ", 10 <= 20)      # True

print("10 > 20 : ", 10 > 20)    # False
print("10 >= 20 : ", 10 >= 20)    # False

print("durga < ravi : ", 'durga' < 'ravi')    # True
print("durga <= ravi : ", 'durga' <= 'ravi')    # True

print("durga > ravi : ", 'durga' > 'ravi')    # False
print("durga >= ravi : ", 'durga' >= 'ravi')    # False

print("True < False : ", True < False)    # False
print("True <= False : ", True <= False)    # False
print("True > False : ", True > False)    # True
print("True >= False : ", True >= False)    # True

print(ord('a'))  # 97
print(ord('1'))  # 49
print(chr(97))      # a
print(chr(98))      # b
print('abc' > '10')     # True

print('abc' > 10)  # TupeError => Not supported

print("10 < 20 < 30 : ", 10 < 20 < 30)        # True
print("10 < 20 < 30 > 50 : ", 10 < 20 < 30 > 50)        # False
