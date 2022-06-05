'''
1762. Buildings With an Ocean View

There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions.
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''
def findBuildings(heights):
    validBuildings = []
    for i, building in enumerate(heights):
        while len(validBuildings)!=0 and heights[validBuildings[-1]] <= building:
            validBuildings.pop()
        validBuildings.append(i)
    return validBuildings

print("Input:[4,2,3,1]  Output:",findBuildings([4,2,3,1]))
print("Input:[4,3,2,1]  Output:",findBuildings([4,3,2,1]))
print("Input:[1,3,2,4]  Output:",findBuildings([1,3,2,4]))