# Pig Latin Translator
## Description

An ancient language was recently uncovered which appears to be a close English language
derivative. A group of researchers requires a program to translate English into this ancient text.
The rules to translate any sentence in English to this foregin language are listed below.

### Translation rules

- If a word has no letters, don't translate it.  
- All punctuation should be preserved.  
- If the word begins with a capital letter, then the translated word should too.   

- Separate each word into two parts. The first part is called the “prefix” and extends from
the beginning of the word up to, but not including, the first vowel. (The letter “y” will be
considered a vowel.) The Rest of the word is called the “stem.”

- The translated text is formed by reversing the order of the prefix and stem and adding the
letters “ay” to the end. For example, “sandwich” is composed of “s” + “andwich” + “ay” +
“.” and would translate to “andwichsay.”

- If the word contains no consonants, let the prefix be empty and the word be the stem.
The word ending should be “yay” instead of merely “ay.” For example, “I” would be
“Iyay.”
