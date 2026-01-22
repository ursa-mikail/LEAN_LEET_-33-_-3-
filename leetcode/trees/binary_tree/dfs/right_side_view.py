class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
"""
Tree:
    1      ← Level 0
   / \
  2   3    ← Level 1  
   \   \
    5   4  ← Level 2

Step-by-Step Execution:

Level 0:
queue = [1], level_size = 1
Process node 1: i = 0, level_size - 1 = 0 → i == level_size - 1 ✅
Add 1 to result: result = [1]
Add children: queue = [2, 3]

Level 1:
queue = [2, 3], level_size = 2
Process node 2: i = 0, level_size - 1 = 1 → 0 == 1? ❌ (not last)
Process node 3: i = 1, level_size - 1 = 1 → 1 == 1? ✅ LAST NODE!
Add 3 to result: result = [1, 3]
Add children: queue = [5, 4]

Level 2:
queue = [5, 4], level_size = 2
Process node 5: i = 0, level_size - 1 = 1 → 0 == 1? ❌ (not last)
Process node 4: i = 1, level_size - 1 = 1 → 1 == 1? ✅ LAST NODE!
Add 4 to result: result = [1, 3, 4]

Final: [1, 3, 4] ✅
"""
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

            # KEY LINE: If this is the LAST node in current level, add to result
            # Because in BFS, nodes are added left-to-right, so the 
            # last node in each level is the rightmost one!
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