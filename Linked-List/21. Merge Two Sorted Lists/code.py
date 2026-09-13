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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Pointers for both lists
        curr_l1 = list1
        curr_l2 = list2

        # Dummy node & it's pointer
        dummy = ListNode(0)
        curr_dummy = dummy

        while curr_l1 and curr_l2:
            # Add value of list1
            if curr_l1.val <= curr_l2.val:
                curr_dummy.next = curr_l1
                curr_l1 = curr_l1.next
            # Add value of list2
            else:
                curr_dummy.next = curr_l2
                curr_l2 = curr_l2.next

            # Move pointer of dummy list
            curr_dummy = curr_dummy.next

        # If 1 list becomes empty, add other
        if not curr_l1:     curr_dummy.next = curr_l2
        if not curr_l2:     curr_dummy.next = curr_l1

        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy.val, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next

        
obj = Solution()

# Create linked list:
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(obj.mergeTwoLists(list1, list2))      # 1 -> 1 -> 2 -> 3 -> 4 -> 4


# Create linked list:
list1 = None

list2 = None
print(obj.mergeTwoLists(list1, list2))      # None


# Create linked list:
list1 = None

list2 = ListNode(0)
list2.next = None
print(obj.mergeTwoLists(list1, list2))      # 0

# T.C: O(N + M)     --> Looping through both Linked-List
# S.C: O(1)         --> No data structure used