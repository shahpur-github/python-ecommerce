# Cryptography Challenge #1 - www.101computing.net/cryptography-challenge-1/
import random, time


# A basic encryption algorithm...

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + character
        for j in range(0, key):
            ciphertext = ciphertext + random.choice(alphabet)
    print('my cephertext:', ciphertext)
    return ciphertext


def decrypt(ciphertext, key):
    decod = ''
    print('plaintext length:', len(ciphertext))
    for h in range(0, len(ciphertext)):
        for g in range(0, key):
            ciphertext = ciphertext[:-1]

        decod += ciphertext[-1]
        ciphertext = ciphertext[:-1]
        print('decod: ', decod)
    return decod


# Main program starts here...
# Input...
plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

# Process...
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)
decode = decrypt(ciphertext, key)
# Output...
print("Ciphertext:")
print(ciphertext)
print('Decoded text:', decode)