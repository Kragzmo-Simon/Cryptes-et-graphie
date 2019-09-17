
from utils import *

# Exercice 5
# Les éléments suivants ont été chiffrés à l’aide de la méthode Vigenère, à l’aide d’une clé d’une longueur
# maximale de 6. Décryptez-le et choisissez ce qui est inhabituel dans le texte en clair. Comment cela at-il affecté les résultats ?
# HDSFGVMKOOWAFWEETCMFTHSKUCAQBILGJOFMAQLGSPVATVXQBIRYSCPCFRMVSWRVNQ
# LSZDMGAOQSAKMLUPSQFORVTWVDFCJZVGAOAOQSACJKBRSEVBELVBKSARLSCDCAARMNV
# RYSYWXQGVELLCYLUWWEOAFGCLAZOWAFOJDLHSSFIKSEPSOYWXAFOWLBFCSOCYLNGQSY
# ZXGJBMLVGRGGOKGFGMHLMEJABSJVGMLNRVQZCRGGCRGHGEUPCYFGTYDYCJKHQLUHGXGZ
# OVQSWPDVBWSFFSENBXAPASGAZMYUHGSFHMFTAYJXMWZNRSOFRSOAOPGAUAAARMFTQS
# MAHVQECEV

CIPHERTEXT = 'HDSFGVMKOOWAFWEETCMFTHSKUCAQBILGJOFMAQLGSPVATVXQBIRYSCPCFRMVSWRVNQLSZDMGAOQSAKMLUPSQFORVTWVDFCJZVGAOAOQSACJKBRSEVBELVBKSARLSCDCAARMNVRYSYWXQGVELLCYLUWWEOAFGCLAZOWAFOJDLHSSFIKSEPSOYWXAFOWLBFCSOCYLNGQSYZXGJBMLVGRGGOKGFGMHLMEJABSJVGMLNRVQZCRGGCRGHGEUPCYFGTYDYCJKHQLUHGXGZOVQSWPDVBWSFFSENBXAPASGAZMYUHGSFHMFTAYJXMWZNRSOFRSOAOPGAUAAARMFTQSMAHVQECEV'

indexes = []
coincidences_counts = [] #store the number of coincidence for a shift between the base message and the shifted mesage
for shifting_index in range(1,7):
    coincidences_count = compare_text_shifting_coincidences(CIPHERTEXT, shifting_index)
    indexes.append(shifting_index)
    coincidences_counts.append(coincidences_count)
    print('For a shift of ', shifting_index, ', we have ', coincidences_count, ' coincidences')

# therefore we can deduce that the vector has a length of 4
max_coincidences = max(coincidences_counts)
vector_length = indexes[coincidences_counts.index(max_coincidences)] #length of the key
print('The vector length is : ', vector_length)

# We divide the ciphertext into different texts so that each text corresponds to a specific key
# of the vector used to cipher the full text
words = []
for i in range(0, vector_length):
    word = ''
    words.append(word)
for index in range(0, len(CIPHERTEXT)):
    for word_index in range(0, vector_length):
        if index%vector_length == word_index:
            words[word_index] += CIPHERTEXT[index]

expected_e = []

for word in words:
    print('For the word : ', word, ' we have these frequencies : ')
    characters_and_frequencies = get_characters_frequency(word)
    characters = characters_and_frequencies[0]
    frequencies = characters_and_frequencies[1]

    for index in range(0, len(characters)):
        print(characters[index], ' : ', frequencies[index])
    # found indices for maximum in frequencies :
    expected_e.append([x for i, x in enumerate(characters) if frequencies[i] == max(frequencies)])
    #print([i for i, x in enumerate(frequencies) if x == max(frequencies)])

#we build the vectors
vectors=[[]]
for x in expected_e:
    t = []
    for y in x:
        for i in vectors:
            t.append(i+[y])
    vectors = t

# We can expect that:
#   A is the ciphertext of E for the first key because it is the most frequent letter
#   W is the ciphertext of E for the second key
#   S is the ciphertext of E for the first key
#   F or A is the ciphertext of E for the first key
print("\nThe key vector is : ")
print(vectors)
for vector in vectors :
    for i, x in enumerate(vector) :
        vector[i] = get_character_number('A') - get_character_number(vector[i])
print("\nThe key vector is : ")
print(vectors)

vectors.append([-get_character_number('N'),-get_character_number('O'),
                -get_character_number('E'),-get_character_number('S')])

# We decode the message :
for vector in vectors :
    print("\nA solution for the plain text is : ")
    message=[]
    PLAINTEXT = ''
    for indice, letter in enumerate(CIPHERTEXT):
        message.append( get_number_character(  (get_character_number(letter) + vector[indice%(len(vector))])%26 )  )
        PLAINTEXT += get_number_character(  (get_character_number(letter) + vector[indice%(len(vector))])%26 )
    #print(message)
    print(PLAINTEXT)

# There is two key for this text : noes and oesn. It's because there is a missing letter in the middle of the text.
# The plaintext also contain no e, which means the decoding method use above won't work as it use the frequency of this
# letter to work.T and A are the next most frequent letter in english, but they're rather close in frequency, which is
# why using one of those instead of E in the code doesn't work either.
# We can decode the cypher using a brute force attack with a dictionary based score for each possibility.
# The possibility containing the most word according to the dictionary should be the plaintext.
# langage will be the good one.
# Using this website to found the key :
# https://www.boxentriq.com/code-breaking/vigenere-cipher
