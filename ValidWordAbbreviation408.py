'''
408. Valid Word AbbreviationA string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):
    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)
The following are not valid abbreviations:
    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)
    Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
A substring is a contiguous non-empty sequence of characters within a string.
'''

def wordAbbreviation(word, abbr) -> bool:
    wordLength, digit = 0, 0
    for character in abbr:
        if character.isdigit():
            if digit == 0 and character == '0':
                return False
            digit = digit*10 + int(character)
        else:
            if digit != 0:
                wordLength += digit
                digit = 0
            if wordLength >= len(word) or word[wordLength] != character:
                return False
            wordLength += 1
    if digit != 0:
        wordLength += digit

    return wordLength == len(word)

print("Input: internationalization, i12iz4n Output:",wordAbbreviation("internationalization", "i12iz4n"))
print("Input: apple, a2e                    Output:",wordAbbreviation("apple", "a2e"))