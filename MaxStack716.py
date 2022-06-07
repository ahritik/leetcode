'''
716. MaxStack

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
Implement the MaxStack class:
MaxStack() Initializes the stack object.
    void push(int x) Pushes element x onto the stack.
    int pop()        Removes the element on top of the stack and returns it.
    int top()        Gets the element on the top of the stack without removing it.
    int peekMax()    Retrieves the maximum element in the stack without removing it.
    int popMax()     Retrieves the maximum element in the stack and removes it.
                     If there is more than one maximum element, only remove the top-most one.
'''

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
            return
        if self.max_stack[-1] > x:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    def pop(self):
        if len(self.stack) != 0:
            self.max_stack.pop(-1)
            return self.stack.pop(-1)

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        if len(self.max_stack) != 0:
            return self.max_stack[-1]

    def popMax(self):
        val = self.peekMax()
        curr = []
        while self.top() != val:
            curr.append(self.pop())
        self.pop()
        while len(curr) != 0:
            self.push(curr.pop(-1))
        return val

def test():
    testStack = MaxStack()
    testStack.push(12)
    testStack.push(1)
    testStack.push(2)
    testStack.push(122)
    testStack.push(21)
    testStack.push(12)

    print("Pushed: 12, 1, 2, 122, 21, 12")
    print("Stack Pop:", testStack.pop())
    print("Stack Top:", testStack.top())
    print("Stack Peek Max:", testStack.peekMax())
    print("Stack Pop Max:", testStack.popMax())

test()