from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def DES_CTR_encrypt(plaintext, DES_key, nonce):
    
    DES_CTR_cipher  = DES.new(DES_key, DES.MODE_CTR, nonce=nonce);
    ciphertext = DES_CTR_cipher.encrypt(plaintext);
    return ciphertext;

def DES_CTR_decrypt(ciphertext, DES_key, nonce):
    
    DES_CTR_cipher  = DES.new(DES_key, DES.MODE_CTR, nonce=nonce);
    plaintext = DES_CTR_cipher.decrypt(ciphertext);
    return plaintext;


plaintext = input("Enter plaintext: ").encode('utf-8')

DES_key = get_random_bytes(8)
nonce = get_random_bytes(7)

ciphertext = DES_CTR_encrypt(plaintext, DES_key, nonce);
decrypted_text = DES_CTR_decrypt(ciphertext, DES_key, nonce);

print ("plaintext: ", plaintext.decode());
print ("ciphertext: ", ciphertext.hex());
print ("decrypted: ", decrypted_text.decode());