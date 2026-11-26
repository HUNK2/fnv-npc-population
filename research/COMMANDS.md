# NPC script and console commands

213 vanilla commands that act on or ask about NPCs. `Execute` is the engine handler address (the function that runs when a script or the console calls the command). Optional parameters are in brackets.

| Command | Short | Opcode | Execute | Parameters | Help |
|---|---|---|---|---|---|
| AddCreatureToLeveledList |  | 0x1235 | 0x005DE670 | Leveled Creature, Creature or Leveled Creature, Level |  |
| AddItemToLeveledList |  | 0x1236 | 0x005DE700 | Leveled Item, Object ID, Level, Count, Health Percent |  |
| AddNPCToLeveledList |  | 0x1234 | 0x005DE670 | Leveled Character, NPC or Leveled Character, Level |  |
| AddScriptPackage |  | 0x1097 | 0x005CC4F0 | Package |  |
| AddToFaction | Addfac | 0x117F | 0x005D5390 | Faction, Value |  |
| AgeRace |  | 0x11E4 | 0x005DA690 | Integer |  |
| AlwaysShowActorSubtitles |  | 0x1277 | 0x005DFF70 | Integer | Set actor to always show subtitles |
| CalcLowPathToPoint | LP2P | 0x0129 | 0x005C25F0 | Integer, Integer, Integer | ignore locks, allow disabled doors, ignore min use |
| CalcPathToPoint | P2P | 0x0128 | 0x005D4A40 |  |  |
| ClearActorsFactionsPlayerEnemyFlag |  | 0x11CA | 0x005D9550 |  |  |
| ClearFactionPlayerEnemyFlag |  | 0x11C9 | 0x005D9500 | Faction |  |
| CreateDetectionEvent |  | 0x1068 | 0x005DAC80 | TESObjectREFR, Integer , [Integer ] |  |
| DamageActorValue | DamageAV | 0x1181 | 0x005BDF20 | Actor Value, Amount | Damage an actor value. |
| DebugCombatPlan | dcp | 0x0196 | 0x005D5720 |  | Debugs the combat plan on an actor |
| Disable |  | 0x1022 | 0x005C45E0 | [Integer (Optional)] |  |
| DisableAllActors | DisAA | 0x11A9 | 0x005C47E0 |  |  |
| DisableLinkedPathPoints |  | 0x112B | 0x005D4A40 |  |  |
| DisableNavMesh |  | 0x11BF | 0x005BD240 | String | Disable navmesh by FormID |
| DuplicateNPCStats |  | 0x114F | 0x005C6C80 | [Actor (optional)] |  |
| Enable |  | 0x1021 | 0x005C43D0 | [Integer (Optional)] |  |
| EnableCellTracking |  | 0x127E | 0x005D4A40 | Integer | Enables or disables cell tracking |
| EnableLinkedPathPoints |  | 0x112A | 0x005D4A40 |  |  |
| EnableNavMesh |  | 0x11C0 | 0x005BD300 | String | Enable navmesh by FormID |
| EssentialDeathReload |  | 0x114D | 0x005B4550 | String |  |
| EvalActorTextures | EAT | 0x01CA | 0x005D4A40 |  |  |
| EvaluatePackage | evp | 0x105E | 0x005C95A0 |  |  |
| FlushNonPersistActors | Flush | 0x017F | 0x005D4400 | Integer | Deletes all the actors in High who are not persistant |
| ForceActorValue | ForceAV | 0x110E | 0x005BE190 | Actor Value, Amount | Does modav XXX (value - getav XXX). [player.forceav luck 25] |
| ForceFlee | Flee | 0x10F5 | 0x005D09E0 | [Cell (optional)], [ObjectReferenceID (optional)] | Forces a actor to flee if destination or cell is passed in uses them |
| FriendDispositionBoost |  | 0x1195 | 0x005BE870 |  |  |
| GetActorAggroRadiusViolated |  | 0x1076 | 0x005DA280 |  |  |
| GetActorCrimePlayerEnemy |  | 0x11CB | 0x005D9590 |  |  |
| GetActorFactionPlayerEnemy |  | 0x11CC | 0x005D95B0 |  |  |
| GetActorsInHigh |  | 0x122D | 0x005DC5C0 |  |  |
| GetActorValue | GetAV | 0x100E | 0x005BD8A0 | Actor Value | Get an actor value. [player.getav luck] |
| GetActorValueInfo | GetAVInfo | 0x01B1 | 0x005BD960 | Actor Value | Get detailed an actor value info. [player.getav luck] |
| GetBaseActorValue | GetBaseAV | 0x1115 | 0x005BE6E0 | Actor Value | Get a base actor value. [player.getbaseav luck] |
| GetClassDefaultMatch |  | 0x10E5 | 0x005D4A40 |  |  |
| GetCombatTarget |  | 0x10E8 | 0x005CE480 |  |  |
| GetCrime |  | 0x107A | 0x005CC2F0 | Actor, [Crime Type (optional)] |  |
| GetCrimeKnown |  | 0x1077 | 0x005CC240 | Crime Type, Criminal, Victim |  |
| GetCurrentAIPackage |  | 0x106E | 0x005CB850 |  |  |
| GetCurrentAIProcedure |  | 0x108F | 0x005CC400 |  |  |
| GetDead |  | 0x102E | 0x005C6A50 |  |  |
| GetDeadCount |  | 0x1054 | 0x005C85C0 | Actor Base |  |
| GetDetected |  | 0x102D | 0x005C69F0 | Actor |  |
| GetDetectionLevel |  | 0x10B4 | 0x005CD990 | Actor |  |
| GetDialogueEmotion |  | 0x11B3 | 0x005D8600 |  |  |
| GetDialogueEmotionValue |  | 0x11B4 | 0x005D8620 |  |  |
| GetDisabled |  | 0x1023 | 0x005C48C0 |  |  |
| GetDisposition |  | 0x104C | 0x005C8450 | Actor |  |
| GetFactionCombatReaction |  | 0x119B | 0x005D75A0 | Faction, Faction |  |
| GetFactionRank |  | 0x1049 | 0x005C7E00 | Faction |  |
| GetFactionRankDifference |  | 0x103C | 0x005C72E0 | Faction, Actor |  |
| GetFactionReaction |  | 0x10A7 | 0x005C7FD0 | Faction, Faction |  |
| GetFactionRelation |  | 0x11C2 | 0x005D9270 | Actor |  |
| GetForceHitReaction |  | 0x1259 | 0x005DDA70 |  |  |
| GetHeadingAngle |  | 0x1063 | 0x005CB050 | ObjectReferenceID |  |
| GetIdleDoneOnce |  | 0x113E | 0x005D2630 |  |  |
| GetIgnoreCrime |  | 0x10C0 | 0x005DB3D0 |  |  |
| GetIgnoreFriendlyHits | gifh | 0x1152 | 0x005D3DC0 |  | See if an actor is ignoring friendly hits |
| GetInFaction |  | 0x1047 | 0x005C79D0 | Faction |  |
| GetIsAlerted |  | 0x105B | 0x005C9700 |  |  |
| GetIsClass |  | 0x1044 | 0x005C7730 | Class |  |
| GetIsClassDefault |  | 0x10E4 | 0x005D4A40 | Class |  |
| GetIsCreature |  | 0x1040 | 0x005C74B0 |  |  |
| GetIsCreatureType |  | 0x11B6 | 0x005C78F0 | Integer |  |
| GetIsCurrentPackage |  | 0x10A1 | 0x005CD440 | Package |  |
| GetIsGhost |  | 0x10ED | 0x005CFF90 |  | Returns 1 if the actor is acting as a 'ghost'. |
| GetIsPlayableRace |  | 0x10FE | 0x005C79B0 |  |  |
| GetIsRace |  | 0x1045 | 0x005C7890 | Race |  |
| GetIsVoiceType |  | 0x11AB | 0x005C4A10 | VoiceType |  |
| GetKillingBlowLimb |  | 0x11F0 | 0x005BE830 |  | Which BGSBodyPart::LIMB_ENUM received the killing blow |
| GetKnockedState |  | 0x106B | 0x005CB780 |  |  |
| GetMajorCrimeCount |  | 0x1075 | 0x005D94E0 |  |  |
| GetMinorCrimeCount |  | 0x1074 | 0x005D94C0 |  |  |
| GetPackageTarget |  | 0x10E9 | 0x005CE520 |  |  |
| GetPCEnemyofFaction |  | 0x10C5 | 0x005CE130 | Faction |  |
| GetPCFactionAttack |  | 0x10C7 | 0x005CE200 | Faction |  |
| GetPCFactionMurder |  | 0x10C3 | 0x005CE060 | Faction |  |
| GetPCInFaction |  | 0x1084 | 0x005C7B50 | Faction |  |
| GetPCIsClass |  | 0x1081 | 0x005C7A30 | Class |  |
| GetPCIsRace |  | 0x1082 | 0x005C7A90 | Race |  |
| GetPermanentActorValue | GetPermAV | 0x11EF | 0x005BD900 | Actor Value | Get an actor value ignoring temporary modifiers. [player.getav luck] |
| GetPlayerTeammate |  | 0x11C6 | 0x005D93F0 |  |  |
| GetPlayerTeammateCount |  | 0x11C7 | 0x005D9410 |  |  |
| GetRestrained |  | 0x10F4 | 0x005D09C0 |  | Returns 1 if is restrained. |
| GetScale |  | 0x1018 | 0x005C1B60 |  |  |
| GetSitting |  | 0x109F | 0x005C6E30 |  |  |
| GetSleeping |  | 0x1031 | 0x005C6E10 |  |  |
| GetTalkedToPC |  | 0x1032 | 0x005C6F30 |  |  |
| GetTalkedToPCParam |  | 0x10AC | 0x005C6F50 | Actor |  |
| GetTimeDead |  | 0x1169 | 0x005D4B40 |  |  |
| GetTrespassWarningLevel |  | 0x1090 | 0x005CC430 |  |  |
| GetUnconscious |  | 0x10F2 | 0x005D0900 |  | Returns 1 if is unconscious. |
| HairTint |  | 0x014C | 0x005C0300 | Integer, Integer, Integer | 3 ints, RGB |
| HasFriendDisposition |  | 0x1193 | 0x005BE850 |  |  |
| IgnoreCrime |  | 0x10AB | 0x005DB3F0 | Integer |  |
| IsActor |  | 0x1161 | 0x005D4AA0 |  |  |
| IsActorAVictim |  | 0x113A | 0x005D2610 |  |  |
| IsActorDetected |  | 0x10B5 | 0x005CDA20 |  |  |
| IsActorEvil |  | 0x1139 | 0x005D25F0 |  |  |
| IsActorRefEssential |  | 0x1272 | 0x005DFC70 |  | Is an actor reference essential |
| IsActorsAIOff |  | 0x112F | 0x005BBEC0 |  |  |
| IsActorTalkingThroughActivator |  | 0x11AE | 0x005D8300 |  |  |
| IsActorUsingATorch |  | 0x1132 | 0x005D1170 |  |  |
| IsCombatTarget |  | 0x1203 | 0x005DB4E0 | Actor |  |
| IsContinuingPackagePCNear |  | 0x1096 | 0x005CC4C0 |  |  |
| IsEssential |  | 0x1162 | 0x005D4A50 |  |  |
| IsGreetingPlayer |  | 0x107B | 0x005DB3B0 |  |  |
| IsIdlePlaying |  | 0x1070 | 0x005CB8B0 |  |  |
| IsInCombat |  | 0x1121 | 0x005D1A90 |  |  |
| IsKiller |  | 0x1199 | 0x005D74E0 | Actor |  |
| IsKillerObject |  | 0x119A | 0x005D7540 | Form List |  |
| IsLastIdlePlayed |  | 0x11C3 | 0x005D92E0 | Idle Form |  |
| IsLimbGone |  | 0x118E | 0x005BE760 | Integer, [Integer (Optional)] | Is BGSBodyPart::LIMB_ENUM been dismembered |
| IsTalking |  | 0x108D | 0x005CC3A0 |  |  |
| IsTalkingActivatorActor |  | 0x1172 | 0x005D4D30 | Actor |  |
| IsTrespassing |  | 0x1091 | 0x005CC460 |  |  |
| KillActor | kill | 0x108B | 0x005BE2A0 | [Actor (optional)], [Integer (Optional)], [Integer (Optional)] |  |
| KillAllActors | killall | 0x113F | 0x005BE4F0 | [Actor (optional)] |  |
| MatchRace |  | 0x11E5 | 0x005DA810 | Actor |  |
| ModActorValue | ModAV | 0x1010 | 0x005BDE40 | Actor Value, Amount | Modify an actor value. [player.modav luck, -10] |
| ModDisposition |  | 0x1053 | 0x005C8510 | Actor, Value |  |
| ModFactionRank |  | 0x108A | 0x005C7F10 | Faction, Value |  |
| ModFactionReaction |  | 0x10A9 | 0x005C82C0 | Faction, Faction, Value |  |
| ModScale |  | 0x113D | 0x005C1C40 | Float | Modify the scale of an object |
| MoveToMarker | MoveTo | 0x109E | 0x005CCF50 | ObjectReferenceID, [Float (Optional)], [Float (Optional)], [Float (Optional)] |  |
| MoveToMarkerWithFade | MoveToFade | 0x124F | 0x005CD0E0 | ObjectReferenceID, [Float (Optional)], [Float (Optional)], [Float (Optional)] |  |
| MoveToQuestTarget | movetoqt | 0x0157 | 0x005CD330 | [Integer (Optional)] | Move player to current quest target (optional param: target number). |
| OpenTeammateContainer |  | 0x11C8 | 0x005D9430 | [Integer (Optional)] |  |
| PickIdle |  | 0x1064 | 0x005CB0C0 |  |  |
| PlaceAtMe |  | 0x1025 | 0x005C4A70 | ObjectID, [Count], [Distance], [Direction] |  |
| PlaceAtMeHealthPercent |  | 0x11BD | 0x005D90A0 | ObjectID, Health Percent, [Count], [Distance], [Direction] |  |
| PlaceLeveledActorAtMe |  | 0x11D1 | 0x005D9810 | ObjectID, [LevelModifier], [ForcedZone] |  |
| PlayGroup |  | 0x1013 | 0x005C0DF0 | Animation Group, Flags | IE: PlayGroup SEQNAME 1 |
| PlayIdle |  | 0x1190 | 0x005CB2D0 | String | Play this idle on the current actor. |
| PrintNPCDialog | pdialog | 0x0158 | 0x005B5D20 |  | Prints NPC dialog |
| PushActorAway |  | 0x118A | 0x005D6B60 | ObjectReferenceID, Integer |  |
| RemoveFromAllFactions |  | 0x1214 | 0x005C8340 |  |  |
| RemoveFromFaction | Removefac | 0x1180 | 0x005D5420 | Faction |  |
| RemoveScriptPackage |  | 0x1098 | 0x005CC7C0 |  |  |
| ResetAI |  | 0x11FA | 0x005C9530 |  |  |
| ResetDialogueFlags | rdf | 0x01AF | 0x005D8930 |  | Debug resets SayOnce, TalkedToPc, etc. |
| RestoreActorValue | RestoreAV | 0x1182 | 0x005BE080 | Actor Value, Amount | Restore an actor value. |
| ResurrectActor | resurrect | 0x108C | 0x005BE5E0 | [Integer (Optional)] |  |
| SameFaction |  | 0x102A | 0x005C6840 | Actor |  |
| SameFactionAsPC |  | 0x1085 | 0x005C6960 |  |  |
| SameRace |  | 0x102B | 0x005C68A0 | Actor |  |
| SameRaceAsPC |  | 0x1086 | 0x005C6990 |  |  |
| Say |  | 0x1033 | 0x005C8A50 | Topic, [Integer (Optional)], [Actor Base], [Integer (Optional)], [Integer (Optional)] |  |
| SayTo |  | 0x1034 | 0x005C9100 | Actor, Topic, [Integer (Optional)], [Integer (Optional)] |  |
| SendTrespassAlarm |  | 0x115C | 0x005D47E0 | Actor |  |
| SetActorAlpha | SAA | 0x1129 | 0x005D23D0 | Float |  |
| SetActorFullName |  | 0x111C | 0x005D1920 | Message |  |
| SetActorRefEssential |  | 0x1273 | 0x005DFD30 | Integer | Set actor reference to essential |
| SetActorRefraction | sar | 0x1154 | 0x005D3F10 | Float |  |
| SetActorsAI |  | 0x118B | 0x005D6A60 | Integer |  |
| SetActorValue | SetAV | 0x100F | 0x005BDCD0 | Actor Value, Amount | Set an actor value. [player.setav luck, 75] |
| SetAlert |  | 0x105A | 0x005C9670 | Integer |  |
| SetAlly |  | 0x1079 | 0x005C8120 | Faction, Faction, [Value(Optional)], [Value(Optional)] |  |
| SetAngle |  | 0x1009 | 0x005C09C0 | Axis, Float |  |
| SetClass |  | 0x10F0 | 0x005D06A0 | Class |  |
| SetCombatActionCost | scc | 0x0197 | 0x005D5780 | String, [Float(optional)] | Sets the cost on a combat action |
| SetCombatStyle | setcs | 0x10B1 | 0x005CD650 | [Combat Style (optional)] |  |
| SetDisposition | SetDisp | 0x1184 | 0x005D54A0 | Actor, Value | Sets the dispostion with modifiers |
| SetEnemy |  | 0x1078 | 0x005C81F0 | Faction, Faction, [Value(Optional)], [Value(Optional)] |  |
| SetEssential |  | 0x1003 | 0x005CD870 | Actor Base, [Integer (Optional)] |  |
| SetFactionRank |  | 0x1089 | 0x005C7E60 | Faction, Value |  |
| SetFactionReaction |  | 0x10A8 | 0x005C80A0 | Faction, Faction, Value |  |
| SetGhost |  | 0x10EC | 0x005CFFB0 | Integer | A value of 1 will make the NPC act as a 'ghost'. |
| SetIgnoreFriendlyHits | sifh | 0x1151 | 0x005D3D50 | Integer | Set whether an actor should ignore friendly hits (0-no, 1-yes) |
| SetNPCRadio | snr | 0x11C4 | 0x005D8100 | Integer, ObjectReferenceID | Enable/Disable NPC radio playback: 0-Off, 1-On  |
| SetPCEnemyofFaction |  | 0x10C6 | 0x005CE190 | Faction, Value |  |
| SetPCFactionAttack |  | 0x10C8 | 0x005CE260 | Faction, Value |  |
| SetPCFactionMurder |  | 0x10C4 | 0x005CE0C0 | Faction, Value |  |
| SetPlayerTeammate |  | 0x11C5 | 0x005D9370 | Integer |  |
| SetPos |  | 0x1007 | 0x005C05F0 | Axis, Float |  |
| SetRestrained |  | 0x10F3 | 0x005D0920 | Integer | A value of 1 will be restrained. |
| SetScale |  | 0x113C | 0x005C1B80 | Float | Set the scale of an object |
| SetTalkingActivatorActor |  | 0x1171 | 0x005D4CC0 | [Actor (optional)] |  |
| SetTaskThreadSleep |  | 0x01C8 | 0x005DE3A0 | Integer | Sets the task thread sleep value (-1 to disable). |
| SetTaskThreadUpdateSleep |  | 0x01C9 | 0x005DE420 | Integer | Sets the task thread update sleep value (-1 to disable). |
| SetUnconscious |  | 0x10F1 | 0x005D0760 | Integer | A value of 1 will be unconscious. |
| SetZoneRespawns |  | 0x11EA | 0x005DAB90 | EncounterZone, Integer |  |
| ShowClassMenu |  | 0x10D9 | 0x005D4A40 |  |  |
| ShowHeadTrackTarget | SHeadT | 0x0164 | 0x005BC310 |  | Show the head track target if set from look function |
| ShowRaceMenu |  | 0x10DA | 0x005CEDF0 |  |  |
| ShowWhoDetectsPlayer | SWDP | 0x0174 | 0x005B5CC0 |  |  Show who detects the player |
| StartCombat |  | 0x1016 | 0x005C1750 | Actor |  |
| StartConversation |  | 0x1056 | 0x005C8740 | TESObjectREFR, [Topic], [TESObjectREFR], [TESObjectREFR], [Integer (Optional)], [Integer (Optional)] | Start a conversation [Bob.StartConversation Joe, SecretTopic] |
| StartRadioConversation |  | 0x11D6 | 0x005D82A0 | [Topic] |  |
| StopCombat |  | 0x1017 | 0x005C1A50 |  |  |
| StopCombatAlarmOnActor | SCAOnActor | 0x1101 | 0x005C1B00 |  |  |
| TestRaceSexTerimnal | trst | 0x01B6 | 0x005D9350 |  | Test race/sex menu rendered terminal |
| ToggleActorMover | tam | 0x01BA | 0x005D4A40 |  | Toggles actor movement through pathing system |
| ToggleActorsAI |  | 0x112E | 0x005BBE10 |  |  |
| ToggleAI | TAI | 0x0106 | 0x005BBF70 | [Actor (optional)] |  |
| ToggleAiSchedules | TAIS | 0x0133 | 0x005BC580 |  |  |
| ToggleCombatAI | tcai | 0x0175 | 0x005BC0D0 |  | Toggles ALL Combat AI |
| ToggleCombatDebug | tcd | 0x0198 | 0x005D5850 | [String] | Toggles combat debug info |
| ToggleCombatStats | TCS | 0x0104 | 0x005B5B90 |  |  |
| ToggleConversations | TCONV | 0x013C | 0x005B9100 |  | Toggle conversation stats |
| ToggleDetection | TDETECT | 0x012E | 0x005BBDA0 |  |  |
| ToggleDetectionStats | tds | 0x015F | 0x005B98A0 | [Actor (optional)] | Show the detection stats of the current seletected Ref. |
| ToggleEmotions | temo | 0x0146 | 0x005B7420 |  | Toggle NPC facial emotions. |
| ToggleHighProcess | THIGHPROCESS | 0x012F | 0x005BC3B0 |  |  |
| ToggleLowProcess | TLOWPROCESS | 0x0130 | 0x005BC430 |  |  |
| ToggleMiddleHighProcess | TMHIGHPROCESS | 0x0132 | 0x005BC510 |  |  |
| ToggleMiddleLowProcess | TMLOWPROCESS | 0x0131 | 0x005BC4A0 |  |  |
| TogglePathingInfoFunction | TPI | 0x019A | 0x005BD3C0 |  | Toggle pathing information. |
| TogglePathLine | TPL | 0x0118 | 0x005D4A40 | [String] | Toggle path display. |
| ToggleRagdollAnim | tra | 0x01A8 | 0x005BA560 |  | Toggles Ragdoll Anim system |
