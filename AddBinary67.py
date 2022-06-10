'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
'''


def binaryAdd(a, b):
    output = ""
    aPointer, bPointer = len(a)-1, len(b)-1
    while aPointer and bPointer:
        aPointer +=1 
