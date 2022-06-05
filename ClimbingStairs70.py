'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def climbStairs(n) -> int:
    if n == 1:
        return 1
    
    steps = [1, 1] + [0] * (n - 1)

    for i in range(2, n):
        steps[i] = steps[i - 1] + steps[i - 2]

    return steps[n-2] + steps[n-1]

print("Input:3   Output:",climbStairs(3))
print("Input:4   Output:",climbStairs(4))
print("Input:7  Output:",climbStairs(7))