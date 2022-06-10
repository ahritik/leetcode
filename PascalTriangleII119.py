'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
'''

def pascalTriangle(rowIndex):
    if(rowIndex == 0):
        return [1]
    
    output = [[1]*i for i in range(1,rowIndex+2)]
    
    for i in range(2,rowIndex+1):
        for j in range(1,i):
            output[i][j] = output[i-1][j-1] + output[i-1][j]

    return output[-1]

print(pascalTriangle(8))