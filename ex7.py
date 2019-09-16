
from utils import *
import numpy as np
import math

# Exercice 7
# Ce qui suit est le CIPHERTEXT d'un chiffrement de Hill
# ZIRKZWOPJJOPTFAPUHFHADRQ
# en utilisant la matrice
# (1 2 3 4)
# (4 3 2 1)
# (11 2 4 6)
# (2 9 6 4)
# Décrypter

CIPHERTEXT = 'ZIRKZWOPJJOPTFAPUHFHADRQ'

print('Exercice4\n')

CIPHER_MATRIX = np.array([
    [1,2,3,4],
    [4,3,2,1],
    [11,2,4,6],
    [2,9,6,4]])

# Build vectors of length 4 from the CIPHERTEXT
vectors_length = len(CIPHER_MATRIX)
number_of_vectors = math.ceil(len(CIPHERTEXT) / vectors_length)
vectors = [None] * number_of_vectors

for index in range(0,len(vectors)):
    vectors[index] = np.zeros(4)

# Fill in the vectors with the cipher text
for index,character in enumerate(CIPHERTEXT):
    vector_index = index//vectors_length
    character_index = index%vectors_length
    vectors[vector_index][character_index] = get_character_number(character)

print('Here are the vectors that we must decipher : ')
for vector in vectors:
    print(vector)

cipher_matrix_determinant = round(np.linalg.det(CIPHER_MATRIX))
print('\nThe determinant of the cipher matrix is : ', cipher_matrix_determinant)

modular_inverse = mod_inverse(round(cipher_matrix_determinant), 26)
print('\nThe modular inverse of the determinant is : ',  modular_inverse)

# for some reason, linalg.inv does not give the correct inverse
INVERSE_MATRIX = np.linalg.inv(CIPHER_MATRIX)
print('\nHere is the inverse of the cipher matrix : ')
print(INVERSE_MATRIX)

print('\n')





### Debug code and stuff i tried

#dat_matrix = INVERSE_MATRIX * modular_inverse / cipher_matrix_determinant

#print(INVERSE_MATRIX.dot(CIPHER_MATRIX))
#print(CIPHER_MATRIX.dot(INVERSE_MATRIX))

#print('\n')
#print(dat_matrix)

dat_inv = (1/55) * np.array([
    [-8,2,5,0],
    [-86,-116,440,55],
    [185,270,95,-110],
    [-80,145,50,55]])

print('\n')
print(dat_inv)

my_matrix = dat_inv * modular_inverse / cipher_matrix_determinant

print(my_matrix)

res = vectors[0].dot(my_matrix)

for i in range(0,len(res)):
    res[i] = get_number_modulo26(round(res[i]))
    #print(type(res[i]), ' : ', res[i])
    print(get_number_character(int(res[i])))
print(res)