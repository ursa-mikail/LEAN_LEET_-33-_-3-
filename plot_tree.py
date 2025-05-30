from anytree import Node, RenderTree
from anytree.exporter import DotExporter

import matplotlib.pyplot as plt

def build_anytree_from_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    node_stack = []
    root = Node("leetcode")
    node_stack.append((0, root))

    for line in lines[1:]:
        stripped = line.rstrip()
        level = stripped.count("│") + stripped.count("├") + stripped.count("└")   # equivalent to the tabs (if tabs are used)
        name = stripped.split('─')[-1].strip()
        
        parent_level, parent_node = node_stack[level - 1]
        new_node = Node(name, parent=parent_node)
        
        if len(node_stack) > level:
            node_stack[level] = (level, new_node)
        else:
            node_stack.append((level, new_node))

    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")
    
    # Optional: Save as image (requires Graphviz)
    DotExporter(root).to_picture("leetcode_tree.png")
    return root

root = build_anytree_from_txt("leetcode_topics.txt")

plt.figure(figsize=(128, 96))
plt.imshow(plt.imread("leetcode_tree.png"))
plt.axis('off')


