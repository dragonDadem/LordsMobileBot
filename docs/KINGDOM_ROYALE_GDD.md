# KINGDOM ROYALE - OFFICIAL GAME DESIGN DOCUMENT (v1.0)

## SECTION 1 - GAME OVERVIEW

### Game Name
**KINGDOM ROYALE**

### Slogan
"Conquer. Survive. Rule. The Crown is Yours."

### Genre
Massively Multiplayer Online (MMO) / Battle Royale (BR) / Grand Strategy Hybrid.

### Sub Genres
- Top-down 2D Survival.
- Persistent Territory Conquest (OpenFront style).
- Tactical Hero-based Combat.
- Real-time Strategy (RTS) Base Building.

### Target Audience
- Hardcore strategy gamers who enjoy competitive territorial control.
- Fans of io-style survival games (Surviv.io, ZombsRoyale.io) seeking more depth.
- Competitive multiplayer enthusiasts looking for a mix of high-intensity combat and long-term progression.
- Mid-core players aged 16-35 who value skill-based gameplay and clan-driven social dynamics.

### Core Gameplay Loop
1.  **Drop & Scavenge:** Players enter a match or spawn in their territory, scavenging for weapons, armor, and raw materials.
2.  **Combat & Survival:** Engage in high-octane 2D top-down combat against players and NPCs while avoiding environmental hazards (The Storm).
3.  **Expansion:** Capture "Land Nodes" to expand territory, granting resource bonuses and defensive advantages.
4.  **Base Building:** Use gathered resources to construct and upgrade structures in controlled zones to produce units and research technology.
5.  **Domination:** Form Alliances/Clans to conquer the Capital City and hold it against the server to win the "Royale Crown".

### Unique Selling Points (USPs)
- **Persistent Territory in a BR Framework:** Unlike standard BRs where progress resets, territory control in Kingdom Royale persists across "World Seasons," while individual skirmishes provide immediate tactical feedback.
- **Dual Combat Layer:** Seamless transition between individual character combat (WASD + Mouse) and strategic army deployment (RTS-style).
- **Infinite Scaling Map:** Procedurally generated biomes that expand based on server population to ensure optimal player density.
- **Evolving Meta:** Dynamic resource scarcity and changing weather patterns (Biomes) force players to adapt their strategies daily.

### Competitive Advantages
- **Browser Accessibility:** Low barrier to entry; plays instantly in any modern browser without heavy downloads.
- **Hybrid Depth:** Combines the "instant fun" of .io games with the "long-term engagement" of grand strategy titles like Civilization or Lords Mobile.
- **Anti-Toxic Social Engine:** Built-in diplomacy tools and clan-based progression incentivize cooperation over pure griefing.

### Long Term Retention Strategy
- **Seasonal Leagues:** Monthly resets with cosmetic rewards based on territory held and rank achieved.
- **World Wonders:** Global events where factions must unite to defeat massive "World Bosses" or build "Legendary Structures".
- **Infinite Progression:** A deep Talent and Skill tree that requires months to master, with branching paths for specialization.
- **Social Ecosystem:** Robust clan features, including internal economies, roles, and shared resource pools.

### Vision Statement
"To create the definitive 2D browser-based multiplayer experience that bridges the gap between fast-paced survival action and deep, persistent territorial conquest, where every bullet fired and every wall built contributes to the legacy of a kingdom."

### Player Experience Goals
- **Adrenaline:** High-stakes combat where positioning and accuracy determine the victor.
- **Empowerment:** Seeing your small campsite grow into a sprawling fortress that dominates the map.
- **Community:** Feeling the camaraderie of a clan defending their borders against an invading force.
- **Intelligence:** Rewarding players who use strategy, diplomacy, and resource management rather than just twitch reflexes.

---

## SECTION 2 - FULL GAME STORY

### Lore: The Shattered Crown
In the year 1200 AR (After Ruin), the world of Aethelgard was a unified paradise under the Eternal Emperor. The discovery of "Aether-Iron," a mineral capable of powering both steam engines and magical artifacts, led to a golden age. However, the Emperor’s obsession with immortality led him to drill into the planet's core, releasing the "Void Mists."

The Mists shattered the continent of Pangaea into seven distinct biomes, each isolated by the "Storm of Chaos." The Emperor vanished, the Crown was lost, and the once-great Empire collapsed into warring city-states.

### World History: The Eras
1.  **The Age of Unity:** 1000 years of peace under the Eternal Emperor.
2.  **The Great Cataclysm:** The day the Mists rose. 90% of the population perished.
3.  **The Dark Interregnum:** 200 years of anarchy and scavenging.
4.  **The Kingdom Royale Era (Present):** New leaders (Players) emerge to reclaim the Aether-Iron and reunite the Crown.

### Continents & Regions
- **Oryxia:** The central hub, once the capital, now a scorched wasteland of ruins and riches.
- **The Frozen Veil:** A northern expanse of perpetual snow and ancient tech-tombs.
- **The Jade Wilds:** A dense, jungle-filled continent where nature has reclaimed the cities.
- **The Iron Sands:** A vast desert containing the world's largest Aether-Iron deposits.

### Factions
- **The Iron Vanguard:** Technocrats who believe in law, order, and heavy machinery.
- **The Verdant Covenant:** Mystics who want to purge the Aether-Iron and return to nature.
- **The Shadow Syndicate:** Mercenaries and outlaws who profit from the chaos.
- **The Remnant Order:** Loyalists to the old Emperor, seeking to restore the monarchy.

### Political Systems
Players operate in a **Feudal Meritocracy**. Every player starts as a "Wanderer." By capturing land, they become "Lords." Lords can swear fealty to "Kings" (Clan Leaders), who in turn compete for the title of "High Sovereign."

### Resources
- **Aether-Iron:** The primary fuel for advanced weaponry and building.
- **Lumen-Water:** Essential for survival and crop growth in the Mists.
- **Ancient Shards:** Remnants of the Emperor's crown, used for high-level research.

### Technology Level
**Arcane-Industrial Steampunk.**
Imagine WWI-era weaponry (rifles, tanks, biplanes) infused with glowing blue energy. Wood and stone are used for basic construction, while iron and oil power the late-game war machine.

### Why Players Fight
The "Great Storm" is closing in. Only the territory held by the High Sovereign's "Aether-Spires" can resist the Mists. To survive the eventual "Final Collapse," one must conquer the map and secure the Spires.

---

## SECTION 3 - MAP SYSTEM

### Total Size
The map is a grid of **100,000 x 100,000 pixels**, divided into 10,000 "Hex-Nodes". Each Hex-Node represents a capturable territory.

### Biomes

#### 1. The Scorched Plains (Scrubland)
- **Visual Style:** Cracked earth, dead grass, scattered ruins.
- **Color Palette:** Burnt Orange (#D35400), Dust Grey (#95A5A6), Pale Yellow (#F1C40F).
- **Resources:** Abundant Stone, Moderate Iron.
- **Enemies:** Scavenger Mutants, Wild Dogs.
- **Buildings:** Adobe-style structures, watchtowers.

#### 2. The Emerald Forest (Forest)
- **Visual Style:** Dense canopy, tall pines, overgrown stone pillars.
- **Color Palette:** Deep Green (#1E8449), Earth Brown (#6E2C00), Fern Green (#2ECC71).
- **Resources:** Abundant Wood, Abundant Food.
- **Enemies:** Timber Wolves, Rogue Druids.
- **Buildings:** Wooden Lodges, Tree-top platforms.

#### 3. The Glacial Highlands (Snow)
- **Visual Style:** Snowdrifts, ice lakes, jagged blue crystals.
- **Color Palette:** Ice Blue (#AED6F1), Pure White (#FBFCFC), Slate Grey (#2C3E50).
- **Resources:** Abundant Energy (from crystals), Abundant Water.
- **Enemies:** Frost Trolls, Mechanical Sentries.
- **Buildings:** Stone Fortresses, Heated Bunkers.

#### 4. The Crimson Desert (Desert)
- **Visual Style:** Massive dunes, sandstone canyons, Oasis spots.
- **Color Palette:** Blood Red (#943126), Desert Sand (#EDBB99), Gold (#D4AC0D).
- **Resources:** Abundant Oil, Abundant Gold.
- **Enemies:** Sand Worms, Desert Bandits.
- **Buildings:** Tent Cities, Sand-anchored oil rigs.

#### 5. The Abyssal Coast (Ocean/Islands)
- **Visual Style:** Tropical islands, shipwrecks, glowing coral.
- **Color Palette:** Deep Sea Blue (#1B4F72), Turquoise (#48C9B0), Sand (#F7DC6F).
- **Resources:** Abundant Naval Supplies, Rare Pearls.
- **Enemies:** Sea Serpents, Ghost Pirates.
- **Buildings:** Docks, Lighthouses, Floating Platforms.

### Special Zones
- **Villages:** Pre-existing NPC hubs where players can trade resources without being attacked (Neutral Zones).
- **Cities:** Strategic choke points that provide massive resource multipliers.
- **Castles:** High-tier fortifications that act as regional capitals.
- **Hidden Zones:** Caves or underground bunkers found under "Destructible Rocks," containing legendary loot.
- **Boss Zones:** Circular arenas located at the center of each biome, home to World Bosses.

---

## SECTION 4 - MATCH STRUCTURE

### Match Start (The Drop)
Players do not drop from a plane. Instead, they choose a "Spawn Sector" on the world map.
- If part of a clan: Spawn within clan territory.
- If solo: Spawn in "Neutral Borderlands."
Players arrive via **Steam-Pod**, which creates a small impact crater and provides 10 seconds of "Shielded Grace."

### Spawn System
- **Fresh Spawn:** Level 1, basic melee (Iron Dagger), 5x Bread.
- **Respawn (After Death):** Lose 50% of held inventory (unless stored in a bank). Respawn at the nearest controlled "Barracks" or "Hospital."

### Safe Zone & The Storm
The "Chaos Storm" is a persistent wall of purple energy that surrounds the map.
- **Dynamic Closing:** The Storm isn't just a circle. It flows like water, closing off biomes that have low player activity.
- **The Eye:** The only permanent safe zone is the "Great Capital" at the map's center.
- **Damage:** Storm damage ignores armor and scales based on how long the player stays inside.

### Territory Expansion
1.  **Exploration:** Move into an unclaimed Hex-Node.
2.  **Claiming:** Build a "Claim Stake" (requires 100 Wood, 50 Stone).
3.  **Fortification:** The node becomes "Contested" for 5 minutes. If no one destroys the Stake, the land is yours.
4.  **Integration:** Connect nodes back to your "Town Hall" to activate resource flow.

### Late Game & End Game
As the season progresses, the Storm pushes everyone toward the center.
- **The Siege of the Capital:** In the final week of a season, the Capital City’s shields drop.
- **Victory Condition:** The clan that holds the Capital Throne for 24 cumulative hours is declared the "High Sovereigns."
- **Rewards:** Unique skins, name on the "Hall of Kings," and resource boosts for the next season.

---

## SECTION 5 - CHARACTER SYSTEM

### Vital Stats
- **Health (HP):** 100 base. Regenerates slowly with food.
- **Armor (AP):** 0-200. Mitigates physical damage. Needs Repair Kits.
- **Hunger:** 0-100. At 0, HP starts dropping. Food refills this.
- **Stamina:** Used for sprinting and heavy attacks. Regenerates fast.
- **Experience (XP):** Earned through combat, building, and harvesting.

### Levels & Skills
Max Level: 100. Every level grants 1 **Talent Point**.
Talent Trees: **Combat**, **Engineering**, **Leadership**.

### Classes

#### 1. Soldier
- **Stats:** High HP, High Stamina.
- **Strengths:** Proficient with Assault Rifles and LMGs.
- **Weakness:** Low movement speed when armored.
- **Visual:** Heavy plate armor, tactical helmet.
- **Abilities:**
    - *Adrenaline Rush:* Increase move speed by 30% for 5s.
    - *Grenade Specialist:* Throws explosives further.

#### 2. Sniper
- **Stats:** Low HP, Very High Stamina.
- **Strengths:** Precision, stealth, long-range.
- **Weakness:** Terrible at close quarters.
- **Visual:** Ghillie suit, lightweight boots.
- **Abilities:**
    - *Eagle Eye:* Zoom out the camera by 20%.
    - *Camo-Crouch:* Become semi-transparent when standing still for 3s.

#### 3. Engineer
- **Stats:** Medium HP, High Resource Capacity.
- **Strengths:** Fast building, building repair, trap placement.
- **Weakness:** Reduced weapon accuracy.
- **Visual:** Tool belt, goggles, leather apron.
- **Abilities:**
    - *Quick-Fix:* Repair structures 50% faster.
    - *Sentry Turret:* Deploy a mini-turret that lasts 30s.

#### 4. Commander
- **Stats:** High HP, Bonus to Army Units.
- **Strengths:** Increases nearby allies' damage.
- **Weakness:** Large hit-box.
- **Visual:** Formal military cape, golden epaulettes.
- **Abilities:**
    - *Rallying Cry:* Heals allies for 20 HP in a radius.
    - *Tactical Map:* Reveal enemies on the mini-map for 10s.

#### 5. Scout
- **Stats:** Low HP, Max Movement Speed.
- **Strengths:** Evasion, looting speed.
- **Weakness:** Low damage output.
- **Visual:** Hooded cloak, light daggers on hip.
- **Abilities:**
    - *Dash:* Short-range teleport (blink).
    - *Loot Vision:* See high-tier loot through walls.

#### 6. Medic
- **Stats:** Medium HP, Fast Regen.
- **Strengths:** Healing others, reviving fallen allies.
- **Weakness:** Lowest combat stats.
- **Visual:** White coat with red accents, medical pack.
- **Abilities:**
    - *Heal Beam:* Channeled heal for a single target.
    - *Smoke Screen:* Drops a smoke grenade that heals everyone inside.

---

## SECTION 6 - COMBAT SYSTEM

### Core Mechanics
- **Perspective:** 2D Top-down (Birds-eye view).
- **Movement:** WASD.
- **Aiming:** Mouse cursor (Crosshair).
- **Firing:** Left Click.
- **Reloading:** 'R' key. Time varies by weapon.

### Damage Calculations
`Final Damage = (Base Damage * Critical Multiplier) - (Armor Value * Mitigation Factor)`
- Armor absorbs 70% of incoming damage until it breaks.

### Hit Detection
- **Projectile-Based:** Bullets are physical objects with travel time (except Snipers, which are hit-scan at short range, projectile at long).
- **Headshots:** 1.5x Damage. Detected by a smaller "hit-circle" within the player's collision box.
- **Critical Hits:** 5% base chance for 2.0x Damage. Can be buffed via Talents.

### Accuracy & Spread
- **Bloom:** Crosshair expands as you fire continuously.
- **Movement Penalty:** Accuracy drops by 40% while running.
- **Crouching:** Increases accuracy by 25%.

### Recoil System
- Weapons pull the cursor in specific patterns (e.g., AK-47 pulls up and right).
- Players must counter-pull with the mouse to stay on target.

---

## SECTION 7 - WEAPONS (COMPLETE LIST)

### Pistols (The Sidearms)
1.  **P-10 Peacemaker:** (Common) 15 Dmg, Med Range, 450 RPM, 12 Mag, 1.5s Reload. Standard issue reliable semi-auto.
2.  **Aether-Spark:** (Uncommon) 20 Dmg, Deals bonus energy dmg, 400 RPM, 10 Mag, 1.8s Reload. Infused with blue crystals.
3.  **Iron-Sight .45:** (Rare) 30 Dmg, High accuracy, 300 RPM, 8 Mag, 2.0s Reload. Heavy stopping power.
4.  **Shadow-Silenced P9:** (Epic) 18 Dmg, No tracer rounds, 500 RPM, 15 Mag, 1.2s Reload. Preferred by assassins.
5.  **The Emperor's Hand:** (Legendary) 50 Dmg, Explosive rounds, 200 RPM, 6 Mag, 2.5s Reload. Gold-plated antiquity.
6.  **Scrap-Shifter:** (Common) 12 Dmg, Jam chance 2%, 600 RPM, 20 Mag, 1.0s Reload. Made from recycled cans.
7.  **Lumen-Beam Pistol:** (Uncommon) 22 Dmg, Perfect accuracy, 350 RPM, 12 Mag, 2.0s Reload. Fires concentrated light.
8.  **Officer's Sidearm:** (Rare) 28 Dmg, +10% move speed when held, 400 RPM, 10 Mag, 1.5s Reload.
9.  **Venom-Spit:** (Epic) 15 Dmg + 5 Dps Poison, 450 RPM, 15 Mag, 1.8s Reload. Coated in swamp frog toxin.
10. **Aether-Overloader:** (Legendary) 35 Dmg, Fires 3-round bursts, 900 RPM Burst, 18 Mag, 2.2s Reload. Unstable energy.

### Revolvers (High Impact)
11. **Rusty Six-Shooter:** (Common) 40 Dmg, 150 RPM, 6 Mag, 3.5s Reload. Found in old barns.
12. **Canyon Magnum:** (Uncommon) 55 Dmg, 120 RPM, 6 Mag, 3.0s Reload. Loud and deadly.
13. **Steam-Cylinder:** (Rare) 60 Dmg, 180 RPM, 6 Mag, 2.0s Reload. Steam-assisted shell ejection.
14. **Bounty Hunter:** (Epic) 75 Dmg, 1.8x Headshot multi, 100 RPM, 5 Mag, 2.8s Reload. Long barrel for range.
15. **The Last Stand:** (Legendary) 100 Dmg, Last bullet deals 3x dmg, 80 RPM, 6 Mag, 4.0s Reload.
16. **Pocket Cannon:** (Common) 45 Dmg, Extreme recoil, 60 RPM, 2 Mag, 2.0s Reload. Basically a hand-held mortar.
17. **Aether-Revolver:** (Uncommon) 38 Dmg, Projectiles bounce once, 140 RPM, 6 Mag, 3.2s Reload.
18. **Judge & Jury:** (Rare) 50 Dmg, Kills instantly reload 1 bullet, 150 RPM, 6 Mag, 3.0s Reload.
19. **Obsidian Wheel:** (Epic) 65 Dmg, Bleed effect, 130 RPM, 6 Mag, 2.5s Reload. Carved from volcanic rock.
20. **Nebula Spin:** (Legendary) 45 Dmg, Every shot is a different element, 200 RPM, 8 Mag, 2.0s Reload.

### SMGs (Close Quarters)
21. **Scrap-Sub:** (Common) 10 Dmg, 900 RPM, 30 Mag, 2.5s Reload. High spread.
22. **Rat-a-Tat:** (Uncommon) 12 Dmg, 950 RPM, 40 Mag, 2.2s Reload. Reliable for suppression.
23. **Viper-9:** (Rare) 15 Dmg, 1000 RPM, 32 Mag, 1.8s Reload. High fire rate, low recoil.
24. **Aether-Flow SMG:** (Epic) 18 Dmg, No recoil, 850 RPM, 35 Mag, 2.0s Reload. Stabilized by magnetic fields.
25. **The Hive:** (Legendary) 22 Dmg, Fires 2 bullets per shot, 800 RPM, 50 Mag, 3.0s Reload.
26. **Mini-Shredder:** (Common) 9 Dmg, 1100 RPM, 25 Mag, 2.0s Reload. Shreds armor faster.
27. **Clockwork SMG:** (Uncommon) 14 Dmg, Accuracy increases while firing, 750 RPM, 30 Mag, 2.4s Reload.
28. **Blue-Streak:** (Rare) 16 Dmg, +5% speed while firing, 900 RPM, 36 Mag, 1.9s Reload.
29. **Ghost-Writer:** (Epic) 19 Dmg, Silent, 800 RPM, 30 Mag, 1.5s Reload. Zero muzzle flash.
30. **Absolute Zero:** (Legendary) 20 Dmg, Slows enemies by 20%, 850 RPM, 40 Mag, 2.2s Reload. Icy projectiles.

### Rifles (Semi-Auto/Lever Action)
31. **Old Bolt:** (Common) 45 Dmg, 60 RPM, 5 Mag, 3.0s Reload. Vintage wood stock.
32. **Frontier Lever:** (Uncommon) 55 Dmg, 90 RPM, 8 Mag, 0.8s per bullet Reload. Classic cowboy feel.
33. **Precision Carbine:** (Rare) 65 Dmg, 120 RPM, 10 Mag, 2.5s Reload. High muzzle velocity.
34. **Steam-Repeater:** (Epic) 75 Dmg, 150 RPM, 12 Mag, 2.0s Reload. Uses steam to cycle the bolt.
35. **The Marksman's Pride:** (Legendary) 95 Dmg, 100% accuracy while standing still, 70 RPM, 5 Mag, 3.5s Reload.
36. **Rust-Laden Longshot:** (Common) 42 Dmg, 50 RPM, 5 Mag, 4.0s Reload. High zoom.
37. **Aether-Infused Rifle:** (Uncommon) 50 Dmg, Rounds pierce 1 enemy, 80 RPM, 6 Mag, 3.2s Reload.
38. **Royal Guard Rifle:** (Rare) 60 Dmg, +15% dmg when in own territory, 100 RPM, 10 Mag, 2.8s Reload.
39. **Desert Vulture:** (Epic) 70 Dmg, Increased dmg to low HP targets, 110 RPM, 8 Mag, 2.6s Reload.
40. **God-Stalker:** (Legendary) 110 Dmg, Bullets travel instantly (hitscan), 40 RPM, 3 Mag, 5.0s Reload.

### Assault Rifles (Versatile)
41. **Standard Issue AR:** (Common) 25 Dmg, 600 RPM, 30 Mag, 2.5s Reload. Jack of all trades.
42. **Trench Rifle:** (Uncommon) 30 Dmg, 550 RPM, 25 Mag, 2.8s Reload. Better range.
43. **Steam-AR v2:** (Rare) 35 Dmg, Overheat mechanic (infinite ammo with cooldown), 700 RPM.
44. **Vanguard Elite:** (Epic) 42 Dmg, Integrated scope, 650 RPM, 30 Mag, 2.2s Reload.
45. **The Kingmaker:** (Legendary) 55 Dmg, Kills grant a temporary shield, 500 RPM, 40 Mag, 3.0s Reload.
46. **Militia Carbine:** (Common) 22 Dmg, 650 RPM, 35 Mag, 2.7s Reload. High recoil.
47. **Iron-Wolf AR:** (Uncommon) 28 Dmg, 600 RPM, 30 Mag, 2.4s Reload. Durable.
48. **Aether-Pulse AR:** (Rare) 33 Dmg, 3-round burst, 800 RPM Burst, 30 Mag, 2.0s Reload.
49. **Night-Ops AR:** (Epic) 38 Dmg, Suppressed, 700 RPM, 30 Mag, 1.8s Reload.
50. **Dragon's Breath:** (Legendary) 40 Dmg + Burn, 600 RPM, 30 Mag, 2.5s Reload. Fire tracers.
51. **Storm-Caller AR:** (Rare) 34 Dmg, Small chance to lightning strike target, 620 RPM, 30 Mag, 2.3s Reload.
52. **Heavy-Metal AR:** (Uncommon) 32 Dmg, Low fire rate but high impact, 450 RPM, 20 Mag, 3.0s Reload.
53. **Scavenger's AR:** (Common) 24 Dmg, Faster reload when magazine is empty, 600 RPM, 30 Mag, 2.0s Reload.
54. **Sovereign AR:** (Epic) 45 Dmg, Gold accents, 580 RPM, 32 Mag, 2.1s Reload.
55. **The Harbinger:** (Legendary) 50 Dmg, Targets are marked on mini-map for 5s, 600 RPM, 30 Mag, 2.2s Reload.

### LMGs (Suppression)
56. **Rusty Belt-Fed:** (Common) 20 Dmg, 700 RPM, 100 Mag, 6.0s Reload. Slow movement.
57. **Iron-Rain LMG:** (Uncommon) 24 Dmg, 750 RPM, 100 Mag, 5.5s Reload. High suppression value.
58. **Steam-Gatling:** (Rare) 28 Dmg, 900 RPM, 150 Mag, 7.0s Reload. Requires 1s spin-up time.
59. **Aether-Behemoth:** (Epic) 35 Dmg, 800 RPM, 120 Mag, 5.0s Reload. Energy-based cooling.
60. **The Wall-Breaker:** (Legendary) 45 Dmg, Deals 3x dmg to buildings, 600 RPM, 200 Mag, 8.0s Reload.
61. **Mercenary LMG:** (Common) 22 Dmg, 650 RPM, 80 Mag, 5.0s Reload.
62. **Bastion LMG:** (Uncommon) 26 Dmg, Accuracy increases the longer you fire, 700 RPM, 100 Mag, 5.8s Reload.
63. **Sentinel's Duty:** (Rare) 30 Dmg, Take 10% less dmg while firing, 600 RPM, 100 Mag, 5.2s Reload.
64. **Thunder-Bust LMG:** (Epic) 38 Dmg, Small AOE on impact, 550 RPM, 80 Mag, 6.5s Reload.
65. **Void-Eater LMG:** (Legendary) 40 Dmg, Heals player for 1% of dmg dealt, 750 RPM, 100 Mag, 6.0s Reload.

### Snipers (Long Range)
66. **Hunters Rifle:** (Common) 80 Dmg, 30 RPM, 1 Mag, 2.5s Reload. Basic scope.
67. **Eagle-Eye:** (Uncommon) 95 Dmg, 40 RPM, 5 Mag, 3.5s Reload. High zoom.
68. **Aether-Lance:** (Rare) 110 Dmg, 20 RPM, 1 Mag, 3.0s Reload. Pierces all enemies in line.
69. **Ghost-Stalker:** (Epic) 130 Dmg, 15 RPM, 5 Mag, 4.0s Reload. Bullet is invisible.
70. **The Widow-Maker:** (Legendary) 180 Dmg, 10 RPM, 5 Mag, 5.0s Reload. 1-shot headshot any tier armor.
71. **Telescope-Bolt:** (Common) 75 Dmg, 35 RPM, 5 Mag, 3.2s Reload.
72. **Mountain King:** (Uncommon) 100 Dmg, 25 RPM, 5 Mag, 3.8s Reload. No sway.
73. **Storm-Front Sniper:** (Rare) 115 Dmg, Slows target on hit, 30 RPM, 5 Mag, 3.5s Reload.
74. **Viper's Tongue:** (Epic) 120 Dmg + Poison, 25 RPM, 5 Mag, 3.0s Reload.
75. **The Final Silence:** (Legendary) 200 Dmg, Kills explode for AOE dmg, 5 RPM, 1 Mag, 6.0s Reload.

### Shotguns (Close Range)
76. **Rusty Pump:** (Common) 10x8 Dmg, 45 RPM, 5 Mag, 1.0s per shell. High spread.
77. **Double-Barrel:** (Uncommon) 15x10 Dmg, 200 RPM, 2 Mag, 2.5s Reload. Instant burst.
78. **Street-Sweeper:** (Rare) 12x8 Dmg, 300 RPM, 12 Mag, 4.0s Reload. Semi-auto.
79. **Aether-Shock:** (Epic) 18x10 Dmg, Stuns for 0.5s, 60 RPM, 6 Mag, 3.0s Reload.
80. **The Executioner:** (Legendary) 25x12 Dmg, 45 RPM, 8 Mag, 3.5s Reload. Ignores 50% armor.
81. **Farmer's Friend:** (Common) 12x6 Dmg, 50 RPM, 2 Mag, 2.0s Reload.
82. **Sawed-Off:** (Uncommon) 18x8 Dmg, 150 RPM, 2 Mag, 1.8s Reload. Fits in pistol slot.
83. **Trench Sweeper:** (Rare) 14x10 Dmg, 120 RPM, 6 Mag, 3.2s Reload.
84. **Slug-Thrower:** (Epic) 80 Dmg (Single Slug), 60 RPM, 5 Mag, 2.8s Reload. Long range shotgun.
85. **Dragon-Mouth:** (Legendary) 15x10 Dmg + Incendiary, 50 RPM, 8 Mag, 3.0s Reload. Fires a cone of fire.

### Explosives (AOE)
86. **Hand Grenade:** (Common) 100 AOE Dmg. 3s fuse.
87. **Sticky Bomb:** (Uncommon) 120 AOE Dmg. Sticks to players/walls.
88. **RPG-7 (Steam-Powered):** (Rare) 150 AOE Dmg. Direct fire.
89. **Aether-Grenade:** (Epic) 100 AOE Dmg + Mana Drain.
90. **The Big One:** (Legendary) 500 AOE Dmg. Massive radius.
91. **Smoke Bomb:** (Common) No Dmg. Blocks vision.
92. **Gas Grenade:** (Uncommon) 10 Dps for 10s.
93. **Flashbang:** (Rare) Blinds for 3s.
94. **Molotov Cocktail:** (Epic) Denies area with fire for 8s.
95. **Singularity Bomb:** (Legendary) Pulls enemies to center for 2s before exploding.

### Special Weapons
96. **Flamethrower:** 15 Dps, Continuous stream, 100 Fuel.
97. **Crossbow:** 60 Dmg, Silent, 1 Mag, 2.0s Reload.
98. **Aether-Staff:** 40 Dmg, Fires homing orbs, 10 Energy.
99. **Chainsaw:** 80 Dmg/s, Melee, 100 Fuel.
100. **Net Launcher:** No Dmg, Roots enemy for 2s.
101. **Tesla Gun:** 30 Dmg, Chains to 3 targets.
102. **Railgun:** 250 Dmg, Charges for 2s, Pierces walls.
103. **Healing Beam:** +20 HP/s to allies.
104. **Drone Controller:** Deploys a mini-drone with an SMG.
105. **The Crown Scepter:** (One per server) 300 Dmg, Kills grant 100% lifesteal.

---

## SECTION 8 - TERRITORY SYSTEM

### Capturing Land
- **Hex-Grid:** The world is divided into hexagons.
- **Influence:** Your "Influence Radius" grows based on the level of your Town Hall.
- **Capture Process:** Stand in a node -> Click "Claim" -> Defend the "Flag" for 120 seconds.

### Territory Levels
Nodes can be upgraded using Wood/Stone/Iron:
- **Level 1 (Outpost):** Provides basic vision.
- **Level 2 (Stronghold):** +10% Resource generation.
- **Level 3 (Fortress):** Enables "Warp-Gate" (fast travel).
- **Level 4 (Citadel):** +20% Defense to all units in range.

### Defense Bonuses
- Structures built on "Home Soil" (your territory) have 50% more HP.
- Players gain a "Patriot Buff" (+5% Damage) while defending their own Hex-Nodes.

### Resource Generation
Each Hex-Node has a "Natural Yield":
- **Forest Node:** 5 Wood / min.
- **Mountain Node:** 5 Iron / min.
- **Plains Node:** 5 Food / min.
Players must build "Collectors" on these nodes to harvest.

### Capital Cities
There are only 7 Capital Cities (one per biome).
- Holding a Capital allows the Clan to set "Taxes" on all players in that biome (1% of their gathered resources go to the Clan Bank).
- Capitals act as the only respawn points for high-tier army units.

---

## SECTION 9 - BUILDING SYSTEM (COMPLETE LIST)

### Core Building Mechanics
- **Grid Placement:** Buildings must be placed on a 1x1 to 5x5 grid within controlled territory.
- **Construction Worker:** Each player starts with 1 "Worker" unit. More can be hired at the Town Hall.
- **Decay:** Buildings lose 1% HP per day if not maintained with "Repair Kits".

### Key Buildings (Category: Governance & Social)
1.  **Town Hall (Levels 1-10):** The heart of your base.
    - *Cost:* 500 Wood, 500 Stone.
    - *Upgrade:* 1000 Wood, 1000 Stone (Level 2).
    - *Benefit:* Sets the global influence radius (500px at Level 1).
2.  **Tax Office:** Converts a percentage of local resource generation into Gold.
    - *Cost:* 300 Wood, 200 Stone.
    - *Benefit:* 5% Tax rate.
3.  **Embassy:** Increases Clan member limit and enables "Reinforce" speed boosts.
    - *Cost:* 800 Stone, 400 Iron.
4.  **Consulate:** Enables diplomatic treaties and resource gifting.
5.  **Town Square:** Increases regional population cap.
6.  **Monument of Heroes:** Increases nearby unit morale (+5% Dmg).
7.  **Hall of Records:** Provides detailed stats on regional resource flow.
8.  **Executioner's Block:** Decreases enemy unit morale when sieging.
9.  **Royal Palace:** Final upgrade for Town Hall (Level 10).
10. **Justice Hall:** Reduces "Corruption" decay in outer nodes.

### Key Buildings (Category: Military)
11. **Barracks (T1):** Trains basic Infantry and Archers.
    - *Cost:* 400 Wood.
12. **Veteran Barracks (T2):** Trains Elite Infantry.
13. **Imperial Barracks (T3):** Trains Royal Guards.
14. **Stables:** Trains Cavalry and scouting mounts.
15. **Great Foundry:** Produces Tanks and Mechs.
16. **Aerodrome:** Builds Biplanes and Aether-Blimps.
17. **Shipyard:** Only buildable on coastlines. Produces Naval units.
18. **Archery Range:** Specialized training for high-accuracy units.
19. **Academy:** Researches unit buffs (Damage, Speed, HP).
20. **Siege Workshop:** Builds Battering Rams and Catapults.
21. **Training Ground:** Passively gives XP to units stationed inside.
22. **Armorery:** Reduces unit recruitment cost by 10%.
23. **War Room:** Unlocks "Rally" attacks for clans.
24. **Mercenary Post:** Hires unique neutral units for Gold.
25. **Fletcher:** Increases Archer range by 5%.
26. **Blacksmith:** Increases Infantry damage by 5%.
27. **Stable Master:** Increases Cavalry speed by 10%.
28. **Tank Factory:** Dedicated T4 tank production.
29. **Aether-Lab (Military):** Equips units with energy weapons.
30. **Naval Academy:** Increases Ship speed and health.

### Key Buildings (Category: Economy & Harvesting)
31. **Sawmill:** +50% Wood production from the current node.
32. **Stone Quarry:** +50% Stone production.
33. **Iron Mine:** +50% Iron production.
34. **Oil Rig:** Essential for late-game fuel.
35. **Wind Farm:** Generates "Energy" for high-tech buildings.
36. **Granary:** Stores and protects Food from raids.
37. **Vault:** Protects a portion of Gold from being stolen during a siege.
38. **Marketplace:** Allows trading resources with other players.
39. **Lumberyard:** Increases Wood storage cap by 5000.
40. **Stone Depot:** Increases Stone storage cap by 5000.
41. **Iron Warehouse:** Increases Iron storage cap by 5000.
42. **Silo:** Increases Food storage cap by 10000.
43. **Oil Tanker:** Increases Oil storage cap by 2000.
44. **Battery Bank:** Stores Energy for night-time or storm use.
45. **Mint:** Passively generates 10 Gold / min.
46. **Fishery:** Harvests food from water tiles.
47. **Farmstead:** Harvests food from plains tiles.
48. **Vineyard:** Produces "Wine" (Luxury resource for morale).
49. **Trade Depot:** Increases resource trading speed.
50. **Aether-Siphon:** Generates "Gems" slowly (Premium currency).
51. **Scrap Yard:** Converts old weapons into Iron.
52. **Tool Shop:** Reduces construction time by 5%.
53. **Well:** Increases Lumen-Water production.
54. **Bakery:** Increases Food efficiency (+5% hunger satiation).
55. **Tannery:** Produces "Leather" for light armor.

### Key Buildings (Category: Defense & Fortification)
56. **Watch Tower:** Attacks enemies automatically within a 500px radius.
57. **Sniper Tower:** Long range, low fire rate defense.
58. **Aether-Wall (Wood):** 1000 HP.
59. **Aether-Wall (Stone):** 5000 HP.
60. **Aether-Wall (Iron):** 15000 HP.
61. **Aether-Wall (Reinforced):** 30000 HP.
62. **Heavy Gate:** Allows allies through while blocking enemies.
63. **Mortar Pit:** Long-range AOE defense.
64. **Tesla Coil:** High-frequency electrical defense against Mechs.
65. **Landmine Factory:** Produces hidden traps for the perimeter.
66. **Moat:** Slows down enemy ground units by 50%.
67. **Spike Trap:** Deals damage to units crossing it.
68. **Searchlight:** Reveals cloaked units (Snipers/Scouts).
69. **Guard Post:** Increases unit defense by 10% in its radius.
70. **Bunker:** Protects units from AOE and Aircraft damage.
71. **Anti-Air Battery:** Dedicated defense against Biplanes.
72. **Coastal Battery:** Dedicated defense against Ships.
73. **Boiling Oil Vat:** Defensive trap for gatehouses.
74. **Signal Fire:** Alerts clan members when an attack starts.
75. **Shield Generator:** Provides a 1000 HP shield to nearby buildings.

### Key Buildings (Category: Science, Utility & Wonders)
76. **Research Center:** The core of the tech tree.
77. **Hospital:** Increases heal rate and stores "Wounded" units.
78. **Weather Station:** Predicts where the Storm will move next.
79. **Radar Station:** Detects incoming large-scale army movements.
80. **Alchemy Lab:** Crafts potions and temporary combat buffs.
81. **Observatory:** Increases mini-map reveal radius.
82. **Library:** Reduces research time by 10%.
83. **Warp-Gate:** Enables fast travel between nodes.
84. **Radio Tower:** Enables global recruitment (buffs population).
85. **Aether-Forge:** Crafts legendary equipment.
86. **Sanctuary:** Increases character HP regen by 20%.
87. **Map Room:** Shows locations of nearby Bosses.
88. **Engineering Firm:** Unlocks T5 Mechs.
89. **Steam Plant:** Increases efficiency of all industrial buildings by 10%.
90. **Wonder: The Eternal Spire:** (End-game) Provides immunity to the Storm for the node.
91. **Wonder: The Great Library:** Unlocks secret T6 technologies.
92. **Wonder: The Golden Citadel:** Doubles Gold generation in the biome.
93. **Wonder: The Iron Wall:** Makes all walls in the biome indestructible for 1 hour/day.
94. **Wonder: The Aether Engine:** Generates massive Energy for the clan.
95. **Clocktower:** Synchronizes all clan unit movements (Buffs speed).
96. **Cathedral:** Increases unit morale and revival speed.
97. **Graveyard:** Allows recovering 5% of lost units.
98. **Trophy Hall:** Displays Boss trophies for server-wide buffs.
99. **The High Sovereign's Throne:** (One per server) Located in the Capital.
100. **Aether-Stabilizer:** Slows the Storm's progress in a 5km radius.
101. **Underground Vault:** Hides 100% of resources but has 10% storage capacity.
102. **Decoy Base:** Looks like a Town Hall but explodes when destroyed.

---

## SECTION 10 - RESOURCE SYSTEM

### The Eight Pillars
1.  **Gold:** The primary currency for trading and hiring units.
    - *Source:* Taxing nodes, killing Bosses, Selling loot.
2.  **Wood:** Basic construction material.
    - *Source:* Chopping trees, Sawmills.
3.  **Stone:** Foundational material for defenses.
    - *Source:* Mining rocks, Quarries.
4.  **Iron:** Used for weapons, armor, and advanced buildings.
    - *Source:* Iron veins, Mines.
5.  **Oil:** Fuel for tanks, aircraft, and high-tier factories.
    - *Source:* Desert/Ocean oil wells.
6.  **Food:** Sustains your character and army units.
    - *Source:* Hunting, Farms, Fishing.
7.  **Energy:** Required to power Aether-tech and Spires.
    - *Source:* Power Plants, Wind Farms, Crystal harvesting.
8.  **Gems:** Rare premium currency for cosmetics and instant-builds.
    - *Source:* Real-world purchase, Rare World Boss drops, Aether-Siphons.

### Economy Balance
- **Storage Caps:** Players must build "Storage" buildings to hold more than 10,000 of any resource.
- **Raid Logic:** In a successful base raid, 30% of the defender's *unprotected* resources are stolen.
- **Inflation Control:** High-tier research costs increase exponentially to ensure late-game players still have goals.

---

## SECTION 11 - ARMY SYSTEM

### Unit Tiers
Units are ranked Tier 1 (T1) to Tier 5 (T5). T5 units require Aether-Iron and Oil.

### Unit Classes
1.  **Infantry (The Grunts):**
    - *Type:* Swordsmen, Spear-wall, Grenadiers.
    - *Pros:* Cheap, fast to build.
    - *Cons:* Vulnerable to AOE and Cavalry.
2.  **Archers (The Range):**
    - *Type:* Longbowmen, Crossbowmen, Musketeers.
    - *Pros:* Can fire over walls.
    - *Cons:* Low HP, easily crushed in melee.
3.  **Cavalry (The Speed):**
    - *Type:* Light Horse, Heavy Knights, Steam-Bikes.
    - *Pros:* Incredible move speed, flanking bonus.
    - *Cons:* Useless in forest/mountain terrain.
4.  **Tanks (The Brutes):**
    - *Type:* Steam-Tank, Iron-Clad, Siege-Breaker.
    - *Pros:* Massive HP, destroys walls.
    - *Cons:* Very slow, expensive.
5.  **Mechs (The High-Tech):**
    - *Type:* Spider-Walker, Goliath, Aether-Suit.
    - *Pros:* Versatile, high DPS.
    - *Cons:* Drains "Energy" resources while deployed.
6.  **Aircraft (The Air):**
    - *Type:* Biplanes, Bombers, Aether-Eagles.
    - *Pros:* Ignores terrain, scouts vast areas.
    - *Cons:* Low armor, destroyed by Tesla Coils.
7.  **Naval (The Sea):**
    - *Type:* Gunboats, Ironclads, Carriers.
    - *Pros:* Controls the Abyssal Coast.
    - *Cons:* Restricted to water.

### Army Control
- **Battalion Logic:** Players don't control individual soldiers, but "Battalions" of 50-100 units.
- **Formation System:** Line, Square, Wedge, and Scattered. Each gives different stat buffs.

---

## SECTION 12 - AI SYSTEM

### Bot Behavior (NPCs)
- **Scavenger AI:** Roams the map looking for loot. If they see a player, they hide or attack if the player is low HP.
- **Guardian AI:** Protects Resource Nodes and Boss Arenas. They use cover and "flanking" logic.
- **Siege AI:** Periodically, "Void Hordes" will spawn from the Storm to attack player-controlled territories, forcing active defense.

### Difficulty Levels
- **Tier 1 (Feral):** Animals and basic mutants. Simple "charge" behavior.
- **Tier 2 (Bandit):** Uses basic weapons and heals when low.
- **Tier 3 (Elite):** Uses skills (dashes, grenades) and coordinates in teams of 3.
- **Tier 4 (Void-Touched):** High-speed, high-damage, requires group play.

### Pathfinding
- Uses A* Navigation Mesh.
- AI recognizes "Destructible Walls" and will target the weakest section of a base.

---

## SECTION 13 - BOSS SYSTEM (THE 50 LEGENDS)

### Biome: The Scorched Plains
1.  **The Storm-Gorgon:** A giant snake of leaves and lightning. Skills: Stun, Knockback. HP: 1M.
2.  **Scavenger King:** Leader of the mutant hordes. Skills: Summon Adds, Pipe-Bomb Barrage. HP: 800k.
3.  **Dust-Wraith:** A flickering ghost of the old empire. Skills: Teleport, Accuracy Debuff. HP: 600k.
4.  **Cactus-Goliath:** Massive sentient cactus. Skills: Spine Burst (AOE), Self-Heal. HP: 1.2M.
5.  **Vulture Queen:** Giant avian boss. Skills: Dive Bomb, Screech (Silence). HP: 900k.
6.  **Rust-Bucket Prime:** Oversized scrap mech. Skills: Flamethrower, Oil Leak. HP: 1.5M.
7.  **The Sand-Herald:** Messenger of the Void. Skills: Gravity Well, Aether-Beam. HP: 1.1M.
8.  **Bone-Cruncher:** Alpha mutated dog. Skills: Bleed Bite, Roar (Flee). HP: 700k.
9.  **Ruins Guardian:** Ancient stone golem. Skills: Ground Slam, Rock Throw. HP: 2M.
10. **The Mirage Master:** Creates clones of itself. Skills: Illusion, Backstab. HP: 500k.

### Biome: The Emerald Forest
11. **Timber-Titan:** Walking Redwood tree. Skills: Root Snare, Leaf Blade. HP: 2.5M.
12. **Spider Matriarch:** Queen of the web. Skills: Web Trap, Poison Spit. HP: 1M.
13. **Rogue Druid Elder:** Corrupted nature mage. Skills: Entangling Vines, Cyclone. HP: 900k.
14. **Mist-Stalker:** Invisible panther. Skills: Pounce, Camouflage. HP: 800k.
15. **The Hive-Mind:** Massive swarm of Aether-Bees. Skills: Stinging Rain, Confusion. HP: 1.3M.
16. **Moss-Covered Behemoth:** Huge sloth-like creature. Skills: Slow Aura, Heavy Strike. HP: 3M.
17. **Fairy-Queen of Thorns:** Cruel sprite. Skills: Thorn Shield, Charm. HP: 700k.
18. **The Emerald Dragon:** Young forest drake. Skills: Acid Breath, Tail Whip. HP: 4M.
19. **Wild-Hunt Commander:** Spectral rider. Skills: Charge, Spear Throw. HP: 1.2M.
20. **Root-Rot Crawler:** Giant centipede. Skills: Burrow, Acid Pool. HP: 1.1M.

### Biome: The Glacial Highlands
21. **The Frost-Lich:** Ghostly scientist. Skills: Blizzard, Ice Wall. HP: 800k.
22. **Mechanical Sentry 01:** Ancient robot. Skills: Laser Beam, Missile Swarm. HP: 2M.
23. **Yeti Alpha:** King of the peaks. Skills: Snowball Throw, Ice Breath. HP: 1.8M.
24. **Glacier-Cracker:** Giant ice worm. Skills: Submerge, Shard Rain. HP: 1.5M.
25. **Cryo-Phoenix:** Bird made of ice. Skills: Flash Freeze, Rebirth. HP: 1.2M.
26. **The Steam-Breaker:** Robot that melts ice. Skills: Steam Burst, Heat Wave. HP: 1.4M.
27. **Avalanche Elemental:** Sentient snowdrift. Skills: Bury, Cold Aura. HP: 2.2M.
28. **Polar-Bear Tyrant:** Armor-clad bear. Skills: Claw Swipe, Heavy Charge. HP: 1.6M.
29. **The Ice-Queen:** Corrupted survivor. Skills: Frozen Statue, Hailstorm. HP: 950k.
30. **Vault-Guardian Prime:** Protector of the tech-tombs. Skills: Shield Pulse, Shockwave. HP: 3.5M.

### Biome: The Crimson Desert
31. **Iron-Behemoth XL:** Malfunctioning mega-tank. Skills: Mortar, Oil Slick. HP: 2.5M.
32. **Sand-Worm Monarch:** Colossal burrower. Skills: Swallow, Sandstorm. HP: 5M.
33. **Bandit Warlord:** Leader of the Iron Sands outlaws. Skills: Dual-Wield, Grenade. HP: 1M.
34. **Scorpion-King:** Giant irradiated scorpion. Skills: Death Sting, Claw Crush. HP: 1.4M.
35. **The Sun-Priest:** Aether-Iron cultist. Skills: Solar Flare, Fire Wall. HP: 1.1M.
36. **Oasis-Phantom:** Water elemental. Skills: Drown, Wave Push. HP: 1.2M.
37. **Dune-Stalker:** Camouflaged reptilian. Skills: Tongue Lash, Venom Cloud. HP: 1.3M.
38. **The Brass-Colossus:** Huge brass robot. Skills: Steam Punch, Overheat. HP: 2.8M.
39. **Sphinx of the Void:** Riddling guardian. Skills: Mind Blast, Telekinesis. HP: 1.5M.
40. **Mummy-General:** Undead soldier. Skills: Cursed Wraps, Army Summon. HP: 1.2M.

### Biome: The Abyssal Coast
41. **Sea Serpent Leviathan:** Massive water snake. Skills: Whirlpool, Constrict. HP: 4M.
42. **Ghost-Captain Morgana:** Spectral pirate. Skills: Ghost Ship, Cannonball. HP: 1.5M.
43. **Crab-Titan Karkinos:** Huge armored crab. Skills: Bubble Shield, Pincer Snap. HP: 3M.
44. **The Kraken:** Multi-tentacled horror. Skills: Tentacle Slam, Ink Cloud. HP: 6M.
45. **Siren-Seductress:** Lures players into traps. Skills: Song (Charm), Water Bolt. HP: 1M.
46. **Deep-Sea Angler:** Lures players in the dark. Skills: Lure Flash (Blind), Bite. HP: 1.4M.
47. **Coral-Golem:** Living coral reef. Skills: Regeneration, Spiky Armor. HP: 2.4M.
48. **The Maelstrom Elemental:** Sentient hurricane. Skills: Tornado, Lightning. HP: 3.2M.
49. **Sunken Knight:** Drowned hero. Skills: Rusty Blade, Water Shield. HP: 1.6M.
50. **Triton the Betrayer:** Former king of the coast. Skills: Trident Throw, Summon Sharks. HP: 2.5M.

### Rewards
- **Boss Chest:** Contains 1 Guaranteed Legendary Weapon and 5,000 Gems.
- **Boss Trophy:** Can be placed in your base to give a 5% global buff to your clan.

### Spawn Conditions
- Bosses spawn every 6 hours in their respective arenas.
- A global notification sounds 10 minutes before spawn: "THE STORM-GORGON STIRS..."

---

## SECTION 14 - UI DESIGN (TECHNICAL SPECIFICATIONS)

*Target Resolution: 1920x1080 (Scaling for 16:9 and 21:9)*

### 1. Login Screen (Layout)
- **Background:** Panoramic WebGL shader at Z-index 0.
- **Logo:** (x: 960, y: 300), Size: 800x400px. Animated glow effect.
- **Google Login Button:** (x: 960, y: 700), Size: 300x60px. CSS: `background: #4285F4; border-radius: 4px;`.
- **Guest Mode Link:** (x: 960, y: 780), Text-align: center, Font: 14px 'Inter'.
- **Version Label:** (x: 1880, y: 1060), Text: "v1.0.4-beta".

### 2. Main Menu (The Hub)
- **Player Stats Header:** (x: 20, y: 20), Container: 400x100px. Includes Avatar (80x80), Name, and Level bar.
- **Currency Cluster:** (x: 1500, y: 20), Horizontal layout: Gold icon + value, Gem icon + value.
- **Start Battle Button:** (x: 1600, y: 850), Size: 280x120px. Color: #E74C3C. Hover: 1.1x Scale.
- **Training Room Button:** (x: 1600, y: 980), Size: 280x60px. Color: #7F8C8D.
- **Navigation Dock:** (x: 960, y: 1000), Anchor: Bottom-Center. Icons (64x64) for:
    - Inventory (Hotkey: I)
    - Shop (Hotkey: P)
    - Clan (Hotkey: G)
    - Leaderboards (Hotkey: L)
    - Settings (Hotkey: ESC)

### 3. Battle Screen (HUD)
- **Mini-map:** (x: 1750, y: 150), Size: 250px diameter. Features: Player pointer, Storm border, Waypoints.
- **Health/Armor Bar:** (x: 960, y: 950), Size: 600x40px total.
    - Top Layer (20px): HP (Red).
    - Bottom Layer (20px): Armor (Blue).
- **Stamina/Hunger Rings:** (x: 640, y: 950), Circular gauges surrounding the character in world-space (toggleable) or static icons.
- **Hotbar:** (x: 960, y: 1020), 5 Slots (80x80px each). Keybindings 1-5 displayed in corner.
- **Ammo Counter:** (x: 1280, y: 950), Text: "30 / 120". Includes reload progress radial.
- **Kill Feed:** (x: 1880, y: 300), Top-right aligned. Format: `[PlayerA] [WeaponIcon] [PlayerB]`.
- **Chat Window:** (x: 20, y: 800), Size: 400x200px. Fades out after 5s of inactivity.

### 4. Inventory & Crafting Screen
- **Character Paperdoll:** (x: 400, y: 540), 3D Render of current character model.
- **Equipment Slots:** Surrounding Paperdoll (Head, Chest, Back, Hands, Feet).
- **Grid View:** (x: 1100, y: 540), 10x6 Grid (Size: 800x600px). Right-click for context menu.
- **Crafting Tab:** Right side sidebar (300px width). List of learnable blueprints.
- **Resource Bar:** Bottom of window, showing totals for Wood, Stone, Iron, Oil.

### 5. Clan Command Center
- **Territory Map:** (x: 600, y: 500), Interactive hex-grid showing clan borders.
- **Member List:** (x: 1500, y: 500), Scrollable list with [Invite], [Kick], [Promote] buttons.
- **Tax Slider:** (x: 1500, y: 900), Range 0-10% for Clan Leaders.

---

## SECTION 15 - GOOGLE LOGIN & ACCOUNT SYSTEM

### Flow
1.  **First Time:** Click Google Login -> Choose Account -> System creates a Unique Player ID (UPID) -> "Welcome Wanderer" tutorial starts.
2.  **Account Linking:** Players can link their Steam or Discord accounts to the same UPID for cross-platform play.
3.  **Guest Mode:** Allows playing without login, but progress is stored in "Local Storage" and lost if cache is cleared.
4.  **Cloud Save:** Every 30 seconds, the client sends a "State Sync" to the backend (Player Pos, Inventory, XP).

---

## SECTION 16 - CLAN SYSTEM

### Guilds & Alliances
- **Creation:** Costs 5,000 Gold.
- **Roles:** Leader, General, Officer, Soldier, Recruit.
- **Diplomacy:** Set other clans as [ALLY], [NEUTRAL], or [WAR].
- **Shared Territory:** All clan members can build on and defend the clan's Hex-Nodes.

### Clan Wars
- Triggered when a Clan Leader "Declares Siege" on another clan's Capital.
- A 24-hour countdown starts to allow both sides to prepare.

---

## SECTION 17 - CHAT SYSTEM

### Channels
- **[Global]:** Entire server. (10s slow-mode to prevent spam).
- **[Clan]:** Private to your guild.
- **[Team]:** For your current 4-man squad.
- **[Whisper]:** Private 1-on-1 messages.

### Moderation
- **Filter:** Real-time regex filter for slurs and toxic language.
- **Reporting:** Right-click player name -> [Report for Cheating/Toxicity].
- **Auto-Ban:** Reaching 10 reports in 1 hour triggers a temporary 24h mute for manual review.


---

## SECTION 18 - ANTI CHEAT ARCHITECTURE

### Layer 1: Client-Side Sanity Checks
- **Input Validation:** Reject movement packets that exceed the maximum "Speed Stat" + 5% buffer.
- **Weapon Cooldowns:** Weapon fire rates are hard-coded; the server rejects firing packets faster than the weapon's RPM.

### Layer 2: Server-Side Authority
- **Prediction & Reconciliation:** The server simulates all movement. If a player’s reported position deviates too far from the simulation, they are "rubber-banded" back.
- **Visibility Checks (Anti-ESP):** The server only sends entity data (players, items) if they are within the player's FOV + a small margin.

### Layer 3: Heuristic Detection (Big Data)
- **Aimbot Detection:** Track "Angular Velocity" and "Snap-to-Target" patterns. Humans have natural micro-tremors; bots move in perfect vectors.
- **Economic Anomalies:** Flags accounts that gather resources 10x faster than the theoretical maximum.

### Layer 4: Bans & Enforcement
- **Shadow Bans:** Cheaters are put in "Hacker-Only" servers without being told.
- **Hardware ID (HWID) Ban:** Uses browser fingerprinting and IP tracking to prevent multi-account ban evasion.

---

## SECTION 19 - BACKEND & NETWORKING

### Architecture
- **Frontend:** React + PixiJS (High-performance 2D WebGL rendering).
- **Backend:** Node.js (Microservices) for logic, Go (gRPC) for high-speed combat calculations.
- **Database:**
    - **Redis:** For real-time position data and match state.
    - **PostgreSQL:** For persistent player data (Levels, Inventory, Clan info).
    - **MongoDB:** For historical logs and chat archives.

### Matchmaking & Scaling
- **Region-Based:** Servers in US-East, EU-West, and Asia-Tokyo.
- **Dynamic Instances:** When a biome hits 200 players, a "Parallel Shard" is created, connected via "World Portals."

### Load Balancing
- Uses NGINX to distribute traffic across a Kubernetes (K8s) cluster.
- **Auto-Scaling:** Spin up new pods during peak hours (e.g., Friday nights).

---

## SECTION 20 - PROGRESSION SYSTEM

### XP & Levels
- **Combat XP:** Killing players (500 XP), killing NPCs (50 XP).
- **Industrial XP:** Building (10 XP / node), Harvesting (1 XP / resource).
- **Diplomatic XP:** Clan contributions, completing "Trade Missions."

### Seasonal Ranks
1.  **Bronze (I-V)**
2.  **Silver (I-V)**
3.  **Gold (I-V)**
4.  **Diamond (I-III)**
5.  **Grand Sovereign (Top 500 Players)**

### Daily/Weekly Missions
- *Daily:* "Harvest 1,000 Wood", "Travel 5,000 meters."
- *Weekly:* "Capture 5 Enemy Nodes", "Participate in a Boss Takedown."

---

## SECTION 21 - COSMETICS & CUSTOMIZATION

### Categories
- **Skins:** Full-body character outfits (e.g., "Neon Ninja", "Steampunk Admiral").
- **Weapon Wraps:** Glowing textures for rifles and melee weapons.
- **Emotes:** Animated actions (Dance, Wave, Taunt).
- **Pets:** Small mechanical or animal companions that follow you (Non-combat).
- **Kill Effects:** Visual explosions or icons that appear when you eliminate an enemy.

### Rarity Scale
- **Common (White):** Basic color swaps.
- **Uncommon (Green):** Minor model changes.
- **Rare (Blue):** Animated textures.
- **Epic (Purple):** Custom sound effects and VO.
- **Legendary (Gold):** Unique particle effects and UI icons.

---

## SECTION 22 - SOUND DESIGN

### Music
- **Main Menu:** Orchestral theme with heavy industrial percussion.
- **Exploration:** Low-fi, ambient tracks that change based on the biome (e.g., Wind chimes in Snow, Didgeridoos in Desert).
- **Combat:** Fast-paced, high-bpm electronic/rock hybrid that kicks in when HP drops or enemies are nearby.

### Sound Effects (SFX)
- **Combat:** Distinct "Clink" for headshots. Muffled sounds when health is below 20%.
- **Environmental:** Crunching leaves in forests, howling wind in mountains.
- **UI:** Mechanical "Click" sounds for buttons, echoing "Level Up" fanfares.

---

## SECTION 23 - TECHNICAL ART DIRECTION

### Character Proportions
- **Style:** Stylized Realism (resembling "Arcane" or "Team Fortress 2").
- **Body:** Slightly elongated limbs for better 2D visibility.
- **Heads:** 10% larger than realistic to emphasize facial expressions and hats.

### Visual Effects (VFX)
- **Aether-Flow:** Everything powered by Aether has a signature blue-cyan trail (#00FFFF).
- **The Storm:** A mix of purple lightning and dark smoke particles.
- **Bullet Tracers:** Subtle yellow streaks for physical rounds, blue for Aether rounds.

### Color Palettes (Environment)
- **Forest:** #1B5E20 (Base), #C8E6C9 (Highlight).
- **Wasteland:** #4E342E (Base), #D7CCC8 (Highlight).
- **Tech:** #212121 (Metal), #00B0FF (Neon).

---

## SECTION 24 - GAME BALANCE FORMULAS

### Damage Scaling
`Damage = Base_Dmg * (1 + Level/100) * Crit_Multiplier`

### Progression Curve (XP for Level N)
`XP_Required = 500 * (1.15^N)`
- This ensures that reaching Level 100 takes roughly 300 hours of active play.

### Economy Pacing
- **Gathering Rate:** 1.5x during the first 10 minutes of a session to encourage fast starts.
- **Building HP Scaling:** Walls gain 2% HP per level of the player who built them.

---

## SECTION 25 - MONETIZATION (ETHICAL & SUSTAINABLE)

### No Pay-to-Win (P2W)
- No items that grant damage, health, or speed can be purchased with Gems.
- Resources cannot be bought; they must be gathered.

### Revenue Streams
1.  **Battle Pass (Premium):** $9.99 per season. Grants 100 tiers of cosmetics.
2.  **Daily Shop:** Rotating selection of 5 skins and 2 emotes.
3.  **Clan Sponsorships:** Large clans can pay for custom "Clan Logos" and "Flags" (Purely cosmetic).
4.  **Premium Currency (Gems):** Used for the above.

---

## SECTION 26 - ROADMAP

### Phase 1: Alpha (Months 1-4)
- **Focus:** Core movement, basic combat, and 2 biomes.
- **Goal:** Stress-test the 2D physics engine with 100 players.

### Phase 2: Beta (Months 5-8)
- **Focus:** Territory system, clan features, and building.
- **Goal:** Balance the resource economy and AI difficulty.

### Phase 3: Early Access (Months 9-12)
- **Focus:** All 5 biomes, 100+ weapons, and 50 bosses.
- **Goal:** Global player acquisition and monetization testing.

### Phase 4: Full Launch (Month 14)
- **Focus:** Season 1 "Rise of the Sovereign."
- **Goal:** eSports tournament and Cross-platform (Mobile/Web) parity.

### Future Seasons
- **Season 2:** "The Deep Sea" (Naval focused).
- **Season 3:** "Sky Citadels" (Aerial focused).

---
**END OF DOCUMENT**
