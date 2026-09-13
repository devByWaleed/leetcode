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
        # Copying next node's value to the point
        node.val = node.next.val

        # Adjust next value
        node.next = node.next.next
        

# Helper Function For Local Code Running
def printList(head):
    while head:
        print(head, end=" -> ")
        head = head.next
    print("None")


obj = Solution()

# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
# Printing
print("Before:-")
printList(head)                         # 4 -> 5 -> 1 -> 9
obj.deleteNode(head.next)
print("After:-")
printList(head)                         # 4 -> 1 -> 9



# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
# Printing
print("Before:-")
printList(head)                              # 4 -> 5 -> 1 -> 9
obj.deleteNode(head.next.next)
print("After:-")
printList(head)                              # 4 -> 5 -> 9

# T.C: O(1)
# S.C: O(1)