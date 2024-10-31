import base64

def decode_secret(encoded):
    byte_encoded = bytes.fromhex(encoded)
    reversed_encoded = byte_encoded[::-1]
    decoded = base64.b64decode(reversed_encoded)

    return decoded

if __name__ == "__main__":
    encoded = '3d3d516343746d4d6d6c315669563362'
    decoded = decode_secret(encoded)
    print(decoded)
