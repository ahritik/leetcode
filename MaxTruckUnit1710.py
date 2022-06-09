'''
1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
'''

def maximumUnits(boxTypes, truckSize: int) -> int:
    boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
    unitSum = 0
    for num, unit in boxTypes:
        if truckSize >= num:
            truckSize -= num
            unitSum += num*unit
        else:
            return unitSum + truckSize*unit
    return unitSum