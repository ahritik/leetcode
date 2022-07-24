"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary diagonal.
"""

def diagonalSum(mat):
        length = len(mat)
        return sum([mat[i][i] if length-i-1 == i else mat[i][i] + mat[i][length-i-1] for i in range(length)])