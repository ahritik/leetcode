'''
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
'''

def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True