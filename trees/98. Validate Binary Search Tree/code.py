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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass


obj = Solution()

# Test Case
root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
print(obj.isValidBST(root))    # True

# Test Case
root = TreeNode(5)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(obj.isValidBST(root))    # False