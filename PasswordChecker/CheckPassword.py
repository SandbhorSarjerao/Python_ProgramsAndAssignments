import requests

url = 'https://api.pwnedpasswords.com/range/' + 'Password@123'
res = requests.get(url)
print(res)

