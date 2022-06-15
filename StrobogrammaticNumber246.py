'''
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
'''

def ifStrobogrammatic(num):

    for i in range((len(num) + 1) // 2):
        left = num[i]
        right = num[len(num) - 1 - i]
        if left == right == '0':
            pass
        elif left == right == '1':
            pass
        elif left == right == '8':
            pass
        elif (left == '6' and right == '9') or (left == '9' and right == '6'):
            pass
        else:
            return False

    return True