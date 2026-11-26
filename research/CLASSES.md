# NPC classes

Every class the catalogue counts as NPC-related, by subsystem. `Bases` is the full RTTI chain, nearest first. `Size` is the checked size from the decomp headers when known. `Funcs` is how many functions in [FUNCTIONS.md](FUNCTIONS.md) belong to the class.

## 1 Spawning and population

Creating references at runtime (PlaceAtMe), leveled actors, encounter zones, cell respawn timers, and the background loader that builds an actor's 3D.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| BGSEncounterZone | TESForm > BaseFormComponent | 0x30 | 0x0102CBBC | 78 | 19 |
| BGSLoadedReferenceCollection |  |  |  |  | 5 |
| ExteriorCellNewReferencesMap | NiTPointerMap<unsigned int,class BSSimpleList<struct ExteriorCellReferenceData *> *> > NiTMapBase<class NiTPointerAllocator<unsigned int>,unsigned int,class BSSimpleList<struct ExteriorCellReferenceData *> *> |  | 0x01080534 | 7 | 3 |
| ExtraEncounterZone | BSExtraData |  | 0x01015C54 | 2 | 2 |
| ExtraLeveledCreature | BSExtraData |  | 0x01015B7C | 2 | 1 |
| ExtraOriginalReference | BSExtraData |  | 0x01015BC4 | 2 | 4 |
| ExtraPackageStartLocation | BSExtraData |  | 0x01015C18 | 2 | 3 |
| ExtraPersistentCell | BSExtraData | 0x10 | 0x01015C3C | 2 | 3 |
| ExtraStartingPosition | BSExtraData |  | 0x01015B40 | 2 | 2 |
| ExtraStartingWorldOrCell | BSExtraData | 0x10 | 0x01015B4C | 2 | 1 |
| InteriorCellNewReferencesMap | NiTPointerMap<unsigned int,class BSSimpleList<unsigned int> *> > NiTMapBase<class NiTPointerAllocator<unsigned int>,unsigned int,class BSSimpleList<unsigned int> *> |  | 0x01080514 | 7 | 3 |
| LoadedReferenceMap | NiTMap<unsigned int,class TESObjectREFR *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class TESObjectREFR *> >,unsigned int,class TESObjectREFR *> | 0x18 | 0x0102CF0C | 7 | 4 |
| ModelLoader |  | 0x30 |  |  | 39 |
| QueuedActor | QueuedReference > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016CA4 | 17 | 2 |
| QueuedCharacter | QueuedActor > QueuedReference > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016CEC | 17 | 5 |
| QueuedCreature | QueuedActor > QueuedReference > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016D34 | 17 | 2 |
| QueuedFaceGenFile | QueuedFileLoad > QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016E1C | 12 | 4 |
| QueuedHead | QueuedFile > IOTask > BSTask<__int64> |  | 0x01016B04 | 11 | 6 |
| QueuedHelmet | QueuedFile > IOTask > BSTask<__int64> |  | 0x01016B4C | 11 | 7 |
| QueuedPlayer | QueuedCharacter > QueuedActor > QueuedReference > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016D7C | 17 | 4 |
| QueuedReference | QueuedFile > IOTask > BSTask<__int64> |  | 0x01016BA4 | 17 | 7 |
| ReanimateEffect | ActiveEffect |  | 0x0107C06C | 23 | 7 |
| SummonCreatureEffect | AssociatedItemEffect > ActiveEffect |  | 0x0107C2AC | 23 | 9 |
| TeleportableReference |  | 0x20 |  |  | 1 |
| TESQueuedCellManager |  |  |  |  | 1 |

## 2 Actor references (the NPC in the world)

Actor, Character, Creature and MobileObject: the live NPC object.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| Actor | MobileObject > TESObjectREFR > TESForm > BaseFormComponent > TESChildCell > MagicCaster > MagicTarget > ActorValueOwner > CachedValuesOwner | 0x1B4 | 0x01084254 | 311 | 213 |
| ActorValue |  |  |  |  | 16 |
| ActorValueOwner |  | 0x4 | 0x01049450 | 11 | 6 |
| ActorValueStore |  | 0x268 |  |  | 5 |
| ActorX |  |  |  |  | 8 |
| CachedValuesOwner |  | 0x4 | 0x01084734 | 17 | 1 |
| Character | Actor > MobileObject > TESObjectREFR > TESForm > BaseFormComponent > TESChildCell > MagicCaster > MagicTarget > ActorValueOwner > CachedValuesOwner | 0x1C8 | 0x01086A6C | 313 | 21 |
| Creature | Actor > MobileObject > TESObjectREFR > TESForm > BaseFormComponent > TESChildCell > MagicCaster > MagicTarget > ActorValueOwner > CachedValuesOwner |  | 0x010870AC | 311 | 13 |
| MatchActor |  |  |  |  | 2 |
| MobileObject | TESObjectREFR > TESForm > BaseFormComponent > TESChildCell | 0x88 | 0x0108A49C | 193 | 49 |
| NonActorMagicTarget | BSExtraData > MagicTarget |  | 0x0107BECC | 2 | 4 |
| XActor |  |  |  |  | 9 |
| xActor |  |  |  |  | 5 |

## 2b Player (shares the Actor code)

PlayerCharacter is an Actor too; listed apart so it is easy to skip.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| PlayerCharacter | Character > Actor > MobileObject > TESObjectREFR > TESForm > BaseFormComponent > TESChildCell > MagicCaster > MagicTarget > ActorValueOwner > CachedValuesOwner | 0xE50 | 0x0108AA3C | 315 | 151 |
| PlayerMover | ActorMover | 0xA0 | 0x0109297C | 15 | 14 |

## 3 Base records (what an NPC is made of)

TESNPC / TESCreature records and their parts: race, class, faction, voice, hair, eyes, head parts, leveled lists, combat style.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorValueInfo | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESDescription > BaseFormComponent > TESIcon > TESTexture > BaseFormComponent |  | 0x01067A2C | 78 | 8 |
| BGSBodyPart |  | 0xB0 | 0x01045404 | 1 | 11 |
| BGSBodyPartData | TESForm > BaseFormComponent > TESModel > BaseFormComponent > BGSPreloadable > BaseFormComponent | 0x74 | 0x01045504 | 78 | 15 |
| BGSEntryPointFunctionDataLeveledList | BGSEntryPointFunctionData | 0x8 | 0x01046320 | 7 | 5 |
| BGSHeadPart | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESModelTextureSwap > TESModel > BaseFormComponent |  | 0x010464B4 | 78 | 10 |
| BGSRagdoll | TESForm > BaseFormComponent > TESModel > BaseFormComponent | 0x148 | 0x010470EC | 78 | 9 |
| BGSVoiceType | TESForm > BaseFormComponent |  | 0x0104733C | 78 | 8 |
| CreatureSounds |  |  |  |  | 3 |
| ExtraFactionChanges | BSExtraData | 0x10 | 0x01015F30 | 2 | 5 |
| ExtraLeveledItem | BSExtraData | 0x14 | 0x01015950 | 2 | 3 |
| TESActorBase | TESBoundAnimObject > TESBoundObject > TESObject > TESForm > BaseFormComponent > TESActorBaseData > BaseFormComponent > TESContainer > BaseFormComponent > BGSTouchSpellForm > BaseFormComponent > TESSpellList > BaseFormComponent > TESAIForm > BaseFormComponent > TESHealthForm > BaseFormComponent > TESAttributes > BaseFormComponent > TESAnimation > BaseFormComponent > TESFullName > BaseFormComponent > TESModel > BaseFormComponent > TESScriptableForm > BaseFormComponent > ActorValueOwner > BGSDestructibleObjectForm > BaseFormComponent | 0x10C | 0x010492AC | 104 | 19 |
| TESActorBaseData | BaseFormComponent | 0x34 | 0x0101B0DC | 27 | 52 |
| TESAIForm | BaseFormComponent | 0x20 | 0x0101BE98 | 7 | 34 |
| TESAnimation | BaseFormComponent | 0xC | 0x0101BF50 | 4 | 7 |
| TESAttributes | BaseFormComponent | 0xC | 0x0101BF84 | 4 | 17 |
| TESClass | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESDescription > BaseFormComponent > TESTexture > BaseFormComponent > TESAttributes > BaseFormComponent | 0x60 | 0x01048BB4 | 78 | 13 |
| TESCombatStyle | TESForm > BaseFormComponent |  | 0x010266E4 | 78 | 10 |
| TESCreature | TESActorBase > TESBoundAnimObject > TESBoundObject > TESObject > TESForm > BaseFormComponent > TESActorBaseData > BaseFormComponent > TESContainer > BaseFormComponent > BGSTouchSpellForm > BaseFormComponent > TESSpellList > BaseFormComponent > TESAIForm > BaseFormComponent > TESHealthForm > BaseFormComponent > TESAttributes > BaseFormComponent > TESAnimation > BaseFormComponent > TESFullName > BaseFormComponent > TESModel > BaseFormComponent > TESScriptableForm > BaseFormComponent > ActorValueOwner > BGSDestructibleObjectForm > BaseFormComponent > TESAttackDamageForm > BaseFormComponent > TESModelList > BaseFormComponent | 0x160 | 0x01048F5C | 104 | 37 |
| TESEyes | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESTexture > BaseFormComponent |  | 0x0104973C | 78 | 8 |
| TESFaction | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESReactionForm > BaseFormComponent | 0x4C | 0x010498DC | 78 | 28 |
| TESHair | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESModel > BaseFormComponent > TESTexture > BaseFormComponent | 0x4C | 0x01049B9C | 78 | 7 |
| TESLevCharacter | TESBoundAnimObject > TESBoundObject > TESObject > TESForm > BaseFormComponent > TESLeveledList > BaseFormComponent > TESModelTextureSwap > TESModel > BaseFormComponent | 0x70 | 0x0102864C | 96 | 6 |
| TESLevCreature | TESBoundObject > TESObject > TESForm > BaseFormComponent > TESLeveledList > BaseFormComponent > TESModelTextureSwap > TESModel > BaseFormComponent | 0x70 | 0x0102886C | 96 | 7 |
| TESLeveledList | BaseFormComponent | 0x1C | 0x0101CD04 | 7 | 22 |
| TESNPC | TESActorBase > TESBoundAnimObject > TESBoundObject > TESObject > TESForm > BaseFormComponent > TESActorBaseData > BaseFormComponent > TESContainer > BaseFormComponent > BGSTouchSpellForm > BaseFormComponent > TESSpellList > BaseFormComponent > TESAIForm > BaseFormComponent > TESHealthForm > BaseFormComponent > TESAttributes > BaseFormComponent > TESAnimation > BaseFormComponent > TESFullName > BaseFormComponent > TESModel > BaseFormComponent > TESScriptableForm > BaseFormComponent > ActorValueOwner > BGSDestructibleObjectForm > BaseFormComponent > TESRaceForm > BaseFormComponent |  | 0x0104A2F4 | 104 | 47 |
| TESRace | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESDescription > BaseFormComponent > TESSpellList > BaseFormComponent > TESReactionForm > BaseFormComponent |  | 0x0104B4BC | 78 | 39 |
| TESRaceForm | BaseFormComponent | 0x8 | 0x0101D398 | 4 | 5 |
| TESSkill | TESForm > BaseFormComponent > TESDescription > BaseFormComponent > TESTexture > BaseFormComponent |  | 0x0104CC0C | 78 | 8 |

## 4 Process levels and the AI update loop

Every actor has a process (High, MiddleHigh, MiddleLow, Low). ProcessLists updates them each frame. This is where the cost of more NPCs goes.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorPathingMessageQueue | BSTCommonLLMessageQueue<class ActorPathingMessage> > BSTCommonMessageQueue<class ActorPathingMessage> > BSTMessageQueue<class ActorPathingMessage> > NiRefObject > NiMemObject |  | 0x01088158 | 7 | 2 |
| ActorsScriptTaskData | MobileObjectTaskletData > BSWin32TaskletData > BSTaskletData | 0x40 | 0x010857C8 | 7 | 5 |
| ActorUpdateTaskData | MobileObjectTaskletData > BSWin32TaskletData > BSTaskletData | 0x3C | 0x01085788 | 7 | 4 |
| ActorValueModifierList |  | 0x10 |  |  | 8 |
| AILinearTaskThread | BSLinearTaskThread > BSThread |  | 0x01085688 | 5 | 4 |
| AILinearTaskThreadManager |  |  |  |  | 5 |
| AITaskManager |  |  |  |  | 2 |
| AITaskThread | BSThread |  | 0x01085818 | 2 | 2 |
| AIThreadManager |  |  |  |  | 3 |
| AnimationTaskData | MobileObjectTaskletData > BSWin32TaskletData > BSTaskletData | 0x38 | 0x01085768 | 7 | 4 |
| BaseProcess |  | 0x30 | 0x01085E2C | 493 | 29 |
| BSPlayerDistanceCheckController | NiTimeController > NiObject > NiRefObject > NiMemObject |  | 0x010867FC | 45 | 4 |
| CachedValues |  |  |  |  | 1 |
| FurnitureProcess |  |  |  |  | 1 |
| HighActorCuller | MobIterOperator |  | 0x01082CC0 | 1 | 4 |
| HighProcess | MiddleHighProcess > MiddleLowProcess > LowProcess > BaseProcess | 0x46C | 0x01087864 | 541 | 160 |
| LowProcess | BaseProcess | 0xB4 | 0x010886E4 | 519 | 86 |
| MiddleHighProcess | MiddleLowProcess > LowProcess > BaseProcess | 0x25C | 0x0108904C | 540 | 151 |
| MiddleLowProcess | LowProcess > BaseProcess | 0xC8 | 0x01089BCC | 520 | 16 |
| MobileObjectTaskletData | BSWin32TaskletData > BSTaskletData | 0x38 | 0x01085748 | 7 | 4 |
| ModifierList |  |  |  |  | 5 |
| ProcessLists |  | 0x103E0 |  |  | 60 |

## 5 AI packages and daily routines

Packages (sandbox, patrol, guard, escort, eat, sleep...) and the procedures that run them: what makes an NPC look busy.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorPackage |  |  |  |  | 1 |
| ActorPackage_008ad970 |  |  |  |  | 1 |
| ActorPackage_GetTarget_Helper |  |  |  |  | 1 |
| ActorPackageContext |  | 0x18 |  |  | 4 |
| ActorPackageData |  | 0x4 | 0x01068AA4 | 6 | 4 |
| ActorPackageLegacySave |  |  |  |  | 1 |
| ActorPackageLoad |  |  |  |  | 1 |
| ActorPackageSaver |  |  |  |  | 1 |
| AlarmPackage | TESPackage > TESForm > BaseFormComponent |  | 0x01092BDC | 88 | 6 |
| AnimIdle | NiRefObject > NiMemObject |  | 0x0101DCD8 | 2 | 12 |
| AvoidancePackage |  |  |  |  | 1 |
| BackUpPackage | TESPackage > TESForm > BaseFormComponent |  | 0x01092D84 | 88 | 6 |
| BGSIdleCollection | BaseFormComponent | 0x10 | 0x0101AA98 | 4 | 12 |
| BGSIdleMarker | TESBoundObject > TESObject > TESForm > BaseFormComponent > BGSIdleCollection > BaseFormComponent | 0x40 | 0x0104664C | 96 | 7 |
| BSFurnitureMarker | NiExtraData > NiObject > NiRefObject > NiMemObject |  | 0x010C2A94 | 37 | 12 |
| CaravanAIPackage |  |  |  |  | 1 |
| DialoguePackage | TESPackage > TESForm > BaseFormComponent |  | 0x01092F6C | 88 | 10 |
| EscortActorPackageData | ActorPackageData | 0x18 | 0x01093188 | 6 | 4 |
| ExtraAction | BSExtraData | 0x14 | 0x01015BAC | 2 | 3 |
| ExtraDataListRemoveTrespassPackage |  |  |  |  | 1 |
| ExtraFollower | BSExtraData |  | 0x01015B64 | 2 | 3 |
| ExtraGuardedRefData | BSExtraData |  | 0x01015B70 | 2 | 5 |
| ExtraPackage | BSExtraData |  | 0x01015C24 | 2 | 2 |
| ExtraPackageData | BSExtraData |  | 0x010151FC | 2 | 2 |
| ExtraPatrolRefInUseData | BSExtraData | 0x10 | 0x01015F70 | 2 | 5 |
| ExtraTresPassPackage | BSExtraData |  | 0x01015944 | 2 | 4 |
| FleePackage | TESPackage > TESForm > BaseFormComponent |  | 0x010931E4 | 88 | 9 |
| FleeSavePackage |  |  |  |  | 1 |
| GuardActorPackageData | ActorPackageData | 0x14 | 0x010933C8 | 6 | 7 |
| IdleAnimationManager |  |  |  |  | 5 |
| IdleSystem |  | 0x8 |  |  | 7 |
| P070Package |  |  |  |  | 1 |
| Package |  |  |  |  | 3 |
| PackageEventActionData |  | 0x10 |  |  | 3 |
| PackageList |  | 0x8 |  |  | 6 |
| PackageLocation |  |  |  |  | 11 |
| PackageTarget |  |  |  |  | 6 |
| PackageTargetRecord |  | 0x10 |  |  | 8 |
| PatrolActorPackageData | ActorPackageData | 0x38 | 0x01093418 | 6 | 12 |
| Procedure |  |  |  |  | 2 |
| ProcedureValue |  |  |  |  | 1 |
| SandBoxActorPackageData | ActorPackageData | 0x64 | 0x010935F8 | 6 | 12 |
| SbActorPackageData |  |  |  |  | 1 |
| SearchPackage | TESPackage > TESForm > BaseFormComponent |  | 0x01093674 | 88 | 3 |
| SpectatorPackage | TESPackage > TESForm > BaseFormComponent |  | 0x0109381C | 88 | 13 |
| TESAmbushPackageData | TESPackageData |  | 0x01068860 | 8 | 4 |
| TESDialoguePackageData | TESPackageData |  | 0x010688AC | 8 | 8 |
| TESEatPackageData | TESPackageData |  | 0x01068938 | 8 | 7 |
| TESEscortPackageData | TESPackageData |  | 0x01068960 | 8 | 7 |
| TESFollowPackageData | TESPackageData |  | 0x01068988 | 8 | 6 |
| TESIdleForm | TESForm > BaseFormComponent > TESModelAnim > TESModel > BaseFormComponent | 0x4C | 0x01049D0C | 78 | 22 |
| TESPackage | TESForm > BaseFormComponent | 0x80 | 0x0106847C | 88 | 85 |
| TESPackageData |  |  | 0x01068884 | 8 | 3 |
| TESPatrolPackageData | TESPackageData |  | 0x010689E4 | 8 | 8 |
| TESUseItemPackageData | TESPackageData |  | 0x01068A0C | 8 | 6 |
| TESUseWeaponPackageData | TESPackageData | 0x24 | 0x01068A64 | 8 | 10 |
| TrespassPackage | TESPackage > TESForm > BaseFormComponent |  | 0x010939EC | 88 | 6 |
| UseWeaponActorPackageData | ActorPackageData | 0x8 | 0x01068A88 | 6 | 4 |

## 6 Movement and pathfinding

ActorMover, the path handlers (Detailed for loaded actors, Virtual for unloaded ones) and pathing requests.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorMover |  | 0x88 | 0x0109223C | 15 | 37 |
| ActorPathHandler |  | 0x14 | 0x0109231C | 33 | 5 |
| bhkCharacterController | bhkCharacterProxy > bhkSerializable > bhkRefObject > NiObject > NiRefObject > NiMemObject > hkpCharacterContext > hkReferencedObject > hkBaseObject > bhkCharacterListener > hkpCharacterProxyListener > hkpSurfaceInfo |  | 0x010C49C4 | 53 | 18 |
| bhkCharacterProxy | bhkSerializable > bhkRefObject > NiObject > NiRefObject > NiMemObject |  | 0x010C45CC | 49 | 9 |
| bhkCharacterStateClimbing | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010C4944 | 9 | 0 |
| bhkCharacterStateFlying | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010C496C | 9 | 0 |
| bhkCharacterStateInAir | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010CB36C | 9 | 1 |
| bhkCharacterStateJumping | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010CB398 | 9 | 1 |
| bhkCharacterStateOnGround | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010CB3F0 | 9 | 1 |
| bhkCharacterStateProjectile | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010CB344 | 9 | 1 |
| bhkCharacterStateSwimming | bhkCharacterState > hkpCharacterState > hkReferencedObject > hkBaseObject |  | 0x010CB3C4 | 9 | 1 |
| DetailedActorPathHandler | ActorPathHandler |  | 0x010923EC | 33 | 19 |
| PathBuilder |  | 0x34 |  |  | 16 |
| Pathing |  |  |  |  | 5 |
| PathingActorData |  | 0xC |  |  | 1 |
| PathingAvoidNode |  |  |  |  | 3 |
| PathingAvoidNodeArray | BSSimpleArrayRefCounted<class PathingAvoidNode,1024> > BSSimpleArray<class PathingAvoidNode,1024> > NiRefObject > NiMemObject |  | 0x0106D1E4 | 4 | 4 |
| PathingCoverLocation | PathingLocation |  | 0x0106CBC0 | 2 | 8 |
| PathingGraphNode |  | 0x3C |  |  | 1 |
| PathingGrid |  |  |  |  | 1 |
| PathingLocation |  | 0x28 | 0x0102583C | 2 | 28 |
| PathingLocationArray |  |  |  |  | 3 |
| PathingLocationCheck |  |  |  |  | 1 |
| PathingLocationOwner |  |  |  |  | 1 |
| PathingLocationProxy |  |  |  |  | 2 |
| PathingLOSGrid |  |  |  |  | 4 |
| PathingLOSGridCell |  |  |  |  | 2 |
| PathingLOSGridMap | NiRefObject > NiMemObject |  | 0x0106CEAC | 2 | 9 |
| PathingLOSGridMapX |  |  |  |  | 1 |
| PathingLOSMap | NiRefObject > NiMemObject |  | 0x0106CF5C | 2 | 9 |
| PathingNode |  |  |  |  | 2 |
| PathingRequest | NiRefObject > NiMemObject | 0xB0 | 0x0106D030 | 9 | 25 |
| PathingRequestClosePoint | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D230 | 9 | 5 |
| PathingRequestCover | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D29C | 9 | 3 |
| PathingRequestCoveredMove | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D2D4 | 9 | 4 |
| PathingRequestFlee | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D300 | 9 | 6 |
| PathingRequestHide | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D32C | 9 | 6 |
| PathingRequestLOS | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D38C | 9 | 6 |
| PathingRequestOptimalLocation | PathingRequest > NiRefObject > NiMemObject |  | 0x0106D3B8 | 9 | 4 |
| PathingRequestSafeStraightLine | PathingRequestClosePoint > PathingRequest > NiRefObject > NiMemObject |  | 0x0106D414 | 9 | 5 |
| PathingSearchRayCast |  |  | 0x0106D47C | 1 | 5 |
| PathingSolution | NiRefObject > NiMemObject | 0x100 | 0x0106D4BC | 2 | 17 |
| PathingSpline |  |  |  |  | 6 |
| PathingTaskData | BSWin32TaskletData > BSTaskletData |  | 0x0106D550 | 4 | 6 |
| PathingTaskShell |  |  |  |  | 1 |
| PathManager |  |  |  |  | 5 |
| PathSearch |  |  |  |  | 4 |
| PathSmoother |  |  |  |  | 10 |
| PathSmootherAccess |  |  |  |  | 1 |
| PathSmootherPOVSearch | AStarSearch<class PathSmootherPOVNode,class PathSmootherPOVLink> |  | 0x0106B9CC | 3 | 17 |
| VirtualActorPathHandler | ActorPathHandler | 0x20 | 0x010929FC | 33 | 9 |

## 6b Navmesh (the data paths run on)

NavMesh data and searches the path code uses.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| NavMesh | TESForm > BaseFormComponent > TESChildCell > NiRefObject > NiMemObject | 0x108 | 0x0106A0B4 | 78 | 44 |
| NavMeshActionController |  |  |  |  | 1 |
| NavMeshAdjust |  |  |  |  | 1 |
| NavMeshBounds |  |  |  |  | 3 |
| NavMeshCollection |  |  |  |  | 1 |
| NavMeshEdgePoint |  |  |  |  | 1 |
| NavMeshEdgeQuery |  |  |  |  | 1 |
| NavMeshGrid |  | 0x28 |  |  | 4 |
| NavMeshGridOwner |  |  |  |  | 1 |
| NavMeshGridX |  |  |  |  | 1 |
| NavMeshInfo |  |  |  |  | 15 |
| NavMeshInfoMap | TESForm > BaseFormComponent |  | 0x0106BB8C | 78 | 11 |
| NavMeshInfoProxy |  |  |  |  | 1 |
| NavMeshInfoSaveShell |  |  |  |  | 1 |
| NavMeshInfoSearch | AStarSearch<class NavMeshInfo const *,class TESObjectREFR *> |  | 0x0106C22C | 3 | 5 |
| NavMeshListNode |  |  |  |  | 1 |
| NavMeshObstacleCutter |  |  |  |  | 6 |
| NavMeshObstacleManager |  |  |  |  | 23 |
| NavMeshOps |  |  |  |  | 1 |
| NavMeshPOVSearch | AStarSearch<class NavMeshPOVSearchNode,class NavMeshPOVSearchLink> |  | 0x0106B39C | 3 | 5 |
| NavMeshProxy |  |  |  |  | 1 |
| NavMeshPtr |  | 0x4 |  |  | 4 |
| NavMeshRender |  |  |  |  | 5 |
| NavMeshSearch | AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B63C | 3 | 9 |
| NavMeshSearchClosePoint | AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B6FC | 3 | 4 |
| NavMeshSearchEdges |  |  |  |  | 1 |
| NavMeshSearchFlee | AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B78C | 3 | 5 |
| NavMeshSearchHide | NavMeshSearch > AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B7DC | 3 | 4 |
| NavMeshSearchLOS | AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B830 | 3 | 5 |
| NavMeshSearchLOSArray |  |  |  |  | 5 |
| NavMeshSearchMaxCost | NavMeshSearch > AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B87C | 3 | 5 |
| NavMeshSearchSLPoint | NavMeshSearch > AStarSearch<struct NavMeshSearchNode,struct NavMeshSearchLink> |  | 0x0106B96C | 3 | 5 |
| NavMeshTriangle |  | 0x10 |  |  | 10 |
| NavMeshTriangleReference |  | 0x14 |  |  | 1 |
| ObstacleData | NiRefObject > NiMemObject |  | 0x0106C490 | 2 | 2 |
| ObstacleTaskData | BSWin32TaskletData > BSTaskletData |  | 0x0106C7EC | 4 | 6 |

## 7 Combat

CombatController, combat groups, goals, actions and procedures.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorCombatGroup |  |  |  |  | 1 |
| CombatAction |  |  | 0x0108CAB8 | 5 | 14 |
| CombatActionAcquireLineOfSight | CombatAction |  | 0x0108CDBC | 5 | 1 |
| CombatActionActivateCombatItem | CombatAction |  | 0x0108CD74 | 5 | 2 |
| CombatActionApproachTarget | CombatAction |  | 0x0108CDA4 | 5 | 1 |
| CombatActionAttackGrenade | CombatAction |  | 0x0108CBF4 | 5 | 2 |
| CombatActionAttackGrenadeFlushTarget | CombatAction |  | 0x0108CC0C | 5 | 3 |
| CombatActionAttackGrenadeFromCover | CombatAction |  | 0x0108CC24 | 5 | 2 |
| CombatActionAttackHandToHand | CombatAction |  | 0x0108CBDC | 5 | 1 |
| CombatActionAttackMelee | CombatAction |  | 0x0108CBC4 | 5 | 2 |
| CombatActionAttackRanged | CombatAction |  | 0x0108CB50 | 5 | 1 |
| CombatActionAttackRangedExplosive | CombatAction |  | 0x0108CB94 | 5 | 2 |
| CombatActionAttackRangedExplosiveFromCover | CombatAction |  | 0x0108CBAC | 5 | 1 |
| CombatActionAttackRangedFromCover | CombatAction |  | 0x0108CB7C | 5 | 1 |
| CombatActionAvoidThreat | CombatAction |  | 0x0108CCE4 | 5 | 1 |
| CombatActionDodge | CombatAction |  | 0x0108CD2C | 5 | 1 |
| CombatActionDrawWeapon | CombatAction |  | 0x0108CCB4 | 5 | 1 |
| CombatActionFlee | CombatAction |  | 0x0108CD5C | 5 | 2 |
| CombatActionHide | CombatAction |  | 0x0108CDD4 | 5 | 3 |
| CombatActionIgnoreBlockedTarget | CombatAction |  | 0x0108CD44 | 5 | 2 |
| CombatActionInvestigate | CombatAction |  | 0x0108CD14 | 5 | 1 |
| CombatActionMove | CombatAction |  | 0x0108CC3C | 5 | 4 |
| CombatActionMoveAndAttackGrenade | CombatActionAttackGrenade > CombatAction |  | 0x0108CC9C | 5 | 2 |
| CombatActionMoveAndAttackRanged | CombatActionAttackRanged > CombatAction |  | 0x0108CC6C | 5 | 1 |
| CombatActionMoveAndAttackRangedExplosive | CombatActionAttackRangedExplosive > CombatAction |  | 0x0108CC84 | 5 | 1 |
| CombatActionMoveAndSwitchToMelee | CombatActionMove > CombatAction |  | 0x0108CC54 | 5 | 2 |
| CombatActionSearch | CombatAction |  | 0x0108CCFC | 5 | 2 |
| CombatActionSwitchWeapon | CombatAction |  | 0x0108CCCC | 5 | 2 |
| CombatActionUseCombatItem | CombatAction |  | 0x0108CD8C | 5 | 2 |
| CombatBox |  |  |  |  | 3 |
| CombatClock |  |  |  |  | 1 |
| CombatController | TESPackage > TESForm > BaseFormComponent |  | 0x0108CE74 | 88 | 40 |
| CombatCoverLocation |  |  |  |  | 3 |
| CombatCoverMap | NiTMap<unsigned int,class ReservedCoverLocation *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class ReservedCoverLocation *> >,unsigned int,class ReservedCoverLocation *> |  | 0x0108D0E4 | 7 | 7 |
| CombatCoverSearchInfo |  |  |  |  | 5 |
| CombatDamageCalculator |  |  |  |  | 2 |
| CombatDecompClass |  |  |  |  | 1 |
| CombatDialogueHandler |  |  |  |  | 1 |
| CombatEntryOwner |  |  |  |  | 1 |
| CombatFlagHolder |  |  |  |  | 5 |
| CombatFormulas |  |  |  |  | 11 |
| CombatGoal |  | 0x1C | 0x0108D440 | 2 | 4 |
| CombatGoalActivateCombatItem | CombatGoal |  | 0x0108D4AC | 2 | 1 |
| CombatGoalAdvance | CombatGoal |  | 0x0108D4F4 | 2 | 1 |
| CombatGoalAmbush | CombatGoal |  | 0x0108D4DC | 2 | 1 |
| CombatGoalAvoidThreats | CombatGoal |  | 0x0108D494 | 2 | 1 |
| CombatGoalCluster | CombatGoal |  | 0x0108D50C | 2 | 1 |
| CombatGoalFallBack | CombatGoal |  | 0x0108D4D0 | 2 | 1 |
| CombatGoalFindTarget | CombatGoal |  | 0x0108D488 | 2 | 1 |
| CombatGoalFlank | CombatGoal |  | 0x0108D4C4 | 2 | 1 |
| CombatGoalFlee | CombatGoal |  | 0x0108D4A0 | 2 | 1 |
| CombatGoalFlushTarget | CombatGoal |  | 0x0108D524 | 2 | 1 |
| CombatGoalGuard | CombatGoal |  | 0x0108D500 | 2 | 1 |
| CombatGoalHideFromTarget | CombatGoal |  | 0x0108D518 | 2 | 1 |
| CombatGoalKillTarget | CombatGoal |  | 0x0108D47C | 2 | 1 |
| CombatGoalReachDestination | CombatGoal |  | 0x0108D4E8 | 2 | 1 |
| CombatGoalStayInCombatArea | CombatGoal |  | 0x0108D530 | 2 | 1 |
| CombatGoalUseCombatItem | CombatGoal |  | 0x0108D4B8 | 2 | 1 |
| CombatGroup |  |  |  |  | 33 |
| CombatGroupCluster |  |  |  |  | 2 |
| CombatGroupData |  |  |  |  | 4 |
| CombatGroupStrategy |  |  | 0x0108D94C | 3 | 3 |
| CombatGroupStrategyAdvance | CombatGroupStrategy |  | 0x0108D97C | 3 | 3 |
| CombatGroupStrategyAmbush | CombatGroupStrategy |  | 0x0108D96C | 3 | 4 |
| CombatGroupStrategyFallBack | CombatGroupStrategy |  | 0x0108D95C | 3 | 3 |
| CombatGroupStrategyFlank | CombatGroupStrategy |  | 0x0108D93C | 3 | 4 |
| CombatLocation |  |  |  |  | 5 |
| CombatLocationTarget |  |  |  |  | 4 |
| CombatLogic |  |  |  |  | 1 |
| CombatLOS |  |  |  |  | 1 |
| CombatManager |  | 0x3C |  |  | 20 |
| CombatMapOwner |  |  |  |  | 1 |
| CombatMapRef |  |  |  |  | 1 |
| CombatMember |  |  |  |  | 2 |
| CombatMove |  |  |  |  | 1 |
| CombatMovementRestrictions |  |  |  |  | 1 |
| CombatNodeArray |  |  |  |  | 1 |
| CombatNodeFinder |  |  |  |  | 1 |
| CombatObj |  |  |  |  | 1 |
| CombatPlan |  |  |  |  | 5 |
| CombatPlanner | AStarSearch<class CombatPlanNode *,class CombatPlanLink *> |  | 0x0108CFD8 | 3 | 5 |
| CombatPlannerData |  |  |  |  | 2 |
| CombatPlanNode |  |  |  |  | 1 |
| CombatPosition |  |  |  |  | 1 |
| CombatProcedure |  | 0x10 | 0x01090874 | 17 | 11 |
| CombatProcedureActivateObject | CombatProcedure |  | 0x0109082C | 17 | 10 |
| CombatProcedureAttackGrenade | CombatProcedure |  | 0x010909BC | 17 | 9 |
| CombatProcedureAttackLow | CombatProcedure |  | 0x01090AEC | 17 | 6 |
| CombatProcedureAttackMelee | CombatProcedure |  | 0x01090C04 | 17 | 17 |
| CombatProcedureAttackRanged | CombatProcedure |  | 0x01090ED4 | 17 | 7 |
| CombatProcedureBeInCover | CombatProcedure |  | 0x010910F4 | 17 | 6 |
| CombatProcedureEngageTarget | CombatProcedure |  | 0x01091514 | 17 | 7 |
| CombatProcedureEvade | CombatProcedure |  | 0x01091984 | 17 | 4 |
| CombatProcedureEx |  |  |  |  | 1 |
| CombatProcedureHideFromTarget | CombatProcedure |  | 0x01091A64 | 17 | 4 |
| CombatProcedureMove | CombatProcedure |  | 0x01091BB4 | 17 | 8 |
| CombatProcedureSearch | CombatProcedure |  | 0x01091DB4 | 17 | 6 |
| CombatProcedureShell |  |  |  |  | 1 |
| CombatProcedureSW |  |  |  |  | 1 |
| CombatProcedureSwitchWeapon | CombatProcedure |  | 0x010920CC | 17 | 5 |
| CombatProcedureUseCombatItem | CombatProcedure |  | 0x0109214C | 17 | 6 |
| CombatRange |  |  |  |  | 1 |
| CombatS |  |  |  |  | 1 |
| CombatSearchCls |  |  |  |  | 1 |
| CombatSearchLocation |  |  |  |  | 1 |
| CombatSearchMgr |  |  |  |  | 1 |
| CombatState |  |  |  |  | 44 |
| CombatStateArray |  |  |  |  | 2 |
| CombatStateHash |  |  |  |  | 1 |
| CombatStyleData |  |  |  |  | 1 |
| CombatTarget |  |  |  |  | 3 |
| CombatTargetMap | NiTMap<class Actor *,class CombatTargetData *> > NiTMapBase<class DFALL<class NiTMapItem<class Actor *,class CombatTargetData *> >,class Actor *,class CombatTargetData *> | 0x10 | 0x0108E1E8 | 7 | 6 |
| CombatTargetTimestamp |  | 0x4 |  |  | 2 |
| CombatThing |  |  |  |  | 1 |
| CombatThreat |  |  |  |  | 2 |
| CombatThreatMap | NiTMap<unsigned int,class CombatThreat *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class CombatThreat *> >,unsigned int,class CombatThreat *> |  | 0x0108E2E8 | 7 | 10 |
| CombatTimer |  |  |  |  | 2 |
| CombatTimeStamp |  |  |  |  | 3 |
| CombatUpdate |  |  |  |  | 1 |
| CombatUpdater |  |  |  |  | 1 |
| CombatUtilities |  |  |  |  | 25 |
| CombatWorldState |  |  |  |  | 2 |
| CombatWorldStateArray |  |  |  |  | 3 |
| CombatWorldStateListNode |  |  |  |  | 1 |

## 8 Detection, crime and reactions

Detection, alarms and crime tracking.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| ActorCause |  |  |  |  | 1 |
| Crime |  |  |  |  | 6 |
| CrimeProcess |  |  |  |  | 1 |
| DetectionList |  |  |  |  | 1 |
| DetectionLists |  |  |  |  | 1 |
| DetectionState |  |  |  |  | 1 |
| DetectionStateProxy |  |  |  |  | 1 |
| DetectionTaskData | MobileObjectTaskletData > BSWin32TaskletData > BSTaskletData | 0x40 | 0x01085728 | 7 | 3 |
| DetectLifeEffect | ValueModifierEffect > ActiveEffect |  | 0x01079E7C | 26 | 6 |
| ExtraActorCause | BSExtraData |  | 0x0101598C | 2 | 3 |
| ExtraOwnership | BSExtraData |  | 0x010158B4 | 2 | 3 |
| ExtraPlayerCrimeList | BSExtraData |  | 0x01015C30 | 2 | 4 |

## 9 Dialogue, barks and companions

Topics, conversations between NPCs, follower barks, companion wheel.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| CompanionWheelMenu | Menu |  | 0x01071D0C | 18 | 10 |
| Conversation |  |  |  |  | 8 |
| DialogMenu | Menu | 0x13C | 0x0107257C | 18 | 15 |
| DialogueItem |  | 0x1C |  |  | 9 |
| DialogueResponse |  |  |  |  | 4 |
| ExtraInfoGeneralTopic | BSExtraData |  | 0x01015C00 | 2 | 4 |
| ExtraSayTopicInfoOnceADay | BSExtraData |  | 0x01015F3C | 2 | 4 |
| ExtraSayToTopicInfo | BSExtraData |  | 0x01015F48 | 2 | 2 |
| LipSyncAnimation |  | 0x10 |  |  | 2 |
| LipSynchAnim |  |  |  |  | 5 |
| LipTask | QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x010885B8 | 12 | 2 |
| MenuTopic |  | 0x2C |  |  | 6 |
| RadioConvTask | QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x0107CF18 | 13 | 5 |
| TESTopic | TESForm > BaseFormComponent > TESFullName > BaseFormComponent | 0x40 | 0x0104D19C | 78 | 31 |
| TESTopicInfo | TESForm > BaseFormComponent | 0x50 | 0x0104D5B4 | 78 | 37 |
| TESTopicInfoData |  | 0x18 |  |  | 2 |
| TopicMenuController |  | 0x18 |  |  | 9 |

## 10 Animation, faces and bodies

FaceGen heads, biped models, animation data and idle animations.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| Animation |  |  |  |  | 46 |
| AnimSequenceBase |  |  | 0x0101D8E8 | 7 | 3 |
| AnimSequenceMultiple | AnimSequenceBase |  | 0x0101D908 | 7 | 6 |
| AnimSequenceSingle | AnimSequenceBase |  | 0x0101D8C8 | 7 | 4 |
| BGSBipedModelList | BaseFormComponent | 0x8 | 0x0101A4C4 | 4 | 7 |
| BipedAnim |  | 0x2B4 |  |  | 33 |
| BodyPartDisplay |  |  |  |  | 3 |
| BSAnimGroupSequence | NiControllerSequence > NiObject > NiRefObject > NiMemObject | 0x78 | 0x0101DE3C | 36 | 12 |
| BSAnimNote | NiObject > NiRefObject > NiMemObject |  | 0x01097BF4 | 36 | 5 |
| BSAnimNoteListener |  |  |  |  | 1 |
| BSAnimNoteReceiver | IBSAnimNoteReceiver |  | 0x0101FC74 | 2 | 3 |
| BSAnimNotes | NiObject > NiRefObject > NiMemObject |  | 0x01097DD4 | 35 | 7 |
| BSFaceGenAnimationData | NiExtraData > NiObject > NiRefObject > NiMemObject |  | 0x01064E1C | 76 | 31 |
| BSFaceGenBaseMorphExtraData | NiExtraData > NiObject > NiRefObject > NiMemObject |  | 0x01065FAC | 37 | 3 |
| BSFaceGenBinaryFile | FutBinaryFileC |  | 0x010A2C38 | 6 | 4 |
| BSFaceGenImage | NiRefObject > NiMemObject |  | 0x010653C4 | 2 | 3 |
| BSFaceGenKeyframe |  | 0xC | 0x010653FC | 19 | 6 |
| BSFaceGenKeyframeMultiple | BSFaceGenKeyframe | 0x14 | 0x0106544C | 21 | 15 |
| BSFaceGenManager |  |  |  |  | 39 |
| BSFaceGenModel | NiRefObject > NiMemObject |  | 0x01065AF4 | 2 | 20 |
| BSFaceGenModelExtraData | NiExtraData > NiObject > NiRefObject > NiMemObject |  | 0x01065BF4 | 39 | 2 |
| BSFaceGenModelMap |  |  | 0x01065678 | 1 | 13 |
| BSFaceGenModelTextureData |  |  |  |  | 1 |
| BSFaceGenMorph |  |  | 0x01065CB8 | 2 | 3 |
| BSFaceGenMorphData | NiRefObject > NiMemObject |  | 0x01065F04 | 18 | 5 |
| BSFaceGenMorphDataHair | BSFaceGenMorphData > NiRefObject > NiMemObject |  | 0x01065F5C | 18 | 3 |
| BSFaceGenMorphDataHead | BSFaceGenMorphData > NiRefObject > NiMemObject |  | 0x01065EB4 | 18 | 5 |
| BSFaceGenMorphDifferential | BSFaceGenMorph |  | 0x01065CC4 | 2 | 4 |
| BSFaceGenMorphStatistical | BSFaceGenMorph |  | 0x01065CD0 | 2 | 4 |
| BSFaceGenNiNode | NiNode > NiAVObject > NiObjectNET > NiObject > NiRefObject > NiMemObject |  | 0x010660DC | 75 | 19 |
| FaceGenBasisOwner |  |  |  |  | 1 |
| FaceGenMatrix<float> |  |  |  |  | 3 |
| FaceGenNpcData |  |  |  |  | 2 |
| FaceGenPaletteBase |  |  |  |  | 2 |
| FaceGenPaletteEntry |  |  |  |  | 1 |
| FaceGenTriData |  |  |  |  | 2 |
| QueuedAnimIdle | QueuedKF > QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016A80 | 12 | 5 |
| QueuedKF | QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016A48 | 12 | 6 |
| QueuedReplacementKF | QueuedKF > QueuedFileEntry > QueuedFile > IOTask > BSTask<__int64> |  | 0x01016AC0 | 12 | 5 |
| QueuedReplacementKFList | QueuedFile > IOTask > BSTask<__int64> |  | 0x01016FC0 | 11 | 3 |
| TESAnimGroup | NiRefObject > NiMemObject |  | 0x010484E8 | 2 | 30 |

## 11 Cells and world loading (where NPCs live)

Grid and cell loading that decides which NPCs are loaded at all.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| BGSCellNumericIDArrayMap | NiTMap<unsigned int,class BSSimpleArray<unsigned int,1024> *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class BSSimpleArray<unsigned int,1024> *> >,unsigned int,class BSSimpleArray<unsigned int,1024> *> |  | 0x0107FEF4 | 7 | 4 |
| BGSReconstructCellBlocksMap | NiTMap<unsigned int,class BGSReconstructCellSubBlocksMap *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class BGSReconstructCellSubBlocksMap *> >,unsigned int,class BGSReconstructCellSubBlocksMap *> |  | 0x0107E990 | 7 | 4 |
| BGSReconstructCellsMap | NiTMap<unsigned int,class BGSReconstructFormsMap *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class BGSReconstructFormsMap *> >,unsigned int,class BGSReconstructFormsMap *> |  | 0x0107E950 | 7 | 4 |
| BGSReconstructCellSubBlocksMap | NiTMap<unsigned int,class BGSReconstructCellsMap *> > NiTMapBase<class DFALL<class NiTMapItem<unsigned int,class BGSReconstructCellsMap *> >,unsigned int,class BGSReconstructCellsMap *> |  | 0x0107E970 | 7 | 4 |
| ExteriorCellLoaderTask | IOTask > BSTask<__int64> |  | 0x0102D028 | 8 | 6 |
| GridArray |  |  | 0x01020634 | 10 | 5 |
| GridCellArray | GridArray |  | 0x01020698 | 10 | 13 |

## (partly) 1 Spawning and population

Big shared classes: only their NPC-related methods are in the function list.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| TESDataHandler |  |  |  |  | 2 |
| TESObjectREFR | TESForm > BaseFormComponent > TESChildCell | 0x68 | 0x0102F55C | 144 | 44 |

## (partly) 11 Cells and world loading (where NPCs live)

Big shared classes: only their NPC-related methods are in the function list.

| Class | Bases | Size | Vtable | Virtuals | Funcs |
|---|---|---|---|---|---|
| TES |  | 0xC4 | 0x010178B4 | 1 | 31 |
| TESObjectCELL | TESForm > BaseFormComponent > TESFullName > BaseFormComponent |  | 0x0102E9B4 | 78 | 66 |
| TESWorldSpace | TESForm > BaseFormComponent > TESFullName > BaseFormComponent > TESTexture > BaseFormComponent |  | 0x0103195C | 80 | 27 |
