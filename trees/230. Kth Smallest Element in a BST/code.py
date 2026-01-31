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
        pass


obj = Solution()


# Test Case
root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.left = TreeNode(2)
print(obj.kthSmallest(root))    # 1


# Test Case
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)
print(obj.kthSmallest(root))    # 3