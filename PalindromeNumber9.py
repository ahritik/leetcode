'''
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
'''

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    reverse = 0
    temp = x

    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10

    return reverse == x

print("Input: 121  Output:",isPalindrome(121))
print("Input: -121 Output:",isPalindrome(-121))
print("Input: 10   Output:",isPalindrome(10))