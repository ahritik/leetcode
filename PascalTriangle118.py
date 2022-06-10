'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

def pascalTriangle(numRows):
    if(numRows == 0):
        return []
    
    output = [[1]*i for i in range(1,numRows+1)]
    
    for i in range(2,numRows):
        for j in range(1,i):
            output[i][j] = output[i-1][j-1] + output[i-1][j]

    return output

print(pascalTriangle(8))