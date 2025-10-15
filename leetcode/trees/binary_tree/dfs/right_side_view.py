def right_side_view(root):
    """
    Return the values of nodes you can see from the right side (top to bottom).
    
    Example:
        1
       / \
      2   3
       \   \
        5   4
    
    Output: [1, 3, 4]
    
    Example:
        1
       / \
      2   3
       \  
        5  
    
    Output: [1, 3, 5]
    """
    def dfs(node, level, result):
        if not node:
            return
        
        # If this is the first node we've seen at this level
        if level == len(result):
            result.append(node.val)
        
        # Traverse right first to get right-side view
        dfs(node.right, level + 1, result)
        dfs(node.left, level + 1, result)
    
    result = []
    dfs(root, 0, result)
    return result

# Alternative BFS approach
def right_side_view_bfs(root):
    """BFS approach for right side view"""
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # If it's the last node in this level, add to result
            if i == level_size - 1:
                result.append(node.val)
            
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

# Tree 2  
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(5)

print("Right Side View (DFS):")
print(f"Tree 1: {right_side_view(root1)}")  # [1, 3, 4]
print(f"Tree 2: {right_side_view(root2)}")  # [1, 3, 5]

print("Right Side View (BFS):")
print(f"Tree 1: {right_side_view_bfs(root1)}")  # [1, 3, 4]
print(f"Tree 2: {right_side_view_bfs(root2)}")  # [1, 3, 5]

"""
Example 1:
text
    1
   / \
  2   3
   \   \
    5   4
Right Side View: [1, 3, 4]

Level 0: Only node 1 → 1
Level 1: Nodes 2 and 3 → 3 (rightmost)
Level 2: Nodes 5 and 4 → 4 (rightmost)

Example 2:
text
    1
   / \
  2   3
 /     
4
Right Side View: [1, 3, 4]

Level 0: Only node 1 → 1
Level 1: Nodes 2 and 3 → 3 (rightmost)
Level 2: Only node 4 → 4
"""