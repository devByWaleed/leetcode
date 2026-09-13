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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Dummy node for edge cases
        dummy = ListNode(0)
        curr = dummy
        
        arr = []
        
        # Add numbers into array
        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                # print(lists[i], end=" -> ")
                lists[i] = lists[i].next

        # Sorting the array
        arr.sort()

        # Creating the sorted list
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next
        

obj = Solution()

# Create linked list:
# List 1: 1 -> 4 -> 5
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

# List 2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# List 3: 2 -> 6
list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]

print(obj.mergeKLists(lists))       # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6


# Create linked list:
lists = []

print(obj.mergeKLists(lists))       # None


# Create linked list:
lists = [None]

print(obj.mergeKLists(lists))       # None

# T.C: O(N LOG N)
# S.C: O(N)


'''
# Print lists column wise
while any(lists):                     # continue while at least one list is not None
    for j in range(len(lists)):
        if lists[j]:                  # if current list still has nodes
            print(lists[j].val, end=" -> ")
            lists[j] = lists[j].next  # move down in that list
'''