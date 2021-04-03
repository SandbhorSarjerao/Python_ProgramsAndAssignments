# Extract Numbers from a string using RegEx
import re
s1 = "1+2-34+7879-237+333-66"

pat = r"[-]?[0-9]+"

print(re.findall(pat, s1))
