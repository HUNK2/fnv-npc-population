# NPC functions

All 6432 NPC-related functions of FalloutNV.exe 1.4.0.525, by subsystem, then class. Status: **proven** = name proven from evidence (fnvsym), **class** = owning class proven, method name not, **probable** = strong evidence, not proven, **decomp** = the decomp's own name (machine-made, treat as a guess), **unnamed** = no name yet, **rejected** = the decomp name was checked and found wrong. The same rows are in [npc_functions.csv](npc_functions.csv) with signatures.

## Contents

- [1 Spawning and population](#1-spawning-and-population) (186)
- [2 Actor references (the NPC in the world)](#2-actor-references-the-npc-in-the-world) (408)
- [2b Player (shares the Actor code)](#2b-player-shares-the-actor-code) (165)
- [3 Base records (what an NPC is made of)](#3-base-records-what-an-npc-is-made-of) (454)
- [4 Process levels and the AI update loop](#4-process-levels-and-the-ai-update-loop) (562)
- [5 AI packages and daily routines](#5-ai-packages-and-daily-routines) (426)
- [6 Movement and pathfinding](#6-movement-and-pathfinding) (365)
- [6b Navmesh (the data paths run on)](#6b-navmesh-the-data-paths-run-on) (221)
- [7 Combat](#7-combat) (524)
- [8 Detection, crime and reactions](#8-detection-crime-and-reactions) (40)
- [9 Dialogue, barks and companions](#9-dialogue-barks-and-companions) (183)
- [10 Animation, faces and bodies](#10-animation-faces-and-bodies) (395)
- [11 Cells and world loading (where NPCs live)](#11-cells-and-world-loading-where-npcs-live) (163)
- [12 Other code in the AI source files](#12-other-code-in-the-ai-source-files) (2340)

## 1 Spawning and population

Creating references at runtime (PlaceAtMe), leveled actors, encounter zones, cell respawn timers, and the background loader that builds an actor's 3D.

### BGSEncounterZone (19)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00525CB0 | 'scalar deleting destructor' | proven | src/bgsencounterzone.cpp:193 |
| 0x00525C40 | BGSEncounterZone | proven | src/bgsencounterzone.cpp:8 |
| 0x00526000 | Compare | proven | src/bgsencounterzone.cpp:555 |
| 0x00525FA0 | CopyFrom | proven | src/bgsencounterzone.cpp:581 |
| 0x00526340 | CreateNoZone | proven | src/bgsencounterzone.cpp:35 |
| 0x00526270 | DetermineLevel | proven | src/bgsencounterzone.cpp:386 |
| 0x00526190 | GetCalcedZoneLevel | proven | src/bgsencounterzone.cpp:165 |
| 0x00567EC0 | GetZoneLevel | proven | src/fallout_shared/tesobjectrefr.cpp:2570 |
| 0x00525F00 | InitItem | class | src/bgsencounterzone.cpp:83 |
| 0x00525D40 | Load | class | src/bgsencounterzone.cpp:48 |
| 0x005264A0 | LoadGame | proven | src/bgsencounterzone.cpp:517 |
| 0x00526250 | QMatchPCBelowMin | decomp | src/bgsencounterzone.cpp:181 |
| 0x00526320 | QNeverReset | proven | src/bgsencounterzone.cpp:439 |
| 0x00525D00 | ResetFormData | class | src/bgsencounterzone.cpp:16 |
| 0x005260A0 | SetAttachTime | proven | src/bgsencounterzone.cpp:301 |
| 0x00526070 | SetDetachTime | proven | src/bgsencounterzone.cpp:270 |
| 0x00526160 | SetZoneLevel | proven | src/bgsencounterzone.cpp:371 |
| 0x005262A0 | ShouldReset | proven | src/bgsencounterzone.cpp:407 |
| 0x00525CE0 | ~BGSEncounterZone | proven | src/bgsencounterzone.cpp:210 |

### BGSLoadedReferenceCollection (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00526C90 | BGSLoadedReferenceCollection | proven | src/staging/blk_00520000_od.cpp:1410 |
| 0x00526E10 | Create | proven | src/staging/blk_00520000_od.cpp:739 |
| 0x005270B0 | FUN_005270b0 | rejected | src/fallout_shared/bgsloadedreferencecollection.cpp:78 |
| 0x005273C0 | GetNextObject | proven | src/staging/blk_00520000_od.cpp:1668 |
| 0x00526D50 | ~BGSLoadedReferenceCollection | proven | src/staging/blk_00520000_od.cpp:818 |

### ExteriorCellNewReferencesMap (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00855410 | 'scalar deleting destructor' | proven | src/fallout_shared/tessaveloadgame.cpp:1631 |
| 0x008553E0 | ExteriorCellNewReferencesMap | proven | src/fallout_shared/tessaveloadgame.cpp:139 |
| 0x00855440 | ~ExteriorCellNewReferencesMap | proven | src/fallout_shared/tessaveloadgame.cpp:3231 |

### ExtraEncounterZone (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432E90 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3848 |
| 0x00432E60 | ExtraEncounterZone | proven | src/fallout_shared/extradataobjects.cpp:855 |

### ExtraLeveledCreature (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004311F0 | ExtraLeveledCreature | proven | src/fallout_shared/extradataobjects.cpp:702 |

### ExtraOriginalReference (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00431980 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:7925 |
| 0x004319D0 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3681 |
| 0x00431950 | ExtraOriginalReference | proven | src/fallout_shared/extradataobjects.cpp:2390 |
| 0x004319B0 | ~ExtraOriginalReference | proven | src/fallout_shared/extradataobjects.cpp:2171 |

### ExtraPackageStartLocation (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432770 | Differs | proven | src/fallout_shared/extradataobjects.cpp:2518 |
| 0x00432650 | ExtraPackageStartLocation | proven | src/fallout_shared/extradataobjects.cpp:1478 |
| 0x004326C0 | ExtraPackageStartLocation | proven | src/fallout_shared/extradataobjects.cpp:2497 |

### ExtraPersistentCell (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432C60 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:1632 |
| 0x00432C20 | ExtraPersistentCell | proven | src/fallout_shared/extradataobjects.cpp:81 |
| 0x00432C90 | ~ExtraPersistentCell | proven | src/fallout_shared/extradataobjects.cpp:371 |

### ExtraStartingPosition (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00430850 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3003 |
| 0x00430780 | ExtraStartingPosition | proven | src/fallout_shared/extradataobjects.cpp:1868 |

### ExtraStartingWorldOrCell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004308C0 | ExtraStartingWorldOrCell | proven | src/fallout_shared/extradataobjects.cpp:102 |

### InteriorCellNewReferencesMap (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008552E0 | 'scalar deleting destructor' | proven | src/fallout_shared/tessaveloadgame.cpp:282 |
| 0x008552B0 | InteriorCellNewReferencesMap | proven | src/fallout_shared/tessaveloadgame.cpp:123 |
| 0x00855310 | ~InteriorCellNewReferencesMap | proven | src/fallout_shared/tessaveloadgame.cpp:2208 |

### LoadedReferenceMap (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00526B40 | 'scalar deleting destructor' | proven | src/fallout_shared/bgsloadedreferencecollection.cpp:27 |
| 0x00526BD0 | AddReference | decomp | src/fallout_shared/bgsloadedreferencecollection.cpp:7 |
| 0x00526B00 | LoadedReferenceMap | proven | src/fallout/ai/baseprocess.cpp:138 |
| 0x00526B70 | ~LoadedReferenceMap | proven | src/fallout_shared/bgsloadedreferencecollection.cpp:123 |

### ModelLoader (39)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00447330 | BuildKFFileList | proven | src/fallout_shared/modelloader.cpp:17176 |
| 0x00445570 | CancelReference | proven | src/fallout_shared/modelloader.cpp:16674 |
| 0x00445430 | CancelReplacementKFList | proven | src/fallout_shared/modelloader.cpp:16614 |
| 0x00448620 | ClearUnusedModels | proven | src/fallout_shared/modelloader.cpp:19963 |
| 0x00447850 | CopyFilenameList | proven | src/fallout_shared/modelloader.cpp:5127 |
| 0x004472A0 | FindModel | proven | src/fallout_shared/modelloader.cpp:1817 |
| 0x004431D0 | FUN_004431d0 | unnamed | src/fallout_shared/modelloader.cpp:229 |
| 0x00443220 | FUN_00443220 | unnamed | src/fallout_shared/modelloader.cpp:235 |
| 0x00448420 | FUN_00448420 | probable | src/staging/blk_00440000_od.cpp:6879 |
| 0x00446A60 | GetModelForBoundObject | proven | src/staging/blk_00440000_od.cpp:6968 |
| 0x00445750 | IsReferenceQueued | proven | src/fallout_shared/modelloader.cpp:20508 |
| 0x004489B0 | LoadAddonNodes | proven | src/fallout_shared/modelloader.cpp:170 |
| 0x00448A90 | LoadAddons | proven | src/fallout_shared/modelloader.cpp:17455 |
| 0x00447080 | LoadFile | proven | src/fallout_shared/modelloader.cpp:9134 |
| 0x004471C0 | LoadKF | proven | src/fallout_shared/modelloader.cpp:5089 |
| 0x00443270 | OutputModelMapContents | proven | src/fallout_shared/modelloader.cpp:9553 |
| 0x00442600 | ProcessQueuedFile | probable | src/fallout_shared/modelloader.cpp:76 |
| 0x00445A10 | QueueAnimations | proven | src/fallout_shared/modelloader.cpp:16879 |
| 0x00444DC0 | QueueBoundObject | proven | src/fallout_shared/modelloader.cpp:9062 |
| 0x004457D0 | QueueCreatureParts | proven | src/fallout_shared/modelloader.cpp:12840 |
| 0x00447A40 | QueueFaceGenFile | proven | src/fallout_shared/modelloader.cpp:9216 |
| 0x004450C0 | QueueHelmet | proven | src/fallout_shared/modelloader.cpp:16556 |
| 0x00446500 | QueueKFList | proven | src/fallout_shared/modelloader.cpp:44 |
| 0x00443DC0 | QueueModel | proven | src/fallout_shared/modelloader.cpp:19777 |
| 0x004440D0 | QueueModel | proven | src/fallout_shared/modelloader.cpp:16291 |
| 0x00444350 | QueueModel | proven | src/fallout_shared/modelloader.cpp:16386 |
| 0x004463B0 | QueueModelList | proven | src/fallout_shared/modelloader.cpp:12892 |
| 0x00444850 | QueueReference | proven | src/fallout_shared/modelloader.cpp:12487 |
| 0x004465F0 | QueueReplacementKFList | proven | src/fallout_shared/modelloader.cpp:17093 |
| 0x004436C0 | QueueTexture | proven | src/fallout_shared/modelloader.cpp:20076 |
| 0x00443AF0 | QueueTexture | proven | src/fallout_shared/modelloader.cpp:19678 |
| 0x004445C0 | QueueTreeModel | proven | src/fallout_shared/modelloader.cpp:12230 |
| 0x00445370 | ReleaseKF | proven | src/fallout_shared/modelloader.cpp:12596 |
| 0x00445300 | ReleaseModel | proven | src/fallout_shared/modelloader.cpp:1760 |
| 0x00443540 | ReuseQueuedTexture | proven | src/fallout_shared/modelloader.cpp:8912 |
| 0x00448920 | TryAndRemoveModel | proven | src/fallout_shared/modelloader.cpp:1929 |
| 0x00446E30 | UpdateLoadingStatusCallback | decomp | src/fallout_shared/modelloader.cpp:99 |
| 0x00446B50 | UpdateQueuedReferencePriorities | proven | src/fallout/ai/actor.cpp:46561 |
| 0x00442AA0 | ~ModelLoader | proven | src/fallout_shared/modelloader.cpp:19439 |

### QueuedActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004411D0 | QueuedActor | proven | src/fallout_shared/modelloader.cpp:1302 |
| 0x004412E0 | QueueDismemberedLimbLoads | class | src/fallout_shared/modelloader.cpp:7942 |

### QueuedCharacter (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004414C0 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3565 |
| 0x00441800 | Attach | class | src/fallout_shared/modelloader.cpp:6 |
| 0x004418B0 | AttachHeadParts | proven | src/fallout_shared/modelloader.cpp:1531 |
| 0x004416C0 | BackgroundClone | proven | src/fallout_shared/modelloader.cpp:20771 |
| 0x00441440 | QueuedCharacter | proven | src/fallout_shared/modelloader.cpp:1353 |

### QueuedCreature (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00441950 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:6038 |
| 0x00441920 | QueuedCreature | proven | src/fallout_shared/modelloader.cpp:6484 |

### QueuedFaceGenFile (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00442010 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3634 |
| 0x00441F80 | QueuedFaceGenFile | proven | src/fallout_shared/modelloader.cpp:4374 |
| 0x004420B0 | QueuedFaceGenFile | proven | src/fallout_shared/modelloader.cpp:12112 |
| 0x00442130 | QueuedFaceGenFile | proven | src/fallout_shared/modelloader.cpp:6595 |

### QueuedHead (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043EB80 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3542 |
| 0x0043ED90 | Attach | proven | src/fallout_shared/modelloader.cpp:15014 |
| 0x0043EC20 | DispatchToManager | class | src/fallout_shared/modelloader.cpp:125 |
| 0x0043EC60 | OnChildCompletion | class | src/fallout_shared/modelloader.cpp:143 |
| 0x0043EAF0 | QueuedHead | proven | src/fallout_shared/modelloader.cpp:4191 |
| 0x0043ECB0 | Run | proven | src/fallout_shared/modelloader.cpp:4259 |

### QueuedHelmet (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043F030 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:10259 |
| 0x0043FB80 | Attach | proven | src/fallout_shared/modelloader.cpp:10349 |
| 0x0043FC10 | FormatQueuedHelmetDescription | class | src/fallout_shared/modelloader.cpp:6433 |
| 0x0043F2B0 | FUN_0043f2b0 | class | src/fallout_shared/modelloader.cpp:10293 |
| 0x0043EFF0 | PostProcess | proven | src/fallout_shared/modelloader.cpp:5485 |
| 0x0043EF10 | QueuedHelmet | proven | src/fallout_shared/modelloader.cpp:11492 |
| 0x0043F240 | UpdateFaceGenModels | class | src/fallout_shared/modelloader.cpp:9772 |

### QueuedPlayer (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00441B50 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3611 |
| 0x00441C30 | Attach | class | src/fallout_shared/modelloader.cpp:12 |
| 0x00441B20 | QueuedPlayer | proven | src/fallout_shared/modelloader.cpp:1564 |
| 0x00441BA0 | QueueModels | proven | src/fallout_shared/modelloader.cpp:4312 |

### QueuedReference (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043FE10 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:10377 |
| 0x00440A90 | BackgroundClone | proven | src/fallout_shared/modelloader.cpp:7779 |
| 0x00440BA0 | DoAttach | proven | src/fallout_shared/modelloader.cpp:7857 |
| 0x00441B80 | FUN_00441b80 | unnamed | src/fallout_shared/modelloader.cpp:223 |
| 0x0043FDF0 | ProcessLoadedAnimIdle | class | src/fallout_shared/modelloader_h_unit.cpp: |
| 0x0043FD40 | QueuedReference | proven | src/fallout_shared/modelloader.cpp:11609 |
| 0x00440050 | QueueModels | proven | src/fallout_shared/modelloader.cpp:7369 |

### ReanimateEffect (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00827340 | CheckTarget | proven | src/fallout/magic/reanimateeffect.cpp:1948 |
| 0x008266A0 | Clone | proven | src/fallout/magic/reanimateeffect.cpp:374 |
| 0x00827440 | GetSaveSize | proven | src/fallout/magic/reanimateeffect.cpp:14 |
| 0x008265B0 | ReanimateEffect | proven | src/fallout/magic/reanimateeffect.cpp:1997 |
| 0x008276E0 | Revert | proven | src/fallout/magic/reanimateeffect.cpp:256 |
| 0x008274A0 | SaveGame | proven | src/fallout/magic/reanimateeffect.cpp:323 |
| 0x00826BE0 | Update | proven | src/fallout_shared/packagelocation.cpp:1118 |

### SummonCreatureEffect (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00828560 | 'scalar deleting destructor' | proven | src/fallout/magic/summoncreatureeffect.cpp:16 |
| 0x00828F00 | CheckSummonLocation | proven | src/fallout/magic/summoncreatureeffect_o2_variant_od_oy_noo2_variant.cpp:603 |
| 0x00829720 | GetSaveSize | proven | src/fallout/magic/summoncreatureeffect.cpp:48 |
| 0x00829900 | InitLoadGame | proven | src/fallout/magic/summoncreatureeffect.cpp:2219 |
| 0x008297A0 | SaveGame | proven | src/fallout/magic/summoncreatureeffect.cpp:1476 |
| 0x008287E0 | Start | proven | src/fallout/magic/summoncreatureeffect.cpp:544 |
| 0x00828470 | SummonCreatureEffect | proven | src/fallout/magic/summoncreatureeffect.cpp:628 |
| 0x00828BA0 | Update | proven | src/fallout/magic/summoncreatureeffect.cpp:1221 |
| 0x00828590 | ~SummonCreatureEffect | proven | src/fallout/magic/summoncreatureeffect.cpp:148 |

### TeleportableReference (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3BB0 | GetTeleportDestinationForm | decomp | src/fallout_shared/teleportdata.cpp:12 |

### TESDataHandler (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004603B0 | AddFormToDataHandler | proven | src/fallout_shared/tesdatahandler.cpp:335 |
| 0x004698A0 | CreateReferenceAtLocation | proven | src/fallout_shared/tesdatahandler.cpp:6379 |

### TESObjectREFR (36)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0056AAC0 | CheckEnableParentLoop | proven | src/fallout_shared/extradatalist.cpp:8551 |
| 0x00574400 | Disable | proven | src/fallout_shared/pathfinding/pathingdebuggeometry.cpp:592 |
| 0x00573F40 | Enable | proven | src/fallout_shared/tesobjectrefr.cpp:44617 |
| 0x00546A90 | FindEncounterZone | probable | src/fallout_shared/tesobjectrefr.cpp:11 |
| 0x0057ADA0 | FixAttachedBSObjectSizeAndTransform | proven | src/fallout_shared/tesobjectrefr.cpp:45966 |
| 0x0055F880 | GetAttachedAnimationSaveSize | proven | src/fallout_shared/tesobjectrefr.cpp:15361 |
| 0x0056AC90 | GetEnableStateChildList | proven | src/fallout_shared/tesobjectrefr.cpp:8559 |
| 0x0056A9F0 | GetEnableStateParent | proven | src/fallout_shared/tesobjectrefr.cpp:48349 |
| 0x00567D20 | GetEncounterZone | proven | src/bgsencounterzone.cpp:127 |
| 0x00567D90 | GetLocationEncounterZone | proven | src/staging/blk_00560000_od.cpp:611 |
| 0x0056AE60 | GetRespawn | proven | src/staging/blk_00560000_od.cpp:1876 |
| 0x0056AFC0 | HasLeveledCreatureCalced | proven | src/staging/blk_00560000_od.cpp:2991 |
| 0x005768B0 | InitHavok | proven | src/fallout_shared/tesobjectrefr_o2_variant_od_oy_noo2_variant.cpp:3219 |
| 0x0056EAB0 | InitHavokForCollisionObject | proven | src/fallout_shared/tesobjectrefr.cpp:42987 |
| 0x0056C8F0 | InitHavokForPlaceableWater | proven | src/fallout_shared/tesobjectrefr.cpp:42368 |
| 0x0056D7E0 | InitHavokForPrimitiveTrigger | proven | src/staging/blk_00560000_o2_od_oy_noo2_variant.cpp:475 |
| 0x0055D760 | InitItem | proven | src/fallout_shared/tesobjectrefr.cpp:24420 |
| 0x0056AF40 | IsLeveledCreature | proven | src/fallout_shared/extradatalist.cpp:5705 |
| 0x0056B2D0 | Load3D | proven | src/fallout_shared/tesobjectrefr.cpp:31139 |
| 0x00561EF0 | MoveToEditorLocation | proven | src/fallout_shared/tesobjectrefr.cpp:18529 |
| 0x00563890 | ResetAnimation | proven | src/fallout_shared/tesobjectrefr.cpp:40077 |
| 0x0055F970 | ResetAttachedAnimation | proven | src/fallout_shared/tesobjectrefr.cpp:26180 |
| 0x00574920 | ResetInventory | proven | src/fallout_shared/tesobjectrefr.cpp:14484 |
| 0x0080FCF0 | ResetProjectileIdleAnimation | decomp | src/fallout/magic/magicballprojectile.cpp:1261 |
| 0x0056B0B0 | RestoreLeveledCreatureOriginalBase | proven | src/fallout_shared/tesobjectrefr.cpp:3138 |
| 0x0055F900 | SaveAttachedAnimation | proven | src/fallout_shared/tesobjectrefr.cpp:25894 |
| 0x005702E0 | Set3D | proven | src/fallout_shared/modelloader.cpp:18855 |
| 0x00570F70 | Set3DSimple | proven | src/fallout_shared/tesobjectrefr.cpp:43558 |
| 0x00571080 | Set3DVerySimple | proven | src/fallout_shared/tesobjectrefr.cpp:3733 |
| 0x00564930 | SetDelete | proven | src/fallout_shared/tesobjectrefr.cpp:1818 |
| 0x0056AA10 | SetEnableStateParent | proven | src/fallout_shared/tesobjectrefr.cpp:14909 |
| 0x00567DD0 | SetEncounterZone | proven | src/fallout_shared/tesobjectrefr.cpp:2554 |
| 0x0056B020 | SetLeveledCreature | proven | src/staging/blk_00560000_od.cpp:2875 |
| 0x00575830 | SetLocationOnReference | proven | src/fallout/misc/saveload/bgssaveloadgame.cpp:2089 |
| 0x00572B60 | SetStartingPosition | proven | src/fallout_shared/tesobjectrefr.cpp:32308 |
| 0x0056AC00 | UpdateEnableStateChildrenFlagsRecursive | proven | src/staging/blk_00560000_od.cpp:1264 |

### TESQueuedCellManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00528540 | FUN_00528540 | probable | src/staging/blk_00520000_od.cpp:90 |

### (free functions) (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F8BF0 | CalcLeveledCreature | class | src/fallout_shared/tesobject.cpp:2109 |
| 0x008289E0 | CleanupSummonedCreature | class | src/fallout/magic/summoncreatureeffect.cpp:978 |
| 0x005C4B30 | PlaceAtMe | proven | src/fallout_shared/tesscriptfunctions_o2_variant_od_oy_noo2_nogf_variant.cpp:987 |
| 0x008D1670 | UpdateDoorSpawn | class | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:237 |

## 2 Actor references (the NPC in the world)

Actor, Character, Creature and MobileObject: the live NPC object.

### Actor (207)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087D830 | 'scalar deleting destructor' | proven | src/fallout/ai/actor.cpp:33796 |
| 0x0087D4A0 | Actor | proven | src/fallout/ai/actor.cpp:18985 |
| 0x0087EEF0 | AddDeathItems | proven | src/fallout/ai/actor.cpp:47788 |
| 0x008C2E50 | AddDefaultSpells | decomp | src/fallout/ai/actor_magic.cpp:123 |
| 0x008B8E20 | AddFaction | proven | src/fallout/ai/actor.cpp:11360 |
| 0x008B7D20 | AddFactionMajorCrime | proven | src/fallout/ai/actor.cpp:81596 |
| 0x008B7C00 | AddFactionMinorCrime | proven | src/fallout/ai/actor.cpp:81541 |
| 0x008BC790 | AddFollower | proven | src/fallout/ai/actor.cpp:13956 |
| 0x0088DB20 | AddWornItem | proven | src/fallout_shared/tesobjectrefr.cpp:49845 |
| 0x008855F0 | AdjustSpeedForFollowing | proven | src/staging/blk_00880000_od.cpp:2334 |
| 0x008AAF40 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/actor.cpp:72803 |
| 0x008A1A70 | ApplyCriticalStage | proven | src/fallout/ai/actor.cpp:25688 |
| 0x008B4D10 | ApplyEffectToBodyParts | decomp | src/fallout_shared/tescreature.cpp:3328 |
| 0x008C0460 | AttackAlarm | proven | src/fallout/ai/actor.cpp:124651 |
| 0x00894D90 | BlockHit | proven | src/fallout/ai/actor.cpp:61485 |
| 0x008B3880 | BuildRequest | proven | src/fallout/ai/actor.cpp:10402 |
| 0x00885020 | CalculateCachedRadius | proven | src/fallout/ai/actor.cpp:32030 |
| 0x008ACBE0 | CalculateCombatStrength | proven | src/fallout/ai/actor.cpp:9265 |
| 0x008B0670 | CanAttackActor | proven | src/fallout/ai/actor.cpp:39859 |
| 0x008845A0 | CanKnockDown | proven | src/fallout/ai/actor.cpp:2988 |
| 0x008843A0 | CanMove | proven | src/fallout/ai/actor.cpp:2361 |
| 0x00884480 | CanSpeak | proven | src/fallout/ai/actor.cpp:2409 |
| 0x008B2010 | CanUseIdle | proven | src/fallout/ai/actor.cpp:30083 |
| 0x008BC9D0 | CanUseWeapon | proven | src/fallout/ai/actor.cpp:87933 |
| 0x008C1320 | CleanUpPointersOnDisable | proven | src/fallout/ai/actor.cpp:15161 |
| 0x0087FAD0 | ClearDisposition | proven | src/fallout/ai/actor.cpp:1489 |
| 0x008B3D30 | ClearLookAtTarget | proven | src/fallout/ai/actor.cpp:10810 |
| 0x008B9240 | ConditionModifiedCallback | proven | src/fallout/ai/actor.cpp:124050 |
| 0x008C3C40 | ConfigureActorState | decomp | src/fallout/ai/actor_magic.cpp:161 |
| 0x0087D890 | ConstructorInitialize | proven | src/staging/blk_00860000_od.cpp:6829 |
| 0x008BC860 | CouldBeFollowing | proven | src/fallout/ai/actor.cpp:45368 |
| 0x008B6AE0 | CreateDismemberedLimbs | proven | src/fallout/ai/actor.cpp:149830 |
| 0x0089D6F0 | DamageHealthAndFatigue | proven | src/fallout/ai/actor.cpp:105644 |
| 0x00891360 | DamageItem | proven | src/fallout/ai/actor.cpp:102879 |
| 0x008B3B90 | DidPathingFail | proven | src/fallout/ai/actor.cpp:10455 |
| 0x008B52A0 | DismemberLimb | proven | src/fallout/ai/actor.cpp:139265 |
| 0x008B43A0 | DismemberLimbs | proven | src/fallout/ai/actor.cpp:130606 |
| 0x008C2B60 | DispelPermanentMagic | proven | src/fallout/ai/actor_magic.cpp:4602 |
| 0x00890610 | DoTrap | proven | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:1248 |
| 0x008929A0 | DropItem | proven | src/fallout/ai/actor.cpp:103374 |
| 0x008B1070 | EndDialogue | proven | src/fallout/ai/actor.cpp:77240 |
| 0x00881680 | EndInterruptPackage | proven | src/fallout/ai/actor.cpp:20970 |
| 0x008990F0 | FindMeleeTarget | proven | src/fallout/ai/actor.cpp:64791 |
| 0x008AA9A0 | FinishInitLoadGameTES | proven | src/fallout/ai/actor.cpp:123018 |
| 0x008ABFE0 | FinishLoadGame | proven | src/fallout/ai/actor.cpp:28940 |
| 0x008A7A90 | ForceIdleAnimation | proven | src/fallout/ai/actor.cpp:121854 |
| 0x008B3AD0 | ForceStopMoving | proven | src/fallout_shared/tesobjectrefr.cpp:6906 |
| 0x00571760 | FUN_00571760 | unnamed | src/fallout_shared/tesobjectrefr.cpp:37238 |
| 0x00884C60 | FUN_00884c60 | unnamed | src/staging/blk_00880000_od.cpp:13 |
| 0x0096C950 | FUN_0096c950 | unnamed | src/fallout/ai/processlists.cpp:278 |
| 0x009B90B0 | FUN_009b90b0 | probable | src/fallout/ai/combat/missileprojectile_o2_variant_od_oy_noo2_variant.cpp:1360 |
| 0x004181E0 | GetActorBase | probable | src/fallout/ai/actor.cpp:6 |
| 0x008A7570 | GetAnimAction | proven | src/fallout/ai/actor.cpp:8116 |
| 0x008B70D0 | GetAnimData | proven | src/fallout/ai/actor.cpp:11012 |
| 0x00897910 | GetAnimGroup | proven | src/fallout/ai/actor.cpp:104038 |
| 0x00897B50 | GetAnimGroupDuration | proven | src/fallout/ai/actor.cpp:44076 |
| 0x008B3B30 | GetAnticipatedLocation | proven | src/fallout/ai/character.cpp:154 |
| 0x0087D7F0 | GetBaseLevel | class | src/fallout/ai/actor_h_unit.cpp: |
| 0x00891CE0 | GetBestAmmo | proven | src/fallout/ai/actor.cpp:36813 |
| 0x00884350 | GetClass | proven | src/fallout/ai/actor.cpp:2330 |
| 0x008A02D0 | GetCombatController | proven | src/fallout/ai/actor.cpp:115026 |
| 0x008A7F80 | GetCombatStyle | proven | src/fallout/ai/actor.cpp:70935 |
| 0x0087FD90 | GetDisposition | proven | src/fallout/ai/actor.cpp:111508 |
| 0x0087FCB0 | GetDispositionModifierTowardActor | proven | src/fallout/ai/actor.cpp:1525 |
| 0x0087F920 | GetEditorLocation | proven | src/fallout_shared/tesobjectrefr.cpp:15149 |
| 0x0087F7A0 | GetEditorLocationInteriorCell | proven | src/fallout/ai/actor.cpp:707 |
| 0x0087F750 | GetEditorLocationWorld | proven | src/fallout/ai/actor.cpp:687 |
| 0x0087F3D0 | GetEssential | proven | src/fallout/ai/actor.cpp:527 |
| 0x008BE940 | GetEyeLevel | proven | src/fallout/ai/actor.cpp:14787 |
| 0x008ADCB0 | GetFaceAnimationData | proven | src/fallout/ai/actor.cpp:9704 |
| 0x008B7FE0 | GetFactionReaction | proven | src/fallout/ai/actor.cpp:123638 |
| 0x00893530 | GetFatiguePercentage | proven | src/fallout/ai/actor.cpp:4861 |
| 0x008ACE90 | GetGhost | proven | src/fallout/ai/actor.cpp:9313 |
| 0x00884560 | GetHasKnockedState | proven | src/fallout/ai/actor.cpp:2713 |
| 0x00893590 | GetHealthPercentage | proven | src/fallout/ai/actor.cpp:4887 |
| 0x008853A0 | GetHeight | proven | src/fallout/ai/actor.cpp:32243 |
| 0x0087D650 | GetIgnoreCrime | proven | src/fallout/ai/actor.cpp:32816 |
| 0x0087D750 | GetIsImmobileCreature | proven | src/fallout/ai/actor.cpp:406 |
| 0x0087F9F0 | GetLevel | proven | src/fallout/ai/actor.cpp:962 |
| 0x004F8960 | GetLifeState | proven | src/fallout/ai/actor.cpp:299 |
| 0x0087D6F0 | GetMagicCaster | class | src/fallout/ai/actor_h_unit.cpp: |
| 0x00952FF0 | GetMagicCaster | class | src/fallout/ai/actor_h_unit.cpp: |
| 0x008A0C20 | GetMaxCarryWeight | proven | src/fallout/ai/actor.cpp:5481 |
| 0x008A8290 | GetMovementPosition | class | src/fallout/ai/actor_h_unit.cpp: |
| 0x0088D640 | GetOutofFurnitureQuick | proven | src/fallout/ai/actor.cpp:23474 |
| 0x00881450 | GetPackage | proven | src/fallout/ai/actor.cpp:1655 |
| 0x00881650 | GetPackageTarget | proven | src/fallout/ai/actor.cpp:2044 |
| 0x008BE0A0 | GetProjectileNode | proven | src/fallout/ai/actor.cpp:110218 |
| 0x0087F4A0 | GetRespawn | proven | src/staging/blk_00860000_od.cpp:2501 |
| 0x008A9020 | GetSaveSize | proven | src/fallout/ai/actor.cpp:72147 |
| 0x0087F4C0 | GetSex | decomp | src/bscore/memorymanager.cpp:73 |
| 0x008B0970 | GetShouldHelp | proven | src/fallout/ai/actor.cpp:123518 |
| 0x0087D690 | GetSkillAdvanceDelayed | proven | src/fallout/ai/actor.cpp:32827 |
| 0x008AE600 | GetTemplateActorBase | proven | src/fallout/ai/actor.cpp:9718 |
| 0x008BDBD0 | GetVATSTargetVisible | proven | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:3430 |
| 0x00888AC0 | HandleRunDetection | proven | src/fallout/ai/actor.cpp:4254 |
| 0x0087F900 | HasEditorLocation | proven | src/fallout/ai/actor.cpp:927 |
| 0x008B8490 | HasFactionThatCaresAboutCrime | proven | src/fallout/ai/actor.cpp:81798 |
| 0x008982C0 | InitiateAvoidPackage | proven | src/fallout/ai/actor.cpp:42525 |
| 0x008B2170 | InitiateDialogue | proven | src/fallout/ai/actor.cpp:78132 |
| 0x008BBF40 | InitiateUseWeaponPackage | proven | src/fallout/ai/actor.cpp:100181 |
| 0x008ABC40 | InitLoadGame | proven | src/fallout/ai/actor.cpp:123446 |
| 0x008AA4C0 | InitLoadGameTES | proven | src/fallout/ai/actor.cpp:142265 |
| 0x00893340 | InitPackageLocations | proven | src/fallout/ai/actor.cpp:24048 |
| 0x008B8CA0 | IntegrateFactionLists | proven | src/fallout/ai/actor.cpp:11262 |
| 0x008BA2F0 | InventoryWeightModifiedCallback | proven | src/fallout/ai/actor.cpp:12011 |
| 0x008C1B30 | IsActorRefEssential | proven | src/fallout/ai/actor.cpp:15533 |
| 0x00884B50 | IsAllowedToSwim | proven | src/staging/blk_00880000_od.cpp:2198 |
| 0x008BFFC0 | IsAngryWithPlayer | proven | src/fallout/ai/actor.cpp:15130 |
| 0x008B2F90 | IsAtPoint | proven | src/bssystem/archive.cpp:323 |
| 0x008A8300 | IsCloseToGround | proven | src/fallout/ai/actor.cpp:115261 |
| 0x008844F0 | IsDead | proven | src/fallout/ai/actor.cpp:2427 |
| 0x0087D6A0 | IsDying | proven | src/fallout/ai/actor.cpp:398 |
| 0x00884110 | IsEscorterBehind | proven | src/fallout/ai/actor.cpp:54405 |
| 0x00493BB0 | IsInCombat | proven | src/fallout/ai/playercharacter.cpp:1304 |
| 0x008BC700 | IsInCombatWithActor | proven | src/fallout/ai/actor.cpp:13899 |
| 0x008B8E90 | IsInFaction | proven | src/fallout/ai/actor.cpp:18520 |
| 0x008849C0 | IsJumping | proven | src/fallout/ai/actor.cpp:54586 |
| 0x004938E0 | IsMoving | proven | src/fallout/ai/actor.cpp:277 |
| 0x008A3B30 | IsMoving | decomp | src/fallout/ai/actor_h_unit.cpp: |
| 0x008BE4F0 | IsParalyzed | proven | src/fallout_shared/tesobjectrefr.cpp:7027 |
| 0x00885520 | IsPointDeepUnderWater | proven | src/fallout/ai/actor.cpp:3801 |
| 0x0088C570 | IsPointInViewCone | proven | src/fallout/ai/actor.cpp:17265 |
| 0x00608D80 | IsReanimated | proven | src/fallout_shared/tesnpc.cpp:1835 |
| 0x008A8870 | IsReloading | proven | src/fallout/ai/actor.cpp:39546 |
| 0x00437BF0 | IsRestrained | proven | src/fallout_shared/extradataobjects.cpp:1367 |
| 0x004997B0 | IsSneaking | proven | src/fallout/ai/actor_h_unit.cpp: |
| 0x005A2030 | IsSwimming | proven | src/fallout_shared/tesconditionfunctions.cpp:2875 |
| 0x00437BD0 | IsUnConscious | proven | src/fallout_shared/extradataobjects.cpp:1354 |
| 0x008B0190 | IsVisible | decomp | src/fallout/ai/mobileobject.cpp:51 |
| 0x008A16D0 | IsWeaponDrawn | proven | src/fallout/ai/actor.cpp:5813 |
| 0x0088B880 | LineOfSight | proven | src/fallout/ai/actor_magic.cpp:7372 |
| 0x0087E060 | Load3D | proven | src/fallout_shared/tesobjectrefr.cpp:22101 |
| 0x008AB3A0 | LoadGame | proven | src/fallout/ai/actor_rtm_variant.cpp:1556 |
| 0x008A9940 | LoadGame2 | proven | src/fallout/ai/actor.cpp:137589 |
| 0x00880C70 | ModActorValueInt | proven | src/fallout/ai/actor.cpp:49088 |
| 0x0087FB40 | ModDisposition | proven | src/fallout/ai/actor.cpp:116172 |
| 0x008B86E0 | ModFactionRank | proven | src/fallout/ai/actor.cpp:40271 |
| 0x008AD1C0 | MoveActorAndFollowers | proven | src/fallout/ai/actor.cpp:143756 |
| 0x008AD910 | MoveActorAndFollowers | proven | src/fallout/ai/actor.cpp:9486 |
| 0x00882B90 | MoveToLow | proven | src/fallout/ai/actor.cpp:112511 |
| 0x008AC680 | OffersServicesPackage | proven | src/fallout/ai/actor.cpp:145762 |
| 0x00895110 | PickAnimations | proven | src/fallout/ai/actor.cpp:97776 |
| 0x008C00E0 | PickpocketAlarm | proven | src/fallout/ai/actor_rtti_variant_decl_variant.cpp:378 |
| 0x00891E00 | PickUpObject | proven | src/fallout/ai/actor_magic.cpp:3118 |
| 0x00886360 | Process | proven | src/fallout/ai/actor.cpp:136084 |
| 0x0088D2F0 | PutActorInChairBedQuick | proven | src/fallout/ai/actor.cpp:118403 |
| 0x0087EAC0 | PutCreatedPackage | proven | src/fallout/ai/actor.cpp:115843 |
| 0x00892E90 | PutItemInReference | proven | src/fallout/ai/actor.cpp:119231 |
| 0x008B7360 | QueueReplacementLocomotion | proven | src/fallout/ai/actor.cpp:81398 |
| 0x008B73F0 | QueueReplacementLocomotion | proven | src/fallout/ai/actor.cpp:109840 |
| 0x008B78C0 | QueueReplacementLocomotions | proven | src/fallout/ai/actor.cpp:81460 |
| 0x00894E90 | Recoil | proven | src/fallout/ai/actor.cpp:61860 |
| 0x008A83C0 | Reload2 | proven | src/fallout/ai/actor.cpp:8863 |
| 0x008C3400 | RemoveSpell | proven | src/fallout/ai/actor.cpp:89841 |
| 0x0088E110 | RemoveWornItem | proven | src/fallout/ai/actor.cpp:145016 |
| 0x008BB520 | RequestRotate | proven | src/fallout/ai/actor.cpp:13448 |
| 0x00887D00 | ResetLoadedAnimations | proven | src/fallout/ai/actor.cpp:117885 |
| 0x008A0960 | RestoreFullHealthAndConditions | proven | src/fallout/ai/actor.cpp:120107 |
| 0x0087D810 | SetActorEssentialState | class | src/fallout/ai/mobileobject.cpp:57 |
| 0x008A1800 | SetActorLifeState | decomp | src/fallout/ai/actor_magic.cpp:85 |
| 0x00880700 | SetActorValue | proven | src/fallout/ai/actor.cpp:19925 |
| 0x008806D0 | SetActorValueInt | proven | src/fallout/ai/actor.cpp:35541 |
| 0x008A5E40 | SetAlert | proven | src/fallout/ai/actor.cpp:6782 |
| 0x008C4790 | SetAlpha | class | src/fallout/ai/actor_magic.cpp:36 |
| 0x00961DE0 | SetAlphaAndFade | class | src/fallout/ai/actor_magic.cpp:43 |
| 0x00920FB0 | SetCurrentSitSleepState | decomp | src/fallout/ai/mobileobject.cpp:119 |
| 0x008B8580 | SetFactionRank | proven | src/fallout/ai/actor.cpp:81852 |
| 0x008ACF10 | SetGhost | proven | src/fallout/ai/actor.cpp:39797 |
| 0x008A6A00 | SetHeading | proven | src/fallout/ai/actor.cpp:7844 |
| 0x0087D5E0 | SetHeadingToRef | proven | src/fallout/ai/actor.cpp:33772 |
| 0x0087D630 | SetIgnoreCrime | proven | src/fallout/ai/actor.cpp:33783 |
| 0x00881D10 | SetLastSeenTime | proven | src/fallout/ai/actor.cpp:33857 |
| 0x008B39F0 | SetMoveMode | proven | src/fallout/ai/actor.cpp:10425 |
| 0x008B3690 | SetPathfindingGoal | proven | src/fallout/ai/actor.cpp:10119 |
| 0x008B36F0 | SetPathfindingGoal | proven | src/fallout/ai/actor.cpp:79532 |
| 0x008BCA90 | SetPlayerTeammate | proven | src/fallout/ai/actor.cpp:44180 |
| 0x008BC750 | SetRunOnceExtraPackage | proven | src/fallout/ai/actor.cpp:13939 |
| 0x008ACE10 | SetUnConscious | proven | src/fallout/ai/actor.cpp:9291 |
| 0x008B1910 | SetUpTalkingActivatorActor | proven | src/fallout/ai/character.cpp:451 |
| 0x00884F80 | SetWalkRunFlagDirty | proven | src/fallout/ai/actor.cpp:3532 |
| 0x008A6840 | SetWantWeaponDrawn | proven | src/fallout/ai/actor.cpp:27786 |
| 0x00881C90 | ShouldReset | proven | src/fallout/ai/actor.cpp:2067 |
| 0x008A78F0 | ShouldSkipFallOutBehavior | proven | src/fallout/ai/actor.cpp:8531 |
| 0x00893190 | ShouldTalkTo | proven | src/fallout/ai/actor.cpp:59626 |
| 0x008A8DD0 | ShouldUseAmmo | proven | src/fallout/ai/actor.cpp:39574 |
| 0x008A20D0 | SpeakSoundFunction | proven | src/fallout/ai/actor.cpp:137217 |
| 0x00893A40 | StartAttack | proven | src/fallout/ai/actor.cpp:147318 |
| 0x00881D30 | StartHighProcess | proven | src/fallout/ai/actor.cpp:101624 |
| 0x008BFA40 | StealAlarm | proven | src/staging/blk_008a0000_od.cpp:3202 |
| 0x008A8E50 | StopAttack | proven | src/fallout/ai/actor.cpp:28461 |
| 0x008A06C0 | StopCombat | proven | src/fallout/ai/actor.cpp:25339 |
| 0x008B3AB0 | StopMoving | proven | src/fallout/ai/actor.cpp:10442 |
| 0x0087F570 | SwimsOnly | proven | src/fallout/ai/actor.cpp:657 |
| 0x008A7D50 | TriggerPain | proven | src/fallout/ai/actor.cpp:121987 |
| 0x008B64E0 | UnhideDismemberedLimb | proven | src/fallout/ai/actor.cpp:141392 |
| 0x008C30A0 | UnloadPermanentMagic | proven | src/fallout/ai/actor_magic.cpp:4732 |
| 0x00888B50 | Update | proven | src/fallout/ai/actor.cpp:133973 |
| 0x00888070 | UpdateActorMovement | class | src/fallout/ai/actor_h_unit.cpp: |
| 0x008C4640 | UpdateActorPresentation | decomp | src/fallout/ai/actor_magic.cpp:53 |
| 0x008885E0 | UpdateAnimationMovement | proven | src/fallout/ai/actor.cpp:96350 |
| 0x008A03A0 | UpdateCombat | proven | src/fallout/ai/actor.cpp:120029 |
| 0x008B65F0 | UpdateDismemberedLimbVel | proven | src/fallout/ai/actor.cpp:141630 |
| 0x008A5580 | UpdateInDialogue | proven | src/fallout/ai/actor.cpp:99507 |
| 0x00888970 | UpdateRagdollAnimation | proven | src/fallout/ai/actor.cpp:44231 |
| 0x008BCDF0 | UpdateRagdollAnimState | proven | src/fallout/ai/actor.cpp:135428 |
| 0x0088B4E0 | UpdateRefLight | proven | src/fallout_shared/tesobjectrefr.cpp:6893 |

### ActorPackageUpdate::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00897DE0 | SetTravelPackage | class | src/fallout/ai/actor.cpp:63085 |

### ActorUpdate3D::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00886CB0 | FUN_00886cb0 | class | src/fallout/ai/actor_rtm_variant.cpp:820 |

### ActorValue (16)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0066EE50 | CheckCallModifiedCallback | proven | src/fallout_shared/actorvalue.cpp:287 |
| 0x0066F190 | ClampActorValue | proven | src/fallout_shared/actorvalue.cpp:190 |
| 0x0066E920 | GetActorValueInfo | proven | src/fallout_shared/actorvalue.cpp:512 |
| 0x0066E950 | GetActorValueName | proven | src/fallout_shared/actorvalue.cpp:252 |
| 0x0066ECF0 | GetCountForSection | decomp | src/fallout_shared/actorvalue.cpp:230 |
| 0x0066EDC0 | GetDependentActorValueIndices | decomp | src/fallout_shared/actorvalue.cpp:317 |
| 0x00406D70 | GetFlag | proven | src/fallout_shared/magic/effectitemlist.cpp:135 |
| 0x0066FD20 | GetSection | decomp | src/fallout_shared/actorvalue.cpp:443 |
| 0x0066EE10 | HasActorValueChangedCallback | decomp | src/fallout_shared/actorvalue.cpp:340 |
| 0x0066FDC0 | IsAIAttribute | decomp | src/fallout_shared/actorvalue.cpp:505 |
| 0x0066FD90 | IsDerivedAttribute | decomp | src/fallout_shared/actorvalue.cpp:498 |
| 0x0047F060 | IsSkill | proven | src/fallout_shared/tesaiform.cpp:345 |
| 0x0066F260 | LoadActorValueDefinitions | decomp | src/fallout_shared/actorvalue.cpp:7 |
| 0x0066EFE0 | RegisterActorValue | decomp | src/fallout_shared/actorvalue.cpp:379 |
| 0x0066EC10 | ToActorValue | proven | src/fallout_shared/actorvalue.cpp:207 |
| 0x0066EC80 | ToArrayIndex | proven | src/fallout_shared/actorvalue.cpp:457 |

### ActorValueOwner (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F78E0 | ActorValueOwner | proven | src/fallout_shared/tesanimation.cpp:35 |
| 0x005F0FB0 | GetActorValue | decomp | src/fallout_shared/bgsdestructibleobjectform.cpp:115 |
| 0x0066EF50 | GetActorValueFloatByIndex | probable | src/fallout_shared/actorvalue.cpp:332 |
| 0x0066EF20 | GetClampedActorValueI | proven | src/fallout_shared/actorvalue.cpp:347 |
| 0x0066ED60 | GetDerivedActorValue | proven | src/fallout_shared/actorvalue.cpp:271 |
| 0x005F7420 | GetPermanentActorValue | proven | src/fallout_shared/tescreature.cpp:546 |

### ActorValueStore (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C6E90 | ActorValueStore | decomp | src/fallout/ai/actorvaluecache.cpp:6 |
| 0x008C6F00 | FUN_008c6f00 | unnamed | src/fallout/ai/actorvaluecache.cpp:49 |
| 0x008C6F70 | InvalidateDependentValues | decomp | src/fallout/ai/actorvaluecache.cpp:22 |
| 0x008C6F40 | InvalidateValue | decomp | src/fallout/ai/actorvaluecache.cpp:12 |
| 0x008C6EB0 | ResetCacheValues | decomp | src/fallout/ai/actorvaluecache.cpp:37 |

### ActorX (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A62B0 | ApplyFallDamage | class | src/fallout/ai/actor.cpp:69684 |
| 0x008B30F0 | CreateActorSubobject | class | src/fallout/ai/actor.cpp:30134 |
| 0x00911F00 | DispatchToTarget | class | src/fallout/ai/lowprocess.cpp:13354 |
| 0x00887B90 | FUN_00887b90 | class | src/fallout/ai/actor.cpp:22954 |
| 0x0093AA10 | FUN_0093aa10 | class | src/fallout/ai/playercharacter.cpp:3186 |
| 0x00885A50 | GetMovementSpeed | class | src/fallout/ai/actor.cpp:21761 |
| 0x008A2ED0 | GetTargetReference | decomp | src/fallout/ai/actor.cpp:26172 |
| 0x0089FB80 | ResetActorEquipment | class | src/fallout/ai/actor.cpp:24542 |

### CachedValuesOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087D860 | CachedValuesOwner | proven | src/fallout/ai/actor.cpp:33813 |

### Character (21)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D1F10 | 'scalar deleting destructor' | proven | src/fallout/ai/character.cpp:181 |
| 0x008D1D30 | Character | proven | src/staging/blk_008c0000_od.cpp:757 |
| 0x008D1F40 | Character | proven | src/fallout/ai/character.cpp:542 |
| 0x008D34D0 | FinishLoadGame | proven | src/fallout/ai/character.cpp:18 |
| 0x008D4E80 | FUN_008d4e80 | unnamed | src/fallout/ai/actor.cpp:33495 |
| 0x008D1ED0 | GetActorGuard | class | src/fallout/ai/character_h_unit.cpp: |
| 0x008D3110 | GetClothingValue | proven | src/fallout/ai/character_rtti_variant.cpp:2568 |
| 0x008D40E0 | GetIsChildSize | proven | src/fallout/ai/actor.cpp:31660 |
| 0x0087D720 | GetMagicTarget | class | src/fallout/ai/character.cpp:25 |
| 0x008D32B0 | GetSaveSize | proven | src/fallout/ai/character.cpp:212 |
| 0x005D9F90 | GetValidBip01Names | proven | src/fallout_shared/tesobjectrefr.cpp:6535 |
| 0x008D2DB0 | InitiateSandmanPackage | proven | src/fallout/ai/actor.cpp:144573 |
| 0x008D34B0 | InitLoadGame | proven | src/fallout/ai/character.cpp:12 |
| 0x008D3380 | InitLoadGameTES | proven | src/fallout/ai/character.cpp:272 |
| 0x008D33F0 | LoadGame | class | src/fallout/ai/character.cpp:61 |
| 0x008D3310 | LoadGame2 | proven | src/fallout/ai/character.cpp:239 |
| 0x008D3330 | Revert | proven | src/fallout/ai/character.cpp:256 |
| 0x008D32F0 | SaveGame | proven | src/fallout/ai/character.cpp:228 |
| 0x008D1EF0 | SetActorGuardState | class | src/fallout/ai/character_h_unit.cpp: |
| 0x008D29B0 | SetValidBip01Names | proven | src/fallout/ai/actor.cpp:16461 |
| 0x008D3550 | Update | proven | src/fallout/ai/actor.cpp:92586 |

### Creature (13)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D44D0 | 'scalar deleting destructor' | proven | src/fallout/ai/creature.cpp:199 |
| 0x008D4EB0 | CalculateRunSpeed | class | src/fallout/ai/creature.cpp:14 |
| 0x008D4F10 | CalculateRunSpeed | proven | src/fallout/ai/actor.cpp:40943 |
| 0x008D43A0 | Creature | proven | src/fallout_shared/tesdatahandler.cpp:4556 |
| 0x008D4500 | Creature | proven | src/fallout/ai/creature.cpp:76 |
| 0x008D49F0 | DamageActorValue | proven | src/fallout/ai/creature.cpp:303 |
| 0x008D4F70 | GetAnimationSpeedMultiplier | decomp | src/fallout/ai/creature.cpp:24 |
| 0x008D46F0 | GetWeaponSkill | proven | src/fallout/ai/creature.cpp:232 |
| 0x008D4FF0 | LoadGame | class | src/fallout/ai/creature.cpp:6 |
| 0x008D4A80 | MapActorValue | proven | src/fallout/ai/creature.cpp:48 |
| 0x008D4960 | ModActorValueInt | proven | src/fallout/ai/creature.cpp:173 |
| 0x008D48D0 | SetActorValue | proven | src/fallout/ai/creature.cpp:147 |
| 0x008D48A0 | SetActorValueInt | proven | src/fallout/ai/creature.cpp:134 |

### MatchActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A40E0 | FUN_008a40e0 | probable | src/fallout/ai/actor.cpp:108427 |
| 0x008B19C0 | FUN_008b19c0 | class | src/fallout/ai/actor.cpp:109391 |

### MobileObject (49)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092EC10 | 'scalar deleting destructor' | proven | src/fallout/ai/mobileobject.cpp:1240 |
| 0x00931D30 | AdvanceMovement | decomp | src/fallout/ai/mobileobject.cpp:12 |
| 0x00932880 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/mobileobject.cpp:7338 |
| 0x00933D20 | EndDialogue | proven | src/fallout/magic/magicballprojectile.cpp:8122 |
| 0x00932D60 | FinishLoadGame | proven | src/fallout/ai/mobileobject.cpp:925 |
| 0x009306D0 | GetCharController | proven | src/fallout/ai/actor.cpp:16696 |
| 0x004B9930 | GetCharControllerFlag | decomp | src/fallout/ai/mobileobject.cpp:114 |
| 0x009344A0 | GetCurrentPackage | proven | src/fallout/ai/actor.cpp:16893 |
| 0x00931850 | GetCurrentProcessLevel | decomp | src/fallout/ai/movement/actormover.cpp:30 |
| 0x009334B0 | GetDesiredProcessLevel | proven | src/fallout/ai/mobileobject.cpp:1135 |
| 0x00931F30 | GetLinearVelocity | proven | src/fallout/ai/actor.cpp:113489 |
| 0x00931D70 | GetLooking | decomp | src/fallout/ai/mobileobject.cpp:18 |
| 0x00933630 | GetMinBounds | proven | src/fallout/ai/mobileobject.cpp:12794 |
| 0x008AE4C0 | GetPos | class | src/fallout/ai/mobileobject_h_unit.cpp: |
| 0x00437BB0 | GetRunsInLow | proven | src/fallout_shared/extradataobjects.cpp:1343 |
| 0x00931FF0 | GetSaveSize | proven | src/fallout/ai/mobileobject.cpp:6467 |
| 0x005A4520 | GetShouldUseEmotionAnimation | decomp | src/fallout_shared/tesconditionfunctions.cpp:123 |
| 0x00931ED0 | GetVectorElement | decomp | src/bshavok/bhkcharactercontroller_h_unit.cpp: |
| 0x00930C70 | InitHavok | proven | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:4397 |
| 0x00934FD0 | InitiateDialogue | proven | src/fallout/ai/mobileobject.cpp:9588 |
| 0x00932B70 | InitLoadGame | proven | src/fallout/ai/mobileobject.cpp:4806 |
| 0x009307D0 | IsActorDead | class | src/fallout/ai/mobileobject.cpp:133 |
| 0x009336C0 | IsCombatStateActive | decomp | src/fallout/ai/mobileobject.cpp:40 |
| 0x00933840 | IsInDialogueWithPlayer | decomp | src/fallout/ai/mobileobject.cpp:25 |
| 0x00574900 | IsTalkingActivator | proven | src/fallout_shared/tesobjectrefr.cpp:4151 |
| 0x009335B0 | Load3D | proven | src/fallout_shared/tesobjectrefr.cpp:7949 |
| 0x00932A00 | LoadGame | proven | src/fallout/ai/mobileobject.cpp:4167 |
| 0x0092EB50 | MobileObject | proven | src/fallout/ai/mobileobject.cpp:279 |
| 0x00931E50 | ModLooking | proven | src/fallout/ai/mobileobject.cpp:713 |
| 0x0092F260 | Move | proven | src/fallout/ai/mobileobject.cpp:5987 |
| 0x00933270 | PlaySoundByEditorName | decomp | src/fallout/ai/mobileobject.cpp:89 |
| 0x0092F1C0 | Process | proven | src/fallout/ai/mobileobject.cpp:1561 |
| 0x009316C0 | ProcessAnimation | decomp | src/fallout/ai/mobileobject.cpp:33 |
| 0x00934450 | PutCreatedPackage | proven | src/staging/blk_00920000_od.cpp:915 |
| 0x00932750 | Revert | proven | src/fallout/ai/mobileobject.cpp:9456 |
| 0x00932F60 | Revert | class | src/fallout/ai/mobileobject.cpp:64 |
| 0x009333E0 | SetDelete | proven | src/fallout/ai/mobileobject.cpp:992 |
| 0x00931B60 | SetHeading | proven | src/fallout/ai/mobileobject.cpp:622 |
| 0x00931CC0 | SetHeadingToRef | proven | src/fallout/ai/mobileobject.cpp:8173 |
| 0x00931D90 | SetLooking | proven | src/fallout/ai/mobileobject.cpp:677 |
| 0x00931620 | SetPosition | proven | src/fallout/ai/mobileobject.cpp:1073 |
| 0x0086D490 | SetRotation | proven | src/fallout/misc/main.cpp:192 |
| 0x00931F80 | SetSize | proven | src/fallout/ai/actor.cpp:16714 |
| 0x009344D0 | SpeakSoundFunction | proven | src/fallout/ai/mobileobject.cpp:13615 |
| 0x00931710 | StartHighProcess | proven | src/fallout/magic/magicballprojectile.cpp:4102 |
| 0x00936B20 | UpdateAnimationAlt | proven | src/fallout/magic/magicballprojectile.cpp:5801 |
| 0x009339A0 | UpdateInDialogue | proven | src/fallout/ai/mobileobject.cpp:11283 |
| 0x00935AE0 | UpdateTopicInfoSayOnce | proven | src/fallout/ai/mobileobject.cpp:6329 |
| 0x0092EC40 | ~MobileObject | proven | src/fallout/ai/mobileobject.cpp:7938 |

### NonActorMagicTarget (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00825F30 | 'scalar deleting destructor' | proven | src/fallout/magic/nonactormagictarget.cpp:27 |
| 0x007D6BB0 | GetActiveEffectList | decomp | src/fallout/magic/nonactormagictarget.cpp:14 |
| 0x00825EA0 | NonActorMagicTarget | proven | src/staging/blk_00820000_od.cpp:1480 |
| 0x00825FD0 | NonActorMagicTarget | proven | src/fallout/magic/nonactormagictarget.cpp:130 |

### PackagePathing::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DB810 | FUN_008db810 | class | src/fallout/ai/highprocess_rtti_variant.cpp:562 |

### s5730d0::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005730D0 | FUN_005730d0 | unnamed | src/fallout_shared/tesobjectrefr.cpp:44363 |

### s88c790::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088C790 | FUN_0088c790 | unnamed | src/fallout/ai/actor.cpp:114591 |

### s891be0::Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891BE0 | FUN_00891be0 | probable | src/fallout/ai/actor.cpp:114800 |

### XActor (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00569B20 | FUN_00569b20 | unnamed | src/fallout_shared/tesobjectrefr.cpp:10747 |
| 0x0056A470 | FUN_0056a470 | unnamed | src/fallout_shared/tesobjectrefr.cpp:16619 |
| 0x0056B1D0 | FUN_0056b1d0 | unnamed | src/fallout_shared/tesobjectrefr.cpp:10770 |
| 0x00572750 | FUN_00572750 | unnamed | src/fallout_shared/tesobjectrefr.cpp:11212 |
| 0x00572770 | FUN_00572770 | unnamed | src/fallout_shared/tesobjectrefr.cpp:16720 |
| 0x00572D10 | FUN_00572d10 | unnamed | src/fallout_shared/tesobjectrefr.cpp:10971 |
| 0x00573050 | FUN_00573050 | unnamed | src/fallout_shared/tesobjectrefr.cpp:16758 |
| 0x00934430 | FUN_00934430 | unnamed | src/staging/blk_00920000_od.cpp:55 |
| 0x009C3D90 | FUN_009c3d90 | unnamed | src/fallout/ai/combat/projectile.cpp:2553 |

### xActor (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0081EBA0 | FUN_0081eba0 | rejected | src/staging/blk_00800000_o2_od_oy_noo2_variant.cpp:366 |
| 0x0088C240 | FUN_0088c240 | probable | src/fallout/ai/actor.cpp:114392 |
| 0x008BD830 | FUN_008bd830 | probable | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:3043 |
| 0x008CCCE0 | FUN_008ccce0 | probable | src/staging/blk_008c0000_o2_od_oy_noo2_variant.cpp:821 |
| 0x008CCFB0 | FUN_008ccfb0 | probable | src/staging/blk_008c0000_o2_od_oy_noo2_variant.cpp:1035 |

### (free functions) (56)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0085F710 | AddActorToList | decomp | src/staging/blk_00840000_od.cpp:1674 |
| 0x009EBAE0 | AddActorToList | decomp | src/fallout/ai/alarmpackage.cpp:368 |
| 0x00881130 | ApplyActorValueDelta | class | src/fallout/ai/actor.cpp:50926 |
| 0x005EAA80 | CallActorFoo | class | src/fallout_shared/bgsperk.cpp:1125 |
| 0x009F1600 | CanActorReachReference | decomp | src/fallout/ai/fleepackage.cpp:1836 |
| 0x0095EC40 | ClearActorList | decomp | src/bscore/bssimplelist_h_unit.cpp:1343 |
| 0x0066F110 | ClearActorValueSlots | decomp | src/fallout_shared/actorvalue.cpp:753 |
| 0x00975F90 | ClearMobileObjectData | probable | src/fallout/ai/processlists.cpp:1185 |
| 0x007DA270 | CompareActorValueNames | decomp | src/staging/blk_007c0000_od.cpp:275 |
| 0x006436C0 | ComputeActorLevel | decomp | src/fallout_shared/aiformulas.cpp:668 |
| 0x005F0640 | CopyCreatureSoundLists | decomp | src/fallout_shared/creaturesounds.cpp:199 |
| 0x006035E0 | CopyFromNPC | class | src/fallout_shared/tesnpc.cpp:475 |
| 0x0098CF70 | CountActorsPerNode | probable | src/fallout/ai/combat/combatgroup.cpp:2711 |
| 0x009724E0 | FindMobileObjectByValue | decomp | src/fallout/ai/processlists.cpp:2891 |
| 0x00973AB0 | FindUsableActorInArray | decomp | src/fallout/ai/processlists.cpp:6500 |
| 0x009A69C0 | GetActorReach | decomp | src/fallout/ai/combat/combatutilities.cpp:594 |
| 0x0097FD80 | GetActorSlotExtent | decomp | src/fallout/ai/combatcontroller.cpp:5743 |
| 0x0092CD90 | GetActorValue | class | src/fallout/ai/middlelowprocess.cpp:552 |
| 0x0066E9B0 | GetActorValueDescription | decomp | src/fallout_shared/actorvalue.cpp:697 |
| 0x00649580 | GetActorValueScaledSetting | decomp | src/staging/blk_00640000_od.cpp:1463 |
| 0x0050E8F0 | GetActorValueShortVector | decomp | src/fallout_shared/tesobject.cpp:428 |
| 0x0092CE00 | GetActorValueWithModifiers | class | src/fallout/ai/middlelowprocess.cpp:141 |
| 0x007700F0 | GetActorValueWithPerkModifiers | decomp | src/fallout/interface/menus/hudmainmenu.cpp:4394 |
| 0x008D0390 | GetDistanceBetweenActors | class | src/fallout/ai/baseprocess.cpp:732 |
| 0x005F0A30 | GetRandomCreatureSound | decomp | src/fallout_shared/creaturesounds.cpp:228 |
| 0x00864660 | GetReferenceAsActor | class | src/fallout/misc/saveload/bgsloadformbuffer.cpp:26 |
| 0x00936A20 | HandleMobileObjectResult | decomp | src/fallout/ai/mobileobject.cpp:1017 |
| 0x0080D4B0 | HasActor | decomp | src/fallout/magic/cureeffect.cpp:17 |
| 0x006E29F0 | InitFromActor | probable | src/fallout/ai/movement/actormover.cpp:1770 |
| 0x009722E0 | IsActorInOtherList | decomp | src/fallout/ai/processlists.cpp:12198 |
| 0x007E05F0 | IsActorValueBelowPermanent | decomp | src/fallout/interface/menus/statsmenu.cpp:278 |
| 0x0082D060 | IsCharacter | decomp | src/fallout/magic/dispeleffect.cpp:35 |
| 0x009C30D0 | NotifyActorIfEligible | probable | src/fallout/ai/combat/projectile.cpp:2068 |
| 0x008C5350 | OnActorValueStageChange | decomp | src/fallout/ai/actor_magic.cpp:6144 |
| 0x008987F0 | ProcessActorInteraction | class | src/fallout/ai/actor.cpp:64218 |
| 0x0096D520 | ProcessPlayerCellActors | decomp | src/fallout/ai/processlists.cpp:6006 |
| 0x009F0CF0 | PruneActorList | class | src/fallout/ai/escortpackage.cpp:373 |
| 0x0087B190 | QueueActorTask | probable | src/fallout/misc/taskqueueinterface.cpp:872 |
| 0x009F0A20 | RegisterActor | decomp | src/fallout/ai/escortpackage.cpp:29 |
| 0x0084A580 | RemoveActorFromMap | decomp | src/fallout/misc/saveload/bgssaveloadgame.cpp:360 |
| 0x008BC590 | ResetActorState | decomp | src/fallout/ai/actor.cpp:30753 |
| 0x00601570 | ResetCharacterData | class | src/fallout_shared/tesnpc.cpp:18 |
| 0x008D7220 | ResolveActorFormId | decomp | src/fallout/ai/highprocess.cpp:3840 |
| 0x00810570 | SetAssociatedActorValue | decomp | src/effectsetting.cpp:370 |
| 0x005F9AF0 | SetCreatureType | decomp | src/fallout_shared/tescreature.cpp:201 |
| 0x0099A680 | SetStampFromActor | decomp | src/fallout/ai/combat/combatstate.cpp:1814 |
| 0x007D32B0 | StartCharacterGeneration | decomp | src/fallout/interface/menus/startmenu.cpp:3863 |
| 0x0091EFC0 | StopActorMoving | class | src/fallout/ai/middlehighprocess.cpp:8197 |
| 0x0092C720 | UpdateActorFlags | class | src/fallout/ai/middlehighprocess.cpp:2743 |
| 0x00912150 | UpdateActorIfStale | class | src/fallout/ai/lowprocess.cpp:5139 |
| 0x008E3F00 | UpdateActorsInRadius | class | src/fallout/ai/highprocess.cpp:33677 |
| 0x008B9960 | UpdateActorValueFlag | decomp | src/fallout/ai/actor.cpp:82444 |
| 0x007DFB00 | UpdateActorValueTile | decomp | src/fallout/interface/menus/statsmenu.cpp:224 |
| 0x009E54A0 | UpdateAliveActorList | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:5607 |
| 0x0080CED0 | UpdateEffectShaderOnActor | decomp | src/fallout/magic/detectlifeeffect.cpp:395 |
| 0x005F6E20 | ValidateSkillActorValue | decomp | src/fallout_shared/tesclass.cpp:121 |

## 2b Player (shares the Actor code)

PlayerCharacter is an Actor too; listed apart so it is easy to skip.

### PlayerCharacter (151)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009398A0 | 'scalar deleting destructor' | proven | src/fallout/ai/playercharacter.cpp:2234 |
| 0x0094C680 | AddActorEffect | proven | src/fallout/ai/playercharacter.cpp:20530 |
| 0x0093A690 | AddActorToPlayerCombatList | proven | src/fallout/ai/playercharacter.cpp:2258 |
| 0x00966A70 | AddNote | proven | src/fallout/ai/playercharacter.cpp:48206 |
| 0x0094C4F0 | AlterModifier | proven | src/fallout/ai/playercharacter.cpp:20463 |
| 0x009590F0 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/playercharacter.cpp:36805 |
| 0x00952D60 | BuildPathToTarget | proven | src/fallout/ai/playercharacter.cpp:31216 |
| 0x00950AD0 | CallGetValidBip01Names | proven | src/fallout/ai/character.cpp:313 |
| 0x009694D0 | CannibalizeActor | proven | src/fallout/ai/character.cpp:2855 |
| 0x0093DB60 | CenterOnCell | proven | src/fallout/ai/playercharacter.cpp:10887 |
| 0x00952C30 | CheckForQuestTargetUpdate | proven | src/fallout/ai/playercharacter.cpp:31114 |
| 0x00952730 | CheckInvulnerable | proven | src/fallout/ai/playercharacter.cpp:30950 |
| 0x0095E6F0 | CheckPoisonWeapon | proven | src/fallout_shared/tesobjectbook.cpp:1194 |
| 0x009690A0 | ClearRockItAmmo | proven | src/fallout/ai/playercharacter.cpp:53848 |
| 0x0093AB80 | DamageActionPoints | proven | src/fallout/ai/playercharacter.cpp:3457 |
| 0x0093AB30 | DamageActionPointsForAction | proven | src/fallout/ai/actor.cpp:41184 |
| 0x0093B7A0 | DamageActorValue | proven | src/fallout/ai/playercharacter.cpp:5934 |
| 0x009508B0 | DamageItem | proven | src/fallout/ai/playercharacter.cpp:27118 |
| 0x00961D50 | DeathMenu | proven | src/fallout/ai/actor.cpp:41247 |
| 0x00961280 | DestroyMouseSpring | proven | src/fallout/ai/playercharacter.cpp:41320 |
| 0x005DE9B0 | DisableHardcoreTracking | proven | src/fallout_shared/tesscriptfunctions.cpp:2237 |
| 0x00954610 | DropItem | proven | src/fallout/ai/playercharacter.cpp:34543 |
| 0x0094ED40 | ExportProgressData | proven | src/fallout/ai/playercharacter.cpp:24327 |
| 0x00958EC0 | FinishInitLoadGameTES | proven | src/fallout/ai/playercharacter.cpp:36320 |
| 0x0095C730 | FinishLoadGame | proven | src/fallout/ai/playercharacter.cpp:38179 |
| 0x00953060 | FocusOnActor | proven | src/fallout/ai/playercharacter.cpp:32129 |
| 0x005C4210 | Force3rdPerson | proven | src/fallout_shared/tesscriptfunctions.cpp:3389 |
| 0x0095F6A0 | ForcePhysicsGrabDrop | proven | src/staging/blk_00940000_od.cpp:255 |
| 0x00950460 | ForceTemp1stPerson | proven | src/fallout/ai/playercharacter.cpp:26294 |
| 0x00950340 | ForceTemp3rdPerson | proven | src/fallout/ai/playercharacter.cpp:25588 |
| 0x007D1340 | FUN_007d1340 | unnamed | src/fallout/interface/menus/startmenu.cpp:36 |
| 0x00874900 | Get1stPersonFOV | proven | src/fallout/misc/main.cpp:1306 |
| 0x005CBB50 | GetActiveQuest | proven | src/fallout_shared/tesscriptfunctions.cpp:1871 |
| 0x0093AC20 | GetActorValue | decomp | src/fallout/ai/playercharacter.cpp:7 |
| 0x0094C3D0 | GetActorValueModifierAmount | decomp | src/fallout/ai/playercharacter.cpp:19 |
| 0x00939750 | GetAdvanceNumber | proven | src/fallout/ai/playercharacter.cpp:2132 |
| 0x00950A60 | GetAnimation | decomp | src/fallout/interface/interface.cpp:316 |
| 0x00950A10 | GetAnimData | proven | src/fallout/ai/playercharacter.cpp:27652 |
| 0x00968690 | GetAnticipatedLocation | proven | src/fallout/ai/character.cpp:501 |
| 0x00950B00 | GetBiped | proven | src/staging/blk_00940000_od.cpp:241 |
| 0x00967A00 | GetBumpedActor | proven | src/fallout/ai/playercharacter.cpp:51552 |
| 0x00967950 | GetBumpedRef | proven | src/fallout/ai/playercharacter.cpp:51507 |
| 0x005DF5B0 | GetCachedWorldCameraPos | proven | src/fallout_shared/tesscriptfunctions.cpp:2319 |
| 0x009396D0 | GetCombatGroup | class | src/fallout/ai/playercharacter_h_unit.cpp: |
| 0x005A03F0 | GetControlsDisabled | proven | src/fallout_shared/tesconditionfunctions.cpp:2343 |
| 0x00950BE0 | GetCurrent3D | proven | src/fallout/ai/playercharacter.cpp:27715 |
| 0x005C7870 | GetInChargen | proven | src/fallout_shared/tesscriptfunctions.cpp:1808 |
| 0x00490F80 | GetInventory3D | proven | src/fallout_shared/animation.cpp:499 |
| 0x009397E0 | GetIsImmobileCreature | proven | src/fallout/ai/playercharacter.cpp:2174 |
| 0x00969760 | GetIsInCanibalAction | proven | src/fallout/ai/playercharacter.cpp:55169 |
| 0x00969700 | GetIsInSandmanAction | proven | src/fallout/ai/playercharacter.cpp:55001 |
| 0x00595D10 | GetListofPerceivedActors | proven | src/fallout_shared/medialocationcontroller.cpp:430 |
| 0x009698A0 | GetMediaLocationController | proven | src/fallout/ai/character.cpp:42 |
| 0x00962620 | GetNumberOfFollowers | proven | src/fallout/ai/highprocess.cpp:26365 |
| 0x009639E0 | GetPerkRank | proven | src/fallout/ai/playercharacter.cpp:44247 |
| 0x009397B0 | GetPerkRankList | proven | src/fallout/ai/playercharacter.cpp:2155 |
| 0x0082EAA0 | GetRegionSounds | decomp | src/fallout/audio/falloutaudio.cpp:475 |
| 0x00954D40 | GetSaveSize | proven | src/fallout/ai/playercharacter.cpp:35538 |
| 0x00939790 | GetSkillAdvanceDelayed | proven | src/fallout/ai/actor.cpp:33540 |
| 0x0093A740 | GetUnderAIControl | proven | src/fallout/ai/playercharacter.cpp:2275 |
| 0x00950A90 | GetValidBip01Names | proven | src/fallout/ai/playercharacter.cpp:27671 |
| 0x00710AB0 | GetWorldFOV | proven | src/fallout/interface/interfacemanager.cpp:419 |
| 0x0095F6C0 | HandlePhysicsGrab | proven | src/staging/blk_00940000_od.cpp:4189 |
| 0x0093BEA0 | HandlePositionPlayerRequest | proven | src/fallout/ai/playercharacter.cpp:7453 |
| 0x00966C10 | HasNote | decomp | src/fallout_shared/bgsterminal.cpp:255 |
| 0x00962350 | HavokActivateDroppedReference | proven | src/fallout/ai/playercharacter.cpp:43047 |
| 0x00969260 | InitiateSandmanPackage | proven | src/fallout/ai/playercharacter.cpp:68315 |
| 0x0095C0A0 | InitLoadGame | proven | src/fallout/ai/playercharacter.cpp:67339 |
| 0x00958990 | InitLoadGameTES | proven | src/fallout/ai/playercharacter.cpp:60824 |
| 0x00966F20 | InsertPerceivedActor | proven | src/fallout/ai/playercharacter.cpp:64993 |
| 0x004EAF60 | Is3rdPerson | proven | src/fallout_shared/teswater.cpp:555 |
| 0x009549A0 | IsActorFollowingPlayer | proven | src/fallout/ai/playercharacter.cpp:34795 |
| 0x00967090 | IsActorPerceived | proven | src/fallout/ai/playercharacter.cpp:48370 |
| 0x00962950 | IsConflictingObject | proven | src/staging/blk_00960000_od.cpp:2832 |
| 0x009526F0 | IsDemigodMode | proven | src/fallout/ai/playercharacter.cpp:30885 |
| 0x009526B0 | IsGodMode | proven | src/fallout/ai/playercharacter.cpp:30859 |
| 0x004D1360 | IsHardcore | proven | src/fallout_shared/inventorychanges.cpp:1030 |
| 0x00954CC0 | IsOverEncumbered | proven | src/fallout/ai/actor.cpp:17142 |
| 0x00953C50 | IsPlayerCharacterInCombat | proven | src/fallout/ai/playercharacter.cpp:32313 |
| 0x00962720 | IsPlayerFollower | proven | src/fallout_shared/package.cpp:6003 |
| 0x0082EAC0 | IsRegionSoundsEnabled | decomp | src/fallout/audio/falloutaudio.cpp:470 |
| 0x005A1E50 | IsSleeping | proven | src/fallout_shared/tesconditionfunctions.cpp:2864 |
| 0x0094DF60 | IsSleepingOrResting | decomp | src/fallout/ai/combat/projectile.cpp:6 |
| 0x009678A0 | IsStandingOnFurniture | proven | src/fallout/ai/playercharacter.cpp:51447 |
| 0x00950090 | IsVanityMode | proven | src/fallout/ai/playercharacter.cpp:25507 |
| 0x0094E1D0 | Load3D | proven | src/fallout/ai/playercharacter.cpp:22536 |
| 0x0095A3B0 | LoadGame | proven | src/fallout/ai/playercharacter.cpp:62307 |
| 0x00956F70 | LoadGame2 | proven | src/fallout/ai/playercharacter.cpp:65578 |
| 0x00953FF0 | PickUpObject | proven | src/fallout/ai/playercharacter.cpp:33605 |
| 0x00938180 | PlayerCharacter | proven | src/staging/blk_00920000_od.cpp:3810 |
| 0x0094DF80 | PlayerSleep | proven | src/fallout/ai/playercharacter.cpp:20991 |
| 0x00962290 | PlayImpactBasedHitShader | proven | src/fallout/ai/playercharacter.cpp:42882 |
| 0x0095E900 | PoisonWeapon | proven | src/staging/blk_00940000_od.cpp:1434 |
| 0x00798400 | QPlayerMapMarker | proven | src/fallout/interface/menus/mapmenu.cpp:169 |
| 0x00951940 | RecursiveReadyInventoryNode | proven | src/fallout/ai/playercharacter.cpp:28622 |
| 0x0095D3F0 | Reload2 | proven | src/fallout/ai/playercharacter.cpp:39473 |
| 0x0093A660 | RemoveActorFromPlayercombatList | proven | src/staging/blk_00920000_od.cpp:651 |
| 0x00967350 | RemovePerceivedActor | proven | src/fallout/ai/playercharacter.cpp:50244 |
| 0x00952F90 | RemovePlayerMapMarker | proven | src/staging/blk_00940000_od.cpp:551 |
| 0x0094C7A0 | RemoveSpell | proven | src/fallout/ai/playercharacter.cpp:20613 |
| 0x00968730 | ReportRadiationChange | proven | src/fallout/ai/playercharacter.cpp:52749 |
| 0x0093BE30 | RequestPositionPlayer | proven | src/fallout/ai/playercharacter.cpp:6220 |
| 0x0095ED80 | ResetActorValueModifiers | class | src/fallout/ai/playercharacter_h_unit.cpp: |
| 0x009480C0 | ResetMapMarkerStructList | proven | src/fallout/ai/playercharacter.cpp:16322 |
| 0x0082EA80 | ResetRegionSoundTimer | decomp | src/fallout/audio/falloutaudio.cpp:465 |
| 0x00969110 | ResetRockItAmmoWeight | proven | src/fallout/ai/playercharacter.cpp:54786 |
| 0x0094FD30 | RewardKarma | proven | src/fallout/ai/playercharacter.cpp:24640 |
| 0x0094FD10 | RewardXP | proven | src/fallout/ai/playercharacter.cpp:68974 |
| 0x00955620 | SaveGame | proven | src/fallout/ai/playercharacter_rtti2_variant.cpp:36899 |
| 0x0094EB40 | Set3D | proven | src/fallout/ai/playercharacter.cpp:23663 |
| 0x009520F0 | SetActionGroupFlags | class | src/fallout/ai/playercharacter_h_unit.cpp: |
| 0x009529D0 | SetActiveQuest | proven | src/fallout/ai/aitaskmanager.cpp:880 |
| 0x0093A7C0 | SetActorBaseValue | proven | src/fallout/ai/playercharacter.cpp:2704 |
| 0x0093A850 | SetActorBaseValue | proven | src/staging/blk_00920000_od.cpp:2328 |
| 0x0093AE40 | SetActorValue | proven | src/fallout/ai/playercharacter.cpp:3480 |
| 0x00939730 | SetAdvanceNumber | proven | src/fallout/ai/playercharacter.cpp:2121 |
| 0x005CC7A0 | SetAIControlledPackage | proven | src/fallout_shared/tesscriptfunctions.cpp:39078 |
| 0x0095F530 | SetControlsDisabled | proven | src/fallout_shared/tesworldspace.cpp:1204 |
| 0x0095F590 | SetControlsDisabled | proven | src/fallout/ai/playercharacter.cpp:41221 |
| 0x00519020 | SetForceActivateRef | proven | src/staging/blk_00500000_od.cpp:318 |
| 0x00950610 | SetFOV | proven | src/fallout/ai/playercharacter.cpp:26874 |
| 0x009526A0 | SetGodMode | proven | src/fallout/ai/playercharacter.cpp:30845 |
| 0x00969E90 | SetHardcore | proven | src/fallout/ai/playercharacter.cpp:57240 |
| 0x00950010 | SetInChargen | proven | src/fallout/ai/playercharacter.cpp:25155 |
| 0x00966EA0 | SetMoveMode | proven | src/fallout/ai/playercharacter.cpp:64097 |
| 0x009590D0 | SetNeedResetHardcoreTimer | proven | src/fallout/ai/playercharacter.cpp:36440 |
| 0x0094CAE0 | SetParentCell | proven | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:6104 |
| 0x009697C0 | SetPCToddler | proven | src/fallout/ai/playercharacter.cpp:55200 |
| 0x00969820 | SetPCYoung | proven | src/fallout/ai/playercharacter.cpp:55719 |
| 0x006159E0 | SetReputationUpdate | proven | src/tesreputation.cpp:101 |
| 0x0094C950 | SetSelectedScroll | proven | src/staging/blk_00940000_od.cpp:493 |
| 0x0094C8E0 | SetSelectedSpell | proven | src/fallout/ai/playercharacter.cpp:20635 |
| 0x0093E530 | SetSlowMoCamera | proven | src/fallout/ai/playercharacter.cpp:13154 |
| 0x0093A5F0 | SetUnderAIControl | decomp | src/bsaudio/bsaudio_h_unit.cpp: |
| 0x0095EDF0 | Setup3rdPersonCameraCaster | proven | src/fallout/ai/playercharacter.cpp:40909 |
| 0x008BBBF0 | SetWeaponSightingNode | proven | src/fallout/ai/actor.cpp:13512 |
| 0x00951A10 | Show1stPerson | proven | src/fallout/ai/playercharacter.cpp:30010 |
| 0x009500A0 | StopVanityMode | proven | src/fallout/ai/playercharacter.cpp:68993 |
| 0x00961E30 | ToggleFlyCam | proven | src/staging/blk_00960000_od.cpp:6519 |
| 0x0093E860 | Update | proven | src/staging/blk_00920000_od.cpp:6304 |
| 0x00950930 | UpdateAnimation | proven | src/fallout/ai/playercharacter.cpp:27630 |
| 0x00952290 | UpdateArmRotation | proven | src/fallout/ai/playercharacter.cpp:30773 |
| 0x00964260 | UpdateAutoAimActor | proven | src/fallout/ai/actor.cpp:132199 |
| 0x00950290 | UpdateCameraMode | decomp | src/bsaudio/bsaudio_h_unit.cpp: |
| 0x00962D00 | UpdateConflictingObjects | proven | src/staging/blk_00960000_od.cpp:1701 |
| 0x00969C30 | UpdateHardcoreMode | proven | src/fallout/ai/playercharacter.cpp:56421 |
| 0x009444D0 | UpdatePlayerCombat | proven | src/fallout/ai/playercharacter.cpp:13230 |
| 0x009624D0 | UpdateRefLight | proven | src/fallout_shared/tesobjectrefr.cpp:9168 |
| 0x00950530 | UpdateTemp1stPerson | proven | src/fallout/ai/playercharacter.cpp:26425 |
| 0x009503D0 | UpdateTemp3rdPerson | proven | src/fallout/ai/playercharacter.cpp:26247 |
| 0x0095DDC0 | UseAmmo | proven | src/fallout/ai/playercharacter.cpp:40736 |

### PlayerMover (14)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E9E00 | 'scalar deleting destructor' | proven | src/fallout/ai/movement/playermover.cpp:337 |
| 0x009EA3B0 | ClearMode | decomp | src/fallout/ai/movement/playermover.cpp:286 |
| 0x009185E0 | GetActorStateFlags | decomp | src/fallout_shared/tesobjectcell.cpp:121 |
| 0x009EA680 | InitLoadGame | class | src/fallout/ai/movement/playermover.cpp:114 |
| 0x009EA610 | LoadGame | class | src/fallout/ai/movement/playermover.cpp:104 |
| 0x009E9D00 | PlayerMover | proven | src/staging/blk_009e0000_od.cpp:2322 |
| 0x009EA6A0 | Revert | class | src/fallout/ai/movement/playermover.cpp:94 |
| 0x009EA5A0 | SaveGame | proven | src/fallout/ai/movement/playermover.cpp:358 |
| 0x009EA2F0 | SetMovementValue | class | src/fallout/ai/movement/playermover.cpp:120 |
| 0x009EA3E0 | SetMoverMode | class | src/fallout/ai/movement/playermover.cpp:235 |
| 0x009EA570 | SetSideVec | decomp | src/fallout/ai/movement/playermover.cpp:280 |
| 0x009E9E50 | Update | class | src/fallout/ai/movement/playermover.cpp:131 |
| 0x009EA360 | UpdatePlayerStatus | decomp | src/fallout/ai/movement/playermover.cpp:270 |
| 0x009E9E30 | ~PlayerMover | proven | src/fallout/ai/movement/playermover.cpp:324 |

## 3 Base records (what an NPC is made of)

TESNPC / TESCreature records and their parts: race, class, faction, voice, hair, eyes, head parts, leveled lists, combat style.

### ActorValueInfo (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00670050 | 'scalar deleting destructor' | proven | src/fallout_shared/actorvalue.cpp:597 |
| 0x0066FE40 | ActorValueInfo | proven | src/fallout_shared/actorvalue.cpp:353 |
| 0x00670540 | Compare | proven | src/fallout_shared/actorvalue.cpp:871 |
| 0x00670430 | CopyFrom | proven | src/fallout_shared/actorvalue.cpp:833 |
| 0x0066FDF0 | GetActorValueFormID | proven | src/fallout_shared/actorvalue.cpp:479 |
| 0x006701A0 | Load | class | src/fallout_shared/actorvalue.cpp:139 |
| 0x006703B0 | SaveForm | proven | src/fallout_shared/actorvalue.cpp:669 |
| 0x00670120 | SetEnumerated | decomp | src/fallout_shared/actorvalue.cpp:408 |

### BGSBodyPart (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005E3AF0 | BGSBodyPart | proven | src/fallout_shared/bgsbodypart.cpp:53 |
| 0x005E5190 | GetActorValue | proven | src/staging/blk_005e0000_od.cpp:4515 |
| 0x005E4730 | HideLimb | proven | src/fallout_shared/bgsbodypart.cpp:357 |
| 0x005E3D80 | InitItem | proven | src/fallout_shared/bgsbodypart.cpp:61 |
| 0x008B4360 | IsExplodablePart | proven | src/fallout/ai/actor.cpp:34394 |
| 0x008B4CD0 | IsExplodeChanceAbsolute | proven | src/staging/blk_008a0000_od.cpp:201 |
| 0x005E4100 | Load | proven | src/fallout_shared/bgsbodypart.cpp:106 |
| 0x005E45E0 | QueueResourceLoad | class | src/fallout_shared/bgsbodypart.cpp:33 |
| 0x005E4970 | ShowLimb | proven | src/staging/blk_005e0000_od.cpp:3670 |
| 0x005E4890 | UnhideLimb | proven | src/fallout_shared/bgsbodypart.cpp:462 |
| 0x005E3C60 | ~BGSBodyPart | proven | src/fallout_shared/bgsbodypart.cpp:320 |

### BGSBodyPartData (15)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005E4B90 | 'scalar deleting destructor' | proven | src/staging/blk_005e0000_od.cpp:5014 |
| 0x005E5220 | AddBodyPart | proven | src/fallout_shared/bgsbodypartdata.cpp:151 |
| 0x005E4AF0 | BGSBodyPartData | proven | src/fallout_shared/bgsbodypartdata.cpp:22 |
| 0x005E51B0 | ClearBodyParts | decomp | src/fallout_shared/bgsbodypartdata.cpp:43 |
| 0x005E4C70 | ClearData | class | src/fallout_shared/bgsbodypartdata.cpp:36 |
| 0x005E53A0 | GenerateDefaultBodyPartData | proven | src/fallout_shared/bgsbodypartdata.cpp:183 |
| 0x005E50F0 | GetBodyPart | proven | src/staging/blk_005e0000_od.cpp:4501 |
| 0x005E5130 | GetBodyPart | proven | src/fallout_shared/bgsbodypartdata.cpp:224 |
| 0x005E55E0 | HideChildLimbs | proven | src/staging/blk_005e0000_od.cpp:5128 |
| 0x005E4C90 | InitItem | class | src/fallout_shared/bgsbodypartdata.cpp:53 |
| 0x005E4D80 | Load | class | src/fallout_shared/bgsbodypartdata.cpp:76 |
| 0x005E5590 | QueueResourceLoad | decomp | src/fallout_shared/bgsbodypartdata.cpp:171 |
| 0x005E4C40 | ResetFormData | class | src/fallout_shared/bgsbodypartdata.cpp:29 |
| 0x005E5750 | ShowChildLimbs | proven | src/staging/blk_005e0000_od.cpp:5214 |
| 0x005E4BC0 | ~BGSBodyPartData | proven | src/staging/blk_005e0000_od.cpp:5066 |

### BGSEntryPointFunctionDataLeveledList (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005E6510 | BGSEntryPointFunctionDataLeveledList | proven | src/staging/blk_005e0000_od.cpp:5338 |
| 0x005E6A60 | Compare | proven | src/fallout_shared/bgsentrypointfunction.cpp:673 |
| 0x005E69D0 | Duplicate | proven | src/fallout_shared/bgsentrypointfunction.cpp:375 |
| 0x005E6B00 | Load | proven | src/fallout_shared/bgsentrypointfunction.cpp:427 |
| 0x005E6AB0 | Save | proven | src/fallout_shared/bgsentrypointfunction.cpp:395 |

### BGSHeadPart (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005E7370 | 'scalar deleting destructor' | proven | src/fallout_shared/bgsheadpart.cpp:678 |
| 0x005E7790 | AddExtraPart | proven | src/bscore/bssimplelist_h_unit.cpp: |
| 0x005E72C0 | BGSHeadPart | proven | src/fallout_shared/bgsheadpart.cpp:105 |
| 0x005E7460 | ClearData | proven | src/fallout_shared/bgsheadpart.cpp:785 |
| 0x005E79A0 | Compare | proven | src/fallout_shared/bgsheadpart.cpp:645 |
| 0x005E78F0 | CopyFrom | proven | src/fallout_shared/bgsheadpart.cpp:611 |
| 0x005E77B0 | InitItem | proven | src/fallout_shared/bgsheadpart.cpp:975 |
| 0x005E7530 | Load | proven | src/fallout_shared/bgsheadpart.cpp:484 |
| 0x005E7440 | ResetFormData | class | src/fallout_shared/bgsheadpart.cpp:99 |
| 0x005E73A0 | ~BGSHeadPart | proven | src/fallout_shared/bgsheadpart.cpp:711 |

### BGSRagdoll (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005EDAC0 | 'scalar deleting destructor' | proven | src/fallout_shared/bgsragdoll.cpp:807 |
| 0x005ED680 | BGSRagdoll | proven | src/fallout_shared/bgsragdoll.cpp:122 |
| 0x005EEC60 | Compare | proven | src/fallout_shared/bgsragdoll.cpp:758 |
| 0x005EEB70 | CopyFrom | proven | src/fallout_shared/bgsragdoll.cpp:709 |
| 0x005EEA20 | InitItem | class | src/fallout_shared/bgsragdoll.cpp:129 |
| 0x005EE640 | Load | class | src/fallout_shared/bgsragdoll.cpp:161 |
| 0x005EDD00 | ResetFormData | class | src/fallout_shared/bgsragdoll.cpp:35 |
| 0x005EE110 | SaveForm | proven | src/fallout_shared/bgsragdoll.cpp:1141 |
| 0x005EDC30 | ~BGSRagdoll | proven | src/fallout_shared/bgsragdoll.cpp:1417 |

### BGSVoiceType (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F00A0 | 'scalar deleting destructor' | proven | src/fallout_shared/bgsvoicetype.cpp:117 |
| 0x005EFFC0 | BGSVoiceType | proven | src/fallout_shared/bgslistform.cpp:464 |
| 0x005F02F0 | Compare | proven | src/fallout_shared/bgsvoicetype.cpp:152 |
| 0x005F02A0 | CopyFrom | proven | src/fallout_shared/bgsvoicetype.cpp:133 |
| 0x005F0060 | GetEditorID | proven | src/fallout_shared/bgsdehydration.cpp:656 |
| 0x005F01A0 | Load | class | src/fallout_shared/bgsvoicetype.cpp:6 |
| 0x005F0140 | SaveForm | proven | src/fallout_shared/bgsvoicetype.cpp:55 |
| 0x005F00D0 | ~BGSVoiceType | proven | src/fallout_shared/bgsvoicetype.cpp:106 |

### CreatureSounds (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F0900 | AddCreatureSound | proven | src/fallout_shared/creaturesounds.cpp:55 |
| 0x005F0480 | LoadCreatureSound | proven | src/fallout_shared/creaturesounds.cpp:80 |
| 0x005F03A0 | Save | proven | src/fallout_shared/creaturesounds.cpp:251 |

### ExtraFactionChanges (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00436D50 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:4722 |
| 0x00436CB0 | ExtraFactionChanges | proven | src/fallout_shared/extradataobjects.cpp:1212 |
| 0x00436E10 | RemoveFaction | decomp | src/fallout_shared/extradataobjects.cpp:288 |
| 0x00436F80 | SetFactionRank | decomp | src/fallout_shared/extradataobjects.cpp:311 |
| 0x00436D80 | ~ExtraFactionChanges | proven | src/fallout_shared/extradataobjects.cpp:4089 |

### ExtraLeveledItem (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00431CC0 | Compare | class | src/fallout_shared/extradataobjects.cpp:156 |
| 0x0042C8C0 | ExtraLeveledItem | proven | src/fallout_shared/extradatalist.cpp:19432 |
| 0x00432BE0 | ExtraLeveledItem | proven | src/fallout_shared/extradataobjects.cpp:73 |

### TESActorBase (19)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F78B0 | 'scalar deleting destructor' | proven | src/fallout_shared/tescreature.cpp:557 |
| 0x005F1F30 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/tesactorbase.cpp:298 |
| 0x005F0B50 | DoesSwim | proven | src/fallout_shared/tesactorbase.cpp:129 |
| 0x005F0BF0 | DoesWalk | proven | src/fallout_shared/tesactorbase.cpp:320 |
| 0x005F0F80 | GetBodyPartData | proven | src/fallout_shared/tesactorbase.cpp:167 |
| 0x005F7480 | GetCurrentActorValue | decomp | src/fallout_shared/tesraceform.cpp:63 |
| 0x005F16F0 | GetSaveSize | proven | src/fallout_shared/tesactorbase.cpp:610 |
| 0x0048CEE0 | GetSex | decomp | src/fallout_shared/tesactorbase.cpp:6 |
| 0x005F0CC0 | GetSex | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:43 |
| 0x005F0D00 | IsAutoCalc | proven | src/fallout_shared/tesactorbase.cpp:13 |
| 0x005F1FD0 | LoadGame | class | src/fallout_shared/tesactorbase.cpp:34 |
| 0x005F1B30 | LoadGame2 | proven | src/fallout_shared/tesactorbase.cpp:1109 |
| 0x005F1690 | MarkAsUnmodified | proven | src/fallout_shared/tesactorbase.cpp:257 |
| 0x005F7520 | ModActorValue | proven | src/fallout_shared/tescreature.cpp:775 |
| 0x005F1630 | NotifyFormIDChanged | class | src/fallout_shared/tesactorbase.cpp:21 |
| 0x005F20A0 | Reset3DForLoadedActors | proven | src/fallout_shared/tesactorbase.cpp:58 |
| 0x005F18C0 | SaveGame | proven | src/fallout_shared/tesactorbase.cpp:845 |
| 0x005F1590 | ShouldUseDefaultAppearance | probable | src/fallout_shared/tesactorbase.cpp:85 |
| 0x005F75E0 | TESActorBase | proven | src/fallout_shared/tescreature.cpp:894 |

### TESActorBaseData (52)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0047E2A0 | AddFormChange | proven | src/fallout_shared/tesactorbasedata.cpp:864 |
| 0x0047CE10 | CalcTemplateForRef | proven | src/fallout_shared/tesactorbasedata.cpp:1975 |
| 0x0047C9B0 | ClearDataComponent | proven | src/fallout_shared/tesactorbasedata.cpp:1082 |
| 0x0047D130 | CreateTemplateActorBase | proven | src/fallout_shared/tesactorbasedata.cpp:381 |
| 0x005F9010 | FUN_005f9010 | unnamed | src/staging/blk_005e0000_od.cpp:686 |
| 0x0047E040 | GetAlignmentForKarma | proven | src/fallout_shared/tesactorbasedata.cpp:973 |
| 0x0047C790 | GetAllowPCDialogue | proven | src/fallout_shared/tesactorbasedata.cpp:1050 |
| 0x0047C7B0 | GetAllowPickPocket | proven | src/fallout_shared/tesactorbasedata.cpp:1067 |
| 0x0047D390 | GetCalcLevelMin | proven | src/fallout_shared/tesactorbasedata.cpp:505 |
| 0x0047D680 | GetFactionRank | proven | src/fallout_shared/tesactorbasedata.cpp:601 |
| 0x004A8AE0 | GetFatigue | class | src/fallout_shared/tesactorbasedata.cpp: |
| 0x00461580 | GetFlagBit | proven | src/bscore/memorymanager.cpp:67 |
| 0x0047C860 | GetHealthRegeneration | class | src/fallout_shared/tesactorbasedata.cpp: |
| 0x0047C7D0 | GetIsGhost | class | src/fallout_shared/tesactorbasedata.cpp: |
| 0x0047C7F0 | GetIsInvulnerable | class | src/fallout_shared/tesactorbasedata.cpp: |
| 0x0047E0E0 | GetKarmicTitle | proven | src/fallout_shared/tesactorbasedata.cpp:726 |
| 0x0047DED0 | GetLevel | proven | src/fallout/ai/actor.cpp:190 |
| 0x0047D1A0 | GetLeveledTemplateInHierarchy | proven | src/fallout_shared/tesactorbasedata.cpp:466 |
| 0x00461560 | GetMatchesPCLevel | proven | src/fallout_shared/tesdatahandler.cpp:2424 |
| 0x0047C830 | GetNoHeadTracking | class | src/fallout_shared/tesactorbasedata.cpp: |
| 0x0047C810 | GetNoKnockdowns | decomp | src/fallout_shared/tesactorbasedata.cpp: |
| 0x005D2780 | GetNoRumors | proven | src/fallout_shared/tesscriptfunctions.cpp:3718 |
| 0x0047C770 | GetNoVATSMelee | proven | src/fallout_shared/tesactorbasedata.cpp:1417 |
| 0x0056AF00 | GetRespawn | proven | src/staging/blk_00560000_od.cpp:95 |
| 0x0055E200 | GetRunsInLow | proven | src/fallout_shared/tesobjectrefr.cpp:1226 |
| 0x0047E380 | GetSaveSize | proven | src/fallout_shared/tesactorbasedata.cpp:1363 |
| 0x0047CD40 | GetTemplateUseFlag | proven | src/fallout_shared/tesactorbasedata.cpp:218 |
| 0x0047CDB0 | GetUsesLeveledTemplate | proven | src/fallout_shared/tesactorbasedata.cpp:249 |
| 0x0047D8B0 | InitItem | proven | src/fallout_shared/tesactorbasedata.cpp:2768 |
| 0x0047D740 | IsInEvilFactionsOnly | proven | src/fallout_shared/tesactorbasedata.cpp:1483 |
| 0x0047EBF0 | IsInFaction | proven | src/fallout_shared/extradataobjects.cpp:167 |
| 0x0047CDD0 | IsTemplateLeveled | proven | src/fallout_shared/tesactorbasedata.cpp:264 |
| 0x0047E6F0 | LoadGame | proven | src/fallout_shared/tesactorbasedata.cpp:2430 |
| 0x0047EA70 | LoadGame | proven | src/staging/blk_00460000_od.cpp:2539 |
| 0x0047CAC0 | Save | proven | src/fallout_shared/tesactorbasedata.cpp:1129 |
| 0x0047E4A0 | SaveGame | proven | src/fallout_shared/tesactorbasedata.cpp:2164 |
| 0x0047EA30 | SaveGame | proven | src/fallout_shared/extradatalist.cpp:16566 |
| 0x0047E240 | SetBarterGold | proven | src/fallout_shared/tesactorbasedata.cpp:791 |
| 0x0047DEA0 | SetBaseDisposition | proven | src/staging/blk_00460000_od.cpp:568 |
| 0x0047DE70 | SetCalcLevelMax | proven | src/fallout_shared/tesactorbasedata.cpp:665 |
| 0x0047DE40 | SetCalcLevelMin | proven | src/fallout_shared/tesactorbasedata.cpp:648 |
| 0x005CD8F0 | SetEssential | proven | src/fallout_shared/tesscriptfunctions.cpp:1048 |
| 0x0047E010 | SetFatigue | proven | src/fallout_shared/tesactorbasedata.cpp:699 |
| 0x0047DD30 | SetFlags | proven | src/fallout_shared/tesactorbasedata.cpp:632 |
| 0x0047E1C0 | SetKarma | proven | src/fallout_shared/tesactorbasedata.cpp:771 |
| 0x0047DFE0 | SetLevel | proven | src/fallout_shared/tesactorbasedata.cpp:682 |
| 0x005D1070 | SetMatchesPCLevel | proven | src/fallout_shared/tesscriptfunctions.cpp:1054 |
| 0x0047EAD0 | SetPCFactionFlags | proven | src/staging/blk_00460000_od.cpp:2565 |
| 0x005F7B50 | SetRunsInLow | proven | src/fallout_shared/tesactorbasedata.cpp:900 |
| 0x0047E270 | SetSpeedMult | proven | src/fallout_shared/tesactorbasedata.cpp:807 |
| 0x0047C700 | TESActorBaseData | proven | src/fallout_shared/tesactorbasedata.cpp:25 |
| 0x0047C880 | ~TESActorBaseData | proven | src/fallout_shared/tesactorbasedata.cpp:42 |

### TESAIForm (34)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0047F790 | AddFormChange | proven | src/fallout_shared/tesaiform.cpp:589 |
| 0x0047F190 | BaseFormRecord | class | src/fallout_shared/tesaiform.cpp:12 |
| 0x0047F300 | CompareComponent | proven | src/fallout_shared/tesaiform.cpp:636 |
| 0x0047F1E0 | CopyAIData | proven | src/fallout_shared/tesaiform.cpp:80 |
| 0x0047F2D0 | CopyAIPackageList | proven | src/fallout_shared/packagelist.cpp:49 |
| 0x0047EDE0 | FreeDataComponent | class | src/fallout_shared/tesaiform.cpp:6 |
| 0x0047EE30 | GetAssistance | proven | src/fallout_shared/tesaiform.cpp:106 |
| 0x0047EEB0 | GetConfidenceLevel | proven | src/fallout_shared/tesaiform.cpp:487 |
| 0x0047F520 | GetCurrentPackage | proven | src/fallout_shared/tesaiform.cpp:23 |
| 0x0047F590 | GetMissedPackages | proven | src/fallout_shared/tesaiform.cpp:39 |
| 0x0062F2F0 | GetMood | proven | src/fallout_shared/tesaiform.cpp:426 |
| 0x0047EFE0 | GetOffersService | proven | src/fallout_shared/tesaiform.cpp:524 |
| 0x0047EF30 | GetResponsibility | proven | src/fallout_shared/tesaiform.cpp:156 |
| 0x0047F7E0 | GetSaveSize | proven | src/fallout_shared/tesaiform.cpp:500 |
| 0x0047F000 | GetTrainingSkill | proven | src/fallout_shared/tesaiform.cpp:192 |
| 0x0047ED10 | InitializeComponent | class | src/fallout_shared/tesaiform.cpp:54 |
| 0x0047F4C0 | InitItem | proven | src/fallout_shared/tesaiform.cpp:369 |
| 0x0047F980 | LoadGame | proven | src/fallout_shared/extradatalist.cpp:14200 |
| 0x0047F940 | SaveGame | proven | src/fallout_shared/extradatalist.cpp:14168 |
| 0x0047F600 | SellBuysItem | proven | src/fallout_shared/tesaiform.cpp:710 |
| 0x0047EE00 | SetAggression | proven | src/fallout_shared/tesaiform.cpp:96 |
| 0x0047EE90 | SetAggroRadius | proven | src/fallout_shared/tesaiform.cpp:129 |
| 0x0047F0B0 | SetAIData | proven | src/fallout_shared/tesaiform.cpp:218 |
| 0x0047EE50 | SetAssistance | proven | src/fallout_shared/tesaiform.cpp:113 |
| 0x0047EED0 | SetConfidence | proven | src/fallout_shared/tesaiform.cpp:136 |
| 0x0047EF00 | SetEnergy | proven | src/fallout_shared/tesaiform.cpp:146 |
| 0x0047EE70 | SetHasAggroRadius | proven | src/fallout_shared/tesaiform.cpp:121 |
| 0x0047EF80 | SetMood | proven | src/fallout_shared/tesaiform.cpp:172 |
| 0x0047EF50 | SetResponsibility | proven | src/fallout_shared/tesaiform.cpp:162 |
| 0x0047EFB0 | SetServiceFlags | proven | src/fallout_shared/tesaiform.cpp:182 |
| 0x0047F020 | SetTrainingSkill | proven | src/fallout_shared/tesaiform.cpp:200 |
| 0x0047F090 | SetTrainingSkillLevel | proven | src/fallout_shared/tesaiform.cpp:211 |
| 0x0047EC40 | TESAIForm | proven | src/fallout_shared/tesaiform.cpp:452 |
| 0x0047ECB0 | ~TESAIForm | proven | src/fallout_shared/tesaiform.cpp:478 |

### TESAnimation (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0047FD20 | AddKFFile | proven | src/fallout_shared/tesanimation.cpp:133 |
| 0x0047FA50 | ClearComponent | class | src/fallout_shared/tesanimation.cpp:14 |
| 0x0047FB50 | CopyComponent | proven | src/fallout_shared/tesanimation.cpp:199 |
| 0x0047FD90 | HasKFFiles | proven | src/fallout_shared/tesanimation.cpp:25 |
| 0x0047FAA0 | LoadAnimationChunk | proven | src/fallout_shared/tesanimation.cpp:39 |
| 0x0047F9C0 | TESAnimation | proven | src/fallout_shared/tesanimation.cpp:79 |
| 0x0047F9F0 | ~TESAnimation | proven | src/fallout_shared/tesanimation.cpp:7 |

### TESAttributes (17)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00480070 | CompareComponent | proven | src/fallout_shared/tesattributes.cpp:207 |
| 0x005F1270 | FUN_005f1270 | unnamed | src/staging/blk_005e0000_od.cpp:438 |
| 0x005F14D0 | FUN_005f14d0 | unnamed | src/staging/blk_005e0000_od.cpp:494 |
| 0x005F14F0 | FUN_005f14f0 | unnamed | src/staging/blk_005e0000_od.cpp:507 |
| 0x005F1530 | FUN_005f1530 | unnamed | src/staging/blk_005e0000_od.cpp:537 |
| 0x005F1570 | FUN_005f1570 | unnamed | src/staging/blk_005e0000_od.cpp:568 |
| 0x00480160 | GetAttributeValue | proven | src/fallout_shared/tesattributes.cpp:43 |
| 0x005F1230 | GetEndurance | proven | src/fallout_shared/tesnpc.cpp:2037 |
| 0x0047FFC0 | InitializeComponent | class | src/fallout_shared/tesattributes.cpp:13 |
| 0x00480130 | Load | proven | src/fallout_shared/tesattributes.cpp:31 |
| 0x004802B0 | LoadGame | proven | src/fallout_shared/extradatalist.cpp:14235 |
| 0x00480100 | Save | proven | src/fallout_shared/tesattributes.cpp:58 |
| 0x00480270 | SaveGame | proven | src/fallout_shared/extradatalist.cpp:16592 |
| 0x005F1550 | SetAttribute | decomp | src/staging/blk_005e0000_od.cpp:554 |
| 0x00480180 | SetAttributeValue | proven | src/fallout_shared/tesattributes.cpp:251 |
| 0x0047FF70 | TESAttributes | proven | src/fallout_shared/tesattributes.cpp:6 |
| 0x0047FFA0 | ~TESAttributes | proven | src/fallout_shared/tesspelllist.cpp:27 |

### TESClass (13)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F66E0 | 'scalar deleting destructor' | proven | src/fallout_shared/tesclass.cpp:302 |
| 0x005F6CF0 | Compare | proven | src/fallout_shared/tesclass.cpp:398 |
| 0x005F6DD0 | GetTrainingSkill | proven | src/fallout_shared/tesclass.cpp:184 |
| 0x005F6E60 | IsGuard | proven | src/fallout_shared/magic/ingredientitem_h_unit.cpp: |
| 0x005A5F40 | IsTagSkill | proven | src/fallout_shared/tesconditionfunctions.cpp:98 |
| 0x005F6930 | Load | class | src/fallout_shared/tesclass.cpp:35 |
| 0x005F7050 | LoadGame | proven | src/staging/blk_005e0000_od.cpp:5695 |
| 0x005F71C0 | LoadGame | class | src/fallout_shared/tesclass.cpp:24 |
| 0x005F67C0 | ResetFormData | class | src/fallout_shared/tesclass.cpp:16 |
| 0x005F6810 | SaveForm | proven | src/fallout_shared/tesclass.cpp:273 |
| 0x005F6F70 | SaveGame | proven | src/staging/blk_005e0000_od.cpp:1767 |
| 0x005F6E80 | SetTagSkill | proven | src/fallout_shared/tesclass.cpp:6 |
| 0x005F6610 | TESClass | proven | src/staging/blk_005e0000_od.cpp:5388 |

### TESCombatStyle (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00505080 | 'scalar deleting destructor' | proven | src/fallout_shared/tescombatstyle.cpp:125 |
| 0x00505000 | GetDefaultCombatStyle | proven | src/staging/blk_00500000_od.cpp:541 |
| 0x009989D0 | GetIgnoreThreats | proven | src/fallout/ai/combat/combatstate.cpp:692 |
| 0x009D32E0 | GetRandomCoverWaitTimer | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:118 |
| 0x009D3340 | GetRandomValue | decomp | src/fallout/ai/combat/combatprocedurebeincover.cpp:149 |
| 0x00505180 | Load | class | src/fallout_shared/tescombatstyle.cpp:32 |
| 0x005050D0 | ResetFormData | class | src/fallout_shared/tescombatstyle.cpp:12 |
| 0x005053C0 | SaveForm | proven | src/fallout_shared/tescombatstyle.cpp:151 |
| 0x00505010 | TESCombatStyle | proven | src/fallout_shared/tescombatstyle.cpp:5 |
| 0x005050B0 | ~TESCombatStyle | proven | src/fallout_shared/teseffectshader.cpp:175 |

### TESCreature (37)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F75B0 | 'scalar deleting destructor' | proven | src/fallout_shared/tescreature.cpp:308 |
| 0x005FB330 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/tescreature.cpp:625 |
| 0x005FA120 | CanWearItem | proven | src/staging/blk_005e0000_od.cpp:3294 |
| 0x005FBDD0 | CheckEmbeddedWeaponNodes | proven | src/staging/blk_005e0000_od.cpp:3323 |
| 0x005F7B80 | ClearData | class | src/fallout_shared/tescreature.cpp:12 |
| 0x005F9B90 | Compare | proven | src/fallout_shared/tescreature_rtti_variant_decl_variant.cpp:13 |
| 0x005FB450 | CopyFromTemplateForm | decomp | src/fallout_shared/tesattackdamageform.cpp:28 |
| 0x00605410 | Create3DModel | class | src/fallout_shared/tesobject.cpp:115 |
| 0x005F9210 | CreateCreatureSounds | proven | src/fallout_shared/tescreature.cpp:48 |
| 0x00567470 | GetBaseScale | proven | src/fallout_shared/tesobjectrefr.cpp:2369 |
| 0x005FA2E0 | GetBodyPartData | class | src/fallout_shared/tescreature.cpp:89 |
| 0x005F8F70 | GetCombatSkill | proven | src/fallout_shared/tesmodellist.cpp:163 |
| 0x005F91D0 | GetCreatureSounds | proven | src/fallout_shared/tescreature.cpp:176 |
| 0x0059F3A0 | GetCreatureType | proven | src/fallout/interface/interface.cpp:273 |
| 0x005F9B30 | GetImpactDataSet | proven | src/fallout_shared/tescreature.cpp:213 |
| 0x005FB180 | GetSaveSize | proven | src/fallout_shared/tescreature.cpp:600 |
| 0x005F9100 | GetSoundCreature | proven | src/fallout_shared/tescreature.cpp:158 |
| 0x005FBEB0 | GetSoundLevelValue | proven | src/staging/blk_005e0000_od.cpp:1574 |
| 0x005F90C0 | GetTiltFrontBack | proven | src/fallout_shared/tescreature.cpp:413 |
| 0x005F90E0 | GetTiltLeftRight | proven | src/fallout_shared/tescreature.cpp:424 |
| 0x005F9E00 | InitDefaultWorn | proven | src/fallout_shared/tescreature.cpp:2500 |
| 0x005F9340 | InitItem | proven | src/fallout_shared/tescreature_rtti2_variant.cpp:255 |
| 0x005FBF20 | IsHumanoidCreature | proven | src/fallout/ai/actor.cpp:33712 |
| 0x005F7EC0 | Load | proven | src/fallout_shared/tescreature.cpp:1916 |
| 0x005FB3B0 | LoadGame | class | src/fallout_shared/tescreature.cpp:59 |
| 0x005FB270 | LoadGame2 | proven | src/fallout_shared/tescreature_rtti2_variant.cpp:372 |
| 0x005F92D0 | PickCreatureSound | proven | src/fallout_shared/extradatalist.cpp:5762 |
| 0x005F7A40 | ResetFormData | class | src/fallout_shared/tescreature.cpp:23 |
| 0x005FB430 | Revert | class | src/fallout_shared/tescreature.cpp:103 |
| 0x005FB1E0 | SaveGame | proven | src/fallout_shared/tescreature.cpp:1117 |
| 0x005FA200 | SetActorValue | proven | src/fallout_shared/tescreature.cpp:1059 |
| 0x005FA310 | SetBodyPartData | class | src/fallout_shared/tescreature.cpp:97 |
| 0x005F8BB0 | SetImpactDataSet | proven | src/fallout_shared/tescreature.cpp:146 |
| 0x005F9140 | SetSoundCreature | proven | src/fallout_shared/tescreature.cpp:71 |
| 0x005F7230 | TESCreature | proven | src/fallout_shared/tescreature.cpp:109 |
| 0x005F8C70 | UnClone3D | proven | src/fallout_shared/tesobject.cpp:2160 |
| 0x005F7900 | ~TESCreature | decomp | src/fallout_shared/tescreature.cpp:6 |

### TESEyes (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005FC0F0 | 'scalar deleting destructor' | proven | src/fallout_shared/teseyes.cpp:136 |
| 0x005FC5F0 | CanBeEyesForNPC | proven | src/fallout_shared/teseyes.cpp:236 |
| 0x005FC590 | CanBeFemale | proven | src/fallout_shared/teseyes.cpp:91 |
| 0x005FC530 | CanBeMale | proven | src/fallout_shared/teseyes.cpp:76 |
| 0x005FC1B0 | InitializeData | proven | src/fallout_shared/testexture.cpp:161 |
| 0x005FC1D0 | SaveForm | proven | src/fallout_shared/teseyes.cpp:172 |
| 0x005FC050 | TESEyes | proven | src/fallout_shared/teseyes.cpp:36 |
| 0x005FC120 | ~TESEyes | proven | src/staging/blk_005e0000_od.cpp:3394 |

### TESFaction (28)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005FC730 | 'scalar deleting destructor' | proven | src/fallout_shared/tesfaction.cpp:372 |
| 0x005FDA50 | AddMajorCrime | proven | src/fallout/ai/alarmpackage.cpp:217 |
| 0x005FDA00 | AddMinorCrime | proven | src/fallout_shared/tesfaction.cpp:662 |
| 0x005FD690 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/tesfaction.cpp:746 |
| 0x005FD850 | CheckFactionReactions | proven | src/fallout_shared/tesfaction.cpp:787 |
| 0x005FC840 | ClearData | proven | src/fallout_shared/tesfaction.cpp:9 |
| 0x005FD210 | CopyFrom | proven | src/fallout_shared/tesfaction.cpp:703 |
| 0x0047D7C0 | GetEvil | proven | src/fallout_shared/tesactorbasedata.cpp:1108 |
| 0x005FD3B0 | GetFactionReaction | proven | src/fallout_shared/tesfaction.cpp:186 |
| 0x005A2270 | GetPCAnEnemy | proven | src/fallout_shared/tesconditionfunctions.cpp:91 |
| 0x005FCF80 | InitItem | proven | src/fallout_shared/tesfaction.cpp:55 |
| 0x005FD7D0 | InitLoadGame | class | src/fallout_shared/tesfaction.cpp:25 |
| 0x005FD660 | InitLoadGameTES | proven | src/fallout_shared/tesfaction.cpp:623 |
| 0x005FD730 | LoadGame | proven | src/fallout_shared/tesfaction.cpp:72 |
| 0x005FD610 | LoadGame2 | proven | src/fallout_shared/tesfaction.cpp:492 |
| 0x005FD400 | ModFactionReaction | proven | src/fallout_shared/tesfaction.cpp:600 |
| 0x005FC800 | ResetFormData | class | src/fallout_shared/tesfaction.cpp:15 |
| 0x005FD800 | Revert | proven | src/fallout_shared/tesfaction.cpp:32 |
| 0x005FD5C0 | SaveGame | proven | src/fallout_shared/tesfaction.cpp:467 |
| 0x005FD430 | SetFactionFightReaction | proven | src/fallout_shared/tesfaction.cpp:222 |
| 0x005FD3D0 | SetFactionReaction | proven | src/fallout_shared/tesfaction.cpp:563 |
| 0x005FC970 | SetFlag | proven | src/fallout_shared/tesfaction.cpp:527 |
| 0x0047EB90 | SetPCAnEnemy | proven | src/staging/blk_00460000_od.cpp:1760 |
| 0x0047EBD0 | SetPCAttacked | proven | src/staging/blk_00460000_od.cpp:593 |
| 0x005CE040 | SetPCExpelled | proven | src/fallout_shared/tesscriptfunctions.cpp:5286 |
| 0x0047EBB0 | SetPCMurdered | proven | src/staging/blk_00460000_od.cpp:581 |
| 0x005FC680 | TESFaction | proven | src/fallout_shared/tesfaction.cpp:355 |
| 0x005FC760 | ~TESFaction | proven | src/fallout_shared/tesfaction.cpp:855 |

### TESFaction_RankDataView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0077A590 | HasFlag40 | decomp | src/staging/blk_00760000_od.cpp:393 |

### TESHair (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005FDB60 | 'scalar deleting destructor' | proven | src/fallout_shared/teshair.cpp:175 |
| 0x005FDFA0 | CanBeHairForNPC | proven | src/fallout_shared/teshair.cpp:92 |
| 0x005FDED0 | Compare | proven | src/fallout_shared/teshair.cpp:228 |
| 0x005FDC30 | InitializeData | proven | src/fallout_shared/testexture.cpp:172 |
| 0x005FDCB0 | Load | class | src/fallout_shared/teshair.cpp:16 |
| 0x005FDC50 | SaveForm | proven | src/fallout_shared/teshair.cpp:211 |
| 0x005FDAA0 | TESHair | proven | src/fallout_shared/teshair.cpp:8 |

### TESLevCharacter (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0050A820 | 'scalar deleting destructor' | proven | src/fallout_shared/teslevcharacter.cpp:249 |
| 0x0050ACF0 | Compare | proven | src/fallout_shared/teslevcharacter.cpp:282 |
| 0x0050ACB0 | CopyFrom | proven | src/fallout_shared/teslevcharacter.cpp:264 |
| 0x0050A930 | Load | class | src/fallout_shared/teslevcharacter.cpp:24 |
| 0x0050A770 | TESLevCharacter | proven | src/fallout_shared/teslevcharacter.cpp:234 |
| 0x0050A850 | ~TESLevCharacter | proven | src/staging/blk_00500000_od.cpp:1471 |

### TESLevCreature (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0050AEA0 | 'scalar deleting destructor' | proven | src/fallout_shared/teslevcreature.cpp:130 |
| 0x0050B320 | Compare | proven | src/fallout_shared/teslevcreature.cpp:254 |
| 0x0050B2E0 | CopyFrom | proven | src/fallout_shared/teslevcreature.cpp:233 |
| 0x0050AD40 | InitItem | decomp | src/fallout_shared/teslevcharacter.cpp:6 |
| 0x0050AF60 | Load | class | src/fallout_shared/teslevcreature.cpp:5 |
| 0x0050ADF0 | TESLevCreature | proven | src/fallout_shared/teslevcreature.cpp:115 |
| 0x0050AED0 | ~TESLevCreature | proven | src/fallout_shared/teslevcreature.cpp:220 |

### TESLeveledList (22)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00487A60 | AddLeveledObject | proven | src/staging/blk_00480000_od.cpp:2103 |
| 0x00487A00 | AddScriptAddedLeveledObject | proven | src/fallout_shared/tesmodel.cpp:254 |
| 0x00487D00 | CalculateCurrentForm | proven | src/fallout_shared/tesleveledlist.cpp:163 |
| 0x00487F70 | CalculateCurrentFormList | proven | src/fallout_shared/tesleveledlist.cpp:30 |
| 0x00488350 | CalculateCurrentFormListForRef | proven | src/fallout_shared/tesleveledlist.cpp:725 |
| 0x00487770 | ClearComponent | class | src/fallout_shared/tesleveledlist.cpp:17 |
| 0x004889D0 | CompareComponent | proven | src/fallout_shared/tesleveledlist.cpp:1589 |
| 0x004887A0 | CopyComponent | proven | src/fallout_shared/tesleveledlist.cpp:1721 |
| 0x0042E680 | FUN_0042e680 | probable | src/fallout_shared/containeritemextra.cpp:120 |
| 0x004877E0 | GetCalcAllBelow | proven | src/fallout_shared/tesleveledlist.cpp:444 |
| 0x00487790 | GetChanceNone | proven | src/fallout_shared/tesleveledlist.cpp:571 |
| 0x00487BE0 | GetFormAsLeveledList | proven | src/fallout_shared/tescontainer.cpp:441 |
| 0x00487840 | GetMultCalc | proven | src/fallout_shared/tesleveledlist.cpp:683 |
| 0x004878A0 | GetUseAll | proven | src/fallout_shared/tesleveledlist.cpp:453 |
| 0x00487740 | InitializeComponent | class | src/fallout_shared/tesleveledlist.cpp:9 |
| 0x00487900 | InitializeLeveledList | decomp | src/fallout_shared/tesleveledlist.cpp:418 |
| 0x00488570 | InitItem | proven | src/fallout_shared/tesleveledlist.cpp:275 |
| 0x00488D70 | LoadGame | proven | src/fallout_shared/tesleveledlist.cpp:352 |
| 0x00488F10 | Revert | decomp | src/fallout_shared/tesleveledlist.cpp:23 |
| 0x00488400 | Save | proven | src/fallout_shared/tesleveledlist.cpp:1419 |
| 0x00487650 | TESLeveledList | proven | src/staging/blk_00480000_od.cpp:2074 |
| 0x004876D0 | ~TESLeveledList | proven | src/staging/blk_00480000_od.cpp:1544 |

### TESNPC (47)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00601370 | 'scalar deleting destructor' | proven | src/fallout_shared/tesnpc.cpp:2208 |
| 0x00607990 | Activate | proven | src/fallout_shared/tesnpc.cpp:7977 |
| 0x00608F00 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/tesnpc.cpp:7866 |
| 0x00607420 | AttachHead | proven | src/fallout_shared/tesnpc.cpp:936 |
| 0x00601750 | ClearData | class | src/fallout_shared/tesnpc.cpp:55 |
| 0x005DD560 | ClearHead | proven | src/fallout_shared/tesnpc_h_unit.cpp: |
| 0x00603790 | CopyHeadData | proven | src/fallout_shared/tesnpc.cpp:503 |
| 0x006055F0 | CreateBipedAnim | proven | src/fallout_shared/tesnpc.cpp:730 |
| 0x00603280 | FillCharGenPresetList | proven | src/fallout_shared/tesnpc.cpp:3334 |
| 0x00609BF0 | FindInFileFast | proven | src/fallout_shared/tesnpc.cpp:2117 |
| 0x006062E0 | FixDisplayedHeadParts | proven | src/fallout_shared/tesnpc.cpp:784 |
| 0x006056F0 | FixNPCNormals | proven | src/bsshader/shadowscenenode_od_variant_ctxr_variant.cpp:466 |
| 0x00607850 | GetActorValue | probable | src/fallout_shared/tesraceform.cpp:34 |
| 0x00607950 | GetCombatStyle | class | src/fallout_shared/tesnpc.cpp:1019 |
| 0x00603AD0 | GetFaceCoord | proven | src/fallout_shared/tesnpc.cpp:523 |
| 0x00607370 | GetFaceGenNodes | probable | src/fallout_shared/tesnpc.cpp:924 |
| 0x006044C0 | GetFaceNPC | proven | src/fallout_shared/tesnpc.cpp:1282 |
| 0x00603FC0 | GetFormHealthLeveled | proven | src/fallout_shared/tesnpc.cpp:3448 |
| 0x00603B50 | GetHair | proven | src/fallout_shared/tesnpc.cpp:536 |
| 0x00602130 | GetHairLength | proven | src/fallout_shared/tesnpc.cpp:1189 |
| 0x006044E0 | GetHeadPartModTexture | proven | src/fallout_shared/tesnpc.cpp:2530 |
| 0x00601800 | GetOffsetFaceCoord | proven | src/fallout_shared/tesnpc.cpp:1160 |
| 0x004AC110 | GetRace | proven | src/fallout_shared/bipedanim.cpp:802 |
| 0x006041D0 | GetRaceHeight | proven | src/fallout_shared/tesnpc.cpp:631 |
| 0x00608DA0 | GetSaveSize | proven | src/fallout_shared/tesnpc.cpp:2189 |
| 0x00604250 | GetWeight | proven | src/fallout_shared/tesnpc.cpp:3597 |
| 0x006047C0 | InitDefaultWorn | proven | src/fallout_shared/tesnpc_decl_variant.cpp:9 |
| 0x00603370 | InitItem | proven | src/fallout_shared/tesnpc.cpp:427 |
| 0x0060A890 | InitLoadFaceGen | proven | src/fallout_shared/tesnpc.cpp:4157 |
| 0x00606540 | InitParts | proven | src/fallout_shared/tesnpc.cpp:854 |
| 0x006061B0 | InitWornObject | proven | src/fallout_shared/tesnpc.cpp:747 |
| 0x00602190 | Load | proven | src/fallout_shared/tesnpc.cpp:69 |
| 0x00609F60 | LoadFaceGen | proven | src/fallout_shared/tesnpc_ctx_variant.cpp:309 |
| 0x00609220 | LoadGame | proven | src/fallout_shared/tesnpc.cpp:7622 |
| 0x00608E80 | LoadGame2 | proven | src/fallout_shared/tesnpc.cpp:2616 |
| 0x00601830 | RandomizeFaceCoord | proven | src/fallout_shared/tesnpc.cpp:4391 |
| 0x00605D70 | ReplaceRefModel | proven | src/fallout_shared/tesnpc.cpp:1494 |
| 0x00609D60 | SaveFaceGen | proven | src/fallout_shared/tesnpc.cpp:6497 |
| 0x00608E00 | SaveGame | proven | src/fallout_shared/tesnpc.cpp:2582 |
| 0x006078E0 | SetActorValue | proven | src/fallout_shared/tescreature.cpp:485 |
| 0x00601C70 | SetClass | proven | src/fallout_shared/tesnpc.cpp:2049 |
| 0x00607970 | SetCombatStyle | class | src/fallout_shared/tesnpc.cpp:1025 |
| 0x00603200 | SetEyeColor | proven | src/fallout_shared/tesnpc.cpp:1222 |
| 0x006031E0 | SetHair | proven | src/fallout_shared/tesnpc.cpp:1211 |
| 0x0060A950 | SwapEyes | proven | src/fallout_shared/tesnpc_ctx_variant.cpp:676 |
| 0x00601170 | TESNPC | proven | src/fallout_shared/tesnpc.cpp:6 |
| 0x006055D0 | UnClone3D | proven | src/fallout_shared/tesobject.cpp:879 |

### TESRace (39)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00610470 | 'scalar deleting destructor' | proven | src/fallout_shared/tesrace.cpp:622 |
| 0x00613910 | AddEyeColor | proven | src/bscore/bssimplelist_h_unit.cpp:250 |
| 0x00613810 | AddHair | proven | src/bscore/bssimplelist_h_unit.cpp:197 |
| 0x00610AC0 | ClearData | proven | src/fallout_shared/tesrace.cpp:765 |
| 0x00613950 | ClearEyeColorList | proven | src/fallout_shared/tesrace.cpp:656 |
| 0x00613850 | ClearHairList | proven | src/fallout_shared/tesrace.cpp:640 |
| 0x00613C50 | CreateHead | proven | src/fallout_shared/tesrace.cpp:2260 |
| 0x00969910 | FUN_00969910 | unnamed | src/staging/blk_00960000_od.cpp:148 |
| 0x006151F0 | GetBipedObjectModel | decomp | src/fallout_shared/tesrace.cpp:118 |
| 0x006147E0 | GetBodyModTextureName | proven | src/fallout_shared/tesrace.cpp:94 |
| 0x00613A20 | GetBodyPartModel | proven | src/fallout_shared/tesrace.cpp:234 |
| 0x00613BB0 | GetBodyPartTexture | proven | src/fallout_shared/tesrace.cpp:751 |
| 0x006149B0 | GetBodyTexture | proven | src/fallout_shared/tesrace.cpp:2362 |
| 0x00614640 | GetBodyTextureFileName | proven | src/fallout_shared/tesrace.cpp:141 |
| 0x006131A0 | GetBodyTextureModel | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:19 |
| 0x00613120 | GetClampFaceGeoValue | proven | src/fallout_shared/tesrace.cpp:714 |
| 0x00613160 | GetClampFaceGeoValue2 | proven | src/fallout_shared/tesrace.cpp:728 |
| 0x00613870 | GetDefaultHair | proven | src/staging/blk_00600000_od.cpp:222 |
| 0x00613100 | GetDefaultHairColor | proven | src/fallout_shared/tesrace.cpp:567 |
| 0x00604780 | GetDefaultVoiceType | proven | src/fallout_shared/tesnpc.cpp:2084 |
| 0x006141F0 | GetFaceGenData | proven | src/fallout_shared/tesrace.cpp:2017 |
| 0x00613970 | GetHeadPartModel | proven | src/fallout_shared/tesrace.cpp:220 |
| 0x00605D40 | GetHeadPartNodeName | proven | src/staging/blk_00600000_od.cpp:543 |
| 0x00613B20 | GetHeadPartTexture | proven | src/fallout_shared/tesrace.cpp:248 |
| 0x005D9FB0 | GetMeanFaceCoord | proven | src/fallout_shared/tesscriptfunctions.cpp:2156 |
| 0x0059F610 | GetPlayable | proven | src/fallout_shared/tesconditionfunctions.cpp:5451 |
| 0x006138B0 | GetRaceEyeColor | proven | src/bscore/bssimplelist_h_unit.cpp:220 |
| 0x006137B0 | GetRaceHair | proven | src/bscore/bssimplelist_h_unit.cpp:168 |
| 0x006128C0 | InitItem | class | src/fallout_shared/tesrace.cpp:29 |
| 0x00613FD0 | KillEGTData | proven | src/fallout_shared/tesrace.cpp:176 |
| 0x00610CD0 | Load | proven | src/fallout_shared/tesrace.cpp:2640 |
| 0x00613A60 | SetBodyPartModel | proven | src/fallout_shared/tesrace.cpp:1870 |
| 0x00613C00 | SetBodyPartTexture | proven | src/fallout_shared/tesrace.cpp:697 |
| 0x00613AD0 | SetBodyTextureModel | proven | src/fallout_shared/tesrace.cpp:1155 |
| 0x00611E30 | SetDefaultHairColor | decomp | src/fallout_shared/tesrace.cpp:6 |
| 0x00610C70 | SetDefaultVoiceType | proven | src/fallout_shared/tesrace.cpp:13 |
| 0x006139B0 | SetHeadPartModel | proven | src/fallout_shared/tesrace.cpp:977 |
| 0x00613B60 | SetHeadPartTexture | proven | src/fallout_shared/tesrace.cpp:679 |
| 0x00610210 | TESRace | proven | src/fallout_shared/tesrace.cpp:169 |

### TESRaceForm (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048B870 | BaseFormRecord | class | src/fallout_shared/tesraceform.cpp:53 |
| 0x00617270 | GetFormRace | proven | src/staging/blk_00600000_od.cpp:2268 |
| 0x0048B920 | InitItem | proven | src/fallout_shared/tesraceform.cpp:7 |
| 0x0048B830 | Save | proven | src/staging/blk_00480000_od.cpp:670 |
| 0x0048B800 | TESRaceForm | proven | src/staging/blk_00480000_od.cpp:179 |

### TESSkill (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00617E50 | 'scalar deleting destructor' | proven | src/fallout_shared/tesskill.cpp:58 |
| 0x00618430 | Compare | proven | src/fallout_shared/tesskill.cpp:493 |
| 0x00617E80 | InitializeData | proven | src/fallout_shared/testexture.cpp:184 |
| 0x00618130 | Load | proven | src/fallout_shared/tesskill.cpp:339 |
| 0x00617EA0 | ResetData | proven | src/fallout_shared/tesskill.cpp:75 |
| 0x00617FC0 | SaveForm | proven | src/fallout_shared/tesskill.cpp:119 |
| 0x00617DA0 | TESSkill | proven | src/tesreputation.cpp:493 |
| 0x00617F40 | ~TESSkill | proven | src/tesreputation.cpp:527 |

### (free functions) (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B8360 | CollectFilteredFactions | probable | src/fallout/ai/actor.cpp:81753 |
| 0x0047CA20 | CopyFactionRanks | decomp | src/fallout_shared/tesactorbasedata.cpp:939 |
| 0x005F6D70 | CopyFromTESClass | class | src/fallout_shared/tesclass.cpp:322 |
| 0x004FECF0 | CopyVoiceTypeFromActivator | class | src/fallout_shared/bgstalkingactivator.cpp:356 |
| 0x0042E4A0 | EnsureLeveledListExtra | decomp | src/fallout_shared/extradatalist.cpp:13933 |
| 0x004A8AB0 | GetActorBaseFatigue | decomp | src/staging/blk_004a0000_od.cpp:271 |
| 0x008B7E20 | GetFactionRankSum | decomp | src/fallout/ai/actor.cpp:81644 |
| 0x0047D720 | HasFactionFlag8 | decomp | src/fallout_shared/tesactorbasedata.cpp:1096 |
| 0x0047C8E0 | InitActorBaseData | class | src/fallout_shared/tesactorbasedata.cpp:115 |
| 0x00488C50 | SaveLeveledListEntries | decomp | src/fallout_shared/tesleveledlist.cpp:1279 |

## 4 Process levels and the AI update loop

Every actor has a process (High, MiddleHigh, MiddleLow, Low). ProcessLists updates them each frame. This is where the cost of more NPCs goes.

### ActorPathingMessageQueue (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DF980 | 'scalar deleting destructor' | proven | src/staging/blk_008c0000_od.cpp:889 |
| 0x008DF900 | ActorPathingMessageQueue | proven | src/gamebryo2.2/corelibs/nimain/nismartpointer_h_unit.cpp: |

### ActorsScriptTaskData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9050 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:415 |
| 0x008C9020 | ActorsScriptTaskData | proven | src/fallout/ai/aitaskmanager.cpp:401 |
| 0x008C90A0 | FUN_008c90a0 | class | src/fallout/ai/aitaskmanager.cpp:1532 |
| 0x008C9110 | HandleMobMessage | proven | src/fallout/ai/aitaskmanager.cpp:1291 |
| 0x008C9080 | ~ActorsScriptTaskData | proven | src/fallout/ai/aitaskmanager.cpp:431 |

### ActorUpdateTaskData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C89D0 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:262 |
| 0x008C89A0 | ActorUpdateTaskData | proven | src/fallout/ai/aitaskmanager.cpp:250 |
| 0x008C8A70 | UpdateActorTask | class | src/fallout/ai/aitaskmanager.cpp:1927 |
| 0x008C8A00 | ~ActorUpdateTaskData | proven | src/fallout/ai/aitaskmanager.cpp:278 |

### ActorValueModifierList (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937280 | AddFastModifier | decomp | src/fallout/ai/modifierlist.cpp:29 |
| 0x00937160 | CopyModifierListFrom | decomp | src/fallout/ai/modifierlist.cpp:91 |
| 0x00937D50 | FUN_00937d50 | unnamed | src/staging/blk_00920000_od.cpp:103 |
| 0x009376E0 | GetActorValueModifierAmount | decomp | src/fallout/ai/modifierlist.cpp:83 |
| 0x00937730 | GetActorValueModifierAmount | decomp | src/fallout/ai/modifierlist.cpp:75 |
| 0x00937760 | GetModifierItem | decomp | src/fallout/ai/modifierlist.cpp:47 |
| 0x00937480 | ModifyModifier | decomp | src/fallout/ai/modifierlist.cpp:108 |
| 0x009370B0 | RemoveAllModifiers | decomp | src/fallout/ai/modifierlist.cpp:10 |

### AILinearTaskThread (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C7830 | 'scalar deleting destructor' | proven | src/fallout/ai/ailineartaskthread.cpp:92 |
| 0x008C7630 | AILinearTaskThread | proven | src/fallout/ai/ailineartaskthread_h_unit.cpp: |
| 0x008C7190 | ExecuteTask | class | src/bsshader/mtrenderingsystem.cpp:10 |
| 0x008C6FF0 | StartTaskThread | class | src/fallout/ai/ailineartaskthread.cpp:72 |

### AILinearTaskThreadManager (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C7DA0 | AIThread1TaskFunc | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:900 |
| 0x008C7F50 | AIThread2TaskFunc | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:780 |
| 0x008C7BD0 | AIThreadCombined | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:666 |
| 0x008C73A0 | DestroyThreads | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:524 |
| 0x00713D80 | QInstance | proven | src/fallout/interface/interfacemanager.cpp:6957 |

### AITaskManager (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9330 | AITaskManager | proven | src/fallout/ai/aitaskmanager.cpp:2000 |
| 0x008C9430 | ~AITaskManager | proven | src/fallout/ai/aitaskmanager.cpp:964 |

### AITaskThread (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9EC0 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:601 |
| 0x008C9BD0 | AITaskThread | proven | src/fallout/ai/aitaskmanager.cpp:1047 |

### AIThreadManager (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C74D0 | LaunchWorkerThread | decomp | src/fallout/ai/ailineartaskthreadmanager.cpp:103 |
| 0x008C80E0 | SetThreadingEnabled | decomp | src/fallout/ai/ailineartaskthreadmanager.cpp:125 |
| 0x008C7290 | StartRenderingTaskThread | decomp | src/fallout/ai/ailineartaskthreadmanager.cpp:75 |

### AnimationTaskData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8860 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:174 |
| 0x008C8830 | AnimationTaskData | proven | src/fallout/ai/aitaskmanager.cpp:159 |
| 0x008C8910 | HandleMobMessage | proven | src/fallout/ai/aitaskmanager.cpp:1215 |
| 0x008C8890 | ~AnimationTaskData | proven | src/fallout/ai/aitaskmanager.cpp:190 |

### BaseProcess (29)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D0610 | 'scalar deleting destructor' | proven | src/fallout/ai/baseprocess.cpp:1954 |
| 0x008D0380 | AddQueuedItem | proven | src/fallout/ai/baseprocess.cpp:838 |
| 0x008D1050 | ApplyLoadBuffer | class | src/fallout/ai/baseprocess.cpp:15 |
| 0x008D0270 | BaseProcess | proven | src/staging/blk_008c0000_od.cpp:694 |
| 0x008D0660 | Copy | class | src/fallout/ai/baseprocess.cpp:68 |
| 0x008D0350 | CreateDetectionEvent | proven | src/fallout/ai/baseprocess.cpp:233 |
| 0x008D0E80 | FinishInitLoadGame | proven | src/fallout/ai/baseprocess.cpp:1594 |
| 0x008D0580 | GetActorValueF | proven | src/fallout/ai/baseprocess.cpp:902 |
| 0x008D0570 | GetActorValueI | proven | src/fallout/ai/baseprocess.cpp:892 |
| 0x008D0540 | GetAttackChance | class | src/fallout/ai/baseprocess.cpp:8 |
| 0x00717E50 | GetCurrentProcessData | class | src/fallout_shared/teleportdata.cpp:6 |
| 0x00859670 | GetOneTimePackage | class | src/fallout/ai/baseprocess_h_unit.cpp: |
| 0x008D0450 | GetPackageInfoValue | class | src/fallout/ai/baseprocess_h_unit.cpp: |
| 0x008D0900 | GetSaveSize | proven | src/fallout/ai/baseprocess.cpp:1210 |
| 0x00884920 | HasCachedValues | proven | src/fallout/ai/actor.cpp:3215 |
| 0x008D1000 | InitLoadGame | class | src/fallout/ai/baseprocess.cpp:21 |
| 0x008D0E60 | InitLoadGameTES | proven | src/fallout/ai/baseprocess.cpp:958 |
| 0x008D0F90 | LoadGame | class | src/fallout/ai/baseprocess.cpp:56 |
| 0x008D1070 | Revert | class | src/fallout/ai/baseprocess.cpp:46 |
| 0x008D0F10 | RevertTES | proven | src/fallout/ai/baseprocess.cpp:996 |
| 0x008D0F30 | SaveGameBGS | proven | src/fallout/ai/baseprocess.cpp:977 |
| 0x008D0A10 | SaveGameTES | proven | src/fallout/ai/baseprocess.cpp:1729 |
| 0x008D0470 | SetAnimationState | class | src/fallout/ai/baseprocess_h_unit.cpp: |
| 0x008D08B0 | SetCurrentPackageAndTarget | class | src/fallout/ai/baseprocess.cpp:29 |
| 0x008D0400 | SetPackageExecutionState | class | src/fallout/ai/baseprocess_h_unit.cpp: |
| 0x008D03C0 | SetPackageInfoState | class | src/fallout_shared/extradataobjects.cpp:135 |
| 0x008D0870 | SetReferenceTarget | class | src/fallout/ai/baseprocess.cpp:36 |
| 0x008D03A0 | StopPackage | class | src/fallout/ai/baseprocess_h_unit.cpp: |
| 0x008D0640 | ~BaseProcess | proven | src/fallout/ai/baseprocess.cpp:173 |

### BSPlayerDistanceCheckController (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D1620 | 'scalar deleting destructor' | proven | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:30 |
| 0x008D15D0 | BSPlayerDistanceCheckController | proven | src/staging/blk_008c0000_od.cpp:727 |
| 0x008D1720 | TargetIsRequiredType | proven | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:282 |
| 0x008D1650 | ~BSPlayerDistanceCheckController | proven | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:299 |

### CachedValues (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884E90 | IsDirty | proven | src/fallout/ai/actor.cpp:3451 |

### FurnitureProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092A9B0 | TryUseFurniture | class | src/fallout/ai/middlehighprocess.cpp:29360 |

### HighActorCuller (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00872E00 | HighActorCuller | proven | src/staging/blk_00860000_od.cpp:6245 |
| 0x008D6D40 | Operate | class | src/fallout/ai/highactorculler.cpp:6 |
| 0x008D6F50 | Run | proven | src/staging/blk_008c0000_od.cpp:865 |
| 0x008D6AF0 | ~HighActorCuller | proven | src/staging/blk_008c0000_od.cpp:3800 |

### HighProcess (160)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FF350 | ActorEntity | decomp | src/fallout/ai/highprocess.cpp:2062 |
| 0x00903180 | AddPostAnimAction | class | src/fallout/ai/highprocess.cpp:1556 |
| 0x009004F0 | AlterActorValue | class | src/fallout/ai/highprocess.cpp:1077 |
| 0x008D9260 | AssignLipSyncAnimation | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008DAA20 | CalculateMoveMode | proven | src/fallout/ai/highprocess.cpp:28378 |
| 0x008D92C0 | CanFireWeapon | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008DA670 | CanProcessActor | class | src/fallout/ai/highprocess.cpp:788 |
| 0x008FFE10 | CanUsePlayerAction | class | src/fallout/ai/highprocess.cpp:1511 |
| 0x00901120 | ClearCachedTargetReferences | class | src/fallout/ai/highprocess.cpp:1320 |
| 0x00901200 | ClearCombatHeadTrackTarget | proven | src/fallout/ai/highprocess.cpp:6350 |
| 0x009010F0 | ClearDefaultHeadTrackTarget | proven | src/fallout/ai/highprocess.cpp:6333 |
| 0x00903F90 | ClearDetectionEvents | class | src/fallout/ai/highprocess.cpp:1350 |
| 0x008D9870 | ClearDialogTarget | proven | src/fallout/ai/highprocess.cpp:15088 |
| 0x008DBDC0 | ClearDialogueItems | class | src/fallout/ai/highprocess.cpp:1375 |
| 0x00901050 | ClearHighProcessState | class | src/fallout/ai/highprocess.cpp:1443 |
| 0x008F6EA0 | ClearIdleAnimation | class | src/fallout/ai/highprocess.cpp:1471 |
| 0x00902230 | ClearMuzzleFlash | class | src/fallout/ai/highprocess.cpp:1397 |
| 0x008DA600 | ClearPackageObjectList | class | src/fallout/ai/highprocess.cpp:1364 |
| 0x008D96B0 | ClearPostAnimActions | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008FEC10 | ClearProcessState | decomp | src/fallout/ai/highprocess.cpp:119 |
| 0x00901550 | ClearTrackedActorEntries | decomp | src/fallout/ai/highprocess.cpp:1220 |
| 0x00901800 | ComputeCanInitiateDialogueWithNPC | proven | src/fallout/ai/highprocess.cpp:24625 |
| 0x00903E40 | CreateDetectionEvent | proven | src/fallout/ai/highprocess.cpp:54719 |
| 0x008F7070 | CreateFollownoEscort | proven | src/fallout/ai/highprocess.cpp:19741 |
| 0x00902190 | CreateMuzzleFlash | proven | src/fallout/ai/highprocess.cpp:10685 |
| 0x009005D0 | DamageModActorValueI | proven | src/fallout/ai/highprocess.cpp:10057 |
| 0x008E5730 | EvaluateBoneLod | proven | src/fallout/ai/highprocess.cpp:70601 |
| 0x008FE9E0 | FadeOutAndMove | proven | src/fallout/ai/highprocess.cpp:70025 |
| 0x008D9390 | FindDetectionEventForActor | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F62B0 | FindDetectionRecord | class | src/fallout/ai/highprocess.cpp:922 |
| 0x008DA250 | GetActorProcessTime | class | src/fallout/ai/highprocess.cpp:1574 |
| 0x008D8E60 | GetActorSoundHandle | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x009002B0 | GetActorValue | class | src/fallout/ai/highprocess.cpp:1505 |
| 0x008DA230 | GetAnimAction | class | src/fallout/ai/highprocess.cpp:1568 |
| 0x008D93D0 | GetAvoidActorList | proven | src/fallout/ai/highprocess.cpp:4849 |
| 0x008D97A0 | GetControllerPhase | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x009002F0 | GetCurrentActorValue | class | src/fallout/ai/highprocess.cpp:1036 |
| 0x008D95B0 | GetCurrentAlpha | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D8DE0 | GetCurrentDialogueEmotion | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9670 | GetCurrentDialogueItem | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9610 | GetCurrentFadeState | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D95D0 | GetCurrentProcessAnimIdle | proven | src/fallout/ai/highprocess.cpp:14014 |
| 0x008D8FD0 | GetDetectAlert | proven | src/fallout/ai/highprocess.cpp:13046 |
| 0x008D9740 | GetDetectionProgress | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F6650 | GetDetectionState | class | src/fallout/ai/highprocess.cpp:1261 |
| 0x008D93F0 | GetDetectionStrength | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F6EF0 | GetEmotionsDispostion | proven | src/fallout/ai/highprocess.cpp:18817 |
| 0x008D9320 | GetFirstProcessFloat | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D94F0 | GetLightLevel | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9240 | GetLipSync | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x0051F510 | GetMobileObject | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9300 | GetMuzzleFlash | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9140 | GetPackageEndTimerValue | proven | src/fallout/ai/highprocess.cpp:4825 |
| 0x00904450 | GetPathingAvoidNodeArray | class | src/fallout/ai/highprocess.cpp:1046 |
| 0x008D9720 | GetPlantedExplosive | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x004727D0 | GetPostAnimationAction | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D8E20 | GetPreviousReference | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x009015F0 | GetPrimaryTargetReference | class | src/fallout/ai/highprocess.cpp:1434 |
| 0x00901640 | GetPrimaryTargetReference | class | src/fallout/ai/highprocess.cpp:1562 |
| 0x008D9090 | GetProcessBlendAmount | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D94B0 | GetProcessBlendWeight | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9010 | GetRadiationRate | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9830 | GetRelatedReference | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008FA630 | GetSaveSize | proven | src/fallout/ai/highprocess.cpp:20810 |
| 0x006214B0 | GetSelectedIdleForm | decomp | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9050 | HasAssignedAnimation | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9430 | HasCombatStarted | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F5410 | HasGroupEntry | decomp | src/fallout/ai/highprocess.cpp:18179 |
| 0x00901460 | HasNoPendingEntries | class | src/fallout/ai/highprocess.cpp:1486 |
| 0x00901400 | HasNoPendingEntriesAndExpired | class | src/fallout/ai/highprocess.cpp:1385 |
| 0x008D7510 | HighProcess | proven | src/fallout/ai/highprocess.cpp:1666 |
| 0x008DA1A0 | InitBoneLOD | proven | src/staging/blk_008c0000_od.cpp:960 |
| 0x008FDBD0 | InitLoadGame | class | src/fallout/ai/highprocess.cpp:431 |
| 0x008D92A0 | IsActorTalking | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F6930 | IsActorVisibleToActor | class | src/fallout/ai/highprocess.cpp:1406 |
| 0x008D8DA0 | IsAsleep | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9810 | IsCombatTargetValid | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9650 | IsCurrentlyDetected | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00904800 | IsCurrentPackageTarget | class | src/fallout/ai/highprocess.cpp:1794 |
| 0x008D8F10 | IsDetecting | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9530 | IsDetectionEnabled | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9180 | IsMovementStopped | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D91E0 | IsProcessStateActive | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008F6FC0 | IsTalking | class | src/fallout/ai/highprocess.cpp:1161 |
| 0x008FCE90 | LoadGame | class | src/fallout/ai/highprocess.cpp:233 |
| 0x008D8CA0 | ModNumberGuardsArresting | proven | src/fallout/ai/highprocess.cpp:4730 |
| 0x00903A80 | OnPackageChanged | class | src/fallout/ai/highprocess.cpp:948 |
| 0x00903D10 | OnPackageEnd | class | src/fallout/ai/highprocess.cpp:1134 |
| 0x00903BF0 | OnPackageStart | class | src/fallout/ai/highprocess.cpp:1110 |
| 0x008DAFD0 | PlayRandomIdle | class | src/fallout/ai/highprocess.cpp:746 |
| 0x009031B0 | ProcessActorGroupState | class | src/fallout/ai/highprocess.cpp:1580 |
| 0x008DAF20 | ProcessActorIdle | class | src/fallout/ai/highprocess.cpp:1184 |
| 0x00904DA0 | ProcessCannibal | proven | src/fallout/ai/highprocess.cpp:26095 |
| 0x008E3140 | ProcessEat | proven | src/fallout/ai/highprocess.cpp:71639 |
| 0x008F69E0 | RefreshActorState | class | src/fallout/ai/highprocess.cpp:1925 |
| 0x009014D0 | RefreshTargetState | decomp | src/fallout/ai/highprocess.cpp:1286 |
| 0x008DA8B0 | ResetCurrentPackage | class | src/fallout/ai/highprocess.cpp:1202 |
| 0x008E40A0 | ResetDetectionState | class | src/fallout/ai/highprocess.cpp:1549 |
| 0x008D91A0 | ResetMovementState | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9470 | ResetSearchTimer | proven | src/fallout/ai/highprocess.cpp:14000 |
| 0x00901310 | ResetTargetReferences | class | src/fallout/ai/highprocess.cpp:1423 |
| 0x00901230 | RestorePreviousReference | class | src/fallout/ai/highprocess.cpp:1305 |
| 0x008FE420 | Revert | class | src/fallout/ai/highprocess.cpp:7 |
| 0x008E40D0 | RunDetection | class | src/fallout/ai/highprocess.cpp:2323 |
| 0x008FC4F0 | SaveGameBGS | proven | src/fallout/ai/highprocess.cpp:50168 |
| 0x008F66E0 | SetActorDetectionLevel | class | src/fallout/ai/highprocess.cpp:865 |
| 0x008DA950 | SetActorDetectionState | class | src/fallout/ai/highprocess.cpp:1240 |
| 0x008D9550 | SetActorProcessEnabled | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00900F00 | SetActorProcessState | class | src/fallout/ai/highprocess.cpp:1457 |
| 0x008D8EA0 | SetActorSoundHandle | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D8E40 | SetActorTargetReference | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008DA270 | SetAnimAction | class | src/fallout/ai/highprocess.cpp:1536 |
| 0x00905280 | SetAnimation | class | src/fallout/ai/highprocess.cpp:1478 |
| 0x008D9070 | SetAnimationEnabled | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00901190 | SetCombatActive | class | src/fallout/ai/highprocess.cpp:1335 |
| 0x008D8F30 | SetCombatAlerted | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D8DC0 | SetCombatEnabled | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00900FA0 | SetCombatHeadTrackTarget | proven | src/fallout/ai/highprocess.cpp:6269 |
| 0x008D9690 | SetCurrentDialogueItem | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008EEDF0 | SetCurrentProcessAnimIdleLoaded | proven | src/fallout/ai/highprocess.cpp:71926 |
| 0x008D9760 | SetDetectionLevel | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9490 | SetDetectionTimer | proven | src/fallout/ai/highprocess.cpp:27713 |
| 0x008D8E00 | SetDialogueEmotion | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9220 | SetDialogueState | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00901710 | SetDiveBreathLevel | class | src/fallout/ai/highprocess.cpp:1528 |
| 0x008D8FF0 | SetEssentialFlag | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9510 | SetFloatProperty | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D97F0 | SetForceRotate | proven | src/fallout/ai/highprocess.cpp:14581 |
| 0x00900E80 | SetHasHealingPotions | proven | src/fallout/ai/highprocess.cpp:23498 |
| 0x00900FF0 | SetHeadTrackTarget | proven | src/fallout/ai/highprocess.cpp:6292 |
| 0x008D9410 | SetIdleForm | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D94D0 | SetLightLevel | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D92E0 | SetLipQuequed | proven | src/fallout/ai/highprocess.cpp:13774 |
| 0x008D8F70 | SetLipSyncValue | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9120 | SetPackageEndTimerValue | proven | src/fallout/ai/highprocess.cpp:4814 |
| 0x00900EC0 | SetPreviousReference | class | src/fallout/ai/highprocess.cpp:1495 |
| 0x008D9030 | SetRadiationRate | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00900F50 | SetScriptHeadTrackTarget | proven | src/fallout/ai/highprocess.cpp:6249 |
| 0x008C8FD0 | SetSkippedLastUpdate | proven | src/fallout/ai/aitaskmanager.cpp:47 |
| 0x008D9340 | SetSocialTalkTimer | proven | src/fallout/ai/highprocess.cpp:13787 |
| 0x008D9160 | SetSubtitleActive | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D9280 | SetTalkingState | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008E4E50 | SetupPhantom | proven | src/fallout/ai/highprocess_o2_variant_od_oy_noo2_variant.cpp:819 |
| 0x008F5480 | ShouldProcessActor | decomp | src/fallout/ai/highprocess.cpp:3109 |
| 0x008FF030 | SkipFadeIn | proven | src/fallout/ai/highprocess.cpp:4072 |
| 0x008DAB40 | StartIdleAnimation | class | src/fallout/ai/highprocess.cpp:681 |
| 0x008FF290 | StartTorchSound | proven | src/fallout/ai/highprocess.cpp:10406 |
| 0x008DA9F0 | StopActorMovement | class | src/fallout/ai/highprocess.cpp:1520 |
| 0x008FF1B0 | StopActorSound | class | src/fallout/ai/highprocess.cpp:1065 |
| 0x008D9570 | StopAllActorSounds | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00900420 | TempModActorValueI | proven | src/fallout/ai/highprocess.cpp:10033 |
| 0x008EEEC0 | Update | proven | src/fallout/ai/highprocess.cpp:65847 |
| 0x008F4020 | Update | proven | src/fallout/ai/highprocess.cpp:45744 |
| 0x008D90E0 | UpdateActorLighting | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008D8FB0 | UpdateActorProcess | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x008DAE00 | UpdateActorReferences | class | src/fallout/ai/highprocess.cpp:1014 |
| 0x008EEDC0 | UpdatePlayerAwarenessTimer | class | src/fallout/ai/highprocess.cpp:1543 |
| 0x008D9100 | UpdateProcessTiming | class | src/fallout/ai/highprocess_h_unit.cpp: |
| 0x00903620 | UpdateReferenceTime | class | src/fallout/ai/highprocess.cpp:839 |
| 0x008D98E0 | ~HighProcess | proven | src/fallout/ai/highprocess.cpp:28124 |

### LowProcess (86)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00906FB0 | 'scalar deleting destructor' | proven | src/fallout/ai/lowprocess.cpp:2389 |
| 0x0090A1A0 | CanProcessActor | class | src/fallout/ai/lowprocess.cpp:471 |
| 0x009078D0 | CanRunPackage | decomp | src/fallout/ai/lowprocess.cpp:2083 |
| 0x0090AC40 | CheckIfHasObject | proven | src/fallout/ai/lowprocess.cpp:12113 |
| 0x009070A0 | ClearData | decomp | src/fallout/ai/lowprocess.cpp:1657 |
| 0x0090CC10 | ClearReferenceRecords | class | src/fallout/ai/lowprocess.cpp:1695 |
| 0x00908CD0 | CreateFollowforEscort | proven | src/fallout/ai/lowprocess.cpp:6840 |
| 0x00907460 | DamageModActorValue | proven | src/fallout/ai/lowprocess.cpp:4343 |
| 0x00907840 | EvaluateActorPackage | class | src/fallout/ai/lowprocess.cpp:2110 |
| 0x00908BF0 | FindPackageTarget | class | src/fallout/ai/lowprocess.cpp:2171 |
| 0x009122E0 | FindPatrolTarget | decomp | src/fallout/ai/lowprocess.cpp:2182 |
| 0x0092CAB0 | FUN_0092cab0 | class | src/fallout/ai/middlelowprocess_decl_variant.cpp:17 |
| 0x008041A0 | GetActiveCombatTarget | decomp | src/fallout/ai/lowprocess.cpp:31 |
| 0x00907260 | GetActorTimeDelta | decomp | src/fallout/ai/lowprocess.cpp:2153 |
| 0x009072D0 | GetActorValue | class | src/fallout/ai/lowprocess.cpp:2045 |
| 0x008D7E60 | GetBit | proven | src/fallout/ai/lowprocess.cpp:2456 |
| 0x00907380 | GetCurrentActorValue | class | src/fallout/ai/lowprocess.cpp:2057 |
| 0x0090EC70 | GetCurrentDestinationCoordinate | proven | src/fallout/ai/lowprocess.cpp:13181 |
| 0x0090F670 | GetCurrentDestinationRadius | proven | src/fallout/ai/lowprocess.cpp:12180 |
| 0x0090E970 | GetCurrentDestinationReference | proven | src/fallout/ai/lowprocess.cpp:12748 |
| 0x0090F3F0 | GetCurrentDestinationWorldSpace | proven | src/fallout/ai/lowprocess.cpp:9799 |
| 0x009B88A0 | GetCurrentDetectionAmount | class | src/fallout/ai/lowprocess.cpp:96 |
| 0x008D7EC0 | GetIsAggressor | proven | src/fallout/ai/highprocess.cpp:4416 |
| 0x00908C50 | GetPackageLocationReference | class | src/fallout/ai/lowprocess.cpp:2250 |
| 0x006286D0 | GetPackageObjectType | decomp | src/fallout/ai/lowprocess.cpp:26 |
| 0x009076A0 | GetPackedStateBits0To8 | class | src/fallout/ai/lowprocess.cpp:2230 |
| 0x009076E0 | GetPackedStateBits13To26 | class | src/fallout/ai/lowprocess.cpp:2225 |
| 0x009076C0 | GetPackedStateBits9To12 | class | src/fallout/ai/lowprocess.cpp:2220 |
| 0x0090F8B0 | GetSaveSize | proven | src/fallout/ai/lowprocess.cpp:8108 |
| 0x008D6F30 | GetTarget | decomp | src/fallout/ai/lowprocess.cpp:16 |
| 0x00907510 | HandlePackageChange | decomp | src/fallout/ai/lowprocess.cpp:1880 |
| 0x0090D480 | HandlePackageLocationLoaded | decomp | src/fallout/ai/lowprocess.cpp:1987 |
| 0x0090D570 | HandlePackageTargetLoaded | decomp | src/fallout/ai/lowprocess.cpp:2025 |
| 0x00912960 | HandlePatrolArrival | decomp | src/fallout/ai/lowprocess.cpp:2212 |
| 0x00910820 | InitLoadGame | class | src/fallout/ai/lowprocess.cpp:1484 |
| 0x008D8060 | IsAnimationStateActive | class | src/fallout/ai/lowprocess.cpp:76 |
| 0x008D80A0 | IsCurrentlyAlerted | class | src/fallout/ai/lowprocess.cpp:86 |
| 0x008D7E80 | IsCurrentProcessComplete | class | src/fallout/ai/lowprocess.cpp:46 |
| 0x008D7E40 | IsMovementComplete | class | src/fallout/ai/lowprocess.cpp:41 |
| 0x008D8000 | IsProcessActivityActive | class | src/fallout/ai/lowprocess.cpp:66 |
| 0x008D7F60 | IsProcessConditionMet | class | src/fallout/ai/lowprocess.cpp:56 |
| 0x00910630 | LoadGame | class | src/fallout/ai/lowprocess.cpp:1546 |
| 0x0090FD80 | LoadGameTES | proven | src/fallout/ai/lowprocess.cpp:8382 |
| 0x00906DC0 | LowProcess | proven | src/fallout/ai/lowprocess.cpp:2344 |
| 0x00907620 | ModEssentialDownTimer | proven | src/fallout/ai/lowprocess.cpp:3437 |
| 0x009134C0 | ModTrackedDamage | proven | src/fallout/ai/lowprocess.cpp:3343 |
| 0x00913510 | OnPackageChanged | class | src/fallout/ai/lowprocess.cpp:2123 |
| 0x00913630 | OnPackageEnd | class | src/fallout/ai/lowprocess.cpp:2139 |
| 0x009135A0 | OnPackageStart | class | src/fallout/ai/lowprocess.cpp:2069 |
| 0x00908F70 | ProcessAcquire | class | src/fallout/ai/lowprocess.cpp:1163 |
| 0x0090D620 | ProcessActivate | class | src/fallout/ai/lowprocess.cpp:1040 |
| 0x0090D240 | ProcessAlarm | proven | src/fallout/ai/lowprocess.cpp:4038 |
| 0x009136B0 | ProcessDialogueTopic | class | src/fallout/ai/lowprocess.cpp:1945 |
| 0x00909C90 | ProcessFlee | proven | src/fallout/ai/lowprocess.cpp:7161 |
| 0x00912B00 | ProcessGuard | class | src/fallout/ai/lowprocess.cpp:1320 |
| 0x009121E0 | ProcessPatrol | class | src/fallout/ai/lowprocess.cpp:1905 |
| 0x00912340 | ProcessPatrolPackage | decomp | src/fallout/ai/lowprocess.cpp:1439 |
| 0x00907650 | ResetPackageState | class | src/fallout/ai/lowprocess.cpp:2205 |
| 0x009089C0 | ResolvePackageLocation | class | src/fallout/ai/lowprocess.cpp:1590 |
| 0x009082D0 | ResolvePackageTarget | class | src/fallout/ai/lowprocess.cpp:841 |
| 0x00910A60 | Revert | class | src/fallout/ai/lowprocess.cpp:2008 |
| 0x009125B0 | RunProcessUpdate | decomp | src/fallout/ai/lowprocess.cpp:1239 |
| 0x00910450 | SaveGameBGS | proven | src/fallout/ai/lowprocess.cpp:8549 |
| 0x009130F0 | SavePackageToExtraData | proven | src/fallout/ai/lowprocess.cpp:5554 |
| 0x00907700 | SelectNextPackage | decomp | src/fallout/ai/lowprocess.cpp:1827 |
| 0x008D80C0 | SetAlert | class | src/fallout/ai/lowprocess.cpp:91 |
| 0x008D7DE0 | SetAnimationComplete | class | src/fallout/ai/lowprocess.cpp:36 |
| 0x008D8080 | SetAnimationStateActive | class | src/fallout/ai/lowprocess.cpp:81 |
| 0x008D7F20 | SetCombatDelayTimer | proven | src/fallout/ai/highprocess.cpp:4442 |
| 0x008D7DC0 | SetCurrentBoundObject | class | src/fallout/ai/lowprocess.cpp:6 |
| 0x008D8040 | SetCurrentCombatTarget | class | src/fallout/ai/lowprocess.cpp:11 |
| 0x0090AC20 | SetFlag40 | decomp | src/fallout/ai/lowprocess.cpp:2271 |
| 0x0090C3E0 | SetMobileObjectState | class | src/fallout/ai/lowprocess.cpp:666 |
| 0x005A8060 | SetPackageObjectType | class | src/fallout/ai/lowprocess.cpp:21 |
| 0x008D7FE0 | SetProcessConditionMet | class | src/fallout/ai/lowprocess.cpp:61 |
| 0x008D8020 | SetProcessModeEnabled | class | src/fallout/ai/lowprocess.cpp:71 |
| 0x009119B0 | SetProcessTarget | class | src/fallout/ai/lowprocess.cpp:1859 |
| 0x008D7EE0 | SetProcessTaskComplete | class | src/fallout/ai/lowprocess.cpp:51 |
| 0x00911E80 | SetTarget | class | src/fallout/ai/lowprocess.cpp:2194 |
| 0x0090AD40 | Update | class | src/fallout/ai/lowprocess.cpp:103 |
| 0x0090C360 | Update | proven | src/fallout/ai/lowprocess.cpp:7346 |
| 0x00909DE0 | UpdateActorPackage | class | src/fallout/ai/lowprocess.cpp:1383 |
| 0x00910B30 | UpdateCurrentPackage | class | src/fallout/ai/lowprocess.cpp:1751 |
| 0x00912990 | UpdatePatrolProgress | decomp | src/fallout/ai/lowprocess.cpp:1782 |
| 0x0090A070 | UpdateTargetFromPackage | decomp | src/fallout/ai/lowprocess.cpp:2237 |
| 0x00906FE0 | ~LowProcess | proven | src/fallout/ai/lowprocess.cpp:2428 |

### MiddleHighProcess (151)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009145E0 | 'scalar deleting destructor' | proven | src/fallout/ai/middlehighprocess.cpp:3630 |
| 0x008D8500 | AddDeferredHideLimb | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00915950 | AddQueuedItem | proven | src/fallout/ai/middlehighprocess.cpp:39205 |
| 0x008D8960 | AddRadiationMagicDelta | proven | src/fallout/ai/highprocess.cpp:4628 |
| 0x008D89E0 | AdvanceMovementTimer | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D82F0 | Assign3DObject | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D84A0 | AssignCharacterController | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x007AC9D0 | AssignEffectShader | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8AA0 | AttachFaceGenerationNode | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00649B80 | BeginIdleAnimation | decomp | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x0091C7E0 | CastSpellAtTarget | class | src/fallout/ai/middlehighprocess.cpp:31 |
| 0x0091C7C0 | CastSpellOnCaster | class | src/fallout/ai/middlehighprocess.cpp:24 |
| 0x008D8770 | Clear3DUpdateFlag | proven | src/fallout/ai/highprocess.cpp:4617 |
| 0x008D87A0 | ClearDetectionFlag | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x009287E0 | ClearFurniture | proven | src/fallout/ai/middlehighprocess.cpp:3010 |
| 0x0092C680 | ClearFurnitureMarker | proven | src/fallout/ai/middlehighprocess.cpp:2704 |
| 0x0092C5E0 | ClearLastAttackHitData | proven | src/fallout/ai/middlehighprocess.cpp:3582 |
| 0x0092C4A0 | ClearLastHitData | proven | src/fallout/ai/middlehighprocess.cpp:3539 |
| 0x008D8310 | ClearProcessStateFlags | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00914B40 | ClearReservation | proven | src/fallout/ai/middlehighprocess.cpp:205 |
| 0x0091EE70 | ClearRunOncePackage | proven | src/fallout/ai/middlehighprocess.cpp:1338 |
| 0x00922960 | EvaluateReferenceforSitSleep | proven | src/fallout/ai/middlehighprocess.cpp:4363 |
| 0x00922670 | FindBedChairs | proven | src/fallout/ai/middlehighprocess_rtm_variant.cpp:123 |
| 0x00925700 | FinishInitLoadGame | proven | src/fallout/ai/middlehighprocess.cpp:38239 |
| 0x0091DB40 | FUN_0091db40 | class | src/fallout/ai/middlehighprocess_decl_variant.cpp:15 |
| 0x00929260 | FUN_00929260 | rejected | src/fallout/ai/middlehighprocess.cpp:50 |
| 0x008D8100 | GetActiveEffectList | proven | src/fallout/ai/actor_h_unit.cpp: |
| 0x008D81E0 | GetActiveWeapon | class | src/fallout_shared/pathfinding/navmesh.cpp:158 |
| 0x00922AF0 | GetActorRootNode | class | src/fallout/ai/middlehighprocess.cpp:73 |
| 0x008D8C20 | GetActorSceneObject | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8330 | GetAimLooking | proven | src/fallout/ai/highprocess.cpp:11560 |
| 0x00602150 | GetAnimation | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D89C0 | GetAnimationElapsedTime | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8B00 | GetAnimationObject | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8A00 | GetAnimationRemainingTime | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8800 | GetArrowProjectiles | decomp | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D88C0 | GetBeginIdlesPlayed | proven | src/fallout/ai/highprocess.cpp:27509 |
| 0x005F7590 | GetCurrentAmmo | class | src/fallout_shared/tescreature_h_unit.cpp: |
| 0x008D8BE0 | GetCurrentFurnitureIndex | proven | src/fallout/ai/highprocess.cpp:12559 |
| 0x008D8420 | GetCurrentProcedure | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00929280 | GetFaceAnimationData | proven | src/fallout/ai/middlehighprocess.cpp:2341 |
| 0x008D8AC0 | GetFaceGenHeadNode | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x005224A0 | GetFacialAnimationNode | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00460FF0 | GetFurnitureMarkerData | class | src/fallout/ai/middlehighprocess.cpp:6 |
| 0x00921080 | GetFurnitureMarkerID | proven | src/fallout/ai/middlehighprocess.cpp:2191 |
| 0x008D8A40 | GetLastAttackHitData | proven | src/fallout/ai/highprocess.cpp:4651 |
| 0x008D8C00 | GetLightingShaderProperty | proven | src/fallout/ai/highprocess.cpp:12570 |
| 0x008F7710 | GetLightIntensity | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8920 | GetLipSyncAnimationData | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x009EE020 | GetObjectBounds | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091EEC0 | GetPackageThatIsRunning | proven | src/fallout/ai/middlehighprocess.cpp:1540 |
| 0x008D8480 | GetPhysicsCharacterController | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091EC20 | GetProcedureIndexRunning | proven | src/fallout/ai/middlehighprocess.cpp:1151 |
| 0x008D8270 | GetProcessState | decomp | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00924220 | GetSaveSize | proven | src/fallout/ai/middlehighprocess.cpp:29987 |
| 0x00502430 | GetSceneRoot | decomp | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8120 | GetSelectedMagicItem | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8B20 | GetSitSleepState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091AB30 | GetTargetForPackage | proven | src/fallout/ai/middlehighprocess.cpp:42469 |
| 0x008D83C0 | GetVisibilityAlpha | class | src/fallout/ai/character_h_unit.cpp: |
| 0x0092B9E0 | GetWeaponCondition | proven | src/fallout/ai/middlehighprocess.cpp:29815 |
| 0x00922B20 | GetWeaponNode | proven | src/fallout/ai/middlehighprocess.cpp:3704 |
| 0x00914BE0 | HandleDeletedReference | proven | src/fallout/ai/middlehighprocess.cpp:41348 |
| 0x00922B40 | HasBeenAttacked | proven | src/fallout/ai/middlehighprocess.cpp:9374 |
| 0x008D86C0 | HasCaughtPlayerPickpocketting | proven | src/fallout/ai/highprocess.cpp:12062 |
| 0x0092C340 | HasMovementAnim | proven | src/fallout/ai/middlehighprocess.cpp:13884 |
| 0x008D8680 | InitializeProcessState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00566950 | IsActorInCombat | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00915D40 | IsAdditionalActorFlagSet | class | src/fallout/ai/middlehighprocess.cpp:18 |
| 0x008D8840 | IsAlert | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x005CE8F0 | IsAnimationPlaying | decomp | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00915D00 | IsFirstActorFlagSet | class | src/fallout/ai/middlehighprocess.cpp:12 |
| 0x008D8860 | IsHoldingWeapon | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0092BF80 | IsPackageDone | proven | src/fallout/ai/middlehighprocess.cpp:2653 |
| 0x008D8600 | IsProcessStateInitialized | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8200 | IsUsingOneHandThrown | proven | src/fallout/ai/highprocess.cpp:4491 |
| 0x008D8240 | IsUsingOneHandThrownMineOrGrenade | proven | src/fallout/ai/highprocess.cpp:4502 |
| 0x008D82B0 | IsWearingPowerArmorHelmet | proven | src/fallout/ai/highprocess.cpp:4514 |
| 0x0091FEE0 | KnockExplosion | proven | src/fallout/ai/middlehighprocess.cpp:33610 |
| 0x00921120 | LoadDynamicIdle | proven | src/fallout/ai/middlehighprocess.cpp:4299 |
| 0x00927000 | LoadGameBGS | proven | src/fallout/ai/middlehighprocess.cpp:36338 |
| 0x00928510 | LoadSitSleepIdle | proven | src/fallout/ai/middlehighprocess.cpp:39089 |
| 0x00913FE0 | MiddleHighProcess | proven | src/fallout/ai/middlehighprocess.cpp:7115 |
| 0x009294B0 | MoveAttachedArrowsToParentCell | proven | src/fallout/ai/middlehighprocess.cpp:36488 |
| 0x0091DED0 | ProcessAlarm | proven | src/fallout/ai/middlehighprocess.cpp:20307 |
| 0x0091FD90 | ProcessDialogue | proven | src/fallout/ai/middlehighprocess.cpp:8600 |
| 0x00917A70 | ProcessEat | proven | src/fallout/ai/middlehighprocess.cpp:16376 |
| 0x0091D790 | ProcessEatOneHour | proven | src/fallout/ai/middlehighprocess.cpp:8149 |
| 0x00918860 | ProcessFlee | proven | src/fallout/ai/middlehighprocess_iso_variant.cpp:2899 |
| 0x0091D3C0 | ProcessFollowOneHour | proven | src/fallout/ai/middlehighprocess.cpp:19264 |
| 0x00921E80 | ProcessGetUp | proven | src/fallout/ai/middlehighprocess.cpp:25189 |
| 0x0092ACD0 | ProcessPatrol | proven | src/fallout/ai/middlehighprocess.cpp:35463 |
| 0x0092AE20 | ProcessPatrolStartTravelToNextRef | proven | src/fallout/ai/middlehighprocess.cpp:13195 |
| 0x00919320 | ProcessTravel | proven | src/fallout/ai/middlehighprocess.cpp:40755 |
| 0x00521630 | RefreshActorRuntimeData | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00928D90 | RefreshMagicShaderEffects | proven | src/fallout/ai/middlehighprocess.cpp:37598 |
| 0x008D8BA0 | RemoveFurniture | proven | src/fallout/ai/highprocess.cpp:4693 |
| 0x008D8740 | ResetActorModel | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8220 | ResetAlertState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091EB20 | ResetTarget | proven | src/fallout/ai/middlehighprocess.cpp:906 |
| 0x009280F0 | RevertBGS | proven | src/fallout/ai/middlehighprocess.cpp:11422 |
| 0x00926000 | RevertTES | proven | src/fallout/ai/middlehighprocess.cpp:27316 |
| 0x00926A20 | SaveGameBGS | proven | src/fallout/ai/middlehighprocess.cpp:27614 |
| 0x00924560 | SaveGameTES | proven | src/fallout/ai/middlehighprocess.cpp:26560 |
| 0x008D82D0 | SetActorAlertState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00929570 | SetAimSequence | proven | src/fallout/ai/middlehighprocess.cpp:3734 |
| 0x008D8620 | SetAlphaMult | proven | src/fallout/ai/highprocess.cpp:4570 |
| 0x0091FE80 | SetAnimation | proven | src/fallout/ai/middlehighprocess.cpp:1841 |
| 0x00521710 | SetAnimationNode | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x005C8A30 | SetBoundingBox | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091E9F0 | SetCurrentAmmo | proven | src/fallout/ai/middlehighprocess.cpp:579 |
| 0x00505E50 | SetCurrentIdle | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8440 | SetCurrentProcedure | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091E100 | SetCurrentWeapon | proven | src/fallout/ai/middlehighprocess.cpp:37369 |
| 0x00407800 | SetFaceAnimationData | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8AE0 | SetFaceGenHeadNode | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D86E0 | SetHasCaughtPlayerPickpocketting | proven | src/fallout/ai/highprocess.cpp:12173 |
| 0x008D88A0 | SetIdleAnimationPlayed | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8820 | SetIronSights | proven | src/fallout/ai/highprocess.cpp:12311 |
| 0x008D8720 | SetIsSummonedCreature | proven | src/fallout/ai/highprocess.cpp:4605 |
| 0x008D8A80 | SetKnockdownStage | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D85C0 | SetLastBoundWeapon | proven | src/fallout/ai/highprocess.cpp:11927 |
| 0x0092C400 | SetLastHitData | proven | src/fallout/ai/middlehighprocess.cpp:3498 |
| 0x00924080 | SetLocationForPackage | proven | src/fallout/ai/lowprocess.cpp:5602 |
| 0x008D8180 | SetMagicTarget | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0092BF60 | SetPixelLightingProperty | class | src/fallout/ai/middlehighprocess.cpp:38 |
| 0x008D88E0 | SetPlayedState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8290 | SetProcessStateFlag | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8A20 | SetRadiationDelta | proven | src/fallout/ai/highprocess.cpp:12466 |
| 0x0091EBB0 | SetRunOncePackage | proven | src/fallout/ai/middlehighprocess.cpp:1069 |
| 0x008D8400 | SetRunOncePackageIndex | class | src/fallout/interface/interfacemanager.cpp:10 |
| 0x008D8640 | SetScriptRefractionPower | proven | src/fallout/ai/highprocess.cpp:12049 |
| 0x008D8140 | SetSelectedMagicItem | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D81C0 | SetShouldCheckMagicNode | proven | src/fallout/ai/highprocess.cpp:4481 |
| 0x008D8880 | SetSustainedState | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0091EA40 | SetTarget | proven | src/fallout/ai/middlehighprocess.cpp:41286 |
| 0x0091ACA0 | SetTargetForPackage | proven | src/fallout/ai/middlehighprocess.cpp:8103 |
| 0x00915400 | SetupNewPackage | proven | src/fallout/ai/middlehighprocess.cpp:232 |
| 0x00915D20 | SetWantWeaponDrawn | proven | src/fallout/ai/middlehighprocess.cpp:7816 |
| 0x00915D60 | SetWeaponDrawn | proven | src/fallout/ai/middlehighprocess.cpp:7840 |
| 0x0091E830 | SetWeaponNode | proven | src/fallout/ai/middlehighprocess.cpp:479 |
| 0x00920FD0 | ShouldDisableCharController | proven | src/fallout/ai/middlehighprocess.cpp:1988 |
| 0x009213E0 | SitOrSleep | proven | src/fallout/ai/middlehighprocess.cpp:24168 |
| 0x008D8540 | StopIdleAnimation | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x0092BD00 | TryReserveProjectileClones | proven | src/fallout/ai/middlehighprocess.cpp:37894 |
| 0x00919F60 | Update | proven | src/fallout/ai/middlehighprocess.cpp:36727 |
| 0x00928D20 | UpdateActorAppearance | class | src/fallout/ai/middlehighprocess.cpp:82 |
| 0x0087D7D0 | UpdateEffectShader | decomp | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D81A0 | UpdateIdleAnimation | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x008D8900 | WasIdleAnimationPlayed | class | src/fallout/ai/middlehighprocess_h_unit.cpp: |
| 0x00914610 | ~MiddleHighProcess | proven | src/fallout/ai/middlehighprocess.cpp:14896 |

### MiddleLowProcess (16)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092C9D0 | 'scalar deleting destructor' | proven | src/fallout/ai/middlelowprocess.cpp:440 |
| 0x0092CF30 | DamageModActorValue | proven | src/fallout/ai/middlelowprocess.cpp:618 |
| 0x008D80E0 | GetProcessInteger | decomp | src/fallout/ai/middlelowprocess.cpp:8 |
| 0x0092E420 | GetSaveSize | proven | src/fallout/ai/middlelowprocess.cpp:673 |
| 0x0092CF10 | GetTemporaryModifier | proven | src/fallout/ai/middlelowprocess.cpp:481 |
| 0x0092EAA0 | LoadGameBGS | proven | src/fallout/ai/middlelowprocess.cpp:263 |
| 0x0092E730 | LoadGameTES | proven | src/fallout/ai/middlelowprocess.cpp:1146 |
| 0x0092C950 | MiddleLowProcess | proven | src/fallout/ai/middlelowprocess.cpp:39 |
| 0x0092EB00 | RevertBGS | proven | src/fallout/ai/middlelowprocess.cpp:388 |
| 0x0092E9F0 | RevertTES | proven | src/fallout/ai/middlelowprocess.cpp:514 |
| 0x0092E560 | SaveGameTES | proven | src/fallout/ai/middlelowprocess.cpp:945 |
| 0x00502C90 | SetProcessInteger | class | src/fallout/ai/middlelowprocess.cpp:13 |
| 0x0092CEC0 | TempModActorValueF | proven | src/fallout/ai/middlelowprocess.cpp:1272 |
| 0x0092D050 | Update | proven | src/fallout/ai/middlelowprocess.cpp:2570 |
| 0x0092E400 | Update | proven | src/fallout/ai/middlelowprocess.cpp:496 |
| 0x0092CA00 | ~MiddleLowProcess | proven | src/staging/blk_00920000_od.cpp:233 |

### MobileObjectTaskletData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8370 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:91 |
| 0x008C82E0 | MobileObjectTaskletData | proven | src/fallout/ai/aitaskmanager.cpp:1434 |
| 0x008C8130 | Process | proven | src/fallout/ai/aitaskmanager.cpp:1375 |
| 0x008C8240 | RunToCompletion | proven | src/fallout/ai/aitaskmanager.cpp:1263 |

### ModifierList (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937380 | AddModifier | proven | src/bscore/bssimplelist.cpp:1020 |
| 0x00937400 | DeleteModifier | proven | src/fallout/ai/modifierlist.cpp:489 |
| 0x00937000 | ModifierList | proven | src/staging/blk_00920000_od.cpp:635 |
| 0x00937B50 | SaveGame | proven | src/staging/blk_00920000_od.cpp:344 |
| 0x009375E0 | SetModifier | proven | src/fallout/ai/modifierlist.cpp:171 |

### ProcessLists (60)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096E2B0 | AddActorToAliveList | decomp | src/fallout/ai/processlists.cpp:40 |
| 0x0096E870 | AddMobileObjectToList | decomp | src/fallout/ai/processlists.cpp:110 |
| 0x0096D450 | AddReference | proven | src/fallout/ai/middlelowprocess.cpp:532 |
| 0x00973FD0 | AddTempEffect | proven | src/fallout/ai/processlists.cpp:6662 |
| 0x0096D4B0 | AdvanceProcessLists | decomp | src/fallout/ai/processlists.cpp:328 |
| 0x00973590 | BuildFollowerListRecursive | proven | src/fallout/ai/processlists.cpp:6310 |
| 0x0096E310 | CalculateAliveActorList | decomp | src/fallout/ai/processlists.cpp:56 |
| 0x0096E7D0 | CanAddActorToList | decomp | src/fallout/ai/processlists.cpp:355 |
| 0x00977CB0 | CommentOnPlayerAction | proven | src/fallout/ai/processlists.cpp:2332 |
| 0x0096BC50 | CountHighActors | proven | src/fallout/ai/processlists.cpp:4484 |
| 0x00977130 | DisableExcessDeadActors | proven | src/fallout/ai/processlists.cpp:4352 |
| 0x00970EE0 | DistanceListCompareFn | proven | src/fallout/ai/processlists.cpp:6149 |
| 0x00974CB0 | FindMagicShaderHitEffect | decomp | src/fallout/ai/processlists.cpp:396 |
| 0x00974A50 | FinishMagicShaderHitEffect | proven | src/fallout/ai/processlists.cpp:3743 |
| 0x0096E290 | GetAliveActorList | decomp | src/fallout/ai/processlists.cpp:32 |
| 0x009727C0 | GetCrimeByIndex | proven | src/fallout/ai/processlists.cpp:6251 |
| 0x00972740 | GetCrimeIndex | proven | src/fallout/ai/processlists.cpp:4510 |
| 0x004610F0 | GetProjectilePostProcessList | proven | src/staging/blk_00460000_od.cpp:45 |
| 0x00975AF0 | InitLoadGame | decomp | src/fallout/ai/processlists.cpp:338 |
| 0x00970D50 | InitPackageLocations | proven | src/fallout/ai/processlists.cpp:6107 |
| 0x0096E3C0 | InsertActorCloseToPlayer | proven | src/fallout/ai/processlists.cpp:3624 |
| 0x00973460 | IsActorDetected | proven | src/fallout/ai/processlists.cpp:14868 |
| 0x00973D50 | IsActorTalkingThroughActivator | decomp | src/fallout/ai/processlists.cpp:92 |
| 0x0096BBC0 | IterateMobs | proven | src/fallout/ai/processlists.cpp:450 |
| 0x00975160 | KillAllProjectiles | proven | src/fallout/ai/processlists.cpp:12524 |
| 0x00973EE0 | MoveActorsToReference | proven | src/fallout/ai/processlists.cpp:16314 |
| 0x00973DE0 | MoveFollowersOnToPlayer | proven | src/fallout/ai/processlists.cpp:899 |
| 0x0096F600 | NullOutTargetRef | proven | src/fallout/ai/processlists.cpp:10823 |
| 0x0096C970 | ParallelUpdateAnimationScenegraph | proven | src/fallout/ai/processlists.cpp:2747 |
| 0x00972D30 | PlaceActorsinBedsOrChairs | proven | src/havok/unplaced/loadedareabound.cpp:660 |
| 0x0096D020 | ProcessLists | proven | src/staging/blk_00960000_od.cpp:9556 |
| 0x00977660 | RebuildActorsCloseToPlayer | proven | src/fallout/ai/processlists.cpp:2974 |
| 0x00976680 | ReferDestructorNullOut | proven | src/fallout/ai/processlists.cpp:7579 |
| 0x0096E6F0 | RemoveActorCloseToPlayer | proven | src/fallout/ai/processlists.cpp:647 |
| 0x0096E2F0 | RemoveActorFromAliveList | decomp | src/fallout/ai/processlists.cpp:49 |
| 0x009785D0 | RemoveDetectionEventsOnActors | proven | src/fallout/ai/processlists.cpp:4461 |
| 0x0096F400 | RemoveMobileObjectFromList | decomp | src/fallout/ai/processlists.cpp:293 |
| 0x0096D470 | RemoveReference | proven | src/fallout_shared/pathfinding/pathfind.cpp:5 |
| 0x009740A0 | RemoveTempEffectsForCell | proven | src/fallout/ai/processlists.cpp:12326 |
| 0x00975C50 | Revert | decomp | src/fallout/ai/processlists.cpp:375 |
| 0x009784C0 | RunActorMagicUpdates | proven | src/fallout/ai/processlists.cpp:3009 |
| 0x0096CB50 | RunActorRagdollAnimationUpdates | proven | src/fallout/ai/processlists.cpp:2810 |
| 0x00978550 | RunActorScripts | proven | src/fallout/ai/processlists.cpp:3224 |
| 0x0096C7C0 | RunActorUpdates | decomp | src/fallout/ai/processlists.cpp:75 |
| 0x0096CFA0 | SkipHighListFadeIn | proven | src/fallout/ai/processlists.cpp:567 |
| 0x0096E570 | SortActorsCloseToPlayer | proven | src/fallout/ai/processlists.cpp:603 |
| 0x00974FC0 | StopAllActorsInDialog | proven | src/fallout/ai/processlists.cpp:4975 |
| 0x00972840 | StopCombatandAlarmonActor | proven | src/fallout/ai/processlists.cpp:14718 |
| 0x00977540 | UnloadAllActorPermanentMagic | proven | src/fallout_shared/tesscriptfunctions.cpp:14038 |
| 0x0096DB30 | UpdateActorsMovement | proven | src/fallout/ai/processlists.cpp:10156 |
| 0x0096C860 | UpdateAnimationScenegraph | proven | src/fallout/ai/processlists.cpp:3146 |
| 0x0096E9B0 | UpdateFollowerTempList | decomp | src/fallout/ai/processlists.cpp:163 |
| 0x00972BB0 | UpdateHighProcess | decomp | src/fallout/ai/processlists.cpp:247 |
| 0x00974420 | UpdateInterfaceTempEffects | decomp | src/fallout/ai/processlists.cpp:190 |
| 0x0096B050 | UpdateLowList | proven | src/fallout/ai/processlists.cpp:1519 |
| 0x0096C240 | UpdateMagicTempEffects | decomp | src/fallout/ai/processlists.cpp:139 |
| 0x0096B810 | UpdateMiddleHighList | proven | src/fallout/ai/processlists.cpp:9279 |
| 0x009781D0 | UpdateNonRenderSafeStuff | proven | src/fallout/ai/processlists.cpp:8547 |
| 0x0096D810 | UpdateProcessLists | proven | src/fallout/ai/processlists.cpp:9826 |
| 0x0096D290 | ~ProcessLists | proven | src/staging/blk_00960000_od.cpp:4299 |

### (free functions) (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C4920 | ReplaceProcessWithMiddleHigh | class | src/fallout/ai/mobileobject.cpp:9839 |
| 0x009320E0 | SetProcessLevel | class | src/fallout/ai/mobileobject.cpp:10906 |

## 5 AI packages and daily routines

Packages (sandbox, patrol, guard, escort, eat, sleep...) and the procedures that run them: what makes an NPC look busy.

### ActorPackage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C6970 | InitLoadGame | proven | src/fallout/ai/actorpackage.cpp:673 |

### ActorPackage_008ad970 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AD970 | FUN_008ad970 | class | src/fallout/ai/actor.cpp:74019 |

### ActorPackage_GetTarget_Helper (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092B550 | GetTargetFromOffset | decomp | src/fallout/ai/middlehighprocess.cpp:3751 |

### ActorPackageContext (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C6B20 | ApplyLoadBuffer | decomp | src/fallout/ai/actorpackage.cpp:380 |
| 0x008C5EF0 | Clear | decomp | src/fallout/ai/actorpackage.cpp:277 |
| 0x008C6730 | LoadGame | decomp | src/fallout/ai/actorpackage.cpp:327 |
| 0x008C6080 | SetPackageAndTarget | decomp | src/fallout/ai/actorpackage.cpp:309 |

### ActorPackageData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067D940 | 'scalar deleting destructor' | proven | src/staging/blk_00660000_od.cpp:701 |
| 0x0067D920 | ActorPackageData | proven | src/staging/blk_00660000_od.cpp:205 |
| 0x0067D970 | ActorPackageData | proven | src/staging/blk_00660000_od.cpp:220 |
| 0x008C6CA0 | CreatePackageData | decomp | src/fallout/ai/actorpackagedata.cpp:16 |

### ActorPackageLegacySave (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C6250 | FUN_008c6250 | probable | src/fallout/ai/actorpackage.cpp:1042 |

### ActorPackageLoad (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C6320 | FUN_008c6320 | probable | src/fallout/ai/actorpackage.cpp:1100 |

### ActorPackageSaver (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C65D0 | SavePackage | decomp | src/fallout/ai/actorpackage.cpp:857 |

### AlarmPackage (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EC640 | 'scalar deleting destructor' | proven | src/fallout/ai/alarmpackage.cpp:121 |
| 0x009EC5D0 | AlarmPackage | proven | src/fallout/ai/alarmpackage.cpp:307 |
| 0x009EC670 | AlarmPackage | proven | src/fallout/ai/alarmpackage.cpp:330 |
| 0x009EC780 | CopyFrom | proven | src/fallout/ai/alarmpackage.cpp:404 |
| 0x009ECBE0 | InitLoadGameTES | proven | src/fallout_shared/package.cpp:12826 |
| 0x009EC700 | ~AlarmPackage | proven | src/fallout/ai/alarmpackage.cpp:354 |

### AnimIdle (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00496980 | 'scalar deleting destructor' | proven | src/fallout_shared/animation.cpp:1341 |
| 0x004965D0 | AnimIdle | proven | src/fallout_shared/animation.cpp:9789 |
| 0x00496A50 | FreeAnimIdleData | proven | src/fallout_shared/animation.cpp:8874 |
| 0x004974C0 | GetAnimIdleSaveSize | proven | src/fallout_shared/animation.cpp:4503 |
| 0x00497100 | GetSaveSize | proven | src/fallout_shared/animation.cpp:4096 |
| 0x004977E0 | LoadAnimIdle | proven | src/fallout_shared/animation.cpp:7188 |
| 0x00496CD0 | Loaded | proven | src/fallout_shared/animation.cpp:9013 |
| 0x004972A0 | LoadGame | proven | src/fallout_shared/animation.cpp:4344 |
| 0x004975E0 | SaveAnimIdle | proven | src/fallout_shared/animation.cpp:9963 |
| 0x00497180 | SaveGame | proven | src/fallout_shared/animation.cpp:9645 |
| 0x00497040 | Update | proven | src/fallout_shared/animation.cpp:2866 |
| 0x004969B0 | ~AnimIdle | proven | src/fallout_shared/animation.cpp:2845 |

### AvoidancePackage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F1830 | RemoveInvalidAvoidedReferences | decomp | src/fallout/ai/fleepackage.cpp:1508 |

### BackUpPackage (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009ED0A0 | 'scalar deleting destructor' | proven | src/fallout/ai/backuppackage.cpp:33 |
| 0x009EDB60 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/backuppackage.cpp:57 |
| 0x009ED030 | BackUpPackage | proven | src/fallout/ai/backuppackage.cpp:378 |
| 0x009ED380 | CalculateBackUpPointInterior | proven | src/staging/blk_009e0000_od.cpp:1718 |
| 0x009ED0D0 | InitializeBackUpPackage | proven | src/fallout/ai/playercharacter.cpp:57327 |
| 0x009ED330 | ~BackUpPackage | proven | src/staging/blk_009e0000_od.cpp:427 |

### BGSIdleCollection (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00479790 | BGSIdleCollection | proven | src/fallout_shared/bgsidlecollection.cpp:158 |
| 0x00479810 | ClearDataComponent | proven | src/fallout_shared/bgsidlecollection.cpp:235 |
| 0x00479850 | CopyComponent | proven | src/fallout_shared/bgsidlecollection.cpp:257 |
| 0x0047A030 | GetIdlesForActor | proven | src/fallout_shared/bgsidlecollection.cpp:99 |
| 0x00479E80 | GetPickType | decomp | src/fallout_shared/bgsidlecollection.cpp:147 |
| 0x00479FB0 | HasIdleForActor | proven | src/fallout_shared/tesmodel.cpp:532 |
| 0x004797E0 | InitializeComponent | class | src/fallout_shared/bgsidlecollection.cpp:6 |
| 0x00479B00 | InitItem | proven | src/fallout_shared/bgsidlecollection.cpp:16 |
| 0x00479C40 | Load | proven | src/fallout_shared/bgsidlecollection.cpp:51 |
| 0x00479EA0 | RemoveIdleAtIndex | proven | src/fallout_shared/bgsidlecollection.cpp:336 |
| 0x004799F0 | Save | proven | src/fallout_shared/bgsidlecollection.cpp:293 |
| 0x004797C0 | ~BGSIdleCollection | proven | src/fallout_shared/bgsidlecollection.cpp:192 |

### BGSIdleMarker (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005E7B10 | 'scalar deleting destructor' | proven | src/fallout_shared/bgsidlemarker.cpp:66 |
| 0x005E7A90 | BGSIdleMarker | proven | src/fallout_shared/bgsidlemarker.cpp:54 |
| 0x005E7F40 | Compare | proven | src/fallout_shared/bgsidlemarker.cpp:265 |
| 0x005E7BB0 | InitItem | class | src/fallout_shared/bgsidlemarker.cpp:17 |
| 0x005E7BF0 | Load | proven | src/fallout_shared/bgsidlemarker.cpp:159 |
| 0x005E7ED0 | SaveForm | proven | src/fallout_shared/bgsidlemarker.cpp:91 |
| 0x005E7B40 | ~BGSIdleMarker | proven | src/fallout_shared/bgsidlemarker.cpp:123 |

### BSFurnitureMarker (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C547E0 | 'scalar deleting destructor' | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:188 |
| 0x00C53F10 | BSFurnitureMarker | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata_ob1_variant.cpp:525 |
| 0x00C54030 | CreateClone | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:119 |
| 0x00C54210 | CreateObject | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:253 |
| 0x00C54400 | Find | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata_ob1_variant.cpp:288 |
| 0x00C54D60 | GetRTTI | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:108 |
| 0x00C542A0 | GetViewerStrings | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:502 |
| 0x00C541E0 | IsEqual | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:145 |
| 0x00C54130 | LinkObject | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:296 |
| 0x00C54150 | RegisterStreamables | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:133 |
| 0x00C54170 | SaveBinary | proven | src/gamebryo2.2/corelibs/nimain/niintegersextradata.cpp:229 |
| 0x00C53FA0 | ~BSFurnitureMarker | proven | src/staging/blk_00c40000_od.cpp:6463 |

### C67ACD0Package (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067ACD0 | GetTypeName | class | src/fallout_shared/tesform.cpp:3216 |

### CaravanAIPackage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0073B730 | Print_WhatIsHeThinking | proven | src/fallout/interface/menus/caravanmenu.cpp:506 |

### CombatReaction::Procedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CD5E0 | EvaluateReaction | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:3183 |

### DialoguePackage (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EDD50 | 'scalar deleting destructor' | proven | src/fallout/ai/dialoguepackage.cpp:29 |
| 0x009EE060 | CopyFrom | proven | src/fallout/ai/dialoguepackage.cpp:139 |
| 0x009EDBC0 | DialoguePackage | proven | src/staging/blk_009e0000_od.cpp:810 |
| 0x009EDD80 | DialoguePackage | proven | src/fallout/ai/mobileobject.cpp:1305 |
| 0x009EF560 | FUN_009ef560 | class | src/fallout/ai/dialoguepackage.cpp:297 |
| 0x009EF6E0 | FUN_009ef6e0 | class | src/fallout/ai/dialoguepackage.cpp:1875 |
| 0x009F0740 | InitLoadGame | proven | src/fallout/ai/dialoguepackage.cpp:391 |
| 0x009F0460 | LoadGame | proven | src/fallout/ai/dialoguepackage.cpp:2038 |
| 0x009F01D0 | SaveGame | class | src/fallout/ai/dialoguepackage.cpp:202 |
| 0x009EDF40 | ~DialoguePackage | proven | src/fallout/ai/dialoguepackage.cpp:69 |

### Engage::Procedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D5000 | CheckAndApply | decomp | src/fallout/ai/combat/combatprocedureengagetarget.cpp:490 |

### EscortActorPackageData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F0980 | 'scalar deleting destructor' | proven | src/fallout/ai/escortpackage.cpp:43 |
| 0x009F0900 | EscortActorPackageData | proven | src/staging/blk_009e0000_od.cpp:863 |
| 0x009F0B70 | HandleDeletedReference | proven | src/fallout/ai/escortpackage.cpp:126 |
| 0x009F09B0 | ~EscortActorPackageData | proven | src/fallout/ai/escortpackage.cpp:333 |

### ExtraAction (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004317C0 | Differs | proven | src/fallout_shared/extradataobjects.cpp:7995 |
| 0x00431780 | ExtraAction | proven | src/fallout_shared/extradataobjects.cpp:43 |
| 0x0041B680 | FUN_0041b680 | unnamed | src/fallout_shared/extradatalist.cpp:7912 |

### ExtraDataListRemoveTrespassPackage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004194B0 | FUN_004194b0 | probable | src/fallout_shared/extradatalist.cpp:12755 |

### ExtraFollower (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00430E70 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:2297 |
| 0x00430DD0 | ExtraFollower | proven | src/fallout_shared/extradataobjects.cpp:1903 |
| 0x00430EA0 | ~ExtraFollower | proven | src/fallout_shared/extradataobjects.cpp:7894 |

### ExtraGuardedRefData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00430FA0 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:7959 |
| 0x004310D0 | AddGuardingActor | decomp | src/fallout_shared/extradataobjects.cpp:147 |
| 0x00431030 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3656 |
| 0x00430F30 | ExtraGuardedRefData | proven | src/fallout_shared/extradataobjects.cpp:686 |
| 0x00430FD0 | ~ExtraGuardedRefData | proven | src/fallout_shared/extradataobjects.cpp:3634 |

### ExtraPackage (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432810 | ExtraPackage | proven | src/fallout_shared/extradataobjects.cpp:4431 |
| 0x00432870 | ExtraPackage | proven | src/fallout_shared/extradataobjects.cpp:3828 |

### ExtraPackageData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00421280 | ExtraPackageData | proven | src/fallout_shared/extradatalist.cpp:8956 |
| 0x0042CBE0 | ExtraPackageData | proven | src/staging/blk_00420000_od.cpp:887 |

### ExtraPatrolRefInUseData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00437A60 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:1699 |
| 0x00437A30 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3357 |
| 0x004379A0 | ExtraPatrolRefInUseData | proven | src/fallout_shared/extradataobjects.cpp:1551 |
| 0x00437AB0 | GetCanBeUsedBy | proven | src/fallout_shared/extradataobjects.cpp:2103 |
| 0x00437A90 | ~ExtraPatrolRefInUseData | proven | src/fallout_shared/extradataobjects.cpp:375 |

### ExtraTresPassPackage (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0042C890 | 'scalar deleting destructor' | proven | src/fallout_shared/extradatalist.cpp:13848 |
| 0x0042C860 | ExtraTresPassPackage | proven | src/fallout_shared/extradatalist.cpp:9015 |
| 0x004328D0 | ExtraTresPassPackage | proven | src/fallout_shared/extradataobjects.cpp:6173 |
| 0x00432900 | ~ExtraTresPassPackage | proven | src/fallout_shared/extradataobjects.cpp:5033 |

### FleePackage (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F1090 | 'scalar deleting destructor' | proven | src/fallout/ai/fleepackage.cpp:13 |
| 0x009F1310 | AddAvoidedRef | proven | src/fallout/ai/fleepackage.cpp:72 |
| 0x009F0E00 | FleePackage | proven | src/fallout/ai/actor.cpp:96206 |
| 0x009F1210 | GetClosestAvoidedRef | proven | src/fallout/ai/fleepackage.cpp:1264 |
| 0x009F25F0 | InitLoadGame | proven | src/fallout/ai/fleepackage.cpp:2260 |
| 0x009F1E80 | InitLoadGameTES | proven | src/fallout/ai/fleepackage.cpp:2090 |
| 0x009F24D0 | LoadGame | proven | src/fallout/ai/fleepackage.cpp:1072 |
| 0x009F1350 | RemoveAvoidedRef | proven | src/fallout/ai/fleepackage.cpp:189 |
| 0x009F10C0 | ~FleePackage | proven | src/fallout/ai/fleepackage.cpp:1597 |

### FleeSavePackage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F1B70 | SaveFleePackage | class | src/fallout/ai/fleepackage.cpp:1932 |

### GuardActorPackageData (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F2800 | 'scalar deleting destructor' | proven | src/fallout/ai/guardpackage.cpp:36 |
| 0x009F27F0 | GetPackageType | class | src/fallout/ai/guardpackage_h_unit.cpp:14 |
| 0x009F27A0 | GuardActorPackageData | proven | src/fallout/ai/patrolpackage.cpp:104 |
| 0x009F2900 | InitLoadGame | class | src/fallout/ai/guardpackage.cpp:20 |
| 0x009F28B0 | LoadGame | class | src/fallout/ai/guardpackage.cpp:11 |
| 0x008C5EC0 | SetReferenceTarget | class | src/fallout/ai/actorpackage.cpp:270 |
| 0x009F2830 | ~GuardActorPackageData | proven | src/fallout/ai/guardpackage.cpp:75 |

### IdleAnimationManager (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00600170 | ClearIdleData | probable | src/fallout_shared/tesidlemanager.cpp:178 |
| 0x00600700 | FindIdleArrayEntry | probable | src/fallout_shared/tesidlemanager.cpp:64 |
| 0x00600690 | GetIdleArray | probable | src/fallout_shared/tesidlemanager.cpp:18 |
| 0x00600930 | GetUsedItemActivate | decomp | src/fallout_shared/tesidlemanager.cpp:12 |
| 0x005FFC20 | InitializeIdleAnimations | decomp | src/fallout_shared/tesidlemanager.cpp:87 |

### IdleSystem (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00AF22D0 | GetRandomGenerator | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:15 |
| 0x00AF2480 | Idle | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:29 |
| 0x00AF23D0 | IdleSystem | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:87 |
| 0x00AF2D20 | Initialize | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:23 |
| 0x00AF2370 | Shutdown | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:76 |
| 0x00AF2360 | Startup | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:95 |
| 0x00AF2400 | ~IdleSystem | decomp | src/bssystemutilities/console/bsawardssystemutility_console.cpp:91 |

### P070Package (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00676390 | IsWithinPackageLocation | class | src/fallout_shared/package.cpp:10467 |

### Package (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006787E0 | GetPackageResult | probable | src/fallout_shared/package.cpp:11648 |
| 0x006773A0 | IsTargetWithinRadius | class | src/fallout_shared/package.cpp:7132 |
| 0x009CAFE0 | UpdateWeaponFire | class | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:1236 |

### PackageEventActionData (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067E190 | InitItem | decomp | src/fallout_shared/packageeventaction.cpp:12 |
| 0x0067DD20 | Load | decomp | src/fallout_shared/packageeventaction.cpp:60 |
| 0x00680890 | PackageEventActionData | decomp | src/fallout_shared/packageeventaction.cpp:8 |

### PackageList (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067E420 | AddPackage | decomp | src/fallout_shared/packagelist.cpp:366 |
| 0x0067E400 | ClearPackageList | decomp | src/fallout_shared/packagelist.cpp:42 |
| 0x0067EC40 | CollectEligiblePackages | decomp | src/fallout_shared/packagelist.cpp:163 |
| 0x0067E440 | Copy | decomp | src/fallout_shared/packagelist.cpp:344 |
| 0x0067E780 | GetPackageForActor | decomp | src/fallout_shared/packagelist.cpp:56 |
| 0x0067E560 | InitItem | decomp | src/fallout_shared/packagelist.cpp:269 |

### PackageLocation (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067F430 | GetLocObject | proven | src/fallout_shared/packagelocation.cpp:1237 |
| 0x0067F480 | GetLocObjectType | proven | src/fallout_shared/packagelocation.cpp:1307 |
| 0x0067F1C0 | GetRadius | proven | src/fallout_shared/packagelocation.cpp:217 |
| 0x0067FC50 | InitLoadGame | proven | src/fallout_shared/packagelocation.cpp:1690 |
| 0x0067FBE0 | LoadGame | proven | src/fallout_shared/packagelocation.cpp:1590 |
| 0x0067F6C0 | Save | proven | src/fallout_shared/packagelocation.cpp:1347 |
| 0x0067FB60 | SaveGame | proven | src/fallout_shared/packagelocation.cpp:1554 |
| 0x0067F410 | SetLocCell | proven | src/fallout_shared/packagelocation.cpp:255 |
| 0x0067F3C0 | SetLocReference | proven | src/fallout_shared/packagelocation.cpp:25 |
| 0x0067F140 | SetLocType | proven | src/fallout_shared/packagelocation.cpp:188 |
| 0x0067F1F0 | SetRadius | proven | src/fallout_shared/packagelocation.cpp:236 |

### PackageTarget (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00680220 | Compare | proven | src/fallout_shared/packagetarget.cpp:241 |
| 0x006801A0 | Copy | proven | src/fallout/ai/middlehighprocess.cpp:141 |
| 0x00680830 | InitLoadGame | proven | src/fallout_shared/packagetarget.cpp:414 |
| 0x0067FF70 | PackageTarget | proven | src/fallout_shared/packagetarget.cpp:165 |
| 0x006802F0 | Save | proven | src/fallout_shared/packagetarget.cpp:281 |
| 0x00680140 | SetTargObject | proven | src/fallout_shared/packagetarget.cpp:218 |

### PackageTargetRecord (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00680170 | FUN_00680170 | unnamed | src/staging/blk_00680000_od.cpp:46 |
| 0x00680020 | GetReferenceTarget | decomp | src/fallout_shared/packagetarget.cpp:38 |
| 0x00680050 | GetTargetForm | decomp | src/fallout_shared/packagetarget.cpp:56 |
| 0x00519B00 | GetTargetKind | probable | src/fallout_shared/packagetarget.cpp:10 |
| 0x00680080 | GetTargetObjectType | decomp | src/fallout_shared/packagetarget.cpp:65 |
| 0x006803B0 | InitItem | decomp | src/fallout_shared/packagetarget.cpp:120 |
| 0x006800B0 | SetTargetKind | decomp | src/fallout_shared/packagetarget.cpp:16 |
| 0x00680110 | SetTargetObjectReference | decomp | src/fallout_shared/packagetarget.cpp:48 |

### PatrolActorPackageData (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F2A40 | 'scalar deleting destructor' | proven | src/fallout/ai/patrolpackage.cpp:476 |
| 0x009F2B30 | ClearReservedPatrolRef | proven | src/fallout_shared/extradatalist.cpp:5934 |
| 0x009F3390 | GetCurrentReference | proven | src/fallout/ai/patrolpackage.cpp:451 |
| 0x009F2D40 | GetInitialReferenceForSetup | proven | src/fallout/ai/patrolpackage.cpp:237 |
| 0x009F2A30 | GetPackageType | proven | src/fallout/ai/patrolpackage.cpp:121 |
| 0x009F2BA0 | Init | proven | src/fallout/ai/patrolpackage.cpp:210 |
| 0x009F3610 | InitLoadGame | proven | src/fallout/ai/patrolpackage_rtti_variant.cpp:321 |
| 0x004F1540 | IsPatrolling | decomp | src/fallout/ai/patrolpackage.cpp:89 |
| 0x009F34E0 | LoadGame | proven | src/fallout/ai/patrolpackage_rtti_variant.cpp:118 |
| 0x009F29A0 | PatrolActorPackageData | proven | src/staging/blk_009e0000_od.cpp:190 |
| 0x009F33D0 | SaveGame | proven | src/fallout/ai/patrolpackage.cpp:546 |
| 0x009F2A70 | ~PatrolActorPackageData | proven | src/fallout/ai/patrolpackage.cpp:514 |

### ProcedureValue (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D82E0 | UpdateOutput | decomp | src/fallout/ai/combat/combatproceduremove.cpp:629 |

### SandBoxActorPackageData (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F3A40 | 'scalar deleting destructor' | proven | src/fallout/ai/sandboxpackage.cpp:932 |
| 0x009F3A30 | GetPackageType | decomp | src/fallout_shared/tempeffects/bstempeffect.cpp:6 |
| 0x009F43C0 | HasProcessTarget | decomp | src/fallout/ai/sandboxpackage.cpp:111 |
| 0x009F5EA0 | InitLoadGame | class | src/fallout/ai/sandboxpackage.cpp:220 |
| 0x009F3D50 | IsActivityTime | decomp | src/fallout/ai/sandboxpackage.cpp:29 |
| 0x009F4300 | IsActorWithinLocationRadius | decomp | src/fallout/ai/sandboxpackage.cpp:310 |
| 0x009F3C10 | IsLocationCheckDue | decomp | src/fallout/ai/sandboxpackage.cpp:8 |
| 0x009F56B0 | IsObjectWithinLocationRadius | decomp | src/fallout/ai/sandboxpackage.cpp:351 |
| 0x009F5CA0 | LoadGame | class | src/fallout/ai/sandboxpackage.cpp:181 |
| 0x009F3900 | SandBoxActorPackageData | proven | src/staging/blk_009e0000_od.cpp:2382 |
| 0x009F40C0 | SetReferenceTarget | class | src/fallout/ai/sandboxpackage.cpp:63 |
| 0x009F3A70 | ~SandBoxActorPackageData | proven | src/fallout/ai/sandboxpackage.cpp:2499 |

### SbActorPackageData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F54D0 | ScanSandboxTargets | decomp | src/fallout/ai/sandboxpackage.cpp:2115 |

### SearchPackage (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F6680 | 'scalar deleting destructor' | proven | src/fallout/ai/searchpackage.cpp:14 |
| 0x009F66B0 | SearchPackage | proven | src/fallout/ai/searchpackage.cpp:157 |
| 0x009F67B0 | ~SearchPackage | proven | src/fallout/ai/searchpackage.cpp:198 |

### SpectatorPackage (13)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F73E0 | 'scalar deleting destructor' | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:106 |
| 0x009F8330 | AddThreatFromActorToCombatTarget | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:1537 |
| 0x009F87D0 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:530 |
| 0x009F76E0 | ComputeCenterPoint | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:1886 |
| 0x009F7500 | CopyFrom | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:1782 |
| 0x009F9D10 | FUN_009f9d10 | unnamed | src/staging/blk_009e0000_o2.cpp:44 |
| 0x009F8770 | InitLoadGameTES | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:160 |
| 0x009F9C80 | IsComplete | decomp | src/fallout/ai/spectatorpackage.cpp:5 |
| 0x009F8900 | LoadGame | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:646 |
| 0x009F7D70 | MakeCombatComment | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:2860 |
| 0x009F72F0 | SpectatorPackage | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:1096 |
| 0x009F8020 | Update | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:3293 |
| 0x009F7410 | ~SpectatorPackage | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:1236 |

### TESAmbushPackageData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067AD90 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedataambush.cpp:13 |
| 0x0067AF50 | Compare | proven | src/fallout_shared/packagedataambush.cpp:140 |
| 0x0067ACF0 | TESAmbushPackageData | proven | src/fallout_shared/package.cpp:4325 |
| 0x0067ADC0 | ~TESAmbushPackageData | proven | src/fallout_shared/packagedataambush.cpp:62 |

### TESDialoguePackageData (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067B1E0 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatadialogue.cpp:28 |
| 0x0067B470 | Compare | proven | src/fallout_shared/packagedatadialogue_rtti2_variant.cpp:198 |
| 0x0067B310 | CopyFrom | proven | src/fallout_shared/packagedatadialogue_rtti_variant_decl_variant.cpp:161 |
| 0x0067B590 | InitItem | class | src/fallout_shared/packagedatadialogue.cpp:6 |
| 0x0067B7D0 | LoadGame | proven | src/fallout_shared/packagedatadialogue.cpp:295 |
| 0x0067B170 | TESDialoguePackageData | proven | src/fallout_shared/package.cpp:7611 |
| 0x0067B210 | TESDialoguePackageData | proven | src/fallout_shared/packagedatadialogue.cpp:233 |
| 0x0067B280 | ~TESDialoguePackageData | proven | src/fallout_shared/packagedatadialogue.cpp:57 |

### TESEatPackageData (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067B980 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedataeat.cpp:57 |
| 0x0067BB40 | Compare | proven | src/fallout_shared/packagedataeat.cpp:142 |
| 0x0067BA40 | CopyFrom | proven | src/fallout_shared/packagedataeat_rtti_variant.cpp:101 |
| 0x0067BFA0 | FUN_0067bfa0 | probable | src/fallout_shared/packagedataeat.cpp:42 |
| 0x0067BBB0 | Save | proven | src/fallout_shared/packagedataeat.cpp:19 |
| 0x0067B950 | TESEatPackageData | proven | src/fallout_shared/package.cpp:4345 |
| 0x0067B9B0 | ~TESEatPackageData | proven | src/fallout_shared/packagedataeat.cpp:110 |

### TESEscortPackageData (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067BC30 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedataescort.cpp:13 |
| 0x0067BE40 | Compare | proven | src/fallout_shared/packagedataescort_rtti2_variant.cpp:85 |
| 0x0067BF40 | FUN_0067bf40 | unnamed | src/fallout_shared/packagedataescort.cpp:106 |
| 0x0067BEC0 | Save | proven | src/fallout_shared/packagedataescort.cpp:75 |
| 0x0067BBF0 | TESEscortPackageData | proven | src/fallout_shared/package.cpp:4360 |
| 0x0067BC60 | TESEscortPackageData | proven | src/fallout_shared/packagedataescort.cpp:42 |
| 0x0067BCA0 | ~TESEscortPackageData | proven | src/fallout_shared/packagedataescort.cpp:132 |

### TESFollowPackageData (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067C010 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatafollow.cpp:21 |
| 0x0067C220 | Compare | proven | src/fallout_shared/packagedatafollow.cpp:123 |
| 0x0067C110 | CopyFrom | proven | src/fallout_shared/packagedatafollow.cpp:169 |
| 0x0067BFD0 | TESFollowPackageData | proven | src/fallout_shared/package.cpp:4377 |
| 0x0067C040 | TESFollowPackageData | proven | src/fallout_shared/packagedatafollow.cpp:40 |
| 0x0067C080 | ~TESFollowPackageData | proven | src/fallout_shared/packagedatafollow.cpp:98 |

### TESIdleForm (22)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005FE130 | 'scalar deleting destructor' | proven | src/fallout_shared/tesidleform.cpp:432 |
| 0x005FE770 | AssignParentPath | decomp | src/fallout_shared/tesidleform_h_unit.cpp: |
| 0x005FF430 | CheckConditions | proven | src/fallout_shared/tesidleform.cpp:36 |
| 0x005FF280 | CheckIdleFile | proven | src/fallout_shared/tesidleform.cpp:26 |
| 0x005FE400 | ClearData | class | src/fallout_shared/tesidleform.cpp:56 |
| 0x005FF610 | DetachFromParent | proven | src/fallout_shared/tesidleform.cpp:804 |
| 0x005FEFA0 | FixNextIdles | proven | src/fallout_shared/tesidleform.cpp:113 |
| 0x005FF4D0 | GetChildByIndex | proven | src/fallout_shared/tesidleform.cpp:464 |
| 0x005FF4A0 | GetChildCount | proven | src/fallout_shared/tesidleform.cpp:386 |
| 0x005FE0F0 | GetEditorID | proven | src/fallout_shared/bgsdehydration.cpp:679 |
| 0x005FF160 | GetIdleAnimGroupSection | proven | src/fallout_shared/tesidleform.cpp:401 |
| 0x005FF2E0 | GetIdleToPlay | proven | src/fallout_shared/tesidleform.cpp:66 |
| 0x005FF520 | GetIndexForChild | proven | src/fallout_shared/tesfaction.cpp:419 |
| 0x005FF770 | GetLoops | proven | src/fallout_shared/tesidleform.cpp:486 |
| 0x005FEDB0 | InitParents | proven | src/fallout_shared/tesidleform.cpp:171 |
| 0x005FE810 | Load | class | src/fallout_shared/tesidleform.cpp:235 |
| 0x005FF5D0 | RemoveChild | proven | src/staging/blk_005e0000_od.cpp:1606 |
| 0x005FF560 | RemoveChildAtIndex | proven | src/gamebryo2.2/corelibs/nimain/nitlargearray_h_unit.cpp:33 |
| 0x005FE3B0 | ResetFormData | class | src/fallout_shared/tesidleform.cpp:14 |
| 0x005FEA50 | SaveForm | proven | src/fallout_shared/tesidleform.cpp:620 |
| 0x005FE040 | TESIdleForm | proven | src/staging/blk_005e0000_od.cpp:3512 |
| 0x005FE180 | ~TESIdleForm | proven | src/fallout_shared/tesidleform.cpp:922 |

### TESPackage (85)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00670880 | 'scalar deleting destructor' | proven | src/fallout_shared/package.cpp:4114 |
| 0x006797C0 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/package.cpp:10969 |
| 0x006777B0 | CalculateProcedureType | proven | src/fallout_shared/package.cpp:2426 |
| 0x00673420 | Compare | proven | src/fallout_shared/package.cpp:13936 |
| 0x00678A80 | ComparePackageSchedule | proven | src/staging/blk_00660000_od.cpp:1632 |
| 0x0067A1B0 | CopyAllFlags | proven | src/fallout_shared/package.cpp:5954 |
| 0x00670B90 | CreatePackage | proven | src/fallout_shared/package.cpp:6825 |
| 0x00679E00 | FormMatchesPackageObjectType | proven | src/fallout_shared/package.cpp:11117 |
| 0x00670ED0 | FUN_00670ed0 | unnamed | src/fallout_shared/package.cpp:166 |
| 0x00670F40 | FUN_00670f40 | unnamed | src/fallout_shared/package.cpp:190 |
| 0x00670F60 | FUN_00670f60 | unnamed | src/fallout_shared/package.cpp:214 |
| 0x00672AA0 | FUN_00672aa0 | probable | src/fallout_shared/tesobjectrefr.cpp:10321 |
| 0x00673890 | FUN_00673890 | unnamed | src/fallout_shared/package.cpp:156 |
| 0x00674D20 | FUN_00674d20 | unnamed | src/fallout_shared/package.cpp:161 |
| 0x0067A480 | GetAlwaysRun | proven | src/fallout_shared/package.cpp:1383 |
| 0x0067A700 | GetContinueDuringCombat | proven | src/fallout_shared/package.cpp:1416 |
| 0x0067A3F0 | GetDefensive | proven | src/fallout_shared/package.cpp:1361 |
| 0x00672760 | GetDialogueTopic | proven | src/fallout/ai/mobileobject.cpp:1431 |
| 0x0067A460 | GetDrawWeaponFlag | proven | src/fallout_shared/package.cpp:1372 |
| 0x006784C0 | GetEscortFollowDistance | proven | src/fallout_shared/package.cpp:4222 |
| 0x0067AC50 | GetFOEnableAvoidRadiationBehavior | proven | src/fallout_shared/package.cpp:1522 |
| 0x00675950 | GetFollowPackageData | proven | src/fallout_shared/package.cpp:4192 |
| 0x00441B00 | GetForceUnequipWeapon | proven | src/fallout_shared/modelloader.cpp:303 |
| 0x00672930 | GetInitialTargetCount | proven | src/fallout_shared/package.cpp:287 |
| 0x00674D40 | GetIsCreated | proven | src/fallout_shared/package.cpp:226 |
| 0x00675C20 | GetLocationCell | proven | src/fallout_shared/package.cpp:13438 |
| 0x00675DE0 | GetLocationCoord | proven | src/fallout_shared/package.cpp:12202 |
| 0x00676280 | GetLocationRadius | proven | src/fallout/ai/highprocess.cpp:982 |
| 0x00676140 | GetLocationReference | proven | src/fallout_shared/package.cpp:5677 |
| 0x00675A50 | GetLocationWorld | proven | src/fallout_shared/package.cpp:5231 |
| 0x00903CF0 | GetNextScript | decomp | src/fallout_shared/extradatalist.cpp:51 |
| 0x00679BA0 | GetObjectTypeFromForm | proven | src/fallout_shared/package.cpp:1240 |
| 0x00670F90 | GetOncePerDay | proven | src/fallout_shared/package.cpp:10 |
| 0x006E25D0 | GetPackageDefaultFloat | decomp | src/fallout_shared/package.cpp:5 |
| 0x00678670 | GetPackageRadiusActorToLocation | proven | src/fallout_shared/package.cpp:892 |
| 0x00672F20 | GetPackageSearchLocation | proven | src/fallout_shared/package.cpp:11342 |
| 0x006728A0 | GetPackageSearchRadius | probable | src/fallout_shared/package.cpp:138 |
| 0x00672DD0 | GetPackageSecondLocation | proven | src/fallout_shared/package.cpp:318 |
| 0x0041CA90 | GetPackType | proven | src/fallout_shared/extradataobjects.cpp:2131 |
| 0x00675920 | GetPatrolPackageData | proven | src/fallout_shared/package.cpp:47 |
| 0x00407840 | GetRefCount | decomp | src/bsshader/speedtreeshaderproperty_h_unit.cpp: |
| 0x006759E0 | GetResolvedTargetReference | probable | src/fallout_shared/package.cpp:92 |
| 0x006757E0 | GetSearchLocationCell | proven | src/fallout_shared/package.cpp:6881 |
| 0x00675830 | GetSearchLocationCoord | proven | src/fallout_shared/package.cpp:6902 |
| 0x006758A0 | GetSearchLocationRadius | proven | src/fallout_shared/package.cpp:4179 |
| 0x006751A0 | GetSecondLocationCell | proven | src/fallout_shared/tesobjectrefr.cpp:21284 |
| 0x00675360 | GetSecondLocationCoord | proven | src/fallout_shared/package.cpp:9488 |
| 0x00675670 | GetSecondLocationRadius | proven | src/fallout_shared/package.cpp:4152 |
| 0x006756A0 | GetSecondLocationReference | proven | src/fallout_shared/package.cpp:9895 |
| 0x00674FD0 | GetSecondLocationWorld | proven | src/fallout_shared/package.cpp:8905 |
| 0x006758F0 | GetUseWeaponPackageData | proven | src/fallout_shared/package.cpp:3808 |
| 0x00674930 | InitItem | proven | src/fallout_shared/package_ctx_variant.cpp:177 |
| 0x00679340 | InitLoadGameTES | proven | src/fallout_shared/package.cpp:13636 |
| 0x00676E40 | IsActorAtRefTarget | proven | src/fallout_shared/package.cpp:3362 |
| 0x00674E40 | IsFlag10000Set | decomp | src/fallout_shared/package.cpp:34 |
| 0x00670EF0 | IsFlag10Set | decomp | src/fallout_shared/package.cpp:178 |
| 0x00670F10 | IsFlag80Set | decomp | src/fallout_shared/package.cpp:202 |
| 0x00678610 | IsInterruptPackage | proven | src/fallout_shared/package.cpp:64 |
| 0x00678D40 | IsitDayofTheWeek | proven | src/fallout_shared/package.cpp:1028 |
| 0x006737A0 | IsReadyToRun | proven | src/fallout_shared/package.cpp:406 |
| 0x00678EC0 | IsTargetAnActor | proven | src/fallout_shared/package.cpp:1181 |
| 0x006709D0 | ResetFormData | class | src/fallout_shared/package.cpp:122 |
| 0x00679B10 | Revert | proven | src/fallout_shared/package.cpp:6535 |
| 0x006738B0 | Save | proven | src/fallout_shared/package.cpp:6263 |
| 0x0067A720 | SetContinueDuringCombat | proven | src/fallout_shared/package.cpp:1427 |
| 0x006729D0 | SetDialogueTopic | proven | src/fallout/ai/actor.cpp:41569 |
| 0x00671A20 | SetDrawWeaponFlag | proven | src/fallout_shared/package.cpp:244 |
| 0x0067A640 | SetForceUnequipWeapon | proven | src/fallout_shared/package.cpp:3910 |
| 0x00674D70 | SetIsCreated | proven | src/fallout_shared/package.cpp:441 |
| 0x00826B90 | SetMustComplete | decomp | src/fallout_shared/packagelocation.cpp:142 |
| 0x00826B40 | SetMustReachLocation | decomp | src/fallout_shared/packagelocation.cpp:136 |
| 0x00674E70 | SetNeverRun | proven | src/fallout_shared/package.cpp:13777 |
| 0x00673200 | SetPackageConditions | proven | src/fallout_shared/package.cpp:6113 |
| 0x00672B70 | SetPackageFlag | decomp | src/staging/blk_00660000_od.cpp:774 |
| 0x006730A0 | SetPackageIdles | proven | src/fallout_shared/package.cpp:6064 |
| 0x00671D30 | SetPackageLocation | proven | src/fallout_shared/package.cpp:4065 |
| 0x00673180 | SetPackageSchedule | proven | src/fallout_shared/package.cpp:111 |
| 0x00671E10 | SetPackageSecondLocation | proven | src/fallout_shared/package.cpp:3599 |
| 0x00672FC0 | SetPackageTarget | proven | src/fallout_shared/package.cpp:1618 |
| 0x00670FC0 | SetPackType | proven | src/fallout_shared/package.cpp:7706 |
| 0x00984F60 | SetProcedureType | decomp | src/fallout_shared/packagelocation.cpp:148 |
| 0x00674F30 | SetWaiting | proven | src/fallout_shared/package.cpp:5754 |
| 0x006707C0 | TESPackage | proven | src/fallout_shared/package.cpp:2726 |
| 0x00674DD0 | UsesPackageAnimation | decomp | src/fallout_shared/package.cpp:22 |
| 0x006708B0 | ~TESPackage | proven | src/fallout_shared/package.cpp:4587 |

### TESPackageData (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067AD40 | 'scalar deleting destructor' | proven | src/staging/blk_00660000_od.cpp:640 |
| 0x0067AD20 | TESPackageData | proven | src/staging/blk_00660000_od.cpp:175 |
| 0x0067AD70 | TESPackageData | proven | src/staging/blk_00660000_od.cpp:188 |

### TESPatrolPackageData (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067C420 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatapatrol.cpp:90 |
| 0x0067C500 | Compare | proven | src/fallout_shared/packagedatapatrol.cpp:274 |
| 0x0067C4B0 | CopyFrom | proven | src/fallout_shared/packagedatapatrol.cpp:297 |
| 0x0067C570 | Save | proven | src/fallout_shared/packagedatapatrol.cpp:216 |
| 0x0067C5E0 | SaveToBuffer | class | src/fallout_shared/packagedatapatrol.cpp:17 |
| 0x0067C3F0 | TESPatrolPackageData | proven | src/staging/blk_00660000_od.cpp:683 |
| 0x0067C450 | TESPatrolPackageData | proven | src/fallout_shared/packagedatapatrol.cpp:114 |
| 0x0067C490 | ~TESPatrolPackageData | proven | src/fallout_shared/packagedatapatrol.cpp:238 |

### TESUseItemPackageData (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067C7A0 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatauseitem.cpp:34 |
| 0x0067C960 | Compare | proven | src/fallout_shared/packagedatauseitem.cpp:74 |
| 0x0067C860 | CopyFrom | proven | src/fallout_shared/packagedatauseitem_rtti_variant_decl_variant.cpp:52 |
| 0x0067C9D0 | Save | proven | src/fallout_shared/packagedatauseitem.cpp:21 |
| 0x0067C770 | TESUseItemPackageData | proven | src/fallout_shared/package.cpp:4396 |
| 0x0067C7D0 | ~TESUseItemPackageData | proven | src/fallout_shared/packagedatauseitem.cpp:56 |

### TESUseWeaponPackageData (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067CB40 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatauseweapon.cpp:62 |
| 0x0067CFC0 | Compare | proven | src/fallout_shared/packagedatauseweapon.cpp:186 |
| 0x0067CD90 | CopyFrom | proven | src/fallout_shared/packagedatauseweapon.cpp:557 |
| 0x0067D1C0 | InitItem | class | src/fallout_shared/packagedatauseweapon.cpp:6 |
| 0x0067D350 | Save | proven | src/fallout_shared/packagedatauseweapon.cpp:308 |
| 0x0067D550 | SaveGame | proven | src/fallout_shared/packagedatauseweapon.cpp:618 |
| 0x0067CAA0 | TESUseWeaponPackageData | proven | src/staging/blk_00660000_od.cpp:2059 |
| 0x0067CB70 | TESUseWeaponPackageData | proven | src/fallout_shared/packagedatauseweapon.cpp:678 |
| 0x0067CC20 | TESUseWeaponPackageData | proven | src/fallout_shared/packagedatauseweapon.cpp:395 |
| 0x0067CCD0 | ~TESUseWeaponPackageData | proven | src/fallout_shared/packagedatauseweapon.cpp:95 |

### TrespassPackage (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F9220 | 'scalar deleting destructor' | proven | src/fallout/ai/trespasspackage.cpp:42 |
| 0x009F98E0 | InitLoadGame | proven | src/fallout/ai/trespasspackage.cpp:64 |
| 0x009F9840 | LoadGame | proven | src/fallout/ai/trespasspackage.cpp:22 |
| 0x009F91B0 | TrespassPackage | proven | src/staging/blk_009e0000_od.cpp:21 |
| 0x009F9250 | TrespassPackage | proven | src/fallout/ai/fleepackage.cpp:139 |
| 0x009F9450 | ~TrespassPackage | proven | src/staging/blk_009e0000_od.cpp:2233 |

### UseWeaponActorPackageData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0067D990 | 'scalar deleting destructor' | proven | src/fallout_shared/packagedatauseweapon.cpp:155 |
| 0x0067D9E0 | SetReferenceTarget | class | src/fallout_shared/packagedatauseweapon.cpp:45 |
| 0x0067D8F0 | UseWeaponActorPackageData | proven | src/fallout/ai/escortpackage.cpp:7 |
| 0x0067D9C0 | ~UseWeaponActorPackageData | proven | src/fallout_shared/packagedatauseweapon.cpp:523 |

### (free functions) (28)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090DD80 | CheckPackageMatch | decomp | src/fallout/ai/lowprocess.cpp:7873 |
| 0x0095EE80 | ClearIdleAnims | probable | src/fallout/ai/playercharacter.cpp:40990 |
| 0x005092F0 | CopyFromFurniture | class | src/fallout_shared/tesfurniture.cpp:342 |
| 0x00996F10 | CreateCombatProcedure | decomp | src/fallout/ai/combat/combatprocedure.cpp:447 |
| 0x00670A50 | DestroyPackage | class | src/fallout_shared/package.cpp:1570 |
| 0x008A75A0 | EnsurePackage26 | class | src/fallout/ai/actor_magic.cpp:3903 |
| 0x00672850 | GetPackageFloatValue | decomp | src/fallout/ai/mobileobject.cpp:1343 |
| 0x00981920 | GetPackageRefCount | decomp | src/staging/blk_00980000_od.cpp:1967 |
| 0x0091EC70 | GetRunningPackageData | class | src/fallout/ai/middlehighprocess.cpp:1214 |
| 0x0041D8C0 | HasRunOncePackage | decomp | src/fallout_shared/extradatalist.cpp:2908 |
| 0x00913250 | InitPackageFromExtraData | class | src/fallout/ai/lowprocess.cpp:5669 |
| 0x008A6170 | IsInPackageType | decomp | src/fallout/ai/actor.cpp:6837 |
| 0x0067ABD0 | IsPackageFlag80Set | decomp | src/fallout_shared/package.cpp:1511 |
| 0x0090CFA0 | IsProcedureTypeAllowed | class | src/fallout/ai/lowprocess.cpp:2654 |
| 0x009F0C40 | LoadPackageAndActors | class | src/fallout/ai/escortpackage.cpp:289 |
| 0x0067BD30 | LoadPackageData | class | src/fallout_shared/packagedataescort.cpp:198 |
| 0x008C6130 | MovePackageData | decomp | src/fallout/ai/actorpackage.cpp:472 |
| 0x0091EFE0 | ProcessPackageTarget | class | src/fallout/ai/middlehighprocess.cpp:3982 |
| 0x009CC4D0 | RunCombatProcedure | class | src/fallout/ai/combat/combatprocedureattackmelee.cpp:153 |
| 0x009D5FB0 | SaveEvadeProcedure | class | src/fallout/ai/combat/combatprocedureevade.cpp:124 |
| 0x0067B6F0 | SavePackageData | class | src/fallout_shared/packagedatadialogue.cpp:189 |
| 0x009F30D0 | SetPatrolRefIndex | probable | src/fallout/ai/patrolpackage.cpp:398 |
| 0x009D33E0 | UpdateCombatProcedure | class | src/fallout/ai/combat/combatprocedurebeincover.cpp:216 |
| 0x00921350 | UpdateFurnitureAlignment | probable | src/fallout/ai/middlehighprocess.cpp:3140 |
| 0x0091ECF0 | UpdatePackageSchedule | class | src/fallout/ai/middlehighprocess.cpp:5411 |
| 0x00564010 | UpdatePackagesFromBuffer | decomp | src/fallout_shared/tesobjectrefr.cpp:40268 |
| 0x00908E90 | UpdatePackageState | decomp | src/fallout/ai/lowprocess.cpp:4619 |
| 0x00909D00 | UpdatePackageTarget | class | src/fallout/ai/lowprocess.cpp:4807 |

## 6 Movement and pathfinding

ActorMover, the path handlers (Detailed for loaded actors, Virtual for unloaded ones) and pathing requests.

### ActorMover (37)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DAEC0 | 'scalar deleting destructor' | proven | src/fallout/ai/movement/actormover.cpp:690 |
| 0x009DAD00 | ActorMover | proven | src/staging/blk_009c0000_od.cpp:2654 |
| 0x009DAF80 | ClearCurrentData | proven | src/fallout/ai/movement/actormover.cpp:182 |
| 0x009DD150 | ClearMovementPath | decomp | src/fallout/ai/movement/actormover.cpp:71 |
| 0x009DCC80 | ComputeApproximateLocation | proven | src/fallout/ai/movement/actormover.cpp:3625 |
| 0x009DC980 | EndOfCurrentPathCheck | proven | src/fallout/ai/movement/actormover.cpp:7720 |
| 0x009DFA00 | FinishLoadGame | proven | src/fallout/ai/movement/actormover.cpp:653 |
| 0x009DD1C0 | FinishMoving | proven | src/fallout/ai/movement/actormover.cpp:433 |
| 0x009DE060 | ForceMoveMode | proven | src/fallout/ai/movement/actormover.cpp:1089 |
| 0x009DD0C0 | ForceStopMoving | decomp | src/fallout/ai/movement/actormover.cpp:99 |
| 0x009DDB70 | GetActorStateFlags | class | src/fallout/ai/movement/actormover.cpp:38 |
| 0x009DE2B0 | GetCurrentGoal | proven | src/fallout/ai/movement/actormover.cpp:3842 |
| 0x0059BB30 | GetCurrentMoveModeType | decomp | src/fallout_shared/pathfinding/navmesh.cpp:140 |
| 0x009DCC50 | GetDistanceRemaining | proven | src/fallout/ai/movement/actormover.cpp:1503 |
| 0x009DE270 | GetLookAtTargetPosition | decomp | src/fallout_shared/globalfunc.cpp:408 |
| 0x009DDBB0 | GetPathingDelta | class | src/fallout/ai/movement/actormover.cpp:59 |
| 0x009DD130 | GetPreferredMoveModeType | proven | src/fallout/ai/movement/actormover.cpp:358 |
| 0x009DCDB0 | HasActiveMovement | decomp | src/fallout/ai/movement/actormover.cpp:84 |
| 0x008B3D10 | HasLookAtTarget | decomp | src/fallout/ai/movement/actormover.cpp:6 |
| 0x009DF8C0 | InitLoadGame | proven | src/fallout/ai/movement/actormover.cpp:2445 |
| 0x009DDB50 | IsMovementActive | decomp | src/fallout/ai/movement/actormover.cpp:11 |
| 0x009DCD40 | IsPathingComplete | proven | src/fallout/ai/movement/actormover.cpp:329 |
| 0x009DF3D0 | LoadGame | proven | src/fallout/ai/movement/actormover.cpp:6305 |
| 0x009DF010 | MoveActorToLocation | proven | src/fallout/ai/movement/actormover.cpp:7644 |
| 0x009DCE20 | RequestRotateActor | proven | src/fallout/ai/movement/actormover.cpp:843 |
| 0x009DCE80 | RequestRotateActor | proven | src/fallout/ai/movement/actormover.cpp:4613 |
| 0x009DE080 | ResetMovementData | class | src/fallout/ai/movement/actormover.cpp:16 |
| 0x009DE230 | RunProcedure | decomp | src/fallout/ai/movement/actormover.cpp:44 |
| 0x009DF100 | SaveGame | proven | src/fallout/ai/movement/actormover.cpp:5951 |
| 0x009DBA50 | SetGoal | proven | src/fallout/ai/movement/actormover.cpp:984 |
| 0x009DBB60 | SetGoalAndAngle | proven | src/fallout/ai/movement/actormover.cpp:1008 |
| 0x009DBC30 | SetGoalAndAngle | proven | src/fallout/ai/movement/actormover.cpp:1307 |
| 0x009DE160 | SetLookAtTarget | proven | src/fallout/ai/movement/actormover.cpp:1156 |
| 0x009DD0A0 | StopMoving | decomp | src/fallout/ai/movement/actormover.cpp:23 |
| 0x009DC120 | Update | proven | src/fallout/ai/movement/actormover.cpp:3249 |
| 0x009DC590 | UpdateMovement | decomp | src/fallout/ai/movement/actormover.cpp:51 |
| 0x009DAEF0 | ~ActorMover | proven | src/fallout/ai/movement/actormover.cpp:908 |

### ActorPathHandler (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DFE10 | 'scalar deleting destructor' | proven | src/fallout/ai/movement/actorpathhandler.cpp:18 |
| 0x009DFD70 | ActorPathHandler | proven | src/staging/blk_009c0000_od.cpp:2705 |
| 0x009DFE40 | ActorPathHandler | proven | src/staging/blk_009c0000_od.cpp:2739 |
| 0x009DFDF0 | CompleteNoPathUpdate | class | src/fallout_shared/magic/effectitemlist.cpp: |
| 0x009DFED0 | ~ActorPathHandler | proven | src/staging/blk_009c0000_od.cpp:2762 |

### bhkCharacterController (18)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C70C60 | 'scalar deleting destructor' | proven | src/staging/blk_00c60000_o2.cpp:1483 |
| 0x008A50D0 | FUN_008a50d0 | probable | src/fallout/ai/actor.cpp:44887 |
| 0x00C6FA20 | FUN_00c6fa20 | unnamed | src/havok/common/base/math/vector/hkvector4.cpp:577 |
| 0x00819250 | GetCollisionGroup | proven | src/fallout/magic/magiccaster.cpp:158 |
| 0x00810660 | GetNiObject | proven | src/staging/blk_00800000_od.cpp:426 |
| 0x00C6E300 | GetPosition | proven | src/havok/common/base/math/vector/hkvector4.cpp:438 |
| 0x00C6E280 | GetRadius | proven | src/staging/blk_00c60000_o2.cpp:8534 |
| 0x005C0880 | GetState | proven | src/fallout_shared/tesscriptfunctions.cpp:1702 |
| 0x00560D30 | GetVectorElement | decomp | src/bshavok/bhkcharactercontroller_h_unit.cpp: |
| 0x00C73ED0 | InitWithParams | proven | src/staging/blk_00c60000_o2.cpp:24508 |
| 0x00C73170 | Move | proven | src/fallout/ai/mobileobject_o2_variant_rtm_variant.cpp:831 |
| 0x00806F10 | QCinfoSize | proven | src/fallout/magic/bhkcharacterlistenerspell.cpp:29 |
| 0x005C0860 | QIsFlying | proven | src/fallout_shared/tesscriptfunctions.cpp:4890 |
| 0x00810A80 | QWaterHeight | proven | src/fallout/magic/magicballprojectile.cpp:11 |
| 0x008106B0 | SetFallTime | proven | src/staging/blk_00800000_od.cpp:175 |
| 0x005620E0 | SetPosition | proven | src/fallout_shared/tesobjectrefr_o2_variant_od_oy_noo2_variant.cpp:2413 |
| 0x0057B1D0 | SetWaterHeight | proven | src/fallout_shared/tesobjectrefr.cpp:6332 |
| 0x00C705C0 | ~bhkCharacterController | proven | src/staging/blk_00c60000_o2.cpp:23204 |

### bhkCharacterProxy (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C6D010 | 'scalar deleting destructor' | proven | src/staging/blk_00c60000_o2.cpp:7157 |
| 0x00C6CE80 | bhkCharacterProxy | proven | src/staging/blk_00c60000_o2.cpp:7106 |
| 0x00806F00 | GetRTTI | class | src/fallout/magic/bhkcharacterlistenerspell.cpp:18 |
| 0x00CAC6B0 | GetViewerStrings | proven | src/staging/blk_00ca0000_o2.cpp:11682 |
| 0x00CABFF0 | LoadBinary | proven | src/staging/blk_00ca0000_o2.cpp:5312 |
| 0x00C6CEE0 | QCinfoSize | proven | src/staging/blk_00c60000_o2.cpp:7112 |
| 0x00CAC070 | RegisterStreamables | proven | src/staging/blk_00ca0000_o2.cpp:880 |
| 0x00CAC0B0 | SaveBinary | proven | src/staging/blk_00ca0000_o2.cpp:5364 |
| 0x00CABF50 | ~bhkCharacterProxy | proven | src/staging/blk_00ca0000_o2.cpp:9401 |

### bhkCharacterStateInAir (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CD3F90 | bhkCharacterStateInAir | proven | src/staging/blk_00cc0000_o2.cpp:14968 |

### bhkCharacterStateJumping (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CD4260 | bhkCharacterStateJumping | proven | src/staging/blk_00cc0000_o2.cpp:14983 |

### bhkCharacterStateOnGround (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CD47E0 | bhkCharacterStateOnGround | proven | src/staging/blk_00cc0000_o2.cpp:1724 |

### bhkCharacterStateProjectile (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CD3C90 | bhkCharacterStateProjectile | proven | src/staging/blk_00cc0000_o2.cpp:14938 |

### bhkCharacterStateSwimming (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CD44C0 | bhkCharacterStateSwimming | proven | src/staging/blk_00cc0000_o2.cpp:1708 |

### DetailedActorPathHandler (19)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E0160 | 'scalar deleting destructor' | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:1157 |
| 0x009E7550 | CheckForEndRotate | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:10797 |
| 0x009E2AA0 | ComputeMoveMode | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:2229 |
| 0x009DFF40 | DetailedActorPathHandler | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:9719 |
| 0x009E0190 | DetailedActorPathHandler | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:6707 |
| 0x009E2860 | GetDistanceRemaining | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5246 |
| 0x009E28A0 | GetPercentTraveled | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5279 |
| 0x009E9760 | InitLoadGame | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:6363 |
| 0x009E3BE0 | IsMovementBlocked | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5319 |
| 0x009E9390 | LoadGame | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:1080 |
| 0x009E8B50 | PrintCurrentStatus | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:9528 |
| 0x009E8790 | ResetMoveModeAndDelta | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:911 |
| 0x009E39C0 | SetInitialPathState | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:32 |
| 0x009E3380 | TransitionFrom | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:49 |
| 0x009E0930 | TurnToAngle | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:6 |
| 0x009E4800 | UpdateHeading | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:3461 |
| 0x009E4C60 | UpdateLooking | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:4919 |
| 0x009E7D70 | UpdateRotation | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:9143 |
| 0x009E03E0 | ~DetailedActorPathHandler | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:114 |

### linear_cast_d9a2a0::PathBuilder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00D9A2A0 | FUN_00d9a2a0 | unnamed | src/staging/blk_00d80000_o2_gs_nogs_rtm_variant.cpp:3252 |

### PathBuilder (15)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006CC5E0 | AddNodesFromNavMesh | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:660 |
| 0x006CAA40 | AppendPathNodeLocations | decomp | src/fallout_shared/pathfinding/pathfind.cpp:108 |
| 0x006CA850 | BuildActorPathSegments | decomp | src/fallout_shared/pathfinding/pathbuilder.cpp:76 |
| 0x006CA0E0 | BuildDetailedPath | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:7884 |
| 0x006C8E10 | BuildPath | decomp | src/fallout_shared/pathfinding/pathbuilder.cpp:39 |
| 0x006CEC40 | BuildPathSegment | decomp | src/staging/blk_006c0000_od.cpp:3168 |
| 0x006CB050 | BuildPathToValidNavMeshTriangle | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:1983 |
| 0x006CB4C0 | BuildStraightPathUsingRayCasts | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:1024 |
| 0x006C9B20 | BuildTeleportDoorPath | proven | src/staging/blk_006c0000_od.cpp:3070 |
| 0x006C9FC0 | FindLoadedNodeIndices | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:1187 |
| 0x006E8F60 | FUN_006e8f60 | unnamed | src/fallout_shared/pathfinding/pathingsolution.cpp:358 |
| 0x009DFD50 | FUN_009dfd50 | unnamed | src/staging/blk_009c0000_od.cpp:210 |
| 0x006C8D30 | PathBuilder | decomp | src/fallout_shared/pathfinding/pathbuilder.cpp:29 |
| 0x006CD1F0 | TryBuildStraightPath | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:5079 |
| 0x006CB950 | TryConnectPathNodes | decomp | src/fallout_shared/pathfinding/pathbuilder.cpp:2239 |

### Pathing (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006D0900 | BuildPath | decomp | src/fallout_shared/pathfinding/pathfind.cpp:64 |
| 0x006D6F80 | FindClosestPathingPoint | decomp | src/fallout_shared/pathfinding/pathfind.cpp:38 |
| 0x006D4EB0 | FindPathDistance | decomp | src/fallout_shared/pathfinding/pathfind.cpp:28 |
| 0x006D7490 | FindPathingLocation | decomp | src/fallout_shared/pathfinding/pathfind.cpp:11 |
| 0x00693D70 | FindReferenceByFormId | decomp | src/fallout_shared/pathfinding/pathfind.cpp:18 |

### PathingActorData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E2B20 | operator= | decomp | src/fallout_shared/doorlock.cpp:41 |

### PathingAvoidNode (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DC910 | LoadGame | proven | src/fallout_shared/pathfinding/pathingavoidnode.cpp:95 |
| 0x006915D0 | PathingAvoidNode | proven | src/fallout_shared/pathfinding/navmesh.cpp:419 |
| 0x006DC890 | SaveGame | proven | src/staging/blk_006c0000_od.cpp:1874 |

### PathingAvoidNodeArray (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E3880 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:179 |
| 0x006DC9F0 | ComputeCenter | proven | src/fallout_shared/pathfinding/pathingavoidnode.cpp:141 |
| 0x006E3850 | PathingAvoidNodeArray | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:187 |
| 0x006E38B0 | ~PathingAvoidNodeArray | decomp | src/fallout_shared/pathfinding/pathingrequest.cpp:194 |

### PathingCoverLocation (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E4650 | CheckDynamicCoverValid | proven | src/havok/unplaced/pathingrequestcover.cpp:371 |
| 0x006E4570 | GetKey | proven | src/havok/unplaced/pathingrequestcover.cpp:419 |
| 0x006E4980 | Load | class | src/havok/unplaced/pathingrequestcover.cpp:208 |
| 0x006D3200 | PathingCoverLocation | proven | src/staging/blk_006c0000_od.cpp:5160 |
| 0x006D6E50 | PathingCoverLocation | proven | src/fallout_shared/pathfinding/pathfind.cpp:1647 |
| 0x0099AA80 | PathingCoverLocation | proven | src/fallout/ai/combat/combatstate.cpp:2570 |
| 0x006E48A0 | SaveToBuffer | class | src/havok/unplaced/pathingrequestcover.cpp:178 |
| 0x006D32C0 | ~PathingCoverLocation | proven | src/staging/blk_006c0000_od.cpp:2101 |

### PathingGraphNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006CA0C0 | IsTransitionNode | decomp | src/fallout_shared/globalfunc.cpp:419 |

### PathingGrid (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E0C40 | SaveGame | decomp | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:1113 |

### PathingLocation (28)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DD640 | FindNavMeshTriangle | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:69 |
| 0x006DD4F0 | GetContainingCell | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:45 |
| 0x006DF760 | GetTriangle | proven | src/fallout_shared/pathfinding/pathfind.cpp:434 |
| 0x006DE250 | HasPathingLocation | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:134 |
| 0x006DD6A0 | HasValidTriangle | decomp | src/fallout_shared/pathfinding/navmeshinfo_h_unit.cpp: |
| 0x006DEEB0 | IsCloseTo | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:725 |
| 0x006DF010 | LoadGame | class | src/fallout_shared/pathfinding/pathinglocation.cpp:109 |
| 0x006DCCE0 | operator= | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:31 |
| 0x004FF7E0 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:6 |
| 0x006DCBB0 | PathingLocation | proven | src/fallout_shared/tesobjectrefr.cpp:6726 |
| 0x006DCC40 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:365 |
| 0x006DCD70 | PathingLocation | proven | src/fallout_shared/tesobjectrefr.cpp:9116 |
| 0x006DCE10 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:13 |
| 0x006DCE60 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:432 |
| 0x006DCEA0 | PathingLocation | proven | src/staging/blk_006c0000_od.cpp:1698 |
| 0x006DCEE0 | PathingLocation | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1498 |
| 0x006DCF20 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:400 |
| 0x006DD010 | PathingLocation | proven | src/fallout_shared/pathfinding/navmesh.cpp:188 |
| 0x006DD0D0 | PathingLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:516 |
| 0x006DD220 | PathingLocation | proven | src/staging/blk_006c0000_od.cpp:4492 |
| 0x006DDBE0 | ResetLocation | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:24 |
| 0x006DD610 | ResolveNavMesh | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:59 |
| 0x006DEF40 | SaveGame | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:637 |
| 0x006DCFE0 | SetAllMeshesReachable | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:329 |
| 0x006DD460 | SetLocation | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:589 |
| 0x006F4ED0 | SetLocationSimple | proven | src/staging/blk_006e0000_od.cpp:745 |
| 0x006DD3E0 | SetNavMeshInfo | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:557 |
| 0x006DD280 | SetupData | proven | src/fallout_shared/pathfinding/pathinglocation.cpp:671 |

### PathingLocationArray (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006D00A0 | ConstructItems | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:101 |
| 0x006CF1B0 | FUN_006cf1b0 | unnamed | src/unmapped/bssimplearray.cpp:296 |
| 0x006D0140 | ResizeAndConstruct | decomp | src/staging/blk_006c0000_od.cpp:1756 |

### PathingLocationCheck (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DED70 | FUN_006ded70 | probable | src/fallout_shared/pathfinding/pathinglocation.cpp:1071 |

### PathingLocationOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006ED730 | FUN_006ed730 | probable | src/fallout_shared/pathfinding/pathinglocation.cpp:774 |

### PathingLocationProxy (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DD6F0 | FindContainingTriangle | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:200 |
| 0x006DD540 | GetAssociatedNavMesh | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:85 |

### PathingLOSGrid (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DFDC0 | IsLocationSeen | proven | src/staging/blk_006c0000_od.cpp:2384 |
| 0x006E0070 | LoadGame | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:1303 |
| 0x006DFFC0 | SaveGame | proven | src/staging/blk_006c0000_od.cpp:5343 |
| 0x006DFE90 | SetLocationSeen | proven | src/staging/blk_006c0000_od.cpp:1938 |

### PathingLOSGridCell (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DF9C0 | SaveGame | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:337 |
| 0x006DF440 | SetSeenTrianglesFromLOSMap | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:601 |

### PathingLOSGridMap (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E0270 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:70 |
| 0x006E03E0 | Clear | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:293 |
| 0x006E0480 | FUN_006e0480 | unnamed | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:87 |
| 0x006E0320 | Initialize | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:753 |
| 0x006E0D20 | LoadGame | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:244 |
| 0x006E01D0 | PathingLOSGridMap | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:697 |
| 0x006E05B0 | Reset | decomp | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:204 |
| 0x006E05F0 | Setup | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:523 |
| 0x006E02A0 | ~PathingLOSGridMap | proven | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:1363 |

### PathingLOSGridMapX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E0920 | UpdateFromNavMeshArray | decomp | src/fallout_shared/pathfinding/pathinglosgridmap.cpp:950 |

### PathingLOSMap (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E1440 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathinglosmap.cpp:15 |
| 0x006D7EE0 | GetAt | proven | src/fallout_shared/pathfinding/pathfind.cpp:828 |
| 0x006AB3B0 | GetLOSValue | decomp | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:140 |
| 0x006E1670 | GetNavMeshAndTriangleForIndex | proven | src/fallout_shared/pathfinding/pathinglosmap.cpp:340 |
| 0x006E1610 | GetTriangleScore | decomp | src/fallout_shared/pathfinding/pathinglosmap.cpp:37 |
| 0x006E2050 | HasNavMeshEntry | decomp | src/fallout_shared/pathfinding/pathinglosmap.cpp:119 |
| 0x006E1370 | PathingLOSMap | proven | src/staging/blk_006e0000_od.cpp:4283 |
| 0x006E1500 | Setup | proven | src/fallout_shared/pathfinding/pathinglosmap.cpp:279 |
| 0x006E1470 | ~PathingLOSMap | proven | src/fallout_shared/pathfinding/pathinglosmap.cpp:225 |

### PathingNode (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E22F0 | ActivateNode | proven | src/fallout_shared/pathfinding/pathingnode.cpp:23 |
| 0x006E23B0 | LoadGame | proven | src/staging/blk_006e0000_od.cpp:7815 |

### PathingRequest (25)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E25E0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:222 |
| 0x006E2750 | CopyTo | class | src/fallout_shared/pathfinding/pathingrequest.cpp:116 |
| 0x006E2F80 | CreateRequestForType | decomp | src/fallout_shared/pathfinding/pathingrequest.cpp:88 |
| 0x009A7C40 | GetActorRadius | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x009B0BD0 | GetCenterRadius | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x00505C00 | GetFaceTargetAtGoal | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:805 |
| 0x0051B8E0 | GetGoalZDelta | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x0051B860 | GetSmoothingRandomness | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x006A78F0 | GetTargetRadius | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x006E38D0 | InitLoadGame | class | src/fallout_shared/pathfinding/pathingrequest.cpp:9 |
| 0x004FDF60 | IsRandomBelowRadiusThreshold | decomp | src/fallout/ai/combat/projectile.cpp:384 |
| 0x006E34F0 | LoadGame | class | src/fallout_shared/pathfinding/pathingrequest.cpp:29 |
| 0x006E2420 | PathingRequest | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:149 |
| 0x006E26A0 | PathingRequest | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:560 |
| 0x006E3230 | SaveGame | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:429 |
| 0x0051B840 | SetActorRadius | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x006D3AE0 | SetActorRadius | proven | src/fallout/ai/movement/actormover.cpp:1076 |
| 0x006D61E0 | SetAvoidNodeArray | decomp | src/gamebryo2.2/corelibs/nimain/nismartpointer_h_unit.cpp: |
| 0x006E2B90 | SetCanFly | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:392 |
| 0x006E2B70 | SetCanSwim | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:260 |
| 0x006E2B50 | SetCantOpenDoors | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:249 |
| 0x006D3B00 | SetCenterRadius | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x006D1BC0 | SetDestination | decomp | src/gamebryo2.2/corelibs/nimain/nismartpointer_h_unit.cpp: |
| 0x006E2960 | SetSmoothingRandomness | decomp | src/fallout_shared/tesobjecttree_h_unit.cpp: |
| 0x006E2620 | ~PathingRequest | proven | src/fallout_shared/pathfinding/pathingrequest.cpp:346 |

### PathingRequestClosePoint (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E3F70 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestclosepoint.cpp:41 |
| 0x006E5F00 | FUN_006e5f00 | unnamed | src/fallout_shared/pathfinding/pathingrequestclosepoint.cpp:67 |
| 0x006E5F50 | FUN_006e5f50 | unnamed | src/fallout_shared/pathfinding/pathingrequestclosepoint.cpp:96 |
| 0x006E3F30 | PathingRequestClosePoint | proven | src/fallout_shared/pathfinding/pathingrequestclosepoint.cpp:25 |
| 0x006E3FB0 | PathingRequestClosePoint | proven | src/fallout_shared/pathfinding/pathingrequestclosepoint.cpp:197 |

### PathingRequestCover (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E41E0 | 'scalar deleting destructor' | proven | src/havok/unplaced/pathingrequestcover.cpp:543 |
| 0x006E4080 | PathingRequestCover | proven | src/staging/blk_006e0000_od.cpp:12260 |
| 0x006E4400 | SetCover | decomp | src/havok/unplaced/pathingrequestcover.cpp:95 |

### PathingRequestCoveredMove (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E4BB0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestcoveredmove.cpp:68 |
| 0x006E4A50 | PathingRequestCoveredMove | proven | src/staging/blk_006e0000_od.cpp:10950 |
| 0x006E4D20 | PathingRequestCoveredMove | proven | src/fallout_shared/pathfinding/pathingrequestcoveredmove.cpp:233 |
| 0x006E4BF0 | ~PathingRequestCoveredMove | proven | src/fallout_shared/pathfinding/pathingrequestcoveredmove.cpp:348 |

### PathingRequestDebugView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E2BE0 | PrintDebugInfo | class | src/fallout_shared/pathfinding/pathingrequest.cpp:584 |

### PathingRequestFlee (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E53C0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestflee.cpp:20 |
| 0x006E5470 | CopyToWithFleeData | class | src/fallout_shared/pathfinding/pathingrequestflee.cpp:114 |
| 0x006E54E0 | LoadGame | proven | src/fallout_shared/pathfinding/pathingrequestflee.cpp:72 |
| 0x006E5390 | PathingRequestFlee | proven | src/fallout_shared/pathfinding/pathingrequestflee.cpp:94 |
| 0x006E5400 | PathingRequestFlee | proven | src/fallout_shared/pathfinding/pathingrequestflee.cpp:190 |
| 0x006E54B0 | SaveGame | proven | src/fallout_shared/pathfinding/pathingrequestflee.cpp:46 |

### PathingRequestHide (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E55A0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequesthide.cpp:15 |
| 0x006E56F0 | CopyTo | proven | src/fallout_shared/pathfinding/pathingrequesthide.cpp:116 |
| 0x006E5790 | LoadGame | proven | src/fallout_shared/pathfinding/pathingrequesthide.cpp:87 |
| 0x006E5510 | PathingRequestHide | proven | src/fallout_shared/pathfinding/pathingrequestcoveredmove.cpp:653 |
| 0x006E5640 | PathingRequestHide | proven | src/fallout_shared/pathfinding/pathingrequesthide.cpp:221 |
| 0x006E5740 | SaveGame | proven | src/fallout_shared/pathfinding/pathingrequesthide.cpp:57 |

### PathingRequestLOS (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E5890 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:23 |
| 0x006E5A80 | CopyTo | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:128 |
| 0x006E5C00 | LoadGame | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:74 |
| 0x006E57E0 | PathingRequestLOS | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:286 |
| 0x006E5940 | PathingRequestLOS | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:466 |
| 0x006E5B20 | SaveGame | proven | src/fallout_shared/pathfinding/pathingrequestlos.cpp:164 |

### PathingRequestOptimalLocation (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E5D70 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestoptimallocation.cpp:18 |
| 0x006E5E60 | CopyTo | proven | src/fallout_shared/pathfinding/pathingrequestoptimallocation.cpp:79 |
| 0x006E5D10 | PathingRequestOptimalLocation | proven | src/fallout_shared/pathfinding/pathingrequestoptimallocation.cpp:47 |
| 0x006E5DB0 | PathingRequestOptimalLocation | proven | src/fallout_shared/pathfinding/pathingrequestoptimallocation.cpp:110 |

### PathingRequestSafeStraightLine (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E5FD0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingrequestsafestraightline.cpp:14 |
| 0x006E6080 | CopyTo | proven | src/fallout_shared/pathfinding/pathingrequestsafestraightline.cpp:80 |
| 0x006E6110 | LoadGame | proven | src/fallout_shared/pathfinding/pathingrequestsafestraightline.cpp:63 |
| 0x006E5FA0 | PathingRequestSafeStraightLine | proven | src/staging/blk_006e0000_od.cpp:1286 |
| 0x006E6010 | PathingRequestSafeStraightLine | proven | src/fallout_shared/pathfinding/pathingrequestsafestraightline.cpp:105 |

### PathingSearchRayCast (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E6280 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingsearchraycast.cpp:13 |
| 0x006E6DB0 | CleanUpRayCasts | proven | src/staging/blk_006e0000_od.cpp:4590 |
| 0x006E61A0 | PathingSearchRayCast | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:8008 |
| 0x006E6320 | ProcessRayCast | decomp | src/fallout_shared/pathfinding/pathbuilder.cpp:5246 |
| 0x006E62B0 | ~PathingSearchRayCast | proven | src/staging/blk_006e0000_od.cpp:1305 |

### PathingSolution (17)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E76F0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:56 |
| 0x0069F920 | AddPathingNode | proven | src/unmapped/bssimplearray.cpp:2385 |
| 0x006D1520 | AddVirtualPathingNode | proven | src/fallout_shared/pathfinding/pathfind.cpp:1537 |
| 0x006E7800 | CalculatePathLength | decomp | src/fallout_shared/pathfinding/pathingsolution.cpp:17 |
| 0x006C93A0 | ClearCurrentDetailedPath | proven | src/fallout_shared/pathfinding/pathbuilder.cpp:169 |
| 0x006E78D0 | ComputeDetailedPathLength | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:429 |
| 0x006E84B0 | ComputeDistanceToParameter | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:911 |
| 0x006E7A10 | ComputeLocationFromParameter | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:823 |
| 0x006E7E70 | FindPointOnPath | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:563 |
| 0x009DDB30 | GetLastVirtualNode | proven | src/fallout/ai/movement/actormover.cpp:1272 |
| 0x006E7970 | GetNode | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:118 |
| 0x006E78B0 | GetVirtualNode | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:100 |
| 0x009DC530 | IsValid | proven | src/fallout/ai/movement/actormover.cpp:232 |
| 0x006E8D50 | LoadGame | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:1128 |
| 0x006E7650 | PathingSolution | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:7 |
| 0x006E8B10 | SaveGame | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:1378 |
| 0x006E7720 | ~PathingSolution | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:404 |

### PathingSpline (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E9AF0 | ApproxLength | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:1200 |
| 0x006E9830 | FindPointOnSpline | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:1440 |
| 0x006E7CC0 | Interpolate | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:237 |
| 0x006E9AB0 | Interpolate | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:739 |
| 0x006E7D60 | InterpolateNoZ | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:465 |
| 0x006E8450 | SetKeys | proven | src/fallout_shared/pathfinding/pathingsolution.cpp:343 |

### PathingTaskData (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E9C90 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathmanager.cpp:502 |
| 0x006EA350 | ComputeRayCasts | proven | src/fallout_shared/pathfinding/pathmanager.cpp:1152 |
| 0x006EA490 | HasPendingMessages | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:16 |
| 0x006E9CC0 | PathingTaskData | proven | src/fallout_shared/pathfinding/pathmanager.cpp:7353 |
| 0x006E9FC0 | Process | class | src/fallout_shared/pathfinding/pathmanager.cpp:73 |
| 0x006E9E20 | ~PathingTaskData | proven | src/fallout_shared/pathfinding/pathmanager.cpp:246 |

### PathingTaskShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006E9DB0 | AssignRequestAndQueue | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:1058 |

### PathManager (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006EB9D0 | BuildPath | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:48 |
| 0x006EB8C0 | Initialize | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:40 |
| 0x006EB820 | PathManager | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:32 |
| 0x0047D0B0 | QInstance | proven | src/fallout/ai/movement/actormover.cpp:6702 |
| 0x006EB980 | Release | proven | src/fallout_shared/pathfinding/pathmanager.cpp:5568 |

### PathSearch (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AACB0 | ExpandNeighbors | class | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:354 |
| 0x006F3D90 | FindPath | decomp | src/staging/blk_006e0000_od.cpp:11508 |
| 0x00996860 | FindPath | decomp | src/staging/blk_00980000_od.cpp:5748 |
| 0x006B3A30 | FUN_006b3a30 | unnamed | src/staging/blk_006a0000_od.cpp:8307 |

### PathSmoother (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006EDD30 | AddFirstEdge | proven | src/staging/blk_006e0000_od.cpp:5213 |
| 0x006EDBC0 | AddStartVert | proven | src/staging/blk_006e0000_od.cpp:8337 |
| 0x006ED850 | BuildInternalArrays | proven | src/staging/blk_006e0000_od.cpp:11093 |
| 0x006EEF80 | BuildShrunkEdgeLeftRightArrays | proven | src/staging/blk_006e0000_od.cpp:5602 |
| 0x006F1E90 | IsSegmentValid | proven | src/staging/blk_006e0000_od.cpp:1814 |
| 0x006ED100 | PathSmoother | proven | src/fallout_shared/pathfinding/pathfind.cpp:1700 |
| 0x006F0050 | PushPoint | proven | src/staging/blk_006e0000_od.cpp:9113 |
| 0x006ED530 | SmoothPath | proven | src/fallout_shared/pathfinding/pathsmoother.cpp:218 |
| 0x006F1D30 | SmoothPathDirections | decomp | src/staging/blk_006e0000_od.cpp:5714 |
| 0x006ED220 | ~PathSmoother | proven | src/fallout_shared/pathfinding/pathsmoother.cpp:113 |

### PathSmootherAccess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B2060 | FindPath | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:6865 |

### PathSmootherPOVSearch (17)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AD660 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:1200 |
| 0x006B05F0 | AddNavMeshEdgeRecord | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:374 |
| 0x006AFCC0 | AddPathPoints | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:6 |
| 0x006AEFC0 | AddPOVsFromAvoidNodes | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:4394 |
| 0x006AF500 | BuildSmoothedPath | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:106 |
| 0x006B2C00 | CalculatePathCost | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:445 |
| 0x006B1E50 | CheckArcAgainstNavMesh | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:6766 |
| 0x006B0AD0 | CollectConnections | class | src/fallout_shared/pathfinding/pathsmootherpov.cpp:260 |
| 0x006AF2B0 | CollectUniqueNavMeshes | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:503 |
| 0x006B23D0 | DoubleCheckArcAgainstNavMesh | proven | src/fallout_shared/pathfinding/pathsmootherpov_decl_variant.cpp:63 |
| 0x006B0F40 | FindPathToPoint | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp:573 |
| 0x006B2FC0 | FUN_006b2fc0 | unnamed | src/fallout_shared/pathfinding/pathsmootherpov.cpp:2030 |
| 0x006B1DC0 | HasReachedGoal | class | src/fallout_shared/pathfinding/pathsmootherpov.cpp:538 |
| 0x006AD4C0 | PathSmootherPOVSearch | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:1391 |
| 0x006AD770 | SearchForPath | decomp | src/fallout_shared/pathfinding/pathsmootherpov.cpp: |
| 0x006B25F0 | TripleCheckSegmentAgainstNavMesh | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:7184 |
| 0x006AD690 | ~PathSmootherPOVSearch | proven | src/fallout_shared/pathfinding/pathsmootherpov.cpp:533 |

### VirtualActorPathHandler (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EA740 | 'scalar deleting destructor' | proven | src/fallout/ai/movement/virtualactorpathhandler.cpp:742 |
| 0x009EB070 | GetDistanceRemaining | proven | src/fallout/ai/movement/virtualactorpathhandler.cpp:705 |
| 0x009EA710 | GetPathingDelta | class | src/fallout/ai/movement/virtualactorpathhandler_h_unit.cpp: |
| 0x009EB0B0 | GetPercentTraveled | proven | src/fallout/ai/movement/virtualactorpathhandler.cpp:795 |
| 0x009EA820 | Init | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:39 |
| 0x009EB3E0 | LoadGame | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:21 |
| 0x009EB040 | SetInitialPathState | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:13 |
| 0x009EA770 | VirtualActorPathHandler | proven | src/fallout/ai/movement/virtualactorpathhandler.cpp:29 |
| 0x009EA7C0 | ~VirtualActorPathHandler | proven | src/fallout/ai/movement/virtualactorpathhandler.cpp:759 |

### (free functions) (25)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006C99C0 | AddPathingItem | probable | src/fallout_shared/pathfinding/pathbuilder.cpp:357 |
| 0x006D3AC0 | AssignPathingLocation | probable | src/staging/blk_006c0000_od.cpp:375 |
| 0x006AC340 | BuildPathingLocationAndSearch | decomp | src/fallout_shared/pathfinding/navmeshsearchslpoint.cpp:56 |
| 0x006D3780 | BuildPathingRequest | decomp | src/staging/blk_006c0000_od.cpp:3450 |
| 0x00553FC0 | CopyCharacterControllerVector | decomp | src/fallout/ai/mobileobject.cpp:148 |
| 0x006D3B20 | DestroyPathingRequest | decomp | src/staging/blk_006c0000_od.cpp:2117 |
| 0x006DAD70 | DestroyPathingRequest | decomp | src/fallout_shared/pathfinding/pathingrequest.cpp:381 |
| 0x006EB7F0 | DispatchPathingMessage | decomp | src/fallout_shared/pathfinding/pathmanager.cpp:396 |
| 0x006D6F60 | ForwardToPathing | decomp | src/fallout_shared/pathfinding/pathfind.cpp:331 |
| 0x005770E0 | GetCharacterControllerValue | decomp | src/staging/blk_00560000_od.cpp:364 |
| 0x009DE460 | GetPathingLocation | decomp | src/fallout/ai/movement/actormover.cpp:1700 |
| 0x006D9100 | GetPathingLocationNormal | decomp | src/fallout_shared/pathfinding/pathfind.cpp:882 |
| 0x009E2900 | GetPathingPosition | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:5440 |
| 0x009DE420 | HasPathingSolution | decomp | src/fallout/ai/movement/actormover.cpp:870 |
| 0x006D9480 | IsPathingLocationClear | decomp | src/fallout_shared/pathfinding/pathfind.cpp:6078 |
| 0x006DD5A0 | IsPathingLocationFlagSet | decomp | src/fallout_shared/pathfinding/pathinglocation.cpp:336 |
| 0x009A6050 | NegateCharacterControllerValue | decomp | src/staging/blk_009a0000_od.cpp:1753 |
| 0x009E8690 | RemoveRefFromPathHandler | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:4993 |
| 0x006E77B0 | ResetPathingSolution | decomp | src/fallout_shared/pathfinding/pathingsolution.cpp:79 |
| 0x009DFB80 | ResetPathingState | class | src/fallout/ai/movement/actormover.cpp:1210 |
| 0x008DBDA0 | SetPathingLocation | decomp | src/fallout/ai/highprocess.cpp:5048 |
| 0x009DBC90 | SetupPathingRequest | decomp | src/fallout/ai/movement/actormover.cpp:1856 |
| 0x008EEAC0 | SubmitWaterHeightPathingRequest | probable | src/fallout/ai/highprocess.cpp:18139 |
| 0x009E8000 | UpdatePathingGoal | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:4448 |
| 0x009E6BA0 | UpdatePathingOrigin | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:6072 |

## 6b Navmesh (the data paths run on)

NavMesh data and searches the path code uses.

### bounds_detail::NavMeshBounds (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0069C070 | FUN_0069c070 | unnamed | src/staging/blk_00680000_od.cpp:3219 |

### NavMesh (44)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068ED30 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmesh.cpp:272 |
| 0x006997E0 | AddDoorObstacle | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:74 |
| 0x006993C0 | ClearAllObstacles | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:2571 |
| 0x00690D50 | ClearNavMesh | proven | src/fallout_shared/pathfinding/navmesh.cpp:1679 |
| 0x00697980 | ComputeTriangleZForLocation | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1651 |
| 0x006942E0 | CopyNavMeshDataTo | decomp | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:38 |
| 0x006959B0 | CreateGrid | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:4147 |
| 0x00699B60 | CreatePOVs | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:906 |
| 0x00690E90 | DeleteExtraEdgeInfo | proven | src/fallout_shared/pathfinding/navmesh.cpp:1817 |
| 0x00697010 | FindClosestOpenEdgeForLocation | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:2282 |
| 0x00696CF0 | FindClosestTriangleForLocation | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:3205 |
| 0x00697730 | FindHeightOnTriangle | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:60 |
| 0x00698160 | FindInterectingEdge2 | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:3413 |
| 0x00698320 | FindIntersectingEdgeFast | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1788 |
| 0x00697C10 | FindRandomPointWithinRadius | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:4095 |
| 0x00696A50 | FindTriangleForLocation | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:3136 |
| 0x00694620 | FinishLoadGame | proven | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:550 |
| 0x006942C0 | ForceSetFormID | decomp | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:17 |
| 0x00464FF0 | FUN_00464ff0 | probable | src/staging/blk_00460000_od.cpp:80 |
| 0x00697290 | FUN_00697290 | unnamed | src/fallout_shared/pathfinding/navmesh_util.cpp:1746 |
| 0x00699AF0 | GetClosedDoorInfo | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:26 |
| 0x0068EFD0 | GetEdge | proven | src/fallout_shared/pathfinding/navmesh.cpp:2651 |
| 0x0068F0C0 | GetEdgeVertices | proven | src/fallout_shared/pathfinding/navmesh.cpp:675 |
| 0x00693D30 | GetExtraEdgeInfo | proven | src/fallout/ai/sandboxpackage.cpp:1083 |
| 0x006D8910 | GetNeighborCount | proven | src/fallout_shared/pathfinding/pathfind.cpp:849 |
| 0x006997B0 | GetObstacleForTriangle | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1251 |
| 0x006987D0 | GetOverlappedTriangleList | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:671 |
| 0x006971E0 | GetPlaneNormal | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:6 |
| 0x0069A830 | GetPOVsForTriangle | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1852 |
| 0x0042FB00 | GetStaticAvoidNodeData | decomp | src/fallout_shared/pathfinding/navmesh.cpp:164 |
| 0x00691660 | GetStaticAvoidNodesForTriangle | decomp | src/fallout_shared/pathfinding/navmesh.cpp:171 |
| 0x005582F0 | GetTriangle | proven | src/fallout_shared/pathfinding/pathingavoidnode.cpp:5 |
| 0x00558220 | GetTriangleCenter | proven | src/fallout_shared/pathfinding/navmesh_h_unit.cpp: |
| 0x0068F0A0 | GetVertex | proven | src/fallout_shared/pathfinding/navmesh.cpp:331 |
| 0x00693E60 | InitItem | class | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:23 |
| 0x00697670 | IsPointInsideNavmesh | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1165 |
| 0x00697810 | IsPointInsideTriangle | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:1613 |
| 0x00692950 | Load | proven | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:996 |
| 0x0068EB80 | NavMesh | proven | src/fallout_shared/bgsdefaultobjectmanager.cpp:87 |
| 0x006967F0 | RemoveTrianglesFromGrid | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:3070 |
| 0x00694090 | SetAltered | proven | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:533 |
| 0x00693FE0 | SetDelete | proven | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:1759 |
| 0x006986D0 | UpdateNavMeshInfo | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:2485 |
| 0x0068ED70 | ~NavMesh | proven | src/fallout_shared/pathfinding/navmesh.cpp:1608 |

### NavMeshActionController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006940E0 | ProcessNavMeshAction | class | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:1869 |

### NavMeshAdjust (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00697D40 | AdjustPointToNavMesh | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:3329 |

### NavMeshBounds (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0069CC80 | CopyTo | decomp | src/fallout_shared/pathfinding/navmeshpovsearch.cpp:6 |
| 0x0069BCF0 | NavMeshBounds | proven | src/fallout_shared/pathfinding/navmeshinfo.cpp:667 |

### NavMeshCollection (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00464F60 | GetNavMeshAt | decomp | src/fallout_shared/pathfinding/navmesharray_h_unit.cpp: |

### NavMeshEdgePoint (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DBB40 | FUN_006dbb40 | unnamed | src/staging/blk_006c0000_od.cpp:1470 |

### NavMeshEdgeQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068F3B0 | FUN_0068f3b0 | probable | src/fallout_shared/pathfinding/navmesh.cpp:2729 |

### NavMeshGrid (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0069D2D0 | Clear | proven | src/fallout_shared/pathfinding/navmesh.cpp:2703 |
| 0x0069DD50 | CopyTo | proven | src/staging/blk_00680000_od.cpp:6223 |
| 0x00691260 | GetCellIndex | decomp | src/fallout_shared/pathfinding/navmesh.cpp:1170 |
| 0x0069D4B0 | GetTriangleDataForAABB | proven | src/staging/blk_00680000_od.cpp:3468 |

### NavMeshGridOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006965D0 | AddTrianglesToGrid | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:3019 |

### NavMeshGridView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0069D370 | GetTriListAtPosition | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:3762 |

### NavMeshGridX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006912A0 | GetCellCoords | decomp | src/fallout_shared/pathfinding/navmesh.cpp:2472 |

### NavMeshInfo (15)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B6390 | 'scalar deleting destructor' | decomp | src/fallout_shared/pathfinding/navmeshinfo.cpp:253 |
| 0x00690860 | AcquireNavMesh | decomp | src/fallout_shared/pathfinding/navmeshptr_h_unit.cpp: |
| 0x006B5AB0 | CopyTo | decomp | src/fallout_shared/pathfinding/navmeshinfo.cpp:211 |
| 0x006B48F0 | FillInfoChunk | proven | src/fallout_shared/pathfinding/navmeshinfo.cpp:475 |
| 0x006B7770 | GetCell | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:603 |
| 0x0068F320 | GetDisabled | proven | src/fallout_shared/pathfinding/navmesh.cpp:353 |
| 0x006B77B0 | GetInteriorCell | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:1643 |
| 0x00690830 | GetParentSpace | proven | src/fallout_shared/pathfinding/navmesh.cpp:379 |
| 0x00690800 | GetWorldSpace | proven | src/fallout_shared/pathfinding/navmesh.cpp:371 |
| 0x006B51A0 | LoadSerializedData | decomp | src/fallout_shared/pathfinding/navmeshinfo.cpp:141 |
| 0x006B46A0 | NavMeshInfo | decomp | src/fallout_shared/pathfinding/navmeshinfomap.cpp:143 |
| 0x006B5490 | ReleaseNavMesh | decomp | src/fallout_shared/pathfinding/navmeshinfo.cpp:120 |
| 0x0069AD00 | ResolveNavMesh | decomp | src/fallout_shared/pathfinding/navmeshinfo_h_unit.cpp: |
| 0x006B4B50 | SetFromInfoChunk | proven | src/fallout_shared/pathfinding/navmeshinfo.cpp:554 |
| 0x006B4790 | ~NavMeshInfo | proven | src/staging/blk_006a0000_od.cpp:4842 |

### NavMeshInfoMap (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B5CD0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:373 |
| 0x006B6B20 | Clear | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:1143 |
| 0x006B77E0 | FindNavMeshInfoForCell | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:579 |
| 0x006B7850 | FindNavMeshInfoForCellKey | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:448 |
| 0x006B7910 | GetAllNavMeshInfo | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:484 |
| 0x006B63C0 | InitItem | class | src/fallout_shared/pathfinding/navmeshinfomap.cpp:52 |
| 0x006B7980 | InsertNavMeshInfo | decomp | src/fallout_shared/pathfinding/navmeshinfomap.cpp:102 |
| 0x006B5C30 | NavMeshInfoMap | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:157 |
| 0x006B6910 | Sort | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:428 |
| 0x006B7CB0 | ValidateNavMeshInfoArrays | decomp | src/fallout_shared/pathfinding/navmeshinfomap.cpp:7 |
| 0x006B5D00 | ~NavMeshInfoMap | proven | src/fallout_shared/pathfinding/navmeshinfomap.cpp:552 |

### NavMeshInfoMapSaveStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B6740 | SaveNavMeshInfoMap | class | src/fallout_shared/pathfinding/navmeshinfomap.cpp:947 |

### NavMeshInfoProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068F2E0 | FUN_0068f2e0 | unnamed | src/fallout_shared/pathfinding/navmesh.cpp:1359 |

### NavMeshInfoSaveShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B4E80 | SaveToBuffer | decomp | src/fallout_shared/pathfinding/navmeshinfo.cpp:374 |

### NavMeshInfoSearch (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006B83F0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:220 |
| 0x006B8490 | CollectConnections | class | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:23 |
| 0x006B8C20 | HasReachedGoal | class | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:16 |
| 0x006B8340 | NavMeshInfoSearch | proven | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:184 |
| 0x006B8420 | ~NavMeshInfoSearch | proven | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:208 |

### NavMeshListNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007A19A0 | FUN_007a19a0 | unnamed | src/staging/blk_007a0000_od.cpp:300 |

### NavMeshObstacleCutter (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006BEC40 | CheckTriangleAgainstObstacle | proven | src/staging/blk_006a0000_od.cpp:7733 |
| 0x006BEDE0 | CheckTriangleAgainstOverlapped | proven | src/staging/blk_006a0000_od.cpp:13500 |
| 0x006BC940 | GetTrianglesMaxObstacleCount | proven | src/staging/blk_006a0000_od.cpp:2739 |
| 0x006BBB80 | NavMeshObstacleCutter | proven | src/fallout_shared/pathfinding/navmesh_util.cpp:2108 |
| 0x006BDCB0 | RemoveInvalidEdges | proven | src/staging/blk_006a0000_od.cpp:9930 |
| 0x006BC8E0 | ResetNavMeshFromObstacleUndoData | proven | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:515 |

### NavMeshObstacleManager (23)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006C5B20 | AddBoundingBox3DNode | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:5500 |
| 0x006C0C30 | AddObstacleForReference | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:1449 |
| 0x006C4F70 | AddProcessedTask | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:5 |
| 0x006C09F0 | ClearAllObstacles | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:3824 |
| 0x006C3970 | GetBackgroundTaskCount | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager_h_unit.cpp: |
| 0x006C2050 | GetNavMeshListForObstacle | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:1692 |
| 0x006C3920 | GetProcessedTaskCount | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager_h_unit.cpp: |
| 0x006C5EF0 | GetTaskForNavMesh | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:910 |
| 0x006C07D0 | Initialize | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:150 |
| 0x006C3570 | IsPointInBox | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:814 |
| 0x006C02C0 | NavMeshObstacleManager | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:7177 |
| 0x006C1060 | OnDoorRemove | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:6260 |
| 0x006C49E0 | ProcessActivatedObstacles | decomp | src/fallout_shared/pathfinding/navmeshrender.cpp:10 |
| 0x006C4AD0 | ProcessDeactivatedObstacles | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager_nogf_variant.cpp:129 |
| 0x006C4D30 | ProcessMovingReferences | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:7153 |
| 0x006C45E0 | ProcessNewReferences | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:2522 |
| 0x006C5CE0 | PushTask | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:2028 |
| 0x006C0900 | Release | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:2985 |
| 0x006C0C80 | RemoveObstacleForReference | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:7281 |
| 0x006C3640 | Update | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:6399 |
| 0x006C1760 | UpdateObstacle | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:3244 |
| 0x006C3440 | UpdateObstacleActiveStatus | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:6303 |
| 0x006C0510 | ~NavMeshObstacleManager | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:3630 |

### NavMeshOps (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00691510 | AddAvoidNode | decomp | src/fallout_shared/pathfinding/navmesh.cpp:2616 |

### NavMeshPOVSearch (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0069E1D0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshpovsearch.cpp:354 |
| 0x0069F010 | BuildPath | proven | src/staging/blk_00680000_od.cpp:6052 |
| 0x006BB570 | FindSphereTangents | decomp | src/fallout_shared/pathfinding/navmeshpovsearch.cpp:25 |
| 0x0069E110 | NavMeshPOVSearch | proven | src/fallout_shared/pathfinding/navmeshpovsearch.cpp:2627 |
| 0x0069E200 | ~NavMeshPOVSearch | proven | src/fallout_shared/pathfinding/navmeshpovsearch.cpp:2874 |

### NavMeshProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068EF70 | GetDoorForm | decomp | src/fallout_shared/pathfinding/navmesh.cpp:1335 |

### NavMeshPtr (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0042FFA0 | FUN_0042ffa0 | unnamed | src/staging/blk_00420000_od.cpp:542 |
| 0x005E05B0 | FUN_005e05b0 | unnamed | src/staging/blk_005e0000_od.cpp:108 |
| 0x0042F4C0 | operator= | decomp | src/gamebryo2.2/corelibs/nimain/nismartpointer_h_unit.cpp: |
| 0x0042FA40 | ~NavMeshPtr | proven | src/fallout_shared/extradatalist.cpp:5188 |

### NavMeshRender (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A37A0 | AddDrawOnlyNavMeshes | proven | src/fallout_shared/pathfinding/navmeshrender.cpp:827 |
| 0x006A36E0 | SetDraw | proven | src/fallout_shared/pathfinding/navmeshrender.cpp:210 |
| 0x006A5EE0 | SetTransparentOverLayMode | proven | src/staging/blk_006a0000_od.cpp:8143 |
| 0x006A5CA0 | UpdateRenderOnlyNavMeshes | proven | src/fallout_shared/pathfinding/navmeshrender.cpp:274 |
| 0x006A3580 | ~NavMeshRender | proven | src/staging/blk_006a0000_od.cpp:14227 |

### NavMeshSearch (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A6AD0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearch.cpp:733 |
| 0x006A6B70 | ComputePath | decomp | src/fallout_shared/pathfinding/navmeshsearch.cpp:7 |
| 0x006A79C0 | HasReachedGoal | class | src/fallout_shared/pathfinding/navmeshsearch.cpp:50 |
| 0x006A6A40 | NavMeshSearch | proven | src/fallout_shared/pathfinding/navmeshsearch.cpp:303 |
| 0x00698F40 | Search | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:2534 |
| 0x006A8B60 | Search | decomp | src/fallout_shared/pathfinding/navmeshsearchclosepoint.cpp:2203 |
| 0x006A6EF0 | SetSearchNodeTriangle | decomp | src/fallout_shared/pathfinding/navmeshsearch.cpp:66 |
| 0x006A6B00 | ~NavMeshSearch | proven | src/fallout_shared/pathfinding/navmeshsearch.cpp:336 |
| 0x006A7C40 | ~NavMeshSearch | decomp | src/fallout_shared/pathfinding/navmeshsearch.cpp:81 |

### NavMeshSearchClosePoint (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A8B10 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchclosepoint.cpp:33 |
| 0x006A8A80 | NavMeshSearchClosePoint | proven | src/staging/blk_006a0000_od.cpp:3302 |
| 0x006A8D20 | SetNodeFromTriangle | decomp | src/fallout_shared/pathfinding/navmeshsearchclosepoint.cpp:66 |
| 0x006A8B40 | ~NavMeshSearchClosePoint | proven | src/fallout_shared/pathfinding/navmeshsearchclosepoint.cpp:18 |

### NavMeshSearchEdges (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A6FA0 | FindEdgeConnections | class | src/fallout_shared/pathfinding/navmeshsearch.cpp:537 |

### NavMeshSearchFlee (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A9290 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchflee.cpp:15 |
| 0x006A9A70 | IsNodeValid | class | src/fallout_shared/pathfinding/navmeshsearchflee.cpp:114 |
| 0x006A9200 | NavMeshSearchFlee | proven | src/staging/blk_006a0000_od.cpp:2632 |
| 0x006A9580 | SetNodeData | proven | src/fallout_shared/pathfinding/navmeshsearchflee.cpp:193 |
| 0x006A92C0 | ~NavMeshSearchFlee | proven | src/fallout_shared/pathfinding/navmeshsearchflee.cpp:232 |

### NavMeshSearchHide (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A9D30 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchhide.cpp:15 |
| 0x006AA470 | IsGoalNode | proven | src/fallout_shared/pathfinding/navmeshsearchhide.cpp:682 |
| 0x006A9CB0 | NavMeshSearchHide | proven | src/staging/blk_006a0000_od.cpp:10761 |
| 0x006A9D60 | ~NavMeshSearchHide | proven | src/fallout_shared/pathfinding/navmeshsearchhide.cpp:721 |

### NavMeshSearchLOS (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AA6E0 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:108 |
| 0x006AB180 | IsGoalNode | proven | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:537 |
| 0x006AA620 | NavMeshSearchLOS | proven | src/staging/blk_006a0000_od.cpp:4293 |
| 0x006AAC10 | SetNodeData | proven | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:196 |
| 0x006AA710 | ~NavMeshSearchLOS | proven | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:169 |

### NavMeshSearchLOSArray (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AC010 | Clear | decomp | src/fallout_shared/pathfinding/navmeshsearchlos.cpp:6 |
| 0x0049FAF0 | FUN_0049faf0 | unnamed | src/staging/blk_00480000_od.cpp:901 |
| 0x006DBDE0 | FUN_006dbde0 | unnamed | src/fallout/ai/combat/combatstate.cpp:393 |
| 0x007D8E20 | FUN_007d8e20 | unnamed | src/fallout/interface/listbox.cpp:842 |
| 0x004A9690 | InsertAt | decomp | src/fallout_shared/bgssceneinfo.cpp:591 |

### NavMeshSearchMaxCost (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AB450 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchmaxcost.cpp:19 |
| 0x006AB4A0 | BuildNodePath | proven | src/fallout_shared/pathfinding/navmeshsearchmaxcost.cpp:306 |
| 0x006ABB60 | IsGoalNode | proven | src/fallout_shared/pathfinding/navmeshsearchmaxcost.cpp:54 |
| 0x006AB410 | NavMeshSearchMaxCost | proven | src/fallout_shared/pathfinding/navmeshsearchflee.cpp:37 |
| 0x006AB480 | ~NavMeshSearchMaxCost | proven | src/fallout_shared/pathfinding/navmeshsearchmaxcost.cpp:4758 |

### NavMeshSearchSLPoint (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006AC180 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshsearchslpoint.cpp:15 |
| 0x006AC8B0 | CheckPointOnGoalCircle | proven | src/staging/blk_006a0000_od.cpp:14035 |
| 0x006AC220 | FindStraightLinePath | proven | src/fallout_shared/pathfinding/navmeshsearchslpoint.cpp:359 |
| 0x006AC0E0 | NavMeshSearchSLPoint | proven | src/staging/blk_006a0000_od.cpp:12910 |
| 0x006AC1B0 | ~NavMeshSearchSLPoint | proven | src/fallout_shared/pathfinding/navmeshsearchslpoint.cpp:4690 |

### NavMeshStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00691350 | CollectTriangleCells | decomp | src/fallout_shared/pathfinding/navmesh.cpp:2563 |

### NavMeshTriangle (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068F1D0 | EdgeHasExtraInfo | proven | src/fallout_shared/pathfinding/navmesh.cpp:2668 |
| 0x00693C10 | Endian | proven | src/staging/blk_00680000_od.cpp:2655 |
| 0x00691040 | GetEdgeCoverData | proven | src/fallout_shared/pathfinding/navmesh.cpp:1125 |
| 0x00691140 | GetFlag | proven | src/fallout_shared/pathfinding/navmesh.cpp:2453 |
| 0x005582D0 | GetVert | proven | src/fallout_shared/tesobjectcell.cpp:2207 |
| 0x00690E10 | HasEdgeExtraInfo | proven | src/fallout_shared/pathfinding/navmesh.cpp:698 |
| 0x0068F200 | IsEdgeConnected | proven | src/fallout_shared/pathfinding/navmesh.cpp:2680 |
| 0x006AD2F0 | SetEdgeCover | proven | src/staging/blk_006a0000_od.cpp:4325 |
| 0x00691570 | SetFlag | proven | src/fallout_shared/pathfinding/navmesh.cpp:2630 |
| 0x00693BD0 | SetObjectCount | proven | src/staging/blk_00680000_od.cpp:1235 |

### NavMeshTriangleReference (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A78D0 | FUN_006a78d0 | probable | src/fallout_shared/pathfinding/pathingavoidnode.cpp:10 |

### NavMeshView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0068F6D0 | Validate | decomp | src/fallout_shared/pathfinding/navmesh.cpp:2039 |

### ObstacleData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006C2490 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:1236 |
| 0x006C23C0 | ObstacleData | proven | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:1018 |

### ObstacleTaskData (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006C7970 | 'scalar deleting destructor' | proven | src/fallout_shared/pathfinding/navmeshobstacletask.cpp:247 |
| 0x006C7A30 | AddOperation | decomp | src/fallout_shared/pathfinding/navmeshobstacletask.cpp:6 |
| 0x006C77A0 | ObstacleTaskData | proven | src/staging/blk_006c0000_od.cpp:2813 |
| 0x006C8170 | Process | class | src/fallout_shared/pathfinding/navmeshobstacletask.cpp:87 |
| 0x006C85E0 | ReplaceNavMesh | proven | src/fallout_shared/pathfinding/navmeshobstacletask.cpp:538 |
| 0x006C79A0 | ~ObstacleTaskData | proven | src/fallout_shared/pathfinding/navmeshobstacletask.cpp:175 |

### (free functions) (18)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00868790 | AddNavMeshToGarbageCollector | decomp | src/fallout/misc/garbagecollector.cpp:185 |
| 0x006F7A80 | BuildNavMeshGeometry | decomp | src/fallout_shared/distant terrain system/bgsdistanttreeblock.cpp:771 |
| 0x006BC870 | CopyFromNavMeshEdge | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:422 |
| 0x006EE5D0 | CreateNavMeshEdges | probable | src/staging/blk_006e0000_od.cpp:4049 |
| 0x0042E2C0 | EnsureNavMeshPortalExtra | probable | src/fallout_shared/extradatalist.cpp:7571 |
| 0x008694C0 | ForEachNavMesh | decomp | src/fallout/misc/garbagecollector.cpp:434 |
| 0x0042E2A0 | GetExtraNavMeshPortal | decomp | src/fallout_shared/extradatalist.cpp:4918 |
| 0x006D9830 | GetNavMeshHeight | decomp | src/fallout_shared/pathfinding/pathfind.cpp:1194 |
| 0x006C0720 | GetNavMeshObstacleManager | decomp | src/fallout_shared/pathfinding/navmeshobstaclemanager.cpp:7208 |
| 0x00692870 | InitNavMeshClosedDoorInfo | decomp | src/fallout_shared/pathfinding/navmesh.cpp:616 |
| 0x006B5D80 | LoadNavMeshInfoMap | class | src/fallout_shared/pathfinding/navmeshinfomap.cpp:255 |
| 0x00464FC0 | MakeNavMeshPointer | probable | src/fallout_shared/pathfinding/navmesh_util.cpp:19 |
| 0x006BE6F0 | MarkNavMeshTriangles | probable | src/fallout_shared/pathfinding/navmesh_util.cpp:1932 |
| 0x00693F30 | PrintNavMeshInfo | class | src/fallout_shared/pathfinding/navmesh_loadsave.cpp:1658 |
| 0x006953B0 | RemoveNavMeshId | decomp | src/fallout_shared/pathfinding/navmesh_util.cpp:2939 |
| 0x006B68B0 | SetAlteredAndRevertNavMeshes | class | src/fallout_shared/pathfinding/navmeshinfomap.cpp:400 |
| 0x007A1450 | SetNavMeshInfo | decomp | src/staging/blk_007a0000_od.cpp:199 |
| 0x006B8C50 | SetupNavMeshSearch | probable | src/fallout_shared/pathfinding/navmeshinfosearch.cpp:326 |

## 7 Combat

CombatController, combat groups, goals, actions and procedures.

### ActorCombatGroup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009891A0 | GetByteAtOffset100 | decomp | src/fallout/ai/combat/combatgroup.cpp:183 |

### CombatAction (14)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097BC60 | AddPossibleEffect | proven | src/fallout/ai/combat/combatactions.cpp:34 |
| 0x00979E90 | CanExecute | proven | src/fallout/ai/combat/combataction.cpp:178 |
| 0x00979BD0 | CombatAction | proven | src/fallout/ai/combat/combataction.cpp:355 |
| 0x00979F90 | CreateAction | decomp | src/fallout/ai/combat/combataction.cpp:7 |
| 0x0097ADC0 | FUN_0097adc0 | unnamed | src/fallout/ai/combat/combatactions.cpp:22 |
| 0x0097ADE0 | FUN_0097ade0 | unnamed | src/fallout/ai/combat/combatactions.cpp:28 |
| 0x00979E60 | GetDebugText | proven | src/fallout/ai/combat/combataction.cpp:135 |
| 0x00994250 | GetFlag | proven | src/staging/blk_00980000_od.cpp:2748 |
| 0x0097ACB0 | GetMovementCost | proven | src/fallout/ai/combat/combataction.cpp:320 |
| 0x00979E20 | GetName | proven | src/fallout/ai/combat/combataction.cpp:90 |
| 0x0097C240 | RemoveEffect | proven | src/fallout/ai/combat/combatactions.cpp:44 |
| 0x0097C260 | RemoveExecutionCondition | proven | src/fallout/ai/combat/combatactions.cpp:49 |
| 0x0097C070 | RemovePrecondition | proven | src/fallout/ai/combat/combatactions.cpp:39 |
| 0x00979C80 | ~CombatAction | proven | src/staging/blk_00960000_od.cpp:2272 |

### CombatActionAcquireLineOfSight (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097D1C0 | CombatActionAcquireLineOfSight | proven | src/fallout/ai/combat/combatactions.cpp:291 |

### CombatActionActivateCombatItem (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CE90 | CombatActionActivateCombatItem | proven | src/fallout/ai/combat/combatactions.cpp:343 |
| 0x0097CF10 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1426 |

### CombatActionApproachTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097D130 | CombatActionApproachTarget | proven | src/fallout/ai/combat/combatactions.cpp:278 |

### CombatActionAttackGrenade (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B620 | CombatActionAttackGrenade | proven | src/fallout/ai/combat/combatactions.cpp:123 |
| 0x0097B6D0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:974 |

### CombatActionAttackGrenadeFlushTarget (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B840 | CanExecute | proven | src/fallout/ai/combat/combatactions.cpp:473 |
| 0x0097B7A0 | CombatActionAttackGrenadeFlushTarget | proven | src/fallout/ai/combat/combatactions.cpp:133 |
| 0x0097B880 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1020 |

### CombatActionAttackGrenadeFromCover (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B9E0 | CombatActionAttackGrenadeFromCover | proven | src/fallout/ai/combat/combatactions.cpp:142 |
| 0x0097BAB0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1065 |

### CombatActionAttackHandToHand (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B4E0 | CombatActionAttackHandToHand | proven | src/fallout/ai/combat/combatactions.cpp:112 |

### CombatActionAttackMelee (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B350 | CombatActionAttackMelee | proven | src/fallout/ai/combat/combatactions.cpp:101 |
| 0x0097B4A0 | GetCost | proven | src/fallout/ai/combat/combatactions.cpp:419 |

### CombatActionAttackRanged (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097AD10 | CombatActionAttackRanged | proven | src/fallout/ai/combat/combatactions.cpp:54 |

### CombatActionAttackRangedExplosive (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B0B0 | CombatActionAttackRangedExplosive | proven | src/fallout/ai/combat/combatactions.cpp:76 |
| 0x0097AB30 | Execute | decomp | src/fallout/ai/combat/combatactions.cpp:12 |

### CombatActionAttackRangedExplosiveFromCover (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B280 | CombatActionAttackRangedExplosiveFromCover | proven | src/fallout/ai/combat/combatactions.cpp:87 |

### CombatActionAttackRangedFromCover (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097AEB0 | CombatActionAttackRangedFromCover | proven | src/fallout/ai/combat/combatactions.cpp:64 |

### CombatActionAvoidThreat (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C9D0 | CombatActionAvoidThreat | proven | src/fallout/ai/combat/combatactions.cpp:230 |

### CombatActionDodge (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CC00 | CombatActionDodge | proven | src/fallout/ai/combat/combatactions.cpp:251 |

### CombatActionDrawWeapon (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C700 | CombatActionDrawWeapon | proven | src/fallout/ai/combat/combatactions.cpp:215 |

### CombatActionFlee (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CD30 | CombatActionFlee | proven | src/fallout/ai/combat/combatactions.cpp:331 |
| 0x0097CDB0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1379 |

### CombatActionHide (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097D250 | CombatActionHide | proven | src/fallout/ai/combat/combatactions.cpp:305 |
| 0x0097D2D0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1509 |
| 0x0097D370 | GetDebugText | proven | src/fallout/ai/combat/combatactions.cpp:774 |

### CombatActionIgnoreBlockedTarget (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CC80 | CombatActionIgnoreBlockedTarget | proven | src/fallout/ai/combat/combatactions.cpp:6 |
| 0x0097CCF0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:732 |

### CombatActionInvestigate (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CB70 | CombatActionInvestigate | proven | src/fallout/ai/combat/combatactions.cpp:244 |

### CombatActionMove (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097BEB0 | ChooseLocation | proven | src/fallout/ai/combat/combatstate.cpp:445 |
| 0x0097BBD0 | CombatActionMove | proven | src/fallout/ai/combat/combatactions.cpp:155 |
| 0x0097BCA0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:566 |
| 0x0097BED0 | StartMovementProcedure | proven | src/fallout/ai/combat/combatactions.cpp:1561 |

### CombatActionMoveAndAttackGrenade (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C560 | CombatActionMoveAndAttackGrenade | proven | src/fallout/ai/combat/combatactions.cpp:201 |
| 0x0097C620 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1222 |

### CombatActionMoveAndAttackRanged (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C170 | CombatActionMoveAndAttackRanged | proven | src/fallout/ai/combat/combatactions.cpp:171 |

### CombatActionMoveAndAttackRangedExplosive (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C3A0 | CombatActionMoveAndAttackRangedExplosive | proven | src/fallout/ai/combat/combatactions.cpp:186 |

### CombatActionMoveAndSwitchToMelee (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097BFE0 | CombatActionMoveAndSwitchToMelee | proven | src/fallout/ai/combat/combatactions.cpp:163 |
| 0x0097C090 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1114 |

### CombatActionMoveStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097BC80 | FUN_0097bc80 | rejected | src/fallout/ai/combat/combatactions.cpp:551 |

### CombatActionSearch (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CA60 | CombatActionSearch | proven | src/fallout/ai/combat/combatactions.cpp:237 |
| 0x0097CAF0 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:794 |

### CombatActionStandIn (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097BD00 | FUN_0097bd00 | unnamed | src/fallout/ai/combat/combatactions.cpp:600 |
| 0x0097C470 | FUN_0097c470 | unnamed | src/fallout/ai/combat/combatactions.cpp:626 |
| 0x0097CD10 | FUN_0097cd10 | unnamed | src/fallout/ai/combat/combatactions.cpp:745 |
| 0x0097CFC0 | GetActionAtIndex | decomp | src/fallout/ai/combat/combatactions.cpp:758 |

### CombatActionSwitchWeapon (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C850 | CombatActionSwitchWeapon | proven | src/fallout/ai/combat/combatactions.cpp:223 |
| 0x0097C8E0 | GetCost | proven | src/fallout/ai/combat/combatactions.cpp:1320 |

### CombatActionUseCombatItem (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097CFE0 | CombatActionUseCombatItem | proven | src/fallout/ai/combat/combatactions.cpp:355 |
| 0x0097D060 | Execute | proven | src/fallout/ai/combat/combatactions.cpp:1470 |

### CombatBox (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009926C0 | FUN_009926c0 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1244 |
| 0x00992700 | FUN_00992700 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1269 |
| 0x009926E0 | SwapAndDispatch | decomp | src/fallout/ai/combat/combatmanager.cpp:1256 |

### CombatClock (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985B40 | GetAdjustedTime | decomp | src/fallout/ai/combat/combatgroup.cpp:3097 |

### CombatController (40)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097D740 | 'scalar deleting destructor' | proven | src/fallout/ai/combatcontroller.cpp:382 |
| 0x0097F930 | AddTarget | proven | src/fallout/ai/combatcontroller.cpp:2160 |
| 0x009819F0 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/combatcontroller.cpp:1444 |
| 0x0097D9D0 | CalculateAttackerInfo | proven | src/fallout/ai/combatcontroller.cpp:3434 |
| 0x00980250 | ClearProcedures | proven | src/fallout/ai/combatcontroller.cpp:328 |
| 0x00980A30 | ClearReferencePointers | proven | src/fallout/ai/combatcontroller.cpp:2601 |
| 0x0097D3A0 | CombatController | proven | src/fallout/ai/combat/combatmanager.cpp:3550 |
| 0x00981940 | CombatPlanContainsAction | proven | src/fallout/ai/combat/combatplan.cpp:17 |
| 0x0097FB80 | DebugCombatPlan | proven | src/fallout/ai/combatcontroller.cpp:2200 |
| 0x00982310 | FinishLoadGame | proven | src/fallout/ai/combatcontroller.cpp:658 |
| 0x0097D990 | FirstUpdate | proven | src/fallout/ai/combatcontroller.cpp:423 |
| 0x0097F200 | ForcePlanUpdate | proven | src/staging/blk_00960000_od.cpp:471 |
| 0x005C1AE0 | ForceStopCombat | proven | src/staging/blk_005c0000_od.cpp:13 |
| 0x00967DA0 | FUN_00967da0 | probable | src/staging/blk_00960000_od.cpp:7799 |
| 0x00980270 | FUN_00980270 | unnamed | src/fallout/ai/combatcontroller.cpp:2509 |
| 0x00981380 | FUN_00981380 | probable | src/fallout/ai/combatcontroller.cpp:2714 |
| 0x00981450 | FUN_00981450 | unnamed | src/fallout/ai/combatcontroller.cpp:2911 |
| 0x00981690 | FUN_00981690 | unnamed | src/fallout/ai/combatcontroller.cpp:1270 |
| 0x00981720 | FUN_00981720 | unnamed | src/fallout/ai/combatcontroller.cpp:368 |
| 0x00998A30 | GetAttackerCanSneak | proven | src/fallout/ai/combat/combatstate.cpp:702 |
| 0x0097FC70 | GetAttackSkill | proven | src/fallout/ai/combatcontroller_iso_variant.cpp:176 |
| 0x00980070 | GetCurrentCombatStyle | proven | src/fallout/ai/combat/combatprocedure.cpp:66 |
| 0x00981900 | GetModifierKey | decomp | src/fallout/ai/combatcontroller.cpp:628 |
| 0x0097FEB0 | GetPowerAttackHitTime | proven | src/fallout/ai/combatcontroller.cpp:2374 |
| 0x00980470 | GetProcedureFailed | proven | src/fallout/ai/combatcontroller.cpp:1183 |
| 0x00982080 | InitLoadGame | proven | src/fallout/ai/combatcontroller.cpp:6907 |
| 0x0097FA10 | IsActoraCombatTarget | proven | src/fallout/misc/taskqueueinterface.cpp:1905 |
| 0x00981D00 | LoadGame | proven | src/fallout/ai/combatcontroller.cpp:6617 |
| 0x009823C0 | LoadProcedure | proven | src/fallout/ai/combatcontroller.cpp:3229 |
| 0x0097F9C0 | RemoveTarget | proven | src/fallout/ai/combatcontroller.cpp:1147 |
| 0x00981660 | ResetCombatState | decomp | src/fallout/ai/combatcontroller.cpp:1251 |
| 0x00980110 | SetActionProcedure | proven | src/fallout/ai/combatcontroller.cpp:2416 |
| 0x009815F0 | SetActualMoveMode | proven | src/fallout/ai/actor.cpp:96106 |
| 0x009801B0 | SetMovementProcedure | proven | src/fallout/ai/combatcontroller.cpp:2454 |
| 0x00981570 | SetMoveMode | proven | src/fallout/ai/combatcontroller.cpp:2969 |
| 0x00980830 | SetTarget | proven | src/fallout/ai/combatcontroller.cpp:6128 |
| 0x009807D0 | StopActorMoving | decomp | src/fallout/ai/combatcontroller.cpp:567 |
| 0x0097F4D0 | StopCombat | proven | src/fallout/ai/combatcontroller.cpp:1789 |
| 0x0097F390 | UpdateCurrentWeapon | proven | src/fallout/ai/combatcontroller.cpp:980 |
| 0x0097D770 | ~CombatController | proven | src/fallout/ai/combatcontroller.cpp:3366 |

### CombatControllerStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F470 | ValidateCurrentWeapon | decomp | src/fallout/ai/combatcontroller.cpp:1042 |

### CombatCoverLocation (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006D3150 | CombatCoverLocation | proven | src/fallout/ai/combat/combatstate.cpp:11377 |
| 0x009A2EA0 | LoadGame | proven | src/fallout/ai/combat/combatstate.cpp:3470 |
| 0x009A2DE0 | SaveGame | proven | src/fallout/ai/combat/combatstate.cpp:3421 |

### CombatCoverMap (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00983100 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatcovermap.cpp:13 |
| 0x009835D0 | CanReserveCoverLocation | proven | src/fallout/ai/combat/combatcovermap.cpp:586 |
| 0x00983080 | CombatCoverMap | proven | src/staging/blk_00980000_od.cpp:3629 |
| 0x0099C210 | LockForWrite | proven | src/fallout/ai/combat/combatstate.cpp:251 |
| 0x00995890 | UnlockForWrite | proven | src/staging/blk_00980000_od.cpp:621 |
| 0x00983520 | UnreserveCoverLocation | proven | src/fallout/ai/combat/combatcovermap.cpp:622 |
| 0x00983130 | ~CombatCoverMap | proven | src/fallout/ai/combat/combatcovermap.cpp:538 |

### CombatCoverSearchInfo (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009975C0 | Clear | proven | src/fallout/ai/combat/combatstate.cpp:572 |
| 0x00997520 | Copy | proven | src/fallout/ai/combat/combatstate.cpp:2132 |
| 0x009A3050 | LoadGame | proven | src/fallout/ai/combat/combatstate.cpp:1700 |
| 0x009A2F50 | SaveGame | proven | src/fallout/ai/combat/combatstate.cpp:1652 |
| 0x006E4D00 | ~CombatCoverSearchInfo | proven | src/fallout_shared/pathfinding/pathingrequestcoveredmove.cpp:38 |

### CombatDamageCalculator (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00646360 | CalculateArmorDamageThreshold | probable | src/fallout_shared/combatformulas.cpp:437 |
| 0x00645380 | CalculateWeaponDamage | probable | src/fallout_shared/combatformulas.cpp:38 |

### CombatDecompClass (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099E060 | InitSubObject | decomp | src/fallout/ai/combat/combatstate.cpp:8292 |

### CombatDialogueHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00983970 | FUN_00983970 | probable | src/fallout/ai/combat/combatdialoguemanager.cpp:23 |

### CombatEntryOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A41E0 | RemoveEntry | decomp | src/staging/blk_009a0000_od.cpp:2442 |

### CombatFlagHolder (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009928A0 | FUN_009928a0 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1281 |
| 0x009A1240 | FUN_009a1240 | unnamed | src/staging/blk_009a0000_od.cpp:52 |
| 0x009928C0 | HasCombatFlag | decomp | src/fallout/ai/combat/combatmanager.cpp:1292 |
| 0x009928E0 | HasCombatFlag40 | decomp | src/fallout/ai/combat/combatmanager.cpp:1305 |
| 0x00992900 | HasCombatFlag80 | decomp | src/fallout/ai/combat/combatmanager.cpp:1318 |

### CombatFormulas (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00646310 | CalcHandToHandDamage | proven | src/fallout_shared/combatformulas.cpp:714 |
| 0x006450F0 | CalcWeaponDamageForDisplay | proven | src/fallout_shared/combatformulas.cpp:1543 |
| 0x00646400 | CheckKnockdown | proven | src/staging/blk_00640000_od.cpp:3621 |
| 0x00646880 | GetArmCondition | proven | src/fallout_shared/combatformulas.cpp:896 |
| 0x00646800 | GetBodyPartCondition | proven | src/fallout_shared/combatformulas.cpp:395 |
| 0x00646580 | GetKnockbackSpeed | proven | src/fallout_shared/combatformulas.cpp:926 |
| 0x006465F0 | GetRandomBetween | proven | src/fallout_shared/combatformulas.cpp:416 |
| 0x00646F70 | GetVATSChanceToHit | proven | src/fallout_shared/combatformulas.cpp:1948 |
| 0x00645DC0 | GetWeaponShotsPerSecond | proven | src/fallout_shared/combatformulas.cpp:836 |
| 0x00647870 | GetWeaponSkillRequirementModifier | proven | src/fallout_shared/combatformulas.cpp:1719 |
| 0x00647810 | GetWeaponStrengthRequirementModifier | proven | src/fallout_shared/combatformulas.cpp:730 |

### CombatGoal (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984BA0 | CombatGoal | proven | src/fallout/ai/combat/combatgoal.cpp:505 |
| 0x00984490 | CreateGoal | decomp | src/fallout/ai/combat/combatgoal.cpp:7 |
| 0x009843B0 | FUN_009843b0 | class | src/fallout/ai/combat/combatgoal_decl_variant.cpp:23 |
| 0x00984290 | ~CombatGoal | proven | src/staging/blk_00980000_od.cpp:6161 |

### CombatGoalActivateCombatItem (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984DD0 | CombatGoalActivateCombatItem | proven | src/fallout/ai/combat/combatgoal.cpp:527 |

### CombatGoalAdvance (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985100 | CombatGoalAdvance | proven | src/fallout/ai/combat/combatgoal.cpp:400 |

### CombatGoalAmbush (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985000 | CombatGoalAmbush | proven | src/fallout/ai/combat/combatgoal.cpp:262 |

### CombatGoalAvoidThreats (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984CB0 | CombatGoalAvoidThreats | proven | src/fallout/ai/combat/combatgoal.cpp:339 |

### CombatGoalCluster (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985200 | CombatGoalCluster | proven | src/fallout/ai/combat/combatgoal.cpp:196 |

### CombatGoalFallBack (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984F80 | CombatGoalFallBack | proven | src/fallout/ai/combat/combatgoal.cpp:127 |

### CombatGoalFindTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984C20 | CombatGoalFindTarget | proven | src/fallout/ai/combat/combatgoal.cpp:312 |

### CombatGoalFlank (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984EE0 | CombatGoalFlank | proven | src/fallout/ai/combat/combatgoal.cpp:104 |

### CombatGoalFlee (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984D40 | CombatGoalFlee | proven | src/fallout/ai/combat/combatgoal.cpp:366 |

### CombatGoalFlushTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985300 | CombatGoalFlushTarget | proven | src/fallout/ai/combat/combatgoal.cpp:287 |

### CombatGoalGuard (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985180 | CombatGoalGuard | proven | src/fallout/ai/combat/combatgoal.cpp:174 |

### CombatGoalHideFromTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985280 | CombatGoalHideFromTarget | proven | src/fallout/ai/combat/combatgoal.cpp:218 |

### CombatGoalKillTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984B20 | CombatGoalKillTarget | proven | src/fallout/ai/combat/combatgoal.cpp:64 |

### CombatGoalReachDestination (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985080 | CombatGoalReachDestination | proven | src/fallout/ai/combat/combatgoal.cpp:151 |

### CombatGoalStayInCombatArea (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985390 | CombatGoalStayInCombatArea | proven | src/fallout/ai/combat/combatgoal.cpp:240 |

### CombatGoalUseCombatItem (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984E60 | CombatGoalUseCombatItem | proven | src/fallout/ai/combat/combatgoal.cpp:83 |

### CombatGroup (33)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009867D0 | AddMember | proven | src/fallout/ai/combat/combatgroup.cpp:1828 |
| 0x0098BFB0 | AddSearchLocation | proven | src/staging/blk_00980000_od.cpp:2160 |
| 0x00986410 | AddTarget | proven | src/fallout/ai/combat/combatgroup.cpp:10822 |
| 0x009866D0 | CanAddTarget | proven | src/fallout/ai/combat/combatgroup.cpp:496 |
| 0x00987220 | CheckRemoveCombatTarget | proven | src/fallout/ai/combat/combatgroup.cpp:1592 |
| 0x00987820 | ClearReferencePointers | proven | src/fallout/ai/combat/combatgroup.cpp:3450 |
| 0x00985D10 | CombatGroup | proven | src/fallout/ai/combat/combatgroup.cpp:11029 |
| 0x00989E20 | ComputeMemberBoundingSphere | proven | src/fallout/ai/combat/combatgroup.cpp:3970 |
| 0x00989EB0 | ComputeTargetBoundingSphere | proven | src/fallout/ai/combat/combatgroup.cpp:2386 |
| 0x00986740 | CopyTargets | proven | src/fallout/ai/combat/combatgroup.cpp:3129 |
| 0x009892A0 | CreateMovementAvoidNodeArray | proven | src/fallout/ai/combat/combatgroup.cpp:8346 |
| 0x00989970 | FindClosestMemberToActor | proven | src/fallout/ai/combat/combatgroup.cpp:769 |
| 0x00989880 | FindMemberNearActor | proven | src/fallout/ai/combat/combatgroup.cpp:3701 |
| 0x009897F0 | FindMemberNearLocation | proven | src/fallout/ai/combat/combatgroup.cpp:3660 |
| 0x009862E0 | ForceCombatGroupStrategy | proven | src/fallout/ai/combat/combatgroup.cpp:10893 |
| 0x00988790 | GetCombatMember | proven | src/fallout/ai/combat/combatgroup.cpp:165 |
| 0x009865F0 | GetCombatMemberForActor | proven | src/fallout/ai/combat/combatgroup_iso_variant.cpp:8153 |
| 0x0098C590 | GetCombatSearchDoor | proven | src/staging/blk_00980000_od.cpp:1025 |
| 0x009865D0 | GetCombatTargetForActor | proven | src/fallout/ai/combat/combatgroup.cpp:11076 |
| 0x00986610 | GetCombatTargetForNumericID | proven | src/fallout/ai/combat/combatgroup.cpp:1956 |
| 0x0098A310 | GetMemberGroupStrategyAssignment | proven | src/fallout/ai/combat/combatgroup.cpp:206 |
| 0x00988770 | GetSearchLocation | proven | src/fallout/ai/combat/combatgroup.cpp:147 |
| 0x00988750 | GetSearchLocationCount | proven | src/fallout/ai/combat/combatgroup.cpp:130 |
| 0x009874B0 | IncrementAttackerCount | proven | src/fallout/ai/combat/combatgroup.cpp:581 |
| 0x00986A80 | IsMember | proven | src/fallout/ai/combat/combatgroup.cpp:535 |
| 0x009865B0 | IsTarget | proven | src/fallout/ai/combat/combatgroup.cpp:472 |
| 0x0098E3D0 | LoadGame | proven | src/fallout/ai/combat/combatgroup.cpp:9579 |
| 0x009869A0 | RemoveMember | proven | src/fallout/ai/combat/combatgroup.cpp:2321 |
| 0x00986500 | RemoveTarget | proven | src/fallout/ai/combat/combatgroup.cpp:1929 |
| 0x00986560 | RemoveTarget | proven | src/fallout/ai/combat/combatgroup.cpp:868 |
| 0x00986150 | Update | proven | src/fallout/ai/combat/combatgroup.cpp:2863 |
| 0x0098D1A0 | UpdateGroupStrategy | proven | src/staging/blk_00980000_od.cpp:4185 |
| 0x00985F90 | ~CombatGroup | proven | src/fallout/ai/combat/combatgroup.cpp:6104 |

### CombatGroupCluster (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985B10 | LoadGame | proven | src/fallout/ai/combat/combatgroup.cpp:378 |
| 0x00985AE0 | SaveGame | proven | src/fallout/ai/combat/combatgroup.cpp:367 |

### CombatGroupData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990320 | CombatGroupData | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:698 |
| 0x009904C0 | GetMembersTargetsIntersecting | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:146 |
| 0x00990AA0 | GetRangedMember | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:69 |
| 0x009863B0 | ~CombatGroupData | proven | src/fallout/ai/combat/combatgroup.cpp:463 |

### CombatGroupStrategy (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098FFB0 | CombatGroupStrategy | proven | src/staging/blk_00980000_od.cpp:419 |
| 0x0098E980 | GetCombatGroupStrategy | proven | src/fallout/ai/combat/combatgroup.cpp:800 |
| 0x00990250 | GetCombatGroupStrategyByName | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:291 |

### CombatGroupStrategyAdvance (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990040 | CombatGroupStrategyAdvance | proven | src/staging/blk_00980000_od.cpp:2494 |
| 0x00990E70 | Execute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:248 |
| 0x00990EC0 | FUN_00990ec0 | class | src/fallout/ai/combat/combatgroupstrategy.cpp:270 |

### CombatGroupStrategyAmbush (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990C40 | CanExecute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:813 |
| 0x00990010 | CombatGroupStrategyAmbush | proven | src/staging/blk_00980000_od.cpp:452 |
| 0x00990CB0 | Execute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:218 |
| 0x00990D30 | FUN_00990d30 | class | src/fallout/ai/combat/combatgroupstrategy.cpp:113 |

### CombatGroupStrategyFallBack (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990B70 | CanExecute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:184 |
| 0x0098FFE0 | CombatGroupStrategyFallBack | proven | src/staging/blk_00980000_od.cpp:434 |
| 0x00990BD0 | Execute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:91 |

### CombatGroupStrategyFlank (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009908B0 | CanFlank | class | src/fallout/ai/combat/combatgroupstrategy.cpp:727 |
| 0x0098FF80 | CombatGroupStrategyFlank | proven | src/staging/blk_00980000_od.cpp:401 |
| 0x00990930 | Execute | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:341 |
| 0x00990AC0 | Update | proven | src/fallout/ai/combat/combatgroupstrategy.cpp:772 |

### CombatGroupStub (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009890E0 | GetDetectedTargetLocation | decomp | src/fallout/ai/combat/combatgroup.cpp:703 |
| 0x0098DC40 | RecenterClusters | decomp | src/staging/blk_00980000_od.cpp:4756 |

### CombatLocation (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097EE20 | CombatLocation | proven | src/fallout/ai/combat/combatstate.cpp:1733 |
| 0x0097BE60 | GetFlag | proven | src/fallout/ai/combat/combatactions.cpp:1601 |
| 0x0099B8B0 | SetPoint | proven | src/fallout/ai/combat/combatstate.cpp:1017 |
| 0x00997400 | SetRef | proven | src/fallout/ai/combat/combatstate.cpp:521 |
| 0x0097EE60 | SetWorldLocation | proven | src/fallout/ai/combat/combatstate.cpp:462 |

### CombatLocationTarget (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A08D0 | CombatLocationTarget | proven | src/fallout/ai/combat/combatstate.cpp:1115 |
| 0x009A3220 | InitLoadGame | proven | src/fallout/ai/combat/combatstate.cpp:4700 |
| 0x009A31B0 | LoadGame | proven | src/fallout/ai/combat/combatstate.cpp:1490 |
| 0x009A3130 | SaveGame | proven | src/fallout/ai/combat/combatstate.cpp:1463 |

### CombatLogic (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A1280 | FUN_009a1280 | probable | src/fallout/ai/combat/combatgroup.cpp:10011 |

### CombatLOS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884FC0 | FUN_00884fc0 | unnamed | src/fallout/ai/actor.cpp:32954 |

### CombatManager (20)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00992110 | AddCombatant | proven | src/fallout/ai/combat/combatmanager.cpp:2947 |
| 0x009922B0 | AddGroupMember | proven | src/fallout/ai/combat/combatmanager.cpp:1594 |
| 0x009929E0 | AddLocalActor | proven | src/fallout/ai/combat/combatmanager.cpp:1339 |
| 0x00992480 | AddSpectatorForCombatGroup | proven | src/fallout/ai/combat/combatmanager.cpp:3772 |
| 0x00993790 | ApplyLoadBuffer | decomp | src/fallout/ai/combat/combatmanager.cpp:6 |
| 0x00992920 | ClearReferencePointers | proven | src/fallout/ai/combat/combatmanager.cpp:1759 |
| 0x00990F20 | Create | proven | src/fallout/ai/combat/combatmanager.cpp:37 |
| 0x00991E80 | CreateCombatGroup | proven | src/fallout/ai/combat/combatmanager.cpp:1561 |
| 0x00990FF0 | Destroy | proven | src/staging/blk_00980000_od.cpp:1853 |
| 0x009931C0 | GetCombatantCount | proven | src/fallout/ai/combat/combatmanager.cpp:2217 |
| 0x00992530 | GetWanttoHelpGroup | proven | src/fallout/ai/combat/combatmanager.cpp:1207 |
| 0x00993600 | InitLoadGame | proven | src/fallout_shared/tesworldspace_rtti_variant.cpp:120 |
| 0x00993440 | LoadGame | proven | src/fallout/ai/combat/combatmanager.cpp:2346 |
| 0x009932D0 | SaveGame | proven | src/fallout/ai/combat/combatmanager.cpp:2431 |
| 0x00992D90 | ShouldPlayCombatMusic | proven | src/fallout/ai/combat/combatmanager.cpp:1027 |
| 0x00991F80 | SplitPlayerCombatGroup | proven | src/fallout/ai/combat/combatmanager.cpp:2883 |
| 0x00992A50 | TargetLocalActor | proven | src/fallout/ai/combat/combatmanager.cpp:1378 |
| 0x00991500 | Update | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:491 |
| 0x00991770 | UpdateDebugGeometry | proven | src/fallout/ai/combat/combatmanager.cpp:526 |
| 0x00991600 | UpdateMainThread | proven | src/fallout/ai/combat/combatmanager.cpp:1860 |

### CombatMapOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00992A30 | FUN_00992a30 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1355 |

### CombatMapRef (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009950A0 | FUN_009950a0 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1521 |

### CombatMember (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985A50 | LoadGame | proven | src/fallout/ai/combat/combatgroup.cpp:341 |
| 0x009859C0 | SaveGame | proven | src/fallout/ai/combat/combatgroup.cpp:1644 |

### CombatMove (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097E4B0 | FUN_0097e4b0 | probable | src/staging/blk_00960000_od.cpp:9303 |

### CombatMovementRestrictions (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CDDE0 | CanMove | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:225 |

### CombatNodeArray (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00991D60 | FindByKey | decomp | src/fallout/ai/combat/combatmanager.cpp:1178 |

### CombatNodeFinder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098C3D0 | FindNearestCombatNode | decomp | src/fallout/ai/combat/combatstate.cpp:5214 |

### CombatObj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009931A0 | FUN_009931a0 | unnamed | src/fallout/ai/combat/combatmanager.cpp:1431 |

### CombatPlan (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00993FD0 | AllocateSteps | proven | src/staging/blk_00980000_od.cpp:2691 |
| 0x00994270 | GetIndexForStep | proven | src/staging/blk_00980000_od.cpp:1311 |
| 0x009949A0 | LoadGame | proven | src/fallout/ai/combat/combatplan.cpp:54 |
| 0x009948F0 | SaveGame | proven | src/fallout/ai/combatcontroller.cpp:3025 |
| 0x00993F70 | ~CombatPlan | proven | src/staging/blk_00980000_od.cpp:1289 |

### CombatPlanner (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097E460 | 'scalar deleting destructor' | proven | src/fallout/ai/combatcontroller.cpp:445 |
| 0x0097E330 | CombatPlanner | proven | src/fallout/ai/combatcontroller.cpp:6724 |
| 0x00994BD0 | CreatePlan | proven | src/fallout/ai/combatcontroller.cpp:9130 |
| 0x00995800 | FUN_00995800 | class | src/fallout/ai/combat/combatplanner.cpp:21 |
| 0x0097E3E0 | ~CombatPlanner | proven | src/fallout/ai/combatcontroller.cpp:6758 |

### CombatPlannerData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009958B0 | CombatPlannerData | proven | src/staging/blk_00980000_od.cpp:1376 |
| 0x00995910 | ~CombatPlannerData | proven | src/staging/blk_00980000_od.cpp:5586 |

### CombatPlanNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00994E60 | CombatPlanNode | proven | src/staging/blk_00980000_od.cpp:1341 |

### CombatPosition (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099D480 | FindCombatPosition | decomp | src/staging/blk_00980000_od.cpp:8805 |

### CombatProcedure (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA6E0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedure.cpp:28 |
| 0x00996EA0 | ClearLookAtTarget | proven | src/fallout/ai/combat/combatprocedure.cpp:125 |
| 0x00996E40 | ClearMoveMode | proven | src/fallout/ai/combat/combatprocedure.cpp:220 |
| 0x009CA680 | CombatProcedure | proven | src/staging/blk_009c0000_od.cpp:2777 |
| 0x009CA6C0 | CombatProcedure | proven | src/staging/blk_009c0000_od.cpp:64 |
| 0x00996DE0 | GetAttacker | proven | src/fallout/ai/actor.cpp:34804 |
| 0x00996E00 | GetTarget | proven | src/fallout/ai/combat/combatprocedure.cpp:181 |
| 0x006ECD40 | Initialize | class | src/fallout/ai/combat/combatprocedureactivateobject.cpp:6 |
| 0x00996EF0 | LoadGame | proven | src/fallout/ai/combat/combatprocedure.cpp:142 |
| 0x009CAAC0 | SetFailed | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:419 |
| 0x00996E20 | SetMoveMode | proven | src/fallout/ai/combat/combatprocedure.cpp:200 |

### CombatProcedureActivateObject (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA710 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:63 |
| 0x009CAB00 | ClearReferencePointers | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:459 |
| 0x009CA5F0 | CombatProcedureActivateObject | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:46 |
| 0x009CAB30 | DisplayDebugText | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:629 |
| 0x006E4BA0 | FUN_006e4ba0 | unnamed | src/fallout/ai/combat/combatprocedureactivateobject.cpp:17 |
| 0x009CAD70 | InitLoadGame | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:698 |
| 0x009CAD00 | LoadGame | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:749 |
| 0x009CACB0 | SaveGame | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:672 |
| 0x009CA760 | Update | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:311 |
| 0x009CA740 | ~CombatProcedureActivateObject | proven | src/fallout/ai/combat/combatprocedureactivateobject.cpp:84 |

### CombatProcedureAttackGrenade (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CAEB0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:42 |
| 0x009CB380 | CheckExplosion | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:432 |
| 0x009CADF0 | CombatProcedureAttackGrenade | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:290 |
| 0x009CAEE0 | CombatProcedureAttackGrenade | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:354 |
| 0x009CB460 | GetTargetedPoint | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:695 |
| 0x009CBA50 | LoadGame | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:199 |
| 0x009CB9C0 | SaveGame | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:119 |
| 0x009CAFC0 | Shutdown | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:16 |
| 0x009CAFA0 | ~CombatProcedureAttackGrenade | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:60 |

### CombatProcedureAttackLow (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CBB20 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureattacklow.cpp:72 |
| 0x009CBAD0 | CombatProcedureAttackLow | proven | src/staging/blk_009c0000_od.cpp:574 |
| 0x009CC040 | LoadGame | proven | src/fallout/ai/combat/combatprocedureattacklow.cpp:167 |
| 0x009CBFD0 | SaveGame | proven | src/fallout/ai/combat/combatprocedureattacklow.cpp:34 |
| 0x009CBB70 | Update | proven | src/fallout/ai/combat/combatprocedureattacklow.cpp:369 |
| 0x009CBB50 | ~CombatProcedureAttackLow | proven | src/fallout/ai/combat/combatprocedureattacklow.cpp:59 |

### CombatProcedureAttackMelee (17)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CC1F0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:112 |
| 0x009CD150 | CheckStopBlocking | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:5393 |
| 0x009CC0C0 | CombatProcedureAttackMelee | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:1054 |
| 0x009CE560 | GetCurrentAttackReach | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:318 |
| 0x009CFD20 | GetFacingTargetDistance | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:432 |
| 0x009CFE90 | GetMovingTargetVelocity | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:6988 |
| 0x009CCED0 | HandleAttack | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:1873 |
| 0x009D0790 | LoadGame | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:617 |
| 0x009D0690 | SaveGame | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:577 |
| 0x009CCB20 | SelectAttack | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:865 |
| 0x009CF6D0 | SetCombatState | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:59 |
| 0x009CF660 | SetManeuverState | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:347 |
| 0x009CE190 | StartAdvance | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:300 |
| 0x009CCE70 | StartAttack | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:175 |
| 0x009CDF00 | StartClose | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:2555 |
| 0x009CFC60 | StopMoving | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:414 |
| 0x009CC220 | ~CombatProcedureAttackMelee | proven | src/fallout/ai/combat/combatprocedureattackmelee.cpp:130 |

### CombatProcedureAttackRanged (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D0950 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:72 |
| 0x009D0890 | CombatProcedureAttackRanged | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:2198 |
| 0x009D1DC0 | Disarmed | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:58 |
| 0x009D23A0 | LoadGame | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:156 |
| 0x009D2310 | SaveGame | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:125 |
| 0x009D09A0 | Shutdown | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:97 |
| 0x009D0980 | ~CombatProcedureAttackRanged | proven | src/fallout/ai/combat/combatprocedureattackranged.cpp:21 |

### CombatProcedureBeInCover (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D2520 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:101 |
| 0x009D2440 | CombatProcedureBeInCover | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:431 |
| 0x009D3470 | DebugText | class | src/fallout/ai/combat/combatprocedurebeincover.cpp:326 |
| 0x009D38F0 | LoadGame | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:525 |
| 0x009D3800 | SaveGame | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:465 |
| 0x009D2550 | ~CombatProcedureBeInCover | proven | src/fallout/ai/combat/combatprocedurebeincover.cpp:161 |

### CombatProcedureEngageTarget (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D3B00 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:40 |
| 0x009D4F50 | CanAttackerSneak | proven | src/staging/blk_009c0000_od.cpp:2549 |
| 0x009D3A00 | CombatProcedureEngageTarget | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:1704 |
| 0x009D5990 | LoadGame | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:160 |
| 0x009D5880 | SaveGame | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:95 |
| 0x009D3B50 | Shutdown | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:23 |
| 0x009D3B30 | ~CombatProcedureEngageTarget | proven | src/fallout/ai/combat/combatprocedureengagetarget.cpp:58 |

### CombatProcedureEvade (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D5B10 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureevade.cpp:78 |
| 0x009D5AD0 | CombatProcedureEvade | proven | src/fallout/ai/combat/combatprocedureevade.cpp:66 |
| 0x009D5FF0 | LoadGame | proven | src/fallout/ai/combat/combatprocedureevade.cpp:26 |
| 0x009D5B40 | ~CombatProcedureEvade | proven | src/fallout/ai/combat/combatprocedureevade.cpp:44 |

### CombatProcedureEx (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00996E60 | SetLookAtPoint | decomp | src/fallout/ai/combat/combatprocedure.cpp:106 |

### CombatProcedureHideFromTarget (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D60F0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:50 |
| 0x009D6030 | CombatProcedureHideFromTarget | proven | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:95 |
| 0x009D60E0 | GetType | proven | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:19 |
| 0x009D6120 | ~CombatProcedureHideFromTarget | proven | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:35 |

### CombatProcedureMove (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D6B70 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatproceduremove.cpp:12 |
| 0x009D69F0 | CombatProcedureMove | proven | src/fallout/ai/combat/combatproceduremove.cpp:373 |
| 0x009D7C80 | CreatePath | proven | src/staging/blk_009c0000_od.cpp:387 |
| 0x009D8AD0 | InitLoadGame | proven | src/fallout/ai/combat/combatproceduremove.cpp:2112 |
| 0x009D89A0 | LoadGame | proven | src/fallout/ai/combat/combatproceduremove.cpp:278 |
| 0x009D8880 | SaveGame | proven | src/fallout/ai/combat/combatproceduremove.cpp:218 |
| 0x009D6CA0 | Update | proven | src/fallout/ai/combat/combatproceduremove.cpp:976 |
| 0x009D6BA0 | ~CombatProcedureMove | proven | src/fallout/ai/combat/combatproceduremove.cpp:432 |

### CombatProcedureSearch (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D8C10 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatproceduresearch.cpp:36 |
| 0x009D8B60 | CombatProcedureSearch | proven | src/fallout/ai/combat/combatproceduresearch.cpp:289 |
| 0x009D8C00 | GetType | proven | src/fallout/ai/combat/combatproceduresearch.cpp:21 |
| 0x009DA640 | LoadGame | proven | src/fallout/ai/combat/combatproceduresearch.cpp:171 |
| 0x009DA5C0 | SaveGame | proven | src/fallout/ai/combat/combatproceduresearch.cpp:137 |
| 0x009D8C40 | ~CombatProcedureSearch | proven | src/fallout/ai/combat/combatproceduresearch.cpp:81 |

### CombatProcedureShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CB6E0 | GetPathingPoint | decomp | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:501 |

### CombatProcedureSW (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DA7C0 | UpdateWeaponDraw | class | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:443 |

### CombatProcedureSwitchWeapon (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DA770 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:61 |
| 0x009DA720 | CombatProcedureSwitchWeapon | proven | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:116 |
| 0x009DA970 | FUN_009da970 | unnamed | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:47 |
| 0x009DA9B0 | LoadGame | proven | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:95 |
| 0x009DA7A0 | ~CombatProcedureSwitchWeapon | proven | src/fallout/ai/combat/combatprocedureswitchweapon.cpp:18 |

### CombatProcedureUseCombatItem (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DAA60 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:50 |
| 0x009DAA10 | CombatProcedureUseCombatItem | proven | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:72 |
| 0x009DAA50 | GetProcedureType | class | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:19 |
| 0x009DAC80 | LoadGame | proven | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:100 |
| 0x009DAAB0 | Update | proven | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:401 |
| 0x009DAA90 | ~CombatProcedureUseCombatItem | proven | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:37 |

### CombatProcStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CFD70 | IsTargetOutOfRange | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:4363 |

### CombatRange (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A4960 | Contains | decomp | src/staging/blk_009a0000_od.cpp:7702 |

### CombatS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F74C0 | FUN_008f74c0 | probable | src/fallout/ai/highprocess.cpp:20005 |

### CombatSearchCls (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098C7B0 | CheckOtherEntriesForTarget | decomp | src/fallout/ai/combat/combatgroup.cpp:5072 |

### CombatSearchLocation (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985BE0 | GetColor | proven | src/fallout/ai/combat/combatgroup.cpp:2150 |

### CombatSearchMgr (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098C710 | FUN_0098c710 | unnamed | src/staging/blk_00980000_od.cpp:4041 |

### CombatState (44)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A0D00 | AddUnreachableCoverLocation | proven | src/fallout/ai/combat/combatstate.cpp:1218 |
| 0x0099D310 | BuildCoveredMoveRequest | proven | src/fallout/ai/combat/combatstate.cpp:8120 |
| 0x0099CB70 | BuildTargetLOSLocationsArray | proven | src/fallout/ai/combat/combatstate.cpp:2964 |
| 0x00997BA0 | ChangeProcessLevel | proven | src/fallout/ai/combat/combatstate.cpp:599 |
| 0x0099CC60 | CheckCoverLOS | proven | src/fallout/ai/combat/combatstate.cpp:7814 |
| 0x0099CCD0 | CheckCoverSafe | proven | src/fallout/ai/combat/combatstate.cpp:8050 |
| 0x0099CEC0 | CheckLedgeCoverAngle | proven | src/fallout/ai/combat/combatstate.cpp:4235 |
| 0x0099A530 | CheckReferences | proven | src/fallout/ai/combat/combatstate.cpp:1609 |
| 0x009A1380 | CheckShouldFlee | proven | src/staging/blk_009a0000_od.cpp:2214 |
| 0x0099CA00 | CheckTargetsCoverLOS | proven | src/fallout/ai/combat/combatstate.cpp:2760 |
| 0x00981340 | ClearCombatItem | proven | src/fallout/ai/combatcontroller.cpp:354 |
| 0x009A0A40 | ClearLocationTarget | proven | src/fallout/ai/combat/combatstate.cpp:280 |
| 0x0099A420 | ClearReferencePointer | proven | src/fallout/ai/combat/combatstate.cpp:7281 |
| 0x00997600 | CombatState | proven | src/fallout/ai/combat/combatstate.cpp: |
| 0x0099A6B0 | DamagedByAttacker | proven | src/fallout/ai/combat/combatstate.cpp:850 |
| 0x0099A720 | Disarmed | proven | src/fallout/ai/combat/combatstate.cpp:885 |
| 0x00997C30 | DoInitialUpdate | proven | src/fallout/ai/combat/combatstate.cpp:2285 |
| 0x0099D030 | FindBestAdvanceLocation | proven | src/fallout/ai/combat/combatstate.cpp:11293 |
| 0x0099EBE0 | FindBestFleeLocation | proven | src/staging/blk_00980000_od.cpp:9398 |
| 0x0099AC20 | FindCombatLocation | proven | src/fallout/ai/combat/combatstate.cpp:10896 |
| 0x0099B5A0 | FindGrenadeThrowLocation | proven | src/fallout/ai/combat/combatstate.cpp:9645 |
| 0x0099E840 | FindOptimalLocation | proven | src/fallout/ai/actor.cpp:111087 |
| 0x0099A5E0 | FiredProjectile | proven | src/fallout/ai/combat/combatstate.cpp:792 |
| 0x0099A2D0 | GetBestCombatWeapon | proven | src/fallout/ai/combat/combatstate.cpp:2398 |
| 0x0097C150 | GetCombatWeapon | proven | src/fallout/ai/combat/combatactions.cpp:612 |
| 0x0097AC90 | GetCombatWeaponDPS | proven | src/fallout/ai/combat/combataction.cpp:304 |
| 0x00575610 | GetInventoryItemCount | probable | src/fallout/ai/combat/combatstate.cpp:6 |
| 0x0097FB60 | GetSecondaryCoverLocation | proven | src/fallout/ai/combatcontroller.cpp:476 |
| 0x009A2A30 | InitLoadGame | proven | src/fallout/ai/combat/combatstate.cpp:11693 |
| 0x009A2040 | LoadGame | proven | src/fallout/ai/combat/combatstate_rtm_variant.cpp:356 |
| 0x0099A780 | PreActivateReference | proven | src/fallout/ai/combat/combatstate.cpp:1835 |
| 0x008BE1B0 | ProcessCoverLOSResult | decomp | src/fallout/ai/combat/combatstate.cpp:21 |
| 0x009A06C0 | SetCombatItem | proven | src/fallout/ai/combat/combatstate.cpp:3115 |
| 0x009A0910 | SetLocationTargetLocation | proven | src/fallout/ai/combat/combatstate.cpp:3645 |
| 0x009A0790 | SetLocationTargetRef | proven | src/fallout/ai/combat/combatstate.cpp:4663 |
| 0x0099A8D0 | TargetChanged | proven | src/fallout/ai/combat/combatstate.cpp:2515 |
| 0x009A05B0 | UnreserveCoverLocation | proven | src/fallout/ai/combat/combatcovermap.cpp:129 |
| 0x00997CB0 | Update | proven | src/fallout/ai/combat/combatstate.cpp:647 |
| 0x00999260 | UpdateCombatPermissions | proven | src/fallout/ai/combat/combatstate.cpp:3887 |
| 0x0064BF90 | UpdateCombatStateData | probable | src/fallout/ai/combat/combatstate.cpp:30 |
| 0x009A1010 | UpdateCombatStrength | proven | src/fallout/ai/combat/combatstate.cpp:1300 |
| 0x00999160 | UpdateLow | proven | src/fallout/ai/combat/combatstate.cpp:2352 |
| 0x0099A840 | UsedCombatItem | proven | src/fallout/ai/combat/combatstate.cpp:2435 |
| 0x00997AA0 | ~CombatState | proven | src/fallout/ai/combat/combatstate.cpp:2244 |

### CombatStateArray (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AAD80 | CopyFrom | decomp | src/fallout/ai/combat/combatworldstate.cpp:67 |
| 0x009AA490 | FUN_009aa490 | unnamed | src/staging/blk_009a0000_od.cpp:230 |

### CombatStateHash (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00994A90 | ComputeHash | decomp | src/staging/blk_00980000_od.cpp:5504 |

### CombatStyleData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005059C0 | Endian | proven | src/fallout_shared/tescombatstyle.cpp:250 |

### CombatTarget (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985930 | InitLoadGame | proven | src/fallout/ai/combat/combatgroup.cpp:444 |
| 0x00985800 | LoadGame | proven | src/fallout/ai/combat/combatgroup.cpp:2104 |
| 0x009856E0 | SaveGame | proven | src/fallout/ai/combat/combatgroup.cpp:2042 |

### CombatTargetMap (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A3EC0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combattargetmap.cpp:52 |
| 0x009A3FE0 | AddTargetAttacker | proven | src/fallout/ai/combat/combattargetmap.cpp:139 |
| 0x009A3E90 | CombatTargetMap | proven | src/staging/blk_009a0000_od.cpp:143 |
| 0x009A4250 | GetTargetsForActor | decomp | src/fallout/misc/saveload/bgssaveloadchangesmap.cpp:15 |
| 0x009A50B0 | ResetTargetMap | decomp | src/fallout/ai/combat/combattargetmap.cpp:6 |
| 0x009A3EF0 | ~CombatTargetMap | proven | src/fallout/ai/combat/combattargetmap.cpp:178 |

### CombatTargetTimestamp (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006A7F50 | FUN_006a7f50 | unnamed | src/unmapped/astarsearch.cpp:25 |
| 0x009A5FF0 | LoadGame | decomp | src/fallout/ai/combat/combattimer.cpp:6 |

### CombatThing (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D1C90 | GetTrajectory | decomp | src/fallout/ai/combat/combatprocedureattackranged.cpp:2329 |

### CombatThreat (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A4C70 | GetAvoidNode | proven | src/staging/blk_009a0000_od.cpp:2815 |
| 0x009A4A10 | GetThreatLinearVelocity | proven | src/staging/blk_009a0000_od.cpp:5126 |

### CombatThreatMap (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A5020 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/combatthreatmap.cpp:101 |
| 0x009A52F0 | AddThreat | proven | src/fallout/ai/combat/projectile.cpp:4736 |
| 0x009A54A0 | AddThreat | proven | src/staging/blk_009a0000_od.cpp:2922 |
| 0x009A5C40 | ApplyLoadBuffer | decomp | src/fallout/ai/combat/combatthreatmap.cpp:7 |
| 0x00991080 | CombatThreatMap | decomp | src/fallout/ai/combat/combatthreatmap.cpp:35 |
| 0x009A4FB0 | CombatThreatMap | proven | src/staging/blk_009a0000_od.cpp:2900 |
| 0x00993800 | FUN_00993800 | unnamed | src/staging/blk_00980000_od.cpp:532 |
| 0x009A5A70 | LoadGame | proven | src/unmapped/nitarray_od_oy_noo2_variant.cpp:279 |
| 0x009A59E0 | SaveThreats | decomp | src/staging/blk_009a0000_od.cpp:1680 |
| 0x009A5050 | ~CombatThreatMap | proven | src/fallout/ai/combat/combatthreatmap.cpp:55 |

### CombatTimer (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097FA50 | IsSet | proven | src/staging/blk_00960000_od.cpp:1473 |
| 0x009A5EB0 | SaveGame | proven | src/fallout/ai/combat/combattimer.cpp:34 |

### CombatTimeStamp (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004300A0 | CombatTimeStamp | proven | src/fallout_shared/extradataobjects.cpp:406 |
| 0x0097FA90 | DisplayElapsedTime | proven | src/staging/blk_00960000_od.cpp:2549 |
| 0x009A5F90 | SaveGame | proven | src/fallout/ai/combat/combattimer.cpp:56 |

### CombatUpdate (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00997CF0 | FUN_00997cf0 | probable | src/fallout/ai/combat/combatstate.cpp:5661 |

### CombatUpdater (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097DA50 | FUN_0097da50 | probable | src/fallout/ai/combatcontroller.cpp:5188 |

### CombatUtilities (25)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A93A0 | CalculateCoverPositions | proven | src/fallout/ai/actor.cpp:41272 |
| 0x009A93E0 | CalculateCoverPositions | proven | src/staging/blk_009a0000_od.cpp:5554 |
| 0x009A7940 | CalculateLOS | proven | src/fallout/ai/combat/combatutilities_decl_variant.cpp:3191 |
| 0x009A6E90 | CalculateProjectileLOS | proven | src/fallout/ai/combat/combatutilities_o2_variant_od_oy_noo2_variant.cpp:164 |
| 0x009A7580 | CheckProjectileArc | proven | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:231 |
| 0x009A7670 | CheckProjectileArc | proven | src/fallout/ai/combat/combatutilities.cpp:2314 |
| 0x009A6830 | ComputeFaceTargetDistance | proven | src/fallout/ai/combat/combatutilities.cpp:1454 |
| 0x009A68B0 | ComputeFaceTargetLocation | proven | src/fallout/ai/combat/combatutilities.cpp:1704 |
| 0x009A9180 | ComputeOptimalWeaponRanges | proven | src/fallout/ai/combat/combatutilities.cpp:3576 |
| 0x009A7DD0 | ComputeProjectileTime | proven | src/fallout/ai/combat/combatutilities.cpp:9 |
| 0x009A7D50 | FindAngleOfProjectile | proven | src/staging/blk_009a0000_od.cpp:3023 |
| 0x009A88E0 | GetAngleToProjectedPoint | proven | src/fallout/ai/combat/combatutilities.cpp:4156 |
| 0x009A8970 | GetAngleToProjectedPoint | proven | src/fallout/ai/combat/combatutilities.cpp:3011 |
| 0x009A87F0 | GetAngleToProjectedTarget | proven | src/staging/blk_009a0000_od.cpp:5514 |
| 0x009A8050 | GetAttackerFiringLocation | proven | src/fallout/ai/combat/combatutilities.cpp:4620 |
| 0x009A8250 | GetAttackerFiringLocationSimple | proven | src/fallout/ai/combat/combatutilities.cpp:212 |
| 0x009A6770 | GetAttackerTargetExtentSum | proven | src/fallout/ai/combat/combatutilities.cpp:1415 |
| 0x009A64D0 | GetDistanceBetweenFacingActors | proven | src/fallout/ai/combat/combatutilities.cpp:1241 |
| 0x009A60E0 | GetFacingTarget | proven | src/fallout/ai/combat/combatutilities.cpp:999 |
| 0x009A8DF0 | GetProjectedPointForTarget | proven | src/fallout/ai/combat/combatutilities.cpp:3446 |
| 0x009A8F00 | GetProjectedPointForTarget | proven | src/fallout/ai/combat/combatutilities.cpp:3496 |
| 0x009A7F00 | GetProjectileMaximumRange | proven | src/fallout/ai/combat/combatutilities.cpp:643 |
| 0x009A8460 | GetTargetFiringZOffset | proven | src/fallout/ai/combat/combatutilities.cpp:2955 |
| 0x009A9630 | IsActorUsingMelee | proven | src/fallout/ai/combat/combatstate.cpp:3565 |
| 0x009A96C0 | IsActorUsingRanged | proven | src/staging/blk_009a0000_od.cpp:585 |

### CombatWorldState (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AA150 | GetDebugText | proven | src/staging/blk_009a0000_od.cpp:1273 |
| 0x009AA1B0 | GetStateValueText | proven | src/staging/blk_009a0000_od.cpp:7726 |

### CombatWorldStateArray (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AA4B0 | ClearValues | proven | src/staging/blk_009a0000_od.cpp:8895 |
| 0x009947F0 | GetStateValue | proven | src/staging/blk_00980000_od.cpp:5437 |
| 0x009AADC0 | IsTrue | proven | src/staging/blk_009a0000_od.cpp:3147 |

### CombatWorldStateListNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0062D990 | GetNext | decomp | src/fallout/ai/combat/combatworldstate.cpp:15 |

### (free functions) (20)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A9A20 | AssignCombatPlanAngles | decomp | src/fallout/ai/combat/combatutilities.cpp:4059 |
| 0x009C4DA0 | ClearCombatStyleAndActorCause | class | src/fallout/ai/mobileobject.cpp:6439 |
| 0x009A3B20 | CopyCombatThreatEntries | decomp | src/staging/blk_009a0000_od.cpp:1095 |
| 0x005054B0 | CopyFromCombatStyle | class | src/fallout_shared/tescombatstyle.cpp:182 |
| 0x009923D0 | CreateCombatController | probable | src/fallout/ai/combat/combatmanager.cpp:1636 |
| 0x0098FDF0 | CreateCombatGroupStrategy | decomp | src/staging/blk_00980000_od.cpp:4969 |
| 0x0097AA40 | DestroyCombatActionTables | decomp | src/staging/blk_00960000_od.cpp:2346 |
| 0x00984470 | GetCombatGoal | probable | src/fallout/ai/combat/combatgoal.cpp:429 |
| 0x0097A990 | InitCombatActions | decomp | src/staging/blk_00960000_od.cpp:918 |
| 0x00984A50 | InitCombatGoalTable | decomp | src/fallout/ai/combat/combatgoal.cpp:412 |
| 0x009B5770 | InitCombatThing | decomp | src/staging/blk_009a0000_od.cpp:4122 |
| 0x0097BD20 | IsCombatActionValid | decomp | src/fallout/ai/combat/combatactions.cpp:1687 |
| 0x00505550 | IsCombatStyleDifferent | class | src/fallout_shared/tescombatstyle.cpp:101 |
| 0x009900F0 | SelectCombatStyleHandler | decomp | src/staging/blk_00980000_od.cpp:5031 |
| 0x008D9630 | SetCombatState | class | src/fallout/ai/highprocess.cpp:4882 |
| 0x00845960 | SetCombatTargetQuantity | decomp | src/fallout/misc/saveload/bgssaveloadchangesmap.cpp:245 |
| 0x0080B850 | StartHostilityAndCombat | decomp | src/fallout/magic/commandeffect.cpp:1054 |
| 0x00916880 | TryStartCombatAction | class | src/fallout/ai/middlehighprocess.cpp:7921 |
| 0x009CDF80 | UpdateCombatMovement | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:5465 |
| 0x009D6C00 | UpdateCombatMovement | class | src/fallout/ai/combat/combatproceduremove.cpp:164 |

## 8 Detection, crime and reactions

Detection, alarms and crime tracking.

### ActorCause (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0066E910 | ClearActorCauseList | decomp | src/fallout_shared/actorcause.cpp:6 |

### AlarmActorView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C09E0 | FUN_008c09e0 | probable | src/fallout/ai/actor.cpp:110806 |

### Crime (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EB9C0 | AddActor | decomp | src/fallout/ai/alarmpackage.cpp:239 |
| 0x009EB500 | Crime | proven | src/fallout/ai/processlists.cpp:8645 |
| 0x009EBB80 | GetSaveSize | proven | src/fallout/ai/alarmpackage.cpp:837 |
| 0x009EC400 | InitLoadGame | proven | src/fallout/ai/alarmpackage.cpp:1749 |
| 0x009EB9A0 | IsActorInList | decomp | src/fallout/ai/alarmpackage.cpp:71 |
| 0x009EB8A0 | ShouldCrimeBeRemoved | proven | src/staging/blk_009e0000_od.cpp:643 |

### CrimeProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00975320 | FUN_00975320 | unnamed | src/fallout/ai/processlists.cpp:12589 |

### DetectionList (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009764A0 | HasNearbyDetectedActor | decomp | src/fallout/ai/processlists.cpp:12868 |

### DetectionLists (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096C330 | UpdateDetection | decomp | src/fallout/ai/processlists.cpp:9707 |

### DetectionState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0066E590 | DetectionState | proven | src/bscore/bssimplelist.cpp:665 |

### DetectionStateProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D7070 | SaveDetectionState | decomp | src/fallout/ai/highprocess.cpp:10355 |

### DetectionTaskData (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8400 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:106 |
| 0x008C82A0 | DetectionTaskData | proven | src/fallout/ai/aitaskmanager.cpp:1403 |
| 0x008C8430 | ~DetectionTaskData | proven | src/fallout/ai/aitaskmanager.cpp:122 |

### DetectionViewData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0066E440 | FUN_0066e440 | unnamed | src/staging/blk_00660000_od.cpp:984 |
| 0x008D7140 | LoadGame | decomp | src/fallout/ai/highprocess.cpp:1092 |

### DetectLifeEffect (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0080CD60 | 'scalar deleting destructor' | proven | src/fallout/magic/detectlifeeffect.cpp:31 |
| 0x0080CDB0 | Clone | proven | src/fallout/magic/detectlifeeffect.cpp:157 |
| 0x0080CD30 | DetectLifeEffect | proven | src/staging/blk_00800000_od.cpp:2777 |
| 0x0080D0E0 | FUN_0080d0e0 | class | src/fallout/magic/detectlifeeffect.cpp:103 |
| 0x0080CE60 | Start | proven | src/fallout/magic/detectlifeeffect.cpp:75 |
| 0x0080CD90 | ~DetectLifeEffect | proven | src/fallout/magic/detectlifeeffect.cpp:49 |

### ExtraActorCause (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0042CB00 | 'scalar deleting destructor' | proven | src/fallout_shared/extradatalist.cpp:9051 |
| 0x0042CA90 | ExtraActorCause | proven | src/fallout_shared/extradatalist.cpp:23500 |
| 0x0042CB30 | ~ExtraActorCause | proven | src/staging/blk_00420000_od.cpp:1932 |

### ExtraOwnership (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00431A70 | Differs | proven | src/fallout_shared/extradataobjects.cpp:3700 |
| 0x0042C5E0 | ExtraOwnership | proven | src/fallout_shared/extradatalist.cpp:10819 |
| 0x00431A40 | ExtraOwnership | proven | src/fallout_shared/extradataobjects.cpp:51 |

### ExtraPlayerCrimeList (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432A70 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:2565 |
| 0x004329D0 | ExtraPlayerCrimeList | proven | src/fallout_shared/extradataobjects.cpp:4475 |
| 0x00432AA0 | ExtraPlayerCrimeList | proven | src/fallout_shared/extradataobjects.cpp:6188 |
| 0x00432B50 | ~ExtraPlayerCrimeList | proven | src/fallout_shared/extradataobjects.cpp:2585 |

### (free functions) (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00975B60 | CleanupCrimeLists | decomp | src/fallout/ai/processlists.cpp:16066 |
| 0x00972570 | FindCrime | decomp | src/fallout/ai/processlists.cpp:3693 |
| 0x008FFD10 | IsTargetDetectable | decomp | src/fallout/ai/highprocess.cpp:10636 |
| 0x009ECF70 | LoadCrimeList | class | src/fallout/ai/alarmpackage.cpp:638 |
| 0x009F5A60 | SaveCrimeData | class | src/fallout/ai/sandboxpackage.cpp:1173 |
| 0x009ECEC0 | SaveCrimeList | class | src/fallout/ai/alarmpackage.cpp:593 |

## 9 Dialogue, barks and companions

Topics, conversations between NPCs, follower barks, companion wheel.

### CompanionWheelMenu (10)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00754C30 | 'scalar deleting destructor' | proven | src/fallout/interface/menus/companionwheelmenu.cpp:93 |
| 0x00754B40 | CompanionWheelMenu | proven | src/fallout/interface/menus/chargenmenu.cpp:1837 |
| 0x00756930 | Do_Backup | proven | src/fallout/interface/menus/companionwheelmenu.cpp:130 |
| 0x007560C0 | Do_ToggleNearFar | proven | src/fallout/interface/menus/companionwheelmenu.cpp:157 |
| 0x007563A0 | Do_ToggleStayFollow | proven | src/fallout/interface/menus/companionwheelmenu.cpp:3792 |
| 0x007552E0 | DoClick | proven | src/fallout/interface/menus/companionwheelmenu.cpp:308 |
| 0x00754D90 | GetShouldCompanionWheelOpen | proven | src/fallout/interface/menus/companionwheelmenu.cpp:34 |
| 0x00755760 | HandleMouseover | proven | src/fallout/interface/menus/companionwheelmenu.cpp:740 |
| 0x00755DC0 | SetButtonContextText | proven | src/fallout/interface/menus/companionwheelmenu.cpp:3580 |
| 0x00754C60 | ~CompanionWheelMenu | proven | src/fallout/interface/menus/companionwheelmenu.cpp:275 |

### Conversation (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0083B930 | ClearList | proven | src/bscore/bssimplelist_h_unit.cpp:1012 |
| 0x0083B9A0 | FirstItem | proven | src/fallout/ai/mobileobject.cpp:12814 |
| 0x0083C420 | FUN_0083c420 | unnamed | src/fallout/dialogue/conversation.cpp:47 |
| 0x0083BAC0 | GetDialogueItemByIndex | proven | src/fallout/dialogue/conversation.cpp:299 |
| 0x0083B9F0 | GetNext | proven | src/fallout/audio/falloutradio.cpp:1085 |
| 0x0083BB30 | GetSaveSize | proven | src/fallout/dialogue/conversation.cpp:514 |
| 0x0083C330 | LoadGame | proven | src/fallout/dialogue/conversation.cpp:338 |
| 0x0083C270 | SaveGame | proven | src/fallout/dialogue/conversation.cpp:583 |

### DialogMenu (15)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00761930 | 'scalar deleting destructor' | proven | src/fallout/interface/menus/dialogmenu.cpp:807 |
| 0x00761900 | AssignTileByID | class | src/fallout/interface/menus/dialogmenu_h_unit.cpp: |
| 0x00762FF0 | BeginDialogueResponse | decomp | src/fallout/interface/menus/dialogmenu.cpp:40 |
| 0x00762160 | Close | decomp | src/fallout/interface/menus/dialogmenu.cpp:589 |
| 0x00761A20 | Create | proven | src/fallout/interface/menus/dialogmenu.cpp:346 |
| 0x007617A0 | DialogMenu | proven | src/staging/blk_00760000_od.cpp:1008 |
| 0x007618F0 | GetClass | class | src/fallout/interface/menus/dialogmenu_h_unit.cpp: |
| 0x007628C0 | HandleMenuInput | class | src/fallout/interface/menus/dialogmenu.cpp:7 |
| 0x007624F0 | HandleSelection | class | src/fallout/interface/menus/dialogmenu.cpp:647 |
| 0x007638B0 | LoadTopicsList | proven | src/fallout/interface/menus/dialogmenu.cpp:220 |
| 0x00763FF0 | ServiceStart | proven | src/fallout/interface/menus/dialogmenu.cpp:851 |
| 0x00762860 | SetCurrentTopic | decomp | src/fallout/interface/menus/dialogmenu.cpp:28 |
| 0x00764200 | SetPause | proven | src/fallout/interface/menus/dialogmenu.cpp:883 |
| 0x00762950 | UpdateDialog | class | src/fallout/interface/menus/dialogmenu.cpp:460 |
| 0x00761960 | ~DialogMenu | proven | src/fallout/interface/menus/dialogmenu.cpp:927 |

### DialogueItem (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0083C520 | DialogueItem | proven | src/fallout/dialogue/dialogueitem.cpp:380 |
| 0x0083C820 | GetActiveResponse | decomp | src/fallout/dialogue/dialogueitem.cpp:6 |
| 0x0083C900 | GetDialogueResponseIndex | proven | src/fallout/dialogue/dialogueitem.cpp:131 |
| 0x0083CC10 | LoadGame | proven | src/fallout/dialogue/dialogueitem.cpp:442 |
| 0x0083C850 | RunResult | proven | src/fallout_shared/tesobjectrefr.cpp:15119 |
| 0x0083CA90 | SaveGame | proven | src/fallout/dialogue/dialogueitem.cpp:219 |
| 0x0083CE40 | SaveGame | proven | src/fallout/dialogue/dialogueitem.cpp:303 |
| 0x005E3FA0 | SelectDefaultResponseList | decomp | src/fallout/dialogue/dialogueitem.cpp:15 |
| 0x0083C7B0 | SelectDefaultResponseList | decomp | src/fallout/dialogue/conversation.cpp:6 |

### DialogueResponse (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0083D1E0 | DialogueResponse | proven | src/fallout/dialogue/dialogueresponse.cpp:107 |
| 0x0083D280 | DialogueResponse | proven | src/fallout/dialogue/dialogueresponse.cpp:168 |
| 0x0083D490 | SaveGame | proven | src/fallout/dialogue/dialogueresponse.cpp:59 |
| 0x0083C750 | ~DialogueResponse | proven | src/staging/blk_00820000_od.cpp:4232 |

### ExtraInfoGeneralTopic (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00432440 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:4408 |
| 0x00432470 | ExtraInfoGeneralTopic | proven | src/fallout_shared/extradataobjects.cpp:4979 |
| 0x004324A0 | ExtraInfoGeneralTopic | proven | src/fallout_shared/extradataobjects.cpp:3477 |
| 0x004323B0 | ~ExtraInfoGeneralTopic | proven | src/fallout_shared/extradataobjects.cpp:2467 |

### ExtraSayTopicInfoOnceADay (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004374E0 | 'scalar deleting destructor' | proven | src/fallout_shared/extradataobjects.cpp:2819 |
| 0x00437440 | ExtraSayTopicInfoOnceADay | proven | src/fallout_shared/extradataobjects.cpp:5776 |
| 0x00437510 | ExtraSayTopicInfoOnceADay | proven | src/staging/blk_00420000_od.cpp:3928 |
| 0x004375C0 | ~ExtraSayTopicInfoOnceADay | proven | src/fallout_shared/tesobjectcell.cpp:16808 |

### ExtraSayToTopicInfo (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00437690 | ExtraSayToTopicInfo | proven | src/fallout_shared/extradataobjects.cpp:1290 |
| 0x004376E0 | ExtraSayToTopicInfo | proven | src/fallout_shared/extradataobjects.cpp:4744 |

### LipSyncAnimation (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004D5930 | ApplyToAnimationData | probable | src/fallout_shared/lipsynchanim.cpp:6 |
| 0x004D5850 | DeleteThis | decomp | src/fallout_shared/lipsynchanim.cpp:34 |

### LipSynchAnim (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004D5AD0 | ChangeFilenameToLipSynch | proven | src/fallout/ai/mobileobject.cpp:1201 |
| 0x004D5880 | Decompress | proven | src/fallout_shared/lipsynchanim.cpp:44 |
| 0x004D4F70 | LipSynchAnim | proven | src/staging/blk_004c0000_od.cpp:1072 |
| 0x004D52F0 | LoadFromFile | proven | src/fallout_shared/distant terrain system/bgsterrainmanager.cpp:7 |
| 0x004D5350 | LoadFromFile | proven | src/fallout_shared/lipsynchanim.cpp:105 |

### LipTask (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00905E00 | GetDescription | proven | src/fallout/ai/lipsyncbackgroundmanager.cpp:17 |
| 0x00905BA0 | LipTask | proven | src/bsmain/queuedfiles.cpp:179 |

### MenuTopic (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0083DF80 | FillResponseList | proven | src/fallout/dialogue/menutopic.cpp:1472 |
| 0x0083E170 | GetActiveResponse | decomp | src/fallout/dialogue/menutopic.cpp:8 |
| 0x0083F280 | GetSaveSize | proven | src/fallout/dialogue/menutopic.cpp:492 |
| 0x0083DB00 | MenuTopic | decomp | src/fallout/dialogue/menutopic.cpp:117 |
| 0x0083E110 | NextResponse | proven | src/bscore/bssimplelist_h_unit.cpp:356 |
| 0x0083FB10 | SaveGame | proven | src/fallout/misc/saveload/bgssavegamebuffer.cpp:397 |

### RadioConvTask (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00837290 | 'scalar deleting destructor' | proven | src/fallout/audio/falloutradio.cpp:1062 |
| 0x008373A0 | GetDescription | class | src/fallout/audio/falloutradio.cpp:790 |
| 0x00837250 | RadioConvTask | proven | src/fallout_shared/tesobjectacti.cpp:237 |
| 0x008372E0 | Run | proven | src/fallout/audio/falloutradio.cpp:1228 |
| 0x008372C0 | ~RadioConvTask | proven | src/fallout/audio/falloutradio.cpp:1593 |

### TESTopic (31)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006186A0 | 'scalar deleting destructor' | proven | src/fallout_shared/testopic.cpp:1054 |
| 0x0061A040 | AddDefaultTopics | proven | src/fallout_shared/testopic.cpp:592 |
| 0x00619B60 | ClearAllSaidOnceInfosForQuest | proven | src/staging/blk_00600000_od.cpp:977 |
| 0x00619A90 | ClearSaidOnceInfosForQuest | proven | src/fallout_shared/testopic.cpp:1115 |
| 0x0061A450 | CompareTopics | proven | src/fallout_shared/testopic.cpp:716 |
| 0x0061B320 | CreateDialogueItem | proven | src/fallout_shared/testopic.cpp:1173 |
| 0x0061A7D0 | FindMatchingTopicInfo | probable | src/fallout_shared/testopic.cpp:27 |
| 0x0083F0D0 | GetDummyNodeState | proven | src/fallout/dialogue/menutopic.cpp:584 |
| 0x00618660 | GetEditorID | proven | src/fallout_shared/bgsdehydration.cpp:804 |
| 0x00619F70 | GetInfoArray | proven | src/fallout_shared/testopic.cpp:1600 |
| 0x00619E10 | GetInfoByID | proven | src/fallout_shared/testopic.cpp:389 |
| 0x00619F20 | GetInfoByIndex | proven | src/fallout_shared/testopic.cpp:430 |
| 0x0061AF30 | GetMatchingFollowUpInfo | proven | src/fallout_shared/testopic_decl_variant.cpp:20 |
| 0x0061A720 | GetMatchingInfo | proven | src/fallout_shared/testopic.cpp:1143 |
| 0x0061A760 | GetMatchingInfo | proven | src/fallout_shared/testopic.cpp:752 |
| 0x0061A790 | GetMatchingInfo | proven | src/fallout_shared/testopic.cpp:17 |
| 0x00619D00 | GetOwnerQuest | proven | src/fallout_shared/testopic.cpp:333 |
| 0x0061A310 | GetOwnerTopic | proven | src/fallout_shared/testopic.cpp:651 |
| 0x00619C50 | GetQuestInfoElement | proven | src/fallout_shared/testopic.cpp:1458 |
| 0x0083DEA0 | HasDummyPrompt | proven | src/staging/blk_00820000_od.cpp:337 |
| 0x00619BC0 | HasQuest | proven | src/fallout_shared/testopic.cpp:1577 |
| 0x0061BCD0 | InitializeData | proven | src/fallout_shared/testopic.cpp:824 |
| 0x00619820 | InsertInfo | proven | src/fallout_shared/testopic.cpp:1875 |
| 0x006195D0 | InsertQuest | proven | src/fallout_shared/testopic.cpp:262 |
| 0x0083DE60 | IsPersuasion | proven | src/fallout/dialogue/menutopic.cpp:250 |
| 0x00619DF0 | IsRemappedRumors | proven | src/fallout_shared/testopic.cpp:375 |
| 0x00618AA0 | Load | proven | src/fallout_shared/testopic.cpp:1276 |
| 0x00619010 | SetDummyPrompt | proven | src/fallout_shared/testopic.cpp:233 |
| 0x00619430 | Sort | proven | src/fallout_shared/testopic.cpp:1417 |
| 0x00618580 | TESTopic | proven | src/fallout_shared/testopic.cpp:920 |
| 0x006186D0 | ~TESTopic | proven | src/staging/blk_00600000_od.cpp:1820 |

### TESTopicInfo (37)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0061CE10 | 'scalar deleting destructor' | proven | src/fallout_shared/testopicinfo.cpp:1971 |
| 0x0061F150 | AddTopicList | decomp | src/fallout_shared/testopicinfo.cpp:284 |
| 0x0061E600 | CheckCondition | proven | src/fallout_shared/testopicinfo.cpp:1259 |
| 0x0061CFF0 | ClearData | class | src/fallout_shared/testopicinfo.cpp:212 |
| 0x0061D230 | ClearResponses | decomp | src/fallout_shared/testopicinfo.cpp:206 |
| 0x0061E330 | CopyFrom | proven | src/fallout_shared/testopicinfo.cpp:1693 |
| 0x0061E780 | DuplicateResponseList | decomp | src/fallout_shared/testopicinfo.cpp:291 |
| 0x0083EC10 | FUN_0083ec10 | unnamed | src/fallout/dialogue/menutopic.cpp:205 |
| 0x007627E0 | GetActorValue | decomp | src/fallout/interface/menus/dialogmenu.cpp:724 |
| 0x00436AA0 | GetAddTopicList | class | src/fallout/ai/actor.cpp: |
| 0x0061F2B0 | GetDifficulty | proven | src/fallout_shared/testopicinfo.cpp:1887 |
| 0x0061E720 | GetDummyNodeState | proven | src/fallout_shared/testopicinfo.cpp:867 |
| 0x0061E2B0 | GetInfoDisplayText | proven | src/fallout_shared/testopicinfo.cpp:1145 |
| 0x00619A70 | GetInfoIndex | proven | src/fallout_shared/testopic.cpp:307 |
| 0x00762820 | GetPerk | decomp | src/fallout/interface/menus/dialogmenu.cpp:732 |
| 0x0061EB60 | GetResultScript | proven | src/fallout_shared/testopicinfo.cpp:686 |
| 0x0083DE40 | HasPrompt | proven | src/fallout/dialogue/menutopic.cpp:238 |
| 0x0061CF40 | InitializeComponent | class | src/fallout_shared/testopicinfo.cpp:180 |
| 0x0061D290 | InitItem | class | src/fallout_shared/testopicinfo.cpp:397 |
| 0x007627C0 | IsChallengeFlagSet | decomp | src/fallout/interface/menus/dialogmenu.cpp:740 |
| 0x00619B20 | IsSayOnce | proven | src/fallout_shared/testopic.cpp:318 |
| 0x0061DBD0 | LoadForm | class | src/fallout_shared/testopicinfo.cpp:31 |
| 0x0061DB30 | LoadGame | class | src/fallout_shared/testopicinfo.cpp:268 |
| 0x0061DAD0 | LoadGame2 | proven | src/fallout_shared/testopicinfo.cpp:1036 |
| 0x0061F220 | MarkAsRefusal | decomp | src/staging/blk_00600000_od.cpp:795 |
| 0x0061D250 | ResetResponseList | decomp | src/fallout_shared/testopicinfo.cpp:198 |
| 0x0061F280 | ResetSaidOnceFlags | proven | src/fallout_shared/testopicinfo.cpp:1220 |
| 0x0061DB80 | Revert | class | src/fallout_shared/testopicinfo.cpp:276 |
| 0x0061F170 | RunResultScript | proven | src/fallout/ai/playercharacter.cpp:1464 |
| 0x0061D6A0 | SetAltered | proven | src/fallout_shared/testopicinfo.cpp:1096 |
| 0x0061F340 | SetInfoIndex | proven | src/fallout_shared/testopicinfo.cpp:911 |
| 0x0061D140 | SetOwnerTopic | decomp | src/fallout_shared/testopicinfo.cpp:236 |
| 0x0061CFD0 | SetPrompt | proven | src/fallout_shared/testopicinfo.cpp:860 |
| 0x0061E180 | SetTopicInfoData | decomp | src/fallout_shared/testopicinfo.cpp:159 |
| 0x0061D710 | Sort | proven | src/fallout_shared/testopicinfo.cpp:1521 |
| 0x0061CCD0 | TESTopicInfo | proven | src/fallout_shared/testopicinfo.cpp:147 |
| 0x0061CEB0 | ~TESTopicInfo | proven | src/fallout_shared/testopicinfo.cpp:1323 |

### TESTopicInfoData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00413F40 | GetLinkToList | decomp | src/bscore/bssimplelist_h_unit.cpp: |
| 0x0061C360 | InitItem | decomp | src/fallout_shared/testopicinfo.cpp:487 |

### TopicMenuController (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0083E3E0 | AdvanceTopic | decomp | src/fallout/dialogue/menutopic.cpp:41 |
| 0x0083E4F0 | GetFirstTopic | decomp | src/fallout/dialogue/menutopic.cpp:34 |
| 0x0083E590 | GetInstance | decomp | src/fallout/dialogue/menutopic.cpp:197 |
| 0x0083E4C0 | GetSelectedTopic | decomp | src/fallout/dialogue/menutopic.cpp:21 |
| 0x004D5C60 | IncrementMiscStat | probable | src/fallout/dialogue/menutopic.cpp:59 |
| 0x0083E620 | Initialize | decomp | src/fallout/dialogue/menutopic.cpp:65 |
| 0x0083EBB0 | RunTopicResultScript | decomp | src/fallout/dialogue/menutopic.cpp:211 |
| 0x0083E370 | SelectTopic | decomp | src/fallout/dialogue/menutopic.cpp:50 |
| 0x0083E1A0 | TopicMenuController | decomp | src/fallout/dialogue/menutopic.cpp:190 |

### (free functions) (28)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008632A0 | AddLoadingTopic | decomp | src/fallout_shared/tessaveloadgame.cpp:1321 |
| 0x008ED400 | AddTopicInfo | class | src/fallout/ai/highprocess.cpp:40111 |
| 0x009527B0 | AddTopics | decomp | src/staging/blk_00940000_od.cpp:395 |
| 0x0061A380 | AddTopicToList | decomp | src/fallout_shared/testopic.cpp:677 |
| 0x00837060 | AdvanceConversation | decomp | src/fallout/audio/falloutradio.cpp:1541 |
| 0x0061BA10 | CheckTopicsForQuest | decomp | src/fallout_shared/testopic.cpp:794 |
| 0x00754CF0 | DestroyCompanionWheelMenu | decomp | src/fallout/interface/menus/companionwheelmenu.cpp:527 |
| 0x00487F50 | DialogueRandom | decomp | src/fallout_shared/tesleveledlist.cpp:462 |
| 0x005E3630 | FindDialogueFile | decomp | src/staging/blk_005e0000_od.cpp:4381 |
| 0x0061B440 | GenerateConversation | decomp | src/fallout_shared/testopic.cpp:2061 |
| 0x00643FF0 | GetFollowerOffset | decomp | src/fallout_shared/aiformulas.cpp:1175 |
| 0x0061D8C0 | GetResponseForTopicInfo | class | src/fallout_shared/testopicinfo.cpp:1582 |
| 0x00807BF0 | GetTopicResult | decomp | src/fallout/magic/bhktelekinesislistener.cpp:80 |
| 0x0061A2D0 | GetTopicSubTypeName | probable | src/fallout_shared/testopic.cpp:627 |
| 0x00618960 | InitLoadingTopic | class | src/fallout_shared/testopic.cpp:1079 |
| 0x0083CF40 | LoadDialogueItem | decomp | src/staging/blk_00820000_od.cpp:815 |
| 0x00754DE0 | OpenCompanionMenu | decomp | src/fallout/interface/menus/companionwheelmenu.cpp:631 |
| 0x0083F1D0 | PopTopicList | decomp | src/fallout/dialogue/menutopic.cpp:443 |
| 0x009805B0 | RemoveTopic | probable | src/fallout/ai/combatcontroller.cpp:3131 |
| 0x007575B0 | RunTopicResultScripts | probable | src/fallout/interface/menus/companionwheelmenu.cpp:220 |
| 0x0067B630 | SaveTopicData | class | src/fallout_shared/packagedatadialogue.cpp:125 |
| 0x00762130 | SetIAmInDialogue | decomp | src/fallout/ai/actor.cpp:354 |
| 0x0061A5A0 | SortTopicList | decomp | src/fallout_shared/testopic.cpp:1523 |
| 0x007640A0 | StartDialogueForTopic | decomp | src/fallout/interface/menus/dialogmenu.cpp:1146 |
| 0x007562B0 | ToggleRelatedTopic | probable | src/fallout/interface/menus/companionwheelmenu.cpp:388 |
| 0x00900830 | UpdateFollowerList | class | src/fallout/ai/highprocess.cpp:51736 |
| 0x0083EC30 | UpdateTopicList | decomp | src/fallout/dialogue/menutopic.cpp:393 |
| 0x0072D6D0 | UpdateTopicMenu | decomp | src/fallout/interface/menus/bartermenu.cpp:432 |

## 10 Animation, faces and bodies

FaceGen heads, biped models, animation data and idle animations.

### Animation (46)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00490500 | AddAnimation | proven | src/fallout_shared/animation.cpp:4967 |
| 0x00490400 | AddAnimationsFromList | proven | src/fallout_shared/animation.cpp:4200 |
| 0x0048F810 | Animation | proven | src/fallout_shared/animation.cpp:147 |
| 0x00498670 | AnimIdleFree | proven | src/fallout_shared/animation.cpp:9119 |
| 0x004994F0 | BlendOut | proven | src/fallout_shared/animation.cpp:7673 |
| 0x00496080 | ClearGroup | proven | src/fallout_shared/animation.cpp:1034 |
| 0x00495F50 | FindNextNoteKey | proven | src/fallout_shared/animation.cpp:6993 |
| 0x004910D0 | FindSkinnedNode | proven | src/fallout_shared/animation.cpp:532 |
| 0x004955C0 | ForceSection | proven | src/fallout_shared/animation.cpp:3120 |
| 0x009442A0 | FUN_009442a0 | unnamed | src/staging/blk_00940000_od.cpp:28 |
| 0x00497280 | GetAnimSequenceMap | proven | src/fallout_shared/animation.cpp:2995 |
| 0x00493830 | GetAnimsLoading | proven | src/fallout_shared/animation.cpp:639 |
| 0x00496940 | GetControllerManager | proven | src/fallout_shared/animation.cpp:1326 |
| 0x00494390 | GetDelta | proven | src/fallout_shared/animation.cpp:9369 |
| 0x00491090 | GetDuration | proven | src/staging/blk_00480000_od.cpp:709 |
| 0x00494300 | GetGroupSpeed | proven | src/fallout_shared/animation.cpp:790 |
| 0x004997F0 | GetSaveSize | proven | src/fallout_shared/animation.cpp:7850 |
| 0x00496550 | GetSmallestHavokBlendValue | proven | src/fallout_shared/animation.cpp:1284 |
| 0x00496500 | GetTESAnimGroup | proven | src/fallout_shared/animation.cpp:3785 |
| 0x00494710 | GroupLoaded | proven | src/fallout_shared/animation.cpp:857 |
| 0x0048FFD0 | Init | proven | src/fallout_shared/animation.cpp:101 |
| 0x0049A1C0 | LoadGame | proven | src/fallout_shared/inventorychanges.cpp:5332 |
| 0x00490330 | LoadSpecialAnims | proven | src/fallout_shared/animation.cpp:3074 |
| 0x00494740 | PlayGroup | proven | src/fallout_shared/animation.cpp:9467 |
| 0x00499240 | ReloadTargets | proven | src/fallout_shared/animation.cpp:7595 |
| 0x0049AB40 | Save | proven | src/staging/blk_00480000_od.cpp:3522 |
| 0x00499B90 | SaveGame | proven | src/fallout_shared/animation.cpp:8278 |
| 0x004C0C90 | SetAttackSpeed | proven | src/fallout_shared/inventorychanges.cpp:803 |
| 0x00490E60 | ShouldQueueSequenceCloning | proven | src/fallout_shared/animation.cpp:4008 |
| 0x0048FF50 | ShutdownAllAnimIdles | proven | src/staging/blk_00480000_od.cpp:1030 |
| 0x00497F20 | SpecialIdleAuto | proven | src/fallout_shared/animation.cpp:1745 |
| 0x004985F0 | SpecialIdleDonePlaying | proven | src/fallout/ai/actor.cpp:44045 |
| 0x00498910 | SpecialIdleFree | proven | src/fallout_shared/animation.cpp:5 |
| 0x00498230 | SpecialIdlePlay | proven | src/fallout_shared/animation.cpp:3550 |
| 0x00498290 | SpecialIdlePlay | proven | src/fallout_shared/animation.cpp:10021 |
| 0x00497CA0 | SpecialIdleQueue | proven | src/fallout_shared/animation.cpp:7268 |
| 0x00498030 | SpecialIdleReplace | proven | src/fallout_shared/animation.cpp:7332 |
| 0x004948C0 | StartGroup | proven | src/fallout_shared/animation.cpp:2637 |
| 0x004949A0 | StartGroup | proven | src/fallout_shared/animation.cpp:6707 |
| 0x00491180 | Update | proven | src/fallout_shared/animation.cpp:5591 |
| 0x0049BCA0 | UpdateBipOnly | proven | src/fallout_shared/animation.cpp:2909 |
| 0x00493900 | UpdateMovement | proven | src/fallout_shared/animation.cpp:3453 |
| 0x004939D0 | UpdateMovementNoWorldUpdate | proven | src/fallout_shared/animation.cpp:8642 |
| 0x00493BD0 | UpdateSceneGraphNoController | proven | src/fallout_shared/animation.cpp:6377 |
| 0x00496280 | ZeroGlobalTransform | proven | src/fallout_shared/animation.cpp:1179 |
| 0x0048FB50 | ~Animation | proven | src/staging/blk_00480000_od.cpp:2267 |

### AnimSequenceBase (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048EF60 | 'scalar deleting destructor' | proven | src/fallout_shared/animation.cpp:9673 |
| 0x0048EF40 | AnimSequenceBase | proven | src/fallout_shared/animation.cpp:190 |
| 0x0048F1B0 | AnimSequenceBase | proven | src/fallout_shared/animation.cpp:294 |

### AnimSequenceMultiple (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048F1D0 | 'scalar deleting destructor' | proven | src/fallout_shared/animation.cpp:3420 |
| 0x0048F0C0 | AnimSequenceMultiple | proven | src/fallout_shared/animation.cpp:282 |
| 0x0048F500 | GetCorrespondingSequence | proven | src/fallout_shared/animation.cpp:4645 |
| 0x0048F790 | GetSequence | proven | src/fallout_shared/animation.cpp:10083 |
| 0x0048F3D0 | RemoveSequence | proven | src/fallout_shared/animation.cpp:4598 |
| 0x0048F220 | ~AnimSequenceMultiple | proven | src/fallout_shared/animation.cpp:4173 |

### AnimSequenceSingle (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048EFC0 | 'scalar deleting destructor' | proven | src/fallout_shared/animation.cpp:2218 |
| 0x00490E10 | AnimSequenceSingle | proven | src/fallout_shared/animation.cpp:464 |
| 0x0048F080 | RemoveSequence | proven | src/fallout_shared/animation.cpp:3400 |
| 0x0048EE70 | ~AnimSequenceSingle | proven | src/fallout_shared/animation.cpp:2251 |

### AnimSequenceStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00495E40 | FUN_00495e40 | probable | src/fallout_shared/animation.cpp:4251 |

### BGSBipedModelList (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00474D10 | BGSBipedModelList | proven | src/fallout_shared/bgsbipedmodellist.cpp:91 |
| 0x00474FC0 | CompareComponent | proven | src/fallout_shared/bgsbipedmodellist.cpp:151 |
| 0x00474F70 | CopyComponent | proven | src/fallout_shared/bgsbipedmodellist.cpp:173 |
| 0x00475020 | GetFormAsBipedModelList | proven | src/fallout_shared/bgsbipedmodellist.cpp:6 |
| 0x00474DA0 | InitItem | proven | src/fallout_shared/bgsbipedmodellist.cpp:30 |
| 0x00474D60 | Save | proven | src/fallout_shared/bgsbipedmodellist.cpp:109 |
| 0x00474D40 | ~BGSBipedModelList | proven | src/fallout_shared/bgsbipedmodellist.cpp:144 |

### BipedAnim (33)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004AF240 | AddAddonNodes | proven | src/fallout_shared/bipedanim.cpp:698 |
| 0x004AD290 | ApplySkinnedObjects | proven | src/fallout_shared/bipedanim.cpp:482 |
| 0x004AD4A0 | AttachBipedModel | probable | src/fallout_shared/bipedanim.cpp:6 |
| 0x004AB750 | AttachBipedWeapon | proven | src/fallout_shared/bipedanim.cpp:1834 |
| 0x004AE250 | AttachFaceGenNode | probable | src/fallout_shared/bipedanim.cpp:334 |
| 0x00571B50 | AttachFaceGenNode | probable | src/fallout_shared/bipedanim.cpp:153 |
| 0x004AEB20 | AttachHelmet | proven | src/fallout_shared/bipedanim.cpp:1350 |
| 0x004ADE40 | AttachToSkeleton | proven | src/fallout_shared/bipedanim.cpp:1593 |
| 0x004AACA0 | BipedAnim | proven | src/fallout_shared/bipedanim.cpp:726 |
| 0x004ABFA0 | CanLoadHiddenBipedObjects | probable | src/fallout_shared/bipedanim.cpp:711 |
| 0x004AF950 | Get1stPersonModelFileName | proven | src/fallout_shared/bipedanim.cpp:614 |
| 0x0043F220 | GetBipObject | proven | src/fallout_shared/modelloader.cpp:11523 |
| 0x004AF290 | GetLightingProperty | proven | src/fallout_shared/bipedanim.cpp:632 |
| 0x004AFA50 | GetModelForSlot | decomp | src/fallout_shared/bipedanim.cpp:679 |
| 0x004AB230 | GetParentBone | proven | src/bsshader/bsshadertextureset.cpp:15 |
| 0x0043F010 | GetRequester | proven | src/fallout_shared/modelloader.cpp:5498 |
| 0x004AF360 | GetSkinBipedObject | proven | src/fallout_shared/bipedanim.cpp:576 |
| 0x004AAD00 | InitRoot | proven | src/fallout_shared/bipedanim.cpp:1482 |
| 0x004AE8A0 | IsSlotHidden | probable | src/fallout_shared/bipedanim.cpp:691 |
| 0x004AE790 | LoadFaceGenModel | proven | src/fallout_shared/bipedanim.cpp:1704 |
| 0x004ABD30 | QueueBipedParts | proven | src/fallout_shared/bipedanim_decl_variant.cpp:9 |
| 0x004AC130 | QueueSkinTexture | proven | src/fallout_shared/bipedanim.cpp:652 |
| 0x004ABFE0 | QueueSkinTextures | proven | src/fallout_shared/bipedanim.cpp:554 |
| 0x004AB130 | RecursivelyRemoveAllDecalPlacementVectorDataFromWeaponBone | proven | src/staging/blk_004a0000_od.cpp:4197 |
| 0x004AAE70 | RemoveAllParts | proven | src/fallout_shared/bipedanim.cpp:665 |
| 0x004AB5B0 | RemoveBipedWeapon | proven | src/fallout/ai/actor.cpp:142796 |
| 0x004AAFF0 | RemovePart | proven | src/fallout_shared/bipedanim.cpp:750 |
| 0x004AB020 | RemovePart | proven | src/fallout_shared/bipedanim.cpp:771 |
| 0x004AAF90 | RemovePartsByParent | decomp | src/fallout_shared/bipedanim.cpp:1236 |
| 0x004AB0C0 | RunBiped3DDetach | proven | src/staging/blk_004a0000_od.cpp:2703 |
| 0x004ABAD0 | SetBipedPart | proven | src/fallout_shared/bipedanim.cpp:442 |
| 0x004AB400 | SetBipedWeapon | proven | src/fallout_shared/bipedanim.cpp:1538 |
| 0x004AB250 | UpdateRaceSex | probable | src/fallout_shared/bipedanim.cpp:522 |

### BodyPartDisplay (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007DBFE0 | FUN_007dbfe0 | unnamed | src/fallout/interface/menus/statsmenu.cpp:1908 |
| 0x007DBFA0 | SetBodyPart | decomp | src/fallout/interface/menus/statsmenu.cpp:1529 |

### BSAnimGroupSequence (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0049BB20 | 'scalar deleting destructor' | proven | src/fallout_shared/animation.cpp:2035 |
| 0x0049BAA0 | BSAnimGroupSequence | proven | src/staging/blk_00480000_od.cpp:1734 |
| 0x004EE9F0 | BSAnimGroupSequence | proven | src/staging/blk_004e0000_od.cpp:3315 |
| 0x004EEC20 | CreateClone | proven | src/fallout_shared/bsanimgroupsequence.cpp:167 |
| 0x004EFDC0 | Deactivate | class | src/fallout_shared/bsanimgroupsequence.cpp:31 |
| 0x0048F7F0 | GetAnimGroup | proven | src/fallout_shared/tesanimgroup.cpp:102 |
| 0x004EF9A0 | GetPriority | probable | src/fallout_shared/bsanimgroupsequence.cpp:7 |
| 0x0049BB10 | GetRTTI | class | src/fallout_shared/bsanimgroupsequence_h_unit.cpp:16 |
| 0x004EFAA0 | GetSequenceSaveSize | proven | src/fallout_shared/bsanimgroupsequence.cpp:213 |
| 0x004EEC40 | GetViewerStrings | proven | src/fallout_shared/bsanimgroupsequence.cpp:189 |
| 0x004EEF00 | PlaySounds | proven | src/fallout_shared/bsanimgroupsequence.cpp:720 |
| 0x004EEB00 | ~BSAnimGroupSequence | proven | src/fallout_shared/bsanimgroupsequence.cpp:77 |

### BSAnimNote (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00A43F70 | GetRTTI | proven | src/gamebryo2.2/corelibs/nianimation/bslookiknote.cpp:8 |
| 0x00A44BF0 | GetViewerStrings | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:543 |
| 0x00A44930 | ParseTextKey | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:26 |
| 0x00A44A90 | SaveBinary | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:623 |
| 0x00A44830 | ~BSAnimNote | proven | src/staging/blk_00a40000_o2.cpp:1143 |

### BSAnimNoteListener (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00A41410 | Update | proven | src/staging/blk_00a40000_o2.cpp:835 |

### BSAnimNoteReceiver (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004B0580 | 'scalar deleting destructor' | proven | src/fallout_shared/bsanimnotereceiver.cpp:32 |
| 0x0057A960 | BSAnimNoteReceiver | proven | src/fallout_shared/tesobjectrefr.cpp:6095 |
| 0x004B0480 | ~BSAnimNoteReceiver | proven | src/staging/blk_004a0000_od.cpp:2798 |

### BSAnimNotes (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00A44A10 | 'scalar deleting destructor' | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:193 |
| 0x00A44940 | CreateObject | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:46 |
| 0x00A44920 | GetRTTI | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:8 |
| 0x00A44AF0 | LoadBinary | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:487 |
| 0x00A448C0 | RegisterStreamables | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:140 |
| 0x00A44B80 | SaveBinary | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:835 |
| 0x00A44970 | ~BSAnimNotes | proven | src/gamebryo2.2/corelibs/nianimation/bsanimnote.cpp:170 |

### BSFaceGenAnimationData (31)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00649CA0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1041 |
| 0x0064AD20 | AddKeyframe | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:48 |
| 0x0064AB40 | AddModifierKeyframe | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:37 |
| 0x00649680 | BSFaceGenAnimationData | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1921 |
| 0x0064A100 | CalculateRotationQuaternion | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:111 |
| 0x0064B5E0 | ClearTransitionTarget | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:6 |
| 0x0064C5A0 | CreateCopyBS | proven | src/staging/blk_00640000_od.cpp:6771 |
| 0x0064A770 | FadeOutMorphs | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:129 |
| 0x008D87E0 | GetChanged | decomp | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x00649B10 | GetCustomMorphWeight | class | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x00649BC0 | GetDead | class | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x006499E0 | GetExpressionWeight | class | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x005DD4A0 | GetModifierValue | proven | src/fallout_shared/tesscriptfunctions.cpp:2187 |
| 0x00649AA0 | GetPhonemeWeight | class | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x0064AA00 | InsertPhonemeKeyframe | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:75 |
| 0x00649C70 | SetAnimCustomMorphValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1026 |
| 0x00649BE0 | SetAnimExpressionValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:986 |
| 0x00649C10 | SetAnimModifierValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:879 |
| 0x00649C40 | SetAnimPhonemeValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1004 |
| 0x00649B50 | SetCustomMorphValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:966 |
| 0x00649A20 | SetExpressionValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:901 |
| 0x0064B2B0 | SetExpressionWeight | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:92 |
| 0x0064C410 | SetEyePosition | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1697 |
| 0x0064BCC0 | SetHeadTrackVector | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1139 |
| 0x00649BA0 | SetModified | class | src/fallout_shared/facegen/bsfacegenanimationdata_h_unit.cpp: |
| 0x00649A70 | SetModifierValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:919 |
| 0x0064AE60 | SetMorphFlags | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:14 |
| 0x00649AE0 | SetPhonemeValue | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:939 |
| 0x0064A920 | SetStateFlags | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:20 |
| 0x0064BE40 | UpdateEyeTracking | proven | src/staging/blk_00640000_od.cpp:3961 |
| 0x00649CE0 | ~BSFaceGenAnimationData | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1389 |

### BSFaceGenBaseMorphExtraData (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006626F0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:496 |
| 0x006624C0 | BSFaceGenBaseMorphExtraData | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:794 |
| 0x00662720 | ~BSFaceGenBaseMorphExtraData | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:519 |

### BSFaceGenBinaryFile (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00AAAB90 | 'scalar deleting destructor' | proven | src/staging/blk_00aa0000_od_ob1_variant.cpp:3034 |
| 0x00AC5490 | BSFaceGenBinaryFile | proven | src/bsmenu/tile_ob1_variant.cpp:1695 |
| 0x00AC5540 | LoadFile | proven | src/staging/blk_00ac0000_od_ob1_variant.cpp:41025 |
| 0x00AC5CF0 | read | proven | src/staging/blk_00ac0000_od.cpp:1391 |

### BSFaceGenImage (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0064CDF0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenimage.cpp:13 |
| 0x0064CCF0 | BSFaceGenImage | proven | src/staging/blk_00640000_od.cpp:4064 |
| 0x0064CE20 | ~BSFaceGenImage | proven | src/staging/blk_00640000_od.cpp:7800 |

### BSFaceGenKeyframe (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0064EAB0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:401 |
| 0x0064EA80 | BSFaceGenKeyframe | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:146 |
| 0x0064EAE0 | BSFaceGenKeyframe | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:162 |
| 0x00488D50 | GetTime | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:6 |
| 0x0064EB30 | SetTime | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:31 |
| 0x0064EB00 | SetType | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:19 |

### BSFaceGenKeyframeMultiple (15)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0064EBE0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:269 |
| 0x0064FC00 | ApplyFaceGenValues | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:114 |
| 0x0064EB60 | BSFaceGenKeyframeMultiple | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:86 |
| 0x0064EC10 | BSFaceGenKeyframeMultiple | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:313 |
| 0x0064F480 | ClearData | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:95 |
| 0x0064F530 | CreateCopy | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:422 |
| 0x0064F760 | GetAttributeStrength | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:57 |
| 0x005DD4E0 | GetQuantity | proven | src/fallout_shared/tesscriptfunctions.cpp:2194 |
| 0x0064F880 | HasNonzeroQuantity | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:72 |
| 0x0064F7E0 | IsEmpty | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:439 |
| 0x0064FB90 | IsQuantityInRange | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:49 |
| 0x0064F850 | NormalizeFaceGenValues | class | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:12 |
| 0x0064A4D0 | SetQuantity | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:167 |
| 0x00649A50 | SetQuantityNoTest | proven | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:1093 |
| 0x0064ED00 | ~BSFaceGenKeyframeMultiple | proven | src/fallout_shared/facegen/bsfacegenkeyframe.cpp:42 |

### BSFaceGenManager (39)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00653470 | ApplyHairMorph | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:626 |
| 0x006558B0 | AttachEyesToHead | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3232 |
| 0x00655320 | AttachHairToHead | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2780 |
| 0x00650EA0 | BSFaceGenManager | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2073 |
| 0x00657820 | BuildFaceGenPartPath | probable | src/fallout_shared/facegen/bsfacegenmanager.cpp:63 |
| 0x00652900 | CompareFaceGenCoord | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3730 |
| 0x006529A0 | CopyFaceGenCoord | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:513 |
| 0x00654720 | CreateFaceGenHead | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:5639 |
| 0x00652510 | CycleFaceGenCoordValue | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4770 |
| 0x00653520 | GetAsEGMFile | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2326 |
| 0x006537D0 | GetAsEGTFile | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2364 |
| 0x00653880 | GetAsNearestDetailDDSFile | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3833 |
| 0x00653620 | GetAsNIFFile | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3778 |
| 0x00653C40 | GetAsNIFFileHighLOD | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3890 |
| 0x00653A10 | GetAsNIFFileLowLOD | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:5270 |
| 0x006536D0 | GetAsTRIFile | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3934 |
| 0x00652440 | GetFaceCoordAttribute | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:486 |
| 0x00652230 | GetFaceCoordValue | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:6179 |
| 0x00653430 | GetFaceGenBaseMorphExtraData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:591 |
| 0x006521E0 | GetFaceGenCoordinates | decomp | src/fallout_shared/facegen/bsfacegenmanager.cpp:5 |
| 0x00651B30 | GetInstance | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:11 |
| 0x006521B0 | GetMaxControlID | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3971 |
| 0x00652110 | GetModelCache | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:25 |
| 0x006521F0 | InitFaceGenCoord | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:52 |
| 0x006519F0 | InitializeSystem | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:389 |
| 0x00651F70 | LoadEGMData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2266 |
| 0x00652040 | LoadEGTData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2299 |
| 0x00652140 | LockFaceGenAccess | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:434 |
| 0x00653E20 | NormalizeFaceGenValues | decomp | src/fallout_shared/facegen/bsfacegenmanager.cpp:34 |
| 0x00652E00 | OffsetFaceGenCoord | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4828 |
| 0x00657150 | QueueHeadParts | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:1678 |
| 0x00652FC0 | RandomizeFaceGenetic | proven | src/staging/blk_00640000_od.cpp:1661 |
| 0x00653340 | RefreshMeshFromBaseMorphExtraData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3431 |
| 0x00653E50 | ReplaceFaceMeshLOD | proven | src/fallout/interface/menus/racesexmenu.cpp:8460 |
| 0x00653DC0 | ResetQuantityArray | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:75 |
| 0x00652470 | SetFaceCoordAttribute | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4067 |
| 0x006524E0 | SetFaceCoordAttributes | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4018 |
| 0x00652320 | SetFaceCoordValue | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:5246 |
| 0x00652190 | UnlockFaceGenAccess | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:473 |

### BSFaceGenModel (20)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00659B20 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:196 |
| 0x0065B410 | ApplyCoordinateTexturingToMesh | proven | src/gamebryo2.2/corelibs/nimain/nifixedstring_h_unit.cpp: |
| 0x0065A970 | ApplyCoordinateToExistingMesh | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:1261 |
| 0x0065A910 | ApplyCoordinateToNewMesh | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:568 |
| 0x00659AE0 | BSFaceGenModel | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:1247 |
| 0x0065BBC0 | CloneTriBasedGeom | decomp | src/staging/blk_00640000_od.cpp:7635 |
| 0x0065A840 | ForceLoadModelTexture | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:808 |
| 0x0065C110 | GetEGMDataSize | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:910 |
| 0x006505D0 | GetEGMFilename | proven | src/staging/blk_00640000_od.cpp:1646 |
| 0x0065C490 | GetEGTDataSize | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:5072 |
| 0x00650600 | GetEGTFilename | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:190 |
| 0x006530E0 | GetFaceGenModelNode | probable | src/fallout_shared/facegen/bsfacegenmodel.cpp:158 |
| 0x0065C400 | KillTextureData | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:997 |
| 0x0065BF80 | LoadEGMData | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:864 |
| 0x0065C2C0 | LoadEGTData | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:129 |
| 0x0065A760 | LoadFaceGenTexture | probable | src/fallout_shared/facegen/bsfacegenmodel.cpp:145 |
| 0x00659C70 | LoadModel | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:212 |
| 0x00659CE0 | LoadModelMesh | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:6 |
| 0x0065C3A0 | UnloadEGTData | proven | src/gamebryo2.2/corelibs/nimain/nifixedstring_h_unit.cpp: |
| 0x00659B50 | ~BSFaceGenModel | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:603 |

### BSFaceGenModelExtraData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0065BEF0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:1047 |
| 0x0065BE60 | BSFaceGenModelExtraData | proven | src/staging/blk_00640000_od.cpp:5131 |

### BSFaceGenModelMap (13)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0064FDE0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4103 |
| 0x0064FD80 | BSFaceGenModelMap | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:133 |
| 0x00651E70 | ClearEGTData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:2225 |
| 0x00650CB0 | FreeLRUData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4325 |
| 0x00658B80 | FUN_00658b80 | unnamed | src/staging/blk_00640000_od.cpp:570 |
| 0x00650200 | GetAt | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:1814 |
| 0x00650930 | GetTotalDataSize | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:1875 |
| 0x00650780 | KillModelTextureData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3565 |
| 0x00650480 | LoadEGMData | proven | src/staging/blk_00640000_od.cpp:4617 |
| 0x00650630 | LoadEGTData | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:4166 |
| 0x0064FE80 | OutputModelMapContents | proven | src/fallout_shared/magic/effectitemlist.cpp:921 |
| 0x0064FFD0 | SetAt | proven | src/fallout_shared/facegen/bsfacegenmanager.cpp:3514 |
| 0x0064FE10 | ~BSFaceGenModelMap | proven | src/staging/blk_00640000_od.cpp:4492 |

### BSFaceGenModelTextureData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00659A20 | ~BSFaceGenModelTextureData | proven | src/fallout_shared/facegen/bsfacegenmodel.cpp:792 |

### BSFaceGenMorph (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006606B0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:104 |
| 0x00660690 | BSFaceGenMorph | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:82 |
| 0x006606E0 | BSFaceGenMorph | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:206 |

### BSFaceGenMorphData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00661D60 | 'scalar deleting destructor' | proven | src/staging/blk_00660000_od.cpp:279 |
| 0x00661D10 | BSFaceGenMorphData | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:566 |
| 0x0045A120 | DynamicCast | decomp | src/niobject_h_unit.cpp: |
| 0x00508120 | FUN_00508120 | unnamed | src/fallout_shared/facegen/bsfacegenmanager.cpp:3459 |
| 0x00661D40 | ~BSFaceGenMorphData | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:398 |

### BSFaceGenMorphDataHair (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006623A0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:480 |
| 0x006621D0 | BSFaceGenMorphDataHair | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:730 |
| 0x006623D0 | ~BSFaceGenMorphDataHair | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:624 |

### BSFaceGenMorphDataHead (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00661DB0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:426 |
| 0x00662030 | ApplyMorph | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:696 |
| 0x00660BA0 | BSFaceGenMorphDataHead | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:6 |
| 0x00661D90 | GetRTTI | class | src/fallout_shared/facegen/bsfacegenmorphdata_h_unit.cpp:17 |
| 0x00661DE0 | ~BSFaceGenMorphDataHead | proven | src/fallout_shared/facegen/bsfacegenmorphdata.cpp:649 |

### BSFaceGenMorphDifferential (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006607F0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:120 |
| 0x00660860 | ApplyDifferentialMorph | class | src/fallout_shared/facegen/bsfacegenmorph.cpp:40 |
| 0x00660700 | BSFaceGenMorphDifferential | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:19 |
| 0x00660820 | ~BSFaceGenMorphDifferential | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:143 |

### BSFaceGenMorphStatistical (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00660A20 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:163 |
| 0x00660A90 | ApplyDifferentialMorph | class | src/fallout_shared/facegen/bsfacegenmorph.cpp:59 |
| 0x00660970 | BSFaceGenMorphStatistical | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:6 |
| 0x00660A50 | ~BSFaceGenMorphStatistical | proven | src/fallout_shared/facegen/bsfacegenmorph.cpp:186 |

### BSFaceGenNiNode (19)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00662AC0 | 'scalar deleting destructor' | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:250 |
| 0x00662F70 | ApplyFacialCustomMorphs | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1565 |
| 0x00662BC0 | ApplyFacialExpressions | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1406 |
| 0x00662CA0 | ApplyFacialModifiers | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1700 |
| 0x00662E90 | ApplyFacialPhonemes | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:3071 |
| 0x006628C0 | BSFaceGenNiNode | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:2588 |
| 0x00663450 | CheckLOD | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1612 |
| 0x00663B80 | CreateClone | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1096 |
| 0x006629F0 | GetAnimationData | class | src/fallout_shared/facegen/bsfacegenninode.cpp: |
| 0x00662A80 | GetApplyRotToParent | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:306 |
| 0x006629E0 | GetRTTI | class | src/fallout_shared/facegen/bsfacegenninode.cpp: |
| 0x00439920 | SetAnimationData | class | src/fallout_shared/facegen/bsfacegenninode.cpp: |
| 0x00662A60 | SetAnimationUpdate | class | src/fallout_shared/facegen/bsfacegenninode.cpp: |
| 0x0097CE70 | SetApplyRotToParent | class | src/fallout_shared/facegen/bsfacegenninode.cpp: |
| 0x00662B70 | SetBaseRotation | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:1253 |
| 0x00663050 | UpdateAllChildrenMorphData | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:2109 |
| 0x00663510 | UpdateMorphing | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:961 |
| 0x00663AB0 | UpdateTransformAndBounds | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:276 |
| 0x00662B00 | ~BSFaceGenNiNode | proven | src/fallout_shared/facegen/bsfacegenninode.cpp:2486 |

### FaceGenBasisOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00AAD500 | FUN_00aad500 | unnamed | src/staging/blk_00aa0000_od.cpp:2205 |

### FaceGenMatrix<float> (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006588A0 | GetTrace | decomp | src/sdk/facegen/matrixvt_h_unit.cpp: |
| 0x00658360 | operator* | decomp | src/sdk/facegen/matrixvt_h_unit.cpp: |
| 0x006581E0 | operator= | decomp | src/sdk/facegen/matrixvt_h_unit.cpp: |

### FaceGenNpcData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005DD590 | FaceGenNpcData | proven | src/bssystem/console/bsconsolefilecache.cpp:7 |
| 0x005DD6F0 | ~FaceGenNpcData | proven | src/fallout_shared/tesscriptfunctions.cpp:45604 |

### FaceGenPaletteBase (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043DC50 | FUN_0043dc50 | unnamed | src/fallout_shared/modelloader.cpp:5473 |
| 0x00446A10 | FUN_00446a10 | unnamed | src/fallout_shared/modelloader.cpp:6072 |

### FaceGenPaletteEntry (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043EBB0 | ~FaceGenPaletteEntry | decomp | src/fallout_shared/facegen/bsfacegenmanager.cpp:88 |

### FaceGenTriData (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0065A5A0 | FUN_0065a5a0 | unnamed | src/fallout_shared/facegen/bsfacegenmodel.cpp:233 |
| 0x0065C720 | FUN_0065c720 | unnamed | src/fallout_shared/facegen/bsfacegenmodel.cpp:477 |

### QueuedAnimIdle (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043E600 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3497 |
| 0x0043E880 | GetDescription | proven | src/fallout_shared/modelloader.cpp:6383 |
| 0x0043E770 | OnChildCompletion | class | src/fallout_shared/modelloader.cpp:118 |
| 0x0043E7B0 | ProcessLoadedAnimIdle | class | src/fallout_shared/modelloader.cpp:155 |
| 0x0043E580 | QueuedAnimIdle | proven | src/fallout_shared/modelloader.cpp:20339 |

### QueuedKF (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043E180 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:3474 |
| 0x00441E10 | DispatchToManager | decomp | src/fallout_shared/modelloader.cpp:112 |
| 0x0043E550 | GetDescription | proven | src/fallout_shared/modelloader.cpp:6364 |
| 0x0043E0F0 | QueuedKF | proven | src/fallout_shared/modelloader.cpp:4126 |
| 0x0043E210 | QueuedKF | proven | src/fallout_shared/modelloader.cpp:4160 |
| 0x0043E2A0 | Run | proven | src/fallout_shared/modelloader.cpp:7009 |

### QueuedReplacementKF (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043E8F0 | 'scalar deleting destructor' | proven | src/fallout_shared/modelloader.cpp:10216 |
| 0x0043E940 | FUN_0043e940 | class | src/fallout_shared/modelloader.cpp:5941 |
| 0x0043EA00 | GetDescription | proven | src/fallout_shared/modelloader.cpp:5969 |
| 0x0043E9B0 | PostProcess | proven | src/fallout_shared/modelloader.cpp:9695 |
| 0x0043E8B0 | QueuedReplacementKF | proven | src/fallout_shared/modelloader.cpp:11433 |

### QueuedReplacementKFList (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00446A40 | FUN_00446a40 | class | src/fallout_shared/modelloader.cpp:5586 |
| 0x0043EA30 | NotifyChildFinishedPostProcessing | proven | src/fallout_shared/modelloader.cpp:9715 |
| 0x004469C0 | QueuedReplacementKFList | proven | src/fallout_shared/modelloader.cpp:12960 |

### StatsMenu::BodyPartDisplay (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007DB2C0 | BodyPartDisplay | decomp | src/fallout/interface/menus/statsmenu_h_unit.cpp: |

### TESAnimGroup (30)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005F22A0 | 'scalar deleting destructor' | proven | src/fallout_shared/tesanimgroup.cpp:170 |
| 0x005F2370 | AnimGroup | proven | src/fallout_shared/tesanimgroup.cpp:8 |
| 0x005F3870 | FindNextLine | decomp | src/fallout_shared/tesanimgroup.cpp:91 |
| 0x004954E0 | GetBlendIn | proven | src/fallout_shared/animation.cpp:887 |
| 0x00495520 | GetBlendOut | proven | src/fallout_shared/animation.cpp:894 |
| 0x005F23C0 | GetMoveType | decomp | src/fallout_shared/tesanimgroup.cpp:15 |
| 0x005F4C70 | GetSpeed | proven | src/fallout_shared/tesanimgroup.cpp:85 |
| 0x005F3780 | GetTime | proven | src/fallout_shared/tesanimgroup.cpp:212 |
| 0x005F2420 | GetType | probable | src/fallout_shared/tesanimgroup.cpp:27 |
| 0x005F2440 | GetType | proven | src/fallout_shared/tesanimgroup.cpp:21 |
| 0x005F2400 | GetWeapon | proven | src/fallout_shared/tesanimgroup.cpp:384 |
| 0x004937C0 | IsAimAction | proven | src/fallout_shared/animation.cpp:3681 |
| 0x005F2630 | IsAimAction | proven | src/fallout_shared/tesanimgroup.cpp:51 |
| 0x004937E0 | IsAttack | proven | src/fallout_shared/animation.cpp:3695 |
| 0x005F2540 | IsAttackAction | proven | src/fallout_shared/tesanimgroup.cpp:117 |
| 0x005F25A0 | IsAttackAction | proven | src/fallout_shared/tesanimgroup.cpp:34 |
| 0x005F25D0 | IsAttackSpinAction | proven | src/fallout_shared/tesanimgroup.cpp:424 |
| 0x005F4CC0 | IsIdleAnim | proven | src/fallout_shared/tesanimgroup.cpp:496 |
| 0x005F2720 | IsIronSightsAction | proven | src/fallout_shared/tesanimgroup.cpp:412 |
| 0x005F4DB0 | IsJumpingLandAnim | proven | src/staging/blk_005e0000_od.cpp:3264 |
| 0x005F4D60 | IsJumpingLoopAnim | proven | src/fallout_shared/tesanimgroup.cpp:69 |
| 0x005F2670 | IsPowerAttackAction | proven | src/fallout_shared/tesanimgroup.cpp:109 |
| 0x005F2700 | IsReloadAction | proven | src/fallout_shared/tesanimgroup.cpp:401 |
| 0x005F26B0 | IsValidAnimationGroup | decomp | src/fallout_shared/tesanimgroup.cpp:62 |
| 0x005F38D0 | ParseAnimGroupFilename | proven | src/fallout_shared/tesanimgroup.cpp:247 |
| 0x005F2B60 | PlaySounds | proven | src/staging/blk_005e0000_od.cpp:3033 |
| 0x005F4D00 | SetSoundsFromSequence | decomp | src/fallout_shared/tesanimgroup.cpp:136 |
| 0x005F2450 | SetType | proven | src/fallout_shared/tesanimgroup.cpp:304 |
| 0x005F21C0 | TESAnimGroup | proven | src/staging/blk_005e0000_od.cpp:2654 |
| 0x005F22D0 | ~TESAnimGroup | proven | src/fallout_shared/tesanimgroup.cpp:348 |

### (free functions) (24)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00655FA0 | ApplyFaceGenTextures | probable | src/fallout_shared/facegen/bsfacegenmanager.cpp:1379 |
| 0x00706D50 | AttachFaceGenAnimationData | decomp | src/fallout/interface/interface.cpp:1332 |
| 0x00493D50 | CheckAnimGroupMovement | probable | src/fallout_shared/animation.cpp:2496 |
| 0x005EDFB0 | ClearRagdollData | class | src/fallout_shared/bgsragdoll.cpp:585 |
| 0x0050C1D0 | CollectHeadParts | decomp | src/fallout_shared/teslevspell.cpp:443 |
| 0x005FC3A0 | CopyFromEyes | class | src/fallout_shared/teseyes.cpp:198 |
| 0x005FDE80 | CopyFromHair | class | src/fallout_shared/teshair.cpp:158 |
| 0x00BCFB00 | CreateFaceGenMorphShader | decomp | src/staging/blk_00bc0000_o2.cpp:11177 |
| 0x006045F0 | GetFaceGenManagerValue | decomp | src/fallout_shared/tesnpc.cpp:1988 |
| 0x006046A0 | GetHeadPartForm | decomp | src/fallout_shared/tesnpc.cpp:2660 |
| 0x005F23A0 | GetMoveAnimGroup | decomp | src/fallout_shared/tesanimgroup.cpp:364 |
| 0x00651B50 | GetOrCreateFaceGenModel | probable | src/fallout_shared/facegen/bsfacegenmanager.cpp:6204 |
| 0x005E7480 | InitializeHeadPart | class | src/fallout_shared/bgsheadpart.cpp:575 |
| 0x007BF530 | IsEyesListBelowThreshold | decomp | src/fallout/interface/menus/roulettemenu.cpp:191 |
| 0x007AD7F0 | IsHairMatching | decomp | src/fallout/interface/menus/racesexmenu.cpp:7394 |
| 0x005FC220 | LoadEyes | class | src/fallout_shared/teseyes.cpp:310 |
| 0x0077F0D0 | RenderFaceGenScene | decomp | src/fallout/interface/menus/hudmainmenu.cpp:7810 |
| 0x0064A310 | ResetFaceGenAnimationData | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:215 |
| 0x0064A520 | ResetFaceGenData | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:273 |
| 0x00495740 | ResolveAnimGroup | probable | src/fallout_shared/animation.cpp:2699 |
| 0x0048F010 | SetAnimSequence | class | src/fallout_shared/animation.cpp:231 |
| 0x008D4490 | SetRagdoll | class | src/fallout/ai/creature.cpp:121 |
| 0x0064B630 | UpdateFaceGenAnimation | class | src/fallout_shared/facegen/bsfacegenanimationdata.cpp:716 |
| 0x00663A70 | UpdateFaceGenNode | class | src/fallout_shared/facegen/bsfacegenninode.cpp:102 |

## 11 Cells and world loading (where NPCs live)

Grid and cell loading that decides which NPCs are loaded at all.

### BGSCellNumericIDArrayMap (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00852840 | 'scalar deleting destructor' | proven | src/fallout/misc/saveload/bgssaveloadreferencesmap.cpp:121 |
| 0x00852810 | BGSCellNumericIDArrayMap | proven | src/fallout/misc/saveload/bgssaveloadreferencesmap.cpp:170 |
| 0x008528D0 | Clear | decomp | src/fallout/misc/saveload/bgssaveloadreferencesmap.cpp:27 |
| 0x00852870 | ~BGSCellNumericIDArrayMap | proven | src/fallout/misc/saveload/bgssaveloadreferencesmap.cpp:405 |

### BGSReconstructCellBlocksMap (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00841A30 | 'scalar deleting destructor' | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:638 |
| 0x00841B20 | AddCellForm | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:1915 |
| 0x008419F0 | BGSReconstructCellBlocksMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:624 |
| 0x00841A60 | ~BGSReconstructCellBlocksMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:2400 |

### BGSReconstructCellsMap (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00841370 | 'scalar deleting destructor' | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:324 |
| 0x00841460 | AddCellForm | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:3788 |
| 0x00841340 | BGSReconstructCellsMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:528 |
| 0x008413A0 | ~BGSReconstructCellsMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:2070 |

### BGSReconstructCellSubBlocksMap (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008416F0 | 'scalar deleting destructor' | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:342 |
| 0x008416C0 | BGSReconstructCellSubBlocksMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:573 |
| 0x00841990 | HasCellWithFlag | decomp | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:589 |
| 0x00841720 | ~BGSReconstructCellSubBlocksMap | proven | src/fallout/misc/saveload/bgsreconstructformsinallfilesmap.cpp:2101 |

### CellLoad::Cell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00554FD0 | LoadChanged | class | src/fallout_shared/tesobjectcell.cpp:16039 |

### ExteriorCellLoaderTask (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00527C40 | 'scalar deleting destructor' | proven | src/fallout_shared/exteriorcellloader.cpp:423 |
| 0x00527C00 | ExteriorCellLoaderTask | proven | src/staging/blk_00520000_od.cpp:537 |
| 0x00527CE0 | FUN_00527ce0 | unnamed | src/fallout_shared/exteriorcellloader.cpp:16 |
| 0x00527D00 | PostProcess | proven | src/fallout_shared/exteriorcellloader.cpp:252 |
| 0x00527CB0 | Run | proven | src/fallout_shared/exteriorcellloader.cpp:235 |
| 0x00527C70 | ~ExteriorCellLoaderTask | proven | src/fallout_shared/exteriorcellloader.cpp:117 |

### GridArray (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004B9E20 | 'scalar deleting destructor' | proven | src/fallout_shared/gridarray.cpp:55 |
| 0x004B9EB0 | DetachAllCells | class | src/fallout_shared/gridarray.cpp:36 |
| 0x004B9E00 | GridArray | proven | src/staging/blk_004a0000_od.cpp:672 |
| 0x004B9E50 | GridArray | proven | src/fallout_shared/gridarray.cpp:71 |
| 0x004B9E70 | Init | class | src/fallout_shared/gridarray.cpp:29 |

### GridCellArray (13)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004BA3D0 | 'scalar deleting destructor' | proven | src/fallout_shared/gridcell.cpp:384 |
| 0x004BA7D0 | AttachAllLand3D | proven | src/fallout_shared/gridcell.cpp:735 |
| 0x004BA960 | AttachToWorld | proven | src/fallout_shared/gridcell.cpp:502 |
| 0x004BAEC0 | ClearCanopyShadowMaskTexture | proven | src/fallout_shared/gridcell.cpp:153 |
| 0x004BA6B0 | Detach | class | src/fallout_shared/gridcell.cpp:72 |
| 0x004BA5A0 | GetAttached | proven | src/fallout_shared/gridcell.cpp:305 |
| 0x004BA490 | GetCell | proven | src/fallout_shared/gridcell.cpp:62 |
| 0x004BA280 | GridCellArray | proven | src/staging/blk_004a0000_od.cpp:3349 |
| 0x004BA5E0 | Init | class | src/fallout_shared/gridcell.cpp:54 |
| 0x004BA8D0 | ReleaseGridCells | probable | src/fallout_shared/gridcell.cpp:83 |
| 0x004BACA0 | ShowLandBorders | proven | src/fallout_shared/gridcell.cpp:686 |
| 0x004BAD40 | ToggleCollisionGeometry | proven | src/fallout_shared/gridcell.cpp:564 |
| 0x004BA400 | ~GridCellArray | proven | src/fallout_shared/gridcell.cpp:880 |

### TES (29)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0045CDA0 | ActivateAllSubmergedReferencesIslands | proven | src/fallout_shared/tes.cpp:7097 |
| 0x004539A0 | ClearAllCells | proven | src/fallout_shared/tes.cpp:8318 |
| 0x00453A80 | ClearOldestBufferedCell | proven | src/fallout_shared/tes.cpp:8382 |
| 0x00450DD0 | CullGridCells | proven | src/fallout_shared/tes.cpp:11139 |
| 0x00459000 | FindActorBaseValue | decomp | src/fallout_shared/tes.cpp:3858 |
| 0x004516D0 | FindFirstGridCellWithWater | proven | src/fallout_shared/tes.cpp:7413 |
| 0x004519D0 | GetCellForPoint | proven | src/fallout_shared/tes.cpp:11203 |
| 0x00458BE0 | GetCellPriority | proven | src/unmapped/rlog_client.cpp:66 |
| 0x00457070 | GetCurrentCell | proven | src/fallout_shared/tes.cpp:3439 |
| 0x00457050 | GetGridCell | proven | src/staging/blk_00440000_od.cpp:666 |
| 0x00451900 | GetGridCellCell | proven | src/fallout_shared/tes.cpp:4421 |
| 0x00452FF0 | GridArrayLoad | proven | src/fallout_shared/tes.cpp:8127 |
| 0x004515A0 | InitGridCells | proven | src/fallout/ai/playercharacter.cpp:1272 |
| 0x004511E0 | IsCellLoaded | proven | src/fallout_shared/tes.cpp:5107 |
| 0x00451110 | IsCoordInLoadedArea | proven | src/fallout_shared/tes.cpp:10896 |
| 0x00451530 | IsRunningCellTests | proven | src/fallout_shared/tes.cpp:2277 |
| 0x00451A50 | LoadGridCell | proven | src/fallout_shared/tes.cpp:4097 |
| 0x00453DC0 | LoadInterior | proven | src/fallout_shared/tes.cpp:8886 |
| 0x00459F10 | PreloadAddonNodes | proven | src/fallout_shared/tes.cpp:10331 |
| 0x004512C0 | ReloadGridCells | proven | src/fallout_shared/tes.cpp:7359 |
| 0x00459AE0 | RunCellTest | proven | src/fallout_shared/tes.cpp:10229 |
| 0x00456D00 | ShowCellNode | proven | src/fallout_shared/tes.cpp:9625 |
| 0x00457D70 | ShowLoadingMenu | proven | src/fallout_shared/tes.cpp:11278 |
| 0x004556D0 | TestAllCells | proven | src/fallout_shared/tes.cpp:11647 |
| 0x00459D20 | TestCell | proven | src/fallout_shared/tes.cpp:4876 |
| 0x00453550 | UpdateCellAnimations | proven | src/fallout_shared/tes.cpp:4221 |
| 0x00452580 | UpdateCurrentGridCell | proven | src/fallout_shared/teswater.cpp:17 |
| 0x00451CF0 | UpdateGridLights | proven | src/fallout_shared/tes.cpp:4388 |
| 0x00455690 | UpdateRefSounds | proven | src/fallout_shared/tes.cpp:3048 |

### TESObjectCELL (66)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005452C0 | AddAnimatedRef | proven | src/fallout_shared/tesobjectcell.cpp:825 |
| 0x005453B0 | AddEmittanceRef | proven | src/fallout_shared/tesobjectcell.cpp:20714 |
| 0x00548230 | AddReference | proven | src/fallout_shared/tesobjectcell_rtti_variant.cpp:413 |
| 0x00548740 | AddReferenceSimple | proven | src/fallout_shared/tesobjectcell.cpp:7251 |
| 0x00557470 | AddReferencesToLoadedReferenceCollection | proven | src/fallout_shared/tesobjectcell.cpp:188 |
| 0x00555630 | AppendSaveLoadFormBuffer | proven | src/fallout_shared/tesobjectcell.cpp:7587 |
| 0x0054C8C0 | AssignPersistentRefsToCellsInWorld | proven | src/fallout_shared/tesobjectcell.cpp:13799 |
| 0x0054BA80 | AttachLights | proven | src/fallout_shared/tesobjectcell.cpp:20864 |
| 0x0054BCF0 | AttachModels | proven | src/fallout_shared/tesobjectcell_rtti2_variant.cpp:247 |
| 0x00548880 | AttachReference3D | proven | src/fallout_shared/tesobjectcell.cpp:17814 |
| 0x0054B950 | AttachSounds | proven | src/fallout_shared/tesobjectcell.cpp:1314 |
| 0x00552970 | AttachToWorld | proven | src/fallout_shared/tesobjectcell.cpp:18729 |
| 0x00550C60 | CalcLeveledCreatures | proven | src/fallout_shared/tesobjectcell.cpp:4570 |
| 0x0054C030 | CalcRefCenterPoint | proven | src/fallout_shared/tesobjectcell.cpp:13545 |
| 0x00541AC0 | CellRefLockEnter | proven | src/fallout_shared/tesobjectcell.cpp:47 |
| 0x00541AE0 | CellRefLockLeave | proven | src/fallout_shared/tesobjectrefr.cpp:772 |
| 0x0054B750 | ClearReference3D | proven | src/fallout_shared/tesobjectcell.cpp:13250 |
| 0x0054CD20 | ClearRefList | proven | src/fallout_shared/tesobjectcell.cpp:14009 |
| 0x00544CE0 | CreateLoadedData | proven | src/fallout_shared/tesobjectcell_ctx_variant.cpp:249 |
| 0x00551180 | CreateLootBagAtRef | proven | src/fallout_shared/tesobjectrefr.cpp:17619 |
| 0x00552BD0 | Detach | proven | src/fallout_shared/tesobjectcell.cpp:9504 |
| 0x0054DA20 | EnumReferencesCloseToPoint | proven | src/fallout_shared/tesobjectcell.cpp:21133 |
| 0x00550E10 | FindReferenceInFile | proven | src/fallout_shared/tesobjectcell.cpp:15204 |
| 0x00546AF0 | GetDetachTime | proven | src/fallout_shared/tesobjectcell.cpp:993 |
| 0x00546C20 | GetEncounterZone | proven | src/fallout_shared/tesobjectcell.cpp:146 |
| 0x0054CEE0 | GetFirstRefr | proven | src/fallout_shared/tesobjectcell.cpp:20963 |
| 0x0054CF20 | GetFirstRefr | proven | src/fallout_shared/tesobjectcell.cpp:14078 |
| 0x00526100 | GetHoursToRespawnCell | proven | src/bgsencounterzone.cpp:321 |
| 0x00551620 | GetLowestProcessMiddleLow | proven | src/fallout_shared/tesobjectcell.cpp:30 |
| 0x00546A40 | GetOwner | proven | src/fallout_shared/tesobjectcell.cpp:159 |
| 0x00546AA0 | GetOwnershipGlobal | proven | src/fallout_shared/tesobjectcell.cpp:980 |
| 0x00546AC0 | GetOwnershipRank | proven | src/fallout_shared/extradatalist.cpp:5563 |
| 0x009604F0 | GetRefList | proven | src/fallout_shared/tesobjectcell.cpp:2583 |
| 0x00545710 | GetWaterRefList | proven | src/fallout_shared/tesobjectcell.cpp:845 |
| 0x0054DF30 | HandleExpiredReferences | proven | src/fallout_shared/tesobjectcell_iso_variant.cpp:334 |
| 0x005559D0 | InitLoadGame | proven | src/fallout_shared/tesobjectcell.cpp:22711 |
| 0x00546EE0 | IsActorBaseCellOwner | proven | src/fallout_shared/tesobjectcell.cpp:22646 |
| 0x00546CA0 | IsActorCellOwner | proven | src/fallout_shared/tesobjectcell.cpp:22566 |
| 0x00546DA0 | IsActorTrespassing | proven | src/fallout_shared/tesobjectcell.cpp:23423 |
| 0x00450FF0 | IsAttached | proven | src/staging/blk_00440000_od.cpp:469 |
| 0x004523C0 | IsAttaching | proven | src/fallout_shared/tes.cpp:610 |
| 0x00450FB0 | IsLoaded | proven | src/staging/blk_00440000_od.cpp:450 |
| 0x00548720 | IsLoading | proven | src/fallout_shared/tesobjectcell.cpp:1152 |
| 0x00557090 | IsRefListLocked | proven | src/fallout_shared/tes.cpp:3477 |
| 0x005422D0 | Load | proven | src/fallout_shared/tesobjectcell_ctx2_variant.cpp:478 |
| 0x00545CF0 | Load3D | proven | src/fallout_shared/tesobjectcell.cpp:11360 |
| 0x00550340 | LoadAllTempData | proven | src/fallout_shared/tesobjectcell.cpp:5517 |
| 0x00555740 | LoadGame | proven | src/fallout_shared/tesobjectcell.cpp:4948 |
| 0x00550500 | LoadTempDataFromFile | proven | src/fallout_shared/tesobjectcell.cpp:18503 |
| 0x005496B0 | PerformCellNodeAttach | proven | src/fallout_shared/tesobjectcell.cpp:2761 |
| 0x0054AE30 | PerformQueuedChildAttaches | proven | src/fallout_shared/tesobjectcell.cpp:4159 |
| 0x005577B0 | ProcessAddonNodesForRefs | proven | src/fallout_shared/tesobjectcell.cpp:21568 |
| 0x0054ABD0 | QueueAttachChild | proven | src/fallout_shared/tesobjectcell.cpp:21648 |
| 0x005571A0 | QueueReferences | proven | src/fallout_shared/tesobjectcell_decl_variant.cpp:32 |
| 0x00558BA0 | RemoveAutoWaterReferenceFromReferencesCurrentWater | proven | src/fallout_shared/tesobjectcell.cpp:5591 |
| 0x005454F0 | RemoveEmittanceRef | proven | src/fallout_shared/tesobjectcell.cpp:8122 |
| 0x0054CA90 | RemoveReference | proven | src/fallout_shared/tesobjectcell.cpp:18374 |
| 0x005574D0 | RemoveReferencesFromLoadedReferenceCollection | proven | src/fallout_shared/tesobjectcell.cpp:19056 |
| 0x00542040 | SaveReferences | proven | src/fallout_shared/tesobjectcell.cpp:10659 |
| 0x00554A20 | SetActorCollisionGeometry | proven | src/staging/blk_00540000_od.cpp:2549 |
| 0x00546B10 | SetDetachTime | proven | src/fallout_shared/tesobjectcell.cpp:6852 |
| 0x00546C70 | SetDetachTime | proven | src/fallout_shared/tesobjectcell.cpp:3743 |
| 0x00551480 | SetLowestProcessToMiddleLow | proven | src/fallout_shared/tesobjectcell_rtti_variant.cpp:971 |
| 0x005508B0 | UnLoadAllTempData | proven | src/unmapped/as_object.cpp:191 |
| 0x0054BC10 | UpdateReferences3DandProcess | proven | src/fallout_shared/tesobjectcell.cpp:13340 |
| 0x005538E0 | UpdateRefSounds | proven | src/fallout_shared/tesobjectcell.cpp:18964 |

### TESWorldSpace (27)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00587670 | AddCell | proven | src/fallout_shared/tesworldspace.cpp:418 |
| 0x005878D0 | AddMultiBoundRef | proven | src/fallout_shared/tesworldspace.cpp:4519 |
| 0x00587FF0 | AddPersistentRef | proven | src/fallout_shared/tesworldspace.cpp:43 |
| 0x00587D10 | AddToPersistentRefData | proven | src/fallout_shared/tesworldspace.cpp:4934 |
| 0x00588150 | AssignPersistentRefsToCell | proven | src/fallout_shared/tesworldspace.cpp:1729 |
| 0x005877E0 | ClearCellMap | proven | src/fallout_shared/tesworldspace.cpp:2156 |
| 0x00587BB0 | ClearMultiBoundRefs | proven | src/fallout_shared/tesworldspace.cpp:1398 |
| 0x00587F40 | ClearPersistentRefData | proven | src/fallout_shared/distant terrain system/bgsterrainmanager.cpp:506 |
| 0x00586480 | ClearWorldSpaceReferences | decomp | src/fallout_shared/tesworldspace.cpp:78 |
| 0x00588070 | CreatePersistentCell | proven | src/fallout_shared/tesworldspace.cpp:533 |
| 0x005885F0 | EnumReferencesCloseToPoint | proven | src/fallout_shared/tesworldspace.cpp:3673 |
| 0x005854F0 | FindCellInFile | proven | src/fallout_shared/tesworldspace.cpp:2028 |
| 0x00588560 | GetCellByEditorID | proven | src/fallout_shared/tesworldspace.cpp:1887 |
| 0x005875A0 | GetCellFromCellCoord | proven | src/fallout_shared/tesworldspace.cpp:91 |
| 0x00587630 | GetCellFromKey | proven | src/fallout_shared/tesworldspace.cpp:34 |
| 0x00587550 | GetCellFromWorldCoord | proven | src/fallout_shared/tesworldspace.cpp:793 |
| 0x00585940 | GetExtCellDataFromFileByEditorID | proven | src/fallout_shared/tesworldspace.cpp:2913 |
| 0x00584530 | GetIndexForCellCoord | proven | src/fallout_shared/tesworldspace.cpp:970 |
| 0x00587410 | GetKeyForCellCoord | proven | src/fallout_shared/tesworldspace.cpp:172 |
| 0x00587870 | GetOverlappedMultiBoundRefs | proven | src/fallout_shared/tesworldspace.cpp:1097 |
| 0x00587C80 | IsFixedRef | proven | src/fallout_shared/tesworldspace.cpp:243 |
| 0x00583560 | Load | proven | src/fallout_shared/tesworldspace.cpp:4128 |
| 0x00585B30 | LoadCell | proven | src/fallout_shared/tesworldspace.cpp:3159 |
| 0x00587760 | ReleaseCell | proven | src/fallout_shared/tesworldspace.cpp:1058 |
| 0x00587E40 | RemoveFromPersistentRefData | proven | src/fallout_shared/tesworldspace.cpp:479 |
| 0x00588030 | RemovePersistentRef | proven | src/fallout_shared/tesworldspace.cpp:280 |
| 0x00585E00 | UnLoadCell | proven | src/fallout_shared/tesobjectcell.cpp:10114 |

## 12 Other code in the AI source files

Functions that live in src/fallout/ai/ but whose names did not place them in a group above (mostly decomp or unnamed). Worth a look; many are NPC logic without a good name yet.

### A_00886b30 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00886B30 | PlaceAtPosition | decomp | src/fallout/ai/actor.cpp:22304 |

### AA10Menu (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099AA10 | HandleMenuEvent | decomp | src/fallout/ai/combat/combatstate.cpp:4060 |

### acquire907_rework::Proc907 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00907D90 | FUN_00907d90 | class | src/fallout/ai/lowprocess_rtm_variant.cpp:274 |

### AcquireProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00909430 | FUN_00909430 | class | src/fallout/ai/lowprocess.cpp:11954 |

### AcquireSortProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091B640 | FUN_0091b640 | unnamed | src/fallout/ai/middlehighprocess_rtm_variant.cpp:31 |

### AcquisitionProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E2B00 | ProcessAcquisitionEntries | class | src/fallout/ai/highprocess.cpp:61378 |

### Act_S (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C3650 | GetSequenceValue | decomp | src/fallout/ai/actor.cpp:30979 |

### ActH2 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A5F20 | FUN_008a5f20 | probable | src/fallout/ai/actor.cpp:134705 |

### ActivateProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091FB30 | ActivatePackageTarget | class | src/fallout/ai/middlehighprocess.cpp:21872 |

### ActivationProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091D810 | CheckActivationTarget | decomp | src/fallout/ai/middlehighprocess.cpp:19389 |

### ActivitySelector (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F3E80 | SelectActivity | decomp | src/fallout/ai/sandboxpackage.cpp:1850 |

### Actor467 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A2D40 | FUN_008a2d40 | probable | src/fallout/ai/actor.cpp:67255 |

### Actor8 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00894940 | UpdateAnimGroupState | decomp | src/fallout/ai/actor.cpp:61024 |

### Actor87 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B87A0 | FUN_008b87a0 | probable | src/fallout/ai/actor.cpp:81912 |

### Actor88 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B150 | UpdateNodeTransform | decomp | src/fallout/ai/actor.cpp:56441 |

### Actor884750 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884750 | FUN_00884750 | unnamed | src/fallout/ai/movement/actormover.cpp:6680 |

### Actor897 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00897BD0 | FUN_00897bd0 | probable | src/fallout/ai/backuppackage.cpp:825 |

### Actor8C1 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C1D20 | EquipPlayableObject | class | src/fallout/ai/actor_magic.cpp:4147 |

### Actor8c37 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C3790 | UpdateAnimationState | decomp | src/fallout/ai/actor_magic.cpp:5019 |

### Actor8c39 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C39B0 | AttachMagicEffect | decomp | src/fallout/ai/actor_magic.cpp:5220 |

### Actor8d2800 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D2800 | TryStartFurnitureUse | class | src/fallout/ai/actor.cpp:91702 |

### Actor9B4 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B4460 | FUN_009b4460 | class | src/fallout/ai/combat/grenadeprojectile_o2_variant_od_oy_noo2_variant.cpp:412 |

### Actor_008acc80 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ACC80 | FUN_008acc80 | probable | src/fallout/ai/actor.cpp:46393 |

### Actor_008be180 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE180 | SendToProcess | class | src/fallout/ai/actor.cpp:14550 |

### ActorAddSpell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C32F0 | AddSpellToActor | class | src/fallout/ai/actor_magic.cpp:4690 |

### ActorAnimation (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009462C0 | FUN_009462c0 | probable | src/fallout/ai/playercharacter.cpp:15499 |

### ActorAvoidanceDataArray (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00983720 | FUN_00983720 | unnamed | src/fallout/ai/movement/detailedactorpathhandler.cpp:4603 |

### ActorBestWeapon_d (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891C80 | FUN_00891c80 | class | src/fallout/ai/actor.cpp:145050 |

### ActorBF (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BF7B0 | FUN_008bf7b0 | probable | src/fallout/ai/character.cpp:2966 |

### ActorCellInitView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A82E0 | FUN_008a82e0 | class | src/fallout/ai/actor.cpp:145591 |

### ActorConsumeShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C2090 | FUN_008c2090 | probable | src/fallout/ai/actor_magic.cpp:8125 |

### ActorCreatureStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D4750 | FUN_008d4750 | class | src/fallout/ai/actor_magic_rtti2_variant.cpp: |

### ActorD (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B6820 | UpdateDismemberedLimbs | decomp | src/fallout/ai/actor.cpp:80503 |

### ActorData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A8060 | EnableActionResourceIfLowState | decomp | src/fallout/ai/actor.cpp:71155 |

### ActorGoldQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891D70 | FUN_00891d70 | probable | src/fallout/ai/actor.cpp:149213 |

### ActorGroupOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00904C80 | CanAddActorToGroup | class | src/fallout/ai/highprocess.cpp:25644 |

### ActorH (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AE000 | FUN_008ae000 | probable | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:2639 |

### ActorHelper (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B2C30 | FUN_008b2c30 | class | src/fallout/ai/actor.cpp:100009 |

### ActorInventoryQueryViews::ActorQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891DB0 | FUN_00891db0 | probable | src/fallout/ai/actor.cpp:145076 |

### ActorMagicQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BCDA0 | GetMagicProcessValue | decomp | src/fallout/ai/actor.cpp:88065 |

### ActorMergeData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00987530 | MergeFrom | decomp | src/fallout/ai/combat/combatgroup.cpp:6389 |

### ActorMovement::Mover (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DE490 | SetEnabled | decomp | src/fallout/ai/movement/actormover.cpp:5266 |

### ActorMover_Standin (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DDC00 | FUN_009ddc00 | probable | src/fallout/ai/movement/actormover.cpp:6815 |

### ActorMoverBuildPath14 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DB090 | FUN_009db090 | probable | src/fallout/ai/movement/actormover.cpp:7482 |

### ActorMoverX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DC5E0 | HandlePathResult | decomp | src/fallout/ai/movement/actormover.cpp:4358 |

### ActorNodeLoader (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D4210 | FUN_008d4210 | class | src/fallout/ai/actor.cpp:93646 |

### ActorPicker (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00986C60 | SelectActor | decomp | src/fallout/ai/combat/combatgroup.cpp:10412 |

### ActorProxy (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008808A0 | FUN_008808a0 | probable | src/fallout/ai/actor.cpp:35556 |
| 0x0087F510 | HasNoRumors | decomp | src/fallout/ai/actor.cpp:35025 |

### ActorProxyFnv (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008EC460 | HandleActorInteraction | class | src/fallout/ai/highprocess.cpp:38990 |

### ActorQueryOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009719E0 | FindDialogueSpeakers | decomp | src/fallout/ai/processlists.cpp:12127 |

### ActorReader (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00894F90 | SetAnimationGroupFromFlags | decomp | src/fallout/ai/actor.cpp:62232 |

### ActorResetView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AA210 | FUN_008aa210 | unnamed | src/fallout/ai/actor.cpp:139610 |

### ActorS_008ac6f0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AC6F0 | FUN_008ac6f0 | probable | src/fallout/ai/actor.cpp:41315 |

### ActorSave (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A9380 | SaveActorData | class | src/fallout/ai/actor.cpp:72470 |

### ActorSoundStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ADED0 | PlayActorSound | decomp | src/fallout/ai/processlists.cpp:8829 |

### ActorSoundView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3230 | FUN_008b3230 | rejected | src/fallout/ai/actor.cpp:79202 |

### ActorStand (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00880FB0 | FUN_00880fb0 | class | src/fallout/ai/actor.cpp:50293 |

### ActorStandIn (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B38D0 | BuildPathingRequest | decomp | src/fallout/ai/actor.cpp:44142 |
| 0x0093AD30 | FUN_0093ad30 | unnamed | src/fallout/ai/actor_magic.cpp:5746 |
| 0x0093AD60 | FUN_0093ad60 | unnamed | src/fallout/ai/actor_magic.cpp:5822 |
| 0x008B9B70 | GetActorValueAndSyncProcess | decomp | src/fallout/ai/actor.cpp:109946 |
| 0x008B6DF0 | RemoveLimb | decomp | src/fallout/ai/actor.cpp:45167 |
| 0x008CDBF0 | UpdateProcessLevel | class | src/fallout/ai/mobileobject.cpp:9010 |

### ActorStandIn008a (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A61B0 | FUN_008a61b0 | probable | src/fallout/ai/actor.cpp:115220 |

### ActorStub (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089F500 | FUN_0089f500 | unnamed | src/fallout/ai/actor.cpp:33235 |
| 0x008C3530 | FUN_008c3530 | unnamed | src/fallout/ai/actor.cpp:125478 |
| 0x008AFF80 | GetCameraPosAndDir | decomp | src/fallout/ai/actor.cpp:74256 |
| 0x008A5340 | GetNodePosition | decomp | src/fallout/ai/actor.cpp:69333 |
| 0x0089F580 | TryMakeTargetThing | decomp | src/fallout/ai/actor.cpp:65866 |

### ActorUpdateShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A3100 | FUN_008a3100 | class | src/fallout/ai/actor.cpp:107562 |

### ActorV_S (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A5D10 | UpdateActorState | class | src/fallout/ai/actor.cpp:27182 |

### ActorView (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A89A0 | ConsumeAmmo | class | src/fallout/ai/actor.cpp:71933 |
| 0x00884320 | FUN_00884320 | probable | src/fallout/ai/actor.cpp:33876 |

### ActorX_S (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A46C0 | GetDetectionFactor | decomp | src/fallout/ai/actor.cpp:26771 |

### ActorY (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00885D90 | FUN_00885d90 | probable | src/fallout/ai/actor.cpp:55213 |

### AgentActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00883240 | ResetAIProcess | class | src/fallout/ai/actor.cpp:52606 |

### AHActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A3C50 | UpdateHandlerState | class | src/fallout/ai/actor.cpp:68060 |

### AIActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F31D0 | CheckTargetAndCombat | decomp | src/fallout/ai/highprocess.cpp:43762 |

### AimPlayer (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009445B0 | FUN_009445b0 | probable | src/fallout/ai/playercharacter.cpp:14652 |
| 0x00965620 | UpdateAim | decomp | src/fallout/ai/playercharacter.cpp:47496 |

### AimProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009295C0 | UpdateAimTurn | class | src/fallout/ai/middlehighprocess.cpp:28187 |

### AITaskThreadManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9AE0 | AddThread | proven | src/fallout/ai/aitaskmanager.cpp:1004 |

### AlignOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AB160 | UpdateAlignment | class | src/fallout/ai/combat/continuousbeamprojectile.cpp:1111 |

### AngleView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00936DA0 | GetAdjustedAngle | decomp | src/fallout/ai/mobileobject.cpp:8464 |

### ArmorProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092BAA0 | UpdatePowerArmorState | class | src/fallout/ai/middlehighprocess.cpp:29897 |

### ArrayProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A32A0 | FUN_009a32a0 | unnamed | src/fallout/ai/combat/combatstate.cpp:4743 |

### ArrowProjectile (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CDDD0 | DeleteAttachedArrows | proven | src/fallout/ai/arrowprojectile.cpp:627 |

### AssignedCharacter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D2A80 | FUN_008d2a80 | class | src/fallout/ai/character.cpp:3625 |

### AutoFireProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929DF0 | UpdateAutoFire | class | src/fallout/ai/middlehighprocess.cpp:28830 |

### AvActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00880370 | FUN_00880370 | probable | src/fallout/ai/actor.cpp:113523 |

### AvoidancePackage_1440 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F1440 | BuildAvoidNodeArray | decomp | src/fallout/ai/fleepackage.cpp:1776 |

### AvoidHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E5AE0 | UpdateAvoidance | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:8890 |

### AvoidWork (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009895A0 | BuildAvoidNodes | decomp | src/fallout/ai/combat/combatgroup.cpp:3609 |

### B17A0Ref (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B17A0 | Update3D | decomp | src/fallout/ai/combat/explosion.cpp:2031 |

### B4E10Outer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C4E10 | CreateAndApplyEffect | decomp | src/fallout/ai/actor.cpp:90913 |

### B5474B0Cell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005474B0 | FUN_005474b0 | probable | src/fallout/ai/actor.cpp:46629 |

### B570ProcessCalls (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092B570 | UpdateTargetTracking | class | src/fallout/ai/middlehighprocess.cpp:29732 |

### B5725B0Form (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005725B0 | FUN_005725b0 | class | src/fallout/ai/mobileobject.cpp:7377 |

### B63E00Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00963E00 | FUN_00963e00 | unnamed | src/fallout/ai/playercharacter.cpp:45839 |

### B6FF0Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B6FF0 | CollectLimbBones | decomp | src/fallout/ai/actor.cpp:80675 |

### B87F200Projectile (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087F200 | FUN_0087f200 | probable | src/fallout/ai/actor.cpp:47899 |

### B88B5A0Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B5A0 | ApplyFatigueDamage | decomp | src/fallout/ai/actor.cpp:56816 |

### B88B7F0Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B7F0 | GetPackageTypeName | decomp | src/fallout/ai/actor.cpp:57018 |

### B8C4890Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C4890 | SetProcessValue | decomp | src/fallout/ai/actor_magic.cpp:1397 |

### B8EB30Group (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EB30 | RemoveActorsNotInGroup | decomp | src/fallout/ai/combat/combatgroup.cpp:5773 |

### B8F6820Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F6820 | FUN_008f6820 | class | src/fallout/ai/highprocess.cpp:18567 |

### B930700Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00930700 | SetParentCellAndUpdateController | class | src/fallout/ai/actor.cpp:93928 |

### B989230Tracker (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989230 | UpdateEntryFromRef | decomp | src/fallout/ai/combat/combatgroup.cpp:3556 |

### B989700List (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989700 | FindRefInRadius | decomp | src/fallout/ai/combat/combatgroup.cpp:10552 |

### B9898B0Group (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009898B0 | FindClosestRef | decomp | src/fallout/ai/combat/combatgroup.cpp:10576 |

### B98EBC0Array (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EBC0 | GetElementAt | decomp | src/fallout/ai/combat/combatgroup.cpp:5798 |

### B9C10Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B9C10 | UpdateControllerValue | decomp | src/fallout/ai/actor.cpp:82606 |

### B_008b3630 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3630 | SetPathingRequestAvoidNodes | decomp | src/fallout/ai/actor.cpp:9944 |

### BackUpPackageProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EDB90 | LoadGameWithBackup | class | src/fallout/ai/backuppackage.cpp:77 |

### BarkPlaybackEntry (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D5BC0 | UpdateBarks | decomp | src/fallout/ai/followerbarks.cpp:5 |

### BaseA8 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008847C0 | FUN_008847c0 | unnamed | src/fallout/ai/actor.cpp:113770 |

### BaseProcessCall (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BA050 | SetEndurance | decomp | src/fallout/ai/actor.cpp:11543 |

### BaseProcessHelper (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884CE0 | SetWalkSpeed | decomp | src/fallout/ai/actor.cpp:3347 |

### BaseProcessShell909320 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00909320 | InitWornForms | class | src/fallout/ai/lowprocess.cpp:6891 |

### BE350Menu (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE350 | FUN_008be350 | rejected | src/fallout/ai/actor.cpp:88285 |

### BeamProjectile (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00979840 | FindBeamGeometryLength | proven | src/fallout/ai/combat/beamprojectile.cpp:1739 |
| 0x009ABF10 | FUN_009abf10 | unnamed | src/fallout/ai/combat/beamprojectile.cpp:61 |
| 0x009B4CF0 | FUN_009b4cf0 | unnamed | src/fallout/ai/combat/beamprojectile.cpp:78 |
| 0x009BAB00 | FUN_009bab00 | unnamed | src/fallout/ai/combat/beamprojectile.cpp:97 |
| 0x009795E0 | ScaleBeamGeometryLength | proven | src/fallout/ai/combat/beamprojectile.cpp:255 |
| 0x00979330 | UpdateProjectile | proven | src/fallout/ai/combat/projectile.cpp:3358 |

### BehaviorUpdate::Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F9320 | FUN_008f9320 | class | src/fallout/ai/highprocess.cpp:47567 |

### BGSExplosion (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AC550 | GetImageSpaceRadiusBSUnits | proven | src/fallout/ai/combat/explosion.cpp:1063 |
| 0x009AD5A0 | GetScaledValue | decomp | src/fallout/ai/combat/explosion.cpp:585 |

### BGSImpactData (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004A4140 | GetAlphaBlending | proven | src/fallout/ai/actor.cpp:33600 |
| 0x004A4180 | GetAlphaTesting | proven | src/fallout/ai/actor.cpp:33616 |
| 0x004A4220 | GetDecalColor | proven | src/fallout/ai/actor.cpp:32783 |
| 0x008AFF10 | GetDecalDepth | proven | src/fallout/ai/actor.cpp:33334 |
| 0x004A41E0 | GetDecalParallaxPasses | proven | src/fallout/ai/actor.cpp:33632 |
| 0x004A41C0 | GetDecalParallaxScale | proven | src/fallout/ai/actor.cpp:34868 |
| 0x004A40E0 | GetDecalShininess | proven | src/fallout/ai/actor.cpp:34848 |
| 0x004A4100 | GetIsParallax | proven | src/fallout/ai/actor.cpp:33584 |

### BGSProjectile (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966980 | GetGravity | proven | src/fallout/ai/combat/combatutilities.cpp:349 |
| 0x00975300 | GetHasExplosionAltTrigger | decomp | src/fallout/ai/processlists.cpp:26 |
| 0x009BAF30 | GetHasMuzzleFlash | proven | src/fallout/ai/combat/muzzleflash.cpp:16 |
| 0x009A7F80 | GetHitScan | proven | src/fallout/ai/combat/combatutilities.cpp:61 |
| 0x009BC870 | GetSupersonic | proven | src/fallout/ai/combat/projectile.cpp:419 |
| 0x009C2E60 | IsFlag200Set | decomp | src/fallout/ai/combat/projectile.cpp:431 |

### BGSSaveLoadManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008512F0 | LoadMostRecentSaveGame | proven | src/fallout/ai/actor.cpp:35003 |

### bhkConstraint (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BA4E0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/missileprojectile.cpp:36 |
| 0x009BA4A0 | bhkConstraint | proven | src/fallout/ai/combat/missileprojectile.cpp:216 |

### bhkFilteredCdBodyCollector (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AFF50 | 'scalar deleting destructor' | proven | src/fallout/ai/actor.cpp:39842 |
| 0x00CB9810 | addCdBodyPair | proven | src/fallout/ai/actor_o2_variant.cpp:1081 |
| 0x008AFF30 | bhkFilteredCdBodyCollector | proven | src/fallout/ai/actor.cpp:34176 |
| 0x00CB9900 | ~bhkFilteredCdBodyCollector | proven | src/fallout/ai/actor_o2_variant.cpp:62 |

### bhkHingeConstraint (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BA520 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/missileprojectile.cpp:114 |
| 0x009BA410 | bhkHingeConstraint | proven | src/fallout/ai/combat/missileprojectile.cpp:1350 |
| 0x00CBDE40 | CreateCinfo | proven | src/fallout/ai/combat/missileprojectile_o2_variant.cpp:529 |
| 0x00CBDD60 | CreateClone | proven | src/fallout/ai/combat/missileprojectile_o2_variant.cpp:295 |

### bhkLiquidAction (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AE250 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/explosion.cpp:188 |
| 0x009AE140 | bhkLiquidAction | proven | src/fallout/ai/combat/explosion.cpp:1107 |
| 0x00CBCAD0 | CreateCinfo | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:693 |
| 0x00CBCA20 | CreateClone | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:420 |
| 0x009AE240 | GetRTTI | class | src/fallout/ai/combat/explosion.cpp:52 |
| 0x00CBD650 | GetViewerStrings | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:651 |
| 0x00CBC650 | LoadBinary | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:273 |
| 0x00CBC6A0 | SaveBinary | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:349 |

### bhkPickData (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004585F0 | GetFrom | proven | src/fallout/ai/combat/projectile.cpp:339 |
| 0x00458820 | GethkTo | proven | src/fallout/ai/combat/projectile.cpp:367 |
| 0x004587F0 | GetTo | proven | src/fallout/ai/combat/projectile.cpp:355 |
| 0x004A3EB0 | SetTo | proven | src/fallout/ai/mobileobject.cpp:269 |

### bhkRagdollController (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7DE30 | 'scalar deleting destructor' | proven | src/fallout/ai/actor_o2_variant.cpp:18 |
| 0x00C7F060 | bhkRagdollController | proven | src/fallout/ai/actor_o2_nood_variant.cpp:2958 |
| 0x00C7BCB0 | CopyPoseTo3DRec | proven | src/fallout/ai/actor_o2_variant.cpp:354 |
| 0x00C7BA10 | EnableRagdollFeedback | proven | src/fallout/ai/actor_o2_variant.cpp:751 |
| 0x00888A50 | FUN_00888a50 | unnamed | src/fallout/ai/actor.cpp:33003 |
| 0x00C7B6A0 | SetRagdollFeedbackActive | proven | src/fallout/ai/actor_o2_nood_variant.cpp:1395 |
| 0x00C7D900 | ~bhkRagdollController | proven | src/fallout/ai/actor_o2_variant.cpp:3046 |

### bhkRigidBodyCinfo (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C8D4A0 | GetQualityTypeString | proven | src/fallout/ai/movement/detailedactorpathhandler_o2_variant.cpp:14 |

### bhkStiffSpringConstraint (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7FA70 | 'scalar deleting destructor' | proven | src/fallout/ai/actor_o2_variant.cpp:45 |
| 0x00C7F9E0 | bhkStiffSpringConstraint | proven | src/fallout/ai/actor_o2_variant.cpp:1028 |
| 0x00C7FA60 | GetRTTI | proven | src/fallout/ai/actor_o2_variant.cpp:31 |

### bhkUtilFunctions (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C802D0 | FindCollisionObject | proven | src/fallout/ai/actor_o2_variant.cpp:153 |

### bhkWorld (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C68F00 | SetWorldActive | decomp | src/fallout/ai/processlists.cpp:304 |

### BlendController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7C870 | FUN_00c7c870 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:280 |

### BoundsGroup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989F40 | ExpandBounds | decomp | src/fallout/ai/combat/combatgroup.cpp:4128 |

### BP (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE670 | FUN_008be670 | unnamed | src/fallout/ai/actor.cpp:14685 |
| 0x008BE810 | FUN_008be810 | unnamed | src/fallout/ai/actor.cpp:14754 |
| 0x00884F20 | GetCachedOrOwnerValue | decomp | src/fallout/ai/actor.cpp:3515 |

### BSAudio (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00AD7480 | GetSoundHandleByFilename | proven | src/fallout/ai/combat/projectile_ob1_variant.cpp:55 |

### BSCriticalSection (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004538C0 | Leave | proven | src/fallout/ai/aitaskmanager.cpp:22 |
| 0x0044B130 | TryLock | proven | src/fallout/ai/middlehighprocess.cpp:66 |

### BSLinearTaskThread (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C74B0 | Shutdown | proven | src/fallout/ai/ailineartaskthreadmanager.cpp:353 |

### BSOcclusionPlane (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AD5F0 | IsNotCulled | decomp | src/fallout/ai/combat/explosion.cpp:108 |

### BSParallelTaskManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C44C90 | RunTask | proven | src/fallout/ai/processlists.cpp:8685 |

### BSSimpleArray<Animation*,1024> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00978E70 | BSSimpleArray | proven | src/fallout/ai/processlists.cpp:1304 |

### BSSimpleArray<BGSBodyPart*,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B7940 | BSSimpleArray | proven | src/fallout/ai/combat/hitdata.cpp:168 |
| 0x009B7970 | ~BSSimpleArray | proven | src/fallout/ai/combat/hitdata.cpp:138 |

### BSSimpleArray<CombatMember,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EFF0 | BSSimpleArray | proven | src/fallout/ai/combat/combatgroup.cpp:420 |
| 0x0098F020 | ~BSSimpleArray | proven | src/fallout/ai/combat/combatgroup.cpp:317 |

### BSSimpleArray<CombatTarget,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098ED30 | BSSimpleArray | proven | src/fallout/ai/combat/combatgroup.cpp:270 |
| 0x0098ED60 | ~BSSimpleArray | proven | src/fallout/ai/combat/combatgroup.cpp:1326 |

### BSSimpleArray<DetailedActorPathHandler::ActorAvoidanceData,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E9950 | BSSimpleArray | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5364 |
| 0x009E9980 | ~BSSimpleArray | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5384 |

### BSSimpleArray<NavMeshTriangleReference,1024> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x006DAD90 | FUN_006dad90 | unnamed | src/fallout/ai/highprocess.cpp:3828 |

### BSSimpleArray<SpectatorThreatInfo,1024> (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8DB0 | 'scalar deleting destructor' | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:288 |
| 0x009F8AE0 | BSSimpleArray | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:196 |
| 0x009F8B10 | ~BSSimpleArray | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:211 |

### BSSimpleArray<TESIdleForm*,1024> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009058E0 | BSSimpleArray | proven | src/fallout/ai/highprocess.cpp:4273 |

### BSSimpleArray<TESObjectWEAP*,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A33E0 | BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:2012 |
| 0x009A3410 | ~BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:319 |

### BSSimpleArray<UnreachableCoverLocation,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A3430 | BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:2030 |
| 0x009A3460 | ~BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:2048 |

### BSSimpleArray<UnreachableLocation,1024> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A35C0 | BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:2066 |
| 0x009A35F0 | ~BSSimpleArray | proven | src/fallout/ai/combat/combatstate.cpp:340 |

### BSSimpleArray_CombatMember_1024 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098F180 | AddCombatMember | decomp | src/fallout/ai/combat/combatgroup.cpp:825 |

### BSSimpleArray_CombatTarget_1024 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EEC0 | FUN_0098eec0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:399 |

### BSTCommonLLMessageQueue<ActorPathingMessage> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00905580 | BSTCommonLLMessageQueue | proven | src/fallout/ai/highprocess.cpp:4254 |

### BSTCommonLLMessageQueue<MobileObjectMessage> (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA710 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:1200 |
| 0x008CA440 | BSTCommonLLMessageQueue | proven | src/fallout/ai/aitaskmanager.cpp:757 |
| 0x008CA480 | ~BSTCommonLLMessageQueue | proven | src/fallout/ai/aitaskmanager.cpp:1113 |

### BSTCommonMessageQueue<MobileObjectMessage> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA540 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:799 |
| 0x008CA500 | ~BSTCommonMessageQueue | proven | src/fallout/ai/aitaskmanager.cpp:771 |

### BSTFreeList<MobileObjectMessage> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA3E0 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:716 |
| 0x008CA3C0 | BSTFreeList | proven | src/fallout/ai/aitaskmanager.cpp:703 |

### BSTMessageQueue<MobileObjectMessage> (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA570 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:815 |
| 0x008CA520 | BSTMessageQueue | proven | src/fallout/ai/aitaskmanager.cpp:785 |

### BSTStaticFreeList<MobileObjectMessage,4096> (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA410 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:731 |
| 0x008CA680 | BSTStaticFreeList | proven | src/fallout/ai/aitaskmanager.cpp:1187 |
| 0x008CA350 | ~BSTStaticFreeList | proven | src/fallout/ai/aitaskmanager.cpp:1092 |

### BSXFlags (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008978D0 | IsBitSet | decomp | src/fallout/ai/actor.cpp:33167 |

### C (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FE8F0 | SetContentCount | decomp | src/fallout/ai/highprocess.cpp:68517 |
| 0x00907AB0 | TrySelectTarget | class | src/fallout/ai/lowprocess.cpp:9104 |

### C008b9e10 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B9E10 | FUN_008b9e10 | unnamed | src/fallout/ai/actor.cpp:40358 |

### C00986670 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00986670 | FUN_00986670 | unnamed | src/fallout/ai/combat/combatgroup.cpp:896 |

### C009ce5b0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CE5B0 | FUN_009ce5b0 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:7083 |

### C8B39D0Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B39D0 | FUN_008b39d0 | unnamed | src/fallout/ai/actor.cpp:79690 |

### C8BCC60Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BCC60 | FUN_008bcc60 | unnamed | src/fallout/ai/actor.cpp:88046 |

### C901C50Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901C50 | IsFlag4Clear | decomp | src/fallout/ai/highprocess.cpp:24671 |

### C90A130Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090A130 | GetControllerPoint | class | src/fallout/ai/lowprocess.cpp:7634 |

### C953C80Form (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00953C80 | HasActorsByPackage | decomp | src/fallout/ai/playercharacter.cpp:32346 |

### C970 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00970F60 | FUN_00970f60 | probable | src/fallout/ai/processlists.cpp:13483 |

### C97FB40Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097FB40 | GetHandle | decomp | src/fallout/ai/combatcontroller.cpp:3611 |

### C98F840Allocator (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098F840 | FUN_0098f840 | unnamed | src/fallout/ai/combat/combatgroup.cpp:5914 |

### C_0087f5c0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087F5C0 | FUN_0087f5c0 | unnamed | src/fallout/ai/actor.cpp:35185 |

### C_008b2b60 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B2B60 | FUN_008b2b60 | probable | src/fallout/ai/actor.cpp:123586 |

### CalcActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B0DD0 | GetCachedSpeed | decomp | src/fallout/ai/actor.cpp:76254 |

### CameraPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094A8C0 | FUN_0094a8c0 | probable | src/fallout/ai/playercharacter.cpp:18856 |

### Candidate (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EBFE0 | SaveToStream | decomp | src/fallout/ai/alarmpackage.cpp:914 |

### CE80Group (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098CE80 | RecountActors | decomp | src/fallout/ai/combat/combatgroup.cpp:9388 |

### CellPlaceStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087F890 | SetPlacement | decomp | src/fallout/ai/actor.cpp:48258 |

### CFActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D9FA0 | CopyFromActor | decomp | src/fallout/ai/middlehighprocess.cpp:14260 |

### CFilter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C19E0 | QNoCollision | proven | src/fallout/ai/combat/projectile.cpp:326 |

### CFUN98fb40Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098FB40 | FUN_0098fb40 | unnamed | src/fallout/ai/combat/combatgroup.cpp:10057 |

### Character536 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D2110 | FUN_008d2110 | class | src/fallout/ai/character_rtti_variant.cpp:2417 |

### CharacterActionState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093DD20 | FUN_0093dd20 | unnamed | src/fallout/ai/playercharacter.cpp:10956 |

### CharacterAnimationBridge (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094C640 | FUN_0094c640 | class | src/fallout/ai/playercharacter.cpp:20501 |

### CharacterProgression (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D5270 | FinishLevelUp | proven | src/fallout/ai/falloutcharacterprogression.cpp:268 |
| 0x008D5300 | ForceLevel | proven | src/fallout/ai/falloutcharacterprogression.cpp:582 |

### CheckActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A4810 | CanInteractWith | decomp | src/fallout/ai/actor.cpp:68984 |

### CleanupOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00980550 | DestroyOwnedObject | decomp | src/fallout/ai/combatcontroller.cpp:5861 |

### ClosedDoorPathFilter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E26D0 | CheckDoorTransition | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:4683 |

### Cls (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009670F0 | FUN_009670f0 | unnamed | src/fallout/ai/playercharacter.cpp:48410 |
| 0x00967B70 | FUN_00967b70 | probable | src/fallout/ai/playercharacter.cpp:52187 |
| 0x00970B30 | FUN_00970b30 | probable | src/fallout/ai/alarmpackage.cpp:1321 |
| 0x00C7BA50 | FUN_00c7ba50 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1770 |
| 0x008B6290 | ProcessObjects | decomp | src/fallout/ai/actor.cpp:80336 |

### Cls9715 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009715C0 | CollectCombatTargets | decomp | src/fallout/ai/processlists.cpp:12008 |

### Cls_0097f3f0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F3F0 | UpdatePointer | decomp | src/fallout/ai/combatcontroller.cpp:1012 |

### CombatAssessment::Group (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009887B0 | UpdateTargetPerception | decomp | src/fallout/ai/combat/combatgroup.cpp:7978 |

### CombatMemberData_985520 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985520 | MergeCombatData | decomp | src/fallout/ai/combat/combatgroup.cpp:3055 |

### CombatProc9cd430 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CD430 | FUN_009cd430 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:2357 |

### CombatProcedure_008b3a50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3A50 | FUN_008b3a50 | unnamed | src/fallout/ai/combat/combatprocedure.cpp:163 |

### CombatRegion::Group (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098A580 | FUN_0098a580 | probable | src/fallout/ai/combat/combatgroup.cpp:8882 |

### CombatWeapons::Manager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009993C0 | EvaluateWeaponScores | decomp | src/fallout/ai/combat/combatstate.cpp:6914 |

### Container (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099A360 | FUN_0099a360 | unnamed | src/fallout/ai/combat/combatstate.cpp:1776 |

### ContinuousBeamProjectile (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DA760 | Initialize | decomp | src/fallout/ai/combat/continuousbeamprojectile.cpp:10 |
| 0x009ABD00 | ScaleBeam3D | proven | src/fallout/ai/combat/continuousbeamprojectile.cpp:1169 |
| 0x009AB390 | UpdateProjectile | proven | src/fallout/ai/combat/projectile.cpp:10410 |

### Controller (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095E670 | FUN_0095e670 | class | src/fallout/ai/actor_magic.cpp:1860 |

### Controller9D1 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D1BC0 | FUN_009d1bc0 | unnamed | src/fallout/ai/combat/combatprocedureattackranged.cpp:2149 |

### ControllerFactory (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D1740 | CreateController | class | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:66 |

### ConvoCheckOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DA420 | CanStartConversation | class | src/fallout/ai/highprocess.cpp:56708 |

### CopyProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F6180 | CopyProcessList | class | src/fallout/ai/highprocess.cpp:18213 |

### CornerAccumulator (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098A110 | UpdateBoundsFromActors | decomp | src/fallout/ai/combat/combatgroup.cpp:4310 |

### CoverProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D25B0 | UpdateCoverState | class | src/fallout/ai/combat/combatprocedurebeincover.cpp:844 |

### CPAM9cc240 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CC240 | UpdateCombatState | class | src/fallout/ai/combat/combatprocedureattackmelee.cpp:5002 |

### CPMap00993a00 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00993A00 | Lookup | decomp | src/fallout/ai/combat/combatmanager.cpp:1455 |

### CPMap00993a80 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00993A80 | GetNextEntry | decomp | src/fallout/ai/combat/combatmanager.cpp:1488 |

### CPPlanner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009950C0 | ExpandNode | class | src/fallout/ai/combat/combatplanner.cpp:190 |

### CPStandIn00992b00 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00992B00 | ClearFlagIfSet | decomp | src/fallout/ai/combat/combatmanager.cpp:1411 |

### CPStandIn009caae0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CAAE0 | SetState | decomp | src/fallout/ai/combat/combatprocedureactivateobject.cpp:434 |

### CS_State (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A1060 | UpdateRangeValue | decomp | src/fallout/ai/combat/combatstate.cpp:9203 |

### CSUnit (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F580 | NotifyTrackerAndAddAmount | decomp | src/fallout/ai/combatcontroller.cpp:5548 |

### CvOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00922B80 | UpdateLevel | class | src/fallout/ai/middlehighprocess.cpp:10058 |

### CVShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008805F0 | FUN_008805f0 | probable | src/fallout/ai/actor.cpp:19246 |

### CWrap (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00888B20 | CallVirtual190 | class | src/fallout/ai/actor.cpp:36448 |

### D (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00885140 | GetScaledXDelta | decomp | src/fallout/ai/actor.cpp:21165 |

### D1C30Task (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D1C30 | ResetTask | decomp | src/fallout/ai/combat/combatprocedureattackranged.cpp:652 |

### D9780Object (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D9780 | FUN_008d9780 | class | src/fallout/ai/highprocess.cpp:14304 |

### Dd (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE420 | FUN_008be420 | probable | src/fallout/ai/actor.cpp:14608 |

### DebugGroup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009878B0 | RebuildDebugVisuals | decomp | src/fallout/ai/combat/combatgroup.cpp:7072 |

### DetailedActorPathHandlerEx (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E3D50 | UpdatePathing | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:3086 |
| 0x009E0470 | UpdatePathTravel | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:1426 |

### detection_008a0d10::ActorMethods (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A0D10 | FUN_008a0d10 | probable | src/fallout/ai/actor.cpp:120964 |

### Dialogue114 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EE0A0 | FUN_009ee0a0 | probable | src/fallout/ai/dialoguepackage.cpp:1125 |

### Dialogue9CF (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CFC90 | StopIfSpeakerOutOfRange | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:4157 |

### DialoguePackageState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EFF60 | ResolveReferences | class | src/fallout/ai/dialoguepackage.cpp:1742 |

### DialoguePlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00968F90 | FUN_00968f90 | probable | src/fallout/ai/playercharacter.cpp:53810 |

### DialogueProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00902BD0 | FUN_00902bd0 | probable | src/fallout/ai/highprocess.cpp:54488 |

### dist8be::B8Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE740 | FUN_008be740 | unnamed | src/fallout/ai/actor.cpp:115331 |

### DoorHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E20C0 | UpdateDoorState | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:7526 |

### DoorInPathFilter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E2690 | DoorInPathFilter | proven | src/fallout/ai/movement/detailedactorpathhandler.cpp:5221 |

### DoorPathHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EAD90 | UpdateDoorPath | decomp | src/fallout/ai/movement/virtualactorpathhandler.cpp:1373 |

### DoorTeleportSpaceReceiver (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DC7F0 | UpdateTeleportPathState | decomp | src/fallout/ai/movement/actormover.cpp:1935 |

### DrawWeaponStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097C990 | FUN_0097c990 | unnamed | src/fallout/ai/combat/combatactions.cpp:710 |

### Dummy00981520 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00981520 | SetFieldC7 | decomp | src/fallout/ai/combatcontroller.cpp:1229 |

### Dummy629670 (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00886C80 | FUN_00886c80 | unnamed | src/fallout/ai/actor.cpp:33904 |
| 0x00931530 | FUN_00931530 | unnamed | src/fallout/ai/actor.cpp:34717 |

### Dummy8879d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008879D0 | FUN_008879d0 | unnamed | src/fallout/ai/actor.cpp:4047 |

### DummyClass (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901360 | ClearRefIfMatches | class | src/fallout/ai/highprocess.cpp:6364 |

### DummyClass_00884970 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884970 | FUN_00884970 | unnamed | src/fallout/ai/actor.cpp:3290 |

### DummyClass_0088b070 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B070 | FUN_0088b070 | unnamed | src/fallout/ai/actor.cpp: |

### DummyFlags (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B0C0 | FUN_0088b0c0 | probable | src/fallout/ai/actor.cpp:33029 |
| 0x009269F0 | FUN_009269f0 | unnamed | src/fallout/ai/middlehighprocess.cpp:3164 |
| 0x009304B0 | HasFlag20 | decomp | src/fallout/ai/mobileobject.cpp:1363 |

### DummyInner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097EE90 | FUN_0097ee90 | probable | src/fallout/ai/combat/combatstate.cpp:11109 |

### DummyOuter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009818B0 | FUN_009818b0 | probable | src/fallout/ai/combatcontroller.cpp:1316 |

### E6C0Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0081E6C0 | SetShown | class | src/fallout/ai/mobileobject.cpp:7828 |

### EActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088E8D0 | FUN_0088e8d0 | probable | src/fallout/ai/actor.cpp:127351 |

### EffectAddedActorView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C4AB0 | FUN_008c4ab0 | unnamed | src/fallout/ai/actor.cpp:150398 |

### EffectProcessLists (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009746C0 | FUN_009746c0 | unnamed | src/fallout/ai/processlists.cpp:12430 |

### EffectSetting (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004FD3E0 | GetHitSound | decomp | src/fallout/ai/actorpackage.cpp:401 |

### ElemArray (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8DE0 | FUN_009f8de0 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:3375 |

### Engage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D5410 | PrintDebugInfo | class | src/fallout/ai/combat/combatprocedureengagetarget.cpp:602 |

### EngageProc (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D3B80 | UpdateEngagement | class | src/fallout/ai/combat/combatprocedureengagetarget.cpp:1217 |

### Engine_00902c80 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00902C80 | FUN_00902c80 | probable | src/fallout/ai/highprocess.cpp:54573 |

### Entry5890 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C5890 | UpdateStageTransition | decomp | src/fallout/ai/actor_magic.cpp:5676 |

### EquipProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009231D0 | UpdateEquipVisuals | class | src/fallout/ai/middlehighprocess.cpp:26079 |

### EvadeProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D5B90 | UpdateFleeState | class | src/fallout/ai/combat/combatprocedureevade.cpp:491 |

### EventActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BA600 | ProcessEvents | decomp | src/fallout/ai/actor.cpp:85396 |

### EventRecord (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00985410 | Init | decomp | src/fallout/ai/combat/combatgroup.cpp:2992 |

### Explosion (12)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AC1D0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/explosion.cpp:35 |
| 0x009ABF30 | Explosion | proven | src/fallout/ai/combat/explosion.cpp:1632 |
| 0x009AC200 | Explosion | proven | src/fallout/ai/combat/explosion.cpp:1842 |
| 0x009B2770 | FinishLoadGame | proven | src/fallout/ai/combat/explosion.cpp:95 |
| 0x009AE280 | InitHavok | proven | src/fallout/ai/mobileobject_o2_variant_od_oy_noo2_variant.cpp:344 |
| 0x009B25B0 | InitLoadGame | proven | src/fallout/ai/combat/explosion.cpp:1495 |
| 0x009B22C0 | LoadGame | proven | src/fallout/ai/combat/explosion.cpp:722 |
| 0x009B2790 | Revert | proven | src/fallout/ai/combat/explosion.cpp:2148 |
| 0x009B1810 | RunLOSPick | proven | src/fallout/ai/combat/explosion_o2_variant_od_oy_noo2_variant.cpp:1000 |
| 0x009AC170 | SetActorCause | proven | src/fallout/ai/combat/explosion.cpp:20 |
| 0x009B2940 | TestExplosionUnderWater | proven | src/fallout/ai/actor_magic.cpp:8077 |
| 0x009AC5A0 | ~Explosion | proven | src/fallout/ai/combat/explosion.cpp:3214 |

### ExplosionSave (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B2040 | WriteToSaveBuffer | class | src/fallout/ai/combat/explosion.cpp:3360 |

### F1990Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901990 | CanBeTargeted | class | src/fallout/ai/highprocess.cpp:52168 |

### F8660Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00978660 | FUN_00978660 | unnamed | src/fallout/ai/processlists.cpp:12973 |

### FadePlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00961C40 | StartFade | class | src/fallout/ai/actor.cpp:96016 |

### FakeActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089D8B0 | FUN_0089d8b0 | probable | src/fallout/ai/actor.cpp:37252 |
| 0x008A5E80 | FUN_008a5e80 | unnamed | src/fallout/ai/actor.cpp:38642 |

### FakeCell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x005547C0 | FUN_005547c0 | probable | src/fallout/ai/highprocess.cpp:4328 |

### FakeClass009014a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009014A0 | FUN_009014a0 | class | src/fallout/ai/highprocess.cpp:6378 |

### FakeCls (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E0AD0 | FUN_008e0ad0 | unnamed | src/fallout/ai/highprocess.cpp:5250 |

### FakeHolder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009057D0 | AssignObject | decomp | src/fallout/ai/highprocess.cpp:6571 |

### FakeMob (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008990A0 | LogBlockedBlow | class | src/fallout/ai/actor.cpp:37217 |

### FakeProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092B970 | SetLimbNode | class | src/fallout/ai/middlehighprocess.cpp:3766 |

### FalloffController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007F7970 | UpdateFalloff | decomp | src/fallout/ai/sandboxpackage.cpp:1316 |

### FalloutRadio_StationState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00836240 | LoadGame | proven | src/fallout/ai/processlists.cpp:16122 |

### FlameProjectile (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B4D40 | IsProximityDetonationTriggered | class | src/fallout/ai/combat/projectile.cpp:23 |
| 0x009B3F00 | LoadGame | proven | src/fallout/ai/combat/flameprojectile.cpp:39 |
| 0x009B3F50 | Revert | proven | src/fallout/ai/combat/flameprojectile.cpp:59 |
| 0x009B36F0 | RunTargetPick | proven | src/fallout/ai/combat/flameprojectile_o2_variant_od_oy_noo2_variant.cpp:499 |

### FleeActorEntry (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A6650 | FUN_008a6650 | probable | src/fallout/ai/actor.cpp:145546 |

### FleeProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00918600 | FUN_00918600 | class | src/fallout/ai/middlehighprocess_iso_variant.cpp:1772 |

### FleeProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00904540 | UpdateFleeTarget | class | src/fallout/ai/highprocess.cpp:55775 |

### FloatValueProvider (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE280 | FUN_008be280 | probable | src/fallout/ai/actor.cpp:14575 |
| 0x008BE7A0 | FUN_008be7a0 | probable | src/fallout/ai/actor.cpp:14716 |

### Flt (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D5510 | FUN_008d5510 | probable | src/fallout/ai/falloutcharacterprogression.cpp:177 |
| 0x008D5550 | FUN_008d5550 | probable | src/fallout/ai/falloutcharacterprogression.cpp:196 |
| 0x008D5210 | LevelUpPlayer | decomp | src/fallout/ai/falloutcharacterprogression.cpp:156 |

### FNV_93dee0_Host (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093DEE0 | FUN_0093dee0 | unnamed | src/fallout/ai/playercharacter.cpp:11971 |

### fnv_anon_008d7fc0::LowProcessExt (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D7FC0 | IsFlag1Set | class | src/fallout/ai/highprocess.cpp:4458 |

### FNVAnimationController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7CB50 | FUN_00c7cb50 | class | src/fallout/ai/actor_o2_nood_variant_rtm_variant.cpp:4439 |

### FNVCurrent (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092ED60 | FUN_0092ed60 | probable | src/fallout/ai/mobileobject.cpp:14244 |

### FNVPlayerScanner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00962190 | FUN_00962190 | unnamed | src/fallout/ai/playercharacter.cpp:42566 |

### FollowProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091DD30 | FUN_0091dd30 | class | src/fallout/ai/middlehighprocess.cpp:19817 |

### FollowProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E0F80 | FUN_008e0f80 | class | src/fallout/ai/highprocess.cpp:33262 |

### FOPipboyManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00974D90 | IsUnk28Set | decomp | src/fallout/ai/processlists.cpp:272 |

### FUN_Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00885ED0 | FUN_00885ed0 | probable | src/fallout/ai/actor.cpp:55796 |

### GameScreen (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BF190 | FUN_009bf190 | probable | src/fallout/ai/combat/projectile.cpp:7109 |

### Getter_9b8 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B88C0 | FUN_009b88c0 | class | src/fallout/ai/highprocess.cpp:26403 |

### GetUpPackagePlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00953EE0 | FUN_00953ee0 | class | src/fallout/ai/playercharacter.cpp:69102 |

### GPShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B4950 | HandleContactHit | decomp | src/fallout/ai/combat/grenadeprojectile.cpp:702 |

### GrabHost (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095F930 | FUN_0095f930 | probable | src/fallout/ai/playercharacter_o2_variant_od_oy_noo2_variant.cpp:950 |

### GrenadeProjectile (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B4740 | FUN_009b4740 | unnamed | src/fallout/ai/combat/grenadeprojectile_decl_variant.cpp:1321 |
| 0x009B3FA0 | GrenadeProjectile | proven | src/fallout/ai/combat/grenadeprojectile.cpp:41 |
| 0x009B4020 | GrenadeProjectile | proven | src/fallout/ai/combat/grenadeprojectile.cpp:310 |
| 0x009BDF80 | IsProximityTriggered | class | src/fallout/ai/combat/grenadeprojectile.cpp:7 |
| 0x009B4D10 | Revert | proven | src/fallout/ai/combat/grenadeprojectile.cpp:108 |
| 0x009B4700 | TurnOff | proven | src/fallout/ai/combat/grenadeprojectile.cpp:70 |

### Grp_Call2 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009899A0 | FUN_009899a0 | probable | src/fallout/ai/combat/combatgroup.cpp:3884 |

### H008ca010 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA010 | ForwardToInner | decomp | src/fallout/ai/aitaskmanager.cpp:1641 |

### H_8b3cd0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3CD0 | FUN_008b3cd0 | probable | src/fallout/ai/actor.cpp:40235 |

### H_9f0b70 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F0A60 | RemoveActorFromList | decomp | src/fallout/ai/escortpackage.cpp:145 |

### HActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089A760 | FUN_0089a760 | probable | src/fallout/ai/actor.cpp:129350 |

### HeadTrackStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009012A0 | FUN_009012a0 | class | src/fallout/ai/highprocess.cpp:10230 |

### HeadTrackTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901390 | RemoveTarget | class | src/fallout/ai/highprocess.cpp:10251 |

### HealthActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00898650 | FUN_00898650 | class | src/fallout/ai/actor.cpp:63452 |

### HideProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D6140 | Update | class | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:637 |

### HideTargetLayout (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D6900 | Load | class | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:197 |

### HighProcess_008d8c60 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D8C60 | RemoveTopicInfo | class | src/fallout/ai/highprocess.cpp:12581 |

### HighProcessAvoid (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009042A0 | AddAvoidArea | decomp | src/fallout/ai/highprocess.cpp:55092 |

### HighProcessEx (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E59C0 | FUN_008e59c0 | class | src/fallout/ai/highprocess.cpp:59082 |

### HighProcessFake (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F68F0 | IsTargetInView | class | src/fallout/ai/highprocess.cpp:5748 |

### HighProcessHack (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F6990 | GetDetectionLevel | class | src/fallout/ai/highprocess.cpp:6086 |

### HighProcessS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F21F0 | FUN_008f21f0 | probable | src/fallout/ai/highprocess.cpp:9946 |

### HighProcessSave (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FAA50 | SaveToStream | class | src/fallout/ai/highprocess.cpp:21170 |

### HighProcessStandIn (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D95F0 | GetKFModel | class | src/fallout/ai/highprocess.cpp:10387 |
| 0x008FFC30 | IsTargetDetected | decomp | src/fallout/ai/highprocess.cpp:10442 |

### HighProcessWorker (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F63E0 | ProcessDetectionStateLists | decomp | src/fallout/ai/highprocess.cpp:46150 |

### Hit (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B73D0 | ApplyDamageEffects | decomp | src/fallout/ai/combat/hitdata.cpp:1113 |

### Hit_00899060 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00899060 | FUN_00899060 | class | src/fallout/ai/actor.cpp:5289 |

### HitData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B7060 | CheckCriticalStrike | proven | src/fallout/ai/combat/hitdata.cpp:612 |
| 0x009B4DC0 | ClearData | proven | src/fallout/ai/combat/hitdata.cpp:100 |
| 0x009B4EC0 | Copy | proven | src/fallout/ai/combat/hitdata.cpp:243 |
| 0x009B4D90 | HitData | proven | src/fallout/ai/combat/hitdata.cpp:232 |
| 0x009B6620 | SetTargetedLimb | proven | src/fallout/ai/combat/hitdata_o2_variant_od_oy_noo2_variant.cpp:808 |

### HkFloatCheck (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7F500 | FUN_00c7f500 | unnamed | src/fallout/ai/actor_o2_variant.cpp:2448 |

### Holder (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A5230 | CallProcessTarget | decomp | src/fallout/ai/actor.cpp:38195 |
| 0x00881330 | CallTargetWithFloat | class | src/fallout/ai/actor.cpp:35813 |
| 0x00881570 | FUN_00881570 | unnamed | src/fallout/ai/actor.cpp:36047 |
| 0x0089D640 | FUN_0089d640 | unnamed | src/fallout/ai/actor.cpp:37239 |
| 0x008D4870 | FUN_008d4870 | unnamed | src/fallout/ai/actor.cpp:16502 |
| 0x008D49C0 | FUN_008d49c0 | class | src/fallout/ai/creature.cpp:288 |
| 0x008D4A20 | FUN_008d4a20 | class | src/fallout/ai/actor.cpp:40922 |
| 0x009C3E10 | FUN_009c3e10 | unnamed | src/fallout/ai/combat/projectile.cpp:462 |
| 0x00989090 | GetCombatTargetTimestamp | decomp | src/fallout/ai/combat/combatgroup.cpp:673 |
| 0x00999120 | IsModifierZero | decomp | src/fallout/ai/combat/combatstate.cpp:745 |
| 0x009D8410 | SetValue | decomp | src/fallout/ai/combat/combatproceduremove.cpp:42 |

### Holder0087 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087F9C0 | FUN_0087f9c0 | unnamed | src/fallout/ai/actor.cpp:35210 |

### Holder008a3b70 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A3B70 | FUN_008a3b70 | probable | src/fallout/ai/actor.cpp:38035 |

### Holder008a7a40 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A7A40 | FUN_008a7a40 | probable | src/fallout/ai/actor.cpp:39013 |

### Holder008bbeb0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BBEB0 | GetAndApplyResult | decomp | src/fallout/ai/actor.cpp:40713 |

### Holder008d8d30 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D8D30 | SetVec | class | src/fallout/ai/highprocess.cpp:4771 |

### Holder0097 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F7F0 | ForwardToInner | decomp | src/fallout/ai/combatcontroller.cpp:1120 |

### Holder009807f0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009807F0 | CallHelperFoo | decomp | src/fallout/ai/combatcontroller.cpp:1210 |

### Holder009dcb30 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DCB30 | FUN_009dcb30 | probable | src/fallout/ai/movement/actormover.cpp:1378 |

### Holder009eb120 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EB120 | GetPoint | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:944 |

### Holder908f40 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00908F40 | FUN_00908f40 | unnamed | src/fallout/ai/lowprocess.cpp:3611 |

### Holder9177a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009177A0 | FUN_009177a0 | class | src/fallout/ai/lowprocess.cpp:3790 |

### Holder91b580 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091B580 | FUN_0091b580 | unnamed | src/fallout/ai/middlehighprocess_rtm_variant.cpp:249 |

### Holder9A2 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A2CC0 | ResolveRef | decomp | src/fallout/ai/combat/combatstate.cpp:9561 |

### Holder_00884aa0 (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884AA0 | FUN_00884aa0 | class | src/fallout/ai/mobileobject.cpp:1489 |
| 0x00930640 | UpdateControllerScale | class | src/fallout/ai/mobileobject.cpp:9411 |

### Holder_009010a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009010A0 | FUN_009010a0 | class | src/fallout/ai/highprocess.cpp:6312 |

### Holder_009816d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009816D0 | FUN_009816d0 | unnamed | src/fallout/ai/combatcontroller.cpp:1298 |

### Holder_009f7fe0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F7FE0 | FUN_009f7fe0 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:325 |

### HolderFUN (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0066CA00 | FUN_0066ca00 | probable | src/fallout/ai/actor.cpp:34947 |

### Host (7)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00623090 | FUN_00623090 | probable | src/fallout/ai/actor.cpp:34919 |
| 0x00913FB0 | FUN_00913fb0 | unnamed | src/fallout/ai/middlehighprocess.cpp:3605 |
| 0x0099A7D0 | FUN_0099a7d0 | probable | src/fallout/ai/combat/combatstate.cpp:1866 |
| 0x009A0A80 | FUN_009a0a80 | probable | src/fallout/ai/combat/combatstate.cpp:1929 |
| 0x009897A0 | IsElapsedTimeBelowSetting | decomp | src/fallout/ai/combat/combatgroup.cpp:1213 |
| 0x008ECBB0 | ProcessActorsForReference | class | src/fallout/ai/highprocess.cpp:39209 |
| 0x009A3780 | ProcessElements | decomp | src/fallout/ai/combat/combatstate.cpp:1534 |

### Host00881620 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00881620 | FUN_00881620 | probable | src/fallout/ai/actor.cpp:36140 |

### Host009 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EC1A0 | ReadFromStream | decomp | src/fallout/ai/alarmpackage.cpp:1576 |

### Host0097f6d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F6D0 | FUN_0097f6d0 | unnamed | src/fallout/ai/combatcontroller.cpp:1079 |

### Host37870 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937870 | FUN_00937870 | unnamed | src/fallout/ai/modifierlist.cpp:265 |

### Host911b00 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00911B00 | UpdateFollowerList | class | src/fallout/ai/lowprocess.cpp:11282 |

### Host95 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095D450 | FUN_0095d450 | unnamed | src/fallout/ai/playercharacter.cpp:39944 |

### Host9f6340 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F6340 | AppendElement | decomp | src/fallout/ai/sandboxpackage.cpp:996 |

### Host_00905250 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00905250 | FUN_00905250 | class | src/fallout/ai/highprocess.cpp:6550 |

### HostActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B06D0 | IsHostileTo | decomp | src/fallout/ai/actor.cpp:74408 |

### HostController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901740 | FUN_00901740 | probable | src/fallout/ai/highprocess.cpp:23829 |

### HostShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A4AF0 | FUN_008a4af0 | class | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:1785 |

### HostT (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DFA10 | FUN_008dfa10 | class | src/fallout/ai/highprocess.cpp:58296 |

### HX (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C47F0 | GetResponseValue | class | src/fallout/ai/actor.cpp:16390 |
| 0x008A5EB0 | GetWeaponObject | decomp | src/fallout/ai/actor.cpp:6812 |

### Iface (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C3FB0 | FUN_008c3fb0 | unnamed | src/fallout/ai/actor.cpp:113467 |

### ImageSpaceModifierInstance (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009655E0 | FUN_009655e0 | unnamed | src/fallout/ai/playercharacter.cpp:46338 |

### ImpactActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ACFF0 | ApplyImpact | decomp | src/fallout/ai/actor.cpp:73473 |

### ImpactHost (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088E1E0 | FUN_0088e1e0 | probable | src/fallout/ai/actor.cpp:102057 |

### ImpactProjectile (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C1B70 | ProcessHits | class | src/fallout/ai/combat/grenadeprojectile.cpp:1456 |

### ImpactResponse::Impact (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B8C90 | HandleContactResponse | decomp | src/fallout/ai/combat/missileprojectile.cpp:2088 |

### Inner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884880 | FUN_00884880 | unnamed | src/fallout/ai/actor.cpp:32935 |

### InputPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009466D0 | FUN_009466d0 | probable | src/fallout/ai/playercharacter.cpp:59883 |

### InteractionProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E8600 | UpdateInteraction | class | src/fallout/ai/highprocess.cpp:36790 |

### InterpolatorStep (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00946140 | FUN_00946140 | unnamed | src/fallout/ai/playercharacter.cpp:68957 |

### InventoryChanges (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x004C8F30 | GetObjectCount | proven | src/fallout/ai/combatcontroller.cpp:882 |

### InversePositionVector (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7F840 | FUN_00c7f840 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:3014 |

### IRContainer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00968BE0 | FUN_00968be0 | probable | src/fallout/ai/playercharacter.cpp:53710 |

### ItemList (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098BC00 | FindBestItem | decomp | src/fallout/ai/combat/combatgroup.cpp:4751 |

### KillActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089D900 | FUN_0089d900 | probable | src/fallout/ai/actor.cpp:148577 |

### LightPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009673D0 | FUN_009673d0 | probable | src/fallout/ai/playercharacter.cpp:51183 |

### LinkedListNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007A8790 | FUN_007a8790 | unnamed | src/fallout/ai/processlists.cpp:5352 |

### LiquidActionCandidate (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CBCCB0 | FUN_00cbccb0 | class | src/fallout/ai/combat/explosion_o2_nood_variant.cpp:3021 |

### Listener9C64 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C6490 | FUN_009c6490 | unnamed | src/fallout/ai/combat/projectilelistener_od_oy_noo2_variant.cpp:702 |

### Lists976030 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00976030 | FUN_00976030 | unnamed | src/fallout/ai/processlists.cpp:12742 |

### LLD_PlayerCharacter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093CCE0 | FUN_0093cce0 | probable | src/fallout/ai/playercharacter.cpp:9073 |

### load926::Self (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00926690 | FUN_00926690 | unnamed | src/fallout/ai/middlehighprocess.cpp:34496 |

### LoadProjectile52 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C52F0 | LoadProjectile | class | src/fallout/ai/combat/projectile.cpp:9226 |

### LookActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B7100 | GetLookAtPosition | decomp | src/fallout/ai/actor.cpp:81333 |

### LowListProcessLists (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096B470 | UpdateLowListProcessLists | decomp | src/fallout/ai/processlists.cpp:8865 |

### LowProcessAccess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090D000 | FUN_0090d000 | class | src/fallout/ai/lowprocess.cpp:9181 |

### LowProcessFA70 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090FA70 | SaveToStream | class | src/fallout/ai/lowprocess.cpp:10041 |

### LowProcessProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090DC10 | FUN_0090dc10 | class | src/fallout/ai/lowprocess.cpp:2936 |

### LowProcessStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090DC60 | UpdateTargetAndMovement | class | src/fallout/ai/lowprocess.cpp:4299 |

### Lst9711 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009711E0 | CollectNearbyRefs | decomp | src/fallout/ai/processlists.cpp:15917 |

### MActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AE660 | FUN_008ae660 | probable | src/fallout/ai/actor.cpp:140906 |

### MagicCasterShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094C800 | ApplyEffect | decomp | src/fallout/ai/actor.cpp:95602 |

### Manager496 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00992BA0 | CountNearbyActors | decomp | src/fallout/ai/combat/combatmanager.cpp:2813 |

### MatchPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093C200 | FUN_0093c200 | probable | src/fallout/ai/playercharacter.cpp:8850 |

### MAVActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093AFB0 | FUN_0093afb0 | class | src/fallout/ai/playercharacter.cpp:3891 |

### MeleeDebugProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CF700 | PrintDebugInfo | class | src/fallout/ai/combat/combatprocedureattackmelee.cpp:3907 |

### MeleeProc (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CCFB0 | FUN_009ccfb0 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:2150 |

### MeleeProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CF420 | IsActionAvailable | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:2937 |

### Menu75x (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00970810 | FUN_00970810 | unnamed | src/fallout/ai/processlists.cpp:15665 |

### MenuTopicOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00900C20 | BuildTopicLists | class | src/fallout/ai/highprocess.cpp:61583 |

### MiddleHigh0091 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091B700 | FUN_0091b700 | class | src/fallout/ai/middlehighprocess_gs_nogs_rtm_variant.cpp:17921 |

### MiddleHighProcess_00924100 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00924100 | ResetWeaponAndAmmo | class | src/fallout/ai/middlehighprocess.cpp:26250 |

### MiddleHighProcess_00929470 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929470 | RemoveArrowProjectile | class | src/fallout/ai/middlehighprocess.cpp:12368 |

### MiddleHighProcess_standin (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00900020 | EngageCombatTarget | class | src/fallout/ai/highprocess.cpp:51461 |

### MiddleHighProcessF (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00915E50 | SetFurnitureMarker | class | src/fallout/ai/middlehighprocess.cpp:3090 |

### MiddleHighProcessQ (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009157E0 | HasMatchingQueuedItem | class | src/fallout/ai/middlehighprocess.cpp:3058 |

### MiddleHighProcessStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929D40 | UpdateShotsPerSecond | class | src/fallout/ai/middlehighprocess.cpp:6802 |

### MidHighStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092C2E0 | SetLipsynchAnim | class | src/fallout/ai/middlehighprocess.cpp:3785 |

### MidProc (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00918120 | FUN_00918120 | class | src/fallout/ai/middlehighprocess_iso_variant.cpp:747 |
| 0x00918EE0 | FUN_00918ee0 | class | src/fallout/ai/middlehighprocess.cpp:33411 |

### MissileActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BA660 | HandleMissileImpact | decomp | src/fallout/ai/combat/missileprojectile.cpp:2598 |

### MissileProjectile (9)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B7A20 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/missileprojectile.cpp:129 |
| 0x009BAAA0 | AppendSaveLoadFormBuffer | proven | src/fallout/ai/combat/missileprojectile.cpp:320 |
| 0x009BAAD0 | LoadGame | proven | src/fallout/ai/combat/missileprojectile.cpp:61 |
| 0x009B7A50 | MissileProjectile | proven | src/fallout/ai/combat/missileprojectile.cpp:669 |
| 0x009B7AF0 | MissileProjectile | proven | src/fallout/ai/combat/missileprojectile.cpp:792 |
| 0x009B8B10 | ProcessImpacts | proven | src/fallout/ai/combat/beamprojectile.cpp:1919 |
| 0x009BAB70 | Revert | proven | src/fallout/ai/combat/missileprojectile.cpp:82 |
| 0x009B8030 | UpdateProjectile | proven | src/fallout/ai/combat/missileprojectile.cpp:1677 |
| 0x009B7BC0 | ~MissileProjectile | proven | src/fallout/ai/combat/missileprojectile.cpp:891 |

### MobileObjectMessage (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8190 | MobileObjectMessage | proven | src/fallout/ai/aitaskmanager.cpp:76 |

### MobileObjectStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B00C0 | UpdateControllerFlag | decomp | src/fallout/ai/actor.cpp:44116 |

### ModifierList_h (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937C60 | LoadModifiers | decomp | src/fallout/ai/actor.cpp:32750 |

### ModifierListCalc (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937AB0 | FUN_00937ab0 | unnamed | src/fallout/ai/modifierlist.cpp:436 |

### MotionRule (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00946280 | FUN_00946280 | unnamed | src/fallout/ai/playercharacter.cpp:15183 |

### MotionTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E4CF0 | UpdateMotion | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:8142 |

### MoveActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009026C0 | SelectMoveTarget | decomp | src/fallout/ai/highprocess.cpp:54369 |
| 0x00881860 | TryMove | decomp | src/fallout/ai/actor.cpp:51630 |

### MoveDebug (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D8520 | PrintDebugInfo | class | src/fallout/ai/combat/combatproceduremove.cpp:2025 |

### MoveHolder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D8480 | ClearTargetRef | class | src/fallout/ai/combat/combatproceduremove.cpp:79 |

### MovementTaskData (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C91A0 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:488 |
| 0x008C8450 | FUN_008c8450 | class | src/fallout/ai/aitaskmanager.cpp:1454 |
| 0x008C91F0 | FUN_008c91f0 | class | src/fallout/ai/aitaskmanager.cpp:527 |
| 0x008C9170 | MovementTaskData | proven | src/fallout/ai/aitaskmanager.cpp:474 |
| 0x008C9220 | UpdateMovementTask | class | src/fallout/ai/aitaskmanager.cpp:2446 |
| 0x008C91D0 | ~MovementTaskData | proven | src/fallout/ai/aitaskmanager.cpp:506 |

### MoveOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00981740 | UpdateMoveTarget | decomp | src/fallout/ai/combatcontroller.cpp:4114 |

### MoverState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DB950 | ResetMoverState | decomp | src/fallout/ai/movement/actormover.cpp:951 |

### MTStand (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C4020 | FUN_008c4020 | unnamed | src/fallout/ai/actor.cpp:18843 |

### MuzzleFlash (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BB690 | Enable | proven | src/fallout/ai/combat/muzzleflash.cpp:72 |
| 0x009BAEE0 | GetMuzzleFlashModel | proven | src/fallout/ai/combat/muzzleflash.cpp:48 |
| 0x009BB080 | Update | proven | src/fallout/ai/combat/muzzleflash.cpp:353 |

### MyActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AAEE0 | FUN_008aaee0 | class | src/fallout/ai/actor.cpp:39746 |
| 0x008BC980 | FUN_008bc980 | unnamed | src/fallout/ai/actor.cpp:40786 |

### MyActor008A5300 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A5300 | CallProcessAt778 | decomp | src/fallout/ai/actor.cpp:38224 |

### MyCand (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EBCA0 | WriteToSave | decomp | src/fallout/ai/alarmpackage.cpp:1443 |

### MyClass (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989040 | GetResultForArg | decomp | src/fallout/ai/combat/combatgroup.cpp:638 |

### MyHigh (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F68A0 | FUN_008f68a0 | class | src/fallout/ai/highprocess.cpp:5408 |

### MyHolder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DCB90 | FUN_009dcb90 | unnamed | src/fallout/ai/movement/actormover.cpp:1420 |

### MyList (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C71F0 | FUN_009c71f0 | unnamed | src/fallout/ai/combat/vats.cpp:178 |

### MyOuter88230 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A8230 | FUN_008a8230 | unnamed | src/fallout/ai/actor.cpp:39107 |

### MyTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A8010 | FUN_008a8010 | unnamed | src/fallout/ai/actor.cpp:39070 |

### NiAVObject (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0043D450 | GetWorldBound | proven | src/fallout/ai/combat/combatthreatmap.cpp:118 |

### NiNodeBooleanState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D51F0 | GetBooleanValue | decomp | src/fallout/ai/falloutcharacterprogression.cpp:6 |

### NiObject (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00621A40 | FUN_00621a40 | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:5180 |

### NiPick (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00632D20 | SetFrontOnly | proven | src/fallout/ai/processlists.cpp:432 |

### NiTMap<NiAVObject*,BSSimpleList<bhkLiquidAction*>*> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CBD4E0 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/explosion_o2_variant.cpp:83 |

### NiTMap<unsigned int,TESObjectREFR*> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00527770 | NiTMap | proven | src/fallout/ai/actorpackage.cpp:417 |

### NiTMap_S (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00405430 | RemoveKey | decomp | src/fallout/ai/actor.cpp:18877 |

### NonLinearInterpolator (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00946190 | GetCurrent | proven | src/fallout/ai/playercharacter.cpp:15164 |
| 0x00946020 | Setup | proven | src/fallout/ai/playercharacter.cpp:15119 |

### ns8c5b10 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C5B10 | OnSleepDeprivationStageChanged | decomp | src/fallout/ai/actor_magic.cpp:7884 |

### NvOuter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C61A0 | ComputeTotal | decomp | src/fallout/ai/actorpackage.cpp:800 |

### Obj (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA070 | FUN_008ca070 | probable | src/fallout/ai/aitaskmanager.cpp:3332 |
| 0x00912DB0 | StartPackagePathing | class | src/fallout/ai/lowprocess.cpp:11581 |
| 0x008E0B00 | UpdatePackageState | class | src/fallout/ai/highprocess.cpp:32076 |

### Obj117 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094AE40 | FUN_0094ae40 | unnamed | src/fallout/ai/playercharacter.cpp:20239 |

### Obj120 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DDDF0 | UpdatePackageExecution | class | src/fallout/ai/highprocess.cpp:30678 |

### Obj_008c9a80 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9A80 | PushItem | decomp | src/fallout/ai/aitaskmanager.cpp:582 |

### Obj_008c9cf0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9CF0 | FUN_008c9cf0 | probable | src/fallout/ai/aitaskmanager.cpp:3474 |

### Obj_008ca620 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA620 | PopNode | class | src/fallout/ai/aitaskmanager.cpp:1146 |

### Obj_930 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00930C50 | HasEntries | decomp | src/fallout/ai/actor.cpp:94941 |

### ObjB300 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BF300 | ApplyScale | decomp | src/fallout/ai/combat/projectile.cpp:11602 |

### ObjQ (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00910310 | ResetAndClear | class | src/fallout/ai/lowprocess.cpp:12351 |

### OSInputGlobals (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00A24180 | GetKeyState | proven | src/fallout/ai/playercharacter.cpp:57369 |
| 0x00A24280 | SetControlHeld | proven | src/fallout/ai/playercharacter.cpp:57415 |

### Outer008848e0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008848E0 | FUN_008848e0 | probable | src/fallout/ai/actor.cpp:36158 |

### Outer008a0330 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A0330 | CallInnerVFunc139 | decomp | src/fallout/ai/actor.cpp:37419 |

### Outer8BCB00 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BCB00 | FUN_008bcb00 | unnamed | src/fallout/ai/actor.cpp:40821 |

### Outer9819 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009819D0 | FUN_009819d0 | unnamed | src/fallout/ai/combatcontroller.cpp:1365 |

### Outer_997440 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00997440 | CopyRefValue | decomp | src/fallout/ai/combat/combatstate.cpp:547 |

### Outer_9dcbf0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DCBF0 | FUN_009dcbf0 | probable | src/fallout/ai/movement/actormover.cpp:1447 |

### OuterObj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00981420 | FUN_00981420 | probable | src/fallout/ai/combatcontroller.cpp:608 |

### Owner (6)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008CA040 | CallMidVirtualB | decomp | src/fallout/ai/aitaskmanager.cpp:1070 |
| 0x008C64D0 | FUN_008c64d0 | probable | src/fallout/ai/actorpackage.cpp:992 |
| 0x0093DF50 | FUN_0093df50 | probable | src/fallout/ai/playercharacter.cpp:12113 |
| 0x00930810 | ReleaseCharacterController | class | src/fallout/ai/mobileobject.cpp:11589 |
| 0x0097FC40 | ReleaseIfFlagged | decomp | src/fallout/ai/combatcontroller.cpp:488 |
| 0x008C84C0 | UpdateProjectile | class | src/fallout/ai/aitaskmanager.cpp:3054 |

### Owner008a0360 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A0360 | FUN_008a0360 | class | src/fallout/ai/actor.cpp:37443 |

### Owner277 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00933010 | PlaySoundAtOwner | decomp | src/fallout/ai/mobileobject.cpp:9997 |

### Owner435 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A17A0 | SaveToStream | decomp | src/fallout/ai/combat/combatstate.cpp:9407 |

### Owner5610 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C5610 | UpdateStageChange | decomp | src/fallout/ai/actor_magic.cpp:5336 |

### Owner8ffe50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FFE50 | AddTargetIfEligible | decomp | src/fallout/ai/highprocess.cpp:50833 |

### Owner911ed0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00911ED0 | FUN_00911ed0 | class | src/fallout/ai/lowprocess.cpp:3142 |

### Owner93 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E51B0 | UpdateSelectionTimer | decomp | src/fallout/ai/highprocess.cpp:34696 |

### Owner933 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00933890 | SetFlagAndCullNodes | class | src/fallout/ai/actor.cpp:95573 |

### Owner93dd80 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093DD80 | FUN_0093dd80 | unnamed | src/fallout/ai/playercharacter.cpp:11931 |

### Owner96 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096DCB0 | UpdateActorsFromList | decomp | src/fallout/ai/processlists.cpp:13380 |

### OwnerProxy (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090CDC0 | RemoveById | class | src/fallout/ai/lowprocess.cpp:7416 |
| 0x009ED700 | SaveBackupPackage | class | src/fallout/ai/backuppackage.cpp:437 |

### OwnerS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00962030 | PlaySound | decomp | src/fallout/ai/playercharacter.cpp:42525 |

### OwnerStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008858C0 | UpdateDetectionFlags | decomp | src/fallout/ai/processlists.cpp:8774 |

### OwnQ (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00975450 | GetTotalSize | decomp | src/fallout/ai/processlists.cpp:16035 |
| 0x008C9D70 | InitMemory | decomp | src/fallout/ai/aitaskmanager.cpp:3445 |

### p076::Shell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A6CE0 | FUN_008a6ce0 | probable | src/fallout/ai/actor.cpp:70503 |

### p07::DelStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BC890 | Destroy | decomp | src/fallout/ai/combat/projectile.cpp:139 |

### P09A (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AAD40 | FUN_008aad40 | unnamed | src/fallout/ai/actor.cpp:43380 |

### P09Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00885BF0 | GetPerkModifiedValue | class | src/fallout/ai/actor.cpp:41933 |

### P09ActorH (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00881360 | SetActorValue | class | src/fallout/ai/actor.cpp:44510 |

### P09X (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AC9D0 | FUN_008ac9d0 | unnamed | src/fallout/ai/actor.cpp:29120 |

### P114Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00916DF0 | FUN_00916df0 | class | src/fallout/ai/middlehighprocess.cpp:15410 |

### P124Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00927D70 | UpdateFurnitureAnimation | class | src/fallout/ai/middlehighprocess.cpp:28122 |

### P157Target (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F2610 | FUN_008f2610 | probable | src/fallout/ai/highprocess.cpp:43100 |

### PackageApproach::PackageHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008EE3E0 | FUN_008ee3e0 | class | src/fallout/ai/highprocess.cpp:63724 |

### PackageEvaluationDetail::PackageProcessView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00917DF0 | FUN_00917df0 | class | src/fallout/ai/middlehighprocess.cpp:41493 |

### PackageMovement::Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E7C70 | ProcessActorMovement | decomp | src/fallout/ai/highprocess.cpp:35732 |

### PackageProcess (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DB240 | FUN_008db240 | probable | src/fallout/ai/highprocess.cpp:28908 |
| 0x0091BC60 | UpdatePackage | class | src/fallout/ai/middlehighprocess.cpp:18978 |

### PackageProcW_1d50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E1D50 | FUN_009e1d50 | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:10710 |

### PackageReader (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009ED8D0 | LoadPackageBlock | class | src/fallout/ai/backuppackage.cpp:872 |

### PackageUpdateTaskData (5)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8B20 | 'scalar deleting destructor' | proven | src/fallout/ai/aitaskmanager.cpp:327 |
| 0x008C8B70 | FUN_008c8b70 | class | src/fallout/ai/aitaskmanager.cpp:1506 |
| 0x008C8AE0 | PackageUpdateTaskData | proven | src/fallout/ai/aitaskmanager.cpp:1479 |
| 0x008C8FF0 | RunPackageUpdateTask | class | src/fallout/ai/aitaskmanager.cpp:379 |
| 0x008C8B50 | ~PackageUpdateTaskData | proven | src/fallout/ai/aitaskmanager.cpp:343 |

### ParticleTable (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7C3A0 | FUN_00c7c3a0 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:2203 |

### PathAngles (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E4450 | GetPathAngles | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:7725 |

### PathSerializationData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E8F80 | Serialize | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:6541 |

### PatrolData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F2EA0 | AdvancePatrolIndex | decomp | src/fallout/ai/patrolpackage.cpp:607 |

### PatrolData2 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F31C0 | SelectClosestPatrolPoint | decomp | src/fallout/ai/patrolpackage.cpp:844 |

### Pawn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008935F0 | TryAttack | decomp | src/fallout/ai/actor.cpp:60452 |

### PC7d (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966D70 | FUN_00966d70 | unnamed | src/fallout/ai/playercharacter.cpp:48336 |
| 0x0095F210 | LoadIdleAnimations | decomp | src/fallout/ai/playercharacter.cpp:41157 |

### PC962 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00962450 | FUN_00962450 | probable | src/fallout/ai/playercharacter.cpp:43092 |

### PC_00891190 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891190 | FUN_00891190 | probable | src/fallout/ai/actor.cpp:118885 |

### PCShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093ACB0 | FUN_0093acb0 | unnamed | src/fallout/ai/actor.cpp:31996 |

### PCTravelStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00947B10 | FUN_00947b10 | probable | src/fallout/ai/playercharacter.cpp:16058 |

### PendingProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00915870 | RemovePendingByGroupAndValue | class | src/fallout/ai/middlehighprocess.cpp:15107 |

### PerkCharacter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00963B20 | RegisterPerk | class | src/fallout/ai/playercharacter.cpp:44913 |

### PickPocketWarningState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966E50 | FUN_00966e50 | unnamed | src/fallout/ai/playercharacter.cpp:69046 |

### PickupSoundActorView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ADCF0 | FUN_008adcf0 | probable | src/fallout/ai/actor_rtti2_variant.cpp:123 |

### pkg902::Self (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00902290 | FUN_00902290 | class | src/fallout/ai/highprocess.cpp:69916 |

### PkgX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E8800 | IsPathClear | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:9299 |

### PlaceHolder008acfa0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ACFA0 | FUN_008acfa0 | unnamed | src/fallout/ai/actor.cpp:39814 |

### Planner9f48 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099F480 | TryAssignAllyTarget | decomp | src/fallout/ai/combat/combatstate.cpp:10557 |

### Player (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009614B0 | FUN_009614b0 | probable | src/fallout/ai/playercharacter.cpp:58408 |

### PlayerAIControl (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093A6F0 | FUN_0093a6f0 | probable | src/fallout/ai/playercharacter.cpp:68941 |

### PlayerAudio (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00962DE0 | FUN_00962de0 | class | src/fallout/ai/playercharacter.cpp:63904 |

### PlayerCellQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093BBA0 | FUN_0093bba0 | unnamed | src/fallout/ai/playercharacter.cpp:6001 |

### PlayerCharacter_stand_in_00958fc0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00958FC0 | FUN_00958fc0 | unnamed | src/fallout/ai/playercharacter.cpp:36394 |

### PlayerCharacter_StandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095D0B0 | AddMagicItem | decomp | src/fallout/ai/playercharacter.cpp:38923 |

### PlayerCharacterCaster (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00939680 | FUN_00939680 | unnamed | src/fallout/ai/actor.cpp:115363 |

### PlayerCharacterStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00952BA0 | FUN_00952ba0 | unnamed | src/fallout/ai/playercharacter.cpp:31070 |

### PlayerCharacterStandin (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093B3A0 | FUN_0093b3a0 | class | src/fallout/ai/playercharacter.cpp:5043 |

### PlayerCharacterValueUpdates (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093AE80 | FUN_0093ae80 | class | src/fallout/ai/playercharacter.cpp:3502 |

### PlayerCharShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966C60 | GetTerminalAccessResult | decomp | src/fallout/ai/playercharacter.cpp:48282 |

### PlayerL (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00928A50 | FUN_00928a50 | unnamed | src/fallout/ai/middlehighprocess_o2_variant_od_oy_noo2_variant.cpp:836 |

### PlayerListCleanup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00948050 | FUN_00948050 | unnamed | src/fallout/ai/playercharacter.cpp:69180 |

### PlayerMarkerOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00952E60 | PlaceMarker | decomp | src/fallout/ai/playercharacter.cpp:31732 |

### PlayerNearbyRefs (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00969930 | FUN_00969930 | probable | src/fallout/ai/playercharacter.cpp:56158 |

### PlayerNoteRemoval (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966B80 | FUN_00966b80 | unnamed | src/fallout/ai/playercharacter.cpp:69128 |

### PlayerStub (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093B0F0 | ApplyModValue | class | src/fallout/ai/playercharacter.cpp:4274 |
| 0x00953D80 | GoToLocation | decomp | src/fallout/ai/playercharacter.cpp:32985 |

### PlayerView (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BB650 | SetActiveState | decomp | src/fallout/ai/actor.cpp:86166 |
| 0x00963EB0 | SetEffectValue | decomp | src/fallout/ai/playercharacter.cpp:46276 |

### PlayerX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00948310 | FUN_00948310 | probable | src/fallout/ai/playercharacter.cpp:17621 |

### PlayerXP_ (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D5100 | AddExperience | decomp | src/fallout/ai/actor.cpp:31959 |

### PLTempEffectSaver (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009756C0 | SaveTempEffects | decomp | src/fallout/ai/processlists.cpp:6926 |

### Point3Offset (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00439E90 | ProjectileLaunched | decomp | src/fallout/ai/combatcontroller.cpp:6 |

### PoseOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C79680 | FUN_00c79680 | class | src/fallout/ai/actor_o2_nood_variant_rtm_variant.cpp:3826 |

### PoseState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CDA4C0 | FUN_00cda4c0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:2603 |

### Proc (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0090F0E0 | GetProcedureCell | class | src/fallout/ai/lowprocess.cpp:9535 |
| 0x0091F6C0 | ProcessActorInteraction | class | src/fallout/ai/middlehighprocess.cpp:21725 |

### Proc104 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F3940 | FUN_008f3940 | class | src/fallout/ai/highprocess.cpp:44599 |

### Proc9 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929FC0 | UpdatePackageState | class | src/fallout/ai/middlehighprocess.cpp:29051 |

### Procedure052 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D7D00 | UpdateMovementRequest | decomp | src/fallout/ai/combat/combatproceduremove.cpp:1765 |

### Procedure98 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CF570 | UpdateState | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:3827 |

### Process (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009177D0 | UpdateTargetSelection | class | src/fallout/ai/middlehighprocess.cpp:16296 |

### Process17 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008EBC60 | ProcessPackage | class | src/fallout/ai/highprocess.cpp:38067 |

### Process59 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901C70 | UpdateIdleProcess | class | src/fallout/ai/highprocess.cpp:53436 |

### Process63 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ED420 | FUN_008ed420 | class | src/fallout/ai/highprocess.cpp:41235 |

### Process65 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DF1E0 | FUN_008df1e0 | probable | src/fallout/ai/highprocess.cpp:31657 |

### Process8db4 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DB4F0 | SelectTarget | decomp | src/fallout/ai/highprocess.cpp:29229 |

### ProcessActivate::ActProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00915F10 | FUN_00915f10 | class | src/fallout/ai/middlehighprocess.cpp:32373 |

### ProcessDDA (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DDAC0 | ProcessActorPackage | class | src/fallout/ai/highprocess.cpp:29939 |

### ProcessListsEx (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00974E90 | FUN_00974e90 | probable | src/fallout/ai/processlists.cpp:6880 |
| 0x009723F0 | UpdateCrimeLists | decomp | src/fallout/ai/processlists.cpp:13073 |

### ProcessListsHigh (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096BCD0 | FUN_0096bcd0 | probable | src/fallout/ai/processlists.cpp:1697 |

### ProcessListsSub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00975D10 | UpdateActor3D | decomp | src/fallout/ai/processlists.cpp:12689 |

### ProcessProxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FF0B0 | FUN_008ff0b0 | probable | src/fallout/ai/highprocess.cpp:21968 |

### ProcessShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E26E0 | UpdateDialogueTarget | class | src/fallout/ai/highprocess.cpp:60928 |

### ProcessStub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F9180 | FUN_008f9180 | unnamed | src/fallout/ai/highprocess.cpp:20662 |

### ProcessUpdate (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00915BC0 | FUN_00915bc0 | class | src/fallout/ai/middlehighprocess.cpp:7772 |

### ProcessUseItem::UseProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091C810 | FUN_0091c810 | unnamed | src/fallout/ai/middlehighprocess.cpp:42245 |

### ProcessView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091F130 | FUN_0091f130 | class | src/fallout/ai/middlehighprocess.cpp:21166 |

### ProcListsExt (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096CDA0 | FUN_0096cda0 | probable | src/fallout/ai/processlists.cpp:5937 |

### ProcObj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929960 | FUN_00929960 | unnamed | src/fallout/ai/middlehighprocess.cpp:28692 |

### ProcX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DBE30 | UpdateDialogue | class | src/fallout/ai/highprocess.cpp:15910 |

### ProjCls (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AE6E0 | FUN_009ae6e0 | probable | src/fallout/ai/combat/explosion_o2_variant_od_oy_noo2_variant.cpp:2162 |

### Projectile (27)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BBC40 | 'scalar deleting destructor' | proven | src/fallout/ai/combat/projectile.cpp:11989 |
| 0x009C2E80 | ApplyImpactForce | proven | src/fallout/ai/combat/projectile_o2_variant_od_oy_noo2_variant.cpp:1741 |
| 0x009C39E0 | CheckExplosionProximity | proven | src/fallout/ai/combat/projectile.cpp:11916 |
| 0x009C4C80 | CheckRefDeleted | proven | src/fallout/ai/combat/projectile.cpp:9041 |
| 0x009C5870 | FinishLoadGame | proven | src/fallout/ai/combat/projectile.cpp:617 |
| 0x00960520 | FUN_00960520 | probable | src/fallout/ai/playercharacter_o2_variant_od_oy_noo2_variant.cpp:1512 |
| 0x00979260 | GetFirstLightParameter | decomp | src/fallout/ai/combat/beamprojectile.cpp:32 |
| 0x009C3930 | GetMineReactsToTarget | proven | src/fallout/ai/combat/projectile.cpp:2255 |
| 0x009BDFF0 | Init3D | proven | src/fallout/ai/combat/projectile.cpp:1252 |
| 0x009BE0A0 | InitHavok | proven | src/fallout/ai/mobileobject_o2_variant_od_oy_noo2_variant.cpp:1615 |
| 0x0087E130 | InitRagdollController | decomp | src/fallout/ai/actor.cpp:47419 |
| 0x009BD830 | Load | class | src/fallout/ai/combat/projectile.cpp:15 |
| 0x009C4B60 | MoveToLow | proven | src/fallout/ai/combat/projectile.cpp:8949 |
| 0x009C4A40 | MoveToMiddleLow | proven | src/fallout/ai/combat/projectile.cpp:4692 |
| 0x009C5AF0 | PickAutoWater | proven | src/fallout/ai/combat/projectile.cpp:2383 |
| 0x009BBC70 | Projectile | proven | src/fallout/ai/combat/projectile.cpp:31 |
| 0x009BBEF0 | Projectile | proven | src/fallout/ai/combat/projectile.cpp:5231 |
| 0x009C58E0 | Revert | proven | src/fallout/ai/combat/projectile.cpp:11298 |
| 0x009C03F0 | RunTargetPick | proven | src/fallout/ai/combat/projectile_o2_variant_od_oy_noo2_variant.cpp:1546 |
| 0x00978ED0 | SetActorCause | proven | src/fallout/ai/combat/beamprojectile.cpp:19 |
| 0x009C4E60 | SetMovementDelta | proven | src/fallout/ai/combat/projectile.cpp:561 |
| 0x009795C0 | SetRange | proven | src/fallout/ai/combat/beamprojectile.cpp:44 |
| 0x009C47D0 | StartHighProcess | proven | src/fallout/ai/combat/projectile.cpp:4560 |
| 0x009C43E0 | TurnOff | proven | src/fallout/ai/combat/beamprojectile.cpp:1034 |
| 0x009BECC0 | Update | proven | src/fallout/ai/combat/projectile_o2_variant_od_oy_noo2_variant.cpp:390 |
| 0x009C3E60 | UpdateLight | proven | src/fallout/ai/combat/projectile.cpp:493 |
| 0x009BC470 | ~Projectile | proven | src/fallout/ai/combat/projectile.cpp:12208 |

### Projectile9B3 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B3CD0 | CanProcessHit | class | src/fallout/ai/combat/flameprojectile.cpp:756 |

### Projectile9b34 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B34C0 | UpdateProjectile | class | src/fallout/ai/combat/projectile.cpp:10890 |

### Projectile_ImpactData (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BBB40 | FinishLoadGame | proven | src/fallout/ai/combat/projectile.cpp:1085 |
| 0x009BBA90 | LoadGame | proven | src/fallout/ai/combat/projectile.cpp:918 |
| 0x009BB970 | SaveGame | proven | src/fallout/ai/combat/projectile.cpp:3076 |

### ProjectileBlastSearch (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C6380 | FUN_009c6380 | probable | src/fallout/ai/combat/projectile.cpp:12319 |

### ProjectileHelper (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C4FF0 | SaveProjectile | class | src/fallout/ai/combat/projectile.cpp:10982 |

### ProjectileHit (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BF5A0 | ProcessHit | class | src/fallout/ai/combat/projectile.cpp:7807 |

### ProjectileObject (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B3320 | UpdateProjectileNode | class | src/fallout/ai/combat/flameprojectile.cpp:401 |

### ProjectileRuntime (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BDA10 | FUN_009bda10 | class | src/fallout/ai/combat/projectile.cpp:6676 |

### ProjS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B7E40 | UpdateProjectileNodeVisibility | class | src/fallout/ai/combat/missileprojectile.cpp:1147 |

### ProjX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BD860 | FUN_009bd860 | probable | src/fallout/ai/combat/projectile.cpp:3754 |

### Proxy (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A51A0 | FUN_008a51a0 | unnamed | src/fallout/ai/actor.cpp:38096 |

### Proxy008d46a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D46A0 | GetFatigueValue | class | src/fallout/ai/actor.cpp:40872 |

### Proxy00917770 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00917770 | FUN_00917770 | class | src/fallout/ai/middlehighprocess.cpp:3680 |

### Proxy72800 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00672800 | FUN_00672800 | unnamed | src/fallout/ai/actor.cpp:34976 |

### Proxy88c600 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088C600 | IsTargetIn360View | decomp | src/fallout/ai/actor.cpp:36792 |

### ProxyActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D47F0 | GetActorBaseValue | class | src/fallout/ai/actor.cpp:40898 |

### PRProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A1400 | SetMode | decomp | src/fallout/ai/highprocess.cpp:56592 |

### PtrArrayView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E98D0 | FUN_009e98d0 | unnamed | src/fallout/ai/movement/detailedactorpathhandler.cpp:6615 |

### QueryOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00560BC0 | FUN_00560bc0 | probable | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:844 |

### QueuedItem (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00913E80 | LoadGame | proven | src/fallout/ai/middlehighprocess.cpp:41061 |
| 0x00913A20 | QueueFiles | proven | src/fallout/ai/middlehighprocess.cpp:14624 |
| 0x00913D60 | SaveGame | proven | src/fallout/ai/middlehighprocess.cpp:41406 |

### QueueProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009154B0 | ProcessQueuedItems | class | src/fallout/ai/middlehighprocess.cpp:15022 |

### R_008b8f20 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B8F20 | FUN_008b8f20 | unnamed | src/fallout/ai/actor.cpp:11410 |

### RagController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C75580 | FUN_00c75580 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1501 |

### RagdollAnimControllerView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7A8D0 | FUN_00c7a8d0 | probable | src/fallout/ai/actor_o2_variant.cpp:3963 |

### RagdollCtl (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7C150 | FUN_00c7c150 | unnamed | src/fallout/ai/actor_o2_variant.cpp:2352 |

### RagdollUpdateController (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7D030 | FUN_00c7d030 | class | src/fallout/ai/actor_o2_nood_variant.cpp:2670 |

### RangedDebug (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D1E80 | PrintDebugInfo | class | src/fallout/ai/combat/combatprocedureattackranged.cpp:2253 |

### RangedFromCoverStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097B070 | FUN_0097b070 | class | src/fallout/ai/combat/combatactions.cpp:389 |

### RAttack (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D0A30 | UpdateAttack | class | src/fallout/ai/combat/combatprocedureattackranged.cpp:1333 |

### Ref (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BC300 | FUN_008bc300 | probable | src/fallout/ai/actor.cpp:32709 |

### ref87f::R8Ref (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087F260 | FUN_0087f260 | probable | src/fallout/ai/actor.cpp:142654 |

### Ref8BC (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BCBD0 | CopyScaleAndResetItems | decomp | src/fallout/ai/actor.cpp:88003 |

### Ref9bf (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BF470 | UpdateNodeTransform | decomp | src/fallout/ai/combat/projectile.cpp:9528 |

### Ref_891d30 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891D30 | FUN_00891d30 | probable | src/fallout/ai/actor.cpp:114835 |

### RefX (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009ACD60 | UpdateExplosion | class | src/fallout/ai/combat/explosion.cpp:2900 |

### RelationOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00967730 | FUN_00967730 | probable | src/fallout/ai/playercharacter.cpp:51392 |

### RemovalArray (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EF10 | FUN_0098ef10 | unnamed | src/fallout/ai/combat/combatgroup.cpp:5863 |

### RenderNode (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7DE60 | FUN_00c7de60 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:1691 |

### ResetActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089F780 | FUN_0089f780 | class | src/fallout/ai/actor.cpp:66607 |

### ResetHighProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FC210 | ResetHighProcessState | class | src/fallout/ai/highprocess.cpp:49024 |

### ResetPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095C9C0 | FUN_0095c9c0 | unnamed | src/fallout/ai/playercharacter.cpp:38721 |

### ResetProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00923C60 | ResetForActor | class | src/fallout/ai/middlehighprocess.cpp:10179 |

### ResistanceTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C40E0 | FUN_008c40e0 | unnamed | src/fallout/ai/actor.cpp:141954 |

### ResponseProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ECF20 | HandleResponse | class | src/fallout/ai/highprocess.cpp:39993 |

### RestoreActionPointsDetail::RestoreActionPointsEntry (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088B660 | FUN_0088b660 | probable | src/fallout/ai/actor.cpp:144958 |

### ResultQuery (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989140 | TryGetQuadForState | decomp | src/fallout/ai/combat/combatgroup.cpp:3487 |

### ReviewedContext (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7B4F0 | FUN_00c7b4f0 | unnamed | src/fallout/ai/actor_o2_nood_variant_rtm_variant.cpp:4048 |

### RigidBodyOwnerL (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00926980 | FUN_00926980 | unnamed | src/fallout/ai/middlehighprocess_o2_variant_od_oy_noo2_variant.cpp:34 |

### RockItAmmoCountDetail::PlayerView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00969040 | FUN_00969040 | unnamed | src/fallout/ai/playercharacter.cpp:69072 |

### S008a69d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A69D0 | FUN_008a69d0 | probable | src/fallout/ai/actor.cpp:38973 |

### S008b0ac0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B0AC0 | FUN_008b0ac0 | unnamed | src/fallout/ai/actor.cpp:40002 |

### S008b39a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B39A0 | ForwardToP190 | decomp | src/fallout/ai/actor.cpp:40194 |

### S008da3d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DA3D0 | GetFileEntry | decomp | src/fallout/ai/highprocess.cpp:4956 |

### S008daef0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DAEF0 | CallVcall800 | class | src/fallout/ai/highprocess.cpp:5007 |

### S00901660 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901660 | FindFirstSetByte | class | src/fallout/ai/highprocess.cpp:6392 |

### S00903f50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00903F50 | FreeField | class | src/fallout/ai/highprocess.cpp:6512 |

### S00926350_Target926350 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00926350 | FUN_00926350 | unnamed | src/fallout/ai/middlehighprocess.cpp:42789 |

### S0092f160 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092F160 | FUN_0092f160 | probable | src/fallout/ai/mobileobject.cpp:1973 |

### S009afc70 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AFC70 | FUN_009afc70 | unnamed | src/fallout/ai/combat/explosion.cpp:445 |

### S009ce870 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CE870 | FUN_009ce870 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:2776 |

### S009d8440 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D8440 | FUN_009d8440 | unnamed | src/fallout/ai/combat/combatproceduremove.cpp:54 |

### S009dccf0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DCCF0 | FUN_009dccf0 | probable | src/fallout/ai/movement/actormover.cpp:1600 |

### S009f8f60 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8F60 | FUN_009f8f60 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:306 |

### S5460 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A3480 | FUN_009a3480 | unnamed | src/fallout/ai/combat/combatstate.cpp:3691 |

### S5620 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E5620 | GetNiPoint3 | decomp | src/fallout/ai/highprocess.cpp:3899 |

### S5870_Holder (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009BABE0 | FUN_009babe0 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:621 |
| 0x009BAB20 | LoadForm | class | src/fallout/ai/combat/missileprojectile.cpp:453 |

### S89 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0089FCF0 | FUN_0089fcf0 | class | src/fallout/ai/actor.cpp:106417 |

### s891b90::Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00891B90 | FUN_00891b90 | probable | src/fallout/ai/actor.cpp:114621 |

### S913460 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00913460 | IsPackageProcedureAllowed | class | src/fallout/ai/lowprocess.cpp:3313 |

### S953f20 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00953F20 | GetWrappedAngle | class | src/fallout/ai/actor.cpp:41229 |

### S9790 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B9790 | FUN_008b9790 | unnamed | src/fallout/ai/actor.cpp:40303 |

### S981990 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00981990 | FUN_00981990 | probable | src/fallout/ai/combatcontroller.cpp:1348 |

### S9b41b0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B41B0 | Update | class | src/fallout/ai/combat/projectile.cpp:11546 |

### S9b46c0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B46C0 | SetLightEnabled | class | src/fallout/ai/combat/grenadeprojectile.cpp:275 |

### S9c_Actor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C0090 | FUN_009c0090 | probable | src/fallout/ai/combat/projectile_o2_variant_od_oy_noo2_variant.cpp:953 |

### S_00884e30 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00884E30 | FUN_00884e30 | unnamed | src/fallout/ai/actor.cpp:3437 |

### S_008a0c60_Obj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A0C60 | GetOrInitValue | decomp | src/fallout/ai/actor.cpp:66990 |

### S_008a51f0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A51F0 | DispatchProcessTarget | decomp | src/fallout/ai/actor.cpp:38136 |

### S_008a8840 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A8840 | FUN_008a8840 | probable | src/fallout/ai/actor.cpp:39531 |

### S_008ace10 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008ACE50 | FUN_008ace50 | probable | src/fallout/ai/actor.cpp:39768 |

### S_008be2f0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE2F0 | FUN_008be2f0 | unnamed | src/fallout/ai/actor.cpp:88210 |

### S_008be870_Obj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BE870 | FUN_008be870 | unnamed | src/fallout/ai/actor.cpp:88486 |

### S_008d90b0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D90B0 | AddTime | class | src/fallout/ai/highprocess.cpp:4804 |

### S_008d9890 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D9890 | DestroyHighProcess | decomp | src/fallout/ai/highprocess.cpp:4919 |

### S_00905f30_Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00905F30 | StartLipSyncTask | decomp | src/fallout/ai/lipsyncbackgroundmanager.cpp:735 |

### S_0092adb0_Proc (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092ADB0 | CheckPackageAndRun | class | src/fallout/ai/middlehighprocess.cpp:12426 |

### S_00979140_Proj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00979140 | FUN_00979140 | class | src/fallout/ai/combat/beamprojectile.cpp:1459 |

### S_00979a70 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00979A70 | ScaleNode | decomp | src/fallout/ai/combat/beamprojectile.cpp:1840 |

### S_009ab280_Proj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AB280 | InitContinuousBeam | class | src/fallout/ai/combat/continuousbeamprojectile.cpp:489 |

### S_009c8c40 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C8C40 | SetValue | decomp | src/fallout/ai/combat/vats.cpp:510 |

### S_009d6750 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D6750 | PrintState | class | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:133 |

### S_009e3520 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E3520 | UpdateSpeed | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:220 |

### S_9292e0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009292E0 | FUN_009292e0 | class | src/fallout/ai/middlehighprocess.cpp:12335 |

### S_972600_Lists (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00972600 | HasMatchingCrime | decomp | src/fallout/ai/processlists.cpp:6183 |

### S_972aa0_Owner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00972AA0 | RemoveCrimeById | decomp | src/fallout/ai/processlists.cpp:12279 |

### S_984af0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00984AF0 | DestroyIfFlagged | decomp | src/fallout/ai/combat/combatgoal.cpp:472 |

### SActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009037E0 | PlayWeaponAnim | decomp | src/fallout/ai/highprocess.cpp:25261 |
| 0x00892520 | ProcessFormInteraction | class | src/fallout/ai/actor.cpp:59187 |

### SandBoxActorPackageData_ext (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F4700 | SelectSandboxActivity | decomp | src/fallout/ai/sandboxpackage.cpp:692 |

### SandBoxChoiceListItem (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F3800 | SandBoxChoiceListItem | proven | src/fallout/ai/sandboxpackage.cpp:915 |

### SandboxTargetData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F3AF0 | FUN_009f3af0 | probable | src/fallout/ai/sandboxpackage.cpp:1813 |

### SaveGameRecordWriter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00926490 | SaveActorRecord | decomp | src/fallout/ai/middlehighprocess.cpp:10400 |

### SaveProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00928880 | SaveControllerState | decomp | src/fallout/ai/middlehighprocess.cpp:12179 |

### SaveProcessLists (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009755B0 | FUN_009755b0 | unnamed | src/fallout/ai/processlists.cpp:12630 |

### Saver (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F86F0 | FUN_009f86f0 | class | src/fallout/ai/spectatorpackage_od_variant.cpp:139 |

### SceneOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7E9A0 | FUN_00c7e9a0 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:730 |

### ScriptableFormForward (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CC4B0 | FUN_009cc4b0 | class | src/fallout/ai/combat/combatprocedureactivateobject.cpp:718 |

### ScScaler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009ABA90 | ScaleObject | decomp | src/fallout/ai/combat/continuousbeamprojectile.cpp:682 |

### SearchC (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099C230 | FindPathCandidate | decomp | src/fallout/ai/combat/combatstate.cpp:7644 |

### SearchDiagnostics::Search (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D9FD0 | PrintDebugInfo | class | src/fallout/ai/combat/combatproceduresearch.cpp:569 |

### SearchOwner (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B1720 | FindEntryResultByCategory | decomp | src/fallout/ai/combat/explosion.cpp:1202 |
| 0x008EEBF0 | FUN_008eebf0 | class | src/fallout/ai/highprocess.cpp:42498 |

### SearchProcedure (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009D8D40 | UpdateSearchState | class | src/fallout/ai/combat/combatproceduresearch.cpp:1105 |

### SearchProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00910E20 | CollectSearchResults | decomp | src/fallout/ai/lowprocess.cpp:10890 |

### SelectingActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A3ED0 | SelectTarget | decomp | src/fallout/ai/actor.cpp:68329 |

### Self (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A1BD0 | PlaySoundOnObject | class | src/fallout/ai/character.cpp:1341 |

### Self_8a2fa0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A2FA0 | GetHeadPosition | class | src/fallout/ai/actor.cpp:67554 |

### SettingT<GameSettingCollection> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0040E0B0 | SettingT | proven | src/fallout/ai/movement/actormover.cpp:138 |

### SettingT<INISettingCollection> (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00408D60 | Bool | probable | src/fallout/ai/processlists.cpp:285 |

### ShapeArrays (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7C2B0 | ~ShapeArrays | decomp | src/fallout/ai/actor_o2_variant.cpp:2685 |

### Shell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00973710 | GetHighestDetectionValue | decomp | src/fallout/ai/processlists.cpp:15385 |

### Shell914 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00914C60 | FUN_00914c60 | unnamed | src/fallout/ai/middlehighprocess.cpp:7617 |

### Shell_8803a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008803A0 | FUN_008803a0 | probable | src/fallout/ai/actor.cpp:116643 |

### SimpleArrayRemove (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098EBE0 | FUN_0098ebe0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:5823 |

### SkeletonBuild::AnimationOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7E3B0 | FUN_00c7e3b0 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:4018 |

### SkeletonPoseData (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00CDA340 | FUN_00cda340 | unnamed | src/fallout/ai/actor_o2_gs_nood_nogs_variant.cpp:220 |

### SoundListView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C71A0 | AddCommand | decomp | src/fallout/ai/combat/vats.cpp:150 |

### SpectatorInfo (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F6F30 | FUN_009f6f30 | probable | src/fallout/ai/spectatorpackage_od_variant.cpp:1707 |

### SpectatorPackageStandIn (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8420 | FUN_009f8420 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:583 |

### SpectatorThreatInfo (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F7230 | InitLoadGame | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:373 |
| 0x009F7170 | LoadGame | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:83 |
| 0x009F70B0 | SaveGame | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:56 |
| 0x009F6D50 | Update | proven | src/fallout/ai/spectatorpackage_od_variant.cpp:972 |

### SpectatorThreatInfo62d0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F7630 | FUN_009f7630 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:492 |

### SpellProc (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009613C0 | FUN_009613c0 | probable | src/fallout/ai/playercharacter.cpp:41791 |

### SSProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00920D00 | UpdateSitSleepState | class | src/fallout/ai/middlehighprocess.cpp:8849 |

### ST_008c8bb0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8BB0 | FUN_008c8bb0 | unnamed | src/fallout/ai/aitaskmanager.cpp:34 |

### ST_00931e50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C6330 | FUN_009c6330 | unnamed | src/fallout/ai/combat/projectile.cpp:823 |

### ST_8dd8a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DD8A0 | FUN_008dd8a0 | class | src/fallout/ai/highprocess.cpp:5225 |

### StandIn (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00907430 | CallTargetWithFloat | class | src/fallout/ai/middlelowprocess.cpp:424 |
| 0x008C1680 | FUN_008c1680 | unnamed | src/fallout/ai/actor.cpp:40841 |

### Standin00898ff0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00898FF0 | FUN_00898ff0 | unnamed | src/fallout/ai/actor.cpp:36868 |

### StandIn009DE3E0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DE3E0 | FUN_009de3e0 | unnamed | src/fallout/ai/movement/actormover.cpp:1678 |

### StandIn_008d9360 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D9360 | AddAttacks | class | src/fallout/ai/highprocess.cpp:4838 |

### StandIn_00929220 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00929220 | FUN_00929220 | unnamed | src/fallout/ai/middlehighprocess.cpp:3187 |

### StandIn_00989010 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00989010 | SetTripleAndValue | decomp | src/fallout/ai/combat/combatgroup.cpp:621 |

### StandInFlame (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B3EB0 | Save | class | src/fallout/ai/combat/flameprojectile.cpp:110 |

### StandinPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095D160 | FUN_0095d160 | unnamed | src/fallout/ai/playercharacter.cpp:39144 |

### State (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00980AE0 | SetupPackageTarget | decomp | src/fallout/ai/combatcontroller.cpp:6370 |

### State057 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CFF90 | UpdateDirection | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:4854 |

### StateTracker (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00437E50 | FUN_00437e50 | unnamed | src/fallout/ai/actor.cpp:46483 |

### std (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00408840 | abs | decomp | src/fallout/ai/guardpackage.cpp:5 |

### StealWarningState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00966E00 | FUN_00966e00 | unnamed | src/fallout/ai/playercharacter.cpp:69167 |

### Strategy990640 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990640 | SortMembersByTargetDistance | decomp | src/fallout/ai/combat/combatgroupstrategy.cpp:1311 |

### Strategy990d60 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990D60 | IsGroupTargetsSpread | class | src/fallout/ai/combat/combatgroupstrategy.cpp:1260 |

### Struct_008bc520 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BC520 | FUN_008bc520 | unnamed | src/fallout/ai/actor.cpp:40758 |

### Stub8bc3d0Obj (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BC3D0 | FUN_008bc3d0 | unnamed | src/fallout/ai/actor.cpp:86838 |

### stub_TESSaveLoadGame (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0085B170 | ComputeFormTableChecksum | decomp | src/fallout/ai/actor.cpp:46869 |

### Sub (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AC8B0 | FUN_008ac8b0 | unnamed | src/fallout/ai/actor.cpp:32514 |

### Sub8bd700 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BD700 | FUN_008bd700 | unnamed | src/fallout/ai/actor.cpp:18561 |

### Subject (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009308F0 | UpdateControllerWorld | class | src/fallout/ai/actor.cpp:94865 |

### SummonOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C51F0 | DispelSummonEffects | decomp | src/fallout/ai/actor_magic.cpp:1818 |

### T (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009508F0 | FUN_009508f0 | class | src/fallout/ai/actor.cpp:41215 |

### T_ (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00887B20 | ForwardToMember | decomp | src/fallout/ai/actor.cpp:32981 |
| 0x00928D00 | ForwardToMember | decomp | src/fallout/ai/middlehighprocess.cpp:3176 |

### T_008fdb90 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008FDB90 | FUN_008fdb90 | unnamed | src/fallout/ai/highprocess.cpp:6178 |

### Target (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00903600 | GetIntAt | decomp | src/fallout/ai/highprocess.cpp:10710 |
| 0x009278D0 | ResolveReferences | class | src/fallout/ai/middlehighprocess.cpp:11281 |
| 0x00920150 | UpdateKnockedDownState | class | src/fallout/ai/middlehighprocess.cpp:23186 |
| 0x008C0EC0 | UpdateTargetUnits | decomp | src/fallout/ai/actor.cpp:89124 |

### Target008dd980 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DD980 | FUN_008dd980 | probable | src/fallout/ai/highprocess.cpp:16872 |

### Target890 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B8900 | FUN_009b8900 | class | src/fallout/ai/combat/missileprojectile.cpp:1294 |

### Target8d (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D0BC0 | LoadAndValidate | class | src/fallout/ai/baseprocess.cpp:1886 |

### Target8da (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008DA2A0 | FUN_008da2a0 | class | src/fallout/ai/highprocess.cpp:15122 |

### Target96 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0096F450 | FUN_0096f450 | unnamed | src/fallout/ai/processlists.cpp:10399 |

### Target97ff (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097FF60 | UpdateActorValues | decomp | src/fallout/ai/combatcontroller.cpp:5786 |

### TargetActor (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008860D0 | FUN_008860d0 | class | src/fallout/ai/actor.cpp:117450 |
| 0x008A6A40 | FUN_008a6a40 | rejected | src/fallout/ai/actor.cpp:121543 |

### TargetAssessmentGroup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098C870 | FUN_0098c870 | probable | src/fallout/ai/combat/combatgroup.cpp:10688 |

### TargetClass (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00990C10 | FUN_00990c10 | class | src/fallout/ai/combat/combatgroupstrategy.cpp:205 |
| 0x00CBCBD0 | FUN_00cbcbd0 | unnamed | src/fallout/ai/combat/explosion_o2_variant.cpp:921 |
| 0x00CBD520 | FUN_00cbd520 | class | src/fallout/ai/combat/explosion_o2_variant.cpp:586 |
| 0x00925490 | ResolveFormPointers | class | src/fallout/ai/middlehighprocess.cpp:26710 |

### TargetProcess (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00904F50 | FUN_00904f50 | class | src/fallout/ai/highprocess.cpp:56294 |
| 0x00924B90 | LoadFromSave | class | src/fallout/ai/middlehighprocess.cpp:30184 |

### TaskOwner (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C9E40 | DispatchTask | decomp | src/fallout/ai/aitaskmanager.cpp:2139 |
| 0x008B8F90 | ProcessTargets | decomp | src/fallout/ai/actor.cpp:82320 |

### TaskOwnerTarget (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C94E0 | FUN_008c94e0 | probable | src/fallout/ai/aitaskmanager.cpp:2612 |

### TempEffectListOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00974290 | RemoveParticleEffectsBySource | decomp | src/fallout/ai/processlists.cpp:6704 |

### TES (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3750 | CallPathMgr | decomp | src/fallout/ai/actor.cpp:10295 |
| 0x0044FB20 | TES | proven | src/fallout/ai/playercharacter.cpp:1063 |

### TESAmmoInitCalls (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00923000 | FUN_00923000 | rejected | src/fallout/ai/middlehighprocess.cpp:44 |

### TESCasino (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x007316D0 | GetChipType | proven | src/fallout/ai/actor.cpp:33748 |

### TESForm (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00440D80 | GetDelete | proven | src/fallout/ai/actor.cpp:17 |
| 0x00954910 | SetBeingDropped | proven | src/fallout/ai/playercharacter.cpp:69116 |

### TESObjectMISC (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DB930 | SetLoopingSound | decomp | src/fallout/ai/movement/actormover.cpp:116 |

### TESObjectREFR (8)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0057A740 | GetAnimNoteReceiever | proven | src/fallout/ai/actor.cpp:33694 |
| 0x00573090 | GetDismembered | proven | src/fallout/ai/mobileobject.cpp:125 |
| 0x00527080 | GetExtraData | proven | src/fallout/ai/processlists.cpp:20 |
| 0x00565690 | IsQuestObject | proven | src/fallout/ai/combat/explosion.cpp:564 |
| 0x00572230 | MarkAsPickedUp | proven | src/fallout/ai/playercharacter.cpp:1359 |
| 0x00575330 | RemoveItemType | proven | src/fallout/ai/actor.cpp:34886 |
| 0x00564DB0 | SetTargeted | proven | src/fallout/ai/movement/actormover.cpp:1033 |
| 0x00567050 | UpdateAnimation | proven | src/fallout/ai/actor.cpp:41457 |

### TESObjectREFR8B3 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B3180 | FUN_008b3180 | class | src/fallout/ai/actor.cpp:78850 |

### TESObjectWEAP (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00524B60 | GetAmmoPerShot | proven | src/fallout/ai/baseprocess.cpp:191 |
| 0x008B2BF0 | GetUse1stPersonISAnims | proven | src/fallout/ai/actor.cpp:34227 |
| 0x008B2C10 | GetUse3rdPersonISAnims | proven | src/fallout/ai/actor.cpp:78714 |

### TESReactionForm (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048BF50 | GetReaction | proven | src/fallout/ai/actor.cpp:232 |

### TESSaveLoadGame (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0085A290 | ClearFormID | proven | src/fallout/ai/alarmpackage.cpp:50 |

### TESSpellList (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0048E140 | LoadGame | proven | src/fallout/ai/alarmpackage.cpp:7 |

### TESWeightForm (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00910B10 | InitializeDataComponent | proven | src/fallout/ai/lowprocess.cpp:13413 |

### Tgt13 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DE8B0 | UpdateTargeting | decomp | src/fallout/ai/movement/actormover.cpp:5727 |

### Tgt_b (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008BB630 | FUN_008bb630 | probable | src/fallout/ai/actor.cpp:34532 |
| 0x009DBB10 | FUN_009dbb10 | unnamed | src/fallout/ai/movement/actormover.cpp:1288 |

### Thing (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00881510 | FUN_00881510 | probable | src/fallout/ai/actor.cpp:113688 |

### This (4)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AD670 | FUN_009ad670 | probable | src/fallout/ai/combat/explosion_o2_variant_od_noo2_variant.cpp:1351 |
| 0x009CC510 | FUN_009cc510 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:1731 |
| 0x008FB330 | Load | class | src/fallout/ai/highprocess.cpp:48367 |
| 0x009EFA50 | LoadSaveData | class | src/fallout/ai/dialoguepackage.cpp:1524 |

### This00902640 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00902640 | FUN_00902640 | probable | src/fallout/ai/highprocess.cpp:6441 |

### This899 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00899CB0 | SpawnProjectile | decomp | src/fallout/ai/actor.cpp:104661 |

### This8b (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B28C0 | PlayAnimationSequence | decomp | src/fallout/ai/actor.cpp:78554 |

### This8e9 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E9640 | FUN_008e9640 | class | src/fallout/ai/highprocess.cpp:62219 |

### This92 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0092B030 | FUN_0092b030 | class | src/fallout/ai/middlehighprocess.cpp:31168 |

### This_008b37c0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B37C0 | FUN_008b37c0 | probable | src/fallout/ai/actor.cpp:40172 |

### ThisC (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0088C830 | FUN_0088c830 | probable | src/fallout/ai/actor.cpp:57700 |
| 0x008C2190 | FUN_008c2190 | class | src/fallout/ai/actor.cpp:125258 |

### ThisC1 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008AC1E0 | FUN_008ac1e0 | unnamed | src/fallout/ai/actor.cpp:73116 |

### ThisCls (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091AE00 | FUN_0091ae00 | probable | src/fallout/ai/middlehighprocess.cpp:17754 |
| 0x009BB240 | UpdateMuzzleFlash | decomp | src/fallout/ai/combat/muzzleflash.cpp:802 |
| 0x009DBDC0 | UpdatePathingState | decomp | src/fallout/ai/movement/actormover.cpp:4078 |

### ThisHack (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00899030 | CallProcessVFunc316 | class | src/fallout/ai/actor.cpp:37201 |

### ThisShell (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094A0C0 | FUN_0094a0c0 | probable | src/fallout/ai/playercharacter_gf_variant.cpp:505 |

### ThisT (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00901A20 | FUN_00901a20 | class | src/fallout/ai/highprocess.cpp:52674 |

### Thr (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C7110 | InitMemory | class | src/fallout/ai/ailineartaskthread.cpp:134 |

### ThreatArray (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8B30 | FUN_009f8b30 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:1575 |

### ThreatManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00992720 | IsThreatWithinLimits | decomp | src/fallout/ai/combat/combatmanager.cpp:3055 |

### ThreatMap (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A5670 | EvaluateThreats | decomp | src/fallout/ai/combat/combatthreatmap.cpp:207 |

### Ths810 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00810FF0 | FUN_00810ff0 | probable | src/fallout/ai/mobileobject.cpp:1474 |

### Thunk0091f100 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0091F100 | FUN_0091f100 | unnamed | src/fallout/ai/middlehighprocess.cpp:3691 |

### TimeCounter (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00969B40 | FUN_00969b40 | unnamed | src/fallout/ai/playercharacter.cpp:56284 |

### TimeoutTimer (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D7F80 | CheckTimer | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:6 |
| 0x009A5F20 | LoadGame | decomp | src/fallout/ai/combat/combattimer.cpp:13 |

### TimeRefresh (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00969B20 | FUN_00969b20 | unnamed | src/fallout/ai/playercharacter.cpp:56263 |

### TransformedPosDAD (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C7F7A0 | FUN_00c7f7a0 | unnamed | src/fallout/ai/actor_o2_gs_nood_nogs_variant.cpp:110 |

### TransitionActor (3)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F7350 | ApplyTransitionToTarget | class | src/fallout/ai/highprocess.cpp:46350 |
| 0x0093D500 | FUN_0093d500 | probable | src/fallout/ai/playercharacter.cpp:10194 |
| 0x00883800 | UpdateTransition | class | src/fallout/ai/actor.cpp:53928 |

### TravelObject (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093D660 | FUN_0093d660 | probable | src/fallout/ai/playercharacter.cpp:10563 |

### TravelRef (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0093CDF0 | FUN_0093cdf0 | probable | src/fallout/ai/playercharacter.cpp:9954 |

### TrespassPackageInit (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F9660 | LoadTrespassPackage | class | src/fallout/ai/trespasspackage.cpp:95 |

### Unk (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DE110 | FUN_009de110 | unnamed | src/fallout/ai/movement/actormover.cpp:1647 |

### Unk008d49 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D4900 | FUN_008d4900 | class | src/fallout/ai/creature.cpp:160 |

### Unk008d4a50 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D4A50 | FUN_008d4a50 | class | src/fallout/ai/creature.cpp:186 |

### Unk008d8350 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D8350 | FUN_008d8350 | class | src/fallout/ai/highprocess.cpp:4526 |

### Unk009dcab0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DCAB0 | FUN_009dcab0 | unnamed | src/fallout/ai/movement/actormover.cpp:1337 |

### Unk009DE3A0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009DE3A0 | SetFormID | decomp | src/fallout/ai/movement/actormover.cpp:1661 |

### Unk147 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00914AB0 | FUN_00914ab0 | unnamed | src/fallout/ai/middlehighprocess.cpp:3646 |

### Unk3713 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00937130 | ReleaseIfFlagged | decomp | src/fallout/ai/modifierlist.cpp:247 |

### Unk68 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0087FA60 | FUN_0087fa60 | class | src/fallout/ai/actor.cpp:35299 |

### Unk80f760 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0080F760 | GetZeroPoint | decomp | src/fallout/ai/mobileobject.cpp:1451 |

### Unk_008a0680 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A0680 | FUN_008a0680 | probable | src/fallout/ai/actor.cpp:37726 |

### Unk_0097f7a0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097F7A0 | FUN_0097f7a0 | unnamed | src/fallout/ai/combatcontroller.cpp:464 |

### Unk_8f25e0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F25E0 | FUN_008f25e0 | unnamed | src/fallout/ai/highprocess.cpp:5337 |

### UnkHolder (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00C72210 | FUN_00c72210 | unnamed | src/fallout/ai/mobileobject_o2_variant.cpp:41 |

### Unknown1 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097D960 | FUN_0097d960 | unnamed | src/fallout/ai/combatcontroller.cpp:399 |

### UnknownClass (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0097EEE0 | IsElapsedTimeAtLeastSetting | decomp | src/fallout/ai/combat/combatstate.cpp:484 |

### UnreachableLocation (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009A2DB0 | LoadGame | proven | src/fallout/ai/combat/combatstate.cpp:1435 |
| 0x009A2D80 | SaveGame | proven | src/fallout/ai/combat/combatstate.cpp:304 |

### UpdateHandler (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009E0A00 | UpdateMovementState | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:7134 |

### UpdateManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008C8BE0 | UpdateMobileObject | class | src/fallout/ai/aitaskmanager.cpp:3207 |

### UpdateOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0098E990 | UpdateElements | decomp | src/fallout/ai/combat/combatgroup.cpp:9762 |

### UpdateState (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00998A50 | FUN_00998a50 | probable | src/fallout/ai/combat/combatstate.cpp:6256 |

### UWProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F7730 | FUN_008f7730 | class | src/fallout/ai/highprocess.cpp:68044 |

### VATS (11)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA410 | ClearCommandList | proven | src/fallout/ai/combat/vats.cpp:107 |
| 0x009C86B0 | FreeHeadAction | proven | src/fallout/ai/combat/vats.cpp:2083 |
| 0x009C71C0 | GetCurrentAction | proven | src/fallout/ai/combat/vats.cpp:163 |
| 0x009C8F20 | GetLineOfSight | proven | src/fallout/ai/combat/vats_o2_variant_od_oy_noo2_variant.cpp:392 |
| 0x009C8CC0 | GetModeTimeMultiplier | decomp | src/fallout/ai/combat/vats.cpp:28 |
| 0x009C9FE0 | GetTargetPercentagePos | proven | src/fallout/ai/combat/vats.cpp:1464 |
| 0x0093E770 | Update | decomp | src/fallout/ai/combat/vats.cpp:6 |
| 0x009C95E0 | UpdateCurrentCameraAction | proven | src/fallout/ai/combat/vats.cpp:1699 |
| 0x009C9280 | UpdateMeleeAttack | proven | src/fallout/ai/combat/vats.cpp:926 |
| 0x009C9AE0 | UpdateVATSLight | proven | src/fallout/ai/combat/vats.cpp:1238 |
| 0x009C9920 | UseNextCamera | proven | src/fallout/ai/combat/vats.cpp:2161 |

### VATS_ca2c0 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA2C0 | FUN_009ca2c0 | probable | src/fallout/ai/combat/vats.cpp:1890 |

### VATS_COMMAND (2)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA4A0 | VATS_COMMAND | proven | src/fallout/ai/combat/vats.cpp:222 |
| 0x009CA4C0 | ~VATS_COMMAND | proven | src/fallout/ai/combat/hitdata.cpp:208 |

### VATS_COMMAND_LIST (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CA1F0 | CreateCommandAndUpdateHUD | decomp | src/fallout/ai/combat/vats.cpp:282 |

### VatsList9c9 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C9F60 | IsValidCommand | decomp | src/fallout/ai/combat/vats.cpp:579 |

### VectorXYZ (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008A5110 | FUN_008a5110 | unnamed | src/fallout/ai/actor_o2_variant_od_oy_noo2_variant.cpp:1888 |

### VirtualActorPathHandlerS (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009EB390 | SaveToBuffer | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:724 |

### VoiceHost (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00578A80 | PlayVoiceTopic | class | src/fallout/ai/mobileobject.cpp:8694 |

### Walker8 (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00845300 | ConstructArray | decomp | src/fallout/ai/combat/combatgroup.cpp:2937 |

### WalkProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E5E90 | ProcessPackageMovement | class | src/fallout/ai/highprocess.cpp:60381 |

### WanderProcess (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008F36C0 | WanderToPoint | decomp | src/fallout/ai/middlehighprocess.cpp:14391 |

### WeaponSearch (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0099F6D0 | SelectBestWeaponTarget | decomp | src/fallout/ai/combat/combatstate.cpp:8785 |

### WeaponShaderCleanup (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00974DB0 | FUN_00974db0 | unnamed | src/fallout/ai/processlists.cpp:17224 |

### WeightedResultList (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009B7990 | FUN_009b7990 | unnamed | src/fallout/ai/combat/hitdata.cpp:194 |

### WorkerView (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008B6E80 | HasSkinBoneInList | decomp | src/fallout/ai/actor.cpp:80603 |

### WorldStateManager (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009AA4E0 | UpdateWorldState | decomp | src/fallout/ai/combat/combatworldstate.cpp:505 |

### Wrap (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009F8730 | FUN_009f8730 | class | src/fallout/ai/spectatorpackage_od_variant.cpp:346 |

### xActorD (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00935480 | StartConversation | class | src/fallout/ai/mobileobject.cpp:12291 |

### XActorQ (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008D4B60 | FUN_008d4b60 | probable | src/fallout/ai/creature.cpp:1085 |

### xBoxShape (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x008E5100 | xBoxShape | decomp | src/fallout/ai/highprocess_o2_variant_od_oy_noo2_variant.cpp:882 |

### xEffOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0094C6C0 | FUN_0094c6c0 | unnamed | src/fallout/ai/playercharacter.cpp:20584 |

### xMelee (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CDB00 | UpdateDodge | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:6719 |

### xPlayer (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x0095D850 | ReloadWeapon | class | src/fallout/ai/playercharacter.cpp:40509 |

### ZActor (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00899200 | FUN_00899200 | probable | src/fallout/ai/actor.cpp:128370 |

### ZMelee (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009CE1D0 | UpdateMeleeCombat | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:5985 |

### ZOwner (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00971C30 | CollectActorsByPackage | decomp | src/fallout/ai/processlists.cpp:13900 |

### ZProjectile (1)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x009C3190 | UpdateDetonation | decomp | src/fallout/ai/combat/projectile.cpp:8769 |

### (free functions) (1280)

| Address | Name | Status | Source |
|---|---|---|---|
| 0x00978740 | ActivateMuzzleFlash | decomp | src/fallout/ai/processlists.cpp:13027 |
| 0x009F5070 | AddActivationChoice | decomp | src/fallout/ai/sandboxpackage.cpp:2390 |
| 0x009528C0 | AddChallenge | probable | src/fallout/ai/playercharacter.cpp:31022 |
| 0x008C48D0 | AddEffectToTarget | decomp | src/fallout/ai/actor.cpp:31363 |
| 0x009EC830 | AddHeadAtOffset | decomp | src/fallout/ai/alarmpackage.cpp:155 |
| 0x009721F0 | AddObjectToList | decomp | src/fallout/ai/processlists.cpp:4644 |
| 0x008D5CB0 | AddTimedEntry | decomp | src/fallout/ai/actor.cpp:93683 |
| 0x008BFF70 | AddToField | decomp | src/fallout/ai/actor.cpp:34601 |
| 0x0049BB50 | AddToOffset | decomp | src/fallout/ai/baseprocess.cpp:126 |
| 0x009293B0 | AddUniqueValue | class | src/fallout/ai/middlehighprocess.cpp:6737 |
| 0x009E3C00 | AdvanceAlongPath | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:5520 |
| 0x008CA5A0 | AppendNode | class | src/fallout/ai/aitaskmanager.cpp:844 |
| 0x008B9830 | ApplyAVModifierAndUpdatePair | decomp | src/fallout/ai/actor.cpp:82425 |
| 0x008C50F0 | ApplyModifier | class | src/fallout/ai/creature.cpp:755 |
| 0x0092CE70 | ApplyModifierIfNotFlagged | class | src/fallout/ai/middlelowprocess.cpp:462 |
| 0x009DE330 | ApplyNodeLookup | probable | src/fallout/ai/movement/actormover.cpp:3888 |
| 0x008BBC40 | ApplyRDTNodeScales | probable | src/fallout/ai/actor.cpp:86355 |
| 0x009BF370 | ApplySpeedAndVector | probable | src/fallout/ai/combat/projectile.cpp:1502 |
| 0x008C16C0 | ApplyValueToFoundObject | probable | src/fallout/ai/actor.cpp:89698 |
| 0x009D9EC0 | AssignAtOffsetB0 | decomp | src/fallout/ai/combat/vats.cpp:238 |
| 0x009C3F50 | BlendWithSetting | decomp | src/fallout/ai/combat/projectile.cpp:545 |
| 0x00644680 | CalculateWeightedValue | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:6638 |
| 0x008C9F70 | CallAllElements | decomp | src/fallout/ai/aitaskmanager.cpp:1606 |
| 0x00501C10 | CallAndReturnSelf | decomp | src/fallout/ai/middlelowprocess.cpp:731 |
| 0x008CA2E0 | CallAt | decomp | src/fallout/ai/aitaskmanager.cpp:662 |
| 0x008BC7D0 | CallFUN_008bc7d0 | decomp | src/fallout/ai/actor.cpp:34552 |
| 0x00573150 | CallLastVirtualMethod | class | src/fallout/ai/character.cpp:820 |
| 0x00880660 | CallMember | class | src/fallout/ai/actor.cpp:1551 |
| 0x0099B580 | CallReferencedFunction | decomp | src/fallout/ai/combat/combatstate.cpp:1002 |
| 0x009060F0 | CallVirtual5 | probable | src/fallout/ai/lipsyncbackgroundmanager.cpp:34 |
| 0x009C2C80 | CanProjectileHit | decomp | src/fallout/ai/combat/projectile.cpp:4001 |
| 0x008FBFD0 | CastFormReferences | class | src/fallout/ai/highprocess.cpp:48936 |
| 0x008E3EA0 | CheckAndQueueRadioRef | decomp | src/fallout/ai/highprocess.cpp:10215 |
| 0x008BA090 | CheckRangeConditions | decomp | src/fallout/ai/actor.cpp:82790 |
| 0x00931920 | CheckTargetAndDelete | decomp | src/fallout/ai/mobileobject.cpp:2422 |
| 0x009F3C90 | CheckTimerState | decomp | src/fallout/ai/sandboxpackage.cpp:1374 |
| 0x00937810 | ClampSumByMode | decomp | src/fallout/ai/modifierlist.cpp:196 |
| 0x00904160 | ClearAndDeleteList | decomp | src/fallout/ai/highprocess.cpp:4223 |
| 0x009A0680 | ClearAndDeletePointer | probable | src/fallout/ai/combat/combatstate.cpp:263 |
| 0x009026A0 | ClearField0C | decomp | src/fallout/ai/highprocess.cpp:6467 |
| 0x008D8D80 | ClearField298 | class | src/fallout/ai/highprocess.cpp:4782 |
| 0x008D9850 | ClearField41C | class | src/fallout/ai/highprocess.cpp:14856 |
| 0x008D1030 | ClearField44 | decomp | src/fallout/ai/baseprocess.cpp:180 |
| 0x008C5330 | ClearField4C | decomp | src/fallout/ai/actor_magic.cpp:567 |
| 0x008D96D0 | ClearFlag | class | src/fallout/ai/highprocess.cpp:4896 |
| 0x006D3280 | ClearFlags | probable | src/fallout/ai/combat/combatstate.cpp:354 |
| 0x009DE040 | ClearFlags | class | src/fallout/ai/movement/actormover.cpp:1614 |
| 0x009877E0 | ClearGlobalObject | decomp | src/fallout/ai/combat/combatgroup.cpp:102 |
| 0x008E56B0 | ClearNode | decomp | src/fallout/ai/highprocess.cpp:3983 |
| 0x00915AE0 | ClearQueuedItems | class | src/fallout/ai/middlehighprocess.cpp:2845 |
| 0x009D9FA0 | ClearRefIfMatches | class | src/fallout/ai/combat/combatproceduresearch.cpp:66 |
| 0x0098C780 | ClearReservedFlag | decomp | src/fallout/ai/combat/combatgroup.cpp:1314 |
| 0x0092B7F0 | ClearState | decomp | src/fallout/ai/middlehighprocess.cpp:3241 |
| 0x009F4680 | ClearTargetReferences | decomp | src/fallout/ai/sandboxpackage.cpp:1030 |
| 0x009A0E10 | CollectAvoidanceItems | decomp | src/fallout/ai/combat/combatstate.cpp:3301 |
| 0x008B8740 | CombineFightReaction | decomp | src/fallout/ai/actor.cpp:11161 |
| 0x0098A4D0 | ComputeAverageRatio | decomp | src/fallout/ai/combat/combatgroup.cpp:4433 |
| 0x008C1740 | ComputeFromNode | decomp | src/fallout/ai/actor.cpp:89750 |
| 0x009A7C60 | ComputeLaunchAngle | decomp | src/fallout/ai/combat/combatutilities.cpp:611 |
| 0x009A7E00 | ComputeProjectileFlightTime | decomp | src/fallout/ai/combat/combatutilities.cpp:2380 |
| 0x009A86E0 | ComputeRelativeFiringAngle | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:4633 |
| 0x009A8BF0 | ComputeTrajectory | decomp | src/fallout/ai/combat/combatutilities.cpp:3352 |
| 0x009B32B0 | ConfigureFlags | class | src/fallout/ai/combat/flameprojectile.cpp:85 |
| 0x009E32F0 | ConsumePendingDelta | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:190 |
| 0x009E2660 | Contains | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:5048 |
| 0x009A0D70 | ContainsItem | decomp | src/fallout/ai/combat/combatstate.cpp:3232 |
| 0x00986B00 | CopyArrayTo | decomp | src/fallout/ai/combat/combatgroup.cpp:1984 |
| 0x0092CA70 | CopyFrom | decomp | src/fallout/ai/cachedvalues.cpp:19 |
| 0x00936FD0 | CopyFrom | decomp | src/fallout/ai/modifierlist.cpp:233 |
| 0x00985980 | CopyFrom | decomp | src/fallout/ai/combat/combatgroup.cpp:17 |
| 0x009378D0 | CountModifiers | decomp | src/fallout/ai/modifierlist.cpp:336 |
| 0x008D0590 | CreateDefaultInstance | class | src/fallout/ai/baseprocess.cpp:919 |
| 0x008C4D10 | CreateMagicHitEffect | decomp | src/fallout/ai/actor.cpp:90741 |
| 0x009BCA60 | CreateProjectile | decomp | src/fallout/ai/combat/projectile.cpp:5754 |
| 0x008D03E0 | DeallocateSound | class | src/fallout/ai/baseprocess.cpp:159 |
| 0x009874F0 | DecrementField4A | decomp | src/fallout/ai/combat/combatgroup.cpp:600 |
| 0x00931E80 | DeleteAndClear | decomp | src/fallout/ai/mobileobject.cpp:724 |
| 0x008C5E70 | DeleteData | decomp | src/fallout/ai/actorpackage.cpp:431 |
| 0x008D9F70 | DestroyIfFlagged | decomp | src/fallout/ai/combat/muzzleflash.cpp:29 |
| 0x00983250 | DestroyIfFlagged | decomp | src/fallout/ai/combat/combatcovermap.cpp:40 |
| 0x009B4BF0 | DispatchReferenceSourceFiles | decomp | src/fallout/ai/combat/grenadeprojectile.cpp:131 |
| 0x008B3C50 | DispatchToReceiver | decomp | src/fallout/ai/actor.cpp:40212 |
| 0x008B3A20 | DispatchToTarget | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:994 |
| 0x009CBF10 | DisplayAttackDebugText | class | src/fallout/ai/combat/combatprocedureattacklow.cpp:110 |
| 0x008D74A0 | DoIt | probable | src/fallout/ai/highprocess.cpp:10186 |
| 0x009A9F20 | DrawDebugLine | decomp | src/fallout/ai/combat/combatutilities.cpp:3657 |
| 0x008C1F80 | EquipItemWithCaster | decomp | src/fallout/ai/actor_magic.cpp:4316 |
| 0x009E5690 | EvaluateAvoidance | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:3800 |
| 0x0096CF60 | ExecElementAt | decomp | src/fallout/ai/processlists.cpp:3455 |
| 0x009A9940 | ExpandFlagBits | decomp | src/fallout/ai/combat/combatutilities.cpp:329 |
| 0x0098A410 | FindByValue | probable | src/fallout/ai/combat/combatgroup.cpp:786 |
| 0x009C3EE0 | FindItemByKey | decomp | src/fallout/ai/combat/projectile.cpp:521 |
| 0x009BD780 | FindProjectObject | decomp | src/fallout/ai/combat/flameprojectile.cpp:595 |
| 0x00707330 | FindSettingIndex | decomp | src/fallout/ai/actor.cpp:41606 |
| 0x00401000 | FormHeap_Allocate | proven | src/fallout/ai/middlehighprocess.cpp:3040 |
| 0x009ED010 | ForwardToBase | decomp | src/fallout/ai/backuppackage.cpp:16 |
| 0x00990A80 | ForwardToHolder | decomp | src/fallout/ai/combat/combatgroupstrategy.cpp:50 |
| 0x0097F7D0 | ForwardToMember | decomp | src/fallout/ai/combatcontroller.cpp:1103 |
| 0x00887B40 | ForwardToScriptLocals | decomp | src/fallout/ai/actor.cpp:33970 |
| 0x008D04A0 | ForwardToVfn144 | class | src/fallout/ai/baseprocess.cpp:1409 |
| 0x009DC950 | ForwardValueToVtbl | decomp | src/fallout/ai/movement/actormover.cpp:285 |
| 0x00938060 | FreeModifierEntry | decomp | src/fallout/ai/modifierlist.cpp:376 |
| 0x0040DF50 | FUN_0040df50 | unnamed | src/fallout/ai/actor_magic.cpp:535 |
| 0x00435DD0 | FUN_00435dd0 | unnamed | src/fallout/ai/actor.cpp:32766 |
| 0x004387B0 | FUN_004387b0 | unnamed | src/fallout/ai/actor.cpp:44012 |
| 0x00453700 | FUN_00453700 | rejected | src/fallout/ai/combat/projectile.cpp:71 |
| 0x0045CEC0 | FUN_0045cec0 | unnamed | src/fallout/ai/movement/actormover.cpp:1253 |
| 0x0047B200 | FUN_0047b200 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:304 |
| 0x00491040 | FUN_00491040 | probable | src/fallout/ai/actor.cpp:256 |
| 0x004E3D00 | FUN_004e3d00 | unnamed | src/fallout/ai/actor.cpp:288 |
| 0x005075F0 | FUN_005075f0 | class | src/fallout/ai/highprocess.cpp:4312 |
| 0x00570F60 | FUN_00570f60 | probable | src/fallout/ai/playercharacter.cpp:1334 |
| 0x00575380 | FUN_00575380 | class | src/fallout/ai/actor.cpp:46677 |
| 0x00575DC0 | FUN_00575dc0 | probable | src/fallout/ai/actor.cpp:115391 |
| 0x005762B0 | FUN_005762b0 | class | src/fallout/ai/combat/explosion.cpp:1041 |
| 0x00576870 | FUN_00576870 | unnamed | src/fallout/ai/combat/explosion.cpp:3415 |
| 0x005DC960 | FUN_005dc960 | rejected | src/fallout/ai/combat/combatstate.cpp:150 |
| 0x005DE0A0 | FUN_005de0a0 | rejected | src/fallout/ai/combat/flameprojectile.cpp:141 |
| 0x005F64F0 | FUN_005f64f0 | unnamed | src/fallout/ai/actor.cpp:46702 |
| 0x00621370 | FUN_00621370 | probable | src/fallout/ai/playercharacter.cpp:1556 |
| 0x0062B930 | FUN_0062b930 | unnamed | src/fallout/ai/mobileobject_o2_variant_od_oy_noo2_variant.cpp:83 |
| 0x00633C90 | FUN_00633c90 | unnamed | src/fallout/ai/actor.cpp:33731 |
| 0x006377E0 | FUN_006377e0 | rejected | src/fallout/ai/middlehighprocess.cpp:91 |
| 0x0063CFE0 | FUN_0063cfe0 | probable | src/fallout/ai/combat/vats.cpp:261 |
| 0x00643F90 | FUN_00643f90 | unnamed | src/fallout/ai/actor.cpp:32790 |
| 0x00644580 | FUN_00644580 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:91 |
| 0x0066DE30 | FUN_0066de30 | unnamed | src/fallout/ai/combat/hitdata.cpp:44 |
| 0x00691C90 | FUN_00691c90 | unnamed | src/fallout/ai/movement/actormover.cpp:1062 |
| 0x006D3370 | FUN_006d3370 | unnamed | src/fallout/ai/combat/combatstate.cpp:373 |
| 0x006D53B0 | FUN_006d53b0 | unnamed | src/fallout/ai/movement/actormover.cpp:2491 |
| 0x006DBEE0 | FUN_006dbee0 | unnamed | src/fallout/ai/combat/combatstate.cpp:419 |
| 0x006F74F0 | FUN_006f74f0 | unnamed | src/fallout/ai/middlehighprocess.cpp:165 |
| 0x006F99E0 | FUN_006f99e0 | unnamed | src/fallout/ai/combat/combattargetmap.cpp:35 |
| 0x007031C0 | FUN_007031c0 | rejected | src/fallout/ai/combatcontroller.cpp:13 |
| 0x00709D40 | FUN_00709d40 | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:4576 |
| 0x00719AE0 | FUN_00719ae0 | unnamed | src/fallout/ai/actor.cpp:341 |
| 0x0076BAD0 | FUN_0076bad0 | unnamed | src/fallout/ai/aitaskmanager.cpp:61 |
| 0x0077A480 | FUN_0077a480 | rejected | src/fallout/ai/aitaskmanager.cpp:2056 |
| 0x0078D900 | FUN_0078d900 | unnamed | src/fallout/ai/playercharacter.cpp:1587 |
| 0x00804B30 | FUN_00804b30 | unnamed | src/fallout/ai/actor_magic.cpp:542 |
| 0x0080F7B0 | FUN_0080f7b0 | class | src/fallout/ai/combat/projectile.cpp:280 |
| 0x00810530 | FUN_00810530 | unnamed | src/fallout/ai/actor.cpp:373 |
| 0x00815340 | FUN_00815340 | class | src/fallout/ai/actor.cpp:33760 |
| 0x00819A50 | FUN_00819a50 | rejected | src/fallout/ai/combat/combatstate.cpp:194 |
| 0x0081E3D0 | FUN_0081e3d0 | class | src/fallout/ai/mobileobject.cpp:11371 |
| 0x0083B830 | FUN_0083b830 | unnamed | src/fallout/ai/dialoguepackage.cpp:127 |
| 0x0083C4D0 | FUN_0083c4d0 | unnamed | src/fallout/ai/highprocess.cpp:4367 |
| 0x008661E0 | FUN_008661e0 | unnamed | src/fallout/ai/processlists.cpp:2454 |
| 0x008675E0 | FUN_008675e0 | unnamed | src/fallout/ai/lowprocess.cpp:3358 |
| 0x0087A6B0 | FUN_0087a6b0 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:319 |
| 0x0087A6D0 | FUN_0087a6d0 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:334 |
| 0x0087D670 | FUN_0087d670 | unnamed | src/fallout/ai/actor.cpp:381 |
| 0x0087D6D0 | FUN_0087d6d0 | unnamed | src/fallout/ai/actor.cpp:32838 |
| 0x0087D770 | FUN_0087d770 | class | src/fallout/ai/actor.cpp:412 |
| 0x0087D790 | FUN_0087d790 | unnamed | src/fallout/ai/actor.cpp:418 |
| 0x0087D7B0 | FUN_0087d7b0 | probable | src/fallout/ai/actor.cpp:424 |
| 0x0087D880 | FUN_0087d880 | unnamed | src/fallout/ai/actor.cpp:33825 |
| 0x0087E9A0 | FUN_0087e9a0 | unnamed | src/fallout/ai/actor.cpp:32846 |
| 0x0087EA60 | FUN_0087ea60 | unnamed | src/fallout/ai/actor.cpp:32868 |
| 0x0087EEB0 | FUN_0087eeb0 | probable | src/fallout/ai/actor.cpp:435 |
| 0x0087F350 | FUN_0087f350 | probable | src/fallout/ai/actor.cpp:454 |
| 0x0087F370 | FUN_0087f370 | probable | src/fallout/ai/actor.cpp:467 |
| 0x0087F390 | FUN_0087f390 | probable | src/fallout/ai/actor.cpp:480 |
| 0x0087F3B0 | FUN_0087f3b0 | probable | src/fallout/ai/actor.cpp:33839 |
| 0x0087F4E0 | FUN_0087f4e0 | unnamed | src/fallout/ai/actor.cpp:641 |
| 0x0087F620 | FUN_0087f620 | unnamed | src/fallout/ai/actor.cpp:671 |
| 0x0087F6C0 | FUN_0087f6c0 | unnamed | src/fallout/ai/actor.cpp:100256 |
| 0x0087F990 | FUN_0087f990 | unnamed | src/fallout/ai/actor.cpp:946 |
| 0x0087FA10 | FUN_0087fa10 | class | src/fallout/ai/actor.cpp:1277 |
| 0x0087FAA0 | FUN_0087faa0 | probable | src/fallout/ai/actor.cpp:1462 |
| 0x00880580 | FUN_00880580 | probable | src/fallout/ai/actor.cpp:48521 |
| 0x00880690 | FUN_00880690 | class | src/fallout/ai/actor.cpp:1587 |
| 0x00880850 | FUN_00880850 | unnamed | src/fallout/ai/actor.cpp:1601 |
| 0x00880890 | FUN_00880890 | unnamed | src/fallout/ai/actor.cpp:1607 |
| 0x008808F0 | FUN_008808f0 | unnamed | src/fallout/ai/actor.cpp:1622 |
| 0x00880910 | FUN_00880910 | unnamed | src/fallout/ai/actor.cpp:1631 |
| 0x00880950 | FUN_00880950 | class | src/fallout/ai/actor.cpp:116927 |
| 0x00880AD0 | FUN_00880ad0 | class | src/fallout/ai/actor.cpp:20278 |
| 0x00880E00 | FUN_00880e00 | class | src/fallout/ai/actor.cpp:49667 |
| 0x00881470 | FUN_00881470 | probable | src/fallout/ai/actor.cpp:1681 |
| 0x008814B0 | FUN_008814b0 | probable | src/fallout/ai/actor.cpp:1871 |
| 0x008815A0 | FUN_008815a0 | class | src/fallout/ai/actor.cpp:1973 |
| 0x00881830 | FUN_00881830 | unnamed | src/fallout/ai/actor.cpp:32919 |
| 0x008840F0 | FUN_008840f0 | probable | src/fallout/ai/actor.cpp:2088 |
| 0x008842C0 | FUN_008842c0 | probable | src/fallout/ai/actor.cpp:2265 |
| 0x00884690 | FUN_00884690 | probable | src/fallout/ai/actor.cpp:3144 |
| 0x008846C0 | FUN_008846c0 | rejected | src/fallout/ai/actor.cpp:3156 |
| 0x00884730 | FUN_00884730 | probable | src/fallout/ai/actor.cpp:3194 |
| 0x00884940 | FUN_00884940 | probable | src/fallout/ai/actor.cpp:3276 |
| 0x00884C80 | FUN_00884c80 | unnamed | src/fallout/ai/actor.cpp:3321 |
| 0x00884D20 | FUN_00884d20 | unnamed | src/fallout/ai/actor.cpp:17238 |
| 0x00884D80 | FUN_00884d80 | probable | src/fallout/ai/actor.cpp:3370 |
| 0x00884DC0 | FUN_00884dc0 | probable | src/fallout/ai/actor.cpp:3393 |
| 0x00884EB0 | FUN_00884eb0 | probable | src/fallout/ai/actor.cpp:3470 |
| 0x00884FF0 | FUN_00884ff0 | unnamed | src/fallout/ai/actor.cpp:36179 |
| 0x00885110 | FUN_00885110 | unnamed | src/fallout/ai/actor.cpp:3554 |
| 0x008851E0 | FUN_008851e0 | unnamed | src/fallout/ai/actor.cpp:3577 |
| 0x00885210 | FUN_00885210 | unnamed | src/fallout/ai/actor.cpp:54674 |
| 0x008852E0 | FUN_008852e0 | unnamed | src/fallout/ai/actor.cpp:3733 |
| 0x00885360 | FUN_00885360 | unnamed | src/fallout/ai/actor.cpp:3763 |
| 0x008854B0 | FUN_008854b0 | unnamed | src/fallout/ai/actor.cpp:3785 |
| 0x008854D0 | FUN_008854d0 | probable | src/fallout/ai/actor.cpp:36222 |
| 0x00885BD0 | FUN_00885bd0 | unnamed | src/fallout/ai/actor.cpp:36237 |
| 0x00886010 | FUN_00886010 | unnamed | src/fallout/ai/actor.cpp:56082 |
| 0x00886080 | FUN_00886080 | unnamed | src/fallout/ai/actor.cpp:4015 |
| 0x00887A00 | FUN_00887a00 | unnamed | src/fallout/ai/actor.cpp:32966 |
| 0x00887A10 | FUN_00887a10 | unnamed | src/fallout/ai/actor.cpp:112639 |
| 0x00887A80 | FUN_00887a80 | unnamed | src/fallout/ai/actor.cpp:112664 |
| 0x00887AC0 | FUN_00887ac0 | unnamed | src/fallout/ai/actor.cpp:33922 |
| 0x00887AF0 | FUN_00887af0 | unnamed | src/fallout/ai/actor.cpp:33943 |
| 0x00888AF0 | FUN_00888af0 | class | src/fallout/ai/actor.cpp:4460 |
| 0x0088B020 | FUN_0088b020 | unnamed | src/fallout/ai/actor.cpp:33011 |
| 0x0088B030 | FUN_0088b030 | probable | src/fallout/ai/actor.cpp:4471 |
| 0x0088B740 | FUN_0088b740 | probable | src/fallout/ai/actor.cpp:4546 |
| 0x0088C650 | FUN_0088c650 | probable | src/fallout/ai/actor.cpp:4693 |
| 0x0088D7D0 | FUN_0088d7d0 | probable | src/fallout/ai/actor.cpp:58617 |
| 0x0088E0F0 | FUN_0088e0f0 | unnamed | src/fallout/ai/actor.cpp:4822 |
| 0x00891B70 | FUN_00891b70 | probable | src/fallout/ai/actor.cpp:33994 |
| 0x00893500 | FUN_00893500 | probable | src/fallout/ai/actor.cpp:4841 |
| 0x00894900 | FUN_00894900 | probable | src/fallout/ai/actor.cpp:4904 |
| 0x00894CC0 | FUN_00894cc0 | probable | src/fallout/ai/actor.cpp:17693 |
| 0x00894D60 | FUN_00894d60 | probable | src/fallout/ai/actor.cpp:4928 |
| 0x00897890 | FUN_00897890 | probable | src/fallout/ai/actor.cpp:33139 |
| 0x008978B0 | FUN_008978b0 | unnamed | src/fallout/ai/actor.cpp:33147 |
| 0x008978C0 | FUN_008978c0 | unnamed | src/fallout/ai/actor.cpp:33155 |
| 0x008978F0 | FUN_008978f0 | unnamed | src/fallout/ai/actor.cpp:33179 |
| 0x00897B30 | FUN_00897b30 | unnamed | src/fallout/ai/actor.cpp:4956 |
| 0x00898250 | FUN_00898250 | unnamed | src/fallout/ai/actor.cpp:36847 |
| 0x008985D0 | FUN_008985d0 | probable | src/fallout/ai/actor_magic.cpp:877 |
| 0x00898FD0 | FUN_00898fd0 | probable | src/fallout/ai/actor.cpp:34044 |
| 0x0089D5E0 | FUN_0089d5e0 | probable | src/fallout/ai/actor.cpp:5435 |
| 0x0089D600 | FUN_0089d600 | unnamed | src/fallout/ai/actor.cpp:5442 |
| 0x0089D620 | FUN_0089d620 | unnamed | src/fallout/ai/actor.cpp:5448 |
| 0x0089F4E0 | FUN_0089f4e0 | probable | src/fallout/ai/actor.cpp:5459 |
| 0x0089F520 | FUN_0089f520 | unnamed | src/fallout/ai/actor.cpp:34055 |
| 0x008A0270 | FUN_008a0270 | class | src/fallout/ai/mobileobject.cpp:1509 |
| 0x008A0A90 | FUN_008a0a90 | unnamed | src/fallout/ai/actor.cpp:66962 |
| 0x008A0AD0 | FUN_008a0ad0 | unnamed | src/fallout/ai/actor.cpp:38011 |
| 0x008A0B10 | FUN_008a0b10 | probable | src/fallout/ai/actor.cpp:25400 |
| 0x008A0CD0 | FUN_008a0cd0 | rejected | src/fallout/ai/actor.cpp:5507 |
| 0x008A16B0 | FUN_008a16b0 | unnamed | src/fallout/ai/actor.cpp:5519 |
| 0x008A1710 | FUN_008a1710 | probable | src/fallout/ai/actor.cpp:5918 |
| 0x008A1760 | FUN_008a1760 | unnamed | src/fallout/ai/actor.cpp:6259 |
| 0x008A2D20 | FUN_008a2d20 | unnamed | src/fallout/ai/actor.cpp:6298 |
| 0x008A30F0 | FUN_008a30f0 | unnamed | src/fallout/ai/actor.cpp:33255 |
| 0x008A3B50 | FUN_008a3b50 | probable | src/fallout/ai/actor.cpp:6312 |
| 0x008A3C10 | FUN_008a3c10 | unnamed | src/fallout/ai/actor.cpp:34097 |
| 0x008A3C30 | FUN_008a3c30 | unnamed | src/fallout/ai/actor.cpp:34116 |
| 0x008A46A0 | FUN_008a46a0 | probable | src/fallout/ai/actor.cpp:6470 |
| 0x008A50F0 | FUN_008a50f0 | unnamed | src/fallout/ai/actor.cpp:34129 |
| 0x008A5170 | FUN_008a5170 | unnamed | src/fallout/ai/actor.cpp:6482 |
| 0x008A5190 | FUN_008a5190 | unnamed | src/fallout/ai/actor.cpp:33263 |
| 0x008A5270 | FUN_008a5270 | unnamed | src/fallout/ai/actor.cpp:18201 |
| 0x008A52C0 | FUN_008a52c0 | unnamed | src/fallout/ai/actor.cpp:113161 |
| 0x008A5530 | FUN_008a5530 | probable | src/fallout/ai/actor.cpp:6552 |
| 0x008A6210 | FUN_008a6210 | probable | src/fallout/ai/actor.cpp:18421 |
| 0x008A6290 | FUN_008a6290 | probable | src/fallout/ai/actor.cpp:6857 |
| 0x008A6630 | FUN_008a6630 | unnamed | src/fallout/ai/actor.cpp:34143 |
| 0x008A6730 | FUN_008a6730 | probable | src/fallout/ai/actor.cpp:7176 |
| 0x008A67F0 | FUN_008a67f0 | probable | src/fallout/ai/actor.cpp:7516 |
| 0x008A6970 | FUN_008a6970 | probable | src/fallout/ai/actor.cpp:7824 |
| 0x008A73E0 | FUN_008a73e0 | probable | src/fallout/ai/actor.cpp:28128 |
| 0x008A7870 | FUN_008a7870 | probable | src/fallout/ai/actor.cpp:8330 |
| 0x008A7F40 | FUN_008a7f40 | unnamed | src/fallout/ai/actor.cpp:33285 |
| 0x008A7F60 | FUN_008a7f60 | unnamed | src/fallout/ai/actor.cpp:33296 |
| 0x008A8150 | FUN_008a8150 | probable | src/fallout/ai/actor.cpp:8675 |
| 0x008A88F0 | FUN_008a88f0 | probable | src/fallout/ai/combat/combatcovermap.cpp:406 |
| 0x008A8E30 | FUN_008a8e30 | probable | src/fallout/ai/actor.cpp:39599 |
| 0x008A8F60 | FUN_008a8f60 | probable | src/fallout/ai/actor.cpp:9093 |
| 0x008ABFA0 | FUN_008abfa0 | unnamed | src/fallout/ai/actor.cpp:34160 |
| 0x008AC850 | FUN_008ac850 | class | src/fallout/ai/character.cpp:1703 |
| 0x008AC990 | FUN_008ac990 | unnamed | src/fallout/ai/actor.cpp:9186 |
| 0x008ACBA0 | FUN_008acba0 | probable | src/fallout/ai/actor.cpp:9231 |
| 0x008ACF70 | FUN_008acf70 | unnamed | src/fallout/ai/actor.cpp:9332 |
| 0x008ADC50 | FUN_008adc50 | unnamed | src/fallout/ai/actor.cpp:9600 |
| 0x008AE640 | FUN_008ae640 | unnamed | src/fallout/ai/actor.cpp:9729 |
| 0x008B01C0 | FUN_008b01c0 | probable | src/fallout/ai/highprocess.cpp:27332 |
| 0x008B0520 | FUN_008b0520 | unnamed | src/fallout/ai/actor.cpp:29611 |
| 0x008B0B00 | FUN_008b0b00 | probable | src/fallout/ai/actor.cpp:74548 |
| 0x008B0BA0 | FUN_008b0ba0 | unnamed | src/fallout/ai/actor.cpp:74942 |
| 0x008B0BD0 | FUN_008b0bd0 | probable | src/fallout/ai/actor.cpp:30011 |
| 0x008B0D30 | FUN_008b0d30 | unnamed | src/fallout/ai/actor.cpp:75337 |
| 0x008B0DB0 | FUN_008b0db0 | unnamed | src/fallout/ai/actor.cpp:34194 |
| 0x008B1FF0 | FUN_008b1ff0 | probable | src/fallout/ai/actor.cpp:9747 |
| 0x008B3200 | FUN_008b3200 | unnamed | src/fallout/ai/actor.cpp:9765 |
| 0x008B3820 | FUN_008b3820 | unnamed | src/fallout/ai/actor.cpp:79552 |
| 0x008B3840 | FUN_008b3840 | unnamed | src/fallout/ai/actor.cpp:79568 |
| 0x008B3860 | FUN_008b3860 | probable | src/fallout/ai/actor.cpp:34243 |
| 0x008B3960 | FUN_008b3960 | probable | src/fallout/ai/actor.cpp:34360 |
| 0x008B3980 | FUN_008b3980 | unnamed | src/fallout/ai/actor.cpp:33364 |
| 0x008B3BD0 | FUN_008b3bd0 | probable | src/fallout/ai/actor.cpp:10473 |
| 0x008B3BF0 | FUN_008b3bf0 | probable | src/fallout/ai/actor.cpp:10487 |
| 0x008B3C10 | FUN_008b3c10 | rejected | src/fallout/ai/actor.cpp:10772 |
| 0x008B3C30 | FUN_008b3c30 | rejected | src/fallout/ai/actor.cpp:10791 |
| 0x008B3C70 | FUN_008b3c70 | unnamed | src/fallout/ai/actor.cpp:33381 |
| 0x008B3CB0 | FUN_008b3cb0 | unnamed | src/fallout/ai/actor.cpp:34383 |
| 0x008B3D50 | FUN_008b3d50 | rejected | src/fallout/ai/movement/detailedactorpathhandler.cpp:5203 |
| 0x008B3EF0 | FUN_008b3ef0 | probable | src/fallout/ai/playercharacter.cpp:2052 |
| 0x008B51B0 | FUN_008b51b0 | probable | src/fallout/ai/actor.cpp:80106 |
| 0x008B6260 | FUN_008b6260 | unnamed | src/fallout/ai/actor.cpp:33407 |
| 0x008B7320 | FUN_008b7320 | unnamed | src/fallout/ai/actor.cpp:11026 |
| 0x008B7B70 | FUN_008b7b70 | probable | src/fallout/ai/actor.cpp:11047 |
| 0x008B7F00 | FUN_008b7f00 | unnamed | src/fallout/ai/actor.cpp:81682 |
| 0x008B8290 | FUN_008b8290 | unnamed | src/fallout/ai/actor.cpp:11136 |
| 0x008B9220 | FUN_008b9220 | unnamed | src/fallout/ai/actor.cpp:11425 |
| 0x008B97F0 | FUN_008b97f0 | unnamed | src/fallout/ai/actor.cpp:34472 |
| 0x008B9AB0 | FUN_008b9ab0 | unnamed | src/fallout/ai/actor.cpp:11436 |
| 0x008B9B10 | FUN_008b9b10 | unnamed | src/fallout/ai/actor.cpp:82512 |
| 0x008B9BE0 | FUN_008b9be0 | unnamed | src/fallout/ai/actor.cpp:34495 |
| 0x008B9C80 | FUN_008b9c80 | unnamed | src/fallout/ai/actor.cpp:40331 |
| 0x008B9CC0 | FUN_008b9cc0 | unnamed | src/fallout/ai/actor.cpp:82652 |
| 0x008B9D20 | FUN_008b9d20 | unnamed | src/fallout/ai/actor.cpp:11464 |
| 0x008B9D80 | FUN_008b9d80 | unnamed | src/fallout/ai/actor.cpp:11489 |
| 0x008B9DB0 | FUN_008b9db0 | unnamed | src/fallout/ai/actor.cpp:82676 |
| 0x008B9E70 | FUN_008b9e70 | unnamed | src/fallout/ai/actor.cpp:40389 |
| 0x008B9EA0 | FUN_008b9ea0 | probable | src/fallout/ai/actor.cpp:82758 |
| 0x008B9FF0 | FUN_008b9ff0 | unnamed | src/fallout/ai/actor.cpp:11512 |
| 0x008BA140 | FUN_008ba140 | unnamed | src/fallout/ai/actor.cpp:83154 |
| 0x008BA270 | FUN_008ba270 | unnamed | src/fallout/ai/actor.cpp:40646 |
| 0x008BA2B0 | FUN_008ba2b0 | unnamed | src/fallout/ai/actor.cpp:34512 |
| 0x008BA3E0 | FUN_008ba3e0 | probable | src/fallout/ai/actor.cpp:12488 |
| 0x008BA410 | FUN_008ba410 | probable | src/fallout/ai/actor.cpp:12952 |
| 0x008BA440 | FUN_008ba440 | unnamed | src/fallout/ai/actor.cpp:13417 |
| 0x008BA470 | FUN_008ba470 | unnamed | src/fallout/ai/actor.cpp:83706 |
| 0x008BB5C0 | FUN_008bb5c0 | probable | src/fallout/ai/actor.cpp:13491 |
| 0x008BBC10 | FUN_008bbc10 | probable | src/fallout/ai/actor.cpp:13786 |
| 0x008BBDB0 | FUN_008bbdb0 | probable | src/fallout/ai/actor.cpp:13802 |
| 0x008BBE00 | FUN_008bbe00 | probable | src/fallout/ai/actor.cpp:13816 |
| 0x008BBE20 | FUN_008bbe20 | unnamed | src/fallout/ai/actor.cpp:13844 |
| 0x008BBE70 | FUN_008bbe70 | unnamed | src/fallout/ai/actor.cpp:13874 |
| 0x008BBF00 | FUN_008bbf00 | unnamed | src/fallout/ai/actor.cpp:40741 |
| 0x008BC560 | FUN_008bc560 | unnamed | src/fallout/ai/actor.cpp:87771 |
| 0x008BC7F0 | FUN_008bc7f0 | probable | src/fallout/ai/actor.cpp:14054 |
| 0x008BCB40 | FUN_008bcb40 | unnamed | src/fallout/ai/actor.cpp:14201 |
| 0x008BCC80 | FUN_008bcc80 | probable | src/fallout/ai/actor.cpp:14252 |
| 0x008BCD20 | FUN_008bcd20 | unnamed | src/fallout/ai/actor.cpp:14335 |
| 0x008BCD60 | FUN_008bcd60 | unnamed | src/fallout/ai/actor.cpp:34573 |
| 0x008BD5E0 | FUN_008bd5e0 | unnamed | src/fallout/ai/actor.cpp:14427 |
| 0x008BE600 | FUN_008be600 | rejected | src/fallout/ai/actor.cpp:14643 |
| 0x008BE6D0 | FUN_008be6d0 | unnamed | src/fallout/ai/actor.cpp:88404 |
| 0x008BE8E0 | FUN_008be8e0 | unnamed | src/fallout/ai/actor.cpp:113198 |
| 0x008BE9B0 | FUN_008be9b0 | unnamed | src/fallout/ai/actor.cpp:14833 |
| 0x008BEA10 | FUN_008bea10 | rejected | src/fallout/ai/actor.cpp:14884 |
| 0x008BEA80 | FUN_008bea80 | unnamed | src/fallout/ai/actor.cpp:14923 |
| 0x008BFF50 | FUN_008bff50 | probable | src/fallout/ai/actor.cpp:34589 |
| 0x008C0050 | FUN_008c0050 | unnamed | src/fallout/ai/actor.cpp:88670 |
| 0x008C09B0 | FUN_008c09b0 | unnamed | src/fallout/ai/actor.cpp:34617 |
| 0x008C1010 | FUN_008c1010 | unnamed | src/fallout/ai/actor.cpp:142058 |
| 0x008C1270 | FUN_008c1270 | class | src/fallout/ai/actor.cpp:89645 |
| 0x008C17C0 | FUN_008c17c0 | probable | src/fallout/ai/actor.cpp:43669 |
| 0x008C1920 | FUN_008c1920 | unnamed | src/fallout/ai/actor.cpp:34629 |
| 0x008C1940 | FUN_008c1940 | probable | src/fallout/ai/actor.cpp:43968 |
| 0x008C1AC0 | FUN_008c1ac0 | unnamed | src/fallout/ai/actor.cpp:15519 |
| 0x008C1BC0 | FUN_008c1bc0 | unnamed | src/fallout/ai/actor.cpp:15552 |
| 0x008C1DE0 | FUN_008c1de0 | probable | src/fallout/ai/actor_magic.cpp:947 |
| 0x008C4090 | FUN_008c4090 | unnamed | src/fallout/ai/actor.cpp:15810 |
| 0x008C4330 | FUN_008c4330 | probable | src/fallout/ai/actor.cpp:90214 |
| 0x008C4400 | FUN_008c4400 | unnamed | src/fallout/ai/actor.cpp:15829 |
| 0x008C4420 | FUN_008c4420 | unnamed | src/fallout/ai/actor.cpp:16096 |
| 0x008C4470 | FUN_008c4470 | unnamed | src/fallout/ai/actor.cpp:16367 |
| 0x008C4560 | FUN_008c4560 | unnamed | src/fallout/ai/actor_magic.cpp:499 |
| 0x008C45E0 | FUN_008c45e0 | unnamed | src/fallout/ai/actor.cpp:34641 |
| 0x008C4610 | FUN_008c4610 | unnamed | src/fallout/ai/actor.cpp:34658 |
| 0x008C47D0 | FUN_008c47d0 | unnamed | src/fallout/ai/actor_magic.cpp:510 |
| 0x008C4E00 | FUN_008c4e00 | unnamed | src/fallout/ai/actor.cpp:33448 |
| 0x008C51C0 | FUN_008c51c0 | probable | src/fallout/ai/actor_magic.cpp:521 |
| 0x008C6030 | FUN_008c6030 | unnamed | src/fallout/ai/actorpackage.cpp:445 |
| 0x008C6060 | FUN_008c6060 | unnamed | src/fallout/ai/actorpackage.cpp:623 |
| 0x008C6100 | FUN_008c6100 | unnamed | src/fallout/ai/actorpackage.cpp:460 |
| 0x008C65A0 | FUN_008c65a0 | unnamed | src/fallout/ai/actorpackage.cpp:634 |
| 0x008C6B00 | FUN_008c6b00 | probable | src/fallout/ai/actorpackage.cpp:491 |
| 0x008C7490 | FUN_008c7490 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:148 |
| 0x008C7AA0 | FUN_008c7aa0 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:264 |
| 0x008C7BC0 | FUN_008c7bc0 | unnamed | src/fallout/ai/ailineartaskthreadmanager.cpp:363 |
| 0x008C80B0 | FUN_008c80b0 | unnamed | src/fallout/ai/ailineartaskthreadmanager.cpp:378 |
| 0x008C80C0 | FUN_008c80c0 | unnamed | src/fallout/ai/ailineartaskthreadmanager.cpp:392 |
| 0x008C80D0 | FUN_008c80d0 | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:401 |
| 0x008C8490 | FUN_008c8490 | class | src/fallout/ai/aitaskmanager.cpp:143 |
| 0x008C88E0 | FUN_008c88e0 | class | src/fallout/ai/aitaskmanager.cpp:229 |
| 0x008C8A20 | FUN_008c8a20 | class | src/fallout/ai/aitaskmanager.cpp:296 |
| 0x008C8A50 | FUN_008c8a50 | class | src/fallout/ai/aitaskmanager.cpp:314 |
| 0x008C8BD0 | FUN_008c8bd0 | unnamed | src/fallout/ai/aitaskmanager.cpp:352 |
| 0x008C90E0 | FUN_008c90e0 | class | src/fallout/ai/aitaskmanager.cpp:451 |
| 0x008C9300 | FUN_008c9300 | class | src/fallout/ai/aitaskmanager.cpp:548 |
| 0x008C9A20 | FUN_008c9a20 | unnamed | src/fallout/ai/aitaskmanager.cpp:976 |
| 0x008C9A50 | FUN_008c9a50 | unnamed | src/fallout/ai/aitaskmanager.cpp:564 |
| 0x008C9FD0 | FUN_008c9fd0 | unnamed | src/fallout/ai/aitaskmanager.cpp:1622 |
| 0x008CA300 | FUN_008ca300 | unnamed | src/fallout/ai/aitaskmanager.cpp:680 |
| 0x008CA330 | FUN_008ca330 | unnamed | src/fallout/ai/aitaskmanager.cpp:695 |
| 0x008CC730 | FUN_008cc730 | unnamed | src/fallout/ai/baseprocess.cpp:782 |
| 0x008CFBC0 | FUN_008cfbc0 | probable | src/fallout/ai/arrowprojectile_o2_variant_od_oy_noo2_variant.cpp:202 |
| 0x008D02A0 | FUN_008d02a0 | class | src/fallout/ai/baseprocess.cpp:797 |
| 0x008D02F0 | FUN_008d02f0 | class | src/fallout/ai/baseprocess.cpp:221 |
| 0x008D0310 | FUN_008d0310 | unnamed | src/fallout/ai/baseprocess.cpp:815 |
| 0x008D0340 | FUN_008d0340 | class | src/fallout/ai/baseprocess.cpp:827 |
| 0x008D0370 | FUN_008d0370 | rejected | src/fallout/ai/baseprocess.cpp:721 |
| 0x008D04D0 | FUN_008d04d0 | class | src/fallout/ai/baseprocess.cpp:853 |
| 0x008D04F0 | FUN_008d04f0 | unnamed | src/fallout/ai/baseprocess.cpp:861 |
| 0x008D0500 | FUN_008d0500 | unnamed | src/fallout/ai/baseprocess.cpp:870 |
| 0x008D0510 | FUN_008d0510_ | decomp | src/fallout/ai/actor.cpp:33459 |
| 0x008D0520 | FUN_008d0520 | unnamed | src/fallout/ai/actor.cpp:34669 |
| 0x008D0530 | FUN_008d0530 | class | src/fallout/ai/baseprocess.cpp:880 |
| 0x008D05C0 | FUN_008d05c0 | class | src/fallout/ai/baseprocess.cpp:936 |
| 0x008D05E0 | FUN_008d05e0 | unnamed | src/fallout/ai/playercharacter.cpp:2086 |
| 0x008D05F0 | FUN_008d05f0 | unnamed | src/fallout/ai/baseprocess.cpp:743 |
| 0x008D0600 | FUN_008d0600 | rejected | src/fallout/ai/baseprocess.cpp:944 |
| 0x008D08F0 | FUN_008d08f0 | class | src/fallout/ai/baseprocess.cpp:751 |
| 0x008D1920 | FUN_008d1920 | unnamed | src/fallout/ai/camerashake.cpp:32 |
| 0x008D1E90 | FUN_008d1e90 | class | src/fallout/ai/character.cpp:98 |
| 0x008D22B0 | FUN_008d22b0 | class | src/fallout/ai/character_rtti_variant.cpp:2501 |
| 0x008D24A0 | FUN_008d24a0 | class | src/fallout/ai/character.cpp:198 |
| 0x008D24F0 | FUN_008d24f0 | class | src/fallout/ai/actor.cpp:126221 |
| 0x008D2A40 | FUN_008d2a40 | class | src/fallout/ai/actor.cpp:16486 |
| 0x008D3290 | FUN_008d3290 | class | src/fallout/ai/playercharacter.cpp:2099 |
| 0x008D3F70 | FUN_008d3f70 | unnamed | src/fallout/ai/actor.cpp:33467 |
| 0x008D3F80 | FUN_008d3f80 | unnamed | src/fallout/ai/actor.cpp:33475 |
| 0x008D3F90 | FUN_008d3f90 | unnamed | src/fallout/ai/actor.cpp:33483 |
| 0x008D41F0 | FUN_008d41f0 | unnamed | src/fallout/ai/actor.cpp:40856 |
| 0x008D4840 | FUN_008d4840 | unnamed | src/fallout/ai/actor_magic.cpp:583 |
| 0x008D4930 | FUN_008d4930 | class | src/fallout/ai/creature.cpp:253 |
| 0x008D4990 | FUN_008d4990 | class | src/fallout/ai/creature.cpp:273 |
| 0x008D4AB0 | FUN_008d4ab0 | probable | src/fallout/ai/creature.cpp:334 |
| 0x008D4CA0 | FUN_008d4ca0 | unnamed | src/fallout/ai/creature.cpp:101 |
| 0x008D4CB0 | FUN_008d4cb0 | unnamed | src/fallout/ai/creature.cpp:111 |
| 0x008D4CC0 | FUN_008d4cc0 | class | src/fallout/ai/creature.cpp:814 |
| 0x008D4DB0 | FUN_008d4db0 | class | src/fallout/ai/creature.cpp:863 |
| 0x008D53F0 | FUN_008d53f0 | probable | src/fallout/ai/falloutcharacterprogression.cpp:871 |
| 0x008D54E0 | FUN_008d54e0 | unnamed | src/fallout/ai/falloutcharacterprogression.cpp:92 |
| 0x008D5590 | FUN_008d5590 | unnamed | src/fallout/ai/falloutcharacterprogression.cpp:210 |
| 0x008D55B0 | FUN_008d55b0 | unnamed | src/fallout/ai/falloutcharacterprogression.cpp:115 |
| 0x008D55E0 | FUN_008d55e0 | probable | src/fallout/ai/falloutcharacterprogression.cpp:69 |
| 0x008D5910 | FUN_008d5910 | unnamed | src/fallout/ai/followerbarks.cpp:53 |
| 0x008D6A80 | FUN_008d6a80 | unnamed | src/fallout/ai/gunwobble.cpp:20 |
| 0x008D72E0 | FUN_008d72e0 | unnamed | src/fallout/ai/highprocess.cpp:4389 |
| 0x008D73B0 | FUN_008d73b0 | unnamed | src/fallout/ai/highprocess.cpp:10142 |
| 0x008D7E00 | FUN_008d7e00 | probable | src/fallout/ai/lowprocess.cpp:2441 |
| 0x008D7F00 | FUN_008d7f00 | class | src/fallout/ai/highprocess.cpp:4426 |
| 0x008D7F40 | FUN_008d7f40 | probable | src/fallout/ai/lowprocess.cpp:2482 |
| 0x008D8580 | FUN_008d8580 | class | src/fallout/ai/highprocess.cpp:4559 |
| 0x008D85A0 | FUN_008d85a0 | class | src/fallout/ai/highprocess.cpp:11828 |
| 0x008D86A0 | FUN_008d86a0 | class | src/fallout/ai/highprocess.cpp:4594 |
| 0x008D8B80 | FUN_008d8b80 | rejected | src/fallout/ai/highprocess.cpp:4675 |
| 0x008D8CF0 | FUN_008d8cf0 | class | src/fallout/ai/highprocess.cpp:4741 |
| 0x008D8D10 | FUN_008d8d10 | class | src/fallout/ai/highprocess.cpp:4752 |
| 0x008D8D60 | FUN_008d8d60 | class | src/fallout/ai/highprocess.cpp:12605 |
| 0x008D8F90 | FUN_008d8f90 | class | src/fallout/ai/highprocess.cpp:12823 |
| 0x008D9200 | FUN_008d9200 | class | src/fallout/ai/highprocess.cpp:13552 |
| 0x008D98C0 | FUN_008d98c0 | unnamed | src/fallout/ai/highprocess.cpp:4939 |
| 0x008DADE0 | FUN_008dade0 | unnamed | src/fallout/ai/highprocess.cpp:3851 |
| 0x008DB4C0 | FUN_008db4c0 | unnamed | src/fallout/ai/highprocess.cpp:5019 |
| 0x008DBD80 | FUN_008dbd80 | unnamed | src/fallout/ai/highprocess.cpp:5030 |
| 0x008DD860 | FUN_008dd860 | unnamed | src/fallout/ai/highprocess.cpp:3864 |
| 0x008DD8E0 | FUN_008dd8e0 | probable | src/fallout/ai/highprocess.cpp:11122 |
| 0x008DEFE0 | FUN_008defe0 | probable | src/fallout/ai/highprocess.cpp:3886 |
| 0x008E30E0 | FUN_008e30e0 | unnamed | src/fallout/ai/highprocess.cpp:5261 |
| 0x008E3100 | FUN_008e3100 | unnamed | src/fallout/ai/highprocess.cpp:5274 |
| 0x008E3E90 | FUN_008e3e90 | unnamed | src/fallout/ai/highprocess.cpp:5293 |
| 0x008E5670 | FUN_008e5670 | unnamed | src/fallout/ai/highprocess.cpp:3919 |
| 0x008E95C0 | FUN_008e95c0 | unnamed | src/fallout/ai/dialoguepackage.cpp:109 |
| 0x008EBB50 | FUN_008ebb50 | unnamed | src/fallout/ai/highprocess.cpp:16938 |
| 0x008EBBE0 | FUN_008ebbe0 | unnamed | src/fallout/ai/highprocess.cpp:17623 |
| 0x008EE370 | FUN_008ee370 | class | src/fallout/ai/highprocess.cpp:17891 |
| 0x008EEA60 | FUN_008eea60 | unnamed | src/fallout/ai/highprocess.cpp:18044 |
| 0x008EEA80 | FUN_008eea80 | unnamed | src/fallout/ai/highprocess.cpp:18066 |
| 0x008EEAA0 | FUN_008eeaa0 | unnamed | src/fallout/ai/highprocess.cpp:5316 |
| 0x008F21A0 | FUN_008f21a0 | unnamed | src/fallout/ai/highprocess.cpp:4053 |
| 0x008F21C0 | FUN_008f21c0 | unnamed | src/fallout/ai/highprocess.cpp:5324 |
| 0x008F4000 | FUN_008f4000 | unnamed | src/fallout/ai/highprocess.cpp:18165 |
| 0x008F6120 | FUN_008f6120 | probable | src/fallout/ai/highprocess.cpp:5372 |
| 0x008FDB10 | FUN_008fdb10 | unnamed | src/fallout/ai/highprocess.cpp:21370 |
| 0x008FE960 | FUN_008fe960 | unnamed | src/fallout/ai/highprocess.cpp:21645 |
| 0x008FEAB0 | FUN_008feab0 | probable | src/fallout/ai/highprocess.cpp:21688 |
| 0x008FEB60 | FUN_008feb60 | probable | src/fallout/ai/highprocess.cpp:10299 |
| 0x008FF080 | FUN_008ff080 | unnamed | src/fallout/ai/highprocess.cpp:4089 |
| 0x008FFDC0 | FUN_008ffdc0 | unnamed | src/fallout/ai/highprocess.cpp:6203 |
| 0x009001C0 | FUN_009001c0 | class | src/fallout/ai/highprocess.cpp:22784 |
| 0x00900400 | FUN_00900400 | unnamed | src/fallout/ai/highprocess.cpp:4128 |
| 0x00903160 | FUN_00903160 | unnamed | src/fallout/ai/highprocess.cpp:6498 |
| 0x00903BB0 | FUN_00903bb0 | unnamed | src/fallout/ai/highprocess.cpp:4141 |
| 0x00903BD0 | FUN_00903bd0 | unnamed | src/fallout/ai/actor.cpp:16511 |
| 0x00903CD0 | FUN_00903cd0 | unnamed | src/fallout/ai/highprocess.cpp:4154 |
| 0x00903DE0 | FUN_00903de0 | unnamed | src/fallout/ai/highprocess.cpp:4170 |
| 0x00903E00 | FUN_00903e00 | unnamed | src/fallout/ai/highprocess.cpp:4185 |
| 0x00903E20 | FUN_00903e20 | unnamed | src/fallout/ai/highprocess.cpp:4200 |
| 0x00904000 | FUN_00904000 | class | src/fallout/ai/highprocess.cpp:54960 |
| 0x009052C0 | FUN_009052c0 | unnamed | src/fallout/ai/combat/combatstate.cpp:430 |
| 0x00905AA0 | FUN_00905aa0 | unnamed | src/fallout/ai/highprocess.cpp:4294 |
| 0x00905D20 | FUN_00905d20 | class | src/fallout/ai/lipsyncbackgroundmanager.cpp:334 |
| 0x00905E30 | FUN_00905e30 | unnamed | src/fallout/ai/lipsyncbackgroundmanager.cpp:54 |
| 0x00906F60 | FUN_00906f60 | probable | src/fallout/ai/lowprocess.cpp:2370 |
| 0x00907960 | FUN_00907960 | probable | src/fallout/ai/lowprocess.cpp:4367 |
| 0x009079F0 | FUN_009079f0 | rejected | src/fallout/ai/lowprocess.cpp:4418 |
| 0x0090E600 | FUN_0090e600 | unnamed | src/fallout/ai/lowprocess.cpp:2957 |
| 0x0090E660 | FUN_0090e660 | probable | src/fallout/ai/lowprocess.cpp:9269 |
| 0x00911AE0 | FUN_00911ae0 | class | src/fallout/ai/lowprocess.cpp:2467 |
| 0x009139B0 | FUN_009139b0 | unnamed | src/fallout/ai/middlehighprocess.cpp:6852 |
| 0x00915EF0 | FUN_00915ef0 | unnamed | src/fallout/ai/middlehighprocess.cpp:352 |
| 0x009180B0 | FUN_009180b0 | class | src/fallout/ai/middlehighprocess.cpp:8048 |
| 0x0091ECB0 | FUN_0091ecb0 | class | src/fallout/ai/middlehighprocess.cpp:1275 |
| 0x0091EF10 | FUN_0091ef10 | class | src/fallout/ai/middlehighprocess.cpp:1632 |
| 0x00920B60 | FUN_00920b60 | unnamed | src/fallout/ai/middlehighprocess.cpp:3108 |
| 0x00920B70 | FUN_00920b70 | unnamed | src/fallout/ai/middlehighprocess.cpp:3116 |
| 0x00922AD0 | FUN_00922ad0 | class | src/fallout/ai/middlehighprocess.cpp:9360 |
| 0x00929240 | FUN_00929240 | unnamed | src/fallout/ai/middlehighprocess.cpp:3200 |
| 0x00929390 | FUN_00929390 | unnamed | src/fallout/ai/middlehighprocess.cpp:12354 |
| 0x00929820 | FUN_00929820 | unnamed | src/fallout/ai/middlehighprocess.cpp:4649 |
| 0x00929D20 | FUN_00929d20 | unnamed | src/fallout/ai/middlehighprocess.cpp:3216 |
| 0x0092A980 | FUN_0092a980 | unnamed | src/fallout/ai/middlehighprocess.cpp:56 |
| 0x0092AC10 | FUN_0092ac10 | class | src/fallout/ai/middlehighprocess.cpp:29617 |
| 0x0092B460 | FUN_0092b460 | class | src/fallout/ai/middlehighprocess.cpp:13447 |
| 0x0092BF20 | FUN_0092bf20 | probable | src/fallout/ai/middlehighprocess.cpp:13829 |
| 0x0092C0C0 | FUN_0092c0c0 | unnamed | src/fallout/ai/middlehighprocess.cpp:6677 |
| 0x0092C8B0 | FUN_0092c8b0 | unnamed | src/fallout/ai/middlehighprocess.cpp:2763 |
| 0x0092CC90 | FUN_0092cc90 | class | src/fallout/ai/middlelowprocess.cpp:574 |
| 0x0092CFD0 | FUN_0092cfd0 | class | src/fallout/ai/middlelowprocess.cpp:751 |
| 0x0092F190 | FUN_0092f190 | unnamed | src/fallout/ai/mobileobject.cpp:2000 |
| 0x009304A0 | FUN_009304a0 | unnamed | src/fallout/ai/mobileobject.cpp:1172 |
| 0x009304D0 | FUN_009304d0 | unnamed | src/fallout/ai/mobileobject.cpp:7977 |
| 0x00930540 | FUN_00930540 | unnamed | src/fallout/ai/mobileobject.cpp:2020 |
| 0x009305A0 | FUN_009305a0 | unnamed | src/fallout/ai/mobileobject.cpp:1596 |
| 0x009305D0 | FUN_009305d0 | unnamed | src/fallout/ai/mobileobject.cpp:2042 |
| 0x00930620 | FUN_00930620 | unnamed | src/fallout/ai/mobileobject.cpp:1259 |
| 0x009314D0 | FUN_009314d0 | unnamed | src/fallout/ai/actor.cpp:34703 |
| 0x00931560 | FUN_00931560 | unnamed | src/fallout/ai/actor.cpp:33529 |
| 0x00931580 | FUN_00931580 | unnamed | src/fallout/ai/actor.cpp:34732 |
| 0x009315C0 | FUN_009315c0 | class | src/fallout/ai/actor.cpp:95023 |
| 0x00931880 | FUN_00931880 | class | src/fallout/ai/mobileobject.cpp:2223 |
| 0x009319C0 | FUN_009319c0 | unnamed | src/fallout/ai/mobileobject.cpp:3214 |
| 0x00931FB0 | FUN_00931fb0 | probable | src/fallout/ai/mobileobject.cpp:741 |
| 0x00933480 | FUN_00933480 | unnamed | src/fallout/ai/mobileobject.cpp:14364 |
| 0x00934250 | FUN_00934250 | probable | src/fallout/ai/mobileobject.cpp:5014 |
| 0x00937B30 | FUN_00937b30 | probable | src/fallout/ai/modifierlist.cpp:221 |
| 0x00937D70 | FUN_00937d70 | unnamed | src/fallout/ai/modifierlist.cpp:148 |
| 0x00937E10 | FUN_00937e10 | unnamed | src/fallout/ai/modifierlist.cpp:402 |
| 0x009396C0 | FUN_009396c0 | class | src/fallout/ai/playercharacter.cpp:2110 |
| 0x00939710 | FUN_00939710 | unnamed | src/fallout/ai/actor.cpp:16906 |
| 0x00939770 | FUN_00939770 | class | src/fallout/ai/playercharacter.cpp:2143 |
| 0x00939840 | FUN_00939840 | unnamed | src/fallout/ai/playercharacter.cpp:2196 |
| 0x00939860 | FUN_00939860 | unnamed | src/fallout/ai/playercharacter.cpp:2207 |
| 0x00939880 | FUN_00939880 | unnamed | src/fallout/ai/playercharacter.cpp:2218 |
| 0x0093A7A0 | FUN_0093a7a0 | probable | src/fallout/ai/playercharacter.cpp:2285 |
| 0x0093A8F0 | FUN_0093a8f0 | class | src/fallout/ai/character.cpp:2177 |
| 0x0093B240 | FUN_0093b240 | class | src/fallout/ai/playercharacter.cpp:4610 |
| 0x0093D4F0 | FUN_0093d4f0 | unnamed | src/fallout/ai/playercharacter.cpp:10066 |
| 0x0093DB40 | FUN_0093db40 | unnamed | src/fallout/ai/playercharacter.cpp:10658 |
| 0x0093E4F0 | FUN_0093e4f0 | unnamed | src/fallout/ai/playercharacter.cpp:12166 |
| 0x0093E510 | FUN_0093e510 | unnamed | src/fallout/ai/playercharacter.cpp:12180 |
| 0x00947C90 | FUN_00947c90 | unnamed | src/fallout/ai/playercharacter.cpp:16130 |
| 0x00947D80 | FUN_00947d80 | probable | src/fallout/ai/playercharacter.cpp:16196 |
| 0x00948000 | FUN_00948000 | unnamed | src/fallout/ai/playercharacter.cpp:16269 |
| 0x00948030 | FUN_00948030 | unnamed | src/fallout/ai/playercharacter.cpp:16283 |
| 0x009481D0 | FUN_009481d0 | probable | src/fallout/ai/playercharacter.cpp:16697 |
| 0x0094A070 | FUN_0094a070 | unnamed | src/fallout/ai/playercharacter.cpp:18250 |
| 0x0094A0A0 | FUN_0094a0a0 | unnamed | src/fallout/ai/playercharacter.cpp:18261 |
| 0x0094C460 | FUN_0094c460 | unnamed | src/fallout/ai/actor.cpp:34760 |
| 0x0094C490 | FUN_0094c490 | unnamed | src/fallout/ai/actor_magic.cpp:598 |
| 0x0094C4C0 | FUN_0094c4c0 | unnamed | src/fallout/ai/actor_magic.cpp:614 |
| 0x0094C660 | FUN_0094c660 | class | src/fallout/ai/playercharacter.cpp:20516 |
| 0x0094C870 | FUN_0094c870 | unnamed | src/fallout/ai/actor.cpp:34772 |
| 0x0094C890 | FUN_0094c890 | unnamed | src/fallout/ai/actor.cpp:34786 |
| 0x0094CA20 | FUN_0094ca20 | unnamed | src/fallout/ai/actor.cpp:16931 |
| 0x0094CA50 | FUN_0094ca50 | unnamed | src/fallout/ai/actor.cpp:46194 |
| 0x0094EAC0 | FUN_0094eac0 | unnamed | src/fallout/ai/playercharacter.cpp:22662 |
| 0x0094EAD0 | FUN_0094ead0 | unnamed | src/fallout/ai/playercharacter.cpp:22670 |
| 0x0094EAE0 | FUN_0094eae0 | unnamed | src/fallout/ai/playercharacter.cpp:22678 |
| 0x0094EAF0 | FUN_0094eaf0 | unnamed | src/fallout/ai/playercharacter.cpp:22740 |
| 0x0094EB30 | FUN_0094eb30 | unnamed | src/fallout/ai/playercharacter.cpp:22750 |
| 0x0094EC90 | FUN_0094ec90 | unnamed | src/fallout/ai/playercharacter.cpp:23712 |
| 0x00950030 | FUN_00950030 | probable | src/fallout/ai/playercharacter.cpp:25489 |
| 0x00950110 | FUN_00950110 | probable | src/fallout/ai/playercharacter.cpp:25544 |
| 0x00950660 | FUN_00950660 | class | src/fallout/ai/playercharacter.cpp:27077 |
| 0x00950B30 | FUN_00950b30 | unnamed | src/fallout/ai/playercharacter.cpp:27686 |
| 0x00950BB0 | FUN_00950bb0 | unnamed | src/fallout/ai/playercharacter.cpp:27704 |
| 0x00950C20 | FUN_00950c20 | probable | src/fallout/ai/playercharacter.cpp:28402 |
| 0x00951900 | FUN_00951900 | unnamed | src/fallout/ai/playercharacter.cpp:28553 |
| 0x00951910 | FUN_00951910 | unnamed | src/fallout/ai/playercharacter.cpp:28561 |
| 0x00951920 | FUN_00951920 | unnamed | src/fallout/ai/playercharacter.cpp:28569 |
| 0x00951930 | FUN_00951930 | unnamed | src/fallout/ai/playercharacter.cpp:28577 |
| 0x009526E0 | FUN_009526e0 | unnamed | src/fallout/ai/playercharacter.cpp:30871 |
| 0x00952720 | FUN_00952720 | unnamed | src/fallout/ai/actor.cpp:17097 |
| 0x00953C20 | FUN_00953c20 | probable | src/fallout/ai/playercharacter.cpp:32299 |
| 0x00953CE0 | FUN_00953ce0 | probable | src/fallout/ai/playercharacter.cpp:32363 |
| 0x00953D40 | FUN_00953d40 | unnamed | src/fallout/ai/playercharacter.cpp:32399 |
| 0x00953F60 | FUN_00953f60 | unnamed | src/fallout/ai/playercharacter.cpp:33014 |
| 0x00953F80 | FUN_00953f80 | unnamed | src/fallout/ai/playercharacter.cpp:33033 |
| 0x00953FB0 | FUN_00953fb0 | class | src/fallout/ai/playercharacter.cpp:33045 |
| 0x00954960 | FUN_00954960 | unnamed | src/fallout/ai/actor.cpp:17113 |
| 0x0095D090 | FUN_0095d090 | unnamed | src/fallout/ai/playercharacter.cpp:38865 |
| 0x0095EE60 | FUN_0095ee60 | unnamed | src/fallout/ai/playercharacter.cpp:40923 |
| 0x0095EE70 | FUN_0095ee70 | unnamed | src/fallout/ai/playercharacter.cpp:40934 |
| 0x00961F90 | FUN_00961f90 | probable | src/fallout/ai/playercharacter.cpp:41843 |
| 0x00963730 | FUN_00963730 | unnamed | src/fallout/ai/playercharacter.cpp:44071 |
| 0x00963B00 | FUN_00963b00 | unnamed | src/fallout/ai/playercharacter.cpp:44334 |
| 0x009655A0 | FUN_009655a0 | probable | src/fallout/ai/playercharacter.cpp:46318 |
| 0x00967160 | FUN_00967160 | unnamed | src/fallout/ai/playercharacter.cpp:49317 |
| 0x00967220 | FUN_00967220 | unnamed | src/fallout/ai/playercharacter.cpp:49356 |
| 0x00967AA0 | FUN_00967aa0 | unnamed | src/fallout/ai/playercharacter.cpp:51574 |
| 0x00967AC0 | FUN_00967ac0 | unnamed | src/fallout/ai/playercharacter.cpp:51585 |
| 0x00967AE0 | FUN_00967ae0 | probable | src/fallout/ai/playercharacter.cpp:52039 |
| 0x009691D0 | FUN_009691d0 | unnamed | src/fallout/ai/playercharacter.cpp:54831 |
| 0x00969860 | FUN_00969860 | probable | src/fallout/ai/playercharacter.cpp:55737 |
| 0x00969AC0 | FUN_00969ac0 | unnamed | src/fallout/ai/playercharacter.cpp:56214 |
| 0x00969AE0 | FUN_00969ae0 | unnamed | src/fallout/ai/playercharacter.cpp:56227 |
| 0x00969B00 | FUN_00969b00 | unnamed | src/fallout/ai/playercharacter.cpp:56240 |
| 0x00969B80 | FUN_00969b80 | unnamed | src/fallout/ai/playercharacter.cpp:56300 |
| 0x00969BC0 | FUN_00969bc0 | unnamed | src/fallout/ai/playercharacter.cpp:56331 |
| 0x00969E70 | FUN_00969e70 | unnamed | src/fallout/ai/playercharacter.cpp:56476 |
| 0x0096A2B0 | FUN_0096a2b0 | unnamed | src/fallout/ai/combat/combatgroup_iso_variant.cpp:8145 |
| 0x0096A820 | FUN_0096a820 | unnamed | src/fallout/ai/procedure.cpp:6 |
| 0x0096A850 | FUN_0096a850 | unnamed | src/fallout/ai/character.cpp:1742 |
| 0x0096AAF0 | FUN_0096aaf0 | unnamed | src/fallout/ai/processlists.cpp:2508 |
| 0x0096C710 | FUN_0096c710 | probable | src/fallout/ai/processlists.cpp:468 |
| 0x0096CB20 | FUN_0096cb20 | unnamed | src/fallout/ai/processlists.cpp:3042 |
| 0x0096CCA0 | FUN_0096cca0 | probable | src/fallout/ai/processlists.cpp:5610 |
| 0x0096D490 | FUN_0096d490 | probable | src/fallout/ai/processlists.cpp:584 |
| 0x0096EB40 | FUN_0096eb40 | probable | src/fallout/ai/processlists.cpp:17070 |
| 0x009707F0 | FUN_009707f0 | unnamed | src/fallout/ai/processlists.cpp:2840 |
| 0x00971BA0 | FUN_00971ba0 | probable | src/fallout/ai/processlists.cpp:2856 |
| 0x00971FD0 | FUN_00971fd0 | unnamed | src/fallout/ai/processlists.cpp:3523 |
| 0x009726E0 | FUN_009726e0 | unnamed | src/fallout/ai/processlists.cpp:6219 |
| 0x00973CB0 | FUN_00973cb0 | probable | src/fallout/ai/processlists.cpp:6547 |
| 0x009749B0 | FUN_009749b0 | unnamed | src/fallout/ai/processlists.cpp:6833 |
| 0x00974AF0 | FUN_00974af0 | unnamed | src/fallout/ai/processlists.cpp:2928 |
| 0x00974B80 | FUN_00974b80 | unnamed | src/fallout/ai/processlists.cpp:4550 |
| 0x00974C30 | FUN_00974c30 | unnamed | src/fallout/ai/processlists.cpp:3190 |
| 0x00975080 | FUN_00975080 | unnamed | src/fallout/ai/processlists.cpp:934 |
| 0x009754F0 | FUN_009754f0 | unnamed | src/fallout/ai/processlists.cpp:4705 |
| 0x00975EA0 | FUN_00975ea0 | probable | src/fallout/ai/processlists.cpp:4742 |
| 0x009781A0 | FUN_009781a0 | unnamed | src/fallout/ai/processlists.cpp:3119 |
| 0x00978420 | FUN_00978420 | probable | src/fallout/ai/processlists.cpp:5325 |
| 0x00978F10 | FUN_00978f10 | class | src/fallout/ai/combat/projectile.cpp:293 |
| 0x00979280 | FUN_00979280 | class | src/fallout/ai/combat/beamprojectile.cpp:421 |
| 0x00979510 | FUN_00979510 | class | src/fallout/ai/combat/beamprojectile.cpp:1626 |
| 0x00979BB0 | FUN_00979bb0 | unnamed | src/fallout/ai/combat/beamprojectile.cpp:110 |
| 0x00979E40 | FUN_00979e40 | class | src/fallout/ai/combat/combataction.cpp:117 |
| 0x00979F50 | FUN_00979f50 | unnamed | src/fallout/ai/combat/combataction.cpp:217 |
| 0x00979F70 | FUN_00979f70 | unnamed | src/fallout/ai/combat/combataction.cpp:234 |
| 0x0097ABD0 | FUN_0097abd0 | unnamed | src/fallout/ai/combat/combataction.cpp:252 |
| 0x0097AE00 | FUN_0097ae00 | class | src/fallout/ai/combat/combatactions.cpp:828 |
| 0x0097AF70 | FUN_0097af70 | unnamed | src/fallout/ai/combat/combatactions.cpp:876 |
| 0x0097B170 | FUN_0097b170 | unnamed | src/fallout/ai/combat/combatactions.cpp:912 |
| 0x0097B240 | FUN_0097b240 | unnamed | src/fallout/ai/combat/combatactions.cpp:403 |
| 0x0097B410 | FUN_0097b410 | unnamed | src/fallout/ai/combat/combatactions.cpp:940 |
| 0x0097B5A0 | FUN_0097b5a0 | class | src/fallout/ai/combat/combatactions.cpp:448 |
| 0x0097B940 | FUN_0097b940 | unnamed | src/fallout/ai/combat/combatactions.cpp:491 |
| 0x0097B980 | FUN_0097b980 | class | src/fallout/ai/combat/combatactions.cpp:517 |
| 0x0097BB90 | FUN_0097bb90 | probable | src/fallout/ai/combat/combatactions.cpp:536 |
| 0x0097BCC0 | FUN_0097bcc0 | class | src/fallout/ai/combat/combatactions.cpp:587 |
| 0x0097C280 | FUN_0097c280 | unnamed | src/fallout/ai/combat/combatactions.cpp:1146 |
| 0x0097C310 | FUN_0097c310 | class | src/fallout/ai/combat/combatactions.cpp:1183 |
| 0x0097C490 | FUN_0097c490 | unnamed | src/fallout/ai/combat/combatactions.cpp:641 |
| 0x0097C4D0 | FUN_0097c4d0 | class | src/fallout/ai/combat/combatactions.cpp:659 |
| 0x0097C520 | FUN_0097c520 | unnamed | src/fallout/ai/combat/combatactions.cpp:675 |
| 0x0097C6B0 | FUN_0097c6b0 | class | src/fallout/ai/combat/combatactions.cpp:691 |
| 0x0097C790 | FUN_0097c790 | unnamed | src/fallout/ai/combat/combatactions.cpp:1266 |
| 0x0097EF30 | FUN_0097ef30 | probable | src/fallout/ai/combat/combatstate.cpp:494 |
| 0x0097F2D0 | FUN_0097f2d0 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:14 |
| 0x0097F310 | FUN_0097f310 | probable | src/fallout/ai/combatcontroller.cpp:3459 |
| 0x0097F720 | FUN_0097f720 | unnamed | src/fallout/ai/combatcontroller.cpp:3544 |
| 0x0097F8C0 | FUN_0097f8c0 | unnamed | src/fallout/ai/combatcontroller.cpp:3068 |
| 0x0097FB20 | FUN_0097fb20 | unnamed | src/fallout/ai/combatcontroller.cpp:301 |
| 0x0097FD40 | FUN_0097fd40 | probable | src/fallout/ai/combatcontroller.cpp:507 |
| 0x0097FD60 | FUN_0097fd60 | unnamed | src/fallout/ai/combatcontroller.cpp:526 |
| 0x00980360 | FUN_00980360 | unnamed | src/fallout/ai/combatcontroller.cpp:2557 |
| 0x00980400 | FUN_00980400 | unnamed | src/fallout/ai/combatcontroller.cpp:3684 |
| 0x009804D0 | FUN_009804d0 | unnamed | src/fallout/ai/combatcontroller.cpp:911 |
| 0x00980700 | FUN_00980700 | unnamed | src/fallout/ai/combatcontroller.cpp:340 |
| 0x00980740 | FUN_00980740 | unnamed | src/fallout/ai/combatcontroller.cpp:549 |
| 0x00980770 | FUN_00980770 | unnamed | src/fallout/ai/combatcontroller.cpp:929 |
| 0x00980790 | FUN_00980790 | unnamed | src/fallout/ai/combatcontroller.cpp:5880 |
| 0x009807B0 | FUN_009807b0 | unnamed | src/fallout/ai/combatcontroller.cpp:944 |
| 0x00981300 | FUN_00981300 | probable | src/fallout/ai/combatcontroller.cpp:579 |
| 0x009818E0 | FUN_009818e0 | probable | src/fallout/ai/combatcontroller.cpp:1335 |
| 0x00981970 | FUN_00981970 | probable | src/fallout/ai/combatcontroller.cpp:956 |
| 0x00982070 | FUN_00982070 | unnamed | src/fallout/ai/combatcontroller.cpp:637 |
| 0x00982350 | FUN_00982350 | unnamed | src/fallout/ai/combatcontroller.cpp:4179 |
| 0x00983280 | FUN_00983280 | unnamed | src/fallout/ai/combat/combatcovermap.cpp:168 |
| 0x00983380 | FUN_00983380 | unnamed | src/fallout/ai/combat/combatcovermap.cpp:218 |
| 0x00984390 | FUN_00984390 | unnamed | src/fallout/ai/combat/combatactions.cpp:318 |
| 0x00984A90 | FUN_00984a90 | unnamed | src/fallout/ai/combat/combatgoal.cpp:441 |
| 0x00985BB0 | FUN_00985bb0 | probable | src/fallout/ai/combat/combatgroup.cpp:847 |
| 0x00986760 | FUN_00986760 | unnamed | src/fallout/ai/combat/combatgroup.cpp:3156 |
| 0x00986950 | FUN_00986950 | unnamed | src/fallout/ai/combat/combatgroup.cpp:520 |
| 0x00986AA0 | FUN_00986aa0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:561 |
| 0x00986B70 | FUN_00986b70 | unnamed | src/fallout/ai/combat/combatgroup.cpp:1181 |
| 0x00986BD0 | FUN_00986bd0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:2009 |
| 0x00986C40 | FUN_00986c40 | unnamed | src/fallout/ai/combat/combatgroup.cpp:37 |
| 0x009871C0 | FUN_009871c0 | probable | src/fallout/ai/combat/combatgroup.cpp:56 |
| 0x009891D0 | FUN_009891d0 | probable | src/fallout/ai/combat/combatgroup.cpp:734 |
| 0x00989490 | FUN_00989490 | probable | src/fallout/ai/combat/combatgroup.cpp:11053 |
| 0x0098A2E0 | FUN_0098a2e0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:1228 |
| 0x0098A340 | FUN_0098a340 | probable | src/fallout/ai/combat/combatgroup.cpp:4367 |
| 0x0098A360 | FUN_0098a360 | unnamed | src/fallout/ai/combat/combatgroup.cpp:231 |
| 0x0098A3C0 | FUN_0098a3c0 | unnamed | src/fallout/ai/combat/combatgroup.cpp:1256 |
| 0x0098A470 | FUN_0098a470 | probable | src/fallout/ai/combat/combatgroup.cpp:1287 |
| 0x0098ED80 | FUN_0098ed80 | unnamed | src/fallout/ai/combat/combatgroup.cpp:2778 |
| 0x0098EFA0 | FUN_0098efa0 | class | src/fallout/ai/combat/combatgroup.cpp:284 |
| 0x0098EFD0 | FUN_0098efd0 | class | src/fallout/ai/combat/combatgroup.cpp:297 |
| 0x0098F040 | FUN_0098f040 | unnamed | src/fallout/ai/combat/combatgroup.cpp:1880 |
| 0x00990480 | FUN_00990480 | unnamed | src/fallout/ai/combat/combatgroupstrategy.cpp:128 |
| 0x00990570 | FUN_00990570 | probable | src/fallout/ai/combat/combatgroupstrategy.cpp:162 |
| 0x00990890 | FUN_00990890 | probable | src/fallout/ai/combat/combatgroupstrategy.cpp:16 |
| 0x00991DC0 | FUN_00991dc0 | unnamed | src/fallout/ai/combat/combatmanager.cpp:68 |
| 0x00992640 | FUN_00992640 | unnamed | src/fallout/ai/combat/combatmanager.cpp:2184 |
| 0x009957F0 | FUN_009957f0 | unnamed | src/fallout/ai/combat/combatworldstate.cpp:33 |
| 0x00995830 | FUN_00995830 | unnamed | src/fallout/ai/combatcontroller.cpp:681 |
| 0x00997480 | FUN_00997480 | unnamed | src/fallout/ai/combat/combatstate.cpp:2094 |
| 0x00997BF0 | FUN_00997bf0 | unnamed | src/fallout/ai/combat/combatstate.cpp:622 |
| 0x00997C10 | FUN_00997c10 | unnamed | src/fallout/ai/combat/combatstate.cpp:206 |
| 0x00998980 | FUN_00998980 | probable | src/fallout/ai/combat/combatstate.cpp:680 |
| 0x00999100 | FUN_00999100 | unnamed | src/fallout/ai/combat/combatstate.cpp:727 |
| 0x0099A2A0 | FUN_0099a2a0 | unnamed | src/fallout/ai/combat/combatstate.cpp:11531 |
| 0x0099A3E0 | FUN_0099a3e0 | unnamed | src/fallout/ai/combat/combatstate.cpp:758 |
| 0x0099A650 | FUN_0099a650 | unnamed | src/fallout/ai/combat/combatstate.cpp:815 |
| 0x0099AB50 | FUN_0099ab50 | unnamed | src/fallout/ai/combat/combatstate.cpp:939 |
| 0x0099B520 | FUN_0099b520 | unnamed | src/fallout/ai/combat/combatstate.cpp:991 |
| 0x0099B8E0 | FUN_0099b8e0 | probable | src/fallout/ai/combat/combatstate.cpp:10047 |
| 0x0099C1F0 | FUN_0099c1f0 | unnamed | src/fallout/ai/combat/combatstate.cpp:1028 |
| 0x0099CB00 | FUN_0099cb00 | unnamed | src/fallout/ai/combat/combatstate.cpp:1049 |
| 0x009A0260 | FUN_009a0260 | unnamed | src/fallout/ai/combat/combatstate.cpp:1074 |
| 0x009A02A0 | FUN_009a02a0 | probable | src/fallout/ai/combat/combatstate.cpp:3019 |
| 0x009A0510 | FUN_009a0510 | probable | src/fallout/ai/combat/combatcovermap.cpp:70 |
| 0x009A0560 | FUN_009a0560 | unnamed | src/fallout/ai/combat/combatcovermap.cpp:98 |
| 0x009A0600 | FUN_009a0600 | unnamed | src/fallout/ai/combat/combatstate.cpp:1906 |
| 0x009A0B00 | FUN_009a0b00 | probable | src/fallout/ai/combat/combatstate.cpp:1957 |
| 0x009A2BF0 | FUN_009a2bf0 | unnamed | src/fallout/ai/combat/combatstate.cpp:1334 |
| 0x009A2D20 | FUN_009a2d20 | unnamed | src/fallout/ai/combat/combatstate.cpp:1387 |
| 0x009A2D50 | FUN_009a2d50 | unnamed | src/fallout/ai/combat/combatstate.cpp:1413 |
| 0x009A3280 | FUN_009a3280 | unnamed | src/fallout/ai/combat/combatstate.cpp:1507 |
| 0x009A3610 | FUN_009a3610 | unnamed | src/fallout/ai/combat/combatstate.cpp:3510 |
| 0x009A3830 | FUN_009a3830 | unnamed | src/fallout/ai/actor.cpp:33568 |
| 0x009A3FB0 | FUN_009a3fb0 | unnamed | src/fallout/ai/combat/combattargetmap.cpp:69 |
| 0x009A40C0 | FUN_009a40c0 | unnamed | src/fallout/ai/combat/combattargetmap.cpp:96 |
| 0x009A6A40 | FUN_009a6a40 | probable | src/fallout/ai/combat/combatutilities.cpp:3683 |
| 0x009A8D80 | FUN_009a8d80 | unnamed | src/fallout/ai/combat/combatutilities.cpp:3426 |
| 0x009A9370 | FUN_009a9370 | probable | src/fallout/ai/combat/combatutilities.cpp:266 |
| 0x009A97B0 | FUN_009a97b0 | unnamed | src/fallout/ai/combat/combatutilities.cpp:17 |
| 0x009A98A0 | FUN_009a98a0 | unnamed | src/fallout/ai/combat/combatutilities.cpp:661 |
| 0x009AAD00 | FUN_009aad00 | unnamed | src/fallout/ai/combat/combatworldstate.cpp:43 |
| 0x009AAD60 | FUN_009aad60 | unnamed | src/fallout/ai/combat/combatworldstate.cpp:25 |
| 0x009AB9A0 | FUN_009ab9a0 | rejected | src/fallout/ai/actor.cpp:34820 |
| 0x009AB9C0 | FUN_009ab9c0 | class | src/fallout/ai/combat/continuousbeamprojectile.cpp:187 |
| 0x009ABEF0 | FUN_009abef0 | unnamed | src/fallout/ai/combat/beamprojectile.cpp:125 |
| 0x009AC910 | FUN_009ac910 | unnamed | src/fallout/ai/combat/explosion.cpp:169 |
| 0x009AE0F0 | FUN_009ae0f0 | unnamed | src/fallout/ai/combat/explosion.cpp:604 |
| 0x009AE580 | FUN_009ae580 | probable | src/fallout/ai/combat/explosion.cpp:405 |
| 0x009AFBE0 | FUN_009afbe0 | unnamed | src/fallout/ai/combat/explosion.cpp:424 |
| 0x009AFC10 | FUN_009afc10 | unnamed | src/fallout/ai/combat/explosion.cpp:143 |
| 0x009AFC30 | FUN_009afc30 | unnamed | src/fallout/ai/combat/explosion.cpp:76 |
| 0x009AFC50 | FUN_009afc30 | unnamed | src/fallout/ai/combat/explosion.cpp:156 |
| 0x009B0D30 | FUN_009b0d30 | unnamed | src/fallout/ai/combat/explosion.cpp:510 |
| 0x009B1450 | FUN_009b1450 | class | src/fallout/ai/mobileobject.cpp:9656 |
| 0x009B28A0 | FUN_009b28a0 | unnamed | src/fallout/ai/actor_magic.cpp:643 |
| 0x009B3490 | FUN_009b3490 | unnamed | src/fallout/ai/combat/projectile.cpp:404 |
| 0x009B3CB0 | FUN_009b3cb0 | unnamed | src/fallout/ai/combat/flameprojectile.cpp:16 |
| 0x009B3F80 | FUN_009b3f80 | unnamed | src/fallout/ai/combat/flameprojectile.cpp:126 |
| 0x009B4440 | FUN_009b4440 | probable | src/fallout/ai/combat/projectile.cpp:864 |
| 0x009B4C70 | FUN_009b4c70 | class | src/fallout/ai/combat/grenadeprojectile.cpp:88 |
| 0x009B4FE0 | FUN_009b4fe0 | unnamed | src/fallout/ai/combat/hitdata.cpp:308 |
| 0x009B7010 | FUN_009b7010 | probable | src/fallout/ai/combat/hitdata.cpp:150 |
| 0x009B7870 | FUN_009b7870 | unnamed | src/fallout/ai/combat/hitdata.cpp:347 |
| 0x009B7C90 | FUN_009b7c90 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:100 |
| 0x009B7CB0 | FUN_009b7cb0 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:8 |
| 0x009BA320 | FUN_009ba320 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:145 |
| 0x009BA350 | FUN_009ba350 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:161 |
| 0x009BA390 | FUN_009ba390 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:176 |
| 0x009BA3D0 | FUN_009ba3d0 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:196 |
| 0x009BA5F0 | FUN_009ba5f0 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:276 |
| 0x009BA610 | FUN_009ba610 | unnamed | src/fallout/ai/combat/missileprojectile.cpp:289 |
| 0x009BABA0 | FUN_009baba0 | class | src/fallout/ai/combat/projectile.cpp:876 |
| 0x009BACB0 | FUN_009bacb0 | unnamed | src/fallout/ai/combat/muzzleflash.cpp:111 |
| 0x009BB6D0 | FUN_009bb6d0 | probable | src/fallout/ai/combat/muzzleflash.cpp:1413 |
| 0x009BC8C0 | FUN_009bc8c0 | class | src/fallout/ai/mobileobject.cpp:1639 |
| 0x009BFFB0 | FUN_009bffb0 | unnamed | src/fallout/ai/combat/projectile.cpp:1548 |
| 0x009C0D80 | FUN_009c0d80 | probable | src/fallout/ai/combat/projectile_gf_variant.cpp:209 |
| 0x009C1A70 | FUN_009c1a70 | unnamed | src/fallout/ai/combat/projectile.cpp:120 |
| 0x009C2FF0 | FUN_009c2ff0 | unnamed | src/fallout/ai/combat/projectile.cpp:1741 |
| 0x009C45D0 | FUN_009c45d0 | class | src/fallout/ai/mobileobject.cpp:5296 |
| 0x009C5BA0 | FUN_009c5ba0 | probable | src/fallout/ai/combat/projectile_o2_variant_od_oy_noo2_variant.cpp:1971 |
| 0x009C8E00 | FUN_009c8e00 | probable | src/fallout/ai/combat/vats.cpp:314 |
| 0x009C8EA0 | FUN_009c8ea0 | unnamed | src/fallout/ai/combat/vats.cpp:199 |
| 0x009C8EF0 | FUN_009c8ef0 | unnamed | src/fallout/ai/combat/vats.cpp:131 |
| 0x009CA500 | FUN_009ca500 | rejected | src/fallout/ai/combat/vats.cpp:452 |
| 0x009CB440 | FUN_009cb440 | probable | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:27 |
| 0x009CB830 | FUN_009cb830 | class | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:88 |
| 0x009CC490 | FUN_009cc490 | unnamed | src/fallout/ai/combat/combatstate.cpp:1548 |
| 0x009CD3D0 | FUN_009cd3d0 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:199 |
| 0x009CD410 | FUN_009cd410 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:214 |
| 0x009CDE10 | FUN_009cde10 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:253 |
| 0x009CEF70 | FUN_009cef70 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:25 |
| 0x009CEF90 | FUN_009cef90 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:36 |
| 0x009CEFB0 | FUN_009cefb0 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:331 |
| 0x009CF030 | FUN_009cf030 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:7125 |
| 0x009CFBD0 | FUN_009cfbd0 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:371 |
| 0x009CFC00 | FUN_009cfc00 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:390 |
| 0x009CFC40 | FUN_009cfc40 | unnamed | src/fallout/ai/combat/combatprocedureattackmelee.cpp:71 |
| 0x009D0590 | FUN_009d0590 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:516 |
| 0x009D0610 | FUN_009d0610 | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:545 |
| 0x009D1DE0 | FUN_009d1de0 | probable | src/fallout/ai/combat/combatprocedureattackranged.cpp:740 |
| 0x009D2510 | FUN_009d2510 | rejected | src/fallout/ai/combat/combatprocedurebeincover.cpp:86 |
| 0x009D3390 | FUN_009d3390 | unnamed | src/fallout/ai/combat/combatgroup.cpp:5965 |
| 0x009D6730 | FUN_009d6730 | unnamed | src/fallout/ai/combat/combatstate.cpp:1562 |
| 0x009D6C80 | FUN_009d6c80 | probable | src/fallout/ai/combat/combatstate.cpp:1575 |
| 0x009D7C20 | FUN_009d7c20 | probable | src/fallout/ai/combat/combatstate.cpp:1587 |
| 0x009D84B0 | FUN_009d84b0 | class | src/fallout/ai/combat/combatproceduremove.cpp:102 |
| 0x009D84E0 | FUN_009d84e0 | class | src/fallout/ai/combat/combatproceduremove.cpp:126 |
| 0x009DBA30 | FUN_009dba30 | unnamed | src/fallout/ai/movement/actormover.cpp:214 |
| 0x009DCAE0 | FUN_009dcae0 | unnamed | src/fallout/ai/movement/actormover.cpp:308 |
| 0x009DCC20 | FUN_009dcc20 | probable | src/fallout/ai/movement/actormover.cpp:1473 |
| 0x009DE0A0 | FUN_009de0a0 | unnamed | src/fallout/ai/movement/actormover.cpp:3810 |
| 0x009E16C0 | FUN_009e16c0 | unnamed | src/fallout/ai/playercharacter.cpp:57265 |
| 0x009E16E0 | FUN_009e16e0 | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:1844 |
| 0x009E22D0 | FUN_009e22d0 | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:7627 |
| 0x009E27E0 | FUN_009e27e0 | unnamed | src/fallout/ai/movement/detailedactorpathhandler.cpp:166 |
| 0x009E2A80 | FUN_009e2a80 | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:5297 |
| 0x009E55E0 | FUN_009e55e0 | unnamed | src/fallout/ai/movement/detailedactorpathhandler.cpp:612 |
| 0x009E6870 | FUN_009e6870 | unnamed | src/fallout/ai/movement/detailedactorpathhandler.cpp:5348 |
| 0x009E6900 | FUN_009e6900 | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:10298 |
| 0x009E71B0 | FUN_009e71b0 | probable | src/fallout/ai/movement/detailedactorpathhandler_o2_variant_od_oy_noo2_variant.cpp:568 |
| 0x009E9DC0 | FUN_009e9dc0 | class | src/fallout/ai/movement/playermover.cpp:308 |
| 0x009E9DE0 | FUN_009e9de0 | class | src/fallout/ai/movement/playermover.cpp:297 |
| 0x009EAD60 | FUN_009ead60 | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:774 |
| 0x009EB420 | FUN_009eb420 | unnamed | src/fallout/ai/playercharacter.cpp:68383 |
| 0x009EBA00 | FUN_009eba00 | unnamed | src/fallout/ai/alarmpackage.cpp:87 |
| 0x009EBA30 | FUN_009eba30 | unnamed | src/fallout/ai/alarmpackage.cpp:275 |
| 0x009EC850 | FUN_009ec850 | unnamed | src/fallout/ai/alarmpackage.cpp:177 |
| 0x009EC890 | FUN_009ec890 | class | src/fallout/ai/alarmpackage.cpp:535 |
| 0x009EC990 | FUN_009ec990 | class | src/fallout/ai/alarmpackage.cpp:1647 |
| 0x009ED5F0 | FUN_009ed5f0 | class | src/fallout/ai/backuppackage.cpp:286 |
| 0x009EE040 | FUN_009ee040 | unnamed | src/fallout/ai/dialoguepackage.cpp:12 |
| 0x009EF530 | FUN_009ef530 | unnamed | src/fallout/ai/dialoguepackage.cpp:160 |
| 0x009F0A80 | FUN_009f0a80 | unnamed | src/fallout/ai/escortpackage.cpp:180 |
| 0x009F1140 | FUN_009f1140 | probable | src/fallout/ai/fleepackage.cpp:769 |
| 0x009F1990 | FUN_009f1990 | unnamed | src/fallout/ai/fleepackage.cpp:38 |
| 0x009F3E20 | FUN_009f3e20 | unnamed | src/fallout/ai/sandboxpackage.cpp:1099 |
| 0x009F41C0 | FUN_009f41c0 | unnamed | src/fallout/ai/sandboxpackage.cpp:478 |
| 0x009F41F0 | FUN_009f41f0 | unnamed | src/fallout/ai/sandboxpackage.cpp:2163 |
| 0x009F4620 | FUN_009f4620 | unnamed | src/fallout/ai/sandboxpackage.cpp:1019 |
| 0x009F6190 | FUN_009f6190 | unnamed | src/fallout/ai/sandboxpackage.cpp:1065 |
| 0x009F63A0 | FUN_009f63a0 | unnamed | src/fallout/ai/sandboxpackage.cpp:1133 |
| 0x009F7050 | FUN_009f7050 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:18 |
| 0x009F7080 | FUN_009f7080 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:38 |
| 0x009F7F20 | FUN_009f7f20 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:2481 |
| 0x009F8300 | FUN_009f8300 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:126 |
| 0x009F84D0 | FUN_009f84d0 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:404 |
| 0x009F8570 | FUN_009f8570 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:2528 |
| 0x009F8660 | FUN_009f8660 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:431 |
| 0x009F8A80 | FUN_009f8a80 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:567 |
| 0x009F8AA0 | FUN_009f8aa0 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:173 |
| 0x009F8AC0 | FUN_009f8ac0 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:183 |
| 0x009F8C70 | FUN_009f8c70 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:1627 |
| 0x009F8D00 | FUN_009f8d00 | unnamed | src/fallout/ai/spectatorpackage_od_variant.cpp:240 |
| 0x009F8D60 | FUN_009f8d60 | class | src/fallout/ai/spectatorpackage_od_variant.cpp:262 |
| 0x009F8E80 | FUN_009f8e80_cls | decomp | src/fallout/ai/spectatorpackage_od_variant.cpp:1671 |
| 0x009F94D0 | FUN_009f94d0 | unnamed | src/fallout/ai/highprocess.cpp:6598 |
| 0x009F9500 | FUN_009f9500 | class | src/fallout/ai/trespasspackage.cpp:151 |
| 0x00ACB7E0 | FUN_00acb7e0 | unnamed | src/fallout/ai/baseprocess.cpp:772 |
| 0x00C59A50 | FUN_00c59a50 | unnamed | src/fallout/ai/actor_ob1_variant.cpp:174 |
| 0x00C69FC0 | FUN_00c69fc0 | unnamed | src/fallout/ai/middlehighprocess_o2_variant.cpp:36 |
| 0x00C6A0B0 | FUN_00c6a0b0 | probable | src/fallout/ai/combat/missileprojectile_o2_variant.cpp:593 |
| 0x00C6A200 | FUN_00c6a200 | unnamed | src/fallout/ai/actor_o2_variant.cpp:724 |
| 0x00C6A350 | FUN_00c6a350 | probable | src/fallout/ai/creature_o2_variant.cpp:85 |
| 0x00C6F500 | FUN_00c6f500 | unnamed | src/fallout/ai/playercharacter_o2_variant_rtm_variant.cpp:1015 |
| 0x00C6FD20 | FUN_00c6fd20 | class | src/fallout/ai/playercharacter_o2_variant.cpp:13 |
| 0x00C6FFC0 | FUN_00c6ffc0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:265 |
| 0x00C74DD0 | FUN_00c74dd0 | unnamed | src/fallout/ai/actor_o2_nood_variant.cpp:1772 |
| 0x00C7BFD0 | FUN_00c7bfd0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1375 |
| 0x00C7D3B0 | FUN_00c7d3b0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:414 |
| 0x00C7D480 | FUN_00c7d480 | unnamed | src/fallout/ai/actor_o2_variant.cpp:872 |
| 0x00C7D520 | FUN_00c7d520 | unnamed | src/fallout/ai/actor_o2_variant.cpp:924 |
| 0x00C7D5C0 | FUN_00c7d5c0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:973 |
| 0x00C7D630 | FUN_00c7d630 | class | src/fallout/ai/actor_o2_variant.cpp:552 |
| 0x00C7D810 | FUN_00c7d810 | unnamed | src/fallout/ai/actor_o2_variant.cpp:622 |
| 0x00C7D890 | FUN_00c7d890 | unnamed | src/fallout/ai/actor_o2_variant.cpp:659 |
| 0x00C7F4A0 | FUN_00c7f4a0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:2402 |
| 0x00C7F900 | FUN_00c7f900 | unnamed | src/fallout/ai/actor_o2_variant.cpp:677 |
| 0x00C7F970 | FUN_00c7f970 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1319 |
| 0x00C7FA90 | FUN_00c7fa90 | probable | src/fallout/ai/actor_o2_variant.cpp:2506 |
| 0x00C812D0 | FUN_00c812d0 | unnamed | src/fallout/ai/creature_o2_variant.cpp:45 |
| 0x00C821B0 | FUN_00c821b0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:3279 |
| 0x00C9BDF0 | FUN_00c9bdf0 | probable | src/fallout/ai/actor_o2_variant.cpp:1276 |
| 0x00CB9650 | FUN_00cb9650 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1445 |
| 0x00CBD500 | FUN_00cbd500 | unnamed | src/fallout/ai/combat/explosion_o2_nood_variant.cpp:2306 |
| 0x00CDA110 | FUN_00cda110 | unnamed | src/fallout/ai/actor_o2_variant.cpp:3114 |
| 0x00CDA4B0 | FUN_00cda4b0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:77 |
| 0x00CDA8D0 | FUN_00cda8d0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:90 |
| 0x00CDB3E0 | FUN_00cdb3e0 | unnamed | src/fallout/ai/actor_o2_variant.cpp:703 |
| 0x00CE4360 | FUN_00ce4360 | unnamed | src/fallout/ai/actor_o2_variant.cpp:1145 |
| 0x009C3F90 | GenerateSpherePoints | decomp | src/fallout/ai/combat/projectile.cpp:4061 |
| 0x005E3FC0 | Get | decomp | src/fallout/ai/actor.cpp:312 |
| 0x009A82B0 | GetAdjustedPosition | decomp | src/fallout/ai/combat/combatutilities.cpp:2772 |
| 0x008BD7B0 | GetAdjustedValue | class | src/fallout/ai/actor.cpp:88159 |
| 0x0080F790 | GetAngleZOnReference | class | src/fallout/ai/mobileobject.cpp:1653 |
| 0x009BA4D0 | GetArg1Ptr | class | src/fallout/ai/combat/missileprojectile.cpp:21 |
| 0x0098DE60 | GetArrayItem | decomp | src/fallout/ai/combat/combatgroup.cpp:252 |
| 0x008BBD90 | GetArrFlags | decomp | src/fallout/ai/actor.cpp:40691 |
| 0x00990A60 | GetArrFlags | decomp | src/fallout/ai/combat/combatgroupstrategy.cpp:33 |
| 0x0097D110 | GetAt | decomp | src/fallout/ai/combat/combatactions.cpp:373 |
| 0x0092B9C0 | GetAtOffset1DC | class | src/fallout/ai/middlehighprocess.cpp:13485 |
| 0x009DA570 | GetAvoidRadius | decomp | src/fallout/ai/combat/combatproceduresearch.cpp:101 |
| 0x008F9120 | GetByte15 | decomp | src/fallout/ai/highprocess.cpp:6132 |
| 0x0092B440 | GetByte5 | decomp | src/fallout/ai/middlehighprocess.cpp:3229 |
| 0x0097B960 | GetByte76 | decomp | src/fallout/ai/combat/combatactions.cpp:502 |
| 0x00886B10 | GetByteAt146 | decomp | src/fallout/ai/actor.cpp:4029 |
| 0x0089F540 | GetByteAt18A | decomp | src/fallout/ai/actor.cpp:33247 |
| 0x0088D2D0 | GetByteAt1991 | decomp | src/fallout/ai/actor.cpp:33052 |
| 0x008D83A0 | GetByteAt1D8 | class | src/fallout/ai/highprocess.cpp:11571 |
| 0x0089D670 | GetByteAt28D | decomp | src/fallout/ai/actor.cpp:33190 |
| 0x0089D690 | GetByteAt28E | probable | src/fallout/ai/actor.cpp:33201 |
| 0x008BBBD0 | GetByteAt650 | decomp | src/fallout/ai/actor.cpp:33419 |
| 0x008B6220 | GetByteAt78 | decomp | src/fallout/ai/actor.cpp:34417 |
| 0x009EF510 | GetByteAtBC | decomp | src/fallout/ai/dialoguepackage.cpp:96 |
| 0x008D8660 | GetByteAtE0 | class | src/fallout/ai/highprocess.cpp:4583 |
| 0x00973A90 | GetByteAtOffset | decomp | src/fallout/ai/processlists.cpp:2480 |
| 0x009B73B0 | GetByteAtOffset | probable | src/fallout/ai/combat/hitdata.cpp:22 |
| 0x008B3C90 | GetByteAtOffset114 | probable | src/fallout/ai/actor.cpp:34371 |
| 0x00987800 | GetByteAtOffset154 | decomp | src/fallout/ai/combat/combatgroup.cpp:113 |
| 0x00824060 | GetByteAtOffset17 | decomp | src/fallout/ai/highprocess.cpp:3834 |
| 0x008D44B0 | GetByteAtOffset1B4 | class | src/fallout/ai/creature.cpp:92 |
| 0x008D1E70 | GetByteAtOffset1C0 | class | src/fallout/ai/character.cpp:6 |
| 0x008BD5C0 | GetByteAtOffset43 | decomp | src/fallout/ai/actor.cpp:14381 |
| 0x0087EA20 | GetByteAtOffset66 | decomp | src/fallout/ai/actor.cpp:32857 |
| 0x0097F2F0 | GetByteAtOffset70 | decomp | src/fallout/ai/actor.cpp:17210 |
| 0x009E20A0 | GetByteAtOffset9F | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:5029 |
| 0x009CF400 | GetByteAtOffsetAD | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:47 |
| 0x008A3BD0 | GetByteAtOffsetB2 | decomp | src/fallout/ai/actor.cpp:34079 |
| 0x0087EED0 | GetByteAtOffsetBE | decomp | src/fallout/ai/actor.cpp:441 |
| 0x009989F0 | GetByteAtOffsetC7 | decomp | src/fallout/ai/combat/combatstate.cpp:217 |
| 0x008F9100 | GetByteAtOffsetE | decomp | src/fallout/ai/highprocess.cpp:6105 |
| 0x00990500 | GetCachedValue | decomp | src/fallout/ai/combat/combatgroup.cpp:1345 |
| 0x009145C0 | GetControllerPhase | class | src/fallout/ai/middlehighprocess.cpp:3617 |
| 0x004B13C0 | GetDirectionAngle | decomp | src/fallout/ai/actor.cpp:33643 |
| 0x00644660 | GetE0 | decomp | src/fallout/ai/combat/projectile.cpp:852 |
| 0x008AC810 | GetEffectCastSound | class | src/fallout/ai/actor.cpp:9125 |
| 0x008BBD60 | GetElementAsUInt | decomp | src/fallout/ai/actor.cpp:40667 |
| 0x00980720 | GetEntryAt | decomp | src/fallout/ai/combatcontroller.cpp:537 |
| 0x00567F00 | GetExtraDataObject3D | class | src/fallout/ai/actor.cpp:33678 |
| 0x008A8170 | GetExtraDataVersion | decomp | src/fallout/ai/actor.cpp:8833 |
| 0x008B6240 | GetField0xA8 | decomp | src/fallout/ai/actor.cpp:33393 |
| 0x008F9140 | GetField14 | decomp | src/fallout/ai/highprocess.cpp:6154 |
| 0x005F9B50 | GetField158 | class | src/fallout/ai/actor.cpp:331 |
| 0x009B7040 | GetField168 | decomp | src/fallout/ai/combat/hitdata.cpp:11 |
| 0x00645C40 | GetField174Float | class | src/fallout/ai/highprocess.cpp:4345 |
| 0x00978400 | GetField18Byte | decomp | src/fallout/ai/processlists.cpp:2486 |
| 0x00778970 | GetField18C | decomp | src/fallout/ai/actor.cpp:360 |
| 0x008D8940 | GetField1A4 | decomp | src/fallout/ai/actor.cpp:34691 |
| 0x008D8160 | GetField1BC | class | src/fallout/ai/highprocess.cpp:4469 |
| 0x008D1EB0 | GetField1C4 | class | src/fallout/ai/actor.cpp:34680 |
| 0x00905230 | GetField1FC | decomp | src/fallout/ai/highprocess.cpp:6540 |
| 0x008D8A60 | GetField244 | class | src/fallout/ai/highprocess.cpp:4662 |
| 0x0089D6D0 | GetField298 | decomp | src/fallout/ai/actor.cpp:33224 |
| 0x008BB5A0 | GetField2AC | decomp | src/fallout/ai/actor.cpp:13464 |
| 0x008C4830 | GetField2B0 | decomp | src/fallout/ai/actor.cpp:16399 |
| 0x008D8F50 | GetField310 | class | src/fallout/ai/highprocess.cpp:4793 |
| 0x009E32D0 | GetField38 | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:178 |
| 0x008D8C80 | GetField39C | class | src/fallout/ai/highprocess.cpp:4717 |
| 0x008AFEF0 | GetField3A8 | decomp | src/fallout/ai/actor.cpp:33318 |
| 0x00900E60 | GetField3AC | class | src/fallout/ai/highprocess.cpp:6228 |
| 0x00900EA0 | GetField3B0 | class | src/fallout/ai/highprocess.cpp:6239 |
| 0x008D9590 | GetField3BC | class | src/fallout/ai/highprocess.cpp:4871 |
| 0x008BCDD0 | GetField3EC | decomp | src/fallout/ai/actor.cpp:14346 |
| 0x00885490 | GetField42C | decomp | src/fallout/ai/actor.cpp:3773 |
| 0x00904430 | GetField440 | decomp | src/fallout/ai/highprocess.cpp:6529 |
| 0x0088B0F0 | GetField548 | decomp | src/fallout/ai/actor.cpp:33983 |
| 0x008D93B0 | GetFieldAt38C | class | src/fallout/ai/highprocess.cpp:13803 |
| 0x0088B130 | GetFieldAt570 | decomp | src/fallout/ai/actor.cpp:33040 |
| 0x0097AE90 | GetFieldBC | decomp | src/fallout/ai/combat/combatactions.cpp:268 |
| 0x00998A10 | GetFieldC5 | decomp | src/fallout/ai/combat/combatstate.cpp:229 |
| 0x0092F140 | GetFieldD2C | decomp | src/fallout/ai/mobileobject.cpp:1164 |
| 0x009396A0 | GetFieldD44 | class | src/fallout/ai/actor.cpp:34743 |
| 0x00885D70 | GetFieldDC | decomp | src/fallout/ai/actor.cpp:33891 |
| 0x009D8D20 | GetFieldEC | decomp | src/fallout/ai/actor.cpp:34831 |
| 0x0097B050 | GetFieldValue | decomp | src/fallout/ai/combat/combatactions.cpp:362 |
| 0x0089D6B0 | GetFileValueAt668 | decomp | src/fallout/ai/actor.cpp:33213 |
| 0x008BCA70 | GetFlag | probable | src/fallout/ai/actor.cpp:40803 |
| 0x008E9620 | GetFlag | decomp | src/fallout/ai/highprocess.cpp:5305 |
| 0x009877C0 | GetFlagsFromSubobject | decomp | src/fallout/ai/combat/combatgroup.cpp:86 |
| 0x009F4640 | GetFlagsMappedValue | decomp | src/fallout/ai/sandboxpackage.cpp:970 |
| 0x009003E0 | GetFloatAt | decomp | src/fallout/ai/highprocess.cpp:4109 |
| 0x009E2830 | GetFloatValue | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:5111 |
| 0x008B6200 | GetFlt | decomp | src/fallout/ai/actor.cpp:40254 |
| 0x008D8460 | GetFormList | class | src/fallout/ai/highprocess.cpp:4548 |
| 0x008BE3C0 | GetHolderValue | decomp | src/fallout/ai/actor.cpp:88330 |
| 0x009A0BE0 | GetIdleAdjustedValue | decomp | src/fallout/ai/combat/combatstate.cpp:1166 |
| 0x009A0B70 | GetInterpolatedValue | decomp | src/fallout/ai/combat/combatstate.cpp:1993 |
| 0x009016A0 | GetKindName | class | src/fallout/ai/highprocess.cpp:68951 |
| 0x009B3DA0 | GetMaxParticleGlobalValue | decomp | src/fallout/ai/combat/flameprojectile.cpp:196 |
| 0x009E8670 | GetMethod | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:5161 |
| 0x0098CB30 | GetModifierSum | probable | src/fallout/ai/combat/combatgroup.cpp:5448 |
| 0x009074F0 | GetModifierValue | class | src/fallout/ai/lowprocess.cpp:3418 |
| 0x008D02D0 | GetNegativeGlobal | class | src/fallout/ai/baseprocess.cpp:204 |
| 0x008D1E50 | GetNextObjectFloat | class | src/fallout/ai/actor.cpp:16426 |
| 0x009E3A70 | GetNextPathPoint | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:4882 |
| 0x009EB160 | GetNextPathPoint | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:1107 |
| 0x0087D600 | GetNiPoint3 | decomp | src/fallout/ai/actor.cpp:32804 |
| 0x008D1610 | GetNiRTTI | class | src/fallout/ai/bsplayerdistancecheckcontroller.cpp:16 |
| 0x008B6800 | GetObjectFlags | decomp | src/fallout/ai/actor.cpp:10885 |
| 0x006D33C0 | GetObjectPosition | decomp | src/fallout/ai/sandboxpackage.cpp:1257 |
| 0x00939820 | GetOffset190 | decomp | src/fallout/ai/playercharacter.cpp:2185 |
| 0x00978F30 | GetOne | decomp | src/fallout/ai/actor.cpp:33562 |
| 0x00983420 | GetOrCreateCoverItem | decomp | src/fallout/ai/combat/combatcovermap.cpp:256 |
| 0x008BD550 | GetOriginalRuntimeFloatSetting37 | decomp | src/fallout/ai/actor.cpp:14358 |
| 0x009E3B60 | GetPairByIndex | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:6455 |
| 0x009A8AF0 | GetPitchYaw | decomp | src/fallout/ai/combat/combatutilities.cpp:4179 |
| 0x00CDB290 | GetPlus4 | decomp | src/fallout/ai/actor_o2_variant.cpp:102 |
| 0x009EB230 | GetPointAtIndex | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:1325 |
| 0x009EBAB0 | GetRaceListSize | decomp | src/fallout/ai/alarmpackage.cpp:106 |
| 0x009D3310 | GetRandomFloat | decomp | src/fallout/ai/combat/combatprocedurebeincover.cpp:132 |
| 0x009F19F0 | GetSaveSize | class | src/fallout/ai/fleepackage.cpp:932 |
| 0x009A0B30 | GetScaledValue | decomp | src/fallout/ai/combat/combatstate.cpp:1133 |
| 0x009A7FA0 | GetScaleOrHeightDelta | decomp | src/fallout/ai/combat/combatutilities.cpp:2535 |
| 0x008F21D0 | GetShortAtOffset12 | decomp | src/fallout/ai/highprocess.cpp:4059 |
| 0x008F9160 | GetShortAtOffset16 | decomp | src/fallout/ai/highprocess.cpp:6165 |
| 0x00963BA0 | GetSlotPointer | class | src/fallout/ai/playercharacter.cpp:44941 |
| 0x009D1B10 | GetTarget | probable | src/fallout/ai/combat/combatprocedure.cpp:44 |
| 0x009A8600 | GetTargetLocationWithOffset | decomp | src/fallout/ai/combat/combatutilities.cpp:238 |
| 0x008B0D70 | GetTargetValue | decomp | src/fallout/ai/actor.cpp:75736 |
| 0x00934F90 | GetTempRefOrSelf | class | src/fallout/ai/mobileobject.cpp:1620 |
| 0x008D85E0 | GetUnk15C | class | src/fallout/ai/highprocess.cpp:11941 |
| 0x008B4380 | GetUnk66 | decomp | src/fallout/ai/actor.cpp:34406 |
| 0x00812870 | GetUnka4 | class | src/fallout/ai/highprocess.cpp:11429 |
| 0x009DA550 | GetValue | decomp | src/fallout/ai/combat/combatproceduresearch.cpp:370 |
| 0x009E3970 | GetValue | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:4854 |
| 0x009D1D30 | GetVec3 | class | src/fallout/ai/combat/combatprocedureattackranged.cpp:683 |
| 0x008846E0 | GetVtbl20Result | probable | src/fallout/ai/actor.cpp:3181 |
| 0x00885560 | GetWaterDepthAtPoint | decomp | src/fallout/ai/actor.cpp:3823 |
| 0x0097AC30 | GetWeaponDPSDeficit | decomp | src/fallout/ai/combat/combataction.cpp:284 |
| 0x00905DC0 | HandleStateChange | class | src/fallout/ai/lipsyncbackgroundmanager.cpp:71 |
| 0x00963CE0 | HasAction | decomp | src/fallout/ai/playercharacter.cpp:45405 |
| 0x008BA4A0 | HasAnyFlag | decomp | src/fallout/ai/actor.cpp:84147 |
| 0x008D87C0 | HasFlag | class | src/fallout/ai/highprocess.cpp:12296 |
| 0x00930570 | HasFlag40000 | decomp | src/fallout/ai/mobileobject.cpp:1183 |
| 0x009A0F40 | HasItemWithinRadius | decomp | src/fallout/ai/combat/combatstate.cpp:3357 |
| 0x0056F6B0 | HasNextWithAtA0 | class | src/fallout/ai/mobileobject.cpp:1420 |
| 0x009040F0 | HasReference | class | src/fallout/ai/highprocess.cpp:10271 |
| 0x008E5700 | HasString | decomp | src/fallout/ai/highprocess.cpp:4004 |
| 0x0089F560 | IncrementCount | decomp | src/fallout/ai/actor.cpp:34068 |
| 0x00902C60 | IncrementLockCount | decomp | src/fallout/ai/highprocess.cpp:6482 |
| 0x009E5AB0 | Init | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:4946 |
| 0x0092B830 | InitBodyPartNodes | class | src/fallout/ai/middlehighprocess.cpp:2479 |
| 0x0087F800 | InitCellOrWorldSpace | decomp | src/fallout/ai/actor.cpp:916 |
| 0x008D1820 | InitializeCameraShake | decomp | src/fallout/ai/camerashake.cpp:6 |
| 0x009F8A10 | InitLoadGame | class | src/fallout/ai/spectatorpackage_od_variant.cpp:458 |
| 0x009B40D0 | InitProjectileFlags | class | src/fallout/ai/combat/grenadeprojectile.cpp:758 |
| 0x009C4EC0 | InitSoundFromArchetype | probable | src/fallout/ai/combat/projectile.cpp:2328 |
| 0x00905C50 | InitTerrainManager | class | src/fallout/ai/lipsyncbackgroundmanager.cpp:784 |
| 0x00900780 | InvalidateValue | class | src/fallout/ai/highprocess.cpp:10073 |
| 0x008B42E0 | InvertTransform | decomp | src/fallout/ai/actor.cpp:10868 |
| 0x009AFCA0 | InvokeCallback | class | src/fallout/ai/combat/explosion.cpp:1168 |
| 0x008C4CB0 | InvokeTailIfLookupValid | decomp | src/fallout/ai/actor.cpp:90621 |
| 0x009358F0 | InvokeTarget | class | src/fallout/ai/mobileobject.cpp:3028 |
| 0x00900000 | IsAlwaysFalse | class | src/fallout/ai/highprocess.cpp:21996 |
| 0x009A9800 | IsBitSetOrNeighbor | decomp | src/fallout/ai/combat/combatutilities.cpp:308 |
| 0x008A67D0 | IsEmpty | decomp | src/fallout/ai/actor.cpp:33274 |
| 0x009A9720 | IsExplosionRadiusValid | decomp | src/fallout/ai/combat/combatutilities.cpp:290 |
| 0x0097E310 | IsField8One | decomp | src/fallout/ai/combatcontroller.cpp:315 |
| 0x008B7D00 | IsFlag100Set | probable | src/fallout/ai/actor.cpp:34442 |
| 0x009F5690 | IsFlag20Clear | decomp | src/fallout/ai/sandboxpackage.cpp:1440 |
| 0x009F4600 | IsFlag2Clear | decomp | src/fallout/ai/sandboxpackage.cpp:1418 |
| 0x008E3120 | IsFlag400Set | decomp | src/fallout/ai/highprocess.cpp:5287 |
| 0x008E7C00 | IsFlag40Set | probable | src/fallout/ai/highprocess.cpp:4023 |
| 0x00981320 | IsFlag4Set | decomp | src/fallout/ai/combatcontroller.cpp:591 |
| 0x009F54B0 | IsFlag8Clear | decomp | src/fallout/ai/sandboxpackage.cpp:1051 |
| 0x009F45E0 | IsFlagBit0Clear | probable | src/fallout/ai/sandboxpackage.cpp:1009 |
| 0x008840D0 | IsFlagBitSet | decomp | src/fallout/ai/actor.cpp:2082 |
| 0x00967700 | IsFlagged | decomp | src/fallout/ai/playercharacter.cpp:51233 |
| 0x009AAD40 | IsFlagSet | decomp | src/fallout/ai/combat/combatworldstate.cpp:53 |
| 0x009D7BD0 | IsFlagSet | decomp | src/fallout/ai/combat/combatproceduremove.cpp:27 |
| 0x009871E0 | IsModifierZero | decomp | src/fallout/ai/combat/combatgroup.cpp:70 |
| 0x009990C0 | IsNegative | decomp | src/fallout/ai/combat/combatstate.cpp:716 |
| 0x008BA530 | IsNodeKindSupported | decomp | src/fallout/ai/actor.cpp:84386 |
| 0x009E3110 | IsPathReachableToPlayer | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:4770 |
| 0x009EDD30 | IsPointerMatch | class | src/fallout/ai/dialoguepackage.cpp:85 |
| 0x009E3990 | IsPointValid | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:5127 |
| 0x009EC810 | IsSpellInList | decomp | src/fallout/ai/alarmpackage.cpp:140 |
| 0x004A4040 | IsStartMenuFlag1Set | probable | src/fallout/ai/playercharacter.cpp:1321 |
| 0x009A6AE0 | IsTargetInCone | decomp | src/fallout/ai/combat/combatutilities.cpp:2202 |
| 0x009A6D70 | IsWithinAimLimits | decomp | src/fallout/ai/combat/combatutilities.cpp:2272 |
| 0x0087F660 | IsWithinProcThreshold | decomp | src/fallout/ai/actor.cpp:48139 |
| 0x009CEFD0 | IsWithinThreshold | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:659 |
| 0x00497C10 | LoadAnimationData | decomp | src/fallout/ai/combat/combatthreatmap.cpp:155 |
| 0x004D52D0 | LoadBGSTerrainManager | decomp | src/fallout/ai/dialoguepackage.cpp:6 |
| 0x009C5740 | LoadForm | class | src/fallout/ai/combat/projectile.cpp:9331 |
| 0x009A2C60 | LoadFormData | decomp | src/fallout/ai/combat/combatstate.cpp:1361 |
| 0x0092EA30 | LoadFromStream | class | src/fallout/ai/middlelowprocess.cpp:1012 |
| 0x008D7420 | LoadGame | probable | src/fallout/ai/highprocess.cpp:10169 |
| 0x009379C0 | LoadModifiers | probable | src/fallout/ai/modifierlist.cpp:287 |
| 0x009ABE40 | MarkGeometryDataMutable | probable | src/fallout/ai/combat/continuousbeamprojectile.cpp:244 |
| 0x00974960 | MarkNodeIfCheckFails | decomp | src/fallout/ai/processlists.cpp:3100 |
| 0x00563200 | MaskWithField | probable | src/fallout/ai/combat/projectile.cpp:840 |
| 0x008F3FE0 | Method | decomp | src/fallout/ai/highprocess.cpp:5351 |
| 0x008A8420 | PlayReloadAnimation | class | src/fallout/ai/actor.cpp:42986 |
| 0x00933150 | PlaySoundByFormID | decomp | src/fallout/ai/mobileobject.cpp:4843 |
| 0x009DABD0 | PrintDebugInfo | class | src/fallout/ai/combat/combatprocedureusecombatitem.cpp:215 |
| 0x009EB2B0 | PrintPathDebugInfo | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:1285 |
| 0x00703C00 | PrintToConsole | proven | src/fallout/ai/processlists.cpp:4587 |
| 0x00576470 | ProbeAndApplyHeight | class | src/fallout/ai/mobileobject.cpp:7539 |
| 0x0097F820 | ProcessActivation | decomp | src/fallout/ai/combatcontroller.cpp:1858 |
| 0x009A5CD0 | ProcessAllProjectiles | decomp | src/fallout/ai/combat/combatthreatmap.cpp:75 |
| 0x008C81C0 | ProcessMessage | decomp | src/fallout/ai/aitaskmanager.cpp:1323 |
| 0x00921250 | ProcessNode | probable | src/fallout/ai/middlehighprocess.cpp:9321 |
| 0x008A05F0 | ProcessResponse | class | src/fallout/ai/actor.cpp:44850 |
| 0x009006A0 | ProcessSpawnedObject | class | src/fallout/ai/highprocess.cpp:23242 |
| 0x008C88B0 | QueryPerformanceCounters | class | src/fallout/ai/aitaskmanager.cpp:209 |
| 0x0092BFF0 | QueueDeferredHideLimb | class | src/fallout/ai/middlehighprocess.cpp:13856 |
| 0x009B7840 | RaiseMaxValue | decomp | src/fallout/ai/combat/hitdata.cpp:34 |
| 0x008E3DC0 | RandomOffsetVectorFromOrigin | decomp | src/fallout/ai/highprocess.cpp:16905 |
| 0x009F8D90 | Reallocate | class | src/fallout/ai/spectatorpackage_od_variant.cpp:276 |
| 0x00963A50 | RegisterObject | class | src/fallout/ai/playercharacter.cpp:44304 |
| 0x009A0470 | ReleaseStageHolder | probable | src/fallout/ai/combat/combatstate.cpp:3068 |
| 0x009C9E90 | RemoveCommandsForTarget | decomp | src/fallout/ai/combat/vats.cpp:534 |
| 0x00963BF0 | RemoveExpiredItems | decomp | src/fallout/ai/playercharacter.cpp:45362 |
| 0x00904220 | RemoveItemByID | class | src/fallout/ai/highprocess.cpp:55019 |
| 0x00963900 | RemovePerk | class | src/fallout/ai/playercharacter.cpp:44206 |
| 0x009F2C30 | RemoveReference | class | src/fallout/ai/patrolpackage.cpp:1059 |
| 0x009CFF10 | Reset | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:467 |
| 0x009E68C0 | Reset | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:5146 |
| 0x0097EF50 | ResetModifierIfActive | probable | src/fallout/ai/combatcontroller.cpp:1728 |
| 0x00964190 | ResetMover | class | src/fallout/ai/actor.cpp:17200 |
| 0x009E5480 | ResetPathState | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:233 |
| 0x009F4060 | ResetReference | decomp | src/fallout/ai/sandboxpackage.cpp:946 |
| 0x00902680 | ResetValue | probable | src/fallout/ai/highprocess.cpp:6456 |
| 0x00920B80 | ResetWeaponState | class | src/fallout/ai/middlehighprocess.cpp:23615 |
| 0x008D34F0 | RevertAndResetFields | class | src/fallout/ai/character.cpp:31 |
| 0x009DA6C0 | RevertAndResolveRef | class | src/fallout/ai/combat/combatproceduresearch.cpp:199 |
| 0x00923E40 | RunScheduledAction | class | src/fallout/ai/middlehighprocess.cpp:10307 |
| 0x008EE220 | RunScriptCommand | class | src/fallout/ai/highprocess.cpp:41740 |
| 0x008C9C70 | RunTaskletLoop | class | src/fallout/ai/aitaskmanager.cpp:1571 |
| 0x009F2380 | SaveExtraData | class | src/fallout/ai/fleepackage.cpp:1010 |
| 0x008D33A0 | SaveFormData | class | src/fallout/ai/character.cpp:288 |
| 0x009F0BB0 | SaveFormList | class | src/fallout/ai/escortpackage.cpp:233 |
| 0x009F9570 | SaveFormRefs | class | src/fallout/ai/trespasspackage.cpp:199 |
| 0x008D7270 | SaveGame | decomp | src/fallout/ai/highprocess.cpp:10098 |
| 0x00932070 | SaveProcess | class | src/fallout/ai/mobileobject.cpp:12349 |
| 0x00996ED0 | SaveToBuffer | class | src/fallout/ai/combat/combatprocedure.cpp:82 |
| 0x009F2850 | SaveToBuffer | class | src/fallout/ai/guardpackage.cpp:59 |
| 0x009F9790 | SaveToBuffer | class | src/fallout/ai/trespasspackage.cpp:129 |
| 0x009A99D0 | ScaleByRatio | decomp | src/fallout/ai/combat/combatutilities.cpp:69 |
| 0x009A99F0 | ScaleCharToFloat | decomp | src/fallout/ai/combat/combatutilities.cpp:32 |
| 0x0099E190 | SelectAndMoveToPoint | probable | src/fallout/ai/combat/combatstate.cpp:4497 |
| 0x009D6820 | Serialize | class | src/fallout/ai/combat/combatprocedurehidefromtarget.cpp:273 |
| 0x005F8BD0 | Set | class | src/fallout/ai/actor.cpp:325 |
| 0x008848C0 | set | probable | src/fallout/ai/actor.cpp:3209 |
| 0x0088B050 | Set | decomp | src/fallout/ai/actor.cpp:4484 |
| 0x0088B0A0 | set | probable | src/fallout/ai/actor.cpp:4517 |
| 0x0088B110 | Set | decomp | src/fallout/ai/actor.cpp:4530 |
| 0x008A3BF0 | Set | decomp | src/fallout/ai/actor.cpp:6325 |
| 0x008BD570 | set | decomp | src/fallout/ai/actor.cpp:14371 |
| 0x008BF4E0 | set | decomp | src/fallout/ai/actor.cpp:14936 |
| 0x00994EF0 | Set | decomp | src/fallout/ai/actor.cpp:17223 |
| 0x008BD630 | SetAlphaRecursive | probable | src/fallout/ai/actor.cpp:45464 |
| 0x0097F450 | SetAttacker | probable | src/fallout/ai/combat/combatprocedure.cpp:13 |
| 0x00906F80 | SetBits | decomp | src/fallout/ai/lowprocess.cpp:3405 |
| 0x008D8560 | SetByte13C | class | src/fallout/ai/highprocess.cpp:11727 |
| 0x008D91C0 | SetByte3B9 | class | src/fallout/ai/highprocess.cpp:13297 |
| 0x0096CC80 | SetByte50 | decomp | src/fallout/ai/processlists.cpp:2468 |
| 0x009D0A10 | SetByteAt142 | decomp | src/fallout/ai/combat/combatprocedureattackranged.cpp:44 |
| 0x008D8700 | SetByteAt18D | class | src/fallout/ai/highprocess.cpp:12185 |
| 0x009315A0 | SetByteAt241 | decomp | src/fallout/ai/actor.cpp:40960 |
| 0x00887B70 | SetByteAt5C | decomp | src/fallout/ai/actor.cpp:32992 |
| 0x00973A70 | SetByteAt66c | decomp | src/fallout/ai/processlists.cpp:3030 |
| 0x009C9900 | SetByteAt76 | decomp | src/fallout/ai/combat/vats.cpp:210 |
| 0x008B2880 | SetByteAtOffset | decomp | src/fallout/ai/actor.cpp:33347 |
| 0x00983400 | SetByteAtOffset | decomp | src/fallout/ai/combat/combatcovermap.cpp:28 |
| 0x009D4F30 | SetByteAtOffset188ToFF | decomp | src/fallout/ai/combat/combatprocedure.cpp:55 |
| 0x00953FD0 | SetByteAtOffset6E8 | class | src/fallout/ai/actor.cpp:33551 |
| 0x00931510 | SetByteAtOffset96 | decomp | src/fallout/ai/actor.cpp:33518 |
| 0x008AD8F0 | SetByteAtOffset9B | probable | src/fallout/ai/actor.cpp:33307 |
| 0x008982A0 | SetByteAtOffsetA8 | decomp | src/fallout/ai/actor.cpp:34033 |
| 0x008B2860 | SetByteAtOffsetBE | decomp | src/fallout/ai/actor.cpp:34205 |
| 0x008F6630 | SetByteAtOffsetC5 | decomp | src/fallout/ai/highprocess.cpp:5391 |
| 0x009D09F0 | SetByteAtOffsetC6 | decomp | src/fallout/ai/combat/combatprocedureattackranged.cpp:33 |
| 0x006546C0 | SetByteE0 | class | src/fallout/ai/highprocess.cpp:11376 |
| 0x008BD610 | SetCastDown | decomp | src/fallout/ai/actor.cpp:14433 |
| 0x00900E40 | SetCastingState | class | src/fallout/ai/highprocess.cpp:6217 |
| 0x009B5050 | SetContextInfo | decomp | src/fallout/ai/combat/hitdata.cpp:1330 |
| 0x008C7D80 | SetCurrent | decomp | src/fallout/ai/ailineartaskthreadmanager.cpp:450 |
| 0x008A80C0 | SetDismemberedLimbsFlag | decomp | src/fallout/ai/actor.cpp:45057 |
| 0x0098A390 | SetElementValue | probable | src/fallout/ai/combat/combatgroup.cpp:2407 |
| 0x008A8820 | SetField | decomp | src/fallout/ai/actor.cpp:39125 |
| 0x008E0AB0 | SetField | decomp | src/fallout/ai/highprocess.cpp:5238 |
| 0x009314F0 | SetField | decomp | src/fallout/ai/actor.cpp:33507 |
| 0x009C0050 | SetField | decomp | src/fallout/ai/combat/projectile.cpp:889 |
| 0x008C1AA0 | SetField11C | decomp | src/fallout/ai/actor.cpp:33439 |
| 0x00939800 | SetField18c | decomp | src/fallout/ai/actor.cpp:16919 |
| 0x009A0650 | SetField18C | decomp | src/fallout/ai/combat/combatstate.cpp:1092 |
| 0x00930600 | SetField558 | decomp | src/fallout/ai/mobileobject.cpp:1189 |
| 0x009396F0 | SetFieldD64 | class | src/fallout/ai/character.cpp:300 |
| 0x009A9F00 | SetFieldE0 | decomp | src/fallout/ai/combat/combatutilities.cpp:45 |
| 0x009D8D00 | SetFieldEC | decomp | src/fallout/ai/combat/combatproceduresearch.cpp:50 |
| 0x008D9450 | SetFinishing | class | src/fallout/ai/highprocess.cpp:4860 |
| 0x00898280 | SetFlag | decomp | src/fallout/ai/actor.cpp:34022 |
| 0x008B28A0 | SetFlag | decomp | src/fallout/ai/actor.cpp:34216 |
| 0x00922B60 | SetFlag | class | src/fallout/ai/middlehighprocess.cpp:3717 |
| 0x008D7EA0 | SetFlag16 | class | src/fallout/ai/highprocess.cpp:4405 |
| 0x00898200 | SetFlag2000000 | decomp | src/fallout/ai/actor.cpp:36833 |
| 0x00810F90 | SetFlag4000 | probable | src/fallout/ai/mobileobject.cpp:1222 |
| 0x008C1B50 | SetFlag40000000 | decomp | src/fallout/ai/actor.cpp:15545 |
| 0x008D9700 | SetFlag444 | class | src/fallout/ai/highprocess.cpp:4907 |
| 0x008DD880 | SetFlag6CC | decomp | src/fallout/ai/highprocess.cpp:3875 |
| 0x008A5CF0 | SetFlag86 | decomp | src/fallout/ai/actor.cpp:6565 |
| 0x009DEFF0 | SetFlagA3 | decomp | src/fallout/ai/movement/actormover.cpp:1173 |
| 0x0099B540 | SetFlags | decomp | src/fallout/ai/combat/combatstate.cpp:1889 |
| 0x0092C540 | SetHitData | class | src/fallout/ai/middlehighprocess.cpp:6697 |
| 0x008852B0 | SetInnerFloat | decomp | src/fallout/ai/actor.cpp:36204 |
| 0x009AAD20 | SetItem | decomp | src/fallout/ai/combat/combatworldstate.cpp:80 |
| 0x009375B0 | SetKeyAndValue | decomp | src/fallout/ai/modifierlist.cpp:135 |
| 0x009C9A50 | SetLight | decomp | src/fallout/ai/combat/vats.cpp:424 |
| 0x009E3360 | SetMode | class | src/fallout/ai/movement/detailedactorpathhandler.cpp:5308 |
| 0x009DDF60 | SetMoveModeFlags | class | src/fallout/ai/movement/actormover.cpp:481 |
| 0x008950F0 | SetMoveSpeed | probable | src/fallout/ai/actor.cpp:4945 |
| 0x009A0EC0 | SetNodeBlockAndTimestamp | decomp | src/fallout/ai/combat/combatstate.cpp:1268 |
| 0x008D8CD0 | SetNumberGuards | class | src/fallout/ai/highprocess.cpp:12592 |
| 0x00963790 | SetPerkRank | class | src/fallout/ai/playercharacter.cpp:44107 |
| 0x008ADC20 | SetPoint | decomp | src/fallout/ai/actor.cpp:39827 |
| 0x008BA210 | SetProcessFlagIfActive | decomp | src/fallout/ai/actor.cpp:83243 |
| 0x00932490 | SetProcessFlags | class | src/fallout/ai/mobileobject.cpp:2924 |
| 0x0088B850 | SetRefractionProperty | class | src/fallout/ai/actor_magic.cpp:557 |
| 0x008924E0 | SetRelationshipRank | decomp | src/fallout/ai/actor.cpp:34010 |
| 0x009E1640 | SetRotationMatrix | decomp | src/fallout/ai/movement/detailedactorpathhandler.cpp:130 |
| 0x0088B510 | SetScaledValue | probable | src/fallout/ai/actor.cpp:56733 |
| 0x008D8C40 | SetShortValue | class | src/fallout/ai/highprocess.cpp:4706 |
| 0x008D8380 | SetShotCount | class | src/fallout/ai/highprocess.cpp:4537 |
| 0x008E7C20 | SetTargetAngle | decomp | src/fallout/ai/highprocess.cpp:4030 |
| 0x008D7340 | SetTargetReference | probable | src/fallout/ai/highprocess.cpp:10115 |
| 0x008BFF30 | SetTlsInt | decomp | src/fallout/ai/actor.cpp:33427 |
| 0x008E7C50 | SetUseSoft | decomp | src/fallout/ai/highprocess.cpp:4042 |
| 0x008B0140 | SetVisibilityMask | decomp | src/fallout/ai/actor.cpp:9741 |
| 0x008AC890 | SetWaterForm | decomp | src/fallout/ai/actor.cpp:9167 |
| 0x008ACB70 | SetWeaponDPS | decomp | src/fallout/ai/actor.cpp:9209 |
| 0x008C9FB0 | SignalAtOffset30 | decomp | src/fallout/ai/aitaskmanager.cpp:647 |
| 0x008C79E0 | SignalThreadEvent | decomp | src/fallout/ai/ailineartaskthreadmanager.cpp:418 |
| 0x009D5B60 | StopAndEngageTarget | class | src/fallout/ai/combat/combatprocedureevade.cpp:104 |
| 0x009D2570 | StopAttackerAndEngageTarget | decomp | src/fallout/ai/combat/combatprocedurebeincover.cpp:190 |
| 0x009C4F90 | StopSound | probable | src/fallout/ai/combat/projectile.cpp:585 |
| 0x008D8990 | SubtractValue | class | src/fallout/ai/highprocess.cpp:4640 |
| 0x008CF8F0 | SwitchProcess | class | src/fallout/ai/mobileobject.cpp:9378 |
| 0x00961D90 | SyncFlaggedFloat | class | src/fallout/ai/actor.cpp:17163 |
| 0x009CF090 | TryAttackTarget | probable | src/fallout/ai/combat/combatprocedureattackmelee.cpp:6515 |
| 0x009E7610 | TurnTowardGoalAngle | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:851 |
| 0x008C1470 | UpdateAlchemyCastSound | decomp | src/fallout/ai/actor.cpp:15481 |
| 0x009B7CC0 | UpdateBeamFlags | class | src/fallout/ai/combat/missileprojectile.cpp:503 |
| 0x008D1B30 | UpdateCameraShake | decomp | src/fallout/ai/camerashake.cpp:160 |
| 0x008D1960 | UpdateDistanceFade | decomp | src/fallout/ai/camerashake.cpp:93 |
| 0x009D8C60 | UpdateEngageTarget | class | src/fallout/ai/combat/combatproceduresearch.cpp:233 |
| 0x00884990 | UpdateFlag800State | decomp | src/fallout/ai/actor.cpp:3296 |
| 0x009DC780 | UpdateFlagFromTarget | decomp | src/fallout/ai/movement/actormover.cpp:3427 |
| 0x00932520 | UpdateFlags | class | src/fallout/ai/mobileobject.cpp:3674 |
| 0x009D0530 | UpdateFlags | decomp | src/fallout/ai/combat/combatprocedureattackmelee.cpp:488 |
| 0x0092C120 | UpdateHideLimbNodes | class | src/fallout/ai/middlehighprocess.cpp:3420 |
| 0x0099ABC0 | UpdateLastSeenFiringLocation | decomp | src/fallout/ai/combat/combatstate.cpp:970 |
| 0x009A0C50 | UpdateModifierState | probable | src/fallout/ai/combat/combatstate.cpp:3183 |
| 0x00910C80 | UpdateMoveToTarget | class | src/fallout/ai/lowprocess.cpp:9001 |
| 0x00978890 | UpdateMuzzleFlashes | decomp | src/fallout/ai/processlists.cpp:1262 |
| 0x009BAF50 | UpdateNodePosition | decomp | src/fallout/ai/combat/muzzleflash.cpp:172 |
| 0x009DD2D0 | UpdatePathMovement | probable | src/fallout/ai/movement/actormover.cpp:4932 |
| 0x009EA8A0 | UpdatePathMovement | class | src/fallout/ai/movement/virtualactorpathhandler.cpp:603 |
| 0x009E3560 | UpdatePathRotation | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:2741 |
| 0x009E77D0 | UpdatePathTether | probable | src/fallout/ai/movement/detailedactorpathhandler.cpp:4132 |
| 0x00953D00 | UpdatePlayerStateIfActive | decomp | src/fallout/ai/playercharacter.cpp:32377 |
| 0x008D10C0 | UpdateProcessTiming | class | src/fallout/ai/baseprocess.cpp:761 |
| 0x0094FCE0 | UpdateSkyObject | class | src/fallout/ai/playercharacter.cpp:24546 |
| 0x0099A9A0 | UpdateStageHolders | probable | src/fallout/ai/combat/combatstate.cpp:910 |
| 0x00910250 | UpdateTargetRefs | class | src/fallout/ai/lowprocess.cpp:4928 |
| 0x00923020 | UpdateWeaponAnimation | class | src/fallout/ai/middlehighprocess.cpp:5767 |
| 0x00923960 | UpdateWeaponDrawnAnimation | probable | src/fallout/ai/middlehighprocess.cpp:6588 |
| 0x0091E780 | UpdateWeaponTypeFlags | probable | src/fallout/ai/middlehighprocess.cpp:4707 |
| 0x008C7A70 | WaitForEvent | probable | src/fallout/ai/ailineartaskthreadmanager.cpp:437 |
| 0x008C1210 | WalkListForTarget | decomp | src/fallout/ai/actor.cpp:89173 |
| 0x009CB890 | WriteDebugText | class | src/fallout/ai/combat/combatprocedureattackgrenade.cpp:1367 |
| 0x008C83A0 | ~FUN_008c83a0 | unnamed | src/fallout/ai/aitaskmanager.cpp:915 |
| 0x008C9EF0 | ~FUN_008c9ef0 | unnamed | src/fallout/ai/aitaskmanager.cpp:635 |
| 0x008D2060 | ~FUN_008d2060 | unnamed | src/fallout/ai/character.cpp:3744 |
| 0x00905E50 | ~FUN_00905e50_Class | probable | src/fallout/ai/lipsyncbackgroundmanager.cpp:393 |
| 0x00914AE0 | ~FUN_00914ae0 | unnamed | src/fallout/ai/middlehighprocess.cpp:3670 |
| 0x009B78E0 | ~FUN_009b78e0 | unnamed | src/fallout/ai/combat/hitdata.cpp:1219 |
| 0x009BADC0 | ~FUN_009badc0 | unnamed | src/fallout/ai/combat/muzzleflash.cpp:1557 |
| 0x009BB940 | ~FUN_009bb940 | unnamed | src/fallout/ai/combat/projectile.cpp:312 |
| 0x00C7C030 | ~FUN_00c7c030 | unnamed | src/fallout/ai/actor_o2_variant.cpp:830 |
| 0x00C7DC40 | ~FUN_00c7dc40 | unnamed | src/fallout/ai/actor_o2_variant.cpp:3519 |
