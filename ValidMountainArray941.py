"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

def isValidMountain(arr):
    if len(arr) < 3:
        return False
    
    i, j = 0, len(arr) - 1
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    while j >= 0 and arr[j] < arr[j - 1]:
        j -= 1
    return i == j and i != 0 and j != len(arr) - 1