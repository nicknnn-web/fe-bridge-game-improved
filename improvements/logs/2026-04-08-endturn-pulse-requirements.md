# 改进需求：回合结束按钮脉冲提示

> 日期：2026-04-08
> 改进点：我方单位全部行动后"结束回合"按钮闪烁提示
> 状态：已实施

---

## 目标

当所有我方存活单位都已完成移动和攻击后，"结束回合"按钮自动开始脉冲闪烁，提示玩家可以结束回合了。

## 现状分析

玩家需要自行判断是否所有单位都已行动完毕，无法获得明确的视觉提示。

## 改动范围

### 1. CSS 脉冲动画
```css
.end-turn-btn.pulse{
  animation:pulse-btn 0.8s ease-in-out infinite;
}
@keyframes pulse-btn{
  0%,100%{ box-shadow:0 0 0 0 rgba(240,192,64,0.4); }
  50%{ box-shadow:0 0 0 8px rgba(240,192,64,0); }
}
```

### 2. `checkAllDone()` 添加脉冲逻辑
```javascript
const allDone=alive.length>0&&alive.every(u=>u.done||u.moved);
const btn=document.getElementById('endTurnBtn');
btn.disabled=alive.length===0;
if(allDone&&this.phase==='player'){
  btn.classList.add('pulse');
}else{
  btn.classList.remove('pulse');
}
```

### 3. 回合开始时移除脉冲
在 `start()` 和 `afterAI()` 中移除 `pulse` class

## 验收标准

1. 所有我方单位行动完毕后按钮开始脉冲
2. 脉冲为金色光晕扩散动画
3. 玩家点击后脉冲停止
4. 敌方回合开始时脉冲自动停止

## 改动文件

- `fe_bridge_v3.html` — CSS动画, `game.checkAllDone()`, `game.start()`, `game.afterAI()`
