'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
'''
from collections import Counter

def unique_occurrences(arr):
    count = Counter(arr)

    return len(count) == len(set(count.values()))

print("Input:[1,2,2,1,1,3]              Output:",unique_occurrences([1,2,2,1,1,3]))
print("Input:[1,2]]                     Output:",unique_occurrences([1,2]))
print("Input:[-3,0,1,-3,1,1,1,-3,10,0]  Output:",unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]))