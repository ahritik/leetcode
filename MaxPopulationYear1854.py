'''
1854. Maximum Population Year

You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
The population of some year x is the number of people alive during that year. 
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. 
Note that the person is not counted in the year that they die.
Return the earliest year with the maximum population.
'''

def maxPopYear(logs):
    popByYear={}
    for person in logs:
        for i in range(person[0], person[1]):
            if i not in popByYear:
                popByYear[i]=1
            else:
                popByYear[i] += 1
        
    return sorted([i for i in popByYear.items () if i[1] ==max(popByYear.values()) ])[0][0]