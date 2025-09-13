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
        
        # Edge case
        if not head.next and n == 1:    return None

        # Dummy node for easy
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy

        # Move fast pointer n steps ahead (so slow ends up before node to delete)
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the target node
        slow.next = slow.next.next


        # For printing whole Linked-List
        '''
        while dummy.next:
            print(dummy.next, end=" -> ")
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

# T.C: O(N)
# S.C: O(1)