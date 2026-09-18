# Blind 75 Part 5: Trees

This part contains problems related to `Trees`, `DFS`, `BFS`, `Tries`

`Total Count = 14`

---

## 1. LeetCode 104: Maximum Depth of Binary Tree (Easy)

* **Identified Pattern Upfront:** Tree / DFS / BFS
* **Time Taken:** 28 minutes
* **Solution Folder:** [`../../Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree/`](../../Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/2143403105)

### Code Solution

```python
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
```

---

## 2. LeetCode 102: Binary Tree Level Order Traversal (Medium)

* **Identified Pattern Upfront:** Tree / BFS
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../Tree/102.%20Binary%20Tree%20Level%20Order%20Traversal/`](../../Tree/102.%20Binary%20Tree%20Level%20Order%20Traversal/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/2144421763)

### Code Solution

```python
from typing import Optional, List
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Final answer
        result = []
        # Queue for BFS
        queue = deque([ root ])
        
        while queue:
        # Get length for completing level traversal
            level = len(queue)
            level_nodes = []
            
            for _ in range(level):
                curr = queue.popleft()
                # Add current value
                level_nodes.append(curr.val)

                # Add left & right childs to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    # Add level's array to result
            result.append(level_nodes)
    
        return result
   
        
obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.levelOrder(root))     # [[3], [9,20], [15,7]]

# Test Case
root = TreeNode(1)
print(obj.levelOrder(root))     # [[1]]

# Test Case
root = None
print(obj.levelOrder(root))     # []

# T.C: O(N)     --> Looping through the queue
# S.C: O(N)     --> Array used for N nodes
```

---

## 3. LeetCode 124: Binary Tree Maximum Path Sum (Hard)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../Tree/124.%20Binary%20Tree%20Maximum%20Path%20Sum/`](../../Tree/124.%20Binary%20Tree%20Maximum%20Path%20Sum/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/2145415922)

### Code Solution

```python
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Used list bcz it will change the value
        rather than creating a new variable inside recursive function
        ''' 
        max_sum = [root.val]
        
        def dfs(root):
            # Edge case: Empty Tree
            if not root:
                return 0
            
            # Handle left & right childs
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            
            # Handle -ve value
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            
            # Store max sum
            max_sum[0] = max(max_sum[0], root.val+max_left+max_right)

            # Return sum of root with either left OR right
            return root.val + max(max_left, max_right)
        
        # Call function
        dfs(root)
        
        # Return Max Path Sum
        return max_sum[0]


obj = Solution()


# Test Case
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
print(obj.maxPathSum(root))    # 6


# Test Case
root = TreeNode(-10)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.maxPathSum(root))    # 42

# T.C: O(N)     --> Function call on N nodes
# S.C: O(H)     --> Recursive call-stack of height H tree
```

---

## 4. LeetCode 226: Invert Binary Tree (Easy)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 10 minutes
* **Solution Folder:** [`../../Tree/226.%20Invert%20Binary%20Tree/`](../../Tree/226.%20Invert%20Binary%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/invert-binary-tree/submissions/2144511668)

### Code Solution

```python
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge cases: Empty Tree & Only Root
        if not root:
            return None
        
        
        def dfs(node):
            # Base condition: Node is empty
            if not node:
                return None
                
            # Inverting
            node.left, node.right = node.right, node.left
            
            # Passing left child
            dfs(node.left)
            # Passing right child
            dfs(node.right)
        
        
        # Passing give root
        dfs(root)
        
        # Printing Tree in BFS form
        '''
        print(breathFirstSearch(root))
        '''
        
        # Returning
        return root
        
'''
def breathFirstSearch(root):
  # Edge case
  if root == None:
     return []
  
  queue = [root]

  queue = deque(queue)
  result = []

  while queue:
    curr = queue.popleft()
    result.append(curr.val)
    
    if curr.left:
      queue.append(curr.left)

    if curr.right:
      queue.append(curr.right)


  return result
'''

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
print(obj.invertTree(root))     # None

# Test Case
root = 1

#root.left = None
root.right = 2
print(obj.invertTree(root))

# T.C: O(N)     --> Function call on N nodes
# S.C: O(H)     --> Recursive call-stack of height H tree
```

---

## 5. LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal (Medium)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 26 minutes
* **Solution Folder:** [`../../Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/`](../../Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/2145404783)

### Code Solution

```python
from typing import Optional, List
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Edge case
        if not preorder or not inorder:
            return None
        
        # Create root node
        root = TreeNode(preorder[0])

        # Find index of current number in inorder array
        mid = inorder.index(preorder[0])

        # Attaching left & right child recursively
        root.left = self.buildTree(preorder[1 : mid+1], inorder[: mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Printing Tree in BFS form
        '''
        # print(breathFirstSearch(root))
        '''

        return root
        

def breathFirstSearch(root: Optional[TreeNode]):
    if not root:
        return []
    
    # Using deque for efficient pops from the left
    queue = deque([root])
    result = []

    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        current_level_vals = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level_vals.append(node.val)
            
            # Add children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Append the entire level to results
        result.append(current_level_vals)

    return result


obj = Solution()

# Test Case
pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]

print(obj.buildTree(pre_order, in_order))   # 3

# Test Case
pre_order = [-1]
in_order = [-1]

print(obj.buildTree(pre_order, in_order))   # -1

# T.C: O(N)     --> Working on N numbers array
# S.C: O(N)     --> Recursive call-stack of N size used
```

---

## 6. LeetCode 98: Validate Binary Search Tree (Medium)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 21 minutes
* **Solution Folder:** [`../../Tree/98.%20Validate%20Binary%20Search%20Tree/`](../../Tree/98.%20Validate%20Binary%20Search%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/validate-binary-search-tree/submissions/2145466108)

### Code Solution

```python
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

        def validate(node, low = -float("inf"), high = float("inf")):
            # Edge case
            if not node:
                return True

            # Checking for value
            if not (low < node.val < high):
                return False

            # Validate it's left BST
            left_bst = validate(node.left, low, node.val)

            # Validate it's right BST
            right_bst = validate(node.right, node.val, high)

            # Final validation
            return left_bst and right_bst

        # Return answer
        return validate(root)
    

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

# Test Case
root = TreeNode(1)

root.left = TreeNode(1)
print(obj.isValidBST(root))    # True

# T.C: O(N)     --> Working on N nodes
# S.C: O(N)     --> Recursive call-stack of N size used
```

---

## 7. LeetCode 230: Kth Smallest Element in a BST (Medium)

* **Identified Pattern Upfront:** Tree / BST / DFS / Stack
* **Time Taken:** 17 minutes
* **Solution Folder:** [`../../Tree/230.%20Kth%20Smallest%20Element%20in%20a%20BST/`](../../Tree/230.%20Kth%20Smallest%20Element%20in%20a%20BST/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/2145501493)

### Code Solution

```python
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
```





---

## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```