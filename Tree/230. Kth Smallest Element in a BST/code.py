from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack for DFS traversal
        stack = []

        # Pointer for root
        curr = root

        # Counter for checking kth value
        counter = 0

        # While traversing BST and getting root
        while stack or curr:

            while curr:
                # Add to stack and move to left childs
                stack.append(curr)
                curr = curr.left

            # Popping and incrementing counter for k values checking
            curr = stack.pop()
            counter += 1

            # If kth smallest found, return it's .val
            if counter == k:
                return curr.val

            # Move to right side of BST
            curr = curr.right

        
obj = Solution()


# Test Case
root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)
print(obj.kthSmallest(root, 1))    # 1


# Test Case
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)
print(obj.kthSmallest(root, 3))    # 3


# Test Case
root = TreeNode(1)

root.right = TreeNode(2)
print(obj.kthSmallest(root, 2))    # 1

# T.C: O(H + k)     --> Traversing through H nodes + k lookup
# S.C: O(H)         --> Stack used for h height BST


# Works on strictly left tree
'''
stack = [root]

# Adding all left nodes to stack
while True:
    curr = stack[-1]
    if curr.left:
        stack.append(curr.left)
    else:
        # Loop stops when tree ends
        break

# Store kth smallest value
kth_val = 0

# Looping k times to get targeted value
for _ in range(k):
    kth_val = stack.pop()

return kth_val.val
'''