
alphabet_lower_bound = ord('A')
alphabet_upper_bound = ord('Z')

def get_character_number(character):
    # Returns the letter rank in the alphabet (A=0, B=1, etc.)
    return ord(character.upper())-ord('A')

def get_number_character(number):
    # Returns the caracter corresponding to the character
    return chr(number + ord('A'))

def character_shift(character, index):
    # shifts the character a number of times equal to index
    # index signs allow for shifting towards both directions
    a = ord(character) + index
    while a < alphabet_lower_bound:
        a += 26
    while alphabet_upper_bound < a:
        a -= 26

    return chr(a)

def get_number_modulo26(number):
    while number < 0:
        number += 26
    while 25 < number:
        number -= 26
    return number

def get_characters_frequency(word):
    # builds an array containing each letter in the word/sentence and its frequency
    characters = []
    frequencies = []
    for character in word:
        if character not in characters:
            characters.append(character)
            frequencies.append(1)
        else:
            frequencies[characters.index(character)] += 1

    return [characters, frequencies]

def mod_inverse(a, modulo) : 
    a = a % modulo; 
    for x in range(1, modulo) : 
        if ((a * x) % modulo == 1) : 
            return x 
    return 1

def compare_text_shifting_coincidences(cyphertext, shifting_index):
    coincidences_count = 0
    for index in range(0, len(cyphertext)-shifting_index):
        #print(index, ' : ', cyphertext[index], ' / ', cyphertext[index-shifting_index])
        if cyphertext[index] == cyphertext[index-shifting_index]:
            coincidences_count += 1
    return coincidences_count



