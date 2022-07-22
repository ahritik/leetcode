"""
1221. Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""

def balancedStringSplit(s):
    def checkSides(right, left):
        return right.count("R") == left.count("R") and right.count("L") == left.count("L")
    
    count = 1
    for i in range(1,len(s)):
        if checkSides(s[:i],s[i:]): count += 1
    return count
