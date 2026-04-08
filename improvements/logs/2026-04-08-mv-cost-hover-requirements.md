# 改进需求：移动消耗悬停显示

> 日期：2026-04-08
> 改进点：选中单位时悬停移动范围显示地形消耗数字
> 状态：已实施

---

## 目标

玩家选中单位后，将鼠标移到可移动的格子上时显示进入该地形需要的移动力消耗。

## 现状分析

移动范围只显示哪些格子可移动，不显示各自消耗多少移动力。

## 改动范围

### 1. 全局 MV_COST 常量
```javascript
const MV_COST={};
MV_COST[T.PLAIN]=1; MV_COST[T.FOREST]=2; MV_COST[T.BLUE_CASTLE]=3;
MV_COST[T.RED_CASTLE]=3; MV_COST[T.MOUNTAIN]=99; MV_COST[T.RIVER]=99;
MV_COST[T.BRIDGE]=1; MV_COST[T.RUINS]=2; MV_COST[T.HILL]=2; MV_COST[T.WALL]=99;
```

### 2. `Renderer.hoverMvCost(x,y,cost)` 渲染消耗数字
```javascript
hoverMvCost(x,y,cost){
  const c=this.ctx;
  if(!cost||cost>=99) return;
  c.font='bold 10px "Press Start 2P",monospace';
  c.textAlign='center';
  c.fillStyle='rgba(0,0,0,0.6)';
  c.fillText(cost,x*TS+TS/2+1,y*TS+TS/2+4+1);
  c.fillStyle='rgba(255,220,100,0.9)';
  c.fillText(cost,x*TS+TS/2,y*TS+TS/2+4);
}
```

### 3. `game.loop()` 悬停检测
```javascript
if(this._hovered&&this.sel&&!this.sel.moved&&this.mvRange.some(...)){
  const c=MAP[ty][tx];
  Renderer.hoverMvCost(tx,ty,MV_COST[c]<99?MV_COST[c]:null);
}
```

## 验收标准

1. 悬停移动范围格子时显示消耗数字
2. 消耗1显示为"1"，消耗2显示为"2"等
3. 河流/山脉/城墙等不可通行地形不显示数字
4. 数字以金色显示在格子中央

## 改动文件

- `fe_bridge_v3.html` — `MV_COST` 常量, `Renderer.hoverMvCost()`, `game.loop()`
