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
        # Edge case
        if root == None:
            return 0
        
        # Creating deque with root for constant removal
        queue = deque([root])
        
        # Store maximum depth
        max_depth = 0

        while queue:

            # Calculating number of nodes in current level
            level = len(queue)

            # Increment depth by 1 for current existed level
            max_depth += 1


            # Looping through the total nodes in current level
            for _ in range(level):
                curr = queue.popleft()      # Remove root node
                
                # Add it's left and right childs
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        

        return max_depth


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

# T.C: O(N)
# S.C: O(W)  W = width of tree





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