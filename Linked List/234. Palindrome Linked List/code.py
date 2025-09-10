from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def middle(self, head: Optional[ListNode]):
        pass


obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(obj.middle(head))        # True


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.middle(head))        # False