'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def sortedSquares(nums):
    return sorted([n**2 for n in nums])

print("Input: range = [0,1,2,4,5,7]   Output:",sortedSquares([0,1,2,4,5,7]))
print("Input: range = [0,2,3,4,6,8,9] Output:",sortedSquares([0,2,3,4,6,8,9]))
print("Input: range = []              Output:",sortedSquares([]))