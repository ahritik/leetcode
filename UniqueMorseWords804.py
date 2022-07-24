"""
804. Unique Morse Code Words

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes.
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
"""

def uniqueMorseRepresentations(words):
    
    def morseTranslation(word: str):
        morseDict = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                        "...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = ""
        for letter in word:
            morse += morseDict[ord(letter) - 97]
        return morse
    
    return len(set([morseTranslation(word) for word in words]))