import re, urllib
import urllib.request

u = urllib.request.urlopen("https://www.redbus.in/info/contactus")
text = u.read()
numbers = set(re.findall('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+', str(text, re.IGNORECASE)))
for n in numbers:
    print(n)