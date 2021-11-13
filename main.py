import string
import re

#find the prefix
vowel = 'aeiouy'
consonants = "bcdfghjklmnpqrstvwxz"
punctuation = string.punctuation

# Input test string here
s = 'Hey buddy, get away from my car!'

def vowel_index(string):
    for index, letter in enumerate(string):
        if letter in vowel:
            return index

def prefix(string):
    index = vowel_index(string)
    return string[:index]

def stem(string):
    index = vowel_index(string)
    return string[index:]

def count_consonant(string):
    count = 0
    s = string.lower()
    for letter in s:
        if letter in consonants:
            count += 1
    return count

def translate(string):
    translated = []
    s = re.findall(r"[\w']+|[.,!?;]", string) #split string in spaces and punctuation
    for word in s:
        if word.isalpha():
            consonant_count = count_consonant(word)
            if consonant_count == 0:
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

