import yaml
import re

def parse_tree_with_difficulty(lines):
    stack = []
    root = {}
    levels = []

    for line in lines:
        line = line.rstrip('\n')
        if not line.strip():
            continue

        # Level is the number of graphical prefix chars
        level = line.count("│") + line.count("├") + line.count("└")

        # Extract topic and optional difficulty label
        match = re.search(r'([^\[]+?)(?:\s*\[(Easy|Medium|Hard)\])?$', line.strip())
        if match:
            topic = match.group(1).strip()
            difficulty = match.group(2)

        # Trim stack to correct depth
        stack = stack[:level]

        # Traverse to parent node
        current = root
        for key in stack:
            current = current.setdefault(key, {})

        # Add topic
        if difficulty:
            current[topic] = {'difficulty': difficulty}
        else:
            current[topic] = {}

        stack.append(topic)

    return root

def txt_to_yaml_with_difficulty(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tree = parse_tree_with_difficulty(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(tree, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"YAML with difficulty written to {output_path}")

# Run
txt_to_yaml_with_difficulty('leetcode_topics.txt', 'leetcode_topics.yaml')

"""
leetcode
├── arrays
│   ├── 1_d
│   │   ├── sliding_window [Medium]
│   │   ├── two_pointers [Easy]
│   │   └── bit_manipulation [Hard]

to

leetcode:
  arrays:
    1_d:
      sliding_window:
        difficulty: Medium
      two_pointers:
        difficulty: Easy
      bit_manipulation:
        difficulty: Hard

"""