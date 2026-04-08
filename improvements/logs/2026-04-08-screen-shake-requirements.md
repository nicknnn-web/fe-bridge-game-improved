# 改进需求：屏幕震动效果

> 日期：2026-04-08
> 改进点：攻击时画面震动
> 状态：已实施

---

## 目标

攻击命中时画面产生短暂震动效果，提升战斗打击感。

## 现状分析

攻击命中时无视觉反馈，画面静止，战斗缺乏冲击力。

## 改动范围

### 1. Renderer 新增 `_shake` 状态
```javascript
this._shake=0;
```

### 2. `Renderer.shake(intensity)` 方法
```javascript
shake(intensity){ this._shake=Math.max(this._shake,intensity||8); }
```

### 3. `game.loop()` 震动渲染块
```javascript
if(Renderer._shake){
  const s=Renderer._shake;
  Renderer.ctx.save();
  Renderer.ctx.translate(Math.random()*s*2-s, Math.random()*s*2-s);
}
// ... 渲染 ...
if(Renderer._shake){ Renderer.ctx.restore(); Renderer._shake*=0.85; if(Renderer._shake<0.5) Renderer._shake=0; }
```

### 4. 触发时机
- `game.attack()` 和 `game.attackAI()` 造成伤害后调用
- 暴击震动强度 10，普通攻击震动强度 5

## 验收标准

1. 攻击时画面有明显震动
2. 暴击震动幅度大于普通攻击
3. 震动平滑衰减，不突兀
4. 不影响游戏逻辑运行

## 改动文件

- `fe_bridge_v3.html` — `Renderer._shake`, `Renderer.shake()`, `game.loop()`, `game.attack()`, `game.attackAI()`
