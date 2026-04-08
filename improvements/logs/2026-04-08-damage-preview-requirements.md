# 改进需求：伤害预览显示

> 日期：2026-04-08
> 改进点：选中攻击单位时在目标上方显示预估伤害
> 状态：已实施

---

## 目标

当玩家选中攻击单位并将鼠标悬停在可攻击目标上时，在目标单位上方显示预估伤害数字。

## 现状分析

玩家需要凭经验估算伤害，无法提前知道具体数值。

## 改动范围

### 1. Renderer 新增 `_atkSel` 状态
```javascript
this._atkSel=null;
```
在选择攻击单位时设置为该单位。

### 2. `Renderer.unit()` 伤害预览渲染
```javascript
if(isAtkTarget && Renderer._atkSel){
  const preDmg=Math.max(1, Renderer._atkSel.atk-(u.def+(bonusMap[MAP[u.y][u.x]]||0)));
  c.fillStyle='rgba(239,68,68,0.8)';
  c.font='bold 11px "Press Start 2P",monospace';
  c.textAlign='center';
  c.fillText(`-${preDmg}`, u.x*TS+TS/2, u.y*TS+8);
}
```

### 3. 触发时机
- 选中攻击单位时设置 `Renderer._atkSel`
- 取消选中时置空

## 验收标准

1. 悬停可攻击目标时显示预估伤害
2. 伤害数字以红色显示在目标上方
3. 伤害计算考虑地形防御加成
4. 伤害预览不影响实际战斗判定

## 改动文件

- `fe_bridge_v3.html` — `Renderer._atkSel`, `Renderer.unit()`, `game.click()`, `game.attack()`
