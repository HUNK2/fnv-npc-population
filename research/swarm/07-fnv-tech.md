# 07 - Technical feasibility inside FNV (terminal company, daily tick, world refs)

Agent angle: how would the caravan company actually run in FNV 1.4.0.525, and what is proven vs documented vs needs a live test.

## 0. Evidence rules for this report

Tags: **[S]** = I opened the source code (GitHub raw files, quoted below) or the decomp. **[D]** = documented on a page I could read. **[M]** = engine map / MCP lookup (read-only). **[W]** = web search snippet only, page not opened. **[?]** = my inference, needs a live test.

Access problem: geckwiki.com, geck.uesp.net and forums.nexusmods.com answer every automated request with a Cloudflare 403 (checked with WebFetch and curl). So I could NOT open any GECK wiki page. Everything I say about vanilla scripting behaviour that is not in the source files is tagged [W] or [?]. All JohnnyGuitar and xNVSE facts below are from the real source files:

- JG terminal functions: `https://raw.githubusercontent.com/carxt/JohnnyGuitarNVSE/dev/JG/functions/fn_terminal.cpp` and `.h`, struct layout in `JG/internal/Game/Bethesda/BGSTerminal.hpp` [S]
- JIP LN: `https://github.com/jazzisparis/JIP-LN-NVSE` (`functions_jip/jip_fn_ui.h`, `jip_fn_script.h`, `functions_ln/ln_fn_terminal.h`) [S]
- xNVSE: `https://github.com/xNVSE/NVSE` (`nvse/nvse/EventManager.cpp`, `ArrayVar.cpp`, `GameUI.h`) [S]
- Decomp: `C:\DecompModGithub\fnv_decomp\src\fallout_shared\tesdescription.cpp`, `src\fallout\interface\menus\computersmenu.cpp` [S]

Important: the terminal functions you named in the brief are real, but they are **JohnnyGuitar NVSE** (JG), not JIP. The FNV MCP command table only knows JIP LN and xNVSE, so `fnv_command_info AddTerminalMenuItem` returns "not found". That is not evidence that the function is missing.

## 1. Key findings

### 1.1 Terminals

**JG terminal function list, exact (from `fn_terminal.h`) [S]**

| Function | Parameters | Returns |
|---|---|---|
| `AddTerminalMenuItem` | terminal form | 1 if added |
| `RemoveTerminalMenuItem` | terminal, index | 1 if removed |
| `GetTerminalMenuItemCount` | terminal | count |
| `GetTerminalMenuItemText` | terminal, textType (1=entry/button, 2=result), index | string |
| `SetTerminalMenuItemText` | terminal, textType (1 or 2), index, string | 1 if set |
| `GetTerminalMenuItemNote` / `SetTerminalMenuItemNote` | terminal, index [, note form] | note form |
| `GetTerminalMenuItemSubmenu` / `SetTerminalMenuItemSubmenu` | terminal, index [, terminal form] | terminal form |
| `GetTerminalMenuItemFlags` / `SetTerminalMenuItemFlags` | terminal, index [, flags int] | flags byte |
| `RefreshTerminalMenu` (alias `rtm`) | none | 1 if the computers menu is open |

What the code shows:

- `RefreshTerminalMenu` calls `ComputersMenu::GetSingleton()->DisplayTerminal(false)`. That is the function at 0x007586E0 [M]. So we do not need our own hook for a menu redraw: JG already calls it. `DisplayTerminal(false)` clears the list box, re-reads the description, and for each menu item re-evaluates the item's condition and rebuilds the "> text" line (decomp, `computersmenu.cpp:1656`) [S]. Result: items can appear, vanish and change their label while the terminal is open.
- **Strings are limited to 259 characters per call.** `SetTerminalMenuItemText` reads the string into `char cText[MAX_PATH]` (260) [S]. One result text or one button label per call, so about 259 characters each.
- **`AddTerminalMenuItem` makes a blank item.** It allocates a `TERMINAL_MENU_ITEM` (size 0x78) with empty text, empty result script, empty condition list [S]. JG has no function to give an added item a result script or conditions. An added item can only: show text, link a note, link a submenu terminal. So added items cannot "do" anything.
- **Therefore actions must be pre-authored items.** Result scripts (set a quest variable) and conditions (show/hide by a global or quest variable) are normal TERM fields written in the plugin. Pattern: a pool of "slot" items in the ESP, each with result script `set CCQuest.pick to N` and condition `CCQuest.slotN_visible == 1` (conditions on TERM menu items are vanilla; `TERMINAL_MENU_ITEM` has a `kConditions` member [S]). Text of each slot is overwritten by script with `SetTerminalMenuItemText`.
- **Navigation without scripts works with added or pooled items**: `SetTerminalMenuItemSubmenu` links an item to another TERM form [S]. A "screen" is a TERM form; a menu button opens another TERM. The vanilla terminal keeps a "recent" list and `DisplayPreviousTerminal` (0x00758A80) for Back [M, S].
- **Body text (the TERM `DESC` welcome text) cannot be changed from script.** `TESDescription::GetDescription` (0x00482E90) is a lazy read: if the data handler is not holding descriptions in memory it calls `TESFile::ReadTESInfo(form, chunk)`, i.e. it re-reads the text from the plugin file on demand [S, decomp `tesdescription.cpp:23`]. There is no BSString we can overwrite, and no JG/JIP setter in either source tree (grep of both function lists: only `SetPasswordNote` for terminals in JIP `ln_fn_terminal.h`) [S]. Menu item text, by contrast, is a live `BSString` (`strEntryText`, `strResultText`) [S].
- **No %-token substitution is documented for FNV terminal text.** I found no code path for substitution in DisplayTerminal (it calls `pDescription` straight into `AddLine`) [S], and the search hits about "text replacement tokens in terminals" are forum threads I could not open and are probably Fallout 4 / Skyrim `<Global=>` features [W]. Treat live numbers as "write the number into the menu text yourself" (below), and test whether `%` or `<Global=...>` do anything in FNV (live test 3).
- **Flags on an item** (`ucFlags`, bit 0 = add note, bit 1 = force redraw, bit 2 = selected) [S].
- **Menu IDs.** In xNVSE `GameUI.h` the enum gives Barter = 0x41D (1053), Surgery 1054, Hacking 1055, VATS 1056, **Computers = 1057** (0x429), SleepWait = 0x3F4 (1012) [S]. A GECK MenuMode page snippet agrees: 1055 Hacking, 1057 Computers [W]. (My first search snippet quoting "1055 for terminals" was wrong; the source says 1057.)
- **Menu events.** JIP gives `SetOnMenuOpenEventHandler script menuID [flags]` and `SetOnMenuCloseEventHandler`, plus `SetOnMenuClickEventHandler` [S, `jip_fn_ui.h:33-35`]. `GetMenuTargetRef 1057` returns the terminal reference that is open (`ComputersMenu::targetRef`) [S, `jip_fn_ui.h:272`]. So one TERM form can serve many offices and the handler learns which ref was used.
- **Typed text input does exist** (`ShowTextInputMenu`, `SetTextInputString` in JIP) [S]. The brief says "FNV terminals only take menu choices": true for terminals, but the company could use a text box for naming things (company name, route nickname) if we want. Optional.
- **Alternate terminal screen model** via JIP `SetTerminalUIModel terminal "path.nif"` [S]. Cosmetic only.

**Vanilla TERM record limits.** I could not read the GECK wiki, so I have no documented numbers for max menu items, max text length, or max body length. What I have from the real data: a vanilla terminal record (SVTerminal01, via `fnv_record`) has `ITXT` (button text), `RNAM` (result text), `ANAM` flags, `INAM` note, `SCHR` result script and conditions per item [M]. The engine side has no hard item limit I can see: items sit in a `BSSimpleList` [S]. The UI limit (scrolling list, typed-text animation, text paging) is a live test. The text menu pages long text itself: `TextMenu::SetTextSource` formats text into a layout of N lines, then advances `fieldbc += consumed` and repeats [S, decomp `computersmenu.cpp` ~1886]. Typing speed is the setting `iComputersDisplayRateMenus` [M]; this is a player pain point for long texts.

**Portable terminal / holotape.** Not documented anywhere I could read. In vanilla a holotape is a NOTE form; the Pip-Boy reads it as text/sound/image and cannot open a terminal [?, my memory, not verified]. Options that need no new UI:

1. An inventory item (aid/misc "Company ledger") with a script `OnEquip` -> `OfficeTerminalRef.Activate Player` [?]. `Activate` is a vanilla command (opcode 0x100D, handler 0x005B59F0 calls `TESObjectREFR::Activate`) [M]. Works only if the terminal ref exists and the Pip-Boy menu has closed. Live test 2.
2. JIP `SetOnMenuOpenEventHandler 1012` (SleepWait) etc. is not needed.
3. The user's decision is "terminal only", so a portable terminal is a convenience for the player who is out in the Mojave. If it fails, HQ-only plus branch terminals is still the design.

**Terminal opened at a distance.** No dedicated command found. `Ref.Activate Player` is the known trick [?]. A script-opened terminal also asks for hacking/password if locked: set the terminal Unlocked flag (the `DNAM` flags show `unlocked` in vanilla [M]). Note TERM has no script slot (no `SCRI` in SVTerminal01) [M], so there is no object `OnActivate` block on the terminal itself; use xNVSE `SetEventHandler "OnActivate"` filtered to the terminal ref [S: `onactivate` is in `EventManager.cpp` event list], or the JIP menu-open handler.

### 1.2 Data storage

- xNVSE arrays are serialized into the **.nvse cosave**, not the .fos. `ArrayVarMap::Save` writes record `'ARVS'` then one `'ARVR'` per array; it calls `Clean()` first (garbage-collects unreferenced arrays) and skips temporary arrays [S, `ArrayVar.cpp:1803`]. Arrays with no live reference are dropped on save. Strings inside arrays carry a `UInt16` length, so up to 65,535 characters each [S].
- I found no array element limit in `ArrayVar.cpp` (grep for max/limit found none relevant) [S]. A Nexus thread (W) reports a 16 MB cosave still loading fine, and another reports a save-game size ceiling of 64 MB (128 MB with an engine fix). Not opened, so treat as [W].
- Size estimate for this mod: 4 towns x about 12 goods x (price, stock, demand, share) + routes + staff + ledger of the last 30 days is a few thousand numbers: tens of KB. Not a bloat risk. The bloat risk is a per-day history that grows forever (cap it: ring buffer of 30 or 60 days).
- **Risk: cosave loss.** If the player loads a save without its .nvse cosave (mod manager copies, cloud sync), all arrays are gone while quest variables, globals and `.fos` state stay. Mirror the **critical state in quest variables and GLOB records** (cash, loan, tier, week counter, last processed day, heat). Arrays hold detail and are rebuildable from the mirror (degrade to "ledger rebuilt").
- JIP also has persistent "aux" variable maps and `GetLoadOrderChanged` (`jip_fn_utility.h`) [S]; not needed.

### 1.3 The daily tick

- **Detect day changes by comparing, not by timers.** `GameDaysPassed` is a vanilla global (Special variables page) [W]. Store `lastDay = floor(GameDaysPassed)`; each quest-script run compute `n = floor(GameDaysPassed) - lastDay`; run `n` day steps (cap at e.g. 30 to avoid long freezes, then keep remainder). This is robust against sleeping, waiting (the Wait menu skips time), fast travel and long absences, because nothing depends on the script having run during that time.
- **Known trap**: community reports that `GameDaysPassed` can desync from `GameHour` in vanilla, and a Nexus fix mod exists (mods/63880) [W]. We should read both and accept a day when `GameDaysPassed` integer part changes, but tolerate +/-1 glitches (never run a day step twice: guard with `lastDay` strictly increasing).
- **Quest script delay.** `SetQuestDelay quest float` is a vanilla command (opcode 0x11DC, handler 0x005DA1E0) [M]. The default setting here is named `fQuestScriptDelayTime` (not `fQuestDelayTime`) [M]. A community post says the default is 5 s and that setting the variable in the script does not always work, `SetQuestDelay` being the reliable way [W]. Plan: `SetQuestDelay CCQuest 5`. At timescale 30 a game day is 48 real minutes, so a 5 s poll is overkill; use 10 to 30 s and only do heavy work on a new day.
- Quest scripts do not run while a menu is up (game paused); the company screen is a menu, so the tick will not advance while the player reads the terminal. That is fine and actually safe (no state change under the player's eyes).
- **Events** (xNVSE `SetEventHandler`, from `EventManager.cpp`) [S]: `LoadGame`, `PostLoadGame`, `PreLoadGame`, `SaveGame`, `NewGame`, `ExitToMainMenu`, `OnActivate`, `OnLoad`, `OnDeath`, `OnMurder`, `OnCellAttach`/`OnCellDetach`/`OnCellRefsLoaded`, `OnEnable`/`OnDisable`, `OnTerminalHacked`, `OnPackageStart`/`OnPackageDone`, `OnHit`, `OnSell`, `OnAdd`/`OnDrop`. **There is no sleep/wait event**, but JIP lets us catch the menu: `SetOnMenuOpenEventHandler`/`Close` for menu 1012 (SleepWait) [S, ID from xNVSE `GameUI.h`]. The day-compare approach makes this unnecessary.
- JIP has `SetDelayElapsed quest float` / `GetDelayElapsed` [S, `jip_fn_script.h`] to force a quest script run soon (e.g. right after loading a save or closing the Wait menu: set elapsed to the delay so the tick fires on the next frame). Useful for "catch up now".
- Event handler registration is **not saved** in the .fos for most NVSE events; register again on `LoadGame`/`PostLoadGame`, which is also the right place to re-push terminal texts [S: `flushOnLoad` field exists in `EventManager.cpp`; rule of thumb from NVSE docs [?]].
- Per-frame cost: day step loops are plain arithmetic. Use a budget (e.g. at most 5 simulated days per quest run) so a 60-day wait does not stall a frame.

### 1.4 Caravans in the world

What vanilla does (via `fnv_record`) [M]:

- Many named travel packages with a clock schedule: `VCaravanMojaveToMojave3pm`, `VCaravan188ToFreesideStartAny5am`, `VCaravanFreesideTo188StartAny7am`, `CaravanTravelPatrol`, `CaravanGuardRetreat`, `VERT1GSCaravanRun`, `VERT2WBCaravanAmbush`, `AttackedCaravanTravelPackage`, `CrimsonCaravanGuardAAMTravel`, plus sandbox/sleep/eat packages for the Crimson Caravan camp (`CrimsonCaravanWorkerSandbox`, `CrimsonCaravaneerSleep22x8`). So vanilla builds caravans from **placed (or script-spawned) actors with time-scheduled Travel packages**, and ambush/attack variants as separate packages and quests. That is the pattern to copy.
- The two vanilla "traveling merchant" NPCs that use `VCaravanMojaveToMojave3pm` are leveled spawn bases (`VSpawnSpecialMerchantMaleGroup01Post188`) [M], i.e. vanilla itself spawns road travellers at runtime. The user's "no runtime spawner" decision covers towns; for roads a spawner may be the only sane option (see below).
- Crimson Caravan faction `CrimsonCaravanFactionNV` (000FED1D), animal faction `CrimsonCaravanAnimalFaction`, Alice `AliceMcLafferty` (000EC7A1), Cass quest `VCassCompanion` "Heartache by the Number" (0015DA16) [M]. Do not edit these forms; read them only.

What is **not proven**: that actors with Travel packages really move "virtually" while unloaded, and how far. The brief states it as a fact; I tried to confirm it in the decomp (grep for virtual movement, `LowProcess` travel) and found nothing readable [S: no hit]. Treat as [?]. Live test 5 settles it.

Proposed design for company caravans (our own, not vanilla's):

1. **Ledger first.** A caravan trip is a record: route, depart day/hour, arrive time, cargo value, guard strength, danger roll. On paper it resolves at the day step.
2. **Visible caravan only near the player.** A quest script checks, each tick, whether the player is within about 8 to 12 cells of any route segment (use route waypoint markers and `GetDistance`, or a cell check). If yes and a trip is "in transit", materialise a real group: **PlaceAtMe a small number of template NPCs** (1 driver, 1 to 2 guards, 1 brahmin) at the interpolated position, give them `AddScriptPackage` (a Travel package to the next waypoint marker) [M: command exists, handler 0x005CC4F0] and tag them with a company faction. When the player leaves, `Disable` + `MarkForDelete` (or reuse the same refs with `Enable`/`Disable`: the `TESObjectREFR::Enable` and `Disable` handlers exist per the NPC catalogue) and fall back to paper.
3. **Placed (not spawned) for the dedicated sites** (HQ staff, town stalls). Placed refs exist in the plugin, work with `Enable`/`Disable` and enable parents, and are always in the save as the same refs. That honours the user's rule.
4. **Why spawn at all for caravans:** a placed caravan crew would exist forever in a cell and must be moved by package schedules even while the player is away; if virtual movement does not work for unloaded actors, they would sit at the start marker or teleport. A transient crew placed at the right place and time avoids that (cost: 3 to 4 actors for a few game hours).
5. **Ambush made real:** the ledger rolls an ambush (danger vs guards) at day step. If the player is near the route when the trip is in transit, instead of resolving on paper put a hostile group (leveled list of the route's faction, e.g. Powder Gangers near Goodsprings/Primm) near the caravan and let the guards fight. The result (survive or lose cargo) is read back from the real fight (alive count after N seconds) and written to the ledger. If the player is not near, the paper result stands. Both paths write the same ledger fields. Cap: at most one live encounter at a time (AI cap: `iAINumberActorsComplexScene` 20 complex actors near the player [M README]).

### 1.5 Visible growth

- Enable/disable placed refs as tiers go up: `Enable`/`Disable`, optionally with an **enable parent** (XMarker with a state controlled by `Enable`/`Disable`): children follow the parent's state [? vanilla feature; handlers `TESObjectREFR::Enable` 0x00573F40, `Disable` 0x00574400 in the NPC catalogue] [M].
- One XMarker per tier per site: enabling the marker shows all its children (sign, wagon, extra crates). Store tiers in a quest variable and apply on `PostLoadGame` and on tier change. Cheap and save-safe because enable state is stored in the reference's save data.
- **Navmesh trap [?]**: enabled/disabled objects that block navmesh (walls, wagons, big crates) have no effect on the navmesh unless the cell has a "navmesh cut" (FNV has no runtime obstacle cutting like Skyrim's dynamic navmesh). Rule: show decorative props that sit on already-clear ground or are small and non-blocking; do not enable a building where NPCs walk. Test by walking an NPC past the enabled prop (live test 4).
- New buildings (stone yard, smokehouse) should be **new interior cells or separate placed prefab clusters on empty ground** rather than altering existing vanilla buildings.

### 1.6 Compatibility

- Placed refs in a vanilla exterior cell require an **override of that CELL record** (plus its child refs). Mods that touch the same cell header (lighting, water, music, owner) and load later win the header; the child refs still merge because refs are separate records. Popular mods that edit Goodsprings, Primm and the Mojave Outpost area exist (this was not checked in the load order I can read: `fnv_record find Goodsprings` shows one override, `HelloExterior.esp` on `GoodspringsSource`, which is the user's own test setup, not representative) [M]. Method for minimising: add only REFR records and new forms, never edit existing refs, copy the CELL header unchanged, and put everything possible in **new interior cells** (HQ office, warehouse, workshops) reached by one door per town.
- Existing saves: new placed refs in already visited cells appear on the next load because the cell reset logic reads the plugin; but the first-time cell data in an old save may not contain new refs until the cell resets (`iHoursToRespawnCell` default 72 [M README]) [?]. Persistent refs (marked persistent) are added immediately on load [?]. Plan: mark company refs persistent, or add them in the HQ interior (fresh cell). Test on an existing save (live test 1).
- **MCM.** MCM (the menu mod) would be a dependency on another mod; the user said "no dependency on other big mods". Settings can be done without MCM through a **settings terminal** (menu buttons that flip globals), consistent with "terminal only". Recommend: no MCM at all, or optional MCM for difficulty only.
- Requirements the user accepts: xNVSE + JohnnyGuitar NVSE (JIP LN likely fine). We need **JG** for terminal text/submenu/refresh; **JIP** only for menu open/close/click events and `GetMenuTargetRef`. Pick one set and state it on the page. Both are in widespread use.
- Load-order conflicts for the **terminal edits**: `SetTerminalMenuItemText` changes the in-memory base form; if two mods shared the same TERM form, they would clash. We use our own TERM forms only. Never touch vanilla terminals.
- Existing quest "Heartache by the Number": we only read Crimson Caravan forms (never edit); the loan from Alice must be gated on that quest state not being active in a way that conflicts (e.g. `GetStageDone VCassCompanion`...), or kept as a simple "Crimson Caravan Credit" via the NCR clerk/Alice's dialogue with a separate quest. Actions: read-only checks on vanilla quest stages.

## 2. Architecture proposal

### 2.1 Quests and scripts

| Quest / script | Job | Delay |
|---|---|---|
| `CCCore` (quest script, start game enabled) | Tick: compare `GameDaysPassed`, run `n` day steps, weekly bills on day % 7, tier checks, apply visible tier, push terminal texts when state changed. Holds mirrored critical state (cash, loan, week, heat, tier, lastDay) as quest variables. | 15 s |
| `CCLedger` (library functions, UDFs in NVSE) | Pure functions: price update, demand, route profit, wages, interest, ambush roll. No game side effects: easy to unit test by running the same functions in the console. | called by CCCore |
| `CCTerm` (quest script) | Terminal bridge: reads `pick` written by result scripts, applies the action (hire, buy, set route), then pushes texts and calls `RefreshTerminalMenu`. Registers the menu-open handler for 1057. | 0.5 s while menu open (via menu-mode block or the event), else idle |
| `CCWorld` (quest script) | Near-player checks (route proximity, spawn/despawn caravan crews, tier enable/disable), runs only when a company trip is "in transit". | 3 s, only when needed |
| `CCEvents` (UDFs) | `LoadGame`/`PostLoadGame`: re-register handlers, re-apply terminal texts, re-apply tier visuals. | event |

### 2.2 Data layout

- **Quest variables / globals (critical, in the .fos):** `cash`, `loanBalance`, `loanDueDay`, `tier`, `week`, `lastDay`, `heat`, `licence`, `strikes`. About 20 floats/ints.
- **xNVSE arrays (detail, cosave):** `towns` (StringMap: name -> map of price/stock/demand/share), `routes` (array of maps), `staff` (array of maps), `ledgerHistory` (ring buffer of day records, cap 60), `events` (queue of memos). Rebuildable from the mirror.
- **TERM forms:** one top-level `CC_HQ_Term` plus about 10 to 14 sub-screen TERMs (Overview, Routes, Staff, Warehouses, Workshops, Contracts, Memos, Loan/Finance, Dodgy, Settings). Each pre-authored with pooled slot items (see 1.1).

### 2.3 Terminal "app"

- Screen = TERM. Button = pooled item with a result script that writes `CCCore.pick = N` and `CCCore.screen = M`. Pooled items 1..12 per screen, conditions control visibility; texts set by script.
- A "dashboard line" = the **button label itself** (up to 259 chars): `"Primm   stock 14/20   price 61   share 38%"`. Labels are plain list entries so they scroll, and `RefreshTerminalMenu` updates them in place. This is the live-number trick; the DESC body stays static (title, hints).
- A "detail page" = result text of the item (259 chars per call, so keep it short or split across 2 to 3 items: "A. Summary", "B. Cost breakdown", "C. Risks").
- Number formatting: xNVSE `sv_Construct "%.0f"` style formatting is available in NVSE strings [W? not opened]; JG's text setter takes a string, so build with `sv_Construct` then `SetTerminalMenuItemText Term 1 idx str`. This is a standard NVSE feature [?], low risk.
- On every state change while the terminal is open: set texts, then `RefreshTerminalMenu`.
- Initial open: the JIP menu-open handler for 1057 (or xNVSE OnActivate) runs `PushAllTexts` for the screen being opened.

### 2.4 World refs

- HQ in Goodsprings (interior cell for the office) + office terminal ref (persistent) + "Company ledger" inventory item for the portable access.
- Branch offices in Primm, Sloan, Mojave Outpost (one interior or one small placed hut each).
- Per tier: XMarker + children (signs, wagon, crates) for each town.
- Route waypoint XMarkers (about 3 to 6 per route) for caravan interpolation.
- Caravan crew templates (NPC bases + brahmin) in a hidden holding spot; spawned on demand near the player.
- Dodgy path: raid event uses real guards (enable parent of an NCR inspection squad at the office) when the player is in the cell, paper otherwise.

## 3. Feasibility table

| Feature | How | Status | Risk |
|---|---|---|---|
| Menu items with live label text | `SetTerminalMenuItemText` type 1 | Documented in code (JG source) | Low: 259-char cap; needs live check that the label redraws |
| Live detail text | same, type 2 (result text) | Documented in code | Medium: unknown if result text is read at select time or cached |
| Redraw while open | `RefreshTerminalMenu` = `DisplayTerminal(false)` | Documented in code (JG source + decomp) | Low-Medium: flicker, scroll position reset unknown |
| Body (DESC) text with numbers | impossible by script (lazy file read) | Proven by decomp | n/a: design around it |
| %-token or `<Global=>` in text | unknown in FNV | Needs live test | Medium (nice-to-have only) |
| Actions from terminal | pre-authored items with result scripts + conditions | Vanilla feature (real TERM record decoded) | Low |
| Added (runtime) menu items | `AddTerminalMenuItem` (blank item, no script) | Documented in code | Low: only nav/info items |
| Submenus | `SetTerminalMenuItemSubmenu` or authored | Documented in code | Low |
| Many items per screen | scrolling list | Needs live test | Medium: UI limit unknown |
| Long text paging | engine `TextMenu::SetTextSource` pages text | Documented in decomp | Medium: slow typing (setting) |
| Open terminal from script | `TermRef.Activate Player` | Needs live test (command exists) | Medium |
| Portable terminal item | OnEquip script -> Activate | Needs live test | Medium-High (Pip-Boy menu timing) |
| Know which terminal is open | JIP `GetMenuTargetRef 1057` | Documented in code | Low |
| Hook on terminal open | JIP `SetOnMenuOpenEventHandler 1057` | Documented in code | Low: ordering vs first draw unknown |
| Day tick, catch-up | compare `GameDaysPassed` | Documented (wiki via snippet) | Low-Medium: desync bug, handle with monotonic guard |
| Quest delay | `SetQuestDelay` | Proven (handler 0x005DA1E0, command exists) | Low |
| Re-apply state on load | xNVSE `PostLoadGame` event | Documented in code (EventManager.cpp) | Low |
| Persistent arrays | xNVSE arrays in cosave | Documented in code | Medium: cosave loss, mirror in vars |
| Placed refs per tier | enable parent XMarkers | Vanilla feature, handlers in engine | Low |
| Navmesh around enabled props | avoid blocking props | Needs live test | Medium |
| Spawned caravan near player | `PlaceAtMe` + `AddScriptPackage` | Command handlers proven | Medium: AI and cap (20) |
| Virtual movement of unloaded caravans | vanilla travel packages | NOT verified | High: do not rely on it |
| Real ambush when near | spawn hostile group, read result | Needs live test | Medium |
| Compatibility (Goodsprings etc.) | refs only, new interiors, no edits to vanilla refs | Documented practice | Medium |
| MCM | skip; settings terminal | n/a | Low |

## 4. Bold ideas

1. **Use button labels as the live dashboard.** Because DESC cannot change but entry text can, build the Overview screen entirely out of buttons that are read-only lines (selecting them opens the detail). It looks like a spreadsheet row per town and updates in place. Cost: easy.
2. **Terminal as a command queue.** Result scripts only push orders into a queue (array); the tick applies them. Gives "Orders pending: 3" on screen, cancel before the day ends, and makes catch-up trivial (the tick consumes the queue). Cost: easy.
3. **Memo drip.** One memo screen per game day, built from a pool of ledger events; the player decides in a short numbered menu, with a "defer" button. Missed memos auto-resolve with the default. Cost: moderate.
4. **Transient real caravan as a reward.** When the player is near the road, the caravan appears (3 to 4 actors) and the player can ride along, take the first shot at an ambush, or ignore it. Rewards: guard bonus on the ledger. Cost: moderate to high.
5. **"Cosave-safe" snapshot.** Write the company state as a short readable text file via JIP `WriteStringToFile`/`WriteArrayToFile` [S, `jip_fn_utility.h`] on each save; on a load with an empty cosave, re-import. Adds a "backup" safety net. Cost: low (optional, but file IO from a Nexus mod may worry some players).

## 5. Pitfalls and design flaws

- **Body text cannot be dynamic.** Any design that shows numbers in the welcome text (the brief's hook idea at 0x007586E0) means patching the engine's text source; it is possible, but avoid it for a public mod. Use labels and result text.
- **259-character cap per text.** A "P&L statement" in one text will not fit. Plan screens that are 6 to 10 short lines (one button each).
- **Terminal edits are not persistent.** They modify an in-memory form; on every load they must be re-applied (inference from the engine design [?]; verify in live test 3). Failing to do so shows stale or empty menus after loading.
- **Do not depend on JG added items for actions.** They have no script.
- **Menu pauses the game.** Quest scripts are asleep while the terminal is open. Do not rely on "the day ticks while reading". The `MenuMode 1057` block [W] or the menu events are the only code that runs in there.
- **Day-step loop budget.** A long absence needs a cap and a "catching up" flag to avoid hitching.
- **Do not assume virtual movement of unloaded NPCs** (see 1.4).
- **Quest-stage coupling to vanilla** (Primm sheriff, Powder Gangers, Quarry Junction, Cass quest) must be done by read-only `GetStageDone`/`GetQuestCompleted` checks: never `SetStage` on vanilla quests.
- **GameDaysPassed bug** (stuck or desynced values) can freeze or double the tick. Guard monotonicity.
- **Cosave dependency** is real; mirror critical state.
- **Added loan from Alice** (the proposal): technically trivial (quest variable), but she is a named vanilla NPC with her own dialogue; the user's rule "vanilla named NPCs untouched" means the loan must come from a **new** dialogue topic on a separate quest, or a terminal-only offer ("Crimson Caravan Credit Office" letter), not edits to Alice's topics.

## 6. Questions only the user can answer

1. Is a hard dependency on JohnnyGuitar NVSE acceptable (needed for terminal text/refresh)? If not, the terminal must be fully static and we lose live numbers.
2. If virtual movement of unloaded caravans turns out not to work, are transient spawned crews for road trips acceptable (the "no runtime spawner" decision was about towns)?
3. Is a typed-text box (JIP `ShowTextInputMenu`) acceptable for naming the company, or is "no typed input" a hard rule?
4. May we add a new interior door in the exterior cells of Goodsprings/Primm/Sloan/Mojave Outpost (one REFR each), or must everything be accessed some other way?

## 7. First five live tests (in order; each uses the real game with the mod loaded)

1. **Terminal text edit + refresh round trip.** Build one throwaway TERM with 3 pooled items. In-game, run `SetTerminalMenuItemText Term 1 0 "Cash 4210"`, open the terminal, then change it with the console while open and call `RefreshTerminalMenu`. Check: does the label change in place, does the scroll position reset, does the edit survive save, quit, reload (expected: no), and does `SetTerminalMenuItemText Term 2 ...` (result text) show at select time. Also try %g / `<Global=...>` in text (the only live check for token support).
2. **Open the terminal by script.** `OfficeTermRef.Activate Player` from a console and from a script `OnEquip` of a misc item used from the Pip-Boy. Check: opens at a distance, Pip-Boy menu closing order, unlocked flag, behaviour while a menu is open.
3. **Menu event timing.** `SetOnMenuOpenEventHandler MyHandler 1057`: does the handler run before the first draw (so texts set there appear), and does `GetMenuTargetRef 1057` return the ref. Plus: do result scripts run before or after the result text is shown.
4. **Item count and text limits.** TERM with 30 pooled items (conditions all true), and 259-char texts: does the list scroll, does it crash, how long does the typing take at the default `iComputersDisplayRateMenus`, can the player skip it.
5. **Virtual movement and spawn/despawn caravan.** (a) A placed NPC with a scheduled Travel package between two markers 40 cells apart: where is it after `wait 6 hours` with the player far away, in the same worldspace? (b) PlaceAtMe of a 4-actor crew with `AddScriptPackage`, then `Disable`/`MarkForDelete` after leaving: any leftover refs, save-size growth, AI cap issues.

Also run in the same session: a tick test (wait 5 days with the 15 s quest delay and verify `n` catch-up steps, one and only one day step per day), and a "load an old save with the mod added" test (new interior and persistent refs appear?).

## 8. Source list (what I actually opened)

- `https://github.com/carxt/JohnnyGuitarNVSE` (README confirms docs live on the GECK wiki category "Functions (JohnnyGuitar NVSE)"); raw `JG/functions/fn_terminal.cpp`, `fn_terminal.h`, `JG/internal/Game/Bethesda/BGSTerminal.hpp`
- `https://github.com/jazzisparis/JIP-LN-NVSE` raw: `functions_jip/jip_fn_ui.h`, `jip_fn_script.h`, `jip_fn_utility.h`, `functions_ln/ln_fn_terminal.h`
- `https://github.com/xNVSE/NVSE` raw: `nvse/nvse/EventManager.cpp`, `nvse/nvse/ArrayVar.cpp`, `nvse/nvse/GameUI.h`
- Local decomp: `fnv_decomp\src\fallout_shared\tesdescription.cpp`, `src\fallout\interface\menus\computersmenu.cpp`
- FNV MCP read-only lookups: `fnv_command_info` (Activate, AddScriptPackage, SetQuestDelay, SetPasswordNote, GetMenuTargetRef, SetOnMenuOpenEventHandler), `fnv_record` (SVTerminal01, caravan PACKs, Crimson Caravan faction, Alice, VCassCompanion), `fnv_func` (ComputersMenu functions, TESDescription)
- Search-snippet only (pages blocked, [W]): GECK wiki `MenuMode`, `Special variables`/`GameDaysPassed`, `Terminal` pages (geck.uesp.net / geckwiki.com); Nexus forum threads on `fQuestDelayTime`, `GameDaysPassed` desync (mods/63880), cosave size, terminal text replacement.
