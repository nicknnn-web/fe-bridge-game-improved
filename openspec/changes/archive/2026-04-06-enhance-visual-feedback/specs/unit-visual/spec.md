## ADDED Requirements

### Requirement: Unit icons are larger and more visually distinct
Job icons SHALL be scaled up approximately 30% from current size, making them more recognizable at a glance.

#### Scenario: Unit icons clearly visible
- **WHEN** player views the game board
- **THEN** each unit's job icon (shield/triangle/diamond/circle) is at least 13px in its largest dimension

### Requirement: Each job class has a distinctive inner ring color
Inside each unit's circle, a 3px colored ring SHALL indicate the job class.

#### Scenario: Job class identifiable by ring color
- **WHEN** player looks at any unit
- **THEN** a colored ring is visible inside the unit circle matching: 领主=gold, 重甲=silver, 骑士=blue, 弓手=orange

### Requirement: Acted units show a small triangle marker below the HP bar
When a unit has `done === true`, a small downward-pointing triangle SHALL appear below the HP bar.

#### Scenario: Acted status visible
- **WHEN** a unit has completed its action (moved and attacked or skipped)
- **THEN** a small ▲ marker appears below the HP bar in a dimmed color
