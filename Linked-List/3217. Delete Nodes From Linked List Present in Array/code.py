from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Creating dummy node for easy removal
        dummy = ListNode(0)
        dummy.next = head

        # Hash-set for O(1) checking
        nums_set = set(nums)

        # Current pointer for traversal
        curr = dummy

        '''
        If element in hashset, remove it.
        Otherwise simple traversal
        '''
        while curr and curr.next:

            if curr.next.val in nums_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
            

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
print(obj.modifiedList([1, 2, 3], head))        # 4 -> 5


# Create linked list: 1 -> 2 -> 1 -> 2 -> 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
print(obj.modifiedList([1], head))        # 2 -> 2 -> 2


# Create linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(obj.modifiedList([5], head))        # 1 -> 2 -> 3 -> 4

# T.C: O(N)
# S.C: O(M)