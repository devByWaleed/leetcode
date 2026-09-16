from typing import Optional
from collections import deque

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if root == None:
            return 0
        
        # Creating deque with root for constant removal
        queue = deque([root])
        
        # Store current-level depth
        depth = 0

        # Store minimum depth
        min_depth = float('inf')


        while queue:

            # Calculating number of nodes in current level
            level = len(queue)

            # Increment depth by 1 for current existed level
            depth += 1


            # Looping through the total nodes in current level
            for _ in range(level):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                # Condition for verifying leaf node
                if not curr.left and not curr.right:
                    min_depth = min(min_depth, depth)
        

        return min_depth


obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.minDepth(root))     # 2

# Test Case
root = TreeNode(2)

root.right = TreeNode(3)

root.right.right = TreeNode(4)

root.right.right.right = TreeNode(5)

root.right.right.right.right = TreeNode(6)
print(obj.minDepth(root))     # 5

# T.C: O(N)
# S.C: O(W)  W = width of tree