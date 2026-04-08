with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern - try to find the current map block
old_map = """  [3,0,0,0,0,0,0,0,0,0,0,2],
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
  [2,0,0,0,0,0,0,0,0,0,0,3],"""

# New map: "防守反击"战术
# 蓝方(玩家)底部，西侧森林纵深，东侧相对开阔
# 红方(敌方)顶部，东侧森林较多，可以包抄
# 中央河流 = 天然屏障，两座桥 = 必争之地
new_map = """  [3,0,0,0,0,0,0,0,0,0,0,0],
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

if old_map in content:
    content = content.replace(old_map, new_map)
    print('Map replaced successfully')
else:
    print('Map pattern not found')
    idx = content.find('const MAP = [')
    if idx >= 0:
        snippet = content[idx:idx+900]
        print('Found MAP:')
        print(repr(snippet))

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)
