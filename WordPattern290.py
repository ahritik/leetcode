"""
290. Word Patterm

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words): return False
    patternDict = {}

    for i in range(len(pattern)):
        if pattern[i] not in patternDict:
            if words[i] in patternDict.values():
                return False
            patternDict[pattern[i]] = words[i]
        elif patternDict[pattern[i]] != words[i]:
            return False
    return True

