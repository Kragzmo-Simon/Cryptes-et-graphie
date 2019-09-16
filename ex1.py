
from utils import *

# Exercice 1
# Le CIPHERTEXT suivant a été chiffré par un chiffrement à décalage :
# YCVEJQWVHQTDTWVWU.
# Décrypter.

CIPHERTEXT = 'YCVEJQWVHQTDTWVWU'

print('Exercice 1\n')

words = []
for key in range(0,26):
    word = ''
    for character in CIPHERTEXT:
        word += character_shift(character, -key)
    words.append(word)
    print(key,' (key) : ',word)

# The printing of all the possible sentences lets us deduce that the plain text is 
# WATCHOUTFORBRUTUS with the key being 2
print('The answer is : ', words[2])

