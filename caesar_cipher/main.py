import sys, random

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet_list = alphabet.split()

def generate_key():
    key = random.randint(0, 25)
    return key

def encrypt(plaintext, key):
    ciphertext = str()
    for i in plaintext:
        alphabet_index = alphabet_list.index(i)
        ciphertext += alphabet_list[(alphabet_index + key) % 26]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = str()
    for i in ciphertext:
        alphabet_index = alphabet_list.index(i)
        plaintext += alphabet_list[(alphabet_index - key) % 26]
    return plaintext

def brute_force(ciphertext):
    print('brute force:')
    for key in range(26):
        plaintext = str()
        for i in ciphertext:
            alphabet_index = alphabet_list.index(i)
            plaintext += alphabet_list[(alphabet_index + key) % 26]
        print(plaintext)

def main():
    plaintext = input('plaintext: ').lower()
    key = generate_key()
    ciphertext = encrypt(plaintext, key)
    plaintext = decrypt(ciphertext, key)
    print('ciphertext: %s' % ciphertext)
    print('plaintext: %s' % plaintext)
    brute_force(ciphertext)

if __name__ == '__main__':
    main()    