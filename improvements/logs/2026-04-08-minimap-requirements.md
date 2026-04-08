# 改进需求：小地图显示

> 日期：2026-04-08
> 改进点：战场右下角显示小地图
> 状态：已实施

---

## 目标

在游戏画面右下角显示缩略小地图，展示战场全貌、地形分布和单位位置。

## 现状分析

玩家需要仔细观察主战场才能了解全局，小地图有助于战术判断。

## 改动范围

### `Renderer.miniMap(units)` 小地图渲染
```javascript
miniMap(units){
  const c=this.ctx;
  const size=72, scale=size/12, ox=this.canvas.width-size-10, oy=this.canvas.height-size-10;
  // 背景
  c.fillStyle='rgba(0,0,0,0.5)';
  c.fillRect(ox,oy,size,size);
  // 地形颜色
  const terrainColors={...};
  for(let y=0;y<12;y++)for(let x=0;x<12;x++){
    c.fillStyle=terrainColors[MAP[y][x]]||'#333';
    c.fillRect(ox+x*scale,oy+y*scale,scale,scale);
  }
  // 单位点
  units.forEach(u=>{
    if(!u.dead){
      c.fillStyle=u.isPlayer?'#3b82f6':'#ef4444';
      c.beginPath();
      c.arc(ox+u.x*scale+scale/2,oy+u.y*scale+scale/2,2,0,7);
      c.fill();
    }
  });
}
```

## 验收标准

1. 右下角显示72x72像素小地图
2. 地形颜色区分清晰
3. 我方单位显示蓝色点，敌方显示红色点
4. 不遮挡主游戏区域

## 改动文件

- `fe_bridge_v3.html` — `Renderer.miniMap()`, `game.loop()`
