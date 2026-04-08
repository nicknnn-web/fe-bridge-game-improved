# 改进需求：攻击范围显示武器类型图标

> 日期：2026-04-08
> 改进点：攻击范围格子上显示武器类型图标
> 状态：已实施

---

## 目标

当选择攻击单位时，在可攻击的目标格子上显示对应武器类型图标。

## 现状分析

攻击范围只显示红色高亮，不显示武器类型信息。

## 改动范围

### `Renderer.atkRange(units, wpType)` 显示图标
```javascript
atkRange(units, wpType){
  units.forEach(u=>{
    // 原有红色高亮...
    // 武器图标
    const ic=wpType==='剑'?'⚔':wpType==='枪'?'🔱':wpType==='斧'?'🪓':wpType==='弓'?'🏹':'⚔';
    c.font='11px sans-serif'; c.textAlign='center';
    c.fillStyle='rgba(255,255,255,0.5)';
    c.fillText(ic, u.x*TS+TS/2, u.y*TS+TS/2+4);
  });
}
```

## 验收标准

1. 攻击目标格子上显示对应武器图标
2. 图标与武器类型对应：剑⚔ 枪🔱 斧🪓 弓🏹
3. 图标半透明，不遮挡地形
4. 攻击范围调用时传入正确武器类型

## 改动文件

- `fe_bridge_v3.html` — `Renderer.atkRange()`, `game.loop()` 调用处
