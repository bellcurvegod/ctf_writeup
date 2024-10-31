import base64
import json

ciphertext = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GJTYOBCU2TRg="
ciphertext = base64.decodebytes(ciphertext)
plaintext = {"showpassword":"no", "bgcolor":"#aaaaaa"}
# Here, we remove the space as JSON implementation in Python is different from PHP
plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")

def xor_decrypt(plaintext, ciphertext):
    secret = ""

    for x in range(len(plaintext)):
        secret += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))

    return secret

def xor_encrypt(key, cookie):
    data = ""
    for x in range(len(key)):
        data += str(chr(cookie[x] ^ key[x % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data

# Result = eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe
secret = xor_decrypt(ciphertext, plaintext)
print(secret)

key = b"eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeD"
new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")

data = xor_encrypt(key, new_cookie)
print(data)



