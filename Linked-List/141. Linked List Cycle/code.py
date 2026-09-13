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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge casee: 1 node
        if not head or not head.next:
            return False

        # Initialize slow & fast pointers
        slow = head
        fast = head

        # Looping till end of list
        while fast and fast.next:
            # 1 time movement
            slow = slow.next

            # 2 time movement
            fast = fast.next.next

            # Checking for same position: cycle found
            if slow == fast:
                return True

        # No cycle found
        return False

        
obj = Solution()

# Create linked list:
head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node_4 = ListNode(-4)

head.next = node2
node2.next = node0
node0.next = node_4
node_4.next = node2   # cycle created here
print(obj.hasCycle(head))       # True


# Create linked list:
head = ListNode(1)
node2 = ListNode(2)

head.next = node2
node2.next = head   # cycle created here
print(obj.hasCycle(head))       # True


# Create linked list:
head = ListNode(1)  # No cycle created
print(obj.hasCycle(head))       # False

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used