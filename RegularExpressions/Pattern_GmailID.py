import re
s = input('Enter Mail Id: ')
m = re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.]com', s)
if m is not None:
    print(s, 'Valid Gmail Email Id')
else:
    print(s, 'Invalid Gmail Id')
