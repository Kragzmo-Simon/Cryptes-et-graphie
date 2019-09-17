
from utils import *

# Exercice 3
# Le CIPHERTEXT suivant a été chiffré par un chiffrement affine :
# EDSGICKXHUKLZVEQZVKXWKZUKCVUB
# Les deux premières lettres du texte en clair sont if. Décrypter.

CIPHERTEXT = 'EDSGICKXHUKLZVEQZVKXWKZUKCVUB'

PLAINTEXT = 'IF'

alpha_key = 0
beta_key = 0

# Equations :
# alpha * I + beta = E [26]
# alpha * F + beta = D [26]

print('Exercice 3\n')

# We test for each possible value of the alpha key if there is a beta key that matches
# Once we have both keys, we can decipher easily the cipher text
for alpha in range(0,25):
    first_beta = get_character_number(CIPHERTEXT[0]) - alpha * get_character_number(PLAINTEXT[0])
    second_beta = get_character_number(CIPHERTEXT[1]) - alpha * get_character_number(PLAINTEXT[1])
    if (first_beta-second_beta)%26 == 0:
        alpha_key = alpha
        beta_key = get_number_modulo26(first_beta)

print('The alpha key is : ', alpha_key)
print('The beta key is : ', beta_key)

# alpha key = 9 so we have gcd(9,26)=1

modular_inverse = mod_inverse(alpha_key, 26)

print('The modular inverse of the alpha key is : ', modular_inverse)

# x = mod_inverse * y - mod_inverse * beta [26]

word = ''
for character in CIPHERTEXT:
    plain_character_number = get_number_modulo26(modular_inverse * (get_character_number(character) - beta_key))
    word += get_number_character(plain_character_number)

print('\nThe plain text is : ', word)

