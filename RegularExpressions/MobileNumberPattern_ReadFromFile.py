import re
try:
    f1 = open('input.txt','r')
    f2 = open('output.txt','w')
    for line in f1:
        mobile_list = set(re.findall('[6-9]\d{9}', line))
        for number in mobile_list:
            f2.write(number, '\n')
    print('Extracted all mobile numbers')
except Exception as e:
    print("Error found", e)
finally:
    f1.close()
    f2.close()