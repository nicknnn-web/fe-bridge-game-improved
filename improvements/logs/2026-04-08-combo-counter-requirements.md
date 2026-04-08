# 改进需求：连击计数器

> 日期：2026-04-08
> 改进点：连续击杀时显示连击数
> 状态：已实施

---

## 目标

当一个单位连续击杀多个敌人时，显示"N连击！"提示，增强战斗成就感。

## 现状分析

连续击杀无特殊提示，战斗连击的爽感无法体现。

## 改动范围

### 1. Renderer 新增 `_combo` 状态
```javascript
this._combo=0;
```

### 2. `Renderer.combo(c)` 显示连击
```javascript
combo(c){
  const fade=Math.min(1, this._comboTime/30);
  c.save();
  c.globalAlpha=fade;
  c.fillStyle='rgba(0,0,0,0.4)';
  c.fillRect(this.canvas.width/2-80,this.canvas.height/2-50,160,40);
  c.fillStyle=`hsl(${40+c*10},100%,60%)`;
  c.font='bold 20px "Press Start 2P",monospace';
  c.textAlign='center'; c.textBaseline='middle';
  c.fillText(`${c}连击!`, this.canvas.width/2, this.canvas.height/2);
  c.restore();
}
```

### 3. 触发与重置
- 击杀敌人时：`Renderer._combo++`，`Renderer._comboTime=60`
- 我方单位死亡时：`Renderer._combo=0`

## 验收标准

1. 连续击杀时显示连击提示
2. 连击数正确累加
3. 我方单位死亡时连击重置
4. 提示有渐隐效果

## 改动文件

- `fe_bridge_v3.html` — `Renderer._combo`, `Renderer.combo()`, `game.loop()`, `game.attack()`
