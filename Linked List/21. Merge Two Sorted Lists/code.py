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
        
        dummy = ListNode(0)     # Dummy node for new merged list
        curr = dummy        # For traversing in dummy

        # Loop until 1 list finished
        while list1 and list2:

            # For less & equal values, add list1
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next

            # For list2 values
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        # After loop, add non-empty list. Similar to the loops below
        curr.next = list1 or list2

        '''
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        
        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        '''


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next   # return new head


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

# T.C: O(N + M)
# S.C: O(1)