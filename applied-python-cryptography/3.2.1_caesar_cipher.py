

def encrypt(plaintext, shift_key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isupper():
            ciphertext += chr((ord(letter) + shift_key - 65) % 26 + 65)
        elif letter.islower():
            ciphertext += chr((ord(letter) + shift_key - 97) % 26 + 97)
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext, shift_key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isupper():
            plaintext += chr((ord(letter) - shift_key - 65) % 26 + 65)
        elif letter.islower():
            plaintext += chr((ord(letter) - shift_key - 97) % 26 + 97)
        else:
            plaintext += letter
    return plaintext

shiftkey = 10
plaintext = input('Enter a string to encrypt: ')
my_string = encrypt(plaintext, shiftkey);
print ('encrypted: ', my_string)
my_string = decrypt(my_string, shiftkey);
print ('decrypted: ', my_string)
