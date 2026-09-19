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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Edge cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Save root in pair
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


obj = Solution()


# Test Case 1
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(obj.isSameTree(p, q))    # True


# Test Case 2
p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(obj.isSameTree(p, q))    # False


# Test Case 3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)

q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)

print(obj.isSameTree(p, q))    # False

# T.C: O(N)     --> Traversing through every node in the smaller tree once
# S.C: O(H)     --> Call-Stack used for H height tree