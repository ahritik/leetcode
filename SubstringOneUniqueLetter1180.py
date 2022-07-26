"""
1180. Substring with One Distinct Letter

Given a string s, return the number of substrings that have only one distinct letter.
"""
def countLetters(string):     
    substringCount = 1
    currentLen = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]: currentLen += 1
        else: currentLen = 1
        substringCount += currentLen
        
    return substringCount