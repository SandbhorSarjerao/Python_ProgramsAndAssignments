f = open('MyData.txt', 'r')
for data in f:
    print(data, end='')

f1 = open('CopyMyData.txt', 'w')
for data in f:
    f1.write(data)
f1.close()

f1 = open('CopyMyData.txt', 'r')
for data in f1:
    print(data, end='')
f1.close()