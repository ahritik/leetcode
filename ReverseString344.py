"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

def reverseString(str):
    left = 0
    right = len(str) - 1

    while left < right:
      str[left], str[right] = str[right], str[left]
      left += 1
      right -= 1
