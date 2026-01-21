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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.isBalanced(root))     # True

# Test Case
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(3)

root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(obj.isBalanced(root))     # False

# Test Case
root = None
print(obj.isBalanced(root))     # True