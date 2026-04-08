# unit-stats Specification

## Purpose
TBD - created by archiving change fix-crit-counter-and-stats. Update Purpose after archive.
## Requirements
### Requirement: Player units have correct stats and positions
Player units (蓝方) SHALL have stats matching the table below and start at the specified coordinates.

| ID | Name | Job | Weapon | HP | ATK | DEF | SPD | MOV | Start X | Start Y |
|----|------|-----|--------|-----|-----|-----|-----|-----|---------|---------|
| p1 | 艾利乌德 | 领主 | 剑 | 28 | 10 | 5 | 5 | 5 | 1 | 9 |
| p2 | 海克托尔 | 重甲 | 斧 | 38 | 7 | 9 | 2 | 4 | 2 | 9 |
| p3 | 琳 | 骑士 | 枪 | 22 | 12 | 4 | 9 | 8 | 1 | 10 |
| p4 | 露西亚 | 弓手 | 弓 | 18 | 9 | 2 | 6 | 5 | 2 | 10 |

#### Scenario: Game starts with correct player positions
- **WHEN** game initializes
- **THEN** p1 is at (1,9), p2 at (2,9), p3 at (1,10), p4 at (2,10)

### Requirement: Enemy units have correct stats and positions
Enemy units (红方) SHALL have stats matching the table below and start at the specified coordinates.

| ID | Name | Job | Weapon | HP | ATK | DEF | SPD | MOV | Start X | Start Y |
|----|------|-----|--------|-----|-----|-----|-----|-----|---------|---------|
| e1 | 黑骑士 | 领主 | 枪 | 28 | 10 | 5 | 5 | 5 | 9 | 1 |
| e2 | 巴里尔 | 重甲 | 斧 | 38 | 7 | 9 | 2 | 4 | 10 | 1 |
| e3 | 佣兵 | 剑士 | 剑 | 22 | 12 | 4 | 9 | 8 | 9 | 2 |
| e4 | 狙击手 | 弓手 | 弓 | 18 | 9 | 2 | 6 | 5 | 10 | 2 |

#### Scenario: Game starts with correct enemy positions
- **WHEN** game initializes
- **THEN** e1 is at (9,1), e2 at (10,1), e3 at (9,2), e4 at (10,2)

