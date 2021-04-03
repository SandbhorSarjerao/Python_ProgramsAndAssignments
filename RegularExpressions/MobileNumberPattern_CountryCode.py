'''
13 Digit mobile Number
- Starting with country code +91
- 10 digits mobile number
Ans1 => [6789][0-9]{9}
Ans2 => [6-9]\d{9}
'''

import re
s = input('Enter Mobile Number to validate: ')
m = re.fullmatch('(0|91|\+91)?[6789]\d{9}', s)
if m is not None:
    print(s, 'Is a valid Mobile Number')
else:
    print(s, 'Is Not valid Mobile Number')