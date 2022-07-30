"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    mid = end = head
    while end and end.next:
        mid = mid.next
        end = end.next.next
    return mid
    