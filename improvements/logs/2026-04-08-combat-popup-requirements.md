# 改进需求：战斗结算弹出提示

> 日期：2026-04-08
> 改进点：攻击命中时目标上方显示伤害弹出框
> 状态：已实施

---

## 目标

攻击命中时在目标单位上方显示一个小型伤害弹出框，增强战斗反馈感。

## 现状分析

伤害数字通过 floater 系统向上飘散，没有即时的弹出反馈。

## 改动范围

### 1. Renderer 新增 `_popup` 和 `_popupTimer` 状态
```javascript
_popup:null, _popupTimer:0,
```

### 2. 攻击时设置弹出
```javascript
Renderer._popup={x:df.px+TS/2,y:df.py-10,text:`-${finalDmg}`,life:40,ml:40};
Renderer._popupTimer=40;
```

### 3. `Renderer.popup()` 渲染弹出框
```javascript
popup(){
  if(!this._popup||this._popupTimer<=0) return;
  this._popupTimer--;
  const p=this._popup, c=this.ctx;
  p.life--;
  const progress=p.life/p.ml;
  const alpha=progress;
  if(progress<=0){this._popup=null; return;}
  const scale=0.8+progress*0.2;
  c.save();
  c.globalAlpha=alpha;
  c.fillStyle='rgba(0,0,0,0.5)';
  const pw=50*scale, ph=20*scale;
  c.fillRect(p.x-pw/2,p.y-ph/2,pw,ph);
  c.fillStyle='#fbbf24';
  c.font=`bold ${12*scale}px "Press Start 2P",monospace`;
  c.textAlign='center'; c.textBaseline='middle';
  c.fillText(p.text,p.x,p.y);
  c.restore();
}
```

### 4. `game.loop()` 调用
在 `floaters()` 后调用 `popup()`

## 验收标准

1. 攻击命中时显示伤害弹出框
2. 弹出框有黑色半透明背景
3. 40帧后自动消失
4. 攻击者和AI攻击都触发弹出

## 改动文件

- `fe_bridge_v3.html` — `Renderer._popup`, `Renderer.popup()`, `game.attack()`, `game.attackAI()`, `game.loop()`
