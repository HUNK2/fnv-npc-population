# Shared brief for the research and brainstorm agents (2026-11-26)

Read this whole file first. It is everything we know so far. You are one of several agents, each with one angle.

## The mod in one paragraph

A Fallout: New Vegas (PC, 1.4.0.525) mod. The big idea is a more lived-in Mojave: towns with real residents who
have jobs, routines and react to the player. Inside that, the part we are designing now: **the player founds and runs
a travelling merchant (caravan) company**. You hire managers and traders, run routes between towns, build
warehouses and workshops, and grow the company against the Crimson Caravan. It is meant to feel like running a
real company (profit and loss, revenue, warehouses, managers), but it must also be a fun game, not a spreadsheet.

## What the user asked for (their words, lightly cleaned)

- "I want to focus on the actual business part for the moment. Want it to have a lose condition with real
  progression that reinforces the player's perception that their business is growing, while also making the
  business engaging. Don't be afraid to look at other games/projects."
- On routes: "You know Transport Fever 2 where there is crafting, like clay = rock + sand." (production chains)
- Tonight: "Do not be afraid to try new gameplay approaches."

## Decided by the user (treat as fixed)

1. The company is run like a real company: P&L, revenue, warehouses, managers. You hire managers and traders.
2. The company is managed **entirely in a terminal** (no dialogue menus, no custom UI menu). FNV terminals only
   take menu choices (no typed text input). Notes, submenus and body text are available.
3. The **Crimson Caravan** (Alice McLafferty, New Vegas) is the business rival.
4. The **NCR** is the government.
5. There is a **dodgy side**: smuggling, risky; the NCR can raid your office.
6. It is a public release (Nexus), so it must work for many players and load orders.
7. Lived-in towns part (related, same mod family): role-based reactions (few defenders fight, the rest flee),
   placed NPCs (no runtime spawner), mod rules apply only to mod-tagged townsfolk, vanilla named NPCs untouched,
   Goodsprings is the first test town.

## Proposed by Claude, not yet answered by the user (you may challenge these)

- Startup loan from Alice McLafferty (Crimson Caravan). In vanilla she bought out Cass's family caravan company
  after its caravans were destroyed, so a loan from her has teeth.
- Failure ladder: missed payment -> warning + late fee -> an asset seized -> takeover (your office becomes a
  Crimson Caravan branch). After the loan is paid off the same ladder runs on wages, rent and tax.
- Second way to lose: NCR shutdown on the dodgy path (heat -> tip-offs -> raid -> licence revoked).
- Everything else costs assets (a caravan, cargo, a warehouse), not the company.
- Company cash is separate from the player's own caps (taking dividends is a real choice).
- Five tiers: Peddler, Outfit, Caravan company, Trading house, Mojave concern. Each gated on money + town trust + a
  deed, each unlocking one new thing, each visible in the world (signs, wagons, staff, buildings).
- Main growth number: market share per town against the Crimson Caravan.
- Time: timescale 30, so a game day is 48 real minutes and a week about 5.6 real hours. A morning report each game
  day with 1-3 decisions ("memos"); bills weekly.
- Vanilla quest state moves demand and danger (Primm with no sheriff, Powder Gangers, Quarry Junction deathclaws).
- The Crimson Caravan moves in on routes that get profitable (so old income does not go stale).
- No forced pickup trips (a top complaint about GTA Online businesses).
- Money is ledger math once per game day; caravans walk for real only when the player is nearby; road events can
  be played for real if the player is there, otherwise resolved on paper (guards vs danger).
- The player's adventuring feeds the company: escort runs, clearing route threats, closing contracts in person.
- Production chains (Transport Fever 2 style), using real FNV recipes where possible:
  - Water: Goodsprings spring -> purifier -> purified water.
  - Building materials (new cargo): Sloan quarry stone (after Quarry Junction deathclaws are dealt with) -> stone
    yard -> materials that physically grow the towns you supply.
  - Food: brahmin + crops -> smokehouse in Primm.
  - Medicine: broc flower + xander root -> healing powder; + surgical syringe and a Science 70 hire -> stimpaks.
  - Ammo: lead (scrap metal -> 200 lead), powder (NCR imports or Powder Gangers contraband), cases, primers ->
    reloading bench in Primm.
  - Workshops are buildings that level up with throughput; recipe skill levels make staff skills matter.
- First version = HQ (Goodsprings) + Primm, Sloan, Mojave Outpost. Later: more of the Mojave.
- Open questions: after losing the company, start over smaller (Claude's pick) or gone for good; goods = FNV items
  plus new building cargo (Claude's pick) vs FNV items only vs all new; one mod vs a towns core + company add-on.

## Hard constraints

- Engine: Gamebryo, FNV 1.4.0.525. Requirements we accept: xNVSE and JohnnyGuitar NVSE (JIP LN NVSE likely fine
  too). JohnnyGuitar NVSE can add, rename and remove terminal menu items, set their notes/submenus and refresh the
  terminal menu from script. `ComputersMenu::DisplayTerminal` (0x007586E0) could be hooked for live numbers in body
  text (untested).
- FNV AI: the game only fully simulates actors near the player; AI updates are capped (about 20 complex actors near
  the player). Unloaded actors move "virtually". So most of the company must be simulated as numbers, not NPCs.
- Must work on existing saves and keep vanilla quests intact (Cass's quest "Heartache by the Number" involves the
  Crimson Caravan; do not break it).
- The player spends most of their time questing elsewhere. The business must not punish time away, and must not
  need babysitting, but must still give decisions worth making.
- No new game required. No dependency on other big mods.

## Research already done (read it, do not repeat it)

- `C:\DecompModGithub\fnv-npc-population\research\BUSINESS-RESEARCH.md`: lose conditions in other games (Recettear,
  OpenTTD, Railroad Tycoon, Capitalism Lab, Offworld, Bannerlord, Papers Please, Frostpunk, Sunless Sea, GTA Online),
  progression (GTA Online, RDO Trader, Bannerlord, Sim Settlements 2, Kenshi, Recettear, Moonlighter, Stardew, Two
  Point, Big Ambitions, Patrician, Offworld, idle design), existing Bethesda business mods (none does a player-run
  company), Transport Fever 2 chains, FNV's own recipes.
- `C:\DecompModGithub\fnv-npc-population\design\caravan-company.html`: the current design board (HTML).
- `C:\DecompModGithub\fnv-npc-population\research\README.md`: catalogue of FNV engine NPC functions (only for
  technical questions).

## Rules for every agent

- Write your report to the file path given in your task, in Markdown. Return only a short summary (under 200 words)
  as your final message.
- Ground claims. For anything from another game or project, give the source URL you actually opened, and tag
  [D] = documented by the source (manual, wiki, developer) or [O] = player or reviewer opinion. Search snippets
  alone are weak: open pages where you can. If a site refuses, move on.
- Be concrete: numbers, formulas, named places, named NPCs, example screens, example decisions. Vague advice
  ("make it engaging") is useless to us.
- Be bold. New gameplay approaches are welcome. But for each idea say how it plays, why it is fun, how it fits FNV
  and the terminal, and roughly how hard it is to build.
- Do not launch the game, do not change any game files, saves or plugins, do not edit files other than your own
  report. FNV MCP tools (mcp__fnv__*) may be used **read-only** (fnv_record, fnv_command_info, fnv_guide, fnv_func,
  fnv_setting_info and similar lookups). Never call a tool that changes the game.
- Do not spawn other agents.
- Report layout:
  1. Key findings (with sources and [D]/[O] tags)
  2. What this means for our mod: concrete proposals (with numbers where you can)
  3. Bold ideas (new gameplay approaches)
  4. Pitfalls and design flaws to avoid (including any you see in the current proposals)
  5. Questions only the user can answer (if any)
- Aim for 1,500 to 3,000 words. Dense beats long.
