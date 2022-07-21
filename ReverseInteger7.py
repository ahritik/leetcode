"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

def reverse(self, x: int) -> int:
    rev = 0
    sign = -1 if x < 0 else 1
    x *= rev

    while x:
      rev = rev * 10 + x % 10
      x //= 10

    return sign * rev