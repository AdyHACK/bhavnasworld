import sys

with open('src/styles/responsive.css', 'r', encoding='utf-8') as f:
    content = f.read()

stack = []
for line_no, line in enumerate(content.split('\n'), 1):
    for ch in line:
        if ch == '{':
            stack.append(line_no)
        elif ch == '}':
            if not stack:
                print(f"Error: unmatched closing }} at line {line_no}")
                sys.exit(1)
            stack.pop()

if stack:
    print(f"Error: unclosed {{ from line {stack[-1]}")
    sys.exit(1)

print("CSS brackets are 100% balanced!")
