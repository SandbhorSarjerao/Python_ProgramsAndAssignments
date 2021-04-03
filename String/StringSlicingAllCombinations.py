s = 'abcdefghij'
print(s[1:6:2])        # bdf
print(s[::1])          # abcdefghij
print(s[::-1])         # jihgfedcba
print(s[3:7:-1])       # ''
print(s[7:4:-1])       # hgf
print(s[0:10000:1])    # abcdefghij
print(s[-4:1:-1])      # gfedc
print(s[-4:1:-2])      # gec
print(s[5:0:1])        # ''
print(s[9:0:0])        # ValueError: Slice step cannot be Zero
print(s[0:-10:-1])     # ''
print(s[0:-11:-1])     # a
print(s[0:0:1])        # ''
print(s[0:-9:-2])      # ''
print(s[-5:-9:-2])     # fd
print(s[10:-1:-1])     # ''
print(s[10000:2:-1])   # jihgfed

#################################################

s = "Sarjerao"
print(s[:])
print(s[::])
print(s[0:])
print(s[0:7])
print(s[::-1])
print(s[0:8:2])
print(s[::2])
# print(s[::0])
print(s[-1:-6:1])
print(s[-1:-5:-1])
print(s[1:7:-2])
print(s[-1::-1])
print(s[:0:-1])
print(s[2:-1:-1])