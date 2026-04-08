# 改进需求：移动路径预览

> 日期：2026-04-08
> 改进点：鼠标悬停移动范围时显示路径预览
> 状态：已实施

---

## 目标

玩家将鼠标移到可移动的格子上时，显示从当前位置到该格子的移动路径。

## 现状分析

显示移动范围但不显示具体路径，玩家需要猜测最优路线。

## 改动范围

### 1. `game._findPath(u, sx, sy, ex, ey)` BFS寻路
```javascript
_findPath(u,sx,sy,ex,ey){
  const vis={}, parent={}, q=[[sx,sy]];
  vis[`${sx},${sy}`]=1;
  // BFS遍历...
  // 重建路径...
  return path;
}
```

### 2. `game.onHover(gx, gy)` 设置路径
```javascript
if(this.phase==='player'&&this.sel&&!this.sel.moved){
  if(this.mvRange.some(([mx,my])=>mx===gx&&my===gy)){
    const path=this._findPath(this.sel,this.sel.x,this.sel.y,gx,gy);
    Renderer._hoverPath=path;
  }
}
```

### 3. `Renderer._hoverPath` 渲染虚线路径
- 路径点显示金色圆点
- 起点到终点绘制虚线

## 验收标准

1. 悬停移动范围格子时显示路径
2. 路径以金色圆点和虚线表示
3. 路径实时跟随鼠标变化
4. 移开鼠标后路径消失

## 改动文件

- `fe_bridge_v3.html` — `game._findPath()`, `game.onHover()`, `Renderer._hoverPath`, `Renderer.mvPath()`
