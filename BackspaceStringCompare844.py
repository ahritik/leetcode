"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
"""

def backspaceCompare(s, t):
    sString = []
    tString = []

    for i in s:
        if i != "#":  sString.append(i)
        elif sString: sString.pop()
    
    for i in t:
        if i != "#":  tString.append(i)
        elif tString: tString.pop()

    return "".join(sString) == "".join(tString)