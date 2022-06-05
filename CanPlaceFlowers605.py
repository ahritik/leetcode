'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

def canPlaceFlowers(flowerbed, n: int) -> bool:
    if n == 0: 
        return True
    flowerbed = [0] + flowerbed + [0]
    
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i] == 1:
            continue
        elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
            n-=1
            flowerbed[i] = 1
            if n == 0:
                return True
    
    return False

print("Input: flowerbed = [1,0,0,0,1], n = 1 Output:",canPlaceFlowers([1,0,0,0,1], 1))
print("Input: flowerbed = [1,0,0,0,1], n = 2 Output:",canPlaceFlowers([1,0,0,0,1], 2))
print("Input: flowerbed = [], n = 2          Output:",canPlaceFlowers([], 2))