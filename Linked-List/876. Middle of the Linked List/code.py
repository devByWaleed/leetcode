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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize 2 pointers at head
        slow, fast = head, head

        # Condition for looping till end of list
        while fast and fast.next:

            # Moving slow pointer 1 time
            slow = slow.next

            # Moving slow pointer 2 time
            fast = fast.next.next

        # For printing whole Linked-List
        '''
        while slow:
            print(slow, end=" -> ")
            slow = slow.next
        '''

        # Mid node will be on slow pointer
        return slow


obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.middleNode(head))        # 3 -> 4 -> 5


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(obj.middleNode(head))        # 4 -> 5 -> 6

# T.C: O(N)
# S.C: O(1)