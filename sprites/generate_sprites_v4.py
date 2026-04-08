#!/usr/bin/env python3
"""生成 v4 精灵图 - 更大胆的轮廓，更易辨认的形状，32x32显示于44x44格子"""
from PIL import Image, ImageDraw

# GBA FE 风格改良调色板 - 更饱和更易辨认
# Army: Blue = #3060d0, Red = #c03030
# Skin: #d4a870, #c09060
# Metal: #e0e0e0(银), #c0c0c0, #808080
# Nature: #40a040(绿), #307030(深绿), #204020(极深绿)
# Brown: #8b5e3c, #5c3a1e
# Gold: #f0c040
# Stone: #a0a0b0(浅灰), #606070(灰), #303040(深灰)
# Water: #5090d0, #306090

P = {
    'bk': (32,32,48),        # 0 深黑轮廓
    'wh': (224,224,224),      # 1 白
    'gy': (160,160,176),     # 2 灰
    'dg': (80,80,96),        # 3 暗灰
    'sk': (212,168,112),     # 4 肤色
    'br': (139,94,60),       # 5 棕色
    'db': (92,58,30),        # 6 深棕
    'lb': (80,144,208),      # 7 浅蓝水
    'bl': (48,96,208),       # 8 蓝色
    'db2': (32,64,160),      # 9 深蓝
    'gr': (64,160,64),       # 10 绿色
    'dg2': (32,96,32),       # 11 深绿
    'sa': (216,184,136),     # 12 沙色
    'ds': (160,120,80),      # 13 暗沙
    'rd': (192,48,48),       # 14 红色
    'gd': (240,192,64),      # 15 金色
    'db3': (80,64,48),       # 16 暗轮廓
    'st': (144,144,160),     # 17 石头色
    'dr': (48,80,160),       # 18 深红蓝
    'rd2': (224,80,48),     # 19 亮红
    'gl': (240,240,240),     # 20 高光白
    'dr2': (32,80,112),      # 21 暗红
    'dg3': (32,32,56),       # 22 极暗灰紫（用于暗处）
}

class DC:
    def __init__(self, draw, ox, oy):
        self.draw = draw
        self.ox = ox
        self.oy = oy
    def px(self, x, y, c):
        ax, ay = self.ox + x, self.oy + y
        if 0 <= ax < 512 and 0 <= ay < 96:
            self.draw.point((ax, ay), fill=c)
    def r(self, x, y, w, h, c):
        for py in range(y, y + h):
            for px_ in range(x, x + w):
                self.px(px_, py, c)
    def rr(self, x, y, w, h, c1, c2):
        """rect with top-left=c1, rest=c2 (3D effect)"""
        self.r(x, y, w, 1, c1)
        self.r(x, y, 1, h, c1)
        self.r(x+w-1, y, 1, h, c2)
        self.r(x, y+h-1, w, 1, c2)
        self.r(x+1, y+1, w-2, h-2, c2)

# ============ 地形 ============

def t_forest(c):
    # 地面
    c.r(0,26,32,6,P['dg2'])
    c.r(2,28,28,4,P['dg2'])
    # 树1 左
    c.r(3,10,8,18,P['dg2'])
    c.r(4,6,6,6,P['gr'])
    c.px(6,4,P['wh'])
    c.r(5,16,4,12,P['br'])
    # 树2 中
    c.r(11,6,10,22,P['dg2'])
    c.r(12,2,8,6,P['gr'])
    c.px(15,0,P['wh'])
    c.r(14,14,4,14,P['br'])
    c.px(15,16,P['db'])
    # 树3 右
    c.r(21,12,8,16,P['dg2'])
    c.r(22,8,6,6,P['gr'])
    c.r(23,16,4,12,P['br'])

def t_river(c):
    c.r(0,4,32,26,P['lb'])
    c.r(1,5,30,24,P['lb'])
    # 水流 - 横条纹
    for y in range(6,28,4):
        c.r(2,y,28,2,P['db2'])
    c.r(0,4,32,2,P['bl'])
    c.r(0,28,32,2,P['bl'])
    # 白色高光
    for i in range(4):
        c.px(4+i*7,8+i,P['wh'])
        c.px(6+i*7,14+i,P['wh'])

def t_mountain(c):
    c.r(2,18,28,14,P['dg'])
    c.r(4,12,24,10,P['gy'])
    c.r(6,8,20,8,P['st'])
    c.r(8,4,16,8,P['wh'])
    c.r(10,2,12,6,P['wh'])
    # 阴影
    c.r(2,18,4,14,P['db3'])
    # 轮廓
    c.r(2,18,28,1,P['bk'])
    c.r(2,31,28,1,P['bk'])

def t_ruins(c):
    c.r(0,24,32,8,P['dg'])
    c.r(2,26,28,6,P['st'])
    # 断柱
    c.r(3,12,6,16,P['st']); c.r(4,8,4,6,P['st'])
    c.r(13,14,5,14,P['st']); c.r(14,10,3,6,P['st'])
    c.r(22,6,7,22,P['st']); c.r(24,2,3,6,P['st'])
    # 碎石
    for x in [6,11,17,26]:
        c.px(x,28,P['gy'])
    c.r(2,24,28,1,P['bk'])

def t_hill(c):
    c.r(0,18,32,14,P['dg2'])
    c.r(2,14,28,8,P['gr'])
    c.r(4,10,24,8,P['gr'])
    c.r(8,6,16,8,P['sa'])
    c.r(10,4,12,4,P['wh'])
    # 轮廓
    c.r(0,18,32,1,P['bk'])
    c.r(0,31,32,1,P['bk'])
    # 草地细节
    for x in [3,9,16,22,27]:
        c.px(x,16,P['dg2'])

def t_wall(c):
    c.r(0,8,32,24,P['br'])
    c.r(2,10,28,20,P['ds'])
    # 顶部垛口
    for i in range(4):
        c.r(2+i*7,4,5,6,P['br'])
        c.r(3+i*7,2,3,4,P['ds'])
    c.r(0,8,32,1,P['bk'])
    # 门洞
    c.r(13,20,6,10,P['dg3'])
    c.r(13,20,6,1,P['bk'])
    c.r(13,29,6,1,P['bk'])
    c.r(13,20,1,10,P['bk'])
    c.r(18,20,1,10,P['bk'])

def t_bridge(c):
    # 河面下层
    c.r(0,24,32,8,P['lb'])
    c.r(1,25,30,6,P['db2'])
    # 木板
    c.r(0,14,32,10,P['br'])
    c.r(2,15,28,8,P['ds'])
    # 木板缝隙
    for i in range(5):
        c.r(2+i*6,15,1,8,P['db'])
    # 栏杆
    c.r(2,10,2,6,P['db']); c.r(3,9,1,1,P['br'])
    c.r(28,10,2,6,P['db']); c.r(28,9,1,1,P['br'])
    c.r(0,14,32,1,P['bk'])

def t_plains(c):
    c.r(0,0,32,32,P['dg2'])
    c.r(2,2,28,28,P['gr'])
    c.r(4,4,24,24,P['gr'])
    # 草地纹理
    for i in range(8):
        c.px(3+i*3+(i%2),3+i*3,P['sa'])
    # 小花
    c.px(6,8,P['rd']); c.px(18,12,P['rd'])
    c.px(10,22,P['gd']); c.px(26,6,P['rd'])
    c.r(0,0,32,1,P['bk'])
    c.r(0,31,32,1,P['bk'])

def t_blue_castle(c):
    # 主体城墙
    c.r(0,8,32,24,P['db2'])
    c.r(2,10,28,20,P['bl'])
    # 垛口
    for i in range(4):
        c.r(2+i*7,4,5,6,P['db2']); c.r(3+i*7,2,3,4,P['bl'])
    c.r(0,8,32,1,P['bk'])
    # 拱门
    c.r(13,18,6,12,P['dg3'])
    c.r(13,18,6,1,P['bk']); c.r(13,29,6,1,P['bk'])
    c.r(13,18,1,12,P['bk']); c.r(18,18,1,12,P['bk'])
    # 窗发光
    c.r(5,12,4,4,P['wh']); c.r(6,13,2,2,P['gl'])
    c.r(23,12,4,4,P['wh']); c.r(24,13,2,2,P['gl'])
    # 旗帜
    c.r(15,2,2,8,P['bl']); c.r(13,2,6,2,P['db2'])

def t_red_castle(c):
    c.r(0,8,32,24,P['dr2'])
    c.r(2,10,28,20,P['rd'])
    for i in range(4):
        c.r(2+i*7,4,5,6,P['dr2']); c.r(3+i*7,2,3,4,P['rd'])
    c.r(0,8,32,1,P['bk'])
    c.r(13,18,6,12,P['dg3'])
    c.r(13,18,6,1,P['bk']); c.r(13,29,6,1,P['bk'])
    c.r(13,18,1,12,P['bk']); c.r(18,18,1,12,P['bk'])
    c.r(5,12,4,4,P['wh']); c.r(6,13,2,2,P['gl'])
    c.r(23,12,4,4,P['wh']); c.r(24,13,2,2,P['gl'])
    c.r(15,2,2,8,P['rd']); c.r(13,2,6,2,P['dr2'])

# ============ 蓝色单位 ============

def u_lord(c):
    # 皇冠
    c.r(10,1,12,4,P['gd']); c.px(12,0,P['gd']); c.px(19,0,P['gd']); c.px(15,-1,P['gd'])
    # 脸
    c.r(10,5,12,7,P['sk']); c.px(12,7,P['bk']); c.px(18,7,P['bk'])
    # 身体
    c.r(8,12,16,14,P['bl']); c.r(10,14,12,10,P['db2'])
    # 披风
    c.r(4,12,6,16,P['bl']); c.r(22,12,6,16,P['bl'])
    c.r(6,12,2,14,P['db2']); c.r(24,12,2,14,P['db2'])
    # 武器-剑
    c.r(26,6,3,20,P['gy']); c.px(26,5,P['wh']); c.r(24,13,7,2,P['gd'])
    # 轮廓
    c.r(8,12,16,1,P['bk']); c.r(8,25,16,1,P['bk'])

def u_armor(c):
    # 头盔
    c.r(7,2,18,12,P['gy']); c.r(9,4,14,8,P['wh'])
    c.px(11,6,P['bk']); c.px(19,6,P['bk'])
    # 蓝色顶饰
    c.r(13,0,6,4,P['bl']); c.px(15,0,P['db2'])
    # 铠甲
    c.r(5,14,22,14,P['gy']); c.r(7,16,18,10,P['dg'])
    # 盾牌
    c.r(1,13,7,13,P['bl']); c.r(2,15,5,9,P['db2']); c.px(4,18,P['gd'])
    # 轮廓
    c.r(5,14,22,1,P['bk']); c.r(5,27,22,1,P['bk'])

def u_knight(c):
    # 头盔
    c.r(9,2,14,10,P['gy']); c.r(11,4,10,6,P['wh'])
    c.px(13,6,P['bk'])
    # 蓝色羽毛
    c.r(22,1,4,8,P['bl']); c.px(24,3,P['db2'])
    # 身体
    c.r(7,12,18,15,P['gy']); c.r(9,14,14,11,P['bl'])
    c.r(11,16,10,7,P['db2'])
    # 剑
    c.r(28,4,2,24,P['gy']); c.px(28,3,P['wh'])
    c.r(26,13,6,2,P['gd'])
    c.r(7,12,18,1,P['bk']); c.r(7,26,18,1,P['bk'])

def u_archer(c):
    # 帽子
    c.r(9,2,14,5,P['gr']); c.r(7,5,4,3,P['gr']); c.r(21,5,4,3,P['gr'])
    # 脸
    c.r(9,7,14,6,P['sk']); c.px(11,9,P['bk']); c.px(19,9,P['bk'])
    # 身体-蓝外套
    c.r(7,13,18,13,P['bl']); c.r(9,15,14,9,P['db2'])
    # 弓
    c.r(26,3,3,24,P['br']); c.px(28,5,P['db']); c.px(28,26,P['db'])
    c.r(2,10,4,14,P['db']); c.px(3,12,P['br'])
    # 箭筒
    c.r(2,14,4,12,P['db']); c.px(3,16,P['br'])
    c.r(7,13,18,1,P['bk']); c.r(7,25,18,1,P['bk'])

def u_swordsman(c):
    # 头发
    c.r(10,1,12,5,P['db'])
    # 脸
    c.r(10,6,12,6,P['sk']); c.px(12,8,P['bk']); c.px(18,8,P['bk'])
    # 身体
    c.r(7,12,18,15,P['bl']); c.r(9,14,14,11,P['db2'])
    # 剑
    c.r(28,2,2,26,P['gy']); c.px(28,1,P['wh']); c.r(26,11,6,2,P['gd'])
    # 腰带
    c.r(7,22,18,2,P['db']); c.px(15,22,P['gd'])
    c.r(7,12,18,1,P['bk']); c.r(7,26,18,1,P['bk'])

def u_axeman(c):
    # 头盔
    c.r(7,2,18,8,P['gy']); c.r(9,4,14,4,P['dg'])
    # 脸
    c.r(9,10,14,5,P['sk']); c.px(11,12,P['bk']); c.px(19,12,P['bk'])
    # 身体
    c.r(7,15,18,13,P['bl']); c.r(9,17,14,9,P['db2'])
    # 斧头
    c.r(28,4,3,8,P['gy']); c.r(28,10,3,4,P['dg'])
    c.r(29,12,2,10,P['br']); c.px(29,13,P['db'])
    c.r(7,15,18,1,P['bk']); c.r(7,27,18,1,P['bk'])

def u_lancer(c):
    # 头盔
    c.r(9,3,14,8,P['gy']); c.r(11,5,10,4,P['dg'])
    c.r(13,1,6,4,P['gd']); c.px(15,0,P['gd'])
    # 脸
    c.r(9,11,14,4,P['sk']); c.px(11,13,P['bk']); c.px(19,13,P['bk'])
    # 身体
    c.r(7,15,18,13,P['bl']); c.r(9,17,14,9,P['db2'])
    # 长矛
    c.r(30,0,2,30,P['br']); c.px(30,-1,P['gy'])
    c.r(28,0,6,5,P['gy']); c.px(30,-2,P['gy'])
    c.r(7,15,18,1,P['bk']); c.r(7,27,18,1,P['bk'])

def u_elf(c):
    # 尖耳
    c.r(2,7,5,4,P['sk']); c.px(1,5,P['sk']); c.r(25,7,5,4,P['sk']); c.px(30,5,P['sk'])
    # 金发
    c.r(10,1,12,7,P['gd']); c.px(8,3,P['ds']); c.px(22,3,P['ds'])
    # 脸
    c.r(10,8,12,6,P['sk']); c.px(12,10,P['bl']); c.px(18,10,P['bl'])
    c.px(12,9,P['wh']); c.px(18,9,P['wh'])
    # 身体
    c.r(7,14,18,14,P['gr']); c.r(9,16,14,10,P['dg2'])
    # 弓
    c.r(0,5,4,22,P['br']); c.px(2,7,P['db']); c.px(2,26,P['db'])
    c.r(4,9,2,14,P['db'])
    c.r(7,14,18,1,P['bk']); c.r(7,27,18,1,P['bk'])

# ============ 红色单位 ============

def r_lord(c):
    c.r(10,1,12,4,P['gd']); c.px(12,0,P['gd']); c.px(19,0,P['gd']); c.px(15,-1,P['gd'])
    c.r(10,5,12,7,P['sk']); c.px(12,7,P['bk']); c.px(18,7,P['bk'])
    c.r(8,12,16,14,P['rd']); c.r(10,14,12,10,P['dr2'])
    c.r(4,12,6,16,P['rd']); c.r(22,12,6,16,P['rd'])
    c.r(6,12,2,14,P['dr2']); c.r(24,12,2,14,P['dr2'])
    c.r(26,6,3,20,P['gy']); c.px(26,5,P['wh']); c.r(24,13,7,2,P['gd'])
    c.r(8,12,16,1,P['bk']); c.r(8,25,16,1,P['bk'])

def r_armor(c):
    c.r(7,2,18,12,P['gy']); c.r(9,4,14,8,P['wh'])
    c.px(11,6,P['bk']); c.px(19,6,P['bk'])
    c.r(13,0,6,4,P['rd']); c.px(15,0,P['dr2'])
    c.r(5,14,22,14,P['gy']); c.r(7,16,18,10,P['dg'])
    c.r(1,13,7,13,P['rd']); c.r(2,15,5,9,P['dr2']); c.px(4,18,P['gd'])
    c.r(5,14,22,1,P['bk']); c.r(5,27,22,1,P['bk'])

def r_knight(c):
    c.r(9,2,14,10,P['gy']); c.r(11,4,10,6,P['wh'])
    c.px(13,6,P['bk'])
    c.r(22,1,4,8,P['rd']); c.px(24,3,P['dr2'])
    c.r(7,12,18,15,P['gy']); c.r(9,14,14,11,P['rd'])
    c.r(11,16,10,7,P['dr2'])
    c.r(28,4,2,24,P['gy']); c.px(28,3,P['wh'])
    c.r(26,13,6,2,P['gd'])
    c.r(7,12,18,1,P['bk']); c.r(7,26,18,1,P['bk'])

def r_archer(c):
    c.r(9,2,14,5,P['gr']); c.r(7,5,4,3,P['gr']); c.r(21,5,4,3,P['gr'])
    c.r(9,7,14,6,P['sk']); c.px(11,9,P['bk']); c.px(19,9,P['bk'])
    c.r(7,13,18,13,P['rd']); c.r(9,15,14,9,P['dr2'])
    c.r(26,3,3,24,P['br']); c.px(28,5,P['db']); c.px(28,26,P['db'])
    c.r(2,10,4,14,P['dr2']); c.px(3,12,P['br'])
    c.r(2,14,4,12,P['dr2']); c.px(3,16,P['br'])
    c.r(7,13,18,1,P['bk']); c.r(7,25,18,1,P['bk'])

def r_swordsman(c):
    c.r(10,1,12,5,P['db'])
    c.r(10,6,12,6,P['sk']); c.px(12,8,P['bk']); c.px(18,8,P['bk'])
    c.r(7,12,18,15,P['rd']); c.r(9,14,14,11,P['dr2'])
    c.r(28,2,2,26,P['gy']); c.px(28,1,P['wh']); c.r(26,11,6,2,P['gd'])
    c.r(7,22,18,2,P['db']); c.px(15,22,P['gd'])
    c.r(7,12,18,1,P['bk']); c.r(7,26,18,1,P['bk'])

def r_axeman(c):
    c.r(7,2,18,8,P['gy']); c.r(9,4,14,4,P['dg'])
    c.r(9,10,14,5,P['sk']); c.px(11,12,P['bk']); c.px(19,12,P['bk'])
    c.r(7,15,18,13,P['rd']); c.r(9,17,14,9,P['dr2'])
    c.r(28,4,3,8,P['gy']); c.r(28,10,3,4,P['dg'])
    c.r(29,12,2,10,P['br']); c.px(29,13,P['db'])
    c.r(7,15,18,1,P['bk']); c.r(7,27,18,1,P['bk'])

def r_lancer(c):
    c.r(9,3,14,8,P['gy']); c.r(11,5,10,4,P['dg'])
    c.r(13,1,6,4,P['gd']); c.px(15,0,P['gd'])
    c.r(9,11,14,4,P['sk']); c.px(11,13,P['bk']); c.px(19,13,P['bk'])
    c.r(7,15,18,13,P['rd']); c.r(9,17,14,9,P['dr2'])
    c.r(30,0,2,30,P['br']); c.px(30,-1,P['gy'])
    c.r(28,0,6,5,P['gy']); c.px(30,-2,P['gy'])
    c.r(7,15,18,1,P['bk']); c.r(7,27,18,1,P['bk'])

def r_elf(c):
    c.r(2,7,5,4,P['sk']); c.px(1,5,P['sk']); c.r(25,7,5,4,P['sk']); c.px(30,5,P['sk'])
    c.r(10,1,12,7,P['gd']); c.px(8,3,P['ds']); c.px(22,3,P['ds'])
    c.r(10,8,12,6,P['sk']); c.px(12,10,P['rd']); c.px(18,10,P['rd'])
    c.px(12,9,P['wh']); c.px(18,9,P['wh'])
    c.r(7,14,18,14,P['gr']); c.r(9,16,14,10,P['dg2'])
    c.r(0,5,4,22,P['br']); c.px(2,7,P['db']); c.px(2,26,P['db'])
    c.r(4,9,2,14,P['db'])
    c.r(7,14,18,1,P['bk']); c.r(7,27,18,1,P['bk'])


def main():
    img = Image.new('RGBA', (512, 96), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 第一行: 地形
    terrain_funcs = [
        t_forest, t_river, t_mountain, t_ruins,
        t_hill, t_wall, t_bridge, t_plains,
        t_blue_castle, t_red_castle
    ]
    for i, func in enumerate(terrain_funcs):
        ctx = DC(draw, i*32, 0)
        func(ctx)

    # 第二行: 蓝色单位
    blue_funcs = [u_lord, u_armor, u_knight, u_archer, u_swordsman, u_axeman, u_lancer, u_elf]
    for i, func in enumerate(blue_funcs):
        ctx = DC(draw, i*32, 32)
        func(ctx)

    # 第三行: 红色单位
    red_funcs = [r_lord, r_armor, r_knight, r_archer, r_swordsman, r_axeman, r_lancer, r_elf]
    for i, func in enumerate(red_funcs):
        ctx = DC(draw, i*32, 64)
        func(ctx)

    out = "D:/Claudecodeworkspace/Projects/fe-bridge-game/sprites/terrain-units-sheet-v4.png"
    img.save(out)
    print(f"Saved: {out} ({img.size[0]}x{img.size[1]})")

    # 验证
    from PIL import Image as Im
    img2 = Im.open(out)
    def check(name, x, y, w=32, h=32):
        region = img2.crop((x, y, x+w, y+h))
        pixels = list(region.getdata())
        non_trans = [p for p in pixels if p[3] > 10]
        if not non_trans:
            print(f'  {name}: TRANSPARENT!')
        else:
            print(f'  {name}: OK ({len(non_trans)} px)')
    print("\nTerrain:")
    for i, n in enumerate(['FOREST','RIVER','MOUNTAIN','RUINS','HILL','WALL','BRIDGE','PLAINS','BLUEC','REDC']):
        check(n, i*32, 0)
    print("Blue units:")
    for i, n in enumerate(['LORD','ARMOR','KNIGHT','ARCHER','SWORD','AXE','LANCE','ELF']):
        check(n, i*32, 32)
    print("Red units:")
    for i, n in enumerate(['LORD','ARMOR','KNIGHT','ARCHER','SWORD','AXE','LANCE','ELF']):
        check(n, i*32, 64)

if __name__ == "__main__":
    main()
