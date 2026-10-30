import sys

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check basic bracket balancing ignoring quotes
    stack = []
    in_single = False
    in_double = False
    in_template = False
    in_line_comment = False
    in_block_comment = False
    i = 0
    line_num = 1
    col_num = 1
    
    while i < len(content):
        c = content[i]
        if c == '\n':
            line_num += 1
            col_num = 1
            if in_line_comment:
                in_line_comment = False
            i += 1
            continue
        
        col_num += 1
        
        # comments
        if not in_single and not in_double and not in_template:
            if not in_block_comment and i + 1 < len(content) and content[i:i+2] == '//':
                in_line_comment = True
                i += 2
                continue
            if not in_line_comment and i + 1 < len(content) and content[i:i+2] == '/*':
                in_block_comment = True
                i += 2
                continue
            if in_block_comment and i + 1 < len(content) and content[i:i+2] == '*/':
                in_block_comment = False
                i += 2
                continue
        
        if in_line_comment or in_block_comment:
            i += 1
            continue
            
        # string escapes
        if (in_single or in_double or in_template) and c == '\\':
            i += 2
            continue
            
        if c == "'" and not in_double and not in_template:
            in_single = not in_single
        elif c == '"' and not in_single and not in_template:
            in_double = not in_double
        elif c == '`' and not in_single and not in_double:
            in_template = not in_template
        elif not in_single and not in_double and not in_template:
            if c in '({[':
                stack.append((c, line_num, col_num))
            elif c in ')}]':
                if not stack:
                    print(f"Error: unmatched '{c}' at {line_num}:{col_num}")
                    return False
                top, l, col = stack.pop()
                expected = {'(': ')', '{': '}', '[': ']'}[top]
                if c != expected:
                    print(f"Error: mismatched '{c}' at {line_num}:{col_num}, expected '{expected}' opened at {l}:{col}")
                    return False
        i += 1

    if stack:
        top, l, col = stack[-1]
        print(f"Error: unclosed '{top}' opened at {l}:{col}")
        return False
        
    print(f"{path}: All brackets balanced, no open strings/comments.")
    return True

print("Checking src/components/app.js:")
check_file('src/components/app.js')
print("Checking src/data/siteContent.js:")
check_file('src/data/siteContent.js')
