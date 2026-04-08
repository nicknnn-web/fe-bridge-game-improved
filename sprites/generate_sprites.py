#!/usr/bin/env python3
"""生成 GBA 火焰纹章风格的像素 sprite sheet - 256x64, 8x2 布局，无边框"""

from PIL import Image, ImageDraw

# GBA 火焰纹章 16 色复古调色板
PALETTE = [
    (0, 0, 0),           # 0: 黑
    (255, 255, 255),     # 1: 白
    (136, 136, 136),     # 2: 灰
    (68, 68, 68),        # 3: 暗灰
    (184, 136, 108),     # 4: 肤色/浅棕
    (144, 96, 56),       # 5: 棕色
    (72, 48, 32),        # 6: 深棕
    (152, 208, 232),     # 7: 浅蓝(天空)
    (104, 160, 208),     # 8: 蓝色
    (40, 72, 152),       # 9: 深蓝
    (72, 136, 72),       # 10: 绿色
    (32, 72, 32),        # 11: 深绿
    (216, 184, 136),     # 12: 沙色
    (184, 152, 104),     # 13: 暗沙
    (232, 56, 56),       # 14: 红色
    (168, 168, 0),       # 15: 金色
]

# 像素风格辅助函数
def set_pixel(draw, x, y, color, size=1):
    """绘制像素块"""
    draw.rectangle([x, y, x + size - 1, y + size - 1], fill=color)

def fill_rect(draw, x, y, w, h, color, pixel_size=2):
    """填充像素矩形"""
    for py in range(y, y + h, pixel_size):
        for px in range(x, x + w, pixel_size):
            draw.rectangle([px, py, px + pixel_size - 1, py + pixel_size - 1], fill=color)

# 图标内偏移：1px 透明边距
ICON_OX = 1
ICON_OY = 1

# 地形绘制函数
def draw_forest(draw, ox, oy, ps=2):
    """森林"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 树冠 (绿色塔形)
    fill_rect(draw, x + 6, y + 2, 16, 8, c[11], ps)   # 深绿底
    fill_rect(draw, x + 8, y + 4, 12, 6, c[10], ps)    # 绿色
    fill_rect(draw, x + 10, y + 6, 8, 4, c[12], ps)    # 暗沙高光
    # 树干
    fill_rect(draw, x + 12, y + 10, 4, 10, c[6], ps)   # 深棕
    set_pixel(draw, x + 13, y + 12, c[5], ps)
    set_pixel(draw, x + 14, y + 14, c[5], ps)

def draw_river(draw, ox, oy, ps=2):
    """河流"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 水面
    fill_rect(draw, x + 2, y + 4, 26, 20, c[7], ps)    # 浅蓝
    fill_rect(draw, x + 4, y + 6, 22, 16, c[8], ps)     # 蓝色
    # 水流波纹
    fill_rect(draw, x + 6, y + 8, 6, 2, c[10], ps)
    fill_rect(draw, x + 14, y + 12, 8, 2, c[10], ps)
    fill_rect(draw, x + 8, y + 16, 6, 2, c[10], ps)
    # 高光
    set_pixel(draw, x + 10, y + 8, c[1], ps)
    set_pixel(draw, x + 18, y + 12, c[1], ps)

def draw_mountain(draw, ox, oy, ps=2):
    """山脉"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 山体 (三角形)
    fill_rect(draw, x + 4, y + 16, 22, 10, c[11], ps)   # 深绿底
    fill_rect(draw, x + 6, y + 12, 18, 8, c[9], ps)     # 深蓝山体
    fill_rect(draw, x + 8, y + 8, 12, 6, c[8], ps)      # 蓝色
    fill_rect(draw, x + 10, y + 4, 8, 4, c[1], ps)      # 白雪/高光
    set_pixel(draw, x + 12, y + 6, c[2], ps)

def draw_ruins(draw, ox, oy, ps=2):
    """废墟"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 残垣
    fill_rect(draw, x + 2, y + 10, 10, 16, c[6], ps)    # 深棕左墙
    fill_rect(draw, x + 16, y + 6, 10, 20, c[6], ps)    # 深棕右墙
    # 碎石
    fill_rect(draw, x + 4, y + 22, 4, 4, c[5], ps)
    fill_rect(draw, x + 20, y + 22, 4, 4, c[5], ps)
    # 裂缝/暗部
    set_pixel(draw, x + 6, y + 12, c[3], ps)
    set_pixel(draw, x + 18, y + 8, c[3], ps)
    # 顶部破损
    set_pixel(draw, x + 4, y + 10, c[1], ps)
    set_pixel(draw, x + 14, y + 8, c[1], ps)

def draw_hills(draw, ox, oy, ps=2):
    """丘陵"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 小山丘
    fill_rect(draw, x + 2, y + 14, 26, 12, c[11], ps)   # 深绿底
    fill_rect(draw, x + 4, y + 10, 22, 8, c[10], ps)    # 绿色
    fill_rect(draw, x + 8, y + 6, 12, 6, c[12], ps)     # 沙色高光
    # 草地细节
    set_pixel(draw, x + 6, y + 12, c[11], ps)
    set_pixel(draw, x + 18, y + 14, c[11], ps)

def draw_wall(draw, ox, oy, ps=2):
    """城墙"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 城墙主体
    fill_rect(draw, x + 2, y + 6, 26, 20, c[5], ps)     # 棕色
    # 城垛
    fill_rect(draw, x + 2, y + 2, 6, 6, c[5], ps)
    fill_rect(draw, x + 11, y + 2, 6, 6, c[5], ps)
    fill_rect(draw, x + 20, y + 2, 6, 6, c[5], ps)
    # 暗部阴影
    fill_rect(draw, x + 2, y + 20, 26, 6, c[6], ps)
    # 高光
    fill_rect(draw, x + 4, y + 4, 2, 2, c[4], ps)
    fill_rect(draw, x + 13, y + 4, 2, 2, c[4], ps)
    fill_rect(draw, x + 22, y + 4, 2, 2, c[4], ps)

def draw_bridge(draw, ox, oy, ps=2):
    """桥梁"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 木板桥面
    fill_rect(draw, x + 2, y + 10, 26, 8, c[5], ps)      # 棕色
    # 木板纹理
    for i in range(4, 26, 4):
        set_pixel(draw, x + i, y + 10, c[6], ps)
        set_pixel(draw, x + i, y + 16, c[6], ps)
    # 栏杆
    fill_rect(draw, x + 4, y + 6, 4, 6, c[6], ps)
    fill_rect(draw, x + 22, y + 6, 4, 6, c[6], ps)
    # 河流水面
    fill_rect(draw, x + 2, y + 20, 12, 6, c[7], ps)
    fill_rect(draw, x + 16, y + 20, 12, 6, c[7], ps)

def draw_plains(draw, ox, oy, ps=2):
    """平地"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 草地
    fill_rect(draw, x + 2, y + 4, 26, 22, c[11], ps)    # 深绿底
    fill_rect(draw, x + 4, y + 6, 22, 18, c[10], ps)    # 绿色
    # 草地细节
    set_pixel(draw, x + 8, y + 10, c[12], ps)
    set_pixel(draw, x + 16, y + 14, c[12], ps)
    set_pixel(draw, x + 22, y + 8, c[12], ps)
    set_pixel(draw, x + 12, y + 18, c[12], ps)

# 单位绘制函数
def draw_lord(draw, ox, oy, ps=2):
    """领主"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 皇冠
    fill_rect(draw, x + 8, y + 0, 12, 4, c[15], ps)     # 金色
    set_pixel(draw, x + 10, y + 2, c[14], ps)
    set_pixel(draw, x + 14, y + 2, c[14], ps)
    set_pixel(draw, x + 18, y + 2, c[14], ps)
    # 脸部
    fill_rect(draw, x + 8, y + 4, 12, 10, c[4], ps)     # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 8, c[0], ps)
    set_pixel(draw, x + 16, y + 8, c[0], ps)
    # 披风
    fill_rect(draw, x + 4, y + 6, 6, 18, c[14], ps)     # 红色
    fill_rect(draw, x + 18, y + 6, 6, 18, c[14], ps)    # 红色
    # 身体
    fill_rect(draw, x + 8, y + 14, 12, 12, c[5], ps)     # 棕色铠甲
    # 武器/权杖
    fill_rect(draw, x + 12, y + 2, 4, 24, c[15], ps)    # 金色权杖
    set_pixel(draw, x + 12, y + 0, c[15], ps)

def draw_knight_heavy(draw, ox, oy, ps=2):
    """重甲骑士"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 头盔
    fill_rect(draw, x + 6, y + 0, 16, 12, c[3], ps)      # 暗灰
    fill_rect(draw, x + 8, y + 2, 12, 8, c[2], ps)      # 灰色
    # 面罩缝隙
    set_pixel(draw, x + 10, y + 6, c[0], ps)
    set_pixel(draw, x + 14, y + 6, c[0], ps)
    # 头盔顶部
    fill_rect(draw, x + 10, y + 0, 8, 2, c[8], ps)       # 蓝色装饰
    # 身体铠甲
    fill_rect(draw, x + 4, y + 12, 20, 16, c[3], ps)    # 暗灰
    fill_rect(draw, x + 6, y + 14, 16, 12, c[2], ps)    # 灰色
    # 肩甲
    fill_rect(draw, x + 2, y + 12, 6, 8, c[3], ps)
    fill_rect(draw, x + 20, y + 12, 6, 8, c[3], ps)
    # 盾牌
    fill_rect(draw, x + 0, y + 10, 8, 14, c[8], ps)     # 蓝色盾牌
    set_pixel(draw, x + 3, y + 14, c[15], ps)           # 金色纹章

def draw_knight(draw, ox, oy, ps=2):
    """骑士"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 头盔
    fill_rect(draw, x + 8, y + 0, 12, 10, c[2], ps)     # 灰色
    fill_rect(draw, x + 10, y + 2, 8, 6, c[3], ps)      # 暗灰面罩
    # 面罩缝隙
    set_pixel(draw, x + 12, y + 4, c[0], ps)
    # 羽毛
    fill_rect(draw, x + 18, y + 0, 4, 8, c[14], ps)     # 红色羽毛
    # 身体铠甲
    fill_rect(draw, x + 6, y + 10, 16, 14, c[2], ps)    # 灰色
    fill_rect(draw, x + 8, y + 12, 12, 10, c[8], ps)   # 蓝色内衬
    # 剑
    fill_rect(draw, x + 22, y + 6, 4, 20, c[2], ps)     # 剑身银
    fill_rect(draw, x + 20, y + 12, 8, 4, c[15], ps)    # 剑柄金色

def draw_archer(draw, ox, oy, ps=2):
    """弓手"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 帽子
    fill_rect(draw, x + 8, y + 0, 12, 6, c[10], ps)      # 绿色帽子
    set_pixel(draw, x + 6, y + 4, c[10], ps)
    set_pixel(draw, x + 20, y + 4, c[10], ps)
    # 脸部
    fill_rect(draw, x + 8, y + 6, 12, 8, c[4], ps)       # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 8, c[0], ps)
    set_pixel(draw, x + 16, y + 8, c[0], ps)
    # 身体/外套
    fill_rect(draw, x + 6, y + 14, 16, 12, c[10], ps)   # 绿色
    # 弓
    fill_rect(draw, x + 20, y + 2, 4, 24, c[5], ps)     # 弓身
    fill_rect(draw, x + 22, y + 6, 2, 16, c[6], ps)     # 弓弦
    # 箭筒
    fill_rect(draw, x + 0, y + 10, 6, 12, c[6], ps)     # 深棕箭筒

def draw_swordsman(draw, ox, oy, ps=2):
    """剑士"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 头发
    fill_rect(draw, x + 8, y + 0, 12, 6, c[6], ps)       # 深棕头发
    # 脸部
    fill_rect(draw, x + 8, y + 6, 12, 8, c[4], ps)       # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 8, c[0], ps)
    set_pixel(draw, x + 16, y + 8, c[0], ps)
    # 身体
    fill_rect(draw, x + 6, y + 14, 16, 12, c[5], ps)    # 棕色外衣
    # 剑
    fill_rect(draw, x + 22, y + 4, 4, 22, c[2], ps)     # 剑身银
    fill_rect(draw, x + 20, y + 10, 8, 4, c[15], ps)    # 剑柄金
    # 腰带
    fill_rect(draw, x + 6, y + 20, 16, 4, c[6], ps)     # 深棕腰带

def draw_axeman(draw, ox, oy, ps=2):
    """斧兵"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 头发/头盔
    fill_rect(draw, x + 6, y + 0, 16, 8, c[3], ps)      # 暗灰头盔
    fill_rect(draw, x + 8, y + 2, 12, 4, c[6], ps)      # 深棕头发
    # 脸部
    fill_rect(draw, x + 8, y + 8, 12, 6, c[4], ps)      # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 10, c[0], ps)
    set_pixel(draw, x + 16, y + 10, c[0], ps)
    # 身体
    fill_rect(draw, x + 6, y + 14, 16, 12, c[5], ps)    # 棕色
    # 斧头
    fill_rect(draw, x + 22, y + 0, 6, 8, c[2], ps)      # 斧刃银
    fill_rect(draw, x + 22, y + 6, 6, 4, c[3], ps)      # 暗灰
    fill_rect(draw, x + 24, y + 8, 2, 8, c[5], ps)      # 斧柄

def draw_pikeman(draw, ox, oy, ps=2):
    """枪兵"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 头盔
    fill_rect(draw, x + 8, y + 0, 12, 8, c[2], ps)      # 灰色
    fill_rect(draw, x + 12, y + 0, 4, 4, c[15], ps)     # 金色顶饰
    # 脸部
    fill_rect(draw, x + 8, y + 8, 12, 6, c[4], ps)      # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 10, c[0], ps)
    set_pixel(draw, x + 16, y + 10, c[0], ps)
    # 身体
    fill_rect(draw, x + 6, y + 14, 16, 12, c[8], ps)   # 蓝色
    # 长矛
    fill_rect(draw, x + 24, y + 0, 4, 28, c[5], ps)    # 矛身
    fill_rect(draw, x + 22, y + 0, 8, 8, c[2], ps)     # 矛头银

def draw_elf(draw, ox, oy, ps=2):
    """精灵"""
    c = PALETTE
    x, y = ox + ICON_OX, oy + ICON_OY
    # 尖耳朵
    fill_rect(draw, x + 2, y + 6, 6, 4, c[4], ps)
    set_pixel(draw, x + 0, y + 4, c[4], ps)
    fill_rect(draw, x + 20, y + 6, 6, 4, c[4], ps)
    set_pixel(draw, x + 26, y + 4, c[4], ps)
    # 头发
    fill_rect(draw, x + 8, y + 0, 12, 8, c[12], ps)     # 沙色长发
    # 脸部
    fill_rect(draw, x + 8, y + 6, 12, 8, c[4], ps)      # 肤色
    # 眼睛
    set_pixel(draw, x + 10, y + 8, c[8], ps)             # 蓝色眼睛
    set_pixel(draw, x + 16, y + 8, c[8], ps)
    set_pixel(draw, x + 10, y + 8, c[1], ps)             # 高光
    set_pixel(draw, x + 16, y + 8, c[1], ps)
    # 身体/精灵装
    fill_rect(draw, x + 6, y + 14, 16, 12, c[10], ps)   # 绿色
    # 弓
    fill_rect(draw, x + 0, y + 2, 4, 24, c[5], ps)       # 弓身
    fill_rect(draw, x + 2, y + 8, 2, 12, c[6], ps)     # 弓弦

def main():
    # 创建 256x64 图像，透明背景
    img = Image.new('RGBA', (256, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 每行8个图标，每个 sprite 32x32 像素
    icon_size = 32

    # 地形 (第一行)
    terrain_funcs = [
        draw_forest, draw_river, draw_mountain, draw_ruins,
        draw_hills, draw_wall, draw_bridge, draw_plains
    ]

    # 单位 (第二行)
    unit_funcs = [
        draw_lord, draw_knight_heavy, draw_knight, draw_archer,
        draw_swordsman, draw_axeman, draw_pikeman, draw_elf
    ]

    # 绘制地形行
    for i, func in enumerate(terrain_funcs):
        x = i * icon_size
        y = 0
        func(draw, x, y, ps=2)

    # 绘制单位行
    for i, func in enumerate(unit_funcs):
        x = i * icon_size
        y = icon_size
        func(draw, x, y, ps=2)

    # 保存
    output_path = "D:/Claudecodeworkspace/Projects/fe-bridge-game/sprites/terrain-units-sheet.png"
    img.save(output_path)
    print(f"Sprite sheet saved to: {output_path}")
    print(f"Size: {img.size}")

if __name__ == "__main__":
    main()
