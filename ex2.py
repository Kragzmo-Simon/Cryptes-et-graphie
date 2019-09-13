
from utils import *

# Exercice 2
# Le CIPHERTEXT suivant était la sortie d'un chiffrement par décalage :
# LCLLEWLJAZLNNZMVYIYLHRMHZA
# En effectuant un compte de fréquence, devinez la clé utilisée dans le chiffrement. Utilisez l'ordinateur
# pour tester votre hypothèse. Quel est le texte en clair déchiffré ?

CYPHERTEXT = 'LCLLEWLJAZLNNZMVYIYLHRMHZA'

print('Exercice 2\n')

characters_and_frequencies = get_characters_frequency(CYPHERTEXT)
characters = characters_and_frequencies[0]
frequencies = characters_and_frequencies[1]

for index in range(0, len(characters)):
    print(characters[index], ' : ', frequencies[index])

# The most frequent character is 'L', thus we can suppose that the plain text of L is E
# Therefore, we can deduce the key and translate the rest of the word

key = ord('L') - ord('E')

print('The decypher key is : ', key)

word = ''
for character in CYPHERTEXT:
    word += character_shift(character, -key)

print("The translation of the cypher text is : ", word)
