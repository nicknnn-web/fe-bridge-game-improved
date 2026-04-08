with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The map currently has errors. Let me find and replace with correct asymmetric map.
# Design: 4 castles as before, but forests/mountains heavily asymmetric
# Player (blue, south): blue castles at (0,11) and (11,11) - bottom row
# Enemy (red, north): red castles at (0,0) and (11,0) - top row
# Asymmetric forests create tactical depth

old_map = """  [3,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0,0,0,1],
  [5,5,5,5,5,6,6,5,5,5,5,5],
  [0,0,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,2],"""

# New asymmetric tactical map
# Player (south/blue): blue castles at (0,11) and (11,11) - bottom row, symmetric
# Enemy (north/red): red castles at (0,0) and (11,0) - top row, symmetric
# BUT: terrain is heavily asymmetric!
# Player side (south/bottom): dense forests on LEFT side - defensive depth
# Enemy side (north/top): forests on RIGHT side - offensive staging areas
# Central river + 2 bridges = the contested zone
new_map = """  [2,0,0,0,0,0,0,0,0,0,0,3],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,1,1,0,0,0,0,0,0,0,0,0],
  [5,5,5,5,5,6,6,5,5,5,5,5],
  [0,0,0,0,0,0,0,0,0,1,1,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [3,0,0,0,0,0,0,0,0,0,0,2],"""

if old_map in content:
    content = content.replace(old_map, new_map)
    print('Corrected map replaced successfully')
else:
    print('Pattern not found, finding current map...')
    idx = content.find('const MAP = [')
    if idx >= 0:
        snippet = content[idx:idx+1000]
        print(repr(snippet))

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)
