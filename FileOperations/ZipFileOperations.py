from zipfile import *

f = ZipFile('files22092019.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
f.close()
print('files22092019.zip created successfully.')


# UnZip Operation
f = ZipFile('files22092019.zip','r',ZIP_STORED)
names = f.namelist()
print(names)
for name in names:
    print('File Name: ', name)
    print('File Content: ')
    f1 = open(name, 'r')
    print(f1.read())
    f1.close()
f.close()