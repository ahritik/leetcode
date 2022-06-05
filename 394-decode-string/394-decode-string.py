class Solution:
    def decodeString(self, s: str) -> str:
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