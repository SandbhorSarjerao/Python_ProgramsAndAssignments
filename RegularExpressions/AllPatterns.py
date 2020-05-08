import re

matcher = re.finditer(' ', 'a7b @k9z')
l = re.findall(' ', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\s', 'a7b @k9z')
l = re.findall('\s', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\S', 'a7b @k9z')
l = re.findall('\S', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\d', 'a7b @k9z')
l = re.findall('\d', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\D', 'a7b @k9z')
l = re.findall('\D', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\w', 'a7b @k9z')
l = re.findall('\w', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\W', 'a7b @k9z')
l = re.findall('\W', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('.', 'a7b @k9z')
l = re.findall('.', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('\S', 'a7b @k9z')
l = re.findall('\S', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[0-9]', 'a7b @k9z')
l = re.findall('[0-9]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[^0-9]', 'a7b @k9z')
l = re.findall('[^0-9]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[a-z]', 'a7b @k9z')
l = re.findall('[a-z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[^a-z]', 'a7b @k9z')
l = re.findall('[^a-z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[A-Z]', 'a7b @k9z')
l = re.findall('[A-Z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[^A-Z]', 'a7b @k9z')
l = re.findall('[^A-Z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[a-zA-Z]', 'a7b @k9z')
l = re.findall('[a-zA-Z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[^a-zA-Z]', 'a7b @k9z')
l = re.findall('[^a-zA-Z]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[a-zA-Z0-9]', 'a7b @k9z')
l = re.findall('[a-zA-Z0-9]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())

matcher = re.finditer('[^a-zA-Z0-9]', 'a7b @k9z')
l = re.findall('[^a-zA-Z0-9]', 'a7b @k9z')
print(l)
for m in matcher:
    print(m.start(), '......', m.group())
