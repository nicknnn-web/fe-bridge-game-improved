# 改进需求：暴击伤害数字弹跳特效

> 日期：2026-04-08
> 改进点：暴击时伤害数字弹跳放大
> 状态：已实施

---

## 目标

暴击伤害数字显示时带有弹跳放大动画，普通伤害数字保持原有浮动方式。

## 现状分析

所有伤害数字均以相同方式向上飘散，无区分度。

## 改动范围

### 1. `addFloater()` 新增 `crit` 参数
```javascript
addFloater(x,y,v,c,crit){
  this._ft.push({x:...,y:...,vy:-2.5,v,c,crit:!!crit,life:40,ml:40,bounce:crit?1:0,bx:x*TS+22,by:y*TS+22});
}
```

### 2. `floaters()` 处理弹跳逻辑
- 暴击浮空器：`bounce` 从 1→0 的正弦曲线
- 字体放大：暴击时 `bold 18px`
- 粒子颜色保持 `#fbbf24`

## 验收标准

1. 暴击伤害数字弹跳幅度约 50%
2. 普通伤害数字无变化
3. 暴击粒子同样使用金色

## 改动文件

- `fe_bridge_v3.html` — `Renderer.addFloater()` + `floaters()`
