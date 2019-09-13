
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

CYPHERTEXT = 'HDSFGVMKOOWAFWEETCMFTHSKUCAQBILGJOFMAQLGSPVATVXQBIRYSCPCFRMVSWRVNQLSZDMGAOQSAKMLUPSQFORVTWVDFCJZVGAOAOQSACJKBRSEVBELVBKSARLSCDCAARMNVRYSYWXQGVELLCYLUWWEOAFGCLAZOWAFOJDLHSSFIKSEPSOYWXAFOWLBFCSOCYLNGQSYZXGJBMLVGRGGOKGFGMHLMEJABSJVGMLNRVQZCRGGCRGHGEUPCYFGTYDYCJKHQLUHGXGZOVQSWPDVBWSFFSENBXAPASGAZMYUHGSFHMFTAYJXMWZNRSOFRSOAOPGAUAAARMFTQSMAHVQECEV'

print('Exercice 5\n')

indexes = []
coincidences_counts = []
for shifting_index in range(1,7):
    coincidences_count = compare_text_shifting_coincidences(CYPHERTEXT, shifting_index)
    indexes.append(shifting_index)
    coincidences_counts.append(coincidences_count)
    print('For a shift of ', shifting_index, ', we have ', coincidences_count, ' coincidences')

# therefore we can deduce that the vector has a length of 4
max_coincidences = max(coincidences_counts)
vector_length = indexes[coincidences_counts.index(max_coincidences)]
print('The vector length is : ', vector_length)

# We divide the cyphertext into 4 different texts so that each text corresponds to a specific key
# of the vector used to cypher the full text
words = []
for i in range(0, vector_length):
    word = ''
    words.append(word)
for index in range(0, len(CYPHERTEXT)):
    for word_index in range(0, vector_length):
        if index%4 == word_index:
            words[word_index] += CYPHERTEXT[index]

vectors = []
vector = []
vectors.append(vector)
for word in words:
    print('For the word : ', word, ' we have these frequencies : ')
    characters_and_frequencies = get_characters_frequency(word)
    characters = characters_and_frequencies[0]
    frequencies = characters_and_frequencies[1]

    for index in range(0, len(characters)):
        print(characters[index], ' : ', frequencies[index])

    indices = [i for i, x in enumerate(frequencies) if x == max(frequencies)]
    for vector in vectors:
        if len(indices) == 1 :
            vector.append(indices[0])
        else:
            for index in indices :
                
            new_vector = vectors
    vector.append()

# We can expect that:
#   A is the cyphertext of E for the first key because it is the most frequent letter
#   W is the cyphertext of E for the second key
#   S is the cyphertext of E for the first key
#   F or K is the cyphertext of E for the first key
