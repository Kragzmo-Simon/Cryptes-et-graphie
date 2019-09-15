
from utils import *

# Exercice 6
# Les éléments suivants ont été chiffrés à l’aide de la méthode Vigenère, à l’aide d’une clé d’une longueur
# maximale de 6.
# XKJUROWMLLPXWZNPIMBVBQJCNOWXPCCHHVVFVSLLFVXHAZITYX
# OHULXQOJAXELXZXMYJAQFSTSRULHHUCDSKBXKNJQIDALLPQALL
# UHIAQFPBPCIDSVCIHWHWEWTHBTXRLJNRSNCIHUVFFUXVOUKJLJ
# SWMAQFVJWJSDYLJOGJXDBOXAJULTUCPZMPLIWMLUBZXVOODYBA
# FDSKXGQFADSHXNXEHSARUOJAQFPFKNDHSAAFVULLUWTAQFRUPW
# JRSZXGPFUTJQIYNRXNYNTWMHCUKJFBIRZSMEHHSJSHYONDDZZN
# TZMPLILRWNMWMLVURYONTHUHABWNVW

CYPHERTEXT = 'XKJUROWMLLPXWZNPIMBVBQJCNOWXPCCHHVVFVSLLFVXHAZITYXOHULXQOJAXELXZXMYJAQFSTSRULHHUCDSKBXKNJQIDALLPQALLUHIAQFPBPCIDSVCIHWHWEWTHBTXRLJNRSNCIHUVFFUXVOUKJLJSWMAQFVJWJSDYLJOGJXDBOXAJULTUCPZMPLIWMLUBZXVOODYBAFDSKXGQFADSHXNXEHSARUOJAQFPFKNDHSAAFVULLUWTAQFRUPWJRSZXGPFUTJQIYNRXNYNTWMHCUKJFBIRZSMEHHSJSHYONDDZZNTZMPLILRWNMWMLVURYONTHUHABWNVW'

indexes = []
coincidences_counts = [] #store the number of coincidence for a shift between the base message and the shifted mesage
for shifting_index in range(1,7):
    coincidences_count = compare_text_shifting_coincidences(CYPHERTEXT, shifting_index)
    indexes.append(shifting_index)
    coincidences_counts.append(coincidences_count)
    print('For a shift of ', shifting_index, ', we have ', coincidences_count, ' coincidences')

# therefore we can deduce that the vector has a length of 5
max_coincidences = max(coincidences_counts)
vector_length = indexes[coincidences_counts.index(max_coincidences)] #length of the key
print('The vector length is : ', vector_length)

# We divide the cyphertext into different texts so that each text corresponds to a specific key
# of the vector used to cypher the full text
words = []
for i in range(0, vector_length):
    word = ''
    words.append(word)
for index in range(0, len(CYPHERTEXT)):
    for word_index in range(0, vector_length):
        if index%vector_length == word_index:
            words[word_index] += CYPHERTEXT[index]

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

#we build the vectors
vectors=[[]]
for x in expected_e:
    t = []
    for y in x:
        for i in vectors:
            t.append(i+[y])
    vectors = t

# We can expect that:
#   F is the cyphertext of E for the first key because it is the most frequent letter
#   H is the cyphertext of E for the second key
#   J is the cyphertext of E for the third key
#   L is the cyphertext of E for the fourth key
#   N is the cyphertext of E for the fifth key
for vector in vectors :
    for i, x in enumerate(vector) :
        vector[i] = get_character_number('E') - get_character_number(vector[i])
print("la cle est : ")
print(vectors)

#we decode the message :
print("Message decode : ")
for vector in vectors :
    message=[]
    for indice, letter in enumerate(CYPHERTEXT):
        message.append( get_number_character(  (get_character_number(letter) + vector[indice%(len(vector))])%26 )  )
    print(message)


