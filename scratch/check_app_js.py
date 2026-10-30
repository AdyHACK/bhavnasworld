import sys

with open('src/components/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check open/close braces
stack = []
pairs = {')': '(', '}': '{', ']': '['}
lines = content.split('\n')

in_multiline_comment = False
in_string = None
escape = False

for line_no, line in enumerate(lines, 1):
    i = 0
    while i < len(line):
        ch = line[i]
        
        if in_multiline_comment:
            if ch == '*' and i + 1 < len(line) and line[i+1] == '/':
                in_multiline_comment = False
                i += 2
                continue
            i += 1
            continue
            
        if in_string:
            if escape:
                escape = False
            elif ch == '\\':
                escape = True
            elif ch == in_string:
                in_string = None
            i += 1
            continue
            
        # Check comments
        if ch == '/' and i + 1 < len(line):
            if line[i+1] == '/':
                break # line comment
            elif line[i+1] == '*':
                in_multiline_comment = True
                i += 2
                continue
                
        # Check string starts
        if ch in ("'", '"', '`'):
            in_string = ch
            i += 1
            continue
            
        if ch in '({[':
            stack.append((ch, line_no))
        elif ch in ')}]':
            if not stack:
                print(f"Error: unmatched closing {ch} at line {line_no}")
                sys.exit(1)
            open_ch, open_line = stack.pop()
            if pairs[ch] != open_ch:
                print(f"Error: mismatched {ch} at line {line_no}, expected match for {open_ch} from line {open_line}")
                sys.exit(1)
        i += 1

if stack:
    print(f"Error: {len(stack)} unclosed brackets, first unclosed: {stack[0]}")
    sys.exit(1)

print("Brackets, braces, parentheses, comments, and strings are fully balanced and clean!")
