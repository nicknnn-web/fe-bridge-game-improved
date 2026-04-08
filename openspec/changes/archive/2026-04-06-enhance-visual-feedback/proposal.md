## Why

职业图标偏小（7-12px）区分度不够，交互反馈缺乏"已行动"确认，且 endTurn 自动触发导致手动按钮失效。

## What Changes

- **P1**: 增强职业图标尺寸（+30%），增加职业专属内圈颜色环
- **P2**: 增加"已行动"视觉确认（单位下方小三角标记）；修复 endTurn auto-end 过早触发 bug
- **EndTurn Bug Fix**: 移除 line 861 的自动 endTurn()，确保玩家可随时手动结束回合

## Capabilities

- `unit-visual`: 单位渲染增强 — 更大职业图标 + 职业颜色环
- `acted-feedback`: 已行动状态视觉反馈
- `endturn-fix`: 修复回合结束按钮 auto-end 逻辑

## Impact

- `fe_bridge_v3.html:1077-1171` (unit rendering), `fe_bridge_v3.html:861` (auto-end removal)
