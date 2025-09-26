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
        
        # Creating dummy node for easy merging
        dummy = ListNode(0)
        # dummy.next = list1        # No need as we need a new sorted list

        # Current pointer for traversal
        curr = dummy

        # Condition for both list traversal
        while list1 and list2:
            
            # Comparing and then assigning list1 node
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next

            # Comparing and then assigning list2 node
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        curr.next = list1 or list2      # If any list becomes empty, assign other list


        # For printing whole Linked-List
        '''
        while dummy.next:
            print(dummy.next, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next


obj = Solution()

# Create linked list:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

print(obj.mergeTwoLists(head1, head2))      # 1 -> 1 -> 2 -> 3 -> 4 -> 4


# Create linked list:
head1 = None

head2 = None
print(obj.mergeTwoLists(head1, head2))      # None


# Create linked list:
head1 = None

head2 = ListNode(0)
head2.next = None
print(obj.mergeTwoLists(head1, head2))      # 0

# T.C: O(N + M)
# S.C: O(1)