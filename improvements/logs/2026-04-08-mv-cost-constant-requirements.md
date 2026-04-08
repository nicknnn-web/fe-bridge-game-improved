# 改进需求：移动消耗常量全局化

> 日期：2026-04-08
> 改进点：地形移动消耗提取为全局 MV_COST 常量
> 状态：已实施

---

## 目标

将分散在各处的地形移动消耗数据统一为全局 MV_COST 常量，消除重复代码。

## 现状分析

`mvCost` 对象在 `bfs()`、`UI.getTerrainInfo()` 等多处重复定义。

## 改动范围

### 全局常量
```javascript
const MV_COST={};
MV_COST[T.PLAIN]=1; MV_COST[T.FOREST]=2; MV_COST[T.BLUE_CASTLE]=3;
MV_COST[T.RED_CASTLE]=3; MV_COST[T.MOUNTAIN]=99; MV_COST[T.RIVER]=99;
MV_COST[T.BRIDGE]=1; MV_COST[T.RUINS]=2; MV_COST[T.HILL]=2; MV_COST[T.WALL]=99;
```

### 替换位置
- `bfs()` — 使用 `MV_COST[t]` 替代 `mvCost[t]`
- `UI.getTerrainInfo()` — 使用 `MV_COST[t]` 替代局部 `mvCost`

## 验收标准

1. 移动消耗行为完全不变
2. 代码中不再有重复的 mvCost 对象定义
3. 地形消耗数据集中在一处管理

## 改动文件

- `fe_bridge_v3.html` — 添加 `MV_COST` 常量, `bfs()`, `UI.getTerrainInfo()`
