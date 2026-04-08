# 改进需求：攻击轨迹线

> 日期：2026-04-08
> 改进点：攻击时画攻击轨迹曲线
> 状态：已实施

---

## 目标

攻击时从攻击者到目标画一条金色曲线轨迹，增强战斗视觉冲击力。

## 现状分析

攻击命中时只有伤害数字和粒子特效，无轨迹连线。

## 改动范围

### 1. Renderer 新增 `_trail` 状态
```javascript
_trail:null,
```

### 2. 攻击时设置轨迹
```javascript
Renderer._trail={x1:at.px+TS/2,y1:at.py+TS/2,x2:df.px+TS/2,y2:df.py+TS/2,t:0,duration:15};
```

### 3. `Renderer.trail()` 渲染轨迹
```javascript
trail(){
  if(!this._trail) return;
  const tr=this._trail, c=this.ctx;
  tr.t++;
  const progress=tr.t/tr.duration;
  if(progress>=1){this._trail=null; return;}
  const alpha=(1-progress)*0.6;
  const sw=8*(1-progress)+2;
  c.save();
  c.globalAlpha=alpha;
  c.strokeStyle='#fbbf24';
  c.lineCap='round';
  c.beginPath();
  const mx=(tr.x1+tr.x2)/2+(Math.sin(progress*Math.PI)*30*(tr.y2>tr.y1?1:-1));
  const my=(tr.y1+tr.y2)/2;
  c.moveTo(tr.x1,tr.y1);
  c.quadraticCurveTo(mx,my,tr.x2,tr.y2);
  c.stroke();
  c.restore();
}
```

### 4. `game.loop()` 调用
在 `floaters()` 后调用 `trail()`

## 验收标准

1. 攻击时从攻击者到目标画金色曲线
2. 轨迹在15帧内衰减消失
3. 曲线有弧度，非直线
4. 攻击者和AI攻击都触发轨迹

## 改动文件

- `fe_bridge_v3.html` — `Renderer._trail`, `Renderer.trail()`, `game.attack()`, `game.attackAI()`, `game.loop()`
