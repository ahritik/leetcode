"""
2224. Minimum Number of Operations to Convert Time

You are given two strings current and correct representing two 24-hour times.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.
Return the minimum number of operations needed to convert current to correct.
"""

def minOperations(current, correct):
    currTime = current.split(':')
    correctTime = correct.split(':')
    currTime = int(currTime[0])*60 + int(currTime[1])
    correctTime = int(correctTime[0])*60 + int(correctTime[1])
    minutes = abs(correctTime - currTime)

    operations = 0
    operations += minutes // 60
    minutes = minutes % 60
    operations += minutes // 15
    minutes = minutes % 15
    operations += minutes // 5
    minutes = minutes % 5

    return operations+minutes

print("Input: current = \"02:30\", correct = \"04:35\"   Output:",minOperations(current = "02:30", correct = "04:35"))
print("Input: current = \"11:00\", correct = \"11:01\"   Output:",minOperations(current = "11:00", correct = "11:01"))