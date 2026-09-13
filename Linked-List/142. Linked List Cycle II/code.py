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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case (0 / 1 node)
        if not head or not head.next:   return None

        # Initialize 2 pointers at head
        slow, fast = head, head

        # Condition for looping till end of list
        while fast and fast.next:

            # Moving slow pointer 1 time
            slow = slow.next

            # Moving slow pointer 2 time
            fast = fast.next.next

            # If pointers meet, cycle detected. Otherwise no cycle
            if slow == fast:

                # Reset one pointer to head and loop to detect the starting point
                fast = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
            
        # If no cycle, return Null
        return None


obj = Solution()

# Create linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
# Create cycle: -4 -> 2
head.next.next.next.next = head.next
print(obj.detectCycle(head))        # 2


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
# Create cycle: 2 -> 1
head.next.next = head
print(obj.detectCycle(head))        # 1


# Create linked list: 1
head = ListNode(1)
# No cycle
print(obj.detectCycle(head))        # None

# T.C: O(N)
# S.C: O(1)