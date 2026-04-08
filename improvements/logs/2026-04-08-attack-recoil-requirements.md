# 改进需求：攻击反作用力（冲锋/后坐）

> 日期：2026-04-08
> 改进点：攻击时攻击者向前冲刺，受击者向后仰
> 状态：已实施

---

## 目标

攻击时攻击者和受击者有位置移动动画，模拟战斗中的冲锋和后仰效果。

## 现状分析

攻击时单位位置固定，战斗动作感不足。

## 改动范围

### 1. Unit.reset() 新增 `_lunge` 属性
```javascript
this._lunge=0;
```

### 2. 攻击时设置冲击力
```javascript
// game.attack() / game.attackAI()
at._lunge=1;    // 攻击者向前冲
df._lunge=-0.5; // 受击者向后仰
```

### 3. 每帧衰减
```javascript
if(u._lunge>0){
  u._lunge=Math.max(0, u._lunge-0.15*this.speed);
} else if(u._lunge<0){
  u._lunge=Math.min(0, u._lunge+0.1*this.speed);
}
```

### 4. 渲染时应用位移
在单位位置计算时乘以 `(1 + lunge)` 系数

## 验收标准

1. 攻击者攻击时有向前冲刺动作
2. 受击者被击中时有向后仰动作
3. 动作平滑过渡后恢复原位
4. 不影响移动和攻击判定

## 改动文件

- `fe_bridge_v3.html` — `Unit.reset()`, `game.attack()`, `game.attackAI()`, 单位渲染逻辑
