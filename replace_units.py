with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_units = """    this.units=[
      new Unit('p1','艾利乌德','领主','SWORD',28,10,5,5,5,'p',4,10),
      new Unit('p2','海克托尔','重甲','AXE',  38,7,9,2,3,'p',2,10),
      new Unit('p3','琳',     '骑士','LANCE',22,12,4,9,8,'p',5,10),
      new Unit('p4','露西亚',  '弓手','BOW',  18,9,2,6,4,'p',7,10),
      new Unit('e1','黑骑士', '领主','LANCE',28,10,5,5,5,'e',5,1),
      new Unit('e2','巴里尔', '重甲','AXE',  38,7,9,2,3,'e',3,1),
      new Unit('e3','佣兵',  '剑士','SWORD',22,12,4,9,8,'e',4,1),
      new Unit('e4','狙击手', '弓手','BOW',  18,9,2,6,4,'e',7,1),
    ];"""

new_units = """    this.units=[
      new Unit('p1','艾利乌德','领主','SWORD',28,10,5,5,5,'p',2,10),
      new Unit('p2','海克托尔','重甲','AXE',  38,7,9,2,3,'p',1,10),
      new Unit('p3','琳',     '骑士','LANCE',22,12,4,9,8,'p',3,10),
      new Unit('p4','露西亚',  '弓手','BOW',  18,9,2,6,4,'p',4,10),
      new Unit('e1','黑骑士', '领主','LANCE',28,10,5,5,5,'e',9,1),
      new Unit('e2','巴里尔', '重甲','AXE',  38,7,9,2,3,'e',10,1),
      new Unit('e3','佣兵',  '剑士','SWORD',22,12,4,9,8,'e',8,1),
      new Unit('e4','狙击手', '弓手','BOW',  18,9,2,6,4,'e',7,1),
    ];"""

if old_units in content:
    content = content.replace(old_units, new_units)
    print('Units repositioned successfully')
    with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print('Units pattern not found')
    idx = content.find("this.units=[")
    print(f'Unit block at: {idx}')
    print(repr(content[idx:idx+500]))
