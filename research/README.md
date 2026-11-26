# NPC catalogue for an NPC-population mod (Fallout: New Vegas 1.4.0.525)

Goal of the mod: more NPCs in the world, so towns and roads feel busier.
This folder lists every engine class and function that has to do with NPCs, and picks out the ones a population mod has to touch.

Built on 2026-11-26 from the fnv-mcp engine map (generated 2026-11-10 from decomp commit `db4568bf` and fnvsym `proofs/verified.csv`).
All addresses are for FalloutNV.exe 1.4.0.525.

## Files

| File | What is in it |
|---|---|
| [CLASSES.md](CLASSES.md) | 441 NPC classes by subsystem: base classes, size, vtable address, number of functions |
| [FUNCTIONS.md](FUNCTIONS.md) | 6,432 NPC functions by subsystem and class, with address, name, proof status and source file |
| [COMMANDS.md](COMMANDS.md) | 213 script and console commands for NPCs, with their engine handler addresses |
| [SETTINGS.md](SETTINGS.md) | 701 game and INI settings that touch NPCs, with defaults |
| `npc_*.csv` | The same four lists as CSV (the function CSV also has signatures) |

### How much of it is named

| Status | Functions | Meaning |
|---|---|---|
| proven | 3,066 | name proven from evidence (community headers, Xbox PDB, RTTI, code) |
| class | 1,043 | the owning class is proven, the method name is not |
| probable | 469 | strong evidence, not proven |
| decomp | 1,071 | the decomp's own name: machine-made, treat it as a guess |
| unnamed | 754 | no name yet |
| rejected | 29 | the decomp name was checked and found wrong |

### Functions per subsystem

| Subsystem | Functions |
|---|---|
| 1 Spawning and population | 186 |
| 2 Actor references (Actor, Character, Creature, MobileObject) | 408 |
| 2b Player (PlayerCharacter shares the Actor code) | 165 |
| 3 Base records (TESNPC, TESCreature, race, class, faction, leveled lists) | 454 |
| 4 Process levels and the AI update loop | 562 |
| 5 AI packages and daily routines | 426 |
| 6 Movement and pathfinding | 365 |
| 6b Navmesh | 221 |
| 7 Combat | 524 |
| 8 Detection, crime and reactions | 40 |
| 9 Dialogue, barks and companions | 183 |
| 10 Animation, faces and bodies | 395 |
| 11 Cells and world loading | 163 |
| 12 Other code in `src/fallout/ai/` without a better name | 2,340 |

## How an NPC gets into the world

1. **Base record.** A `TESNPC` or `TESCreature` (both `TESActorBase`), or a leveled list (`TESLevCharacter`, `TESLevCreature`) that picks one.
2. **Reference.** A placed reference from a plugin, or one made at runtime by `PlaceAtMe` -> `TESDataHandler::CreateReferenceAtLocation`. Leveled references are resolved when their cell loads (`TESObjectCELL::CalcLeveledCreatures`).
3. **3D.** `ModelLoader::QueueReference` queues a `QueuedCharacter` / `QueuedCreature`; the body is cloned on a background thread and the FaceGen head is built by `QueuedHead` / `BSFaceGenManager::CreateFaceGenHead`. Then `Actor::Load3D`.
4. **Process.** `MobileObject::GetDesiredProcessLevel` picks a level from the state of the actor's cell, and `SetProcessLevel` gives the actor a `HighProcess`, `MiddleHighProcess`, `MiddleLowProcess` or `LowProcess` and registers it with `ProcessLists`.
5. **Every frame.** `ProcessLists::UpdateProcessLists` runs the lists; high-process actors get full AI, movement, animation, scripts and magic updates.
6. **Behaviour.** AI packages (sandbox, patrol, guard, eat, sleep...) choose what the NPC does; `ActorMover` and the path handlers move it.

## Start here: the functions a population mod touches

All of these were checked against the engine map; status is given when the name is not proven.

### Spawning NPCs

| Address | Function | Notes |
|---|---|---|
| 0x005C4B30 | `PlaceAtMe` | Engine side of the PlaceAtMe command. For a leveled list (form type 0x2C creature, 0x2D character) it runs the list's leveled calculation, then calls `CreateReferenceAtLocation` once per result; a new actor starts at alpha 0 and gets `Reset3D`, so it fades in. Other objects are spread over 9 points around the caller with a ray check. |
| 0x005C4A70 | `Cmd_PlaceAtMe_Execute` | Script/console handler |
| 0x005D9810 | `Cmd_PlaceLeveledActorAtMe_Execute` | Script/console handler |
| 0x004698A0 | `TESDataHandler::CreateReferenceAtLocation` | Makes a new reference of a base form at a position and angle in a cell or worldspace. The core "spawn" call. |
| 0x00487F70 | `TESLeveledList::CalculateCurrentFormList` | Picks entries from a leveled list for a level |
| 0x00488350 | `TESLeveledList::CalculateCurrentFormListForRef` | The same, for a reference |
| 0x00550C60 | `TESObjectCELL::CalcLeveledCreatures` | Resolves the leveled actors of a cell |
| 0x0056B020 | `TESObjectREFR::SetLeveledCreature` | |
| 0x0056AF40 | `TESObjectREFR::IsLeveledCreature` | |
| 0x0056B0B0 | `TESObjectREFR::RestoreLeveledCreatureOriginalBase` | |
| 0x00573F40 | `TESObjectREFR::Enable` | Despawn and respawn without deleting |
| 0x00574400 | `TESObjectREFR::Disable` | |
| 0x00564930 | `TESObjectREFR::SetDelete` | Marks a runtime reference for deletion |
| 0x005262A0 | `BGSEncounterZone::ShouldReset` | Encounter zones decide level and reset of their actors |
| 0x00526270 | `BGSEncounterZone::DetermineLevel` | |
| 0x00526100 | `TESObjectCELL::GetHoursToRespawnCell` | Cell respawn timer (`iHoursToRespawnCell`, default 72) |
| 0x00546B10 | `TESObjectCELL::SetDetachTime` | Time a cell was unloaded, used for respawn |

### Loading an NPC's 3D (the per-NPC loading cost)

| Address | Function | Notes |
|---|---|---|
| 0x00444850 | `ModelLoader::QueueReference` | Queues a reference's 3D on the background loader |
| 0x00446B50 | `ModelLoader::UpdateQueuedReferencePriorities` | Reorders the queue (nearer first) |
| 0x004416C0 | `QueuedCharacter::BackgroundClone` | Clones the body on the loader thread |
| 0x004418B0 | `QueuedCharacter::AttachHeadParts` | |
| 0x0043ECB0 | `QueuedHead::Run` | Builds the FaceGen head |
| 0x00654720 | `BSFaceGenManager::CreateFaceGenHead` | |
| 0x0087E060 | `Actor::Load3D` | |

### Process levels and the AI loop (the per-frame cost of more NPCs)

| Address | Function | Notes |
|---|---|---|
| 0x009334B0 | `MobileObject::GetDesiredProcessLevel` | Returns 0 High, 1 MiddleHigh, 2 MiddleLow or 3 Low from the state of the actor's cell (`TES::IsCellBuffered`), not from distance. So the loaded grid (`uGridsToLoad`, default 5) is likely what decides how many NPCs run at High; not yet tested in game. |
| 0x009320E0 | `SetProcessLevel` (class proven) | Creates the process object for the new level and calls `ProcessLists::AddReference` |
| 0x00931710 | `MobileObject::StartHighProcess` | |
| 0x00881D30 | `Actor::StartHighProcess` | |
| 0x0096D450 | `ProcessLists::AddReference` | |
| 0x0096D470 | `ProcessLists::RemoveReference` | |
| 0x0096D810 | `ProcessLists::UpdateProcessLists` | Per-frame driver. Below 50 FPS it skips list updates on some frames, below 10 FPS it runs them about once a second. Then runs the low list, the middle-high list and crime lists. |
| 0x00972BB0 | `ProcessLists::UpdateHighProcess` (decomp name) | |
| 0x0096B810 | `ProcessLists::UpdateMiddleHighList` | |
| 0x0096B050 | `ProcessLists::UpdateLowList` | |
| 0x0096C7C0 | `ProcessLists::RunActorUpdates` (decomp name) | |
| 0x0096DB30 | `ProcessLists::UpdateActorsMovement` | |
| 0x00978550 | `ProcessLists::RunActorScripts` | |
| 0x0096C970 | `ProcessLists::ParallelUpdateAnimationScenegraph` | |
| 0x0096E3C0 | `ProcessLists::InsertActorCloseToPlayer` | The "actors close to the player" list is a fixed array of **50**, sorted by distance, and also capped by `iAINumberActorsComplexScene` (default **20**). Actors past the cap are not in it. |
| 0x0096E570 | `ProcessLists::SortActorsCloseToPlayer` | Also reads `iAINumberActorsComplexScene` |
| 0x00977660 | `ProcessLists::RebuildActorsCloseToPlayer` | |
| 0x0096BC50 | `ProcessLists::CountHighActors` | |
| 0x00977130 | `ProcessLists::DisableExcessDeadActors` | Removes bodies once there are too many. Normal scene: needs 15 dead (`iRemoveExcessDeadCount`) and 20 actors (`iRemoveExcessDeadTotalActorCount`). With 25 or more high actors in a complex scene: 3 dead (`iRemoveExcessDeadComplexCount`) and 20 actors (`iRemoveExcessDeadComplexTotalActorCount`). |
| 0x008D6F50 | `HighActorCuller::Run` | By its name, culls high-process actors (not read yet) |
| 0x008EEEC0 | `HighProcess::Update` | One update per process level |
| 0x00919F60 | `MiddleHighProcess::Update` | |
| 0x0092D050 | `MiddleLowProcess::Update` | |
| 0x0090C360 | `LowProcess::Update` | |
| 0x00888B50 | `Actor::Update` | |
| 0x008C7DA0 | `AILinearTaskThreadManager::AIThread1TaskFunc` | AI worker threads (`bUseThreadedAI:General`, default off) |
| 0x008C7F50 | `AILinearTaskThreadManager::AIThread2TaskFunc` | |

### Making NPCs look busy

| Address | Function | Notes |
|---|---|---|
| 0x00907700 | `LowProcess::SelectNextPackage` (decomp name) | Package choice |
| 0x00881450 | `Actor::GetPackage` | |
| 0x00673180 | `TESPackage::SetPackageSchedule` | |
| 0x005C95A0 | `Cmd_EvaluatePackage_Execute` | Force a package re-check |
| 0x009F4700 | `SandBoxActorPackageData_ext::SelectSandboxActivity` (decomp name) | Sandbox: pick eat, sit, sleep, wander, idle marker |
| 0x00972D30 | `ProcessLists::PlaceActorsinBedsOrChairs` | |
| 0x00970D50 | `ProcessLists::InitPackageLocations` | |
| 0x00977CB0 | `ProcessLists::CommentOnPlayerAction` | NPC comments on the player |

### Which cells are loaded

| Address | Function |
|---|---|
| 0x00451A50 | `TES::LoadGridCell` |
| 0x00450DD0 | `TES::CullGridCells` |
| 0x004511E0 | `TES::IsCellLoaded` |

## Settings that limit how many NPCs you can have

"Checked" means the code that reads the setting was read for this catalogue. "Name" means the meaning comes from the setting's name and the functions that read it; read them before relying on it.

| Setting | Default | What it does | Read by | |
|---|---|---|---|---|
| `uGridsToLoad:General` | 5 | Size of the loaded grid around the player; process level follows the loaded cells | `TES::CullGridCells`, `TES::GetGridCellCell` and 48 more | name |
| `iAINumberActorsComplexScene` | 20 | Cap on the sorted "close to player" actor list (hard limit 50) | `ProcessLists::InsertActorCloseToPlayer`, `SortActorsCloseToPlayer` | checked |
| `iRemoveExcessDeadCount` / `iRemoveExcessDeadTotalActorCount` | 15 / 20 | Bodies are removed only when there are at least this many dead and this many actors (normal scene) | `ProcessLists::DisableExcessDeadActors` | checked |
| `iRemoveExcessDeadComplexCount` / `iRemoveExcessDeadComplexTotalActorCount` | 3 / 20 | The same in a complex scene | `ProcessLists::DisableExcessDeadActors` | checked |
| `fRemoveExcessDeadTime` | 10.0 | Seconds between dead-body checks | `ProcessLists::DisableExcessDeadActors` | checked |
| `iLowProcessingMilliseconds` | 2 | Time budget for the low-process list | `ProcessLists::UpdateLowList` | name |
| `fSortActorDistanceListTimer` | 3.0 | Timer for the actor distance list | `PlayerCharacter::Update` | name |
| `iNumberActorsInCombatPlayer` | 20 | Actors that may fight the player at once | `TryStartCombatAction` | name |
| `iMaxHiPerfCombatCount:Combat` | 4 | Combatants that get the expensive combat updates | two unnamed Actor functions | name |
| `bUseThreadedAI:General` | False | Run AI on worker threads | two unnamed AI thread functions | name |
| `iAIThread1HWThread:General` / `iAIThread2HWThread:General` | 3 / 4 | Hardware threads for the two AI threads | | name |
| `bUseMultiThreadedFaceGen:BackgroundLoad` | True | FaceGen on a worker thread | `BipedAnim::CanLoadHiddenBipedObjects` | name |
| `bBackgroundCellLoads:BackgroundLoad` | True | Load cells in the background | | name |
| `fLODFadeOutMultActors:LOD` | 2.5 | Actor fade-out distance multiplier | `TES::InitFadeOutMultipliers` | name |
| `fActorLODDefault` / `fActorLODMin` / `fActorLODMax` (`:LOD`) | 6.5 / 2.0 / 15.0 | Actor fade distance slider | | name |
| `iActorShadowCountExt` / `iActorShadowCountInt` (`:Display`) | 2 / 4 | Actors that cast shadows | | name |
| `fAISocialRadiusToTriggerConversation` (and `...Interior`) | 2000 / 500 | How close NPCs must be to start talking to each other | `HighProcess::IsCurrentPackageTarget` | name |
| `fAISocialchanceForConversation` (and `...Interior`) | 60 / 25 | Chance they do | | name |
| `fSandbox*` | various | Meal times, sleep times and activity lengths for sandboxing NPCs | | name |

## What to read before writing code

- `decomp` and `unnamed` names are guesses or blanks; read the code (`fnv_func action=code`) before hooking one.
- Most of the 2,340 functions in group 12 are real NPC logic without a good name yet. If the mod needs one, name it from its code first.
- The engine map is from 2026-11-10; names proven since then are not in it.
