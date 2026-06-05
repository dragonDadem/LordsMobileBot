# KINGDOM ROYALE: OFFICIAL GAME DESIGN DOCUMENT

## VERSION 1.0 - CONFIDENTIAL

---

# SECTION 1: GAME OVERVIEW

## 1.1 Project Identity
- **Game Name:** Kingdom Royale
- **Slogan:** "Conquer the Land, Outlast the Storm, Rule the Realm."
- **Genre:** Massive Multiplayer Online Battle Royale Strategy (MMOBRS)
- **Sub-Genres:**
    - 2D Top-Down Survival
    - Territory Control / 4X Lite
    - Class-Based Tactical Shooter
    - Persistence-Lite Base Building
- **Platform:** Web Browser (Desktop/Mobile), Standalone PC Client
- **Engine:** Custom WebGL-based High-Performance Engine
- **Target Audience:** Core gamers (16-35), fans of battle royale titles (Surviv.io, ZombsRoyale.io), and territory-based strategy fans (OpenFront, Agar.io, Diep.io).

## 1.2 The Vision
Kingdom Royale aims to bridge the gap between fast-paced session-based shooters and deep, persistent strategy games. Most Battle Royale games offer no progression within a match beyond loot. Most strategy games lack the "twitch" excitement of real-time combat. Kingdom Royale merges these: every tile you stand on can be captured, every building you raise provides a strategic buff, and every bullet you fire is calculated with professional-grade physics.

## 1.3 Core Gameplay Loop
1.  **Drop & Spawn:** Players select a starting sector within the outer rim of the massive world map.
2.  **Gather & Scavenge:** Immediate top-down survival. Players break crates for weapons and mine resources (Wood, Stone, Iron) using class-specific tools.
3.  **Establish Territory:** By standing in a sector, players begin the "Conquest Timer." Once captured, the tile changes color to the player’s faction/kingdom.
4.  **Base Infrastructure:** Captured land allows the placement of structures (Barracks, Walls, Turrets). This turns a simple survivor into a local lord.
5.  **Army Mobilization:** Resources are spent to train AI units that follow the player or defend the captured territory.
6.  **The Storm/Encroachment:** As the game progresses, the outer regions are consumed by "The Void," forcing players into the central "Nexus" where the most valuable land resides.
7.  **Final Hegemony:** The match ends when one player or clan controls the "Crown Tile" at the center of the map while being the last survivors.

## 1.4 Unique Selling Points (USPs)
- **Persistent Conquest in a BR Setting:** Unlike other BRs where land is just cover, in Kingdom Royale, land is a resource. Capturing a "Forest" tile grants passive wood income until the storm takes it.
- **Hybrid Combat System:** Real-time WASD movement and mouse-aiming combined with RTS-style unit management.
- **Dynamic Building System:** Instant-deployment of fortifications (Fortnite-style speed but with strategy-game permanence).
- **Class-Based Depth:** Players aren't just "skins"; they are specialized roles that dictate their resource gathering speed, weapon handling, and army leadership.

## 1.5 Competitive Advantages
- **Low Barrier to Entry:** Browser-based technology ensures anyone with an internet connection can play instantly.
- **High-Fidelity 2D Physics:** Advanced hit-reg, bullet penetration, and environmental destruction that rivals standalone titles.
- **Deep Economy:** An 8-resource system ensures that players must manage logistics, not just aim.

## 1.6 Long Term Retention Strategy
- **Seasonal Metagame:** While matches reset, players earn "Crown Points" to upgrade their account-wide "Mastery Tree."
- **Clan Persistence:** Clans can own "Home Realms" that persist across matches, acting as social hubs and trophy rooms.
- **Live Events:** "The Titan Incursions" where massive AI bosses spawn, forcing players into temporary, shaky alliances.

## 1.7 Player Experience Goals
- **Tension:** The constant threat of being ambushed while expanding territory.
- **Agency:** Every building placement and class choice feels meaningful.
- **Satisfaction:** The visual feedback of seeing your color spread across the minimap.

---

# SECTION 2: FULL GAME STORY (LORE)

## 2.1 The World of Aethelgard
Aethelgard was once a unified super-continent of floating islands and lush valleys, governed by the "Eternal Compact." For three thousand years, the four Great Kingdoms lived in a state of magi-technical harmony. This ended during the "Event of the Bleeding Sky."

## 2.2 The Great Collapse
A mysterious cosmic anomaly known as "The Void" pierced the atmosphere. It didn't just destroy; it began "eating" reality. The continent began to shrink from the edges inward. The laws of physics started to fray at the borders, leaving only the "Nexus"—the central point of the world—stable.

## 2.3 The Four Great Kingdoms
### 1. The Iron Hegemony (The North)
- **Visuals:** Industrial, Steampunk, Heavy Metal.
- **Philosophy:** Strength through Steel. They believe the Void can be repelled by building a massive iron wall around the Nexus.
- **Technology:** Steam-powered tanks, heavy artillery, and automated sentries.

### 2. The Sylvan Collective (The East)
- **Visuals:** Bioluminescent forests, organic architecture, living weapons.
- **Philosophy:** Harmony through Adaptability. They believe the Void is a natural cycle and that by evolving their DNA, they can survive within it.
- **Technology:** Bio-engineered beasts, poison-gas launchers, and rapid-regrowth structures.

### 3. The Frost-Guard (The West)
- **Visuals:** Crystal palaces, runic ice-armor, ethereal glows.
- **Philosophy:** Preservation through Stasis. They seek to freeze time itself to stop the Void's encroachment.
- **Technology:** Cryo-weapons, teleportation circles, and energy shields.

### 4. The Desert Wraiths (The South)
- **Visuals:** Scavenged tech, sand-blown cloaks, nomadic rigs.
- **Philosophy:** Survival at any Cost. They are the scavengers who have learned to harvest the Void's energy.
- **Technology:** Plasma-whips, cloaking devices, and high-speed hovercrafts.

## 2.4 The Factions & Political Systems
While the Kingdoms provide the cultural background, players belong to **The Royale Seekers**—an elite guild of survivors who have abandoned their national loyalties in a desperate bid to reach the Nexus.

- **The High Council:** An NPC body that dictates the "Laws of Engagement" (the rules of the match).
- **The Void Cult:** A shadowy group that worships the encroaching storm and sabotages player efforts.

## 2.5 Resources & Tech Level
The world is in a "Magipunk" era.
- **Aether-Steel:** Iron infused with magical energy, used for all advanced construction.
- **Sun-Stone:** The primary energy source, found in the hottest regions.
- **The World Core:** The ultimate resource located at the Nexus, rumored to have the power to restart the world.

## 2.6 The Eternal Conflict
Players fight because there is only room for **one** at the center of the world. As the Void closes in, resources become scarce, and land becomes the only thing that matters. To survive is to conquer; to be passive is to be erased.

---

# SECTION 3: MAP SYSTEM

## 3.1 The Great Arena: Technical Specs
- **Total Dimensions:** 64,000 x 64,000 World Units (Approximately 4096 individual tiles).
- **Coordinate System:** Standard Cartesian grid (X, Y) with (0,0) at the geographic center (The Nexus).
- **Tile System:** Hexagonal grid for territory control, ensuring equidistant adjacency for all borders.

## 3.2 The Master Layout
The map is structured in concentric rings:
1.  **The Outlands (Outer Rim):** Starting zones. High resource density (Wood/Stone), low strategic value. High exposure to the initial Void.
2.  **The Mid-Rim:** Transition zone. Mixed biomes, early-game boss spawns, and first-tier cities.
3.  **The Inner Sanctum:** High-level resource zones (Iron/Oil). Heavily fortified AI-controlled castles.
4.  **The Nexus (Center):** A single, massive 10x10 tile area. Contains the Crown Throne.

## 3.3 Biomes & Regions

### 3.3.1 The Rust Deserts (South)
- **Visual Style:** Post-apocalyptic wasteland, scorched orange sand, rusted metal wreckage.
- **Color Palette:** #D35400 (Pumpkin), #BA4A00 (Rust), #2E4053 (Steel Blue).
- **Resources:** Scavenged Iron (High), Oil (High), Food (Very Low).
- **Enemies:** Sand-Golems, Scavenger Drones, Dust Storm Wraiths.
- **Buildings:** Scrap-Refineries, Solar Arrays.

### 3.3.2 The Whisper Forests (East)
- **Visual Style:** Dense canopy, bioluminescent flora, floating spores.
- **Color Palette:** #145A32 (Deep Green), #58D68D (Bright Mint), #AF7AC5 (Purple Spores).
- **Resources:** Wood (Abundant), Food (High), Energy (Medium).
- **Enemies:** Root-Walkers, Spore-Spitters, Giant Arachnids.
- **Buildings:** Ancient Totems, Tree-Huts, Living Walls.

### 3.3.3 The Glacial Peaks (West)
- **Visual Style:** Jagged ice mountains, perpetual blizzards, frozen lakes.
- **Color Palette:** #D6EAF8 (Pale Blue), #AED6F1 (Sky Blue), #FDFEFE (Pure White).
- **Resources:** Stone (High), Energy (High), Wood (Very Low).
- **Enemies:** Ice-Trolls, Frost-Bite Bats, Elemental Specters.
- **Buildings:** Crystal Pylons, Igloo Bunkers.

### 3.3.4 The Ember Lowlands (North)
- **Visual Style:** Volcanic cracks, obsidian plains, rivers of magma.
- **Color Palette:** #C0392B (Blood Red), #212F3C (Obsidian), #F39C12 (Orange).
- **Resources:** Stone (Medium), Iron (High), Gems (High).
- **Enemies:** Magma-Slugs, Fire-Elementals, Ash-Drakes.
- **Buildings:** Heat-Exchangers, Obsidian Forges.

## 3.4 Key Locations
- **Villages:** Found in the Outlands. 4-5 small buildings. Capturing grants a small population cap increase.
- **Cities:** Found in the Mid-Rim. 10-15 buildings. Capturing provides a "Trade Hub" (Gold generation).
- **Castles:** One per quadrant in the Inner Sanctum. Massive AI defense. Capturing grants the "Kingdom Blessing" (Global buff).
- **The Nexus:** The ultimate fortress. Heavily shielded until the late-game phase.

---

# SECTION 4: MATCH STRUCTURE

## 4.1 The Pre-Game Phase (Lobby)
- **Duration:** 60 seconds.
- **Function:** Players spawn in a "Void-Safe" training area. Here they select their Class and primary starting Loadout (Basic Pistol vs. Basic Axe).

## 4.2 The Drop System (Infiltration)
- **Mechanic:** No plane. Instead, players appear in "Drop Pods" at the very edge of the map.
- **Selection:** Players can influence their drop quadrant by clicking on the minimap during the final 5 seconds of the lobby.

## 4.3 Phase 1: Survival & Scavenging (0:00 - 5:00)
- **Objective:** Get basic weapons and armor. Capture the first 5-10 tiles around the spawn point.
- **The Storm:** "The Void" is dormant but visible at the edges.

## 4.4 Phase 2: Territory Expansion (5:00 - 12:00)
- **Objective:** Build a base. Upgrade Town Hall to Level 2. Train first army units.
- **The Storm:** The Void starts shrinking the map. 25% of the outer rim is consumed.
- **Conflict:** Borders begin to touch. First skirmishes for resource nodes.

## 4.5 Phase 3: Total War (12:00 - 20:00)
- **Objective:** Siege enemy cities. Move towards the Inner Sanctum.
- **The Storm:** 60% of the map is consumed. The biomes begin to merge as the map shrinks.
- **Mechanics:** AI Bosses spawn at the Mid-Rim borders, carrying "Legendary Loot."

## 4.6 Phase 4: The Nexus Siege (20:00 - 25:00)
- **Objective:** The Nexus Shield drops. All remaining players/clans rush for the center.
- **The Storm:** Only the Inner Sanctum and Nexus remain.
- **Lategame:** High-tier weapons (Snipers, RPGs) become essential.

## 4.7 Phase 5: End Game (25:00+)
- **Objective:** "King of the Hill."
- **Condition:** Control the Nexus Crown Tile for 120 seconds continuously while being the last surviving kingdom/player.
- **The Void:** Shrinks until only the Nexus Crown Tile exists.

## 4.8 Victory Conditions
1.  **Hegemony Victory:** Capture the Crown Tile and hold it.
2.  **Last Man Standing:** Standard BR victory if all other players are eliminated before the timer.
3.  **Resource Dominance:** If time runs out, the player with the highest "Total Territory Value" wins.


# SECTION 5: CHARACTER SYSTEM

## 5.1 Attribute Definitions
- **Health (HP):** Standard vitality. Max 100. Degenerates at 0 Hunger.
- **Armor (AP):** Damage reduction layer. Max 100. Absorbs 50-80% of incoming damage depending on quality.
- **Hunger:** Depletes over time (1 unit per 10 seconds). At 0, HP drains. Restored by Food.
- **Stamina:** Used for sprinting and heavy melee. Regens at 5 units/sec when standing still.
- **Experience (XP):** Earned via combat, building, and harvesting.
- **Level:** Max level per match is 20. Each level grants a "Talent Point."

## 5.2 Classes

### 5.2.1 The Soldier (The Vanguard)
- **Visuals:** Heavy plate-carrier, tactical helmet, green/brown camo.
- **Stats:** 120 HP, 100 AP, 80 Stamina.
- **Strengths:** High survivability, increased magazine size (+20%), faster reload.
- **Weaknesses:** Louder footsteps, slower sprint speed.
- **Abilities:**
    - *Active: Overdrive:* Temporarily increases fire rate by 30% for 5 seconds.
    - *Passive: Lead Wall:* Take 10% less damage from front-facing projectiles.

### 5.2.2 The Sniper (The Assassin)
- **Visuals:** Ghillie suit elements, sleek carbon-fiber armor, hood.
- **Stats:** 80 HP, 50 AP, 120 Stamina.
- **Strengths:** Extreme range, higher critical hit chance (+15%), silent movement.
- **Weaknesses:** Very fragile, slow movement when aiming.
- **Abilities:**
    - *Active: Ghost Walk:* Semi-transparency for 3 seconds (breaks on attack).
    - *Passive: Eagle Eye:* Increased zoom level on all scoped weapons.

### 5.2.3 The Engineer (The Architect)
- **Visuals:** Tool-belt, robotic arm, goggles, orange vest.
- **Stats:** 100 HP, 80 AP, 100 Stamina.
- **Strengths:** 50% faster construction, 20% reduced building costs.
- **Weaknesses:** Low weapon accuracy with rifles.
- **Abilities:**
    - *Active: Sentry Drop:* Deploy a temporary mini-turret.
    - *Passive: Reinforced Walls:* Buildings captured/built by Engineer have +25% HP.

### 5.2.4 The Commander (The Tactician)
- **Visuals:** Officer cap, long coat, radio backpack, golden trim.
- **Stats:** 100 HP, 100 AP, 90 Stamina.
- **Strengths:** Higher Army Cap (+5 units), faster territory capture speed (+25%).
- **Weaknesses:** High target priority (displays on minimap if standing still).
- **Abilities:**
    - *Active: Rally Cry:* Buffs nearby AI units with +20% damage.
    - *Passive: Logistics:* Passively generates 1 Gold per second.

### 5.2.5 The Scout (The Pathfinder)
- **Visuals:** Light jumpsuit, visor, jet-boots (visual only), neon accents.
- **Stats:** 90 HP, 40 AP, 150 Stamina.
- **Strengths:** Fastest movement speed, highest vision range.
- **Weaknesses:** Lowest armor cap.
- **Abilities:**
    - *Active: Scan:* Reveals nearby enemies behind walls for 5 seconds.
    - *Passive: Marathon:* Stamina regens while walking (not just standing).

### 5.2.6 The Medic (The Lifeblood)
- **Visuals:** White/Red armor, glowing canisters, medical cross.
- **Stats:** 110 HP, 70 AP, 100 Stamina.
- **Strengths:** 100% faster healing, can revive teammates (in Duo/Squad).
- **Weaknesses:** Limited explosive inventory.
- **Abilities:**
    - *Active: Healing Aura:* Heals self and allies in a small radius.
    - *Passive: Triage:* Gain 5% move speed for every wounded ally nearby.

---

# SECTION 6: COMBAT SYSTEM

## 6.1 Damage Calculations
`Final Damage = (Base Weapon Damage * Crit Multiplier * Body Part Multiplier) - (Armor DR * Armor Quality)`

- **Base Weapon Damage:** Defined per weapon.
- **Crit Multiplier:** Random chance (base 5%) to deal 1.5x damage.
- **Body Part Multipliers:**
    - Head: 2.5x
    - Torso: 1.0x
    - Limbs: 0.7x

## 6.2 Hit Detection & Physics
- **System:** Server-side raycasting for instant-hit (Hitscan) weapons and high-speed projectile physics for others (Snipers/Explosives).
- **Lag Compensation:** Back-track reconciliation (interpolating player positions up to 100ms).
- **Bullet Penetration:** Certain weapons (Rifles/LMGs) can pierce thin walls (Wood/Sand) with a 50% damage reduction.

## 6.3 Accuracy & Spread
- **Movement Penalty:** Spread increases by up to 300% while sprinting.
- **Crouch Bonus:** Spread decreases by 40% when stationary and crouched.
- **Bloom:** Sequential shots increase the spread circle. Reset time is weapon-dependent.

## 6.4 Recoil System
- **Vertical Recoil:** The camera/crosshair moves up during sustained fire.
- **Horizontal Jitter:** Random left/right sway, more prominent in LMGs.
- **Recovery:** Crosshair returns to center over 0.5 seconds after firing stops.

## 6.5 Reload Mechanics
- **Partial Reload:** Faster, retains chambered round (+1).
- **Empty Reload:** Slower animation, requires bolt-pull.
- **Interruptible:** Reloading can be canceled by switching weapons or sprinting (retains progress if empty).

## 6.6 Movement Penalties
- **Weight:** Carrying heavy weapons (LMG/Sniper) reduces base move speed by 10-15%.
- **ADS (Aim Down Sights):** Reduces move speed by 40%.
- **Water/Mire:** Reduces move speed by 50% in rivers or swamps.


# SECTION 7: WEAPONS (100+ CATALOG)

## 7.1 PISTOLS (Common to Rare)
1. **P-9 "Service":** 15 Dmg | Med Range | Fast FR | 12 Mag | 1.2s Reload | Common. Standard issue.
2. **P-12 "Executive":** 18 Dmg | Med Range | Med FR | 15 Mag | 1.3s Reload | Common. Reliable.
3. **Ghost-S Silenced:** 14 Dmg | Short Range | Fast FR | 10 Mag | 1.1s Reload | Uncommon. No muzzle flash.
4. **Viper-9 Burst:** 12 Dmg (x3) | Short Range | Burst FR | 18 Mag | 1.5s Reload | Uncommon. High burst DPS.
5. **Aether-7:** 20 Dmg | Long Range | Slow FR | 7 Mag | 1.0s Reload | Rare. Energy-based, high accuracy.
6. **Magna-Pistol:** 25 Dmg | Short Range | Slow FR | 6 Mag | 1.8s Reload | Rare. Magnetic rounds pull armor.
7. **Copperhead:** 16 Dmg | Med Range | Very Fast FR | 20 Mag | 1.4s Reload | Uncommon. Fast swap speed.
8. **Officer's Sidearm:** 22 Dmg | Med Range | Med FR | 8 Mag | 1.2s Reload | Rare. Increased headshot multi (3.0x).
9. **Scrap-Pistol:** 10 Dmg | Very Short Range | Fast FR | 15 Mag | 2.0s Reload | Common. High spread, cheap.
10. **Void-Touch:** 5 Dmg + 2 Dps | Med Range | Fast FR | 15 Mag | 1.5s Reload | Epic. Deals Void burn damage.

## 7.2 REVOLVERS (High Impact)
11. **R-38 "Peacemaker":** 35 Dmg | Med Range | Slow FR | 6 Mag | 2.5s Reload | Common. Classic heavy hitter.
12. **Iron-Slugger:** 45 Dmg | Short Range | Very Slow FR | 5 Mag | 3.0s Reload | Uncommon. High knockback.
13. **Wild-West 1800:** 32 Dmg | Long Range | Med FR | 6 Mag | 2.2s Reload | Uncommon. High velocity.
14. **Glacial-Six:** 30 Dmg | Med Range | Slow FR | 6 Mag | 2.5s Reload | Rare. Chills target (Slows by 10%).
15. **The Hand Cannon:** 60 Dmg | Long Range | Slow FR | 5 Mag | 3.5s Reload | Epic. Sniper-tier damage.
16. **Obsidian Magnum:** 50 Dmg | Short Range | Slow FR | 6 Mag | 2.8s Reload | Rare. Ignites target.
17. **Cavalry Revolver:** 38 Dmg | Med Range | Med FR | 6 Mag | 2.4s Reload | Uncommon. Increased damage while moving.
18. **Dual-Face:** 25 Dmg (x2) | Short Range | Med FR | 12 Mag | 3.0s Reload | Rare. Fires two barrels at once.
19. **Royal Webley:** 40 Dmg | Med Range | Slow FR | 6 Mag | 2.0s Reload | Epic. Fast reload for a revolver.
20. **Void-Eye:** 100 Dmg | Extreme Range | Single Shot | 1 Mag | 4.0s Reload | Legendary. Mini-railgun.

## 7.3 SMGs (Close Quarters)
21. **Spray-N-Pray:** 8 Dmg | Short Range | Insane FR | 30 Mag | 1.8s Reload | Common. High spread.
22. **Tactical MP:** 12 Dmg | Med Range | Fast FR | 25 Mag | 1.5s Reload | Common. Low recoil.
23. **Vector-X:** 10 Dmg | Short Range | Hyper FR | 20 Mag | 1.2s Reload | Uncommon. Shreds at close range.
24. **Biolume-SMG:** 9 Dmg | Med Range | Fast FR | 40 Mag | 2.2s Reload | Rare. Heals 1 HP per 10 hits.
25. **Frost-Bite MP:** 11 Dmg | Med Range | Med FR | 30 Mag | 1.8s Reload | Rare. Reduces target's Stamina.
26. **Uzi-Pro:** 13 Dmg | Short Range | Fast FR | 32 Mag | 1.6s Reload | Uncommon. Can be dual-wielded.
27. **Stinger:** 7 Dmg | Short Range | Insane FR | 50 Mag | 2.5s Reload | Rare. Poison rounds (Stackable).
28. **Nexus-Mini:** 15 Dmg | Med Range | Fast FR | 20 Mag | 1.4s Reload | Epic. Perfectly accurate first 3 shots.
29. **Compact S:** 11 Dmg | Short Range | Fast FR | 25 Mag | 1.1s Reload | Rare. Fastest swap speed in class.
30. **Void-Rattle:** 14 Dmg | Short Range | Fast FR | 35 Mag | 2.0s Reload | Legendary. Bullets pass through targets.
31. **Copper-Cat:** 10 Dmg | Med Range | Fast FR | 30 Mag | 1.7s Reload | Uncommon. Lightweight.
32. **Iron-Storm:** 16 Dmg | Short Range | Med FR | 20 Mag | 1.9s Reload | Uncommon. High armor penetration.
33. **Steam-Pistol SMG:** 12 Dmg | Short Range | Fast FR | 40 Mag | 3.0s Reload | Common. Overheats after 10 shots.
34. **Wraith-Wailer:** 9 Dmg | Med Range | Fast FR | 45 Mag | 2.4s Reload | Epic. Sounds disorienting to enemies.
35. **Sector-9:** 13 Dmg | Med Range | Fast FR | 30 Mag | 1.6s Reload | Rare. Bonus dmg to structures.

## 7.4 RIFLES (Marksman)
36. **Old-Reliable:** 25 Dmg | Long Range | Semi FR | 10 Mag | 2.0s Reload | Common. Basic semi-auto.
37. **Precision-7:** 28 Dmg | Extreme Range | Semi FR | 8 Mag | 2.2s Reload | Uncommon. Very high velocity.
38. **Crystal-Rifle:** 30 Dmg | Long Range | Semi FR | 5 Mag | 2.5s Reload | Rare. Precision shots freeze water tiles.
39. **Sylvan-Longbow:** 40 Dmg | Long Range | Charge FR | 1 Mag | 1.5s Reload | Uncommon. Silent, projectile-based.
40. **Aether-Marksman:** 35 Dmg | Extreme Range | Semi FR | 10 Mag | 1.8s Reload | Rare. Energy rounds, no bullet drop.
41. **Iron-Hegemon:** 45 Dmg | Med Range | Semi FR | 5 Mag | 3.0s Reload | Rare. High damage to Armor.
42. **Wraith-Musket:** 65 Dmg | Long Range | Single Shot | 1 Mag | 4.0s Reload | Rare. High smoke screen on fire.
43. **Royal Carabine:** 22 Dmg | Med Range | Fast Semi FR | 15 Mag | 1.5s Reload | Epic. Low recoil.
44. **Void-Piercer:** 50 Dmg | Extreme Range | Semi FR | 3 Mag | 3.0s Reload | Legendary. Ignores 50% Armor.
45. **Tribal-Spear (Thrown):** 55 Dmg | Short Range | Single Shot | 1 Mag | 1.0s Reload | Uncommon. Can be retrieved.


## 7.5 ASSAULT RIFLES (The Standard)
46. **M-16 "Patriot":** 18 Dmg | Med Range | Fast FR | 30 Mag | 2.0s Reload | Common. Versatile.
47. **AK-47 "Classic":** 24 Dmg | Med Range | Med FR | 30 Mag | 2.5s Reload | Common. High recoil, high damage.
48. **SCAR-L:** 20 Dmg | Long Range | Fast FR | 30 Mag | 2.2s Reload | Uncommon. High accuracy.
49. **Sylvan-Vine:** 17 Dmg | Med Range | Fast FR | 35 Mag | 2.3s Reload | Rare. Hits slow enemies.
50. **Frost-AR:** 19 Dmg | Med Range | Fast FR | 30 Mag | 2.0s Reload | Rare. High efficiency in Snow Biomes.
51. **Iron-Slug AR:** 28 Dmg | Short Range | Med FR | 20 Mag | 2.8s Reload | Uncommon. High impact.
52. **Bullpup-Z:** 21 Dmg | Med Range | Very Fast FR | 25 Mag | 1.8s Reload | Rare. Compact, good for Scout.
53. **Nexus-Dominator:** 25 Dmg | Long Range | Fast FR | 30 Mag | 2.0s Reload | Epic. Integrated Red Dot.
54. **Void-Eater:** 30 Dmg | Med Range | Med FR | 30 Mag | 2.5s Reload | Legendary. Heals on kill.
55. **Plasma-Caster:** 22 Dmg | Long Range | Fast FR | 40 Mag | 3.0s Reload | Rare. Projectile speed is slow.
56. **Scrap-Rifle:** 15 Dmg | Med Range | Fast FR | 40 Mag | 3.5s Reload | Common. Chance to jam (1%).
57. **G36-Hex:** 23 Dmg | Long Range | Fast FR | 30 Mag | 2.1s Reload | Uncommon. 1.5x zoom.
58. **FAMAS-Burst:** 14 Dmg (x3) | Med Range | Burst FR | 30 Mag | 2.2s Reload | Uncommon.
59. **AUG-Crystal:** 22 Dmg | Long Range | Med FR | 42 Mag | 2.5s Reload | Rare. 2.0x zoom.
60. **Honey-Badger:** 20 Dmg | Short Range | Very Fast FR | 30 Mag | 1.6s Reload | Rare. Built-in suppressor.

## 7.6 LMGs (Suppression)
61. **M249 SAW:** 18 Dmg | Med Range | Fast FR | 100 Mag | 4.5s Reload | Common. Great for suppression.
62. **Iron-Wall LMG:** 25 Dmg | Med Range | Slow FR | 80 Mag | 5.0s Reload | Uncommon. High structure damage.
63. **Sylvan-Spore LMG:** 16 Dmg | Short Range | Fast FR | 150 Mag | 6.0s Reload | Rare. Leaves poison clouds.
64. **PKM-Heavy:** 30 Dmg | Long Range | Slow FR | 100 Mag | 5.5s Reload | Uncommon. Highest LMG damage.
65. **Void-Screamer:** 20 Dmg | Med Range | Fast FR | 120 Mag | 4.0s Reload | Legendary. Increases fire rate as mag empties.
66. **Frost-Gatling:** 15 Dmg | Short Range | Hyper FR | 200 Mag | 8.0s Reload | Rare. Movement speed -20% while held.
67. **Mini-Gun:** 12 Dmg | Short Range | Hyper FR | 500 Mag | 10s Reload | Epic. Requires wind-up (1s).
68. **Lewis-Gun:** 28 Dmg | Med Range | Slow FR | 47 Mag | 3.5s Reload | Common. High accuracy.
69. **Browning-50:** 45 Dmg | Long Range | Very Slow FR | 50 Mag | 6.0s Reload | Rare. Semi-auto LMG.
70. **Storm-Hose:** 10 Dmg | Short Range | Hyper FR | 300 Mag | 5.0s Reload | Uncommon. Very high spread.

## 7.7 SNIPERS (Long Distance)
71. **Bolt-Action:** 80 Dmg | Extreme Range | Single FR | 5 Mag | 3.5s Reload | Common. One-shot headshot (no armor).
72. **Barrett-50:** 110 Dmg | Extreme Range | Single FR | 5 Mag | 4.5s Reload | Rare. High anti-material damage.
73. **Sylvan-Needle:** 70 Dmg | Long Range | Single FR | 1 Mag | 1.0s Reload | Uncommon. Silent, projectile drop.
74. **Void-Gaze:** 150 Dmg | Infinite Range | Single FR | 1 Mag | 6.0s Reload | Legendary. Raycast, pierces players.
75. **Dragon-Breath:** 90 Dmg | Long Range | Single FR | 5 Mag | 4.0s Reload | Rare. Ignites target.
76. **AWM-Crystal:** 95 Dmg | Extreme Range | Single FR | 5 Mag | 3.8s Reload | Epic. No bullet trail.
77. **SKS-Semi:** 45 Dmg | Long Range | Semi FR | 10 Mag | 2.5s Reload | Uncommon. Low recoil sniper.
78. **Kar-98:** 85 Dmg | Extreme Range | Single FR | 5 Mag | 4.0s Reload | Common. Fast ADS.
79. **VSS-Silent:** 35 Dmg | Med Range | Fast FR | 10 Mag | 2.0s Reload | Rare. Integrally suppressed, semi-auto.
80. **M24-Elite:** 90 Dmg | Extreme Range | Single FR | 5 Mag | 3.2s Reload | Rare. High velocity.

## 7.8 SHOTGUNS (Close Range)
81. **Pump-Action:** 10x8 Dmg | Short Range | Slow FR | 5 Mag | 0.8s/shell | Common. High spread.
82. **Double-Barrel:** 12x10 Dmg | Very Short Range | Hyper FR | 2 Mag | 2.0s Reload | Uncommon. Massive burst.
83. **SAIGA-12:** 8x8 Dmg | Short Range | Fast FR | 8 Mag | 2.5s Reload | Rare. Semi-auto shotgun.
84. **Sylvan-Thorn:** 6x12 Dmg | Short Range | Med FR | 5 Mag | 2.0s Reload | Uncommon. Spiky pellets stick and explode.
85. **Iron-Buster:** 15x6 Dmg | Short Range | Slow FR | 4 Mag | 3.0s Reload | Rare. High knockback.
86. **Void-Slug:** 60 Dmg | Med Range | Single FR | 1 Mag | 1.5s Reload | Rare. Single powerful projectile.
87. **AA-12 Auto:** 7x8 Dmg | Short Range | Fast FR | 20 Mag | 3.5s Reload | Epic. Full auto shotgun.
88. **Sawed-Off:** 10x10 Dmg | Point Blank | Fast FR | 2 Mag | 2.2s Reload | Common. Secondary slot weapon.
89. **Spas-12:** 11x8 Dmg | Short Range | Med FR | 8 Mag | 3.0s Reload | Uncommon. Fast swap.
90. **Crystal-Shards:** 5x20 Dmg | Short Range | Fast FR | 10 Mag | 2.5s Reload | Rare. Pellets bounce off walls.

## 7.9 EXPLOSIVES (Heavy)
91. **RPG-7:** 120 Dmg | Long Range | Single FR | 1 Mag | 4.0s Reload | Uncommon. High AOE.
92. **Grenade Launcher:** 80 Dmg | Med Range | Slow FR | 6 Mag | 5.0s Reload | Rare. Bouncing projectiles.
93. **C4-Charges:** 200 Dmg | Melee Range | Remote | 1 Mag | N/A | Uncommon. Sticky.
94. **Frag Grenade:** 100 Dmg | Med Range | Thrown | 1 Mag | N/A | Common. 3s fuse.
95. **Void-Bomb:** 50 Dmg | Med Range | Thrown | 1 Mag | N/A | Rare. Creates a gravity well.

## 7.10 SPECIAL WEAPONS (Exotic)
96. **Flamethrower:** 10 Dps | Short Range | Continuous | 100 Fuel | 4.0s Reload | Rare. Ignites environment.
97. **Crossbow:** 60 Dmg | Long Range | Single FR | 1 Mag | 2.0s Reload | Uncommon. Recoverable bolts.
98. **Tesla-Coil:** 15 Dmg | Short Range | Arcing | 50 Energy | 3.0s Reload | Rare. Hits up to 3 targets.
99. **The Crowbar:** 30 Dmg | Melee | Fast | N/A | N/A | Common. Breaks crates faster.
100. **Katana:** 50 Dmg | Melee | Fast | N/A | N/A | Rare. Can deflect bullets (10% chance).
101. **Nexus-Staff:** 40 Dmg | Med Range | Fast FR | 30 Energy | 2.0s Reload | Legendary. Fires homing orbs.


# SECTION 8: TERRITORY SYSTEM

## 8.1 Mechanics of Conquest
- **Capturing Land:** To capture a tile, a player or their army must stay within the tile boundaries for a duration (Base: 10 seconds).
- **Contestation:** If two players from different kingdoms are on the same tile, the capture timer pauses.
- **Kingdom Borders:** Captured tiles change to the kingdom's color. Adjacent tiles provide a "Defense Bonus" (+5% Armor) to the owner.
- **Expansion Mechanics:** Players can only capture tiles adjacent to their existing territory (Starting from the spawn pod).

## 8.2 Territory Levels
Each tile can be leveled up by spending resources:
- **Level 1 (Outpost):** No bonus.
- **Level 2 (Fortified):** +10% HP for all buildings on this tile.
- **Level 3 (Developed):** Passive resource generation speed +15%.
- **Level 4 (Stronghold):** Provides a minimap "Fog of War" reveal for 2 tiles out.
- **Level 5 (Bastion):** Reduces enemy movement speed by 20% on this tile.

## 8.3 Capital Cities
The first tile captured (Drop Pod location) becomes the "Initial Capital." If this tile is lost, all territory benefits are halved until a new Capital is designated (at a cost).

---

# SECTION 9: BUILDING SYSTEM (100+ CATALOG)

## 9.1 INFRASTRUCTURE & RESOURCE BUILDINGS (Part 1)

1. **Town Hall (Lvl 1):** Cost: 100 Wood, 100 Stone. Time: 30s. Essential for all other buildings.
2. **Town Hall (Lvl 2):** Cost: 500 Wood, 500 Stone, 100 Iron. Time: 120s. Unlocks Tier 2 units.
3. **Town Hall (Lvl 3):** Cost: 2000 Wood, 2000 Stone, 1000 Iron, 500 Oil. Time: 300s. Unlocks Tier 3 units.
4. **Woodcutter’s Hut:** Cost: 50 Wood. Time: 15s. Generates 5 Wood/min.
5. **Sawmill:** Cost: 200 Wood, 100 Stone. Time: 45s. Increases Woodcutter output by 50%.
6. **Logging Camp:** Cost: 500 Wood, 200 Stone. Time: 90s. Can harvest distant trees.
7. **Stone Quarry:** Cost: 50 Stone. Time: 15s. Generates 5 Stone/min.
8. **Masonry Shop:** Cost: 200 Stone, 100 Iron. Time: 45s. Increases Quarry output by 50%.
9. **Granite Mine:** Cost: 600 Stone, 300 Iron. Time: 120s. High-yield stone source.
10. **Iron Mine:** Cost: 150 Wood, 150 Stone. Time: 60s. Generates 2 Iron/min.
11. **Blast Furnace:** Cost: 400 Iron, 200 Stone. Time: 90s. Refines Iron into Aether-Steel.
12. **Oil Rig:** Cost: 500 Iron, 300 Stone. Time: 120s. Generates 2 Oil/min. Only on Oil Nodes.
13. **Oil Refinery:** Cost: 1000 Iron, 500 Oil. Time: 180s. Increases Oil output by 40%.
14. **Small Granary:** Cost: 100 Wood. Time: 30s. Stores 1000 Food.
15. **Large Silo:** Cost: 500 Stone, 200 Iron. Time: 60s. Stores 5000 Food.
16. **Basic Farm:** Cost: 50 Wood. Time: 20s. Generates 10 Food/min.
17. **Irrigated Fields:** Cost: 200 Stone. Time: 40s. Increases Farm output by 30%.
18. **Cattle Ranch:** Cost: 300 Wood, 100 Food. Time: 60s. High-yield Food source.
19. **Water Well:** Cost: 50 Stone. Time: 10s. Reduces building fire risk.
20. **Power Plant:** Cost: 1000 Iron, 500 Oil. Time: 150s. Generates 10 Energy/min.
21. **Solar Array:** Cost: 800 Iron, 200 Gems. Time: 120s. Passive Energy in Deserts.
22. **Wind Turbine:** Cost: 600 Wood, 400 Iron. Time: 100s. Energy source for Mountains.
23. **Battery Bank:** Cost: 500 Iron, 100 Oil. Time: 60s. Stores 500 Energy.
24. **Storage Depot (Wood):** Cost: 100 Wood, 50 Stone. Time: 20s. +500 Wood Cap.
25. **Storage Depot (Stone):** Cost: 100 Stone, 50 Wood. Time: 20s. +500 Stone Cap.
26. **Iron Vault:** Cost: 300 Iron. Time: 40s. +300 Iron Cap.
27. **Oil Tank:** Cost: 400 Iron. Time: 45s. +400 Oil Cap.
28. **Gem Safe:** Cost: 500 Stone, 500 Iron. Time: 60s. +100 Gem Cap.
29. **Workshop:** Cost: 200 Wood, 200 Stone. Time: 40s. Increases gathering speed by 10%.
30. **Tool Smithy:** Cost: 300 Iron, 100 Stone. Time: 60s. Unlocks Tier 2 tools.
31. **Foundry:** Cost: 600 Iron. Time: 90s. Required for Tank production.
32. **Laboratory:** Cost: 1000 Iron, 200 Gems. Time: 180s. Unlocks Level 2 Spells/Tech.
33. **Research Wing:** Cost: 2000 Iron, 500 Gems. Time: 300s. Required for Tier 4 tech.
34. **Marketplace:** Cost: 500 Wood, 500 Stone. Time: 60s. Allows resource trading.
35. **Trade Depot:** Cost: 1000 Stone, 500 Iron. Time: 90s. Passive Gold from territory.
36. **Bank:** Cost: 2000 Iron, 1000 Gems. Time: 200s. Interest on Gold (1%/min).
37. **Road (Dirt):** Cost: 10 Stone/tile. Time: 1s. +10% Move Speed.
38. **Road (Paved):** Cost: 30 Stone, 10 Iron/tile. Time: 3s. +25% Move Speed.
39. **Bridge:** Cost: 100 Wood, 50 Iron. Time: 20s. Allows crossing Rivers.
40. **Signpost:** Cost: 10 Wood. Time: 2s. Mark locations on Clan Map.
41. **Small House:** Cost: 50 Wood. Time: 15s. +2 Population Cap.
42. **Large Tenement:** Cost: 200 Wood, 100 Stone. Time: 40s. +10 Population Cap.
43. **Apartment Block:** Cost: 500 Stone, 200 Iron. Time: 90s. +30 Population Cap.
44. **Hospital:** Cost: 400 Stone, 200 Iron. Time: 60s. Heals nearby allies (5 HP/sec).
45. **Clinic:** Cost: 100 Wood, 50 Stone. Time: 30s. Heals 2 HP/sec.
46. **Sanatorium:** Cost: 1000 Iron, 500 Gems. Time: 120s. Heals 10 HP/sec + removes debuffs.
47. **Mess Hall:** Cost: 200 Wood, 100 Food. Time: 40s. Reduces hunger rate by 20%.
48. **Kitchen:** Cost: 50 Wood, 50 Stone. Time: 20s. Converts raw food to "Rations" (Higher regen).
49. **Bakery:** Cost: 300 Wood. Time: 30s. Passive Food generation.
50. **Fisherman’s Pier:** Cost: 100 Wood. Time: 25s. Generates Food from Oceans/Rivers.


## 9.2 MILITARY & SPECIAL BUILDINGS (Part 2)

51. **Infantry Barracks:** Cost: 200 Wood, 100 Stone. Time: 45s. Trains Soldiers and Archers.
52. **Archery Range:** Cost: 300 Wood, 150 Iron. Time: 60s. Increases Archer accuracy by 10%.
53. **Cavalry Stables:** Cost: 500 Wood, 200 Food. Time: 90s. Trains Knights and Light Cavalry.
54. **Vehicle Workshop:** Cost: 1000 Iron, 500 Oil. Time: 150s. Trains Tanks and Armored Cars.
55. **Airfield:** Cost: 2000 Iron, 1000 Oil. Time: 240s. Trains Aircraft and Drones.
56. **Shipyard:** Cost: 1000 Wood, 500 Iron. Time: 180s. Only on Oceans. Trains Boats.
57. **Training Ground:** Cost: 400 Stone. Time: 60s. Passively XP-levels nearby units.
58. **Armory:** Cost: 500 Iron. Time: 80s. Unlocks Tier 2 Armor for units.
59. **Munition Factory:** Cost: 1000 Iron. Time: 120s. Unlocks Tier 2 Ammo (+10% damage).
60. **Wood Wall (Section):** Cost: 10 Wood. Time: 2s. Basic 100 HP barrier.
61. **Stone Wall (Section):** Cost: 25 Stone. Time: 5s. 500 HP barrier.
62. **Iron Wall (Section):** Cost: 50 Iron. Time: 10s. 2000 HP barrier.
63. **Reinforced Gate:** Cost: 100 Stone, 50 Iron. Time: 15s. Ally-only passage.
64. **Watch Tower:** Cost: 100 Wood. Time: 30s. +300% Vision Range.
65. **Guard Tower (Arrow):** Cost: 200 Stone. Time: 45s. Passive auto-attack (Short range).
66. **Ballista Tower:** Cost: 500 Wood, 200 Iron. Time: 60s. Anti-Cavalry / Anti-Tank.
67. **Cannon Battery:** Cost: 1000 Iron. Time: 90s. Long-range siege defense.
68. **Flak Cannon:** Cost: 800 Iron. Time: 70s. Anti-Air defense.
69. **Tesla Tower:** Cost: 1500 Iron, 500 Gems. Time: 120s. Chain-lightning defense.
70. **Mortar Pit:** Cost: 600 Stone, 400 Iron. Time: 80s. Indirect fire defense.
71. **Moat (Tile):** Cost: 200 Wood. Time: 30s. -80% Enemy Move Speed.
72. **Spike Trap:** Cost: 20 Wood, 10 Iron. Time: 5s. Hidden damage to Infantry.
73. **Land Mine:** Cost: 50 Iron, 20 Oil. Time: 5s. Hidden AOE damage.
74. **Radar Station:** Cost: 1500 Iron, 1000 Energy. Time: 150s. Reveals map in large radius.
75. **Jammer Tower:** Cost: 1000 Iron, 500 Energy. Time: 100s. Hides territory from enemy Radar.
76. **Shield Generator:** Cost: 2000 Energy, 1000 Gems. Time: 200s. Absorbs 5000 Dmg for tile.
77. **Communication Hub:** Cost: 500 Iron. Time: 60s. Increases Clan Chat range.
78. **Diplomatic Embassy:** Cost: 1000 Stone. Time: 90s. Required for Alliances.
79. **Bounty Board:** Cost: 200 Wood. Time: 30s. Rewards for killing specific players.
80. **Prison:** Cost: 1000 Stone, 500 Iron. Time: 120s. Captures downed enemy players (timed).
81. **Statue of Victory:** Cost: 5000 Gems. Time: 600s. Global buff (+5% Dmg) for Kingdom.
82. **Royal Palace:** Cost: 10000 Stone, 5000 Iron, 1000 Gems. Time: 1200s. Alternate Victory condition.
83. **Aether-Forge:** Cost: 2000 Iron, 1000 Energy. Time: 180s. Crafts Legendary Weapons.
84. **Alchemist’s Lab:** Cost: 500 Food, 500 Energy. Time: 90s. Creates combat potions.
85. **Portal (Entry):** Cost: 2000 Energy, 500 Gems. Time: 150s. Fast travel (Must have exit).
86. **Portal (Exit):** Cost: 1000 Energy, 200 Gems. Time: 60s.
87. **Repair Station:** Cost: 300 Iron. Time: 40s. Passively repairs buildings/vehicles.
88. **Scrap Yard:** Cost: 100 Stone. Time: 30s. Converts unused weapons to Iron.
89. **Temple of the Void:** Cost: 3000 Gems. Time: 300s. Slows Void encroachment nearby.
90. **Dragon Perch:** Cost: 5000 Food, 2000 Gems. Time: 600s. Spawns high-tier AI Dragon.
91. **Mech Hangar:** Cost: 5000 Iron, 2000 Energy. Time: 400s. Trains Giant Mechs.
92. **Cryo-Chamber:** Cost: 1000 Energy. Time: 120s. Stores player if they disconnect (Safe-logout).
93. **Spy Agency:** Cost: 1000 Gold. Time: 90s. See enemy resource counts.
94. ** Propaganda Tower:** Cost: 500 Gold. Time: 60s. Increases NPC recruit speed.
95. **Tax Office:** Cost: 500 Gold. Time: 60s. Converts population to passive Gold.
96. **Observatory:** Cost: 1000 Stone, 500 Gems. Time: 180s. Predicts where Storm will shrink.
97. **Underground Bunker:** Cost: 2000 Stone. Time: 240s. Safe from Air-strikes.
98. **Treasure Vault:** Cost: 5000 Stone, 5000 Gems. Time: 300s. Passive Gem generation.
99. **Market Stall:** Cost: 50 Wood. Time: 10s. Sell Food for Gold.
100. **The Crown Throne:** Cost: N/A. (Spawned in Nexus). Final Victory Building.

---

# SECTION 10: RESOURCE SYSTEM

## 10.1 The Resource Loop
Kingdom Royale utilizes 8 distinct resources to balance combat, building, and logistics.

1. **Gold:**
   - **Generation:** Trade Depots, Tax Offices, Player Kills, Selling items.
   - **Usage:** Trading, Mercenary recruitment, Diplomacy costs, Respawning.
2. **Wood:**
   - **Generation:** Forests, Woodcutter Huts, Breaking Crates.
   - **Usage:** Early building, Arrows, Bridges, Ships.
3. **Stone:**
   - **Generation:** Mountains, Quarries, Mining.
   - **Usage:** Walls, Defensive Towers, Permanent Infrastructure.
4. **Iron:**
   - **Generation:** Deserts, Mines, Scrapping items.
   - **Usage:** Advanced weapons, Tanks, Armor, Tier 2+ buildings.
5. **Oil:**
   - **Generation:** Oil Rigs (Desert/Ocean nodes).
   - **Usage:** Vehicle fuel, Explosives, Power Plants.
6. **Food:**
   - **Generation:** Farms, Fishing, Hunting AI Animals.
   - **Usage:** Hunger management, Training AI Units (Maintenance).
7. **Energy:**
   - **Generation:** Power Plants, Solar/Wind, Nexus Orbs.
   - **Usage:** Advanced tech (Shields, Radars, Teleports), Laser weapons.
8. **Gems:**
   - **Generation:** Boss loot, Deep Mines, Gem Safes.
   - **Usage:** Legendary upgrades, Palace construction, Special abilities.

## 10.2 Economy Balance
- **Scarcity:** Iron and Oil are 70% less common in the Outlands than the Mid-Rim.
- **Conversion:** Marketplaces allow trading (e.g., 5 Wood -> 1 Iron) with a 20% Tax.
- **Maintenance:** AI Armies consume Food and Gold every minute. If resources run out, units desert or defect.


# SECTION 11: ARMY SYSTEM

## 11.1 Unit Control & Groups
- **The Squad:** Each player can lead a squad of AI units. Max squad size is determined by Level and the "Commander" class bonus (Base: 5, Max: 20).
- **Command Keys:**
  - `F1`: Follow Me (Aggressive).
  - `F2`: Defend Location (Stay in tile).
  - `F3`: Attack Target (Focus fire).
  - `F4`: Patrol (Cycle between two tiles).

## 11.2 Unit Classifications

### 11.2.1 Infantry (The Frontline)
1. **Recruit:** 50 HP. Basic SMG. Cheap, low accuracy.
2. **Veteran:** 100 HP. Assault Rifle. Solid all-rounder.
3. **Shield-Bearer:** 150 HP. Riot Shield + Pistol. Absorbs fire.
4. **Heavy Gunner:** 200 HP. LMG. Slow movement, high suppression.

### 11.2.2 Archers (The Ranged)
1. **Longbowman:** 40 HP. High range, low fire rate.
2. **Crossbowman:** 60 HP. Armor-piercing bolts.
3. **Fire-Archer:** 40 HP. Sets buildings on fire.

### 11.2.3 Cavalry (The Mobile)
1. **Light Cavalry:** Fast horses. Used for scouting and flanking.
2. **Heavy Knight:** High armor, lance charge (stun effect).
3. **Hover-Biker:** Tech-cavalry. High speed, dual blasters.

### 11.2.4 Tanks (The Siege)
1. **Light Tank:** 1000 HP. Fast, light cannon.
2. **Main Battle Tank:** 2500 HP. Heavy cannon, co-axial MG.
3. **Siege Ram:** 5000 HP. Melee only. Massive building damage.

### 11.2.5 Mechs (The Titans)
1. **Spider Mech:** Can climb walls. Dual SMGs.
2. **Nexus Colossus:** 10000 HP. Laser beams. Requires Gems to build.

### 11.2.6 Aircraft (The Air)
1. **Scout Drone:** Silent, reveals fog of war.
2. **Attack Chopper:** Rockets and MG. Fast but fragile to Flak.
3. **Bomber:** Slow, drops heavy AOE bombs on tiles.

### 11.2.7 Naval Units (The Sea)
1. **Patrol Boat:** Fast, light MG.
2. **Destroyer:** Long-range artillery.
3. **Submarine:** Stealthy, torpedoes.

---

# SECTION 12: AI SYSTEM

## 12.1 Bot Behavior (The "Ghost" System)
Kingdom Royale features 3 levels of AI difficulty:

1. **Passive (Wildlife/Scavengers):**
   - Flee from players.
   - Attack only if cornered.
   - Focus on resource nodes.
2. **Aggressive (The Void Cultists):**
   - Patrol the Void edges.
   - Attack any player on sight.
   - Do not capture land, but destroy buildings.
3. **Strategic (Enemy Commanders):**
   - Mimic player behavior.
   - Capture land, build bases, and train armies.
   - Use "Squad Formations" (V-shape for attack, Square for defense).

## 12.2 Pathfinding (A* Grid)
- **Dynamic Obstacles:** AI recalculates paths when walls are built or destroyed.
- **Biometric Preference:** Sylvan units move faster in Forest; Iron units avoid Magma.
- **Flanking Logic:** If a player is in cover, the AI attempts to split into two groups to flank.

## 12.3 Target Selection (Priority Weighting)
AI prioritizes targets based on a score (0-100):
- **High Weight (90+):** Wounded players, Medics, unprotected Town Halls.
- **Medium Weight (50-80):** Enemy soldiers, Towers, Resource collectors.
- **Low Weight (<50):** Walls, Tanks, high-HP fortifications.

## 12.4 Base Defense
- **Alarm System:** If one AI unit is attacked, all units in a 5-tile radius converge on the attacker.
- **Repair Logic:** Engineer-class AI units prioritize repairing damaged structures over combat.


# SECTION 13: BOSS SYSTEM

## 13.1 Boss Mechanics
- **Spawn Conditions:** Bosses appear in specific "Boss Zones" (3.3) or are triggered by player actions (e.g., reaching Level 10, capturing a City).
- **Phasing:** Most bosses have 3 phases at 100%, 50%, and 10% HP.
- **Loot Table:** Bosses drop "Artifacts" (Permanent match buffs) and massive amounts of Gems.

## 13.2 BOSS LIST (1-25)

1. **The Rust King:** Lore: Former ruler of the South. Skills: Magnetic Pull, Scrap Rain. HP: 5000. Spawn: Desert Outskirts.
2. **Iron Behemoth:** Lore: A rogue Hegemony tank. Skills: Cannon Barrage, Smoke Screen. HP: 8000. Spawn: Mid-Rim Roads.
3. **Sylvan Queen:** Lore: Guardian of the East. Skills: Entangling Vines, Spore Cloud. HP: 4500. Spawn: Deep Forest.
4. **Frost-Lord Vael:** Lore: A corrupted sentinel. Skills: Blizzard Aura, Ice Spike. HP: 6000. Spawn: Glacial Peaks.
5. **Magma Golem:** Lore: Born from the Ember Lowlands. Skills: Lava Pool, Ground Slam. HP: 9000. Spawn: Volcanic Crater.
6. **The Void-Stalker:** Lore: A creature from beyond. Skills: Teleport, Life Drain. HP: 3000 (Hard to hit). Spawn: Void Edge.
7. **Captain "Grog" Flint:** Lore: Pirate lord of the North. Skills: Cannon Volley, Cutlass Dash. HP: 5500. Spawn: Coastal City.
8. **Mech-Prime:** Lore: First experimental AI. Skills: Laser Beam, Rocket Salvo. HP: 10000. Spawn: Industrial Zone.
9. **The Great Arachnid:** Lore: mutated spider. Skills: Web Trap, Poison Bite. HP: 4000. Spawn: Forest Caves.
10. **Sky-Dreadnought:** Lore: Flying fortress. Skills: Carpet Bomb, AA-Defense. HP: 12000. Spawn: Mid-air (Drops crates).
11. **Emerald Dragon:** Lore: Ancient forest protector. Skills: Poison Breath, Wing Buffet. HP: 15000. Spawn: Dragon Perch.
12. **Obsidian Titan:** Lore: The mountain itself. Skills: Boulder Throw, Earthquake. HP: 20000. Spawn: Northern Pass.
13. **Nexus Guardian (Alpha):** Lore: Protector of the Crown. Skills: Shield Pulse, Energy Burst. HP: 7000. Spawn: Nexus Gate.
14. **The Sand-Worm:** Lore: Terror of the dunes. Skills: Burrow, Swallow. HP: 6500. Spawn: Shifting Sands.
15. **Cryo-Lich:** Lore: Former Frost-Guard priest. Skills: Freeze Ray, Summon Skelton. HP: 5000. Spawn: Crystal Palace.
16. **The Scrap-Reaper:** Lore: Scavenger bot gone mad. Skills: Chainsaw Dash, Hook Pull. HP: 4000. Spawn: Junkyard.
17. **Abyssal Kraken:** Lore: Ocean terror. Skills: Tentacle Slam, Whirlpool. HP: 11000. Spawn: Deep Sea.
18. **The Fire-Phoenix:** Lore: Eternal flame. Skills: Fire Nova, Rebirth. HP: 3000 (Revives once). Spawn: Ember Lowlands.
19. **Void-Horror:** Lore: Embodiment of the Storm. Skills: Darkness Veil, Fear Induce. HP: 9000. Spawn: Final Storm Circle.
20. **Steam-Sovereign:** Lore: Hegemony’s greatest engineer. Skills: Steam Burst, Turret Deploy. HP: 6000. Spawn: Iron Factory.
21. **The Bone-Dragon:** Lore: Necrotic remains. Skills: Bone Spikes, Death Breath. HP: 13000. Spawn: Cursed Valley.
22. **Glitch-Master:** Lore: Corrupted data form. Skills: Clone, Lag-Spike (Visual). HP: 4500. Spawn: Hidden Lab.
23. **The Golem-Mother:** Lore: Creator of the sand-golems. Skills: Summon Minions, Rock Shield. HP: 8500. Spawn: Desert Temple.
24. **Storm-Caller:** Lore: Master of weather. Skills: Lightning Strike, Tornado. HP: 7000. Spawn: Peak Observatory.
25. **The Royal Traitor:** Lore: Hero who betrayed Aethelgard. Skills: Parry, Rapid Slash. HP: 5500. Spawn: Capital Ruins.


## 13.3 BOSS LIST (26-50)

26. **The Void-Whale:** Lore: Massive flying creature. Skills: Gravity Shift, Tail Swipe. HP: 25000. Spawn: Upper Atmosphere (Requires Aircraft).
27. **Shadow-General:** Lore: Leader of the Void Cult. Skills: Dark Slash, Summon Wraiths. HP: 6000. Spawn: Cultist Camp.
28. **Techno-Lich:** Lore: Undead cyborg. Skills: Virus Hack (Disables bots), Plasma Bolt. HP: 7500. Spawn: Data Center.
29. **The Emerald Basilisk:** Lore: Gaze of death. Skills: Petrification, Acid Spit. HP: 8000. Spawn: Jungle Temple.
30. **Glacial Hydra:** Lore: Multiple frozen heads. Skills: Ice Beam, Bite. HP: 12000. Spawn: Frozen Lake.
31. **Solar Flare:** Lore: Living energy. Skills: Sun Beam, Blindness. HP: 4000. Spawn: Desert Peak.
32. **The Rust Colossus:** Lore: Scrap metal giant. Skills: Metal Stomp, Magnetize. HP: 15000. Spawn: Scrap-Town.
33. **Iron-Drake:** Lore: Armored dragon. Skills: Fireball, Wing Slam. HP: 14000. Spawn: Iron Mountain.
34. **The Ghost-Ship:** Lore: Cursed frigate. Skills: Spectral Broadside, Fog. HP: 9000. Spawn: Ocean Ghost Zone.
35. **Obsidion Beetle:** Lore: Armored insect. Skills: Charge, Shell Spin. HP: 10000. Spawn: Volcanic Tubes.
36. **The Great Totem:** Lore: Sylvan defense pillar. Skills: Nature’s Wrath, Healing Roots. HP: 20000. Spawn: Forest Heart.
37. **Void-Seeker:** Lore: Storm vanguard. Skills: Rift Opening, Energy Drain. HP: 5000. Spawn: Storm Eye.
38. **The Clockwork Spider:** Lore: Hegemony trap. Skills: Web Trap, Self-Destruct. HP: 3500. Spawn: Factory Basement.
39. **Elder Treant:** Lore: Oldest living tree. Skills: Root Crush, Leaf Storm. HP: 18000. Spawn: Ancient Woods.
40. **The Mirage Stalker:** Lore: Desert phantom. Skills: Invisibility, Backstab. HP: 4500. Spawn: Sandstorm.
41. **Ice-Phoenix:** Lore: Frozen rebirth. Skills: Cold Snap, Ice Blast. HP: 4000. Spawn: Snowy Peak.
42. **The Drill-Machine:** Lore: Subterranean terror. Skills: Burrow, Ground Drill. HP: 11000. Spawn: Underground.
43. **Aether-Elemental:** Lore: Pure magic. Skills: Random Spell, Pulse. HP: 6000. Spawn: Magic Fountain.
44. **The Bone-Goliath:** Lore: Undead giant. Skills: Bone Throw, Scream. HP: 14000. Spawn: Graveyard.
45. **Cyborg-Bear:** Lore: Augmented predator. Skills: Maul, Sonic Roar. HP: 7000. Spawn: Tech-Forest.
46. **The Void-Queen:** Lore: Storm's conscience. Skills: Reality Warp, Summon Elite. HP: 30000. Spawn: Nexus Throne.
47. **Alpha-Wolf (Tech):** Lore: Pack leader with laser. Skills: Laser Bite, Howl (Summon). HP: 5500. Spawn: Forest Rim.
48. **The Crystal Golem:** Lore: Reflective protector. Skills: Laser Reflection, Shard Rain. HP: 12000. Spawn: Crystal Cave.
49. **Steam-Tank Mark VII:** Lore: Ultimate prototype. Skills: Rapid Fire, Flamethrower. HP: 15000. Spawn: Capital Defense.
50. **The Final Sentinel:** Lore: Guardian of the End. Skills: All previous boss skills. HP: 50000. Spawn: Final 1x1 Tile.


# SECTION 14: UI DESIGN

## 14.1 General Aesthetics
- **Style:** Flat, futuristic "Magi-tech" HUD. Semi-transparent dark panels with glowing cyan accents.
- **Font:** Roboto Condensed for data; Orbitron for headers.
- **Layering:** UI is rendered in 3 layers: Game Layer, HUD Layer, and Menu Layer.

## 14.2 Pixel-Perfect Screen Layouts

### 14.2.1 Login Screen
- **Center:** Kingdom Royale Logo (Animated with Void particles).
- **Below Logo:** "Sign in with Google" button (240x50px, standard branding).
- **Bottom Left:** Version Number (v1.0.4).
- **Bottom Right:** Terms of Service & Privacy Policy links.
- **Background:** Panoramic sweep of the Nexus map.

### 14.2.2 Main Menu
- **Top Bar:**
  - Left: Player Avatar, Name, Level.
  - Right: Gold, Gems, Energy count.
- **Center Left:** 3D Character Model of current Class.
- **Center Right:**
  - [PLAY] Button (Large, Green, 400px).
  - [LOADOUT] Button (Grey).
  - [CLAN] Button (Blue).
- **Bottom Bar:**
  - [SHOP], [SETTINGS], [LEADERBOARDS], [NEWS].

### 14.2.3 Battle HUD (In-Game)
- **Top Left:** Minimap (Circular, 200px diameter). Shows territory colors and Storm circle.
- **Top Right:** Kill Feed & Player Count.
- **Bottom Left:**
  - Health Bar (Green, 300px).
  - Armor Bar (Blue, 300px).
  - Hunger Bar (Orange, 200px).
- **Bottom Center:** Hotbar (1-5 slots for Weapons/Consumables).
- **Bottom Right:** Ammo Counter, Stamina Bar (Vertical, yellow).
- **Center Left (Small):** Army Command Menu (F1-F4 icons).
- **Center Right (Small):** Quick Build Menu (Walls/Towers).

### 14.2.4 Inventory / Build Menu (Tab Key)
- **Left Panel:** Grid of 20 slots for collected loot.
- **Middle Panel:** Detailed Item Stats.
- **Right Panel:** Building Categories (Resource, Military, Defense).
- **Bottom:** "Drop Item" and "Craft" buttons.

### 14.2.5 Clan Screen
- **Left:** Clan List & Member Count.
- **Right:** Diplomacy Map (Shows allied vs enemy territory in the current match).
- **Center:** Clan Level & Perk Tree.

## 14.3 Button Locations (Coordinates for 1920x1080)
- **Exit Menu:** (1880, 40) - Red 'X'.
- **Chat Open:** (40, 1040) - Speech Bubble icon.
- **Map Expand:** (200, 200) - Corner of minimap.

---

# SECTION 15: GOOGLE LOGIN & ACCOUNT SYSTEM

## 15.1 Authentication Flow
1. **Initiation:** Player clicks "Sign in with Google."
2. **OAuth 2.0:** Redirects to Google secure popup.
3. **Token Exchange:** Backend receives JWT (JSON Web Token), validates with Google API.
4. **Account Creation:** If UID doesn't exist in PostgreSQL, create new record.
5. **Session:** Backend issues a secure Session Cookie and connects to Socket.io.

## 15.2 Guest Mode
- Limited to Level 5.
- Data stored in `localStorage`.
- Warning prompt: "Sign in to save progression and join Clans."

## 15.3 Account Linking
- Players can link Guest accounts to Google accounts via Settings -> Account.
- Merge logic: Guest XP is added to Google Account XP if Google Account is Level 1.

## 15.4 Security System
- **Rate Limiting:** Max 5 login attempts per minute per IP.
- **Encryption:** All user data (Email/UID) encrypted using AES-256 at rest.
- **Tokens:** Refresh tokens rotate every 24 hours.

## 15.5 Cloud Save & Recovery
- Player "State" (Unlocks, Ranks, Purchases) is synced every 60 seconds to the DB.
- Recovery is handled entirely via Google Account recovery tools.


# SECTION 16: CLAN SYSTEM

## 16.1 Guild Structure
- **Tiers:** Recruits, Knights, Officers, Elders, King/Queen.
- **Perks:** Passively earned by donating Gold to the Clan Bank.
- **Clan Hall:** A persistent persistent social space for the guild.

## 16.2 Alliances & Diplomacy
- **Peace Treaty:** Cannot damage each other's units for 10 minutes.
- **Trade Agreement:** 0% Marketplace tax between allied clans.
- **War Declaration:** Allows capturing the other clan's capital city even in the Outlands.

## 16.3 Clan Territory Ownership
- In competitive "Season Maps," clans fight to own persistent regions of the world.
- Revenue from "Tax Offices" in these regions is shared among top contributors.

---

# SECTION 17: CHAT SYSTEM

## 17.1 Channels
- **Global:** All players in the match.
- **Kingdom:** All players of the same faction.
- **Clan:** Private guild chat.
- **Whisper:** One-on-one private messages.

## 17.2 Moderation & Reporting
- **Profanity Filter:** Automated regex-based masking of toxic language.
- **Report UI:** Right-click player name -> Report for [Cheating, Toxicity, Griefing].
- **Auto-Mute:** 3 reports in 10 minutes results in a 1-hour global mute.

---

# SECTION 18: ANTI-CHEAT ARCHITECTURE

## 18.1 Client-Side Protection
- **Memory Obfuscation:** Critical values (HP, Ammo) are stored as XOR-encrypted variables to prevent Cheat Engine scanning.
- **WASM Integrity:** The game binary is checked for tampering on load.

## 18.2 Server-Side Validation (SSV)
- **Movement:** Server calculates Max Speed for each class. If player Delta-X/Y exceeds this, they are rubber-banded back.
- **Combat:** Hits are validated via server-side raycasting against player position history.
- **Fire Rate:** Server tracks "Time Since Last Shot." If faster than weapon allows, shots are ignored.

## 18.3 Detection Algorithms
- **Aimbot Detection:** Analyze angular velocity of crosshair. Humans have jitter; bots move in perfect linear/Bezier curves.
- **Macro Detection:** Analyze click intervals. Perfect 0.100s clicks are flagged as macros.

## 18.4 Banning
- **Shadow Ban:** Cheaters are placed in lobbies with other cheaters.
- **HWID Ban:** Unique hardware identifiers are banned, preventing easy account remaking.

---

# SECTION 19: BACKEND ARCHITECTURE

## 19.1 Tech Stack
- **API Server:** Node.js / Express.
- **Real-time Engine:** Socket.io with Binary Serialization (Protocol Buffers).
- **Database:**
  - PostgreSQL for persistent user data.
  - Redis for match state and leaderboard caching.
- **Matchmaking:** Go-based microservice using Elo-rating system.

## 19.2 Horizontal Scaling
- **Load Balancer:** Nginx/AWS ELB distributes traffic.
- **Game Instances:** Each match runs on an isolated Docker container (1 CPU / 2GB RAM).
- **Auto-Scaling:** K8s clusters spin up new instances based on queue length.

---

# SECTION 20: PROGRESSION SYSTEM

## 20.1 Player XP & Levels
- **Combat XP:** 100 XP per kill, 10 XP per hit.
- **Strategic XP:** 50 XP per tile captured, 200 XP per building finished.
- **Rank Titles:** Level 1-10: Peasant; 11-30: Squire; 31-60: Knight; 61-90: Lord; 91-100: Monarch.

## 20.2 Seasonal Ranks
- **Bronze -> Silver -> Gold -> Platinum -> Diamond -> Crown.**
- Ranks reset every 3 months. Rewards based on peak rank.

## 20.3 Missions
- **Daily:** "Capture 10 Desert Tiles," "Deal 1000 DMG with SMGs."
- **Weekly:** "Participate in 3 Clan Wars," "Defeat a Mid-Rim Boss."
- **Achievements:** 500+ unique badges (e.g., "The Pacifist" - win a match with 0 kills).


# SECTION 21: COSMETICS

## 21.1 Player Skins
- **Themed Sets:** High-fantasy, Cyberpunk, Tactical, and Seasonal (Halloween/Winter).
- **Rarity:** Common (Palette swap), Rare (New model detail), Epic (VFX trails), Legendary (Custom voice/animations).

## 21.2 Weapon Skins
- **Camo:** Practical military patterns.
- **Neon:** Glow-in-the-dark lines.
- **Relic:** Gold and engraved steel.

## 21.3 Animations & Emotes
- **Victory Dance:** Plays on the final Nexus tile.
- **Spray Paints:** Players can "Tag" captured territory with their emblem.

---

# SECTION 22: SOUND DESIGN

## 22.1 Music Landscape
- **Dynamic Score:** Calm orchestral music during scavenging; shifts to heavy industrial techno when in combat; high-tension strings as the Storm closes.
- **Biome Themes:** Wind-howls in Mountains, mechanical humming in Desert.

## 22.2 Combat SFX
- **Audio Spatialization:** HRTF-based 3D sound. Players can hear the exact direction of footsteps and gunshots.
- **Weapon Samples:** Authentic high-bitrate recordings of each caliber.

---

# SECTION 23: TECHNICAL ART DIRECTION

## 23.1 Character Design
- **Shape Language:**
  - Soldiers: Squares (Stable/Strong).
  - Scouts: Triangles (Fast/Sharp).
  - Medics: Circles (Healing/Soft).
- **Proportions:** 2D top-down, slightly oversized heads (1:4 ratio) for better emote visibility.

## 23.2 Visual Effects (VFX)
- **Void Particles:** Dark purple swirling nebulae with "static" glitch effects.
- **Destruction:** Buildings shatter into 3-5 physics-based "debris" chunks before disappearing.

---

# SECTION 24: GAME BALANCE FORMULAS

## 24.1 Combat Scaling
- `Armor_DR = Armor_Value / (Armor_Value + 100)` -> Diminishing returns on high armor.

## 24.2 Economy Pacing
- `Capture_Time = 10s * (1.5 ^ Number_of_Allied_Tiles)` -> Expansion becomes harder the larger you are.

---

# SECTION 25: MONETIZATION (ETHICAL MODEL)

## 25.1 NO Pay-to-Win (P2W)
- Zero gameplay advantages can be bought. No "VIP damage bonuses" or "Instant Build" purchases with real money.

## 25.2 The Battle Pass
- **Free Track:** 50 levels of basic skins and gold.
- **Premium Track ($9.99):** 100 levels of exclusive Legendary cosmetics and Gem rewards.

## 25.3 Daily Shop
- Rotating selection of 4 weapon skins and 2 emotes.

---

# SECTION 26: ROADMAP

## 26.1 Phase 1: Alpha (Months 1-4)
- Core combat and 10 weapons.
- Map: Desert biome only.
- Tech: Multiplayer stress testing (100 players).

## 26.2 Phase 2: Beta (Months 5-8)
- All 4 biomes.
- First 25 Bosses.
- Building system v1.0.

## 26.3 Phase 3: Launch (Month 12)
- All 100 weapons and 100 buildings.
- Full Google Login and Clan system.
- Season 1: "The Void Rises."

## 26.4 Live Ops
- **Season 2:** "Sea of Shadows" (Naval units focus).
- **Season 3:** "Titan Fall" (New giant mechs).


### 14.2.6 Loading Screen
- **Visuals:** High-resolution concept art of a battle between the Iron Hegemony and Sylvan Collective.
- **Center Bottom:** Progress bar (300px wide) with a "Void" energy filling effect.
- **Tips Text:** Randomly cycles through gameplay tips (e.g., "Press F1 to make your army follow you!").
- **Background:** Dynamic parallax effect on the concept art.

### 14.2.7 Profile Screen
- **Left Panel:** 3D model of the player's most used character class.
- **Right Panel:** Statistics (Kills, Wins, Territory Captured, Total XP).
- **Bottom:** Mastery Tree interface for spending Crown Points.
- **Exit:** Top-right 'X' button (1880, 40).

### 14.2.8 Settings Screen
- **Tabs:** General, Video, Audio, Controls.
- **Video:** Resolution, Fullscreen toggle, Bloom intensity, Particle quality.
- **Audio:** Master, Music, SFX, Ambient sliders.
- **Controls:** Keybinding grid for all 20+ actions.

### 14.2.9 Shop Screen
- **Left:** Categories (Skins, Emotes, Battle Pass).
- **Center:** 3x3 grid of featured items with Gem prices.
- **Right:** Preview window for selected cosmetic on a dummy model.

### 14.2.10 Leaderboards Screen
- **Columns:** Rank, Player Name, Clan, Crown Points.
- **Tabs:** Global, Regional, Clan-Only.
- **Bottom:** "Your Rank" highlight bar.
