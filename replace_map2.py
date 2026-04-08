with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_map = """const MAP = [
  [3,0,0,0,0,0,0,0,0,0,0,2],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,0,0,0,0,0,0,0,0,0],
  [0,0,1,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [5,5,5,5,5,6,6,5,5,5,5,5],
  [0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [2,0,0,0,0,0,0,0,0,0,0,3],
];"""

new_map = """const MAP = [
  [0,0,0,0,0,1,0,1,0,0,0,0],
  [0,0,0,0,0,1,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,0,0,1,0,0],
  [5,5,5,5,5,6,6,5,5,5,5,5],
  [0,0,1,0,0,0,0,0,0,0,0,0],
  [0,0,1,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [1,0,0,0,0,1,0,1,0,0,0,1],
];"""

if old_map in content:
    content = content.replace(old_map, new_map)
    print('Map replaced')
else:
    print('Pattern not found, trying with different whitespace')
    # Try line by line
    idx = content.find('const MAP = [')
    print(f'MAP at: {idx}')
    snippet = content[idx:idx+800]
    print(repr(snippet[:500]))

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)
