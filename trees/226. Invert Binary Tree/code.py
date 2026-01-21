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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


obj = Solution()

# Test Case
root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(obj.invertTree(root))     # 4

# Test Case
root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
print(obj.invertTree(root))     # 2

# Test Case
root = None
print(obj.invertTree(root))     # []