import yaml

def parse_tree(lines):
    stack = []
    root = {}
    current_dict = root

    for line in lines:
        # Clean line
        line = line.rstrip('\n')
        if not line.strip():
            continue

        # Count indentation level using '│', '├', '└'
        level = line.count("│") + line.count("├") + line.count("└")

        # Extract the node name
        name = line.split('─')[-1].strip()

        # Walk back to correct level
        while len(stack) > level:
            stack.pop()

        # Traverse to the correct parent
        current = root
        for part in stack:
            current = current[part]

        # Add new entry
        if name not in current:
            current[name] = {}

        # Push current node onto the stack
        stack.append(name)

    # Convert dict of dicts to nested lists
    def dict_to_list(d):
        out = {}
        for k, v in d.items():
            if v:
                out[k] = dict_to_list(v)
            else:
                out[k] = None
        return out

    return dict_to_list(root)

def txt_to_yaml(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tree = parse_tree(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(tree, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"YAML written to {output_path}")

# Run the conversion
txt_to_yaml('leetcode_topics.txt', 'leetcode_topics.yaml')

"""
YAML written to leetcode_topics.yaml
"""