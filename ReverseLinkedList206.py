'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    pointer = head

    while pointer != None:
        next = pointer.next
        pointer.next = prev
        prev = pointer
        pointer = next

    return prev
