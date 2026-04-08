with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_map = """const MAP = [
  [2,0,4,1,0,0,0,0,1,4,0,2],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,0,0,1,0,0,0,0],
  [4,0,0,0,0,0,0,0,0,0,0,4],
  [0,0,1,0,0,0,0,0,0,1,0,0],
  [5,5,5,5,5,6,6,5,5,5,5,5],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,0,0,0,0,0,0,1,0,0],
  [4,0,0,0,0,0,0,0,0,0,0,4],
  [0,0,0,0,1,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0],
  [3,0,4,1,0,0,0,0,1,4,0,3],
];"""

new_map = """const MAP = [
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

if old_map in content:
    content = content.replace(old_map, new_map)
    print('Map replaced successfully')
else:
    print('Map pattern not found')
    # Find the actual map
    idx = content.find('const MAP = [')
    if idx >= 0:
        snippet = content[idx:idx+600]
        print('Found map at:', idx)
        print(repr(snippet))

# Also update unit positions for new map
# Player units (west side, team='p')
# Enemy units (east side, team='e')

old_units = """this.units=[
  new Unit(0,'领主','领主','SWORD',28,10,5,5,5,'p',1,10),
  new Unit(1,'骑士','骑士','LANCE',24,10,5,9,7,'p',4,10),
  new Unit(2,'重甲','重甲','AXE',38,7,9,2,3,'p',7,10),
  new Unit(3,'弓手','弓手','BOW',18,9,2,6,4,'p',9,10),
  new Unit(4,'敌领主','领主','SWORD',28,10,5,5,5,'e',10,1),
  new Unit(5,'敌骑士','骑士','LANCE',24,10,5,9,7,'e',7,1),
  new Unit(6,'敌重甲','重甲','AXE',38,7,9,2,3,'e',4,1),
  new Unit(7,'敌弓手','弓手','BOW',18,9,2,6,4,'e',1,1),
];"""

new_units = """this.units=[
  new Unit(0,'领主','领主','SWORD',28,10,5,5,5,'p',1,10),
  new Unit(1,'骑士','骑士','LANCE',24,10,5,9,7,'p',1,7),
  new Unit(2,'重甲','重甲','AXE',38,7,9,2,3,'p',2,9),
  new Unit(3,'弓手','弓手','BOW',18,9,2,6,4,'p',1,8),
  new Unit(4,'敌领主','领主','SWORD',28,10,5,5,5,'e',10,1),
  new Unit(5,'敌骑士','骑士','LANCE',24,10,5,9,7,'e',10,4),
  new Unit(6,'敌重甲','重甲','AXE',38,7,9,2,3,'e',9,2),
  new Unit(7,'敌弓手','弓手','BOW',18,9,2,6,4,'e',10,3),
];"""

if old_units in content:
    content = content.replace(old_units, new_units)
    print('Units repositioned')
else:
    print('Units pattern not found')
    idx = content.find('this.units=[\n]')
    if idx >= 0:
        snippet = content[idx:idx+400]
        print(repr(snippet))

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)
