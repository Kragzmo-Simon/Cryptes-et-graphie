
from utils import *

# Exercice 4
# Le CIPHERTEXT suivant a été chiffré par un chiffrement affine à l'aide de la fonction 3𝑥 + 𝑏 pour
# certains 𝑏:
# TCABTIQMFHEQQMRMVMTMAQ
# Décrypter.

CYPHERTEXT = 'TCABTIQMFHEQQMRMVMTMAQ'
alpha_key = 3

print('Exercice4\n')

modular_inverse = mod_inverse(alpha_key, 26)

print(modular_inverse)

for beta_key in range(0, 25):
    word = ''
    for character in CYPHERTEXT:
        plain_character_number = get_number_modulo26(modular_inverse * (get_character_number(character) - beta_key))
        word += get_number_character(plain_character_number)

    print(beta_key, ' (key) : ', word)

# answer is TWENTYSIXPOSSIBILITIES and the key is 14
