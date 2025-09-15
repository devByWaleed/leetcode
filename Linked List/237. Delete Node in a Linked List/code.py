# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pass

obj = Solution()

# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
print(obj.deleteNode(5))        # 4 -> 1 -> 9


# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
print(obj.deleteNode(1))        # 4 -> 5 -> 9