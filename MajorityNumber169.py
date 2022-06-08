'''
169. Majority Element

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

def majorityElement(self, nums) -> int:
    return sorted(nums)[len(nums)//2]