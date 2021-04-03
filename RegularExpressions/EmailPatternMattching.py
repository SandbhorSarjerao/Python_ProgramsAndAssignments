import re

f = open("Resume.txt")
content = f.read()

pat = r"[a-zA-Z_0-9.]+@[a-zA-Z_0-9]+[.][a-zA-Z]+[.]?[a-zA-Z.]+"

list_emailids = re.findall(pat, content)

print(list_emailids)

valid_ids = []
for id in list_emailids:
    valid_ids.append(id.strip("."))

print(list_emailids)
print(valid_ids)

print(list(set(list_emailids)))
