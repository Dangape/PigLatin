import string
import re

#find the prefix
vowel = 'aeiouy'
consonants = "bcdfghjklmnpqrstvwxz"
punctuation = string.punctuation

# Input test string here
s = 'Hey buddy, get away from my car!'

# function to find all vowel indexes in a word
def vowel_index(string):
    for index, letter in enumerate(string):
        if letter in vowel:
            return index

# function to find word´s prefix
def prefix(string):
    index = vowel_index(string)
    return string[:index]

# function to find word´s stem
def stem(string):
    index = vowel_index(string)
    return string[index:]

# function to count consonants
def count_consonant(string):
    count = 0
    s = string.lower()
    for letter in s:
        if letter in consonants:
            count += 1
    return count

# function to translate word
def translate(string):
    translated = []
    s = re.findall(r"[\w']+|[.,!?;]", string) #split string in spaces and punctuation
    for word in s:
        if word.isalpha(): #check if word contains only letters
            consonant_count = count_consonant(word)
            if consonant_count == 0: # word only contains consonants
                pref = ''
                st = stem(word)
                translated_string = st + pref + 'yay'
                translated.append(translated_string)
            else:
                if word[0].isupper():
                    word = word.lower()
                    pref = prefix(word)
                    st = stem(word)
                    translated_string = st + pref + 'ay'
                    translated.append(translated_string[0].upper() + translated_string[1:])
                else:
                    word = word.lower()
                    pref = prefix(word)
                    st = stem(word)
                    translated_string = st + pref + 'ay'
                    translated.append(translated_string)
        else:
            translated.append(word)
    return ' '.join(translated)

print(translate(s))

