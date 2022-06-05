'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

def isValid(s: str) -> bool:
    stack = []
    for character in s:
        if character == '(':
            stack.append(')')
        elif character == '{':
            stack.append('}')
        elif character == '[':
            stack.append(']')
        elif len(stack) ==0 or stack.pop() != character:
            return False

    return len(stack)==0

print("Input:()       Output:",isValid("()"))
print("Input:()[]{}   Output:",isValid("()[]{}"))
print("Input:(])      Output:",isValid("(])"))
