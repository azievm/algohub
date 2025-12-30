"""
Slow and Fast Pointers (Tortoise & Hare).
Used for cycle detection and middle of linked lists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --------------------------------------------------
# Detect cycle in linked list
# --------------------------------------------------

def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# --------------------------------------------------
# Find middle of linked list
# --------------------------------------------------

def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
