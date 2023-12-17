from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# note use pip3 install pycryptodome
# https://stackoverflow.com/questions/19623267/importerror-no-module-named-crypto-cipher

def DES_CBC_encrypt(plaintext, DES_key, initialization_vector):
    DES_CBC_cipher  = DES.new(DES_key, DES.MODE_CBC, initialization_vector)
    
    ciphertext = DES_CBC_cipher.encrypt(pad(plaintext, DES.block_size))

    return ciphertext

def DES_CBC_decrypt(ciphertext, DES_key, initialization_vector):
    DES_CBC_cipher  = DES.new(DES_key, DES.MODE_CBC, iv=initialization_vector)

    plaintext = unpad(DES_CBC_cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

plaintext = input("Enter plaintext: ").encode('utf-8')
DES_key = get_random_bytes(8)
initialization_vector = get_random_bytes(8)

ciphertext = DES_CBC_encrypt(plaintext, DES_key, initialization_vector)
decrypted_plaintext = DES_CBC_decrypt(ciphertext, DES_key, initialization_vector)

print("plain text: ", plaintext.decode())
print("encrypted text: ", ciphertext.hex())
print("decrypted text: ", decrypted_plaintext.decode())

print();
print('ugly:')
print("plain text: ", plaintext)
print("encrypted text: ", ciphertext)
print("decrypted text: ", decrypted_plaintext)