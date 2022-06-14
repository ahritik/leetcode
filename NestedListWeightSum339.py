'''
339. Nested List Weight Sum

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.
'''

def weightNestedSum(nums, layer=1):
    sum = 0
    for i in nums:
        if type(i) == list:
            sum += weightNestedSum(i, layer+1)
        else:
            sum += i
    return sum * layer

