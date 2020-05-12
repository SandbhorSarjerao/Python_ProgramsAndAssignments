

# int()
print(int(10.123))      # 10
print(int(10+20j))      # Error
int(True)       # 1
int(False)      # 0
int('1234')     # 1234
int('1234.1234')    # Error


# float()
print(float(10))        # 10.0
float(10+20j)       # Error
float(True)     # 1.0
float(False)        # 0.0
float('10.5')       # 10.5
float('10')         # 10.0

# complex()
complex(10)     # 10+0j
complex(10.5)     # 10.5+0j
complex(True)     # 0+0j
complex(x, y)     # x+yj

# bool()    # 0 means False otherwise True
bool(0)     # False
bool(10)    # True
bool(-10)   # True
bool(0.0)   # False
bool(12.35) # True
bool(0+0j)  # False
bool(0.1+10j)   # True
bool('')    # False
bool(' ')   # True
bool('True')    # True
bool('False')   # True

# str()
str(10)
str(10.5)
str(10+20j)
str(True)
str(False)


# str()

