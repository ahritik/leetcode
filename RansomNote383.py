"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(ransomNote, magazine):
    for i in ransomNote:
        if i not in magazine:
            return False
        else:
            magazine = magazine.replace(i, "", 1)
    return True