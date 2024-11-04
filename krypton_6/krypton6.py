key = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
ciphertext = "PNUKLYLWRQKGKBE"

for i in range(len(ciphertext)):
    shift = ord(ciphertext[i]) - ord(key[i])
    if shift < 0: 
        shift += 26
    decrypted_char_ascii = shift + ord('A')
    print(chr(decrypted_char_ascii), end='')
