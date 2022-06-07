'''
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
'''

def fizzBuzz(n: int):
    output = []
    for num in range(1,n+1):
        string = ""
        if num % 3 == 0:
            string = string + "Fizz"
        if num % 5 == 0:
            string = string + "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            string = string + str(num)
        output.append(string)
    return output

