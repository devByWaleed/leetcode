from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# Reverse it
reversed_head = obj.reverseList(head)
print(reversed_head)        # 5 -> 4 -> 3 -> 2 -> 1


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
# Reverse it
reversed_head = obj.reverseList(head)
print(reversed_head)        # 2 -> 1


# Create linked list:
head = None
# Reverse it
reversed_head = obj.reverseList(head)
print(reversed_head)        # NULL  