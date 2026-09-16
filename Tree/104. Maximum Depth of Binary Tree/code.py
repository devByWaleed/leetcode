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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: Empty Tree
        if root == None:
            return 0

        # Creating deque for constant node removal
        queue = deque([ root ])

        # Final depth count
        depth = 0

        while queue:
            # Get size of current level
            level = len(queue)

            for _ in range(level):
                # POP current node
                curr = queue.popleft()

                # Add left & right childs
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            # After processing level
            depth += 1

        return depth

        
obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.maxDepth(root))     # 3

# Test Case
root = TreeNode(1)

root.right = TreeNode(2)
print(obj.maxDepth(root))     # 2

# T.C: O(N)     --> Looping through N nodes
# S.C: O(W)     --> Queue used for W width tree





# BFS & DFS (recursively) at same time
'''
# queue = deque([root.val])
        queue = deque([root])
        max_depth = 0

        while True:
            if root.left:
                queue.appendleft(root.left)
                max_depth = max(max_depth, len(queue))
                
                if root.left.left:
                    child = self.maxDepth(root.left)
                    # print(child)
                if root.left.right:
                    child = self.maxDepth(root.left)
                    # print(child)
            


            if root.right:
                if root.left:
                    queue.popleft()
                queue.appendleft(root.right)
                max_depth = max(max_depth, len(queue))
                
                if root.right.left:
                    child = self.maxDepth(root.right)
                    # print(child)
                if root.right.right:
                    child = self.maxDepth(root.right)
                    # print(child)

            break
'''