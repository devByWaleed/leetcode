from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"
    

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
# Reverse it
print(obj.deleteDuplicates(head))        # 1 -> 2


# Create linked list:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
# Reverse it
print(obj.deleteDuplicates(head))        # 1 -> 2 -> 3