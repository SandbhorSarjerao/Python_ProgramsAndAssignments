import re

s = "Some VEryfy VERY"
p = r"[A-Z]+"

print("UpperCase Letters: ", re.findall(p, s))

p = r"\b[A-Z]+\b"

print("UpperCase Words: ", re.findall(p, s))

# Phone
s = "-3+4+45-12+34"