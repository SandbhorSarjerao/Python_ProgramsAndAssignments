import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}, Check the API & Try Again!')
    return res

request_api_data('Password@123')

def pwned_api_check(password):
    print(password.encode('utf-8'))
    print(hashlib.sha1(password.encode('utf-8').hexdigest()).upper())
    sha1password = hashlib.sha1(password.encode('utf-8'))
    first5_char = sha1password[:5]
    tail = sha1password[5:]
    print(first5_char, tail)
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response, tail)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    print(hashes)
    for h, count in hashes:
        print(h, count)
        if h == hash_to_check:
            return count
    return 0

# pwned_api_check('Password@123')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times..... \n You should change your password')
        else:
            print(f'{password} was NOT found. Carry On...')
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# Run from CMD Line with below command
# Python CheckPassword.py Hello
# Python CheckPassword.py Hello Hello@123
# Python CheckPassword.py Hello Hello@123 Password@123