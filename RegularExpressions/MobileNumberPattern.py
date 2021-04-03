'''
10 Digit mobile Number
- Starting with 9/8/7/7
- 10 digits
Ans1 => [6789][0-9]{9}
Ans2 => [6-9]\d{9}
'''

import re
s = input('Enter Mobile Number to validate: ')
m = re.fullmatch('[6789][0-9]{9}', s)
if m is not None:
    print(s, 'Is a valid Mobile Number')
else:
    print(s, 'Is Not valid Mobile Number')