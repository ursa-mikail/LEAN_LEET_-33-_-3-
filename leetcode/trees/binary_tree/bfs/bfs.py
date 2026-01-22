from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    """BFS/Level Order Traversal - returns list of values in BFS order"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def bfs_level_by_level(root):
    """BFS that returns levels as separate lists"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Create a sample binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Test basic BFS
print("BFS traversal (single list):")
print(bfs(root))  # [1, 2, 3, 4, 5, 6]

print("\nBFS traversal (level by level):")
levels = bfs_level_by_level(root)
for i, level in enumerate(levels):
    print(f"Level {i}: {level}")
# Output:
# Level 0: [1]
# Level 1: [2, 3]
# Level 2: [4, 5, 6]