# fe-bridge-game 版本更新日志

> 记录每个改进轮次的主要变更，每次改进后追加一条记录。

---

## [v0.7.0] - 2026-04-08

### 改进 #30：回合结束按钮脉冲提示
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-endturn-pulse-requirements.md`
- **改动说明**：我方单位全部行动后"结束回合"按钮金色光晕脉冲闪烁

### 改进 #29：战斗结算弹出提示
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-combat-popup-requirements.md`
- **改动说明**：攻击命中时目标上方显示伤害弹出框，40帧后消失

### 改进 #28：移动消耗悬停显示
- **类型**：交互体验
- **需求文档**：`improvements/logs/2026-04-08-mv-cost-hover-requirements.md`
- **改动说明**：选中单位时悬停移动范围格子显示地形消耗数字

### 改进 #27：移动消耗常量全局化
- **类型**：代码质量
- **需求文档**：`improvements/logs/2026-04-08-mv-cost-constant-requirements.md`
- **改动说明**：地形移动消耗统一为全局 MV_COST 常量，消除重复代码

### 改进 #26：攻击轨迹线
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-attack-trail-requirements.md`
- **改动说明**：攻击时画金色曲线轨迹从攻击者到目标，15帧衰减

## [v0.6.0] - 2026-04-08

### 改进 #25：胜负界面战斗统计
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-victory-summary-requirements.md`
- **改动说明**：胜负界面显示生还数/总兵数、歼敌数，完美胜利特殊提示

### 改进 #24：伤害预览显示
- **类型**：交互体验
- **需求文档**：`improvements/logs/2026-04-08-damage-preview-requirements.md`
- **改动说明**：选中攻击单位时悬停目标显示预估伤害数字

### 改进 #23：连击计数器
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-combo-counter-requirements.md`
- **改动说明**：连续击杀时显示"N连击！"提示，连击重置机制

### 改进 #22：攻击范围武器图标
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-weapon-icons-requirements.md`
- **改动说明**：攻击目标格子上显示武器类型图标（⚔🔱🪓🏹）

### 改进 #21：单位呼吸光晕增强
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-breathing-aura-requirements.md`
- **改动说明**：选中单位光晕透明度+半径呼吸脉动效果

### 改进 #20：小地图显示
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-minimap-requirements.md`
- **改动说明**：战场右下角显示72x72小地图，地形+单位位置

### 改进 #19：移动路径预览
- **类型**：交互体验
- **需求文档**：`improvements/logs/2026-04-08-mvpath-preview-requirements.md`
- **改动说明**：悬停移动范围显示金色虚线路径+圆点

### 改进 #18：攻击反作用力
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-attack-recoil-requirements.md`
- **改动说明**：攻击者向前冲刺，受击者向后仰，平滑恢复

### 改进 #17：伤害数字随机偏移
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-damage-offset-requirements.md`
- **改动说明**：伤害数字位置±8px/±4px随机偏移，避免堆叠

### 改进 #16：屏幕震动效果
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-screen-shake-requirements.md`
- **改动说明**：攻击命中画面震动，暴击10强度/普攻5强度

## [v0.5.0] - 2026-04-08

### 改进 #15：战场格子呼吸动画
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-grid-breathing-requirements.md`
- **改动说明**：网格线透明度随时间在0.006-0.018间正弦波动

### 改进 #14：HP条颜色平滑渐变
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-hp-gradient-requirements.md`
- **改动说明**：HP条颜色在绿/黄/红之间线性插值平滑过渡，非三档跳变

### 改进 #13：暴击伤害数字弹跳特效
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-crit-floater-requirements.md`
- **改动说明**：暴击伤害数字带弹跳放大动画，普通伤害不变

### 改进 #12：回合开始公告
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-round-banner-requirements.md`
- **改动说明**：回合/敌方回合开始时画面中央显示公告条，fade in+保持+fade out

### 改进 #11：单位选中粒子特效
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-selection-particles-requirements.md`
- **改动说明**：选中单位周围持续发射金色粒子

## [v0.4.0] - 2026-04-08

### 改进 #10：单位死亡渐隐动画
- **类型**：视觉效果
- **需求文档**：`improvements/logs/2026-04-08-unit-death-animation-requirements.md`
- **改动说明**：单位HP归零时播放0.5秒渐隐缩小动画再移除
- **Commit**：`c3fa098`

### 改进 #9：地形防御加成Canvas贴片显示
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-terrain-bonus-canvas-requirements.md`
- **改动说明**：有加成地形格子上直接显示+2/+4等数字
- **Commit**：`c3fa098`

### 改进 #8：AI行动日志增强
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-ai-log-requirements.md`
- **改动说明**：敌方回合显示分隔符，AI瞄准/移动增加战术说明日志
- **Commit**：`b290b16`

### 改进 #7：速度按钮视觉增强
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-speed-control-requirements.md`
- **改动说明**：速度按钮三档文字+激活金色边框，切换颜色区分
- **Commit**：`f1e712a`

### 改进 #6：地形悬停预览
- **类型**：交互体验
- **需求文档**：`improvements/logs/2026-04-08-terrain-preview-requirements.md`
- **改动说明**：鼠标悬停格子显示地形信息+金色脉冲边框，80ms节流
- **Commit**：`dada4bd`

### 改进 #5：胜利/失败界面美化
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-end-screen-requirements.md`
- **改动说明**：胜利/失败界面显示生还数/击杀数，完美胜利特殊文案
- **Commit**：`3dec736`

### 改进 #4：单位详情面板增强
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-unit-panel-enhance-requirements.md`
- **改动说明**：属性增加图标，防御显示4(+2)格式，状态标签加●前缀
- **Commit**：`3ddab5c`

## [v0.3.0] - 2026-04-08

### 改进 #3：战斗日志超过20条自动折叠
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-combat-log-requirements.md`
- **改动说明**：Log对象新增 `_render()/toggle()`，超20条显示"查看更多历史"，点击展开/收起
- **Commit**：`3acd91e`

### 改进 #2：可攻击目标橙色闪烁边框
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-atktarget-flash-requirements.md`
- **改动说明**：Renderer.unit() 增加 isAtkTarget 参数，攻击目标显示橙色脉冲边框
- **Commit**：`3505b93`

## [v0.2.0] - 2026-04-08

### 改进 #1：移动/攻击范围高亮颜色区分
- **类型**：UI/UX
- **需求文档**：`improvements/logs/2026-04-08-range-highlight-requirements.md`
- **改动说明**：移动范围高亮由红色改为蓝色（`rgba(59,130,246,.15)`），攻击范围保持红色
- **Commit**：`8688de8`

---

## [v0.1.0] - 2026-04-08

### 初始版本
- **类型**：功能完整
- **说明**：v3完整战棋游戏，含回合制、AI、移动/攻击、武器克制、暴击反击、地形系统、v4 GBA精灵图
- **Commit**：`6fec70c`

---
