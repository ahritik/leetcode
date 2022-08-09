"""
696. Count Binary Substrings

Given a binary string s, return the number of non-empty substrings that have the same number
of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
"""

def countBinarySubstrings(s):
    prev, current, count = 0, 1, 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current += 1
        else:
            prev, current = current, 1
        if prev >= current:
            count += 1
            
    return count
