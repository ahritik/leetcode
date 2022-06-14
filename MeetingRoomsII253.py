'''
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''
import heapq

def minMeetingRooms(intervals) -> int:
    intervals.sort()
    endHeap = []
    
    for start, end in intervals:
        if endHeap and start >= endHeap[0]:
            heapq.heappop(endHeap)
        heapq.heappush(endHeap, end)

    return len(endHeap)