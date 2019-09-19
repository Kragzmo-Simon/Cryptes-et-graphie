
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

"""
Step 1 : calculate the key length
"""

indexes = []
coincidences_counts = [] #store the number of coincidence for a shift between the base message and the shifted message
for shifting_index in range(1,7):
    coincidences_count = compare_text_shifting_coincidences(CIPHERTEXT, shifting_index)
    indexes.append(shifting_index)
    coincidences_counts.append(coincidences_count)
    print('For a shift of ', shifting_index, ', we have ', coincidences_count, ' coincidences')

# therefore we can deduce that the vector has a length of 4
max_coincidences = max(coincidences_counts)
vector_length = indexes[coincidences_counts.index(max_coincidences)] #length of the key
print('\nTherefore, the vector length is : ', vector_length)

# We tried an attack based on the frequency of the letters but it did not work.
# Thus, we use a brute force attack.

"""
Step 2 : build all shift combinations
"""

shifting_key_combinations = [[]]
for step in range(0,vector_length):
    solution = []
    for index in range(1,26):   # we expect a shift to be non-zero
        for preceding_shift in shifting_key_combinations:
            solution.append(preceding_shift+[index])
    shifting_key_combinations = solution

"""
Step 3 : Decipher
"""

number_of_combinations = len(shifting_key_combinations)
progress_percentage_step = 2
progress_step = get_progress_step(number_of_combinations, progress_percentage_step)
print('\nBrute force attack (it\'s very slow though (~few mins))')
for key_number, shifting_key in enumerate(shifting_key_combinations):
    PLAINTEXT = ''
    for index, letter in enumerate(CIPHERTEXT):
        PLAINTEXT += get_number_character(  (get_character_number(letter) + shifting_key[index%vector_length])%26 )

    # We tested if the plain text contained a combination of common such as 'THIS', 'THAT', 'AND' or 'YOU'.
    # The two following sentences are just to show only the two solutions when we had found them
    if 'UPONTHISBASIS' in PLAINTEXT or 'ITISASTORYABOUT' in PLAINTEXT:
        print('\nOne solution may be : ', shifting_key)
        print(PLAINTEXT)

    if key_number%progress_step == 0:
        print('Progress : ', (key_number//progress_step) * progress_percentage_step, '% finished')

#SOLUTION1 = 'UPONTHISBASISIAMGOINGTOSHOWYOUHOWABUNCHOFBRIGHTYOUNGFOLKSDIDFINDACHAMPIONAMANWITHBOYSANDGIRLSOFHISWWNAMANOFSODOMINATINGANDHAPPYINDIVIDUALITYTHATYOUTHISMBMBOPXWHBIWNBVZTUEONVWOMCEKGJJWNBIHJSOOWPKHVTCOGMJCROYHDTDCOBWCNTYDTZQFIOEFDTYHVEHMHPDCOPDCPTQQXPKBOGKZGPVGPDXQPTJCHBHMAJBZDOIONSEAVOJWXNECIMYUCUSONUYBBNKFFZIVVEEKNEEKIBBCIHMWIEYBBDEIIUHMMPQR'
#SOLUTION2 = 'TZASSRUXAKENRSMRFYUSFDAXGYIDNETTVKNZMMTTELDNFRFDNEZLEYXPRNUIESZIZMTFLZUTMKYFMGUYGLADRKZIFSDQRYRMHCIBMKYFMYRXNNARHXMYHXSFMNTFOZKNMNUAHNGFKSFDSRMYXYGYGSERAWNTOHIMASISAFLYTOASUGARBOWLITISASTORYABOUTASMALLTOWNITISNOTAGOSSIPYYARNNORISITADRYMONOTONOUSACCOUNTFULLOFSUCHCUSTOMARYFILLINSASROMANTICMOONLIGHTCASTINGMURKYSHADOWSDOWNALONGWINDINGCOUNTRYROAD'

# There is two key for this text : (12,22,8,13) and (13,12,22,8). It's because there is a missing letter in the middle of the text.
# The plaintext also contain no 'e', which means the decoding method based on frequency won't work as it use the frequency of the 'e'
# letter to work.T and A are the next most frequent letter in english, but they're rather close in frequency, which is
# why using only one of those instead of E in the code doesn't work either.
# We can decode the message using common words that are used in english to detect which solution is the actual plaintext.
# We used this website as well to help us figure out why frequency didn't work :
# https://www.boxentriq.com/code-breaking/vigenere-cipher

# If we place a letter in the middle of the text, we can restore the original plaintext

print('\nWhen adding a letter in the middle of the text to counter the shifting of the message, we get the following plain text : ')
#                                                                                                                                                                    V = added letter
CIPHERTEXT = 'HDSFGVMKOOWAFWEETCMFTHSKUCAQBILGJOFMAQLGSPVATVXQBIRYSCPCFRMVSWRVNQLSZDMGAOQSAKMLUPSQFORVTWVDFCJZVGAOAOQSACJKBRSEVBELVBKSARLSCDCAARMNVRYSYWXQGVELLCYLUWWVEOAFGCLAZOWAFOJDLHSSFIKSEPSOYWXAFOWLBFCSOCYLNGQSYZXGJBMLVGRGGOKGFGMHLMEJABSJVGMLNRVQZCRGGCRGHGEUPCYFGTYDYCJKHQLUHGXGZOVQSWPDVBWSFFSENBXAPASGAZMYUHGSFHMFTAYJXMWZNRSOFRSOAOPGAUAAARMFTQSMAHVQECEV'
PLAINTEXT = ''
shifting_key = [13,12,22,8]
for index, letter in enumerate(CIPHERTEXT):
    PLAINTEXT += get_number_character(  (get_character_number(letter) + shifting_key[index%vector_length])%26 )
print(PLAINTEXT)
