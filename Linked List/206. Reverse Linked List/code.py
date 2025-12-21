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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if not head or not head.next:
            return head
        
        # Initializing 3 pointers
        curr = head
        prev, next_node = None, None

        # Safe condition for traversing
        while curr is not None:

            # Store next node, for tracking rest of list
            next_node = curr.next

            # Reverse the link
            curr.next = prev
            
            # Move prev, points to current node
            prev = curr
            
            # Move curr to continue loop
            curr = next_node

        
        # For printing whole Linked-List
        '''
        while prev:
            print(prev, end=" -> ")
            prev = prev.next
        '''

        return prev
        

obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reverseList(head))        # 5 -> 4 -> 3 -> 2 -> 1


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.reverseList(head))        # 2 -> 1


# Create linked list:
head = None
print(obj.reverseList(head))        # None

# T.C: O(N)
# S.C: O(1)