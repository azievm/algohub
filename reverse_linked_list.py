"""
In-place linked list reversal examples.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --------------------------------------------------
# Reverse entire linked list
# --------------------------------------------------

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
