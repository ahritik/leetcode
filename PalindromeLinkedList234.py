"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.
"""

def isPalindrome(head):
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]