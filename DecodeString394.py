'''
394. Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].
'''

def decodeString(s: str) -> str:
    num = 0
    output = ''
    stack = []
    for letter in s:
        if letter.isdigit():
            num = num*10 + int(letter)
        elif letter == "[":
            stack.append(output)
            stack.append(num)
            output = ''
            num = 0
        elif letter.isalpha():
            output += letter
        elif letter == ']':
            pre_num = stack.pop()
            pre_string = stack.pop()
            output = pre_string + pre_num * output
    return output

print("Input: 3[a]2[bc]      Output:",decodeString("3[a]2[bc]"))
print("Input: 3[a2[c]]       Output:",decodeString("3[a2[c]]"))
print("Input: 2[abc]3[cd]ef  Output:",decodeString("2[abc]3[cd]ef"))