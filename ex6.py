
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

CIPHERTEXT = 'XKJUROWMLLPXWZNPIMBVBQJCNOWXPCCHHVVFVSLLFVXHAZITYXOHULXQOJAXELXZXMYJAQFSTSRULHHUCDSKBXKNJQIDALLPQALLUHIAQFPBPCIDSVCIHWHWEWTHBTXRLJNRSNCIHUVFFUXVOUKJLJSWMAQFVJWJSDYLJOGJXDBOXAJULTUCPZMPLIWMLUBZXVOODYBAFDSKXGQFADSHXNXEHSARUOJAQFPFKNDHSAAFVULLUWTAQFRUPWJRSZXGPFUTJQIYNRXNYNTWMHCUKJFBIRZSMEHHSJSHYONDDZZNTZMPLILRWNMWMLVURYONTHUHABWNVW'

indexes = []
coincidences_counts = [] #store the number of coincidence for a shift between the base message and the shifted mesage
for shifting_index in range(1,7):
    coincidences_count = compare_text_shifting_coincidences(CIPHERTEXT, shifting_index)
    indexes.append(shifting_index)
    coincidences_counts.append(coincidences_count)
    print('For a shift of ', shifting_index, ', we have ', coincidences_count, ' coincidences')

# therefore we can deduce that the vector has a length of 5
max_coincidences = max(coincidences_counts)
vector_length = indexes[coincidences_counts.index(max_coincidences)] #length of the key
print('The vector length is : ', vector_length)

# We divide the ciphertext into different texts so that each text corresponds to a specific key
# of the vector used to cipher the full text
# For instance, if the key is 5, the first vector will contain the 1st letter, the 6th, the 11th, etc.
# The second vector will contain the 2nd, 7th, 12th, etc. letters.
words = []
for i in range(0, vector_length):
    word = ''
    words.append(word)
for index in range(0, len(CIPHERTEXT)):
    for word_index in range(0, vector_length):
        if index%vector_length == word_index:
            words[word_index] += CIPHERTEXT[index]

most_frequent_characters = []

for word in words:
    print('For the word : ', word, ' we have these frequencies : ')
    frequency_display = ''
    characters_and_frequencies = get_characters_frequency(word)
    characters = characters_and_frequencies[0]
    frequencies = characters_and_frequencies[1]

    for index in range(0, len(characters)):
        frequency_display += characters[index] + ' : ' + str(frequencies[index]) + '  ;  '
    # found indices for maximum in frequencies :
    most_frequent_characters.append([x for i, x in enumerate(characters) if frequencies[i] == max(frequencies)])
    print(frequency_display)

display_most_frequent_characters(most_frequent_characters)

# We build the vectors that contains the most frequent characters
vectors=[[]]
for most_common_characters_combination in most_frequent_characters:
    solution = []
    for character in most_common_characters_combination:
        for i in vectors:
            solution.append(i+[character])
    vectors = solution

# We can expect that:
#   F is the ciphertext of E for the first key because it is the most frequent letter
#   H is the ciphertext of E for the second key
#   J is the ciphertext of E for the third key
#   L is the ciphertext of E for the fourth key
#   N is the ciphertext of E for the fifth key
for vector in vectors :
    for i, x in enumerate(vector) :
        vector[i] = get_character_number('E') - get_character_number(vector[i])
print("\nThe key vector is : ")
print(vectors)

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



