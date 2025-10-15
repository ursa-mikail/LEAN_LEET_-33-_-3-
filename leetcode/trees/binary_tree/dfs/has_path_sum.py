class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, targetSum):
    """
    Check if the tree has a root-to-leaf path where sum of values equals targetSum.
    
    Example:
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    
    targetSum = 22 → True (5→4→11→2 = 22)
    """
    if not root:
        return False
    
    # If we're at a leaf node, check if we've reached the target
    if not root.left and not root.right:
        return root.val == targetSum
    
    # Recursively check left and right subtrees with updated target
    remaining = targetSum - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)

def path_sum_paths(root, targetSum):
    """
    Find all root-to-leaf paths where each path's sum equals targetSum.
    Return list of paths.
    
    Example:
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    
    targetSum = 22 → [[5,4,11,2]]
    """
    def dfs(node, current_path, current_sum, result):
        if not node:        # None ← STOPS HERE
            return
        
        current_path.append(node.val)       # ← This is the PUSH operation (# Push at entry)
        current_sum += node.val
        
        # Check if we're at a leaf node with matching sum
        if not node.left and not node.right and current_sum == targetSum:
            result.append(current_path[:])
        
        # Explore left and right subtrees
        dfs(node.left, current_path, current_sum, result)
        dfs(node.right, current_path, current_sum, result)
        
        # Backtrack
        current_path.pop()                  # Pop ONCE after ALL children done ✅
    
    result = []
    dfs(root, [], 0, result)
    return result

# Test cases
# Tree from example
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print("Has Path Sum:")
print(f"Target 22: {has_path_sum(root, 22)}")  # True
print(f"Target 26: {has_path_sum(root, 26)}")  # True (5→8→13)
print(f"Target 10: {has_path_sum(root, 10)}")  # False

print("\nAll Paths with Sum 22:")
paths = path_sum_paths(root, 22)
for path in paths:
    print(f"Path: {path}")  # [5, 4, 11, 2]

print("\nAll Paths with Sum 26:")
paths = path_sum_paths(root, 26)
for path in paths:
    print(f"Path: {path}")  # [5, 8, 13]

"""
Has Path Sum:
Target 22: True
Target 26: True
Target 10: False

All Paths with Sum 22:
Path: [5, 4, 11, 2]

All Paths with Sum 26:
Path: [5, 8, 13]
"""    

""" path trace sample explanation: 

def dfs(node, path, sum, result):
    if not node: return
    
    # PUSH CURRENT NODE
    path.append(node.val)           # ← PUSH happens here
    sum += node.val
    
    print(f"ENTER node {node.val}: path = {path}")
    
    if not node.left and not node.right:
        print(f"LEAF node {node.val}: path = {path}")
        result.append(path[:])
    
    # Explore children
    dfs(node.left, path, sum, result)
    dfs(node.right, path, sum, result)
    
    # POP CURRENT NODE ← This happens for EVERY node after exploring ALL children
    popped = path.pop()             # ← POP happens here
    print(f"EXIT node {node.val}: popped {popped}, path now = {path}")

    1
   / \
  2   3

dfs(1, [], 0, [])
│
├── PUSH 1: path = [1]
├── ENTER node 1: path = [1]
│
├── dfs(2, [1], 1, [])
│   │
│   ├── PUSH 2: path = [1,2]
│   ├── ENTER node 2: path = [1,2]
│   │   ├── LEAF node 2: path = [1,2] ✅
│   │   ├── dfs(None, [1,2], 3, [[1,2]])  # left child
│   │   ├── dfs(None, [1,2], 3, [[1,2]])  # right child  
│   │   └── POP 2: path = [1]  ← Backtrack from node 2
│   │
│   └── EXIT node 2: popped 2, path now = [1]
│
├── dfs(3, [1], 1, [[1,2]])
│   │
│   ├── PUSH 3: path = [1,3]
│   ├── ENTER node 3: path = [1,3]
│   │   ├── LEAF node 3: path = [1,3] ✅
│   │   ├── dfs(None, [1,3], 4, [[1,2],[1,3]])  # left child
│   │   ├── dfs(None, [1,3], 4, [[1,2],[1,3]])  # right child
│   │   └── POP 3: path = [1]  ← Backtrack from node 3
│   │
│   └── EXIT node 3: popped 3, path now = [1]
│
└── POP 1: path = []  ← Final backtrack from node 1
└── EXIT node 1: popped 1, path now = []
"""