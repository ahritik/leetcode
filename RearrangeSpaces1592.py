"""
1592. Rearrange Spaces Between Words

You are given a string text of words that are placed among some number of spaces. 
Each word consists of one or more lowercase English letters and are separated by at least one space. 
It's guaranteed that text contains at least one word.
Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. 
If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
Return the string after rearranging the spaces.
"""

def RearrangeSpaces(text):
    words = text.strip().split()
    spaces = text.count(" ")
    if spaces == 0:
        return text
    if len(words) == 1:
        return words[0] + " " * spaces
    
    final = spaces % (len(words) - 1)
    output = ""
    for i in range(len(words)):
        output += words[i]
        if i == len(words) - 1:
            output += " " * final
        else:
            output += " " * (spaces // (len(words) - 1))
    return output


print("Input: text = \"  this   is  a sentence \"     Output: |"+RearrangeSpaces("  this   is  a sentence ")+"|")
print("Input: text = \" practice   makes   perfect\"  Output: |"+RearrangeSpaces(" practice   makes   perfect")+"|")