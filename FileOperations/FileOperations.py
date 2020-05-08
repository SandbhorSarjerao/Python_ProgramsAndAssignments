# Read Mode File
f = open('abc.txt', 'r')
print('File Name', f.name)
print('File Mode', f.mode)
print('Is File Readable ?', f.readable())
print('Is File Writable ?', f.writable())
print('Is File Closed ?', f.closed)
f.close()
print('Is File really Closed ?', f.closed)

# Write Mode File
f = open('abc.txt', 'w')
print('File Name', f.name)
print('File Mode', f.mode)
print('Is File Readable ?', f.readable())
print('Is File Writable ?', f.writable())
print('Is File Closed ?', f.closed)
f.close()
print('Is File really Closed ?', f.closed)

# Append Mode File
f = open('abc.txt', 'a')
print('File Name', f.name)
print('File Mode', f.mode)
print('Is File Readable ?', f.readable())
print('Is File Writable ?', f.writable())
print('Is File Closed ?', f.closed)
f.close()
print('Is File really Closed ?', f.closed)

# r+ (Read + Write) Mode File
f = open('abc.txt', 'r+')
print('File Name', f.name)
print('File Mode', f.mode)
print('Is File Readable ?', f.readable())
print('Is File Writable ?', f.writable())
print('Is File Closed ?', f.closed)
f.close()
print('Is File really Closed ?', f.closed)