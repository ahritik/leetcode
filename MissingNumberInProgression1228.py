"""
1228. Missing Number In Arithmetic Progression

In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
A value from arr was removed that was not the first or last value in the array.
Given arr, return the removed value.
"""

def missingNumber(arr):
    arrSum = sum(arr)
    changes = min([abs(arr[i]-arr[i-1]) for i in range(1,len(arr))])
    sumRange = sum(range(1, len(arr) + changes))
    return sumRange - arrSum
    