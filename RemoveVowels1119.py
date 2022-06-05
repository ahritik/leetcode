'''
1119. Remove Vowels from a String

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
'''

def remove_vowels(s):
    noVowels = ""

    for letter in s:
        if letter not in ['a', 'e', 'i', 'o', 'u']:
            noVowels += letter

    return noVowels


print("Input: leetcodeisacommunityforcoders   Output:",remove_vowels("leetcodeisacommunityforcoders"))
print("Input: aeiou                           Output:",remove_vowels("aeiou"))
print("Input: hritik                          Output:",remove_vowels("hritik"))