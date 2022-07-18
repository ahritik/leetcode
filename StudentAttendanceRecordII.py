'''
552. Student Attendance Record II

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. 
The record only contains the following three characters:
	'A': Absent.
	'L': Late.
	'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:
	The student was absent ('A') for strictly fewer than 2 days total.
	The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. 
The answer may be very large, so return it modulo 109 + 7.

'''

def checkRecord(int n):
	