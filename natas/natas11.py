import base64
import json

def decrypt_xor(plain, cipher):
    secret_key = ""

    for x in range(len(plain)):
        secret_key += str(chr(cipher[x] ^ plain[x % len(plain)]))

    return secret_key

def encrypt_xor(key, cookie):
    data = ""
    for x in range(len(cookie)):
        data += chr(cookie[x] ^ key[x % len(key)])   

    data = base64.encodebytes(data.encode('utf-8')).decode().strip()  
    return data

if __name__ == "__main__":
    cipher = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GJTYOBCU2TRg="
    cipher = base64.decodebytes(cipher)

    plain = {"showpassword": "no", "bgcolour": "#aaaaaa"}
    plain = json.dumps(plain).encode('utf-8').replace(b" ", b"")

    secret_key = decrypt_xor(cipher, plain)
    print(secret_key)
    # Secret Key = eDWoeDWoeDWoeDWoeDWoeDWoeDWob¶Owd♠WoeDW

    # Added another byte by adding "o" at the end to indicate "yes"
    # secret_key = "eDWoeDWoeDWoeDWoeDWoeDWoeDWob¶Owd♠WoeDWo"
    
    # Format new cookie data as JSON string
    new_cookie = {"showpassword": "yes", "bgcolour": "#aaaaaa"}
    new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")

    # Encode secret key
    data = encrypt_xor(secret_key.encode('utf-8'), new_cookie)  
    print(data)
