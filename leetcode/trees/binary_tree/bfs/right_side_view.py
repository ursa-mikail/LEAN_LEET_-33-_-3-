from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view_bfs(root):
    """
    Get right side view using BFS (level order traversal).
    At each level, take the last node.
    
    Example:
        1
       / \
      2   3
       \   \
        5   4
    Output: [1, 3, 4]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # If this is the last node in current level, add to result
            if i == level_size - 1:
                result.append(node.val)
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Test cases
# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)

# Tree 2 - Right heavy
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)

# Tree 3 - Left heavy but still take rightmost at each level
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
root3.right = TreeNode(3)

# Tree 4 - Single node
root4 = TreeNode(1)

print("Right Side View (BFS):")
print(f"Tree 1: {right_side_view_bfs(root1)}")  # [1, 3, 4]
print(f"Tree 2: {right_side_view_bfs(root2)}")  # [1, 3, 5]
print(f"Tree 3: {right_side_view_bfs(root3)}")  # [1, 3, 5]
print(f"Tree 4: {right_side_view_bfs(root4)}")  # [1]

