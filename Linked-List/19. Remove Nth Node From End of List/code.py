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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:       
        # Dummy node for easy head removal
        dummy = ListNode(0)
        dummy.next = head

        # Both pointers at dummy
        slow, fast = dummy, dummy

        # Including n
        for _ in range(n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Removing Nth node
        slow.next = slow.next.next


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy.val, end=" -> ")
            dummy = dummy.next
        '''
        return dummy.next


obj = Solution()

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.removeNthFromEnd(head, 2))        # 1 -> 2 -> 3 -> 5


# Create linked list: 1
head = ListNode(1)
print(obj.removeNthFromEnd(head, 1))        # None


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 1))        # 1


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 2))        # 2

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used



"""
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Calculate target index
        target_index = length - n
        
        # Dummy node for easy head removal
        dummy = ListNode(0)
        dummy.next = head

        new_curr = dummy

        # Loop till the index
        for _ in range(target_index):
            new_curr = new_curr.next

        # Skip the target node
        new_curr.next = new_curr.next.next


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy.val, end=" -> ")
            dummy = dummy.next
        '''
        return dummy.next


obj = Solution()

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.removeNthFromEnd(head, 2))        # 1 -> 2 -> 3 -> 5


# Create linked list: 1
head = ListNode(1)
print(obj.removeNthFromEnd(head, 1))        # None


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 1))        # 1


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 2))        # 2

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used
"""