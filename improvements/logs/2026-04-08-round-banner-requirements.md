# 改进需求：回合开始公告

> 日期：2026-04-08
> 改进点：回合开始时在画面中央显示公告条
> 状态：已实施

---

## 目标

玩家/敌方回合开始时，在画面中央显示 "第 N 回合" 或 "敌方回合" 公告条，fade in + hold + fade out。

## 现状分析

当前仅在顶部标题栏显示回合数，无中央公告。

## 改动范围

### 1. `Renderer` 新增 banner 系统
```javascript
_banner:null,

banner(){
  if(!this._banner) return;
  // fade in 10%, hold 60%, fade out 30%
  // 居中显示，带边框和背景
},

showBanner(text,enemy,ms){
  this._banner={text,enemy,life:...,ml:...};
}
```

### 2. `game.start()` / `game.endTurn()` / `game.afterAI()` 调用
- `start()` → 显示 "第 1 回合"（蓝色边框）
- `endTurn()` → 显示 "敌方回合"（红色边框，1.5秒）
- `afterAI()` → 显示 "第 N 回合"（蓝色边框，2秒）

### 3. `game.loop()` 调用 `Renderer.banner()`

## 验收标准

1. 开战时显示 "第 1 回合" 公告（2秒）
2. 敌方回合开始时显示 "敌方回合" 公告（1.5秒）
3. 我方回合开始时显示 "第 N 回合" 公告（2秒）
4. 公告有淡入/保持/淡出动画

## 改动文件

- `fe_bridge_v3.html` — `Renderer.banner/showBanner()` + `game.start/endTurn/afterAI`
