'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

def mergeIntervals(intervals):
    merged = []

    for interval in sorted(intervals):
      if len(merged)==0 or merged[-1][1] < interval[0]:
        merged.append(interval)
      else:
        merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

print("Input: [[1,3],[2,6],[8,10],[15,18]] Output:",mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
print("Input: [[1,4],[4,5]]                Output:",mergeIntervals([[1,4],[4,5]]))