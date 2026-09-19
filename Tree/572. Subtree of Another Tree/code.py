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
    def isSubtree(self, root: Optional['TreeNode'], subRoot: Optional['TreeNode']) -> bool:
        # Function to check sub_tree
        def isSameTree(p, q):
            queue = deque([ (p, q) ])

            while queue:
                # Pop the leftmost
                node1, node2 = queue.popleft()

                # If both empty, continue
                if not node1 and not node2:
                    continue

                # 1 is empty or value not matched
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                # Add left & right childs
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

            return True


        # Working on "root"
        main_queue = deque([ root ])

        while main_queue:
            curr = main_queue.popleft()

            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
                
            if curr.left:
                main_queue.append(curr.left)
            if curr.right:
                main_queue.append(curr.right)
        
        return False


obj = Solution()


# Test Case 1
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(obj.isSubtree(root, subRoot))    # True


# Test Case 2
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(obj.isSubtree(root, subRoot))    # False

# T.C: O(M * N)     --> N = nodes in root, M = nodes in subRoot (isSame check at each node)
# S.C: O(max(M,N))         --> Recursion stack, H = height of the root tree