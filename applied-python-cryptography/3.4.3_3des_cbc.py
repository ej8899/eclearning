from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def DES3_CBC_encrypt(plaintext, DES3_key, initialization_vector):
    
    DES3_CBC_cipher  = DES3.new(DES3_key, DES3.MODE_CBC, initialization_vector)

    ciphertext = DES3_CBC_cipher.encrypt(pad(plaintext, DES3.block_size))

    return ciphertext

def DES3_CBC_decrypt(ciphertext, DES3_key, initialization_vector):
    
    DES3_CBC_cipher  = DES3.new(DES3_key, DES3.MODE_CBC, initialization_vector)

    plaintext = unpad(DES3_CBC_cipher.decrypt(ciphertext), DES3.block_size)
    return plaintext



plaintext = input("Enter plaintext: ").encode('utf-8')

DES3_key = DES3.adjust_key_parity(get_random_bytes(24))
initialization_vector = get_random_bytes(8)

ciphertext = DES3_CBC_encrypt(plaintext, DES3_key, initialization_vector);
decrypted_text = DES3_CBC_decrypt(ciphertext, DES3_key, initialization_vector);

print ('cipher text: ',ciphertext.hex())
print ('decrypted text: ',decrypted_text.decode())