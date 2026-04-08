# 改进需求：胜负界面战斗统计

> 日期：2026-04-08
> 改进点：胜负界面显示生还数和击杀数统计
> 状态：已实施

---

## 目标

战斗结束后在胜负界面显示详细的战斗统计，包括我方生还数、击杀数等信息。

## 现状分析

胜负界面只显示"胜利/失败"，无具体统计数据。

## 改动范围

### `UI.showEnd(win)` 增强统计显示
```javascript
showEnd(win){
  // 显示胜利/失败标题
  // 统计生还和击杀
  const survivors=game.units.filter(u=>u.isPlayer&&!u.dead).length;
  const kills=game.units.filter(u=>!u.isPlayer&&u.dead).length;
  // 显示统计信息
  const info=document.createElement('div');
  info.style.cssText='...';
  info.innerHTML=`
    <div>我方生还：${survivors}/${playerCount}</div>
    <div>歼敌数量：${kills}/${enemyCount}</div>
    ${survivors===playerCount?'<div style="color:#fbbf24">完美胜利！</div>':''}
  `;
  // 触发连击重置
  Renderer._combo=0;
}
```

## 验收标准

1. 显示我方生还数/总兵数
2. 显示敌方被击杀数/总敌数
3. 我方零伤亡时显示"完美胜利"特殊提示
4. 胜负界面整体视觉美观

## 改动文件

- `fe_bridge_v3.html` — `UI.showEnd()`, `Renderer._combo` 重置
