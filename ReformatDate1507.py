'''
1507. Reformat Date

Given a date string in the form Day Month Year, where:
Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:
YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
'''
import re

def reformatDate(date) -> str:

    months = {
        "Jan": "01", 
        "Feb": "02", 
        "Mar": "03", 
        "Apr": "04", 
        "May": "05", 
        "Jun": "06", 
        "Jul": "07", 
        "Aug": "08", 
        "Sep": "09", 
        "Oct": "10", 
        "Nov": "11", 
        "Dec": "12"
    }

    date = date.split()
    if len(date) != 3:
        return

    day = re.sub('[^0-9]','', date[0])
    
    if len(day) == 1:
        day = "0" + day
    
    return date[2] + "-" + months[date[1]] + "-" + day

print("Input: 20th Oct 2052   Output:",reformatDate("20th Oct 2052"))
print("Input: 6th Jun 1933    Output:",reformatDate("6th Jun 1933"))
print("Input: 26th May 1960   Output:",reformatDate("26th May 1960"))