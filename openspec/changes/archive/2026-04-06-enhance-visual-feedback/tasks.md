## 1. 职业图标放大 + 职业颜色环

- [ ] 1.1 修改 `_drawUnitIcon()` 放大所有图标坐标（领主盾、重甲圆、骑士三角、弓手菱形）约 30%
- [ ] 1.2 在 `unit()` 函数中，HP bar 上方添加职业颜色环（领主金/重甲银/骑士蓝/弓手橙，3px 宽弧线）

## 2. 已行动标记

- [ ] 2.1 在 `unit()` 函数中，当 `u.done === true` 时，在 HP bar 下方绘制小三角（暗淡灰色 ▲）

## 3. 修复 endTurn Auto-End Bug

- [ ] 3.1 删除 `checkAllDone()` 中的 `if(...&&this.phase==='player'){this.endTurn();}` 这一行
- [ ] 3.2 验证按钮逻辑：按钮在所有单位 done 时启用，玩家可随时点击手动结束
