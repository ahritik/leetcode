"""
1832. Check If The Sentence Is Panagram

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

def checkIfPangram(self, sentence: str) -> bool:
    return 26 == [letter in sentence for letter in "qwertyuiopasdfghjklzxcvbnm"].count(True)
    