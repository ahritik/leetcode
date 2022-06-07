'''
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

def isPalindrome(s: str) -> bool:
    
    top, bottom = 0, len(s) - 1
    oneChange = False

    while top < bottom:
        print("\ntop points to:   ", s[top])
        print("bottom points to:", s[bottom])
        if s[top] == s[bottom]:
            top += 1
            bottom -= 1
        elif s[top] == s[bottom-1] and not oneChange:
            oneChange = True
            top += 1
            bottom -= 2
        elif s[top] == s[bottom-1] and not oneChange:
            oneChange = True
            top += 2
            bottom -= 1
        else:
            return False
        print("one change:",oneChange)

    return True

print("Input: aba          Output:",isPalindrome("aba"))
print("Input: abbca         Output:",isPalindrome("abbca"))
print("Input: abca          Output:",isPalindrome("abca"))
print("Input: hitik         Output:",isPalindrome("hitik"))
print("Input: ab         Output:",isPalindrome("ab"))
