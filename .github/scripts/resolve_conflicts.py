import re

def resolve_conflicts(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Match Git conflict markers
    conflict_pattern = r"<<<<<<< HEAD(.*?)=======\n(.*?)>>>>>>>.*?\n"
    
    # Resolve by merging unique lines from both sides
    def conflict_resolver(match):
        head = match.group(1).strip().split('\n')
        incoming = match.group(2).strip().split('\n')
        merged = sorted(set(head + incoming))  # Remove duplicates and sort
        return '\n'.join(merged)

    resolved_content = re.sub(conflict_pattern, conflict_resolver, content, flags=re.S)

    with open(file_path, 'w') as file:
        file.write(resolved_content)

# Path to participants list
resolve_conflicts('README.md')
