
from utils import *

# Exercice 4
# Le CIPHERTEXT suivant a été chiffré par un chiffrement affine à l'aide de la fonction 3𝑥 + 𝑏 pour
# certains 𝑏:
# TCABTIQMFHEQQMRMVMTMAQ
# Décrypter.

CIPHERTEXT = 'TCABTIQMFHEQQMRMVMTMAQ'
alpha_key = 3

print('Exercice4\n')

modular_inverse = mod_inverse(alpha_key, 26)

print('The modular inverse of the alpha key is : ', modular_inverse)

# Brute force attack
words = []
print('\nThe possibilities of plain texts are :')
for beta_key in range(0, 25):
    word = ''
    for character in CIPHERTEXT:
        plain_character_number = get_number_modulo26(modular_inverse * (get_character_number(character) - beta_key))
        word += get_number_character(plain_character_number)
    words.append(word)
    print(beta_key, ' (key) : ', word)

# We can see that the correct answer corresponds to beta_key=14
print('\nThe plain text is : ', words[14])
