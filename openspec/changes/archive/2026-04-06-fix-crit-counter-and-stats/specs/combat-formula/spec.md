## ADDED Requirements

### Requirement: Critical hits deal double damage
When a critical hit is triggered during combat, the damage SHALL be multiplied by 2.

#### Scenario: Critical hit damage calculation
- **WHEN** attacker initiates combat and `spd_diff >= 4` triggers a critical hit
- **THEN** damage = `floor(ATK × weapon_multiplier × 2 - (DEF + terrain_bonus))`
- **AND** counterattack SHALL NOT occur

#### Scenario: Normal hit damage unchanged
- **WHEN** attacker initiates combat and no critical is triggered
- **THEN** damage = `floor(ATK × weapon_multiplier - (DEF + terrain_bonus))`

### Requirement: Counterattack by defender
After an attacker performs a non-critical attack, if the defender's weapon range covers the attacker AND the defender has not yet acted this combat, the defender SHALL perform a counterattack.

#### Scenario: Counterattack triggers
- **WHEN** attacker deals non-critical damage to defender
- **AND** defender's weapon range >= attacker's weapon range
- **AND** defender is not dead
- **THEN** defender retaliates with normal damage (no counter-counter)

#### Scenario: Counterattack blocked by range
- **WHEN** attacker is out of defender's weapon range
- **THEN** no counterattack occurs

#### Scenario: Counterattack blocked by critical
- **WHEN** attacker deals critical damage
- **THEN** counterattack does not occur (attacker has initiative advantage)

### Requirement: Terrain bonus in damage calculation
Terrain bonus SHALL be subtracted from damage after weapon multiplier, applied to both attacker and defender in both normal attacks and counterattacks.

#### Scenario: Terrain bonus on defender
- **WHEN** defender is on terrain with bonus DEF
- **THEN** damage received is reduced by terrain bonus
