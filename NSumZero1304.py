"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

def sumZero(n):
    ans=[]
    for i in range(1,n//2+1):
        ans.append(i)
        ans.append(-i)
    if n % 2 !=0: ans.append(0)
        
    return ans