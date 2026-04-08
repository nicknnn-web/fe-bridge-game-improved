## ADDED Requirements

### Requirement: End turn button is always manually clickable
The "结束回合" button SHALL always be clickable once enabled, without the turn auto-ending.

#### Scenario: Player manually ends turn
- **WHEN** player clicks the "结束回合" button
- **THEN** the turn ends and enemy phase begins
- **AND** the button is disabled during enemy phase

### Requirement: Auto-end is removed from checkAllDone
The `checkAllDone()` function SHALL NOT automatically call `endTurn()`.

#### Scenario: Turn does not auto-end
- **WHEN** all player units have completed their actions
- **THEN** the turn does NOT automatically end
- **AND** the button becomes enabled to allow manual end
