'''
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.
'''

def lastStoneWeight(stones):
    while (len(stones) > 1):
        
        max1 = max(stones)
        stones.remove(max1)
        
        max2 = max(stones)
        stones.remove(max2)
        
        if max1 - max2 != 0:
            stones.append(max1 - max2)
        
    if (len(stones) == 1):            
        return stones[0]
    
    return 0

print("Input: range = [1,2,4,5,7]   Output:",lastStoneWeight([1,2,4,5,7]))
print("Input: range = [2,3,4,6,8,9] Output:",lastStoneWeight([2,3,4,6,8,9]))
print("Input: range = []              Output:",lastStoneWeight([]))