f = open('MyData.txt', 'r')
f1 = open('CopyMyData.txt', 'w')
print('MyData.txt File Data ==> ')
for data in f:
    print(data, end='')

    f1.write(data)
f.close()
f1.close()

print('CopyMyData.txt File Data ==> ')
f1 = open('CopyMyData.txt', 'r')
for data in f1:
    print(data, end='')
f1.close()