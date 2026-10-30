with open('src/components/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect lines 950-1015
start_idx = code.find('// 5. Instantiate Planets')
end_idx = code.find('// 6. Interactive Raycasting')
print(code[start_idx:end_idx])
