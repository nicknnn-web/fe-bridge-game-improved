#!/usr/bin/env python3
"""生成精细像素精灵图 - 真正32x32像素, ps=1"""
from PIL import Image, ImageDraw

# GBA Fire Emblem 风格 16 色调色板
P = [
    (0,0,0),          # 0 黑
    (255,255,255),    # 1 白
    (136,136,136),   # 2 灰
    (68,68,68),       # 3 暗灰
    (184,136,108),    # 4 肤色
    (144,96,56),      # 5 棕色
    (72,48,32),       # 6 深棕
    (152,208,232),    # 7 浅蓝
    (104,160,208),    # 8 蓝
    (40,72,152),      # 9 深蓝
    (72,136,72),      # 10 绿
    (32,72,32),       # 11 深绿
    (216,184,136),    # 12 沙色
    (184,152,104),    # 13 暗沙
    (232,56,56),      # 14 红
    (200,160,40),     # 15 金
]

class DrawingContext:
    def __init__(self, draw, ox, oy):
        self.draw = draw
        self.ox = ox
        self.oy = oy
    def set_pixel(self, x, y, c):
        ax, ay = self.ox + x, self.oy + y
        if 0 <= ax < 512 and 0 <= ay < 96:
            self.draw.point((ax, ay), fill=c)
    def rect(self, x, y, w, h, c):
        for py in range(y, y+h):
            for px_ in range(x, x+w):
                self.set_pixel(px_, py, c)


def self.set_pixel(ox, oy, x, y, c):
    ax, ay = ox + x, oy + y
    if 0 <= ax < 512 and 0 <= ay < 96:
        draw.point((ax, ay), fill=c)

def self.rect(ox, oy, x, y, w, h, c):
    for py in range(y, y+h):
        for px_ in range(x, x+w):
            self.set_pixel(ox, oy, px_, py, c)

# ============ 地形 (第一行) ============

def terrain_forest(ox, oy):
    x, y = ox, oy
    # 地面
    self.rect(x+2, y+24, 28, 6, P[11])
    self.rect(x+4, y+26, 24, 4, P[10])
    # 树1 (左)
    self.rect(x+4, y+12, 10, 14, P[11])
    self.rect(x+6, y+8, 6, 8, P[10])
    self.set_pixel(x+8, y+6, P[10])
    self.rect(x+8, y+16, 2, 10, P[6])
    # 树2 (中，右边高点)
    self.rect(x+14, y+8, 12, 18, P[11])
    self.rect(x+16, y+4, 8, 8, P[10])
    self.set_pixel(x+18, y+2, P[12])
    self.rect(x+18, y+14, 3, 12, P[6])
    self.set_pixel(x+19, y+16, P[5])
    # 树3 (右，小)
    self.rect(x+24, y+14, 6, 12, P[11])
    self.rect(x+25, y+11, 4, 5, P[10])
    self.rect(x+26, y+18, 2, 8, P[6])

def terrain_river(ox, oy):
    x, y = ox, oy
    # 水面主体
    self.rect(x+2, y+6, 28, 20, P[7])
    self.rect(x+4, y+8, 24, 16, P[8])
    # 水流纹理 - 斜向波纹
    for i in range(3):
        self.rect(x+4+i*8, y+8+i*2, 6, 2, P[7])
        self.set_pixel(x+6+i*8, y+9+i*2, P[1])
    for i in range(3):
        self.rect(x+8+i*8, y+14+i*2, 6, 2, P[7])
        self.set_pixel(x+10+i*8, y+15+i*2, P[1])
    # 浅色边缘
    self.rect(x+2, y+6, 2, 20, P[8])
    self.rect(x+28, y+6, 2, 20, P[8])
    # 底部岩石
    self.rect(x+6, y+24, 8, 4, P[3])
    self.rect(x+20, y+24, 6, 4, P[3])
    self.set_pixel(x+8, y+24, P[2])
    self.set_pixel(x+22, y+25, P[2])

def terrain_mountain(ox, oy):
    x, y = ox, oy
    # 山体 (大三角形)
    self.rect(x+4, y+18, 24, 12, P[3])
    self.rect(x+6, y+14, 20, 8, P[2])
    self.rect(x+8, y+10, 16, 6, P[8])
    self.rect(x+10, y+6, 12, 6, P[7])
    # 雪顶
    self.rect(x+12, y+2, 8, 6, P[1])
    self.rect(x+10, y+6, 4, 2, P[1])
    self.rect(x+18, y+6, 4, 2, P[1])
    # 阴影
    self.rect(x+4, y+18, 4, 12, P[0])
    # 纹理线条
    self.set_pixel(x+10, y+12, P[3])
    self.set_pixel(x+14, y+10, P[3])
    self.set_pixel(x+18, y+12, P[3])

def terrain_ruins(ox, oy):
    x, y = ox, oy
    # 背景地面
    self.rect(x+2, y+22, 28, 8, P[3])
    self.rect(x+4, y+24, 24, 6, P[6])
    # 断裂石柱 左
    self.rect(x+3, y+8, 8, 16, P[2])
    self.rect(x+4, y+4, 6, 6, P[2])
    self.set_pixel(x+4, y+8, P[3])
    self.set_pixel(x+6, y+6, P[3])
    # 断裂石柱 中
    self.rect(x+13, y+12, 6, 12, P[2])
    self.rect(x+14, y+10, 4, 4, P[2])
    # 断裂石柱 右
    self.rect(x+22, y+6, 7, 18, P[2])
    self.rect(x+24, y+2, 4, 6, P[2])
    self.set_pixel(x+24, y+6, P[3])
    # 碎石
    self.set_pixel(x+8, y+26, P[5])
    self.set_pixel(x+12, y+28, P[5])
    self.set_pixel(x+18, y+26, P[5])
    self.set_pixel(x+26, y+28, P[5])
    self.set_pixel(x+10, y+24, P[3])
    self.set_pixel(x+20, y+24, P[3])

def terrain_hill(ox, oy):
    x, y = ox, oy
    # 大山丘
    self.rect(x+2, y+16, 28, 14, P[11])
    self.rect(x+4, y+12, 24, 8, P[10])
    self.rect(x+8, y+8, 16, 8, P[10])
    # 雪/高光顶
    self.rect(x+10, y+4, 12, 6, P[12])
    self.set_pixel(x+12, y+6, P[13])
    self.set_pixel(x+18, y+5, P[13])
    # 草地纹理
    self.set_pixel(x+6, y+14, P[11])
    self.set_pixel(x+14, y+16, P[11])
    self.set_pixel(x+24, y+14, P[11])
    self.set_pixel(x+20, y+18, P[11])
    # 阴影
    self.rect(x+2, y+26, 4, 4, P[11])

def terrain_wall(ox, oy):
    x, y = ox, oy
    # 城墙主体
    self.rect(x+2, y+10, 28, 20, P[5])
    self.rect(x+4, y+12, 24, 16, P[13])
    # 顶部垛口
    for i in range(4):
        self.rect(x+2+i*7, y+4, 5, 8, P[5])
        self.rect(x+3+i*7, y+2, 3, 4, P[13])
        self.set_pixel(x+4+i*7, y+6, P[3])
    # 砖缝纹理
    self.rect(x+4, y+16, 24, 1, P[6])
    self.rect(x+4, y+22, 24, 1, P[6])
    self.set_pixel(x+12, y+12, P[6])
    self.set_pixel(x+20, y+12, P[6])
    self.set_pixel(x+8, y+18, P[6])
    self.set_pixel(x+16, y+18, P[6])
    self.set_pixel(x+24, y+18, P[6])
    # 拱形门口
    self.rect(x+13, y+22, 6, 8, P[9])

def terrain_bridge(ox, oy):
    x, y = ox, oy
    # 河面 (下层)
    self.rect(x+2, y+20, 28, 8, P[7])
    self.rect(x+4, y+21, 24, 6, P[8])
    # 水波
    self.set_pixel(x+6, y+22, P[7])
    self.set_pixel(x+14, y+24, P[7])
    self.set_pixel(x+22, y+22, P[7])
    # 木板桥面
    self.rect(x+2, y+12, 28, 8, P[5])
    self.rect(x+4, y+13, 24, 6, P[13])
    # 木板缝隙
    for i in range(5):
        self.rect(x+4+i*5, y+13, 1, 6, P[6])
    # 栏杆
    self.rect(x+4, y+8, 3, 6, P[6])
    self.rect(x+25, y+8, 3, 6, P[6])
    self.set_pixel(x+5, y+7, P[5])
    self.set_pixel(x+26, y+7, P[5])
    # 铆钉
    self.set_pixel(x+5, y+10, P[15])
    self.set_pixel(x+26, y+10, P[15])

def terrain_plains(ox, oy):
    x, y = ox, oy
    # 草地
    self.rect(x+2, y+4, 28, 24, P[11])
    self.rect(x+4, y+6, 24, 20, P[10])
    # 草地纹理细节
    for i in range(6):
        sx = x+4+i*4+(i%2)*2
        self.set_pixel(sx, y+8, P[12])
        self.set_pixel(sx+2, y+12, P[12])
        self.set_pixel(sx, y+16, P[12])
        self.set_pixel(sx+2, y+20, P[12])
    # 小花
    self.set_pixel(x+8, y+10, P[14])
    self.set_pixel(x+20, y+16, P[14])
    self.set_pixel(x+14, y+24, P[15])
    self.set_pixel(x+24, y+8, P[1])
    self.set_pixel(x+6, y+22, P[1])

# ============ 蓝色系单位 (第二行) ============

def unit_lord_b(ox, oy):
    x, y = ox, oy
    # 皇冠
    self.rect(x+10, y+2, 12, 4, P[15])
    self.set_pixel(x+12, y+1, P[15])
    self.set_pixel(x+18, y+1, P[15])
    self.set_pixel(x+15, y+0, P[15])
    # 脸部
    self.rect(x+10, y+6, 12, 8, P[4])
    self.set_pixel(x+12, y+8, P[0])
    self.set_pixel(x+18, y+8, P[0])
    # 蓝披风
    self.rect(x+6, y+8, 6, 16, P[8])
    self.rect(x+20, y+8, 6, 16, P[8])
    self.rect(x+8, y+10, 2, 12, P[9])
    self.rect(x+22, y+10, 2, 12, P[9])
    # 铠甲
    self.rect(x+10, y+14, 12, 12, P[9])
    self.rect(x+12, y+16, 8, 8, P[8])
    # 武器-剑
    self.rect(x+24, y+4, 3, 20, P[2])
    self.rect(x+22, y+12, 7, 3, P[15])

def unit_armor_b(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+8, y+2, 16, 12, P[3])
    self.rect(x+10, y+4, 12, 8, P[2])
    self.set_pixel(x+12, y+6, P[0])
    self.set_pixel(x+18, y+6, P[0])
    # 蓝色顶饰
    self.rect(x+14, y+0, 4, 4, P[8])
    self.set_pixel(x+15, y+0, P[9])
    # 身体铠甲
    self.rect(x+6, y+14, 20, 14, P[3])
    self.rect(x+8, y+16, 16, 10, P[2])
    # 肩甲
    self.rect(x+4, y+14, 6, 8, P[3])
    self.rect(x+22, y+14, 6, 8, P[3])
    # 蓝盾牌
    self.rect(x+2, y+12, 8, 14, P[8])
    self.rect(x+4, y+14, 4, 10, P[9])
    self.set_pixel(x+5, y+18, P[15])

def unit_knight_b(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+10, y+2, 12, 10, P[2])
    self.rect(x+12, y+4, 8, 6, P[3])
    self.set_pixel(x+14, y+6, P[0])
    # 蓝色羽毛
    self.rect(x+22, y+2, 4, 8, P[8])
    self.rect(x+23, y+4, 2, 4, P[9])
    # 身体
    self.rect(x+8, y+12, 16, 14, P[2])
    self.rect(x+10, y+14, 12, 10, P[8])
    self.rect(x+12, y+16, 8, 6, P[9])
    # 剑
    self.rect(x+26, y+4, 3, 22, P[2])
    self.rect(x+24, y+14, 7, 3, P[15])

def unit_archer_b(ox, oy):
    x, y = ox, oy
    # 绿色帽子
    self.rect(x+10, y+2, 12, 6, P[10])
    self.rect(x+8, y+6, 4, 3, P[10])
    self.rect(x+20, y+6, 4, 3, P[10])
    # 脸部
    self.rect(x+10, y+8, 12, 7, P[4])
    self.set_pixel(x+12, y+10, P[0])
    self.set_pixel(x+18, y+10, P[0])
    # 身体-蓝外套
    self.rect(x+8, y+15, 16, 12, P[8])
    self.rect(x+10, y+17, 12, 8, P[9])
    # 弓
    self.rect(x+24, y+4, 4, 22, P[5])
    self.rect(x+26, y+8, 2, 14, P[6])
    # 箭筒
    self.rect(x+2, y+12, 6, 12, P[6])
    self.set_pixel(x+3, y+14, P[5])

def unit_swordsman_b(ox, oy):
    x, y = ox, oy
    # 头发
    self.rect(x+10, y+2, 12, 6, P[6])
    # 脸部
    self.rect(x+10, y+8, 12, 7, P[4])
    self.set_pixel(x+12, y+10, P[0])
    self.set_pixel(x+18, y+10, P[0])
    # 身体-蓝衣
    self.rect(x+8, y+15, 16, 12, P[8])
    self.rect(x+10, y+17, 12, 8, P[9])
    # 剑
    self.rect(x+26, y+4, 3, 22, P[2])
    self.rect(x+24, y+12, 7, 3, P[15])
    # 腰带
    self.rect(x+8, y+22, 16, 3, P[6])

def unit_axeman_b(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+8, y+2, 16, 8, P[3])
    self.rect(x+10, y+4, 12, 4, P[6])
    # 脸部
    self.rect(x+10, y+10, 12, 6, P[4])
    self.set_pixel(x+12, y+12, P[0])
    self.set_pixel(x+18, y+12, P[0])
    # 身体
    self.rect(x+8, y+16, 16, 12, P[8])
    self.rect(x+10, y+18, 12, 8, P[9])
    # 斧头
    self.rect(x+26, y+4, 5, 8, P[2])
    self.rect(x+26, y+10, 5, 4, P[3])
    self.rect(x+28, y+12, 2, 8, P[5])

def unit_lanceman_b(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+10, y+4, 12, 8, P[2])
    self.rect(x+14, y+2, 4, 4, P[15])
    self.set_pixel(x+15, y+1, P[15])
    # 脸部
    self.rect(x+10, y+12, 12, 5, P[4])
    self.set_pixel(x+12, y+14, P[0])
    self.set_pixel(x+18, y+14, P[0])
    # 身体-蓝甲
    self.rect(x+8, y+17, 16, 12, P[8])
    self.rect(x+10, y+19, 12, 8, P[9])
    # 长矛
    self.rect(x+28, y+2, 3, 28, P[5])
    self.rect(x+26, y+2, 7, 6, P[2])
    self.set_pixel(x+28, y+0, P[2])

def unit_elf_b(ox, oy):
    x, y = ox, oy
    # 尖耳
    self.rect(x+4, y+8, 6, 4, P[4])
    self.set_pixel(x+2, y+6, P[4])
    self.rect(x+22, y+8, 6, 4, P[4])
    self.set_pixel(x+28, y+6, P[4])
    # 金发
    self.rect(x+10, y+2, 12, 8, P[12])
    self.set_pixel(x+8, y+4, P[13])
    self.set_pixel(x+22, y+4, P[13])
    # 脸
    self.rect(x+10, y+10, 12, 7, P[4])
    self.set_pixel(x+12, y+12, P[8])
    self.set_pixel(x+18, y+12, P[8])
    self.set_pixel(x+12, y+11, P[1])
    self.set_pixel(x+18, y+11, P[1])
    # 身体-绿
    self.rect(x+8, y+17, 16, 12, P[10])
    self.rect(x+10, y+19, 12, 8, P[11])
    # 弓
    self.rect(x+2, y+6, 4, 22, P[5])
    self.rect(x+4, y+10, 2, 14, P[6])

# ============ 红色系单位 (第三行) ============

def unit_lord_r(ox, oy):
    x, y = ox, oy
    # 皇冠
    self.rect(x+10, y+2, 12, 4, P[15])
    self.set_pixel(x+12, y+1, P[15])
    self.set_pixel(x+18, y+1, P[15])
    self.set_pixel(x+15, y+0, P[15])
    # 脸部
    self.rect(x+10, y+6, 12, 8, P[4])
    self.set_pixel(x+12, y+8, P[0])
    self.set_pixel(x+18, y+8, P[0])
    # 红披风
    self.rect(x+6, y+8, 6, 16, P[14])
    self.rect(x+20, y+8, 6, 16, P[14])
    self.rect(x+8, y+10, 2, 12, P[5])
    self.rect(x+22, y+10, 2, 12, P[5])
    # 铠甲-红
    self.rect(x+10, y+14, 12, 12, P[14])
    self.rect(x+12, y+16, 8, 8, P[5])
    # 剑
    self.rect(x+24, y+4, 3, 20, P[2])
    self.rect(x+22, y+12, 7, 3, P[15])

def unit_armor_r(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+8, y+2, 16, 12, P[3])
    self.rect(x+10, y+4, 12, 8, P[2])
    self.set_pixel(x+12, y+6, P[0])
    self.set_pixel(x+18, y+6, P[0])
    # 红色顶饰
    self.rect(x+14, y+0, 4, 4, P[14])
    self.set_pixel(x+15, y+0, P[5])
    # 身体铠甲
    self.rect(x+6, y+14, 20, 14, P[3])
    self.rect(x+8, y+16, 16, 10, P[2])
    # 肩甲
    self.rect(x+4, y+14, 6, 8, P[3])
    self.rect(x+22, y+14, 6, 8, P[3])
    # 红盾牌
    self.rect(x+2, y+12, 8, 14, P[14])
    self.rect(x+4, y+14, 4, 10, P[5])
    self.set_pixel(x+5, y+18, P[15])

def unit_knight_r(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+10, y+2, 12, 10, P[2])
    self.rect(x+12, y+4, 8, 6, P[3])
    self.set_pixel(x+14, y+6, P[0])
    # 红色羽毛
    self.rect(x+22, y+2, 4, 8, P[14])
    self.rect(x+23, y+4, 2, 4, P[5])
    # 身体
    self.rect(x+8, y+12, 16, 14, P[2])
    self.rect(x+10, y+14, 12, 10, P[14])
    self.rect(x+12, y+16, 8, 6, P[5])
    # 剑
    self.rect(x+26, y+4, 3, 22, P[2])
    self.rect(x+24, y+14, 7, 3, P[15])

def unit_archer_r(ox, oy):
    x, y = ox, oy
    # 绿帽子
    self.rect(x+10, y+2, 12, 6, P[10])
    self.rect(x+8, y+6, 4, 3, P[10])
    self.rect(x+20, y+6, 4, 3, P[10])
    # 脸部
    self.rect(x+10, y+8, 12, 7, P[4])
    self.set_pixel(x+12, y+10, P[0])
    self.set_pixel(x+18, y+10, P[0])
    # 身体-红外套
    self.rect(x+8, y+15, 16, 12, P[14])
    self.rect(x+10, y+17, 12, 8, P[5])
    # 弓
    self.rect(x+24, y+4, 4, 22, P[5])
    self.rect(x+26, y+8, 2, 14, P[6])
    # 箭筒
    self.rect(x+2, y+12, 6, 12, P[6])
    self.set_pixel(x+3, y+14, P[5])

def unit_swordsman_r(ox, oy):
    x, y = ox, oy
    # 头发
    self.rect(x+10, y+2, 12, 6, P[6])
    # 脸部
    self.rect(x+10, y+8, 12, 7, P[4])
    self.set_pixel(x+12, y+10, P[0])
    self.set_pixel(x+18, y+10, P[0])
    # 身体-红外衣
    self.rect(x+8, y+15, 16, 12, P[14])
    self.rect(x+10, y+17, 12, 8, P[5])
    # 剑
    self.rect(x+26, y+4, 3, 22, P[2])
    self.rect(x+24, y+12, 7, 3, P[15])
    # 腰带
    self.rect(x+8, y+22, 16, 3, P[6])

def unit_axeman_r(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+8, y+2, 16, 8, P[3])
    self.rect(x+10, y+4, 12, 4, P[6])
    # 脸部
    self.rect(x+10, y+10, 12, 6, P[4])
    self.set_pixel(x+12, y+12, P[0])
    self.set_pixel(x+18, y+12, P[0])
    # 身体
    self.rect(x+8, y+16, 16, 12, P[14])
    self.rect(x+10, y+18, 12, 8, P[5])
    # 斧头
    self.rect(x+26, y+4, 5, 8, P[2])
    self.rect(x+26, y+10, 5, 4, P[3])
    self.rect(x+28, y+12, 2, 8, P[5])

def unit_lanceman_r(ox, oy):
    x, y = ox, oy
    # 头盔
    self.rect(x+10, y+4, 12, 8, P[2])
    self.rect(x+14, y+2, 4, 4, P[15])
    self.set_pixel(x+15, y+1, P[15])
    # 脸部
    self.rect(x+10, y+12, 12, 5, P[4])
    self.set_pixel(x+12, y+14, P[0])
    self.set_pixel(x+18, y+14, P[0])
    # 身体-红甲
    self.rect(x+8, y+17, 16, 12, P[14])
    self.rect(x+10, y+19, 12, 8, P[5])
    # 长矛
    self.rect(x+28, y+2, 3, 28, P[5])
    self.rect(x+26, y+2, 7, 6, P[2])
    self.set_pixel(x+28, y+0, P[2])

def unit_elf_r(ox, oy):
    x, y = ox, oy
    # 尖耳
    self.rect(x+4, y+8, 6, 4, P[4])
    self.set_pixel(x+2, y+6, P[4])
    self.rect(x+22, y+8, 6, 4, P[4])
    self.set_pixel(x+28, y+6, P[4])
    # 金发
    self.rect(x+10, y+2, 12, 8, P[12])
    self.set_pixel(x+8, y+4, P[13])
    self.set_pixel(x+22, y+4, P[13])
    # 脸
    self.rect(x+10, y+10, 12, 7, P[4])
    self.set_pixel(x+12, y+12, P[14])
    self.set_pixel(x+18, y+12, P[14])
    self.set_pixel(x+12, y+11, P[1])
    self.set_pixel(x+18, y+11, P[1])
    # 身体-绿
    self.rect(x+8, y+17, 16, 12, P[10])
    self.rect(x+10, y+19, 12, 8, P[11])
    # 弓
    self.rect(x+2, y+6, 4, 22, P[5])
    self.rect(x+4, y+10, 2, 14, P[6])


def main():
    # 512x96 (16列 x 3行 x 32x32)
    img = Image.new('RGBA', (512, 96), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 第一行: 地形
    terrain_funcs = [
        terrain_forest, terrain_river, terrain_mountain, terrain_ruins,
        terrain_hill, terrain_wall, terrain_bridge, terrain_plains
    ]
    for i, func in enumerate(terrain_funcs):
        ctx = DrawingContext(draw, i*32, 0); func(ctx, i*32, 0)

    # 第二行: 蓝色单位
    blue_funcs = [
        unit_lord_b, unit_armor_b, unit_knight_b, unit_archer_b,
        unit_swordsman_b, unit_axeman_b, unit_lanceman_b, unit_elf_b
    ]
    for i, func in enumerate(blue_funcs):
        func(draw, i*32, 32)

    # 第三行: 红色单位
    red_funcs = [
        unit_lord_r, unit_armor_r, unit_knight_r, unit_archer_r,
        unit_swordsman_r, unit_axeman_r, unit_lanceman_r, unit_elf_r
    ]
    for i, func in enumerate(red_funcs):
        func(draw, i*32, 64)

    out = "D:/Claudecodeworkspace/Projects/fe-bridge-game/sprites/terrain-units-sheet-v2.png"
    img.save(out)
    print(f"Saved: {out} ({img.size[0]}x{img.size[1]})")

if __name__ == "__main__":
    main()
