

'''
and     ==> Both Conditions must be True
or      ==> True if either is True otherwise False
not     ==>
'''

print("10==10 and 20==20 : ", 10==10 and 20==20)    # True
print("10==10 and 20!=20 : ", 10==10 and 20!=20)    # False
print("10!=10 and 20!=20 : ", 10!=10 and 20!=20)    # False


print("10==10 or 20==20 : ", 10==10 or 20==20)    # True
print("10==10 or 20!=20 : ", 10==10 or 20!=20)    # True
print("10!=10 or 20!=20 : ", 10!=10 and 20!=20)   # False

print(not 10!=10)   # True
print(not 10==10)   # False

# 0 means False, Non-Zero means True
print(0)        # 0
print(not 0)    # True ==> 0 means False, Non-Zero means True

print(10)        # 10
print(not 10)    # False   ==> 0 means False, Non-Zero means True

# Empty String is False, Non-Empty String is True
print(not '')        # True
print(not 'Durga')   # False

print(not True)    # False
print(not False)   # True

# None is False
print(not None)     # True