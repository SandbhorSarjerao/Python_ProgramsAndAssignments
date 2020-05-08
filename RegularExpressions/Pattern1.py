'''
Pattern ->
1. The allowed characters are: alphabetes, digits, #
2. First character should be lower case and from a to k
3. The 2nd character should be any digit divisible by 3
4. The length of identifier should be atleast 2
'''

import re
s = input('Enter identifier to validate: ')
m = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*  ', s)
if m!= None:
    print(s, 'Is a Valid required Identifier')
else:
    print(s, 'Is Not Valid required Identifier')