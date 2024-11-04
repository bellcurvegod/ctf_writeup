import base64
import json

def encrypt_xor(key, cookie):
    data = ""
    for x in range(len(key)):
        data += str(chr(cookie[x] ^ key[x % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data

def decrypt_xor(plaintext, ciphertext):
    key = ""

    for x in range(len(plaintext)):
        key += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))

    return key

if __name__ == "__main__":
    ciphertext = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GJTYOBCU2TRg="
    ciphertext = base64.decodebytes(ciphertext)
    plaintext = {"showpassword":"no", "bgcolor":"#aaaaaa"}

    # Format JSON by removing space
    plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")

    key = decrypt_xor(ciphertext, plaintext)
    print(key)

    key = b"eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeD"
    new_cookie = {"showpassword":"yes", "bgcolor":"#aaaaaa"}
    new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")
    data = encrypt_xor(key, new_cookie)
    print(data)
