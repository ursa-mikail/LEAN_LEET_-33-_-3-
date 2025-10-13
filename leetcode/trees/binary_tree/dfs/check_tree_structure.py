class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Find the maximum depth of a binary tree.
    Maximum depth = number of nodes along the longest path from root to farthest leaf.
    
    Example:
        3
       / \
      9  20
         /  \
        15   7
    Depth: 3
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

def is_balanced(root):
    """
    Check if a binary tree is height-balanced.
    A balanced tree: |left_height - right_height| <= 1 for every node
    
    Example:
    Balanced:
        1
       / \
      2   3
     /
    4
    
    Not balanced:
        1
       / 
      2
     /
    3
    """
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        current_balanced = left_balanced and right_balanced and (abs(left_height - right_height) <= 1)
        current_height = max(left_height, right_height) + 1
        
        return current_height, current_balanced
    
    return check_balance(root)[1]

# Test cases
# Tree 1: Balanced
#     3
#    / \
#   9  20
#      / \
#     15  7
tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

# Tree 2: Not balanced
#     1
#    / \
#   2   2
#  / \
# 3   3
#/ \
#4  4
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(3)
tree2.left.left.left = TreeNode(4)
tree2.left.left.right = TreeNode(4)

# Tree 3: Single node
tree3 = TreeNode(1)

# Tree 4: Empty
tree4 = None

print("Max Depth:")
print(f"Tree 1: {max_depth(tree1)}")  # 3
print(f"Tree 2: {max_depth(tree2)}")  # 4
print(f"Tree 3: {max_depth(tree3)}")  # 1
print(f"Tree 4: {max_depth(tree4)}")  # 0

print("\nIs Balanced:")
print(f"Tree 1: {is_balanced(tree1)}")  # True
print(f"Tree 2: {is_balanced(tree2)}")  # False
print(f"Tree 3: {is_balanced(tree3)}")  # True
print(f"Tree 4: {is_balanced(tree4)}")  # True

"""
Max Depth:
Tree 1: 3
Tree 2: 4
Tree 3: 1
Tree 4: 0

Is Balanced:
Tree 1: True
Tree 2: False
Tree 3: True
Tree 4: True
"""