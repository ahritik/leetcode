"""
2047. Number of Valid Words in a Sentence

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. 
Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
A token is a valid word if all three of the following are true:
    It only contains lowercase letters, hyphens, and/or punctuation (no digits).
    There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
    There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
    Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
Given a string sentence, return the number of valid words in sentence.
"""

def countValidWords(sentence):
    def isValidWord(str):
        if len(str) < 1: return False
        if str.isalpha(): return True
        if "-" in str and ((str[0] == "-" or str[-1]== "-") or str.count("-") > 1): return False
        if "!" in str or "." in str or "," in str:
            if str.count("!") > 1 or str.count(".") > 1 or str.count(",") > 1: return False
            if str[-1] not in "!.," or str[0] not in "!.,": return False
        return True
    
    return [isValidWord(word) for word in sentence.split()].count(True)
    