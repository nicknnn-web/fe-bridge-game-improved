## Why

暴击伤害未实际应用（`dmg()` 返回 `c:true` 但伤害未 ×2），反击机制完全缺失，单位数值（移动力）与 SPEC.md 多处不一致。这些问题直接影响战斗平衡和游戏手感。

## What Changes

- **暴击伤害修复**：攻击时若 `c:true`，实际伤害 ×2
- **反击系统实现**：防御方在满足条件时进行反击
- **单位数值对齐**：重甲 MOV 4（目前 3）、弓手 MOV 5（目前 4）
- **起点位置对齐**：蓝方/红方单位位置按 SPEC 坐标放置
- **山脉地形**：SPEC 定义为不可通行，保持现状（已可通行，消耗3）需决策

## Capabilities

### New Capabilities

- `combat-formula`: 暴击 ×2 伤害、反击触发条件及伤害计算规则
- `unit-stats`: 单位属性数值表（HP/ATK/DEF/SPD/MOV）、起点坐标、武器克制表

### Modified Capabilities

- （无现有 specs，不涉及修改）

## Impact

- `fe_bridge_v3.html`：`dmg()` 函数、`Unit` 类、单位初始化数据、地图数据
- 无外部依赖
