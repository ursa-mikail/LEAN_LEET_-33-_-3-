#!pip install anytree

import os

def build_dirs_from_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    path_stack = []
    for line in lines:
        stripped = line.rstrip()
        level = stripped.count("│") + stripped.count("├") + stripped.count("└")
        name = stripped.split('─')[-1].strip()

        # Adjust the current path stack based on indentation level
        path_stack = path_stack[:level]
        path_stack.append(name)

        dir_path = os.path.join(*path_stack)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created: {dir_path}")

build_dirs_from_txt("leetcode_topics.txt")

"""
Created: leetcode
Created: leetcode/arrays
Created: leetcode/arrays/1_d
Created: leetcode/arrays/1_d/sliding_window
Created: leetcode/arrays/1_d/two_pointers
Created: leetcode/arrays/1_d/prefix_sum
Created: leetcode/arrays/1_d/bit_manipulation
Created: leetcode/arrays/2_d
Created: leetcode/arrays/grid
Created: leetcode/arrays/prefix_sum
Created: leetcode/arrays/dynamic_programming
Created: leetcode/pointers
Created: leetcode/pointers/1_d
Created: leetcode/pointers/1_d/linked_list
Created: leetcode/pointers/1_d/linked_list/cycle_detection
Created: leetcode/pointers/1_d/linked_list/merge_nodes
Created: leetcode/pointers/1_d/linked_list/reverse_nodes
Created: leetcode/pointers/1_d/stack
:
"""