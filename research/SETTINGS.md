# NPC settings

701 game settings (GMST) and INI settings that touch NPCs. INI settings carry their section after the colon (`bUseThreadedAI:General` goes under `[General]` in FalloutNV.ini / FalloutCustom.ini). `Used by` counts the engine functions that read the setting; the CSV lists their addresses.

| Setting | Default | Used by | Address |
|---|---|---|---|
| bActorLookWithHavok:General | False | 1 | 0x011DF93C |
| bActorSelfShadowing:Display | False | 3 | 0x011C7664 |
| bAllow20HairShader:Display | True | 2 | 0x011C73A4 |
| bBackgroundCellLoads:BackgroundLoad | True | 2 | 0x011C9670 |
| bBackgroundNavmeshUpdate:Pathfinding | True | 2 | 0x011D71A0 |
| bBackgroundPathing:Pathfinding | True | 2 | 0x011D77CC |
| bCheckCellOffsetsOnInit:General | False | 1 | 0x011CA63C |
| bCreateShaderPackage:General | False | 2 | 0x011C7610 |
| bCrossHair:GamePlay | True | 3 | 0x011D8A38 |
| bCurrentCellOnly:Landscape | False | 1 | 0x011C9F60 |
| bDialogueSubtitles:GamePlay | True | 3 | 0x011D8934 |
| bDisableCombatDialogue:Combat | False | 2 | 0x011F1764 |
| bDisableCombatGroupStrategies:Combat | True | 2 | 0x011F18D8 |
| bDisableHeadTracking:HeadTracking | False | 3 | 0x011DF6D0 |
| bDisableNPCAttacks:Combat | False | 2 | 0x011DF6C4 |
| bDisplayMissingContentDialogue:SaveGame | True | 2 | 0x011DE248 |
| bDoActorShadows:Display | True | 2 | 0x011C7368 |
| bDrawPathBounds:Pathfinding | False | 1 | 0x011D846C |
| bEncounterZoneTargetRestrict:Combat | True | 4 | 0x011F1840 |
| bFaceGenTexturing:General | True | 4 | 0x011CB99C |
| bFixAIPackagesOnLoad:General | False | 2 | 0x011C5348 |
| bForceNPCsUseAmmo:Combat | False | 2 | 0x011C94D0 |
| bGlobalNavMeshCheck:NavMeshGeneration | False | 2 | 0x011D6CA8 |
| bLoadBackgroundFaceGen:BackgroundLoad | False | 1 | 0x011D5A24 |
| bLoadFaceGenHeadEGTFiles:General | False | 3 | 0x011D5ADC |
| bPlayHitLocationIdles:Combat | True | 2 | 0x011DF760 |
| bPreCullActors:General | True | 2 | 0x011DED80 |
| bPreemptivelyUnloadCells:General | False | 4 | 0x011C3D40 |
| bRagdollAnim:RagdollAnim | True | 3 | 0x01267C24 |
| bRagdollFeedback:RagdollAnim | True | 1 | 0x01267C54 |
| bRebuildPathIfSmootherFailed:Pathfinding | True | 1 | 0x011D7428 |
| bRigidBodyController:FootIK | True | 1 | 0x01267E1C |
| bRunActorMovementDuringRendering:General | True | 3 | 0x011DFB88 |
| bRunDetectionDuringRendering:General | True | 3 | 0x011DFC70 |
| bRunMiddleLowLevelProcess:General | True | 1 | 0x011E0E4C |
| bSelectedPathDrawAvoidNodes:Pathfinding | False | 1 | 0x011D6E40 |
| bTaskletActorAnimMovementUpdates:General | True | 2 | 0x011F126C |
| bTaskletActorHavokSync:General | True | 2 | 0x011DF214 |
| bTaskletActorSceneGraphUpdates:General | False | 2 | 0x011F1260 |
| bTaskletCellTransformsUpdate:General | True | 3 | 0x011DF1B8 |
| bTrackAllDeaths:General | False | 2 | 0x011DF690 |
| bUseActorAvoidance:Pathfinding | True | 2 | 0x011F2BB8 |
| bUseFaceGenHeads:General | True | 3 | 0x011D5A44 |
| bUseFaceGenLOD:LOD | False | 2 | 0x011D5A5C |
| bUseFartherCheckForAvoidance:Pathfinding | False | 1 | 0x011F2BE0 |
| bUseMovementBlockedPackage:General | False | 2 | 0x011DF6B0 |
| bUseMultiThreadedFaceGen:BackgroundLoad | True | 2 | 0x011D5A10 |
| bUseObstacleAvoidance:Pathfinding | True | 8 | 0x011D73E4 |
| bUseOldPathSmoothing:Pathfinding | False | 2 | 0x011D7434 |
| bUsePathSmoothing:Pathfinding | True | 1 | 0x011D73F0 |
| bUseThreadedAI:General | False | 3 | 0x011DFB68 |
| fActorAlertSoundTimer | 5.0 | 2 | 0x011CD8D8 |
| fActorAnimZAdjust | 1.8 | 1 | 0x011D0418 |
| fActorArmorDesirabilityDamageMult | 0.5 | 1 | 0x011D0718 |
| fActorArmorDesirabilitySkillMult | 10.0 | 1 | 0x011D0814 |
| fActorLODDefault:LOD | 6.5 | 2 | 0x011DAC38 |
| fActorLODMax:LOD | 15.0 | 2 | 0x011DAAF4 |
| fActorLODMin:LOD | 2.0 | 2 | 0x011DAB1C |
| fActorLookForce | 500.0 | 1 | 0x011D0B78 |
| fActorLuckSkillMult | 0.4 | 1 | 0x011D123C |
| fActorStrengthEncumbranceMult | 5.0 | 1 | 0x011D01BC |
| fActorSwimBreathBase | 10.0 | 2 | 0x011D0868 |
| fActorSwimBreathDamage | 0.2 | 2 | 0x011D117C |
| fActorSwimBreathMult | 0.5 | 2 | 0x011D0E28 |
| fActorTeleportFadeSeconds | 0.5 | 2 | 0x011CDAB8 |
| fActorTurnAnimMinTime | 0.3 | 3 | 0x011CD294 |
| fActorWeaponDesirabilityDamageMult | 0.5 | 1 | 0x011D0724 |
| fActorWeaponDesirabilitySkillMult | 10.0 | 1 | 0x011D028C |
| fAIAcquireObjectDistance | 4000.0 | 8 | 0x011CDEBC |
| fAiAcquireStealBase |  | 1 | 0x011CD738 |
| fAiAcquireStealMult | -1.0 | 1 | 0x011CCFCC |
| fAIAwareofPlayerTimer | 5.0 | 2 | 0x011CD210 |
| fAIBestHeadTrackDistance | 500.0 | 2 | 0x011CD114 |
| fAICombatFleeScoreThreshold | 10.0 | 1 | 0x011CF050 |
| fAICombatNoAreaEffectAllyDistance | 350.0 | 1 | 0x011CFCE0 |
| fAICombatNoTargetLOSPriorityMult |  | 1 | 0x011CF730 |
| fAICombatSlopeDifference | 48.0 | 2 | 0x011CE4A0 |
| fAICombatTargetUnreachablePriorityMult | 0.25 | 1 | 0x011CE1AC |
| fAICombatTurnSpeedScale:Pathfinding | 2.5 | 4 | 0x011F2AC4 |
| fAICombatUnreachableTargetPriorityMult | 0.9 | 1 | 0x011CEDDC |
| fAIConversationExploreTime | 0.25 | 2 | 0x011CD968 |
| fAIDefaultSpeechMult | 0.05 | 3 | 0x011CD0BC |
| fAIDodgeDecisionBase | 10.0 | 2 | 0x011CF8F8 |
| fAIDodgeFavorLeftRightMult | 2.0 | 2 | 0x011CF288 |
| fAIDodgeVerticalRangedAttackMult | 0.1 | 1 | 0x011CF558 |
| fAIDodgeWalkChance | 75.0 | 3 | 0x011CE380 |
| fAIEnergyLevelBase |  | 2 | 0x011CD550 |
| fAIEngergyLevelMult |  | 2 | 0x011CD7F0 |
| fAIEscortHysteresisWidth | 50.0 | 2 | 0x011CD1C8 |
| fAIEscortWaitDistanceExterior | 2.0 | 8 | 0x011CD82C |
| fAIEscortWaitDistanceInterior | 512.0 | 8 | 0x011CDBAC |
| fAIExplosiveWeaponDamageMult |  | 1 | 0x011CE894 |
| fAIExplosiveWeaponRangeMult |  | 1 | 0x011CF5E8 |
| fAIExteriorSpectatorDetection | 1000.0 | 3 | 0x011CDFE4 |
| fAIExteriorSpectatorDistance | 450.0 | 4 | 0x011CD990 |
| fAIFaceTargetAnimationAngle | 35.0 | 1 | 0x011CE17C |
| fAIFindBedChairsDistance | 8000.0 | 2 | 0x011CD24C |
| fAIFleeConfBase | 40.0 | 1 | 0x011CF1EC |
| fAIFleeConfMult | -0.5 | 1 | 0x011CF8E0 |
| fAIFleeHealthMult | 20.0 | 1 | 0x011CF5C4 |
| fAIFleeSuccessTimeout | 120.0 | 1 | 0x011CEAF0 |
| fAIFurnitureDestinationRadius | 5.0 | 2 | 0x011CDD0C |
| fAIGreetingTimer | 20.0 | 3 | 0x011CD450 |
| fAIHoldDefaultHeadTrackTimer | 10.0 | 6 | 0x011CDBB8 |
| fAIIdleAnimationDistance | 2000.0 | 3 | 0x011CD674 |
| fAIIdleWaitTime |  | 3 | 0x011CDD30 |
| fAIInteriorHeadTrackMult | 0.5 | 1 | 0x011CD920 |
| fAIInteriorSpectatorDetection | 600.0 | 2 | 0x011CDDB8 |
| fAIInteriorSpectatorDistance | 200.0 | 2 | 0x011CD814 |
| fAIMagicSpellMult | 3.0 | 1 | 0x011CEB14 |
| fAIMagicTimer | 3.0 | 1 | 0x011CF4A4 |
| fAIMaxHeadTrackDistance | 400.0 | 3 | 0x011CD938 |
| fAIMaxHeadTrackDistanceFromPC | 2000.0 | 4 | 0x011CD2F4 |
| fAIMaxSmileDistance | 200.0 | 2 | 0x011CD750 |
| fAIMaxWanderTime | 100.0 | 2 | 0x011CDB0C |
| fAIMeleeArmorMult |  | 1 | 0x011CE29C |
| fAIMeleeHandMult | 1.3 | 2 | 0x011CEC70 |
| fAIMeleeWeaponMult | 2.0 | 2 | 0x011CE448 |
| fAIMinGreetingDistance | 150.0 | 2 | 0x011CD414 |
| fAIMoveDistanceToRecalcFollowPath | 300.0 | 8 | 0x011CD950 |
| fAIPowerAttackCreatureChance | 75.0 | 1 | 0x011CF864 |
| fAIPowerAttackFatigueBase | 15.0 | 1 | 0x011CFC44 |
| fAIPowerAttackFatigueMult | -15.0 | 1 | 0x011CF074 |
| fAIPowerAttackKnockdownBonus | 15.0 | 1 | 0x011CF564 |
| fAIPowerAttackNPCChance | 20.0 | 1 | 0x011CF0F0 |
| fAIPowerAttackRecoilBonus | 10.0 | 1 | 0x011CEDA0 |
| fAIPursueDistanceLineOfSight | 2500.0 | 2 | 0x011CD5D4 |
| fAIRadiusToRunDetectionExterior | 2000.0 | 1 | 0x011CD574 |
| fAIRadiusToRunDetectionInterior | 800.0 | 1 | 0x011CDE80 |
| fAIRangedWeaponMult | 5.0 | 1 | 0x011CF344 |
| fAIRangMagicSpellMult | 5.0 | 1 | 0x011CF4D4 |
| fAISocialchanceForConversation | 60.0 | 3 | 0x011CDC04 |
| fAISocialchanceForConversationInterior | 25.0 | 2 | 0x011CD02C |
| fAISocialRadiusToTriggerConversation | 2000.0 | 2 | 0x011CD92C |
| fAISocialRadiusToTriggerConversationInterior | 500.0 | 2 | 0x011CD75C |
| fAISocialTimerForConversationsMax | 30.0 | 4 | 0x011CD038 |
| fAISocialTimerForConversationsMin | 5.0 | 4 | 0x011CD328 |
| fAISpectatorCommentTimer | 20.0 | 2 | 0x011CCFF0 |
| fAISpectatorRememberThreatTimer | 20.0 | 2 | 0x011CD264 |
| fAItalktoNPCtimer | 60.0 | 1 | 0x011CDBE0 |
| fAItalktosameNPCtimer | 120.0 | 5 | 0x011CDCD8 |
| fAITrespassWarningTimer | 10.0 | 3 | 0x011CD2C4 |
| fAITurnSpeedScale:Pathfinding | 1.5 | 4 | 0x011F2AD8 |
| fAIUpdateMovementRestrictionsDistance | 48.0 | 3 | 0x011CF968 |
| fAIUseWeaponDistance | 5000.0 | 2 | 0x011CDD3C |
| fAmbushOverRideRadiusforPlayerDetection | 1000.0 | 2 | 0x011CD55C |
| fAVDDefaultBodyPartCondition | 100.0 | 2 | 0x011CDA70 |
| fAVDNPCFatigueBase | 90.0 | 3 | 0x011CD974 |
| fAVDNPCFatigueEnduranceMult | 20.0 | 3 | 0x011CE018 |
| fAVDNPCFatigueLevelMult | 10.0 | 2 | 0x011CDB54 |
| fAVDNPCHealthEnduranceMult | 5.0 | 3 | 0x011CD544 |
| fAVDNPCHealthEnduranceOffset | -1.0 | 3 | 0x011CD27C |
| fAVDNPCHealthLevelMult | 20.0 | 2 | 0x011CD908 |
| fAVDSkillSneakBase | 4.0 | 1 | 0x011CD820 |
| fAvoidanceAvoidAllRadius:Pathfinding | 100.0 | 3 | 0x011F2B8C |
| fAvoidanceAvoidNodeCost | 2.0 | 2 | 0x011F2B5C |
| fAvoidanceConeAngle:Pathfinding | 45.0 | 2 | 0x011F2BA8 |
| fAvoidanceDefaultWaitTime:Pathfinding | 5.0 | 2 | 0x011F2B74 |
| fAvoidanceDetectionTime:Pathfinding | 0.5 | 2 | 0x011F2B1C |
| fAvoidanceIgnoreMinTime:Pathfinding | 2.5 | 2 | 0x011F2BC4 |
| fAvoidanceIgnoreTime:Pathfinding | 5.0 | 2 | 0x011F2B3C |
| fAvoidanceMinWaitTime:Pathfinding | 0.25 | 3 | 0x011F2B2C |
| fAvoidanceTimeCheck:Pathfinding | 0.75 | 2 | 0x011F2B98 |
| fAvoidanceWiderConeAngle:Pathfinding | 60.0 | 2 | 0x011F2AF8 |
| fBuoyancyMultBody |  | 2 | 0x011D0E64 |
| fCameraCasterFadeSittingRadius:HAVOK | 45.0 | 2 | 0x011CC188 |
| fCharacterControllerMultipleStepSpeed | 25.0 | 3 | 0x011C3CE8 |
| fCharacterDefaultTurningSpeed | 90.0 | 2 | 0x011CD0FC |
| fCheckDeadBodyTimer | 20.0 | 1 | 0x011CDB00 |
| fCombatAbsoluteMaxRangeMult | 1.5 | 2 | 0x011CE87C |
| fCombatAdvanceNormalAttackChance |  | 2 | 0x011CF27C |
| fCombatAvoidThreatsChance | 0.5 | 2 | 0x011CE954 |
| fCombatBetweenAdvanceTimer | 2.0 | 1 | 0x011CE5B8 |
| fCombatBuffMaxTimer | 6.0 | 1 | 0x011CFBC0 |
| fCombatBuffStandoffTimer | 3.0 | 1 | 0x011CFDFC |
| fCombatClusterUpdateTime |  | 1 | 0x011CE708 |
| fCombatCollectAlliesTimer |  | 1 | 0x011CE9A8 |
| fCombatConfidenceModifierMax | 0.5 | 2 | 0x011CF7EC |
| fCombatConfidenceModifierMin | -0.5 | 2 | 0x011CFDCC |
| fCombatCoverMaxRangeMult | 1.5 | 2 | 0x011CE3F0 |
| fCombatCurrentWeaponAbsoluteMaxRangeMult | 1.5 | 2 | 0x011CE4AC |
| fCombatDamageBonusMeleeSneakingMult | 5.0 | 2 | 0x011CEAE0 |
| fCombatDamageBonusSneakingMult |  | 2 | 0x011CF794 |
| fCombatDamageScale | 0.5 | 1 | 0x011CEDC4 |
| fCombatDeadActorHitConeMult | 2.0 | 2 | 0x011CFDA4 |
| fCombatDetectionBufferTime | 10.0 | 5 | 0x011CE9B4 |
| fCombatDetectionDialogueIdleMaxElapsedTime | 10.0 | 3 | 0x011CE35C |
| fCombatDetectionDialogueIdleMinElapsedTime | 3.0 | 3 | 0x011CF24C |
| fCombatDetectionDialogueMaxElapsedTime | 3.0 | 2 | 0x011CFA4C |
| fCombatDetectionDialogueMinElapsedTime |  | 2 | 0x011CF0B0 |
| fCombatDetectionLostTime | 15.0 | 7 | 0x011CE528 |
| fCombatDialogueAttackMaxElapsedTime | 5.0 | 2 | 0x011CE4C8 |
| fCombatDialogueAttackMinElapsedTime |  | 2 | 0x011CFB20 |
| fCombatDialogueAvoidThreatMaxElapsedTime | 5.0 | 2 | 0x011CF898 |
| fCombatDialogueAvoidThreatMinElapsedTime | 3.0 | 2 | 0x011CF858 |
| fCombatDialogueFireExplosiveMaxElapsedTime | 5.0 | 2 | 0x011CFCBC |
| fCombatDialogueFireExplosiveMinElapsedTime |  | 2 | 0x011CED40 |
| fCombatDialogueFleeMaxElapsedTime | 5.0 | 2 | 0x011CE248 |
| fCombatDialogueFleeMinElapsedTime | 3.0 | 2 | 0x011CEBA4 |
| fCombatDisarmedFindBetterWeaponInitialTime |  | 2 | 0x011CE058 |
| fCombatDisarmedFindBetterWeaponTime | 2.5 | 2 | 0x011CE9D8 |
| fCombatDismemberedLimbVelocity | 10.0 | 3 | 0x011CEF14 |
| fCombatDistance | 128.0 | 4 | 0x011CF84C |
| fCombatDistanceMin | 400.0 | 1 | 0x011CEA8C |
| fCombatEnvironmentBloodChance | 0.75 | 2 | 0x011CEF8C |
| fCombatFindBetterWeaponTime | 5.0 | 2 | 0x011CF9F8 |
| fCombatFiringArcStationaryTurnMult | 0.75 | 3 | 0x011CFB84 |
| fCombatFleeBoostConfidenceTargetRadius | 512.0 | 2 | 0x011CE08C |
| fCombatFleeDoorTargetCheckDistance | 128.0 | 2 | 0x011CE2F0 |
| fCombatFleeInitialDoorRestrictChance | 0.75 | 2 | 0x011CF294 |
| fCombatFleeLastDoorRestrictTime | 30.0 | 2 | 0x011CEED8 |
| fCombatFleeMaxAllyDistance | 4096.0 | 2 | 0x011CF020 |
| fCombatFleeMaxCoverDistance | 3072.0 | 2 | 0x011CF8D4 |
| fCombatFleeMaxDoorDistance | 1024.0 | 2 | 0x011CF234 |
| fCombatFleeMinAllyDistance | 1536.0 | 2 | 0x011CE040 |
| fCombatFleeMinCoverDistance | 1536.0 | 2 | 0x011CED34 |
| fCombatFleeNormalDistance | 2048.0 | 2 | 0x011CEA80 |
| fCombatFleeTargetAvoidCost | 5.0 | 2 | 0x011CEB2C |
| fCombatFleeTargetAvoidRadius | 2048.0 | 18 | 0x011CE900 |
| fCombatFleeTargetGatherRadius | 3072.0 | 2 | 0x011CEA50 |
| fCombatFleeUseDoorRestrictTime | 15.0 | 2 | 0x011CEAD4 |
| fCombatFleeWaitTime | 60.0 | 2 | 0x011CE6E4 |
| fCombatFollowRadiusBase | 512.0 | 2 | 0x011CE218 |
| fCombatFollowRadiusMin | 512.0 | 2 | 0x011CEFCC |
| fCombatFollowRadiusMult | 3.0 | 2 | 0x011CEAFC |
| fCombatFollowSneakFollowRadius | 512.0 | 2 | 0x011CF45C |
| fCombatForwardAttackChance | 0.25 | 1 | 0x011CF038 |
| fCombatGiantCreatureReachMult | 2.0 | 2 | 0x011CE484 |
| fCombatGrenadeBounceTimeMax | 5.0 | 1 | 0x011CE814 |
| fCombatGrenadeBounceTimeMin | 0.5 | 1 | 0x011CF174 |
| fCombatGroupCombatStrengthUpdateTime | 2.0 | 2 | 0x011CFE84 |
| fCombatGroupFleeingTargetLostRemoveDistance | 3072.0 | 2 | 0x011CE38C |
| fCombatGroupFleeingTargetLostRemoveDistanceTime | 15.0 | 2 | 0x011CE750 |
| fCombatGroupFleeingTargetLostRemoveTime | 30.0 | 2 | 0x011CE290 |
| fCombatGuardFollowBufferDistance | 384.0 | 3 | 0x011CE7F0 |
| fCombatGuardRadiusMin | 384.0 | 2 | 0x011CEC10 |
| fCombatGuardRadiusMult | 1.5 | 2 | 0x011CE630 |
| fCombatHideFailedTargetDistance | 384.0 | 2 | 0x011CFDE4 |
| fCombatHitConeAngle | 35.0 | 3 | 0x011CFA58 |
| fCombatInTheWayTimer |  | 1 | 0x011CE96C |
| fCombatInventoryUpdateTimer | 5.0 | 2 | 0x011CF660 |
| fCombatIronSightsDistance | 512.0 | 3 | 0x011CEBF8 |
| fCombatIronSightsRangeMult | 5.0 | 2 | 0x011CE5F4 |
| fCombatItemBuffTimer | 45.0 | 2 | 0x011CF480 |
| fCombatItemRestoreTimer | 30.0 | 2 | 0x011CFDD8 |
| fCombatLineOfSightTimer | 0.25 | 1 | 0x011CF450 |
| fCombatLocationTargetRadiusMin | 10.0 | 3 | 0x011CF0D8 |
| fCombatLOSBufferTime | 5.0 | 2 | 0x011CEA98 |
| fCombatLowFleeingTargetHitPercent | 0.25 | 2 | 0x011CE230 |
| fCombatLowMaxAttackDistance | 2048.0 | 2 | 0x011CE820 |
| fCombatLowTargetHitPercent | 0.5 | 2 | 0x011CFBB4 |
| fCombatMaxHoldScore | 30.0 | 3 | 0x011CEA38 |
| fCombatMinEngageDistance | 64.0 | 6 | 0x011CEB98 |
| fCombatMissileImpaleDepth | 12.0 | 3 | 0x011CE1E8 |
| fCombatMissileStickDepth | 10.0 | 2 | 0x011CFC8C |
| fCombatMonitorBuffsTimer | 3.0 | 1 | 0x011CF770 |
| fCombatMoveToActorBufferDistance | 64.0 | 3 | 0x011CF144 |
| fCombatMusicGroupThreatRatioMax | 2.0 | 2 | 0x011CF944 |
| fCombatMusicGroupThreatRatioMin | 0.5 | 2 | 0x011CEE6C |
| fCombatMusicGroupThreatRatioTimer |  | 2 | 0x011CEB44 |
| fCombatMusicNearCombatInnerRadius | 2500.0 | 2 | 0x011CFE5C |
| fCombatMusicNearCombatOuterRadius | 3500.0 | 2 | 0x011CE454 |
| fCombatMusicPlayerCombatStrengthCap | 35000.0 | 1 | 0x011CEBE0 |
| fCombatMusicPlayerNearStrengthMult |  | 2 | 0x011CE72C |
| fCombatMusicPlayerTargetedThreatRatio | 2.0 | 2 | 0x011CE04C |
| fCombatMusicStopTime | 5.0 | 2 | 0x011CFC14 |
| fCombatMusicUpdateTime |  | 2 | 0x011CEEC0 |
| fCombatOverheadHitConeAngle | 40.0 | 2 | 0x011CEB80 |
| fCombatPathingLookAheadDelta | 0.5 | 2 | 0x011CE3FC |
| fCombatPlayerLimbDamageMult | 0.5 | 2 | 0x011CFA40 |
| fCombatProjectileMaxRangeOptimalMult | 0.85 | 2 | 0x011CEAB0 |
| fCombatRadiusMinMult | 0.9 | 2 | 0x011CFB2C |
| fCombatRangedStandoffTimer | 6.0 | 1 | 0x011CE84C |
| fCombatRelativeDamageMod | 100.0 | 1 | 0x011CF540 |
| fCombatRoundAmount | 3.0 | 6 | 0x011CD6CC |
| fCombatSearchAreaUpdateTime | 5.0 | 3 | 0x011CF870 |
| fCombatSearchBufferDistance | 256.0 | 2 | 0x011CE7B0 |
| fCombatSearchCheckDestinationMaxDistance | 512.0 | 2 | 0x011CF3C0 |
| fCombatSearchCheckDestinationMidDistance | 384.0 | 2 | 0x011CF2E0 |
| fCombatSearchCheckDestinationMinDistance | 256.0 | 2 | 0x011CEB68 |
| fCombatSearchCheckDestinationTime |  | 2 | 0x011CECC4 |
| fCombatSearchCheckDoorDistance | 1536.0 | 2 | 0x011CF938 |
| fCombatSearchCheckDoorLowDistance | 4096.0 | 2 | 0x011CEF5C |
| fCombatSearchCheckDoorMovingDistance | 1024.0 | 2 | 0x011CE0F0 |
| fCombatSearchCheckDoorMovingTime | 5.0 | 2 | 0x011CE8F4 |
| fCombatSearchCheckInvestigateInitialTime | 2.0 | 4 | 0x011CE9C0 |
| fCombatSearchCheckInvestigateMaxDistance | 512.0 | 3 | 0x011CF2A0 |
| fCombatSearchCheckInvestigateTime |  | 3 | 0x011CFAD4 |
| fCombatSearchExteriorMaxRadius | 4096.0 | 1 | 0x011CE0CC |
| fCombatSearchExteriorMediumRadius | 2048.0 | 1 | 0x011CE930 |
| fCombatSearchExteriorMinRadius | 1024.0 | 1 | 0x011CEFBC |
| fCombatSearchInteriorMaxRadius | 2048.0 | 1 | 0x011CF6F4 |
| fCombatSearchInteriorMediumRadius | 1024.0 | 1 | 0x011CEEE4 |
| fCombatSearchInteriorMinRadius | 512.0 | 1 | 0x011CF180 |
| fCombatSearchLocationRemoveDistance | 256.0 | 2 | 0x011CF684 |
| fCombatSearchLookTime |  | 1 | 0x011CF02C |
| fCombatSearchSightRadius | 1536.0 | 2 | 0x011CF42C |
| fCombatSearchTargetHiddenMaxTime | 20.0 | 2 | 0x011CF0A4 |
| fCombatSearchTargetHiddenRemoveTime | 10.0 | 2 | 0x011CF3B4 |
| fCombatSearchUpdateTime |  | 2 | 0x011CE43C |
| fCombatSneakAttackBonusMult | 3.0 | 2 | 0x011CE858 |
| fCombatSoundArmorPct | 0.9 | 1 | 0x011CAF70 |
| fCombatSoundFleshPct | 0.8 | 1 | 0x011CAF4C |
| fCombatSoundWeaponPct | 0.85 | 1 | 0x011CAF80 |
| fCombatSpeakAttackChance | 0.1 | 1 | 0x011CEA5C |
| fCombatSpeakHitChance | 0.35 | 2 | 0x011CEE30 |
| fCombatSpeakHitThreshold | 0.1 | 2 | 0x011CF5A0 |
| fCombatSpeakPowerAttackChance | 0.5 | 2 | 0x011CE3D8 |
| fCombatSpeakTauntChance | 0.01 | 1 | 0x011CFDC0 |
| fCombatSplashDamageMaxSpeed | 3000.0 | 2 | 0x011CEBD4 |
| fCombatSplashDamageMinDamage | 20.0 | 2 | 0x011CEB5C |
| fCombatSplashDamageMinRadius | 50.0 | 2 | 0x011CF270 |
| fCombatStaffTimer | 2.0 | 1 | 0x011CE624 |
| fCombatStepAdvanceDistance | 128.0 | 2 | 0x011CEEA8 |
| fCombatStrengthUpdateTime |  | 3 | 0x011CF198 |
| fCombatSweepHitConeAngle | 100.0 | 2 | 0x011CFA04 |
| fCombatTargetLostRemoveDistance | 4096.0 | 2 | 0x011CF3FC |
| fCombatTargetLostRemoveDistanceTime | 60.0 | 2 | 0x011CF368 |
| fCombatTargetLostRemoveTime | 30.0 | 2 | 0x011CE744 |
| fCombatTeammateFollowRadiusBase | 512.0 | 2 | 0x011CE588 |
| fCombatTeammateFollowRadiusMin | 512.0 | 2 | 0x011CE6A8 |
| fCombatTeammateFollowRadiusMult | 3.0 | 2 | 0x011CED7C |
| fCombatThreatAvoidCost |  | 2 | 0x011CEF98 |
| fCombatThreatDangerousObjectHealth | 30.0 | 2 | 0x011CE1B8 |
| fCombatThreatExplosiveObjectThreatTime | 3.0 | 2 | 0x011CEF20 |
| fCombatThreatExtrudeTime | 2.0 | 3 | 0x011CE990 |
| fCombatThreatExtrudeVelocityThreshold | 2.0 | 3 | 0x011CF48C |
| fCombatThreatNegativeExtrudeTime | 0.5 | 1 | 0x011CED0C |
| fCombatThreatProximityExplosionAvoidTime | 10.0 | 2 | 0x011CF764 |
| fCombatThreatRatioUpdateTime | 5.0 | 4 | 0x011CF804 |
| fCombatThreatSignificantScore | 0.05 | 4 | 0x011CFBCC |
| fCombatThreatTimedExplosionLength | 5.0 | 3 | 0x011CEABC |
| fCombatUnarmedCritDamageMult | 0.5 | 2 | 0x011CE57C |
| fCombatUppercutHitConeAngle | 50.0 | 2 | 0x011CFE44 |
| fCombatVulnerabilityMod | 0.1 | 1 | 0x011CE2A8 |
| fCombatYieldRetryTime | 600.0 | 2 | 0x011CEDB8 |
| fCombatYieldTime | 10.0 | 3 | 0x011CE3A8 |
| fCreatureCalcCombat | 2.0 | 2 | 0x011CB5B4 |
| fCreatureCalcDamage |  | 2 | 0x011CB58C |
| fCreatureCalcMagic | 2.0 | 1 | 0x011CB574 |
| fCreatureCalcStealth | 2.0 | 1 | 0x011CB5D4 |
| fCreatureCombatTurnSpeedScale:Pathfinding | 1.25 | 4 | 0x011F2B10 |
| fCreatureDefaultTurningSpeed | 45.0 | 2 | 0x011CFABC |
| fCreatureRadioMax:Audio | 2000.0 | 2 | 0x011DD62C |
| fCreatureRadioMin:Audio | 200.0 | 2 | 0x011DD5B0 |
| fCreatureTurnSpeedScale:Pathfinding | 1.25 | 4 | 0x011F2C10 |
| fCrimeAlarmRespMult | 1.7 | 1 | 0x011CDC1C |
| fCrimeDispAttack | -10.0 | 2 | 0x011D13E0 |
| fCrimeDispMurder | -50.0 | 1 | 0x011D0C18 |
| fCrimeDispPersonal | 2.0 | 1 | 0x011D0AC0 |
| fCrimeDispPickpocket | -25.0 | 1 | 0x011D1488 |
| fCrimeDispSteal | -0.5 | 1 | 0x011D04FC |
| fCrimeDispTresspass | -20.0 | 1 | 0x011D0688 |
| fCrimeGoldSteal | 0.5 | 1 | 0x011D04C0 |
| fCrimeSoundBase |  | 1 | 0x011CD95C |
| fCrimeSoundMult |  | 1 | 0x011CD914 |
| fDamageSneakAttackMult | 4.0 | 1 | 0x011CEFD8 |
| fDeathForceDamageMax | 50.0 | 2 | 0x011CFE74 |
| fDeathForceDamageMin |  | 2 | 0x011CF618 |
| fDeathForceForceMax | 85.0 | 2 | 0x011CFB9C |
| fDeathForceForceMin | 35.0 | 3 | 0x011CF724 |
| fDeathForceRangedDamageMax | 10.0 | 3 | 0x011CF624 |
| fDeathForceRangedDamageMin | 0.1 | 2 | 0x011CFD58 |
| fDeathForceRangedForceMax | 40.0 | 2 | 0x011CF950 |
| fDeathForceRangedForceMin | 20.0 | 2 | 0x011CFD04 |
| fDeathSoundMaxDistance | 1000.0 | 2 | 0x011D0F9C |
| fDetectionActionTimer | 1.2 | 2 | 0x011CD4FC |
| fDetectionCommentTimer | 20.0 | 1 | 0x011CD3CC |
| fDetectionEventExpireTime | 10.0 | 2 | 0x011CE558 |
| fDetectionLargeActorSizeMult |  | 2 | 0x011CDEEC |
| fDetectionLargeActorThreshold | 135.0 | 2 | 0x011CD240 |
| fDetectionNightEyeBonus | 3.0 | 2 | 0x011D0F90 |
| fDetectionSneakLightMod |  | 3 | 0x011CDB84 |
| fDetectionTimerSetting | 0.3 | 3 | 0x011D0B08 |
| fDetectionViewCone | 190.0 | 5 | 0x011CD668 |
| fDialogFocalDepthRange | 300.0 | 2 | 0x011D46FC |
| fDialogFocalDepthStrength | 0.65 | 2 | 0x011D318C |
| fDialogHitSoundCooldownMax:Audio | 4.0 | 2 | 0x011DF70C |
| fDialogHitSoundCooldownMin:Audio | 2.0 | 2 | 0x011DF73C |
| fDialogMaxDistance:Audio | 50000.0 | 1 | 0x011F6DB4 |
| fDialogMinDistance:Audio | 70.0 | 1 | 0x011F6DA8 |
| fDialogSpeechDelaySeconds | 2.0 | 5 | 0x011D32C4 |
| fDialogueFadeDecibels:Audio | 6.0 | 1 | 0x011F6E80 |
| fDialogueFadeSecondsIn:Audio | 2.0 | 1 | 0x011F6E8C |
| fDialogueFadeSecondsOut:Audio |  | 1 | 0x011F6E98 |
| fDialogueHeadPitchExaggeration:Audio | 2.0 | 2 | 0x011C6528 |
| fDialogueHeadRollExaggeration:Audio | 2.0 | 2 | 0x011C6534 |
| fDialogueHeadYawExaggeration:Audio | 2.0 | 2 | 0x011C651C |
| fDialogZoomInSeconds | 1.5 | 3 | 0x011D3EE0 |
| fDialogZoomOutSeconds | 0.5 | 2 | 0x011D243C |
| fDispActorCharBase | -30.0 | 1 | 0x011CCFC0 |
| fDispActorCharMult | 10.0 | 1 | 0x011CD384 |
| fDispActorRespBase | -50.0 | 2 | 0x011CD228 |
| fDispActorRespMult |  | 2 | 0x011CDC28 |
| fDistanceExteriorReactCombat | 600.0 | 1 | 0x011CD9D0 |
| fDistanceInteriorReactCombat | 300.0 | 1 | 0x011CD068 |
| fDistanceProjectileExplosionDetection | 400.0 | 1 | 0x011CD798 |
| fDistancetoPlayerforConversations | 3000.0 | 1 | 0x011CD514 |
| fDlgHeadingDegStart:Interface | 13.0 | 2 | 0x011E0B28 |
| fDlgHeadingDegStop:Interface | 0.2 | 2 | 0x011E08C4 |
| fEssentialDeathTime | 10.0 | 2 | 0x011D0700 |
| fExplosiveProjectileBlockedResetTime | 5.0 | 2 | 0x011CF15C |
| fEyeHeadingMaxOffsetEmotionAngry | 0.1 | 2 | 0x011D5750 |
| fEyeHeadingMaxOffsetEmotionFear | 0.5 | 2 | 0x011D58D8 |
| fEyeHeadingMaxOffsetEmotionHappy | 0.2 | 2 | 0x011D5988 |
| fEyeHeadingMaxOffsetEmotionNeutral | 0.2 | 2 | 0x011D5908 |
| fEyeHeadingMaxOffsetEmotionSad | 0.4 | 2 | 0x011D5894 |
| fEyeHeadingMinOffsetEmotionAngry | -0.1 | 2 | 0x011D5968 |
| fEyeHeadingMinOffsetEmotionFear | -0.5 | 2 | 0x011D5868 |
| fEyeHeadingMinOffsetEmotionHappy | -0.2 | 2 | 0x011D5794 |
| fEyeHeadingMinOffsetEmotionNeutral | -0.2 | 2 | 0x011D585C |
| fEyeHeadingMinOffsetEmotionSad | -0.4 | 2 | 0x011D5930 |
| fFightAbleToDetectTimer | 3.0 | 1 | 0x011CDD24 |
| fFirstPersonHandFollowMult | 0.85 | 2 | 0x011CDCB0 |
| fFleeDistanceExterior | 2000.0 | 3 | 0x011CF998 |
| fFleeDistanceInterior | 300.0 | 4 | 0x011CE570 |
| fFleeDoneDistanceExterior | 2500.0 | 2 | 0x011CF70C |
| fFleeDoneDistanceInterior | 600.0 | 2 | 0x011CE6C0 |
| fFleeIsSafeTimer | 30.0 | 3 | 0x011CD348 |
| fFlickerMovement:bLightAttenuation | 8.0 | 2 | 0x011C8FCC |
| fFollowExtraCatchUpSpeedMult | 0.2 | 2 | 0x011CD354 |
| fFollowMatchSpeedZoneWidth | 128.0 | 3 | 0x011CD85C |
| fFollowRunMaxSpeedupMultiplier | 1.25 | 2 | 0x011CD744 |
| fFollowRunMinSlowdownMultiplier | 0.9 | 2 | 0x011CD5F0 |
| fFollowSlowdownZoneWidth | 150.0 | 2 | 0x011CDE74 |
| fFollowSpaceBetweenFollowers | 100.0 | 3 | 0x011CD65C |
| fFollowStopZoneMinMult | 0.5 | 2 | 0x011CD420 |
| fFollowWalkMaxSpeedupMultiplier | 1.5 | 2 | 0x011CD9B4 |
| fFollowWalkMinSlowdownMultiplier | 0.75 | 2 | 0x011CDF9C |
| fFollowWalkZoneMult |  | 2 | 0x011CE00C |
| fGuardPackageAttackRadiusMult | 0.25 | 2 | 0x011CD1F8 |
| fGunSpreadHeadBase |  | 1 | 0x011CFE14 |
| fGunSpreadHeadMult | -1.0 | 1 | 0x011CEC1C |
| fGunSpreadNPCArmBase | 0.5 | 1 | 0x011CE774 |
| fGunSpreadNPCArmMult |  | 1 | 0x011CEA20 |
| fHCSleepDeprivationRate | 0.26 | 2 | 0x011D1440 |
| fHCSleepRestorationMod | 60.0 | 2 | 0x011D0C24 |
| fHealingRateSleepingBase | 2.0 | 2 | 0x011D01FC |
| fHealingRateSleepingMult | 2.0 | 2 | 0x011D1164 |
| fHelloCooldownTime | 30.0 | 2 | 0x011D03A0 |
| fHiPerfNPCTargetLOSTimer:Combat | 0.5 | 1 | 0x011F1A38 |
| fHostileActorExteriorDistance | 3000.0 | 2 | 0x011D0BB4 |
| fHostileActorInteriorDistance | 2000.0 | 2 | 0x011D04B4 |
| fIdleChatterCommentTimer | 5.0 | 4 | 0x011CD008 |
| fIdleChatterCommentTimerMax | 30.0 | 4 | 0x011CD18C |
| fImprovedDetectModifier | 0.25 | 2 | 0x011D031C |
| fINIDetectDoorsForPathingTime:Pathing | 0.5 | 3 | 0x011E029C |
| fItemDetectionTimer | 5.0 | 3 | 0x011D0658 |
| fKarmaDeathPenalty | 1.5 | 1 | 0x011C4EDC |
| fKarmaModKillingEvilActor |  | 2 | 0x011CDED4 |
| fKarmaModKillingVeryEvilActor | 2.0 | 2 | 0x011CD508 |
| fKarmaModMurderingGoodNPC | -50.0 | 2 | 0x011CD7A4 |
| fKarmaModMurderingNonEvilCreature |  | 2 | 0x011CD164 |
| fKarmaModMurderingNonEvilNPC |  | 2 | 0x011CDF6C |
| fKarmaModMurderingVeryGoodNPC | -100.0 | 2 | 0x011CDCA4 |
| fKarmaModStealing | -5.0 | 7 | 0x011CDE20 |
| fLeveledActorMultBoss |  | 1 | 0x011C3A7C |
| fLeveledActorMultEasy | 0.25 | 1 | 0x011C39DC |
| fLeveledActorMultHard | 0.75 | 1 | 0x011C3A10 |
| fLeveledActorMultMedium | 0.5 | 1 | 0x011C39C4 |
| fLeveledLockMult | 1.5 | 2 | 0x011C39B4 |
| fLODActorAvoidanceDistance:General | 500.0 | 3 | 0x011F2BD0 |
| fLODFadeOutActorMultCity:LOD |  | 2 | 0x011DED98 |
| fLODFadeOutActorMultComplex:LOD |  | 2 | 0x011DED8C |
| fLODFadeOutActorMultInterior:LOD |  | 2 | 0x011DECC8 |
| fLODFadeOutMultActors:LOD | 2.5 | 3 | 0x011C3EC0 |
| fLowLevelNPCBaseHealthMult | 0.25 | 1 | 0x011D01B0 |
| fLowPerfCombatantVoiceDistance | 1000.0 | 1 | 0x011F1C94 |
| fLowPerfNPCTargetLOSTimer:Combat |  | 1 | 0x011F1AD4 |
| fMagicResistActorSkillBase |  | 1 | 0x011D1C34 |
| fMagicResistActorSkillMult | -0.0025 | 1 | 0x011D1A20 |
| fMeleeMovementRestrictionsUpdateTime |  | 2 | 0x011CEE60 |
| fMovementNearTargetAvoidCost | 25.0 | 3 | 0x011CF120 |
| fMovementNearTargetAvoidRadius | 64.0 | 3 | 0x011CF4E0 |
| fMovementTargetAvoidCost | 25.0 | 3 | 0x011CFCF8 |
| fMovementTargetAvoidRadius | 512.0 | 2 | 0x011CE648 |
| fMovementTargetAvoidRadiusMult | 1.25 | 2 | 0x011CF380 |
| fMoveSneakMult | 0.6 | 2 | 0x011CFFF4 |
| fMsActorRefCount:BudgetCaps | 0.245 | 1 | 0x011C5A2C |
| fNoticeTextTimePerCharacter | 0.06 | 4 | 0x011D2178 |
| fNPCAttributeHealthMult | 0.5 | 1 | 0x011D0A3C |
| fNPCBaseMagickaMult | 0.2 | 1 | 0x011D07E4 |
| fNPCGeneticVariation | 0.5 | 2 | 0x011CB7A0 |
| fNPCMaxGunWobbleAngle | 5.0 | 3 | 0x011CE034 |
| fObjectWeightPickupDetectionMult |  | 2 | 0x011CDF84 |
| fPathingLargeActorRadius | 80.0 | 10 | 0x011D6EF0 |
| fPathPointTurningSpeed | 10.0 | 1 | 0x011D03F4 |
| fPathPointZDistanceAllowance | 10.0 | 2 | 0x011D09D0 |
| fPerkSneakAttackMarksmanApprenticeMult | 8.0 | 1 | 0x011CE124 |
| fPerkSneakAttackMarksmanExpertMult | 8.0 | 1 | 0x011CED1C |
| fPerkSneakAttackMarksmanJourneymanMult | 8.0 | 1 | 0x011CFBE4 |
| fPerkSneakAttackMarksmanMasterMult | 8.0 | 1 | 0x011CE2D8 |
| fPerkSneakAttackMarksmanNoviceMult | 6.0 | 1 | 0x011CF630 |
| fPerkSneakAttackMeleeApprenticeMult | 6.0 | 1 | 0x011CF12C |
| fPerkSneakAttackMeleeExpertMult | 6.0 | 1 | 0x011CFDB0 |
| fPerkSneakAttackMeleeJourneymanMult | 6.0 | 1 | 0x011CE408 |
| fPerkSneakAttackMeleeMasterMult | 6.0 | 1 | 0x011CE254 |
| fPerkSneakAttackMeleeNoviceMult | 4.0 | 1 | 0x011CEA08 |
| fPickPocketActorSkillBase |  | 2 | 0x011CDEF8 |
| fPickPocketActorSkillMult |  | 2 | 0x011CD8E4 |
| fPlayerCharacterTurnMult:Controls | 0.02 | 3 | 0x011E0964 |
| fPlayerDeathReloadTime | 5.0 | 2 | 0x011CD62C |
| fPlayerDetectActorValue | -35.0 | 3 | 0x011D13C8 |
| fPlayerTargetCombatDistance | 3000.0 | 1 | 0x011CF444 |
| fPOVSmootherAvoidNodeCost:Pathfinding | 7.0 | 2 | 0x011D7084 |
| fQuestCinematicCharacterFadeIn | 2.0 | 2 | 0x011D2238 |
| fQuestCinematicCharacterFadeInDelay | 0.1 | 2 | 0x011D2688 |
| fQuestCinematicCharacterFadeOut | 2.0 | 2 | 0x011D4F30 |
| fQuestCinematicCharacterRemain | 4.0 | 2 | 0x011D4D14 |
| fRadiationAvoidThreshold | 50.0 | 2 | 0x011CD874 |
| fRadiationResistanceAvoidLevel | 10.0 | 2 | 0x011CDCC8 |
| fRadioDialogMute:Audio | 0.5 | 1 | 0x011DD5A4 |
| fRemoteCombatMissedAttack | 4.0 | 1 | 0x011CDB78 |
| fRemoveExcessComplexDeadTime | 2.5 | 3 | 0x011D1530 |
| fRemoveExcessDeadTime | 10.0 | 2 | 0x011D0A84 |
| fReputationMajorCrimeNeg | 30.0 | 2 | 0x011CBAF8 |
| fReputationMinorCrimeNeg | 2.0 | 2 | 0x011CBB1C |
| fSandboxBreakfastMax | 9.0 | 1 | 0x011CD99C |
| fSandboxBreakfastMin | 6.0 | 1 | 0x011CDEB0 |
| fSandboxDinnerMax | 20.0 | 1 | 0x011CD2A0 |
| fSandboxDinnerMin | 17.0 | 1 | 0x011CD0D8 |
| fSandboxDurationBase | 10.0 | 2 | 0x011CDC74 |
| fSandboxDurationMultEating | 0.75 | 1 | 0x011CD390 |
| fSandboxDurationMultFurniture | 2.0 | 1 | 0x011CDF90 |
| fSandboxDurationMultIdleMarker |  | 1 | 0x011CD598 |
| fSandboxDurationMultWandering | 0.5 | 1 | 0x011CD944 |
| fSandboxDurationRangeMult | 0.25 | 2 | 0x011CD1D4 |
| fSandboxEnergyMult | 0.05 | 2 | 0x011CDC10 |
| fSandboxEnergyMultEating | -0.05 | 1 | 0x011CDC50 |
| fSandboxEnergyMultFurniture | -0.1 | 1 | 0x011CDB90 |
| fSandboxEnergyMultIdleMarker | 0.05 | 1 | 0x011CD020 |
| fSandboxEnergyMultWandering | 0.2 | 1 | 0x011CD608 |
| fSandBoxExtraDialogueRange | 384.0 | 3 | 0x011CCF38 |
| fSandboxLunchMax | 14.0 | 1 | 0x011CDE44 |
| fSandboxLunchMin | 11.0 | 1 | 0x011CD9A8 |
| fSandboxMealDurationMax | 2.0 | 1 | 0x011CDB18 |
| fSandboxMealDurationMin | 0.5 | 1 | 0x011CD9C4 |
| fSandboxSleepDurationMax | 10.0 | 1 | 0x011CCF70 |
| fSandboxSleepDurationMin | 6.0 | 1 | 0x011CD36C |
| fSandboxSleepStartMax |  | 1 | 0x011CD58C |
| fSandboxSleepStartMin | 19.0 | 1 | 0x011CD708 |
| fSearchPackageDistanceToTarget | 350.0 | 2 | 0x011CDA7C |
| fSearchPackageTimer | 10.0 | 1 | 0x011CD6D8 |
| fSittingMaxLookingDown | 40.0 | 2 | 0x011CD8CC |
| fSneakActionMult |  | 3 | 0x011CD080 |
| fSneakAlertMod | 0.2 | 3 | 0x011CDFC0 |
| fSneakAmbushNonTargetMod | -0.25 | 2 | 0x011CD1E0 |
| fSneakAmbushTargetMod | 2.5 | 2 | 0x011CDBF8 |
| fSneakBaseValue | -25.0 | 3 | 0x011CD7E4 |
| fSneakBootWeightBase | 14.0 | 2 | 0x011CD258 |
| fSneakBootWeightMult |  | 2 | 0x011CDC80 |
| fSneakCombatMod | -0.4 | 3 | 0x011CDBD4 |
| fSneakDistanceAttenuationExponent | 2.0 | 3 | 0x011CD304 |
| fSneakExteriorDistanceMult | 2.0 | 5 | 0x011CDCBC |
| fSneakLightMoveMult | 0.01 | 2 | 0x011CDD18 |
| fSneakLightMult | 1.4 | 3 | 0x011CD08C |
| fSneakLightRunMult | 0.2 | 2 | 0x011CD2DC |
| fSneakLostMin | -20.0 | 1 | 0x011CDA4C |
| fSneakMaxDistance | 1500.0 | 7 | 0x011CD7D8 |
| fSneakNoticedMin | -20.0 | 6 | 0x011CD45C |
| fSneakNoticeMin | -20.0 | 1 | 0x011D3CB8 |
| fSneakPerceptionSkillMax | 90.0 | 3 | 0x011CDD9C |
| fSneakPerceptionSkillMin | 10.0 | 3 | 0x011CDF04 |
| fSneakRunningMult | 2.0 | 2 | 0x011CD148 |
| fSneakSeenMin |  | 5 | 0x011CDF10 |
| fSneakSizeBase | 20.0 | 1 | 0x011CD650 |
| fSneakSkillMult | 0.5 | 2 | 0x011CDA04 |
| fSneakSleepBonus | -0.2 | 3 | 0x011CD774 |
| fSneakSoundLosMult | 0.25 | 3 | 0x011CD2E8 |
| fSneakSoundsMult | 1.6 | 3 | 0x011CE024 |
| fSneakStealthBoyMult |  | 2 | 0x011CD310 |
| fSneakUnseenMin |  | 1 | 0x011CDE5C |
| fSortActorDistanceListTimer | 3.0 | 3 | 0x011CD8F0 |
| fSpellCastingDetectionHitActorMod | 40.0 | 1 | 0x011CD0F0 |
| fSpellCastingDetectionMod | 10.0 | 1 | 0x011CDD48 |
| fTrackDeadZoneXY | 20.0 | 2 | 0x011D58A0 |
| fTrackDeadZoneZ | 10.0 | 2 | 0x011D5974 |
| fUnarmedCreatureDPSMult |  | 2 | 0x011CF6C0 |
| fUnarmedNPCDPSMult | 1.57 | 2 | 0x011CFBF0 |
| fVanityModeWheelDeadMin | 75.0 | 3 | 0x011CD614 |
| fVATSStealthMult | 0.5 | 2 | 0x011CEE54 |
| fVATSTargetActorHeightPanMult | 0.2 | 1 | 0x011CEBBC |
| fVATSTargetActorZMultFar | 0.2 | 1 | 0x011CE5C4 |
| fVATSTargetActorZMultFarDist | 175.0 | 1 | 0x011CE8AC |
| fVATSTargetActorZMultNear | 0.8 | 1 | 0x011CEAA4 |
| iActorKeepTurnDegree | 10 | 6 | 0x011CDA1C |
| iActorsDismemberedPerFrame:GamePlay | 2 | 2 | 0x011E0A10 |
| iActorShadowCountExt:Display | 2 | 3 | 0x011C72E4 |
| iActorShadowCountInt:Display | 4 | 3 | 0x011C72D8 |
| iActorTorsoMaxRotation | 45 | 1 | 0x011CD050 |
| iActorTurnDegree | 100 | 3 | 0x011CD480 |
| iAICombatMaxAllySummonCount | 3 | 1 | 0x011CE148 |
| iAICombatRestoreFatiguePercentage | 30 | 1 | 0x011CE414 |
| iAICombatRestoreHealthPercentage | 30 | 2 | 0x011CE0B4 |
| iAICombatRestoreMagickaPercentage | 30 | 1 | 0x011CFB14 |
| iAIDistanceRadiusMinLocation | 100 | 14 | 0x011CDE98 |
| iAIFleeMaxHitCount | 3 | 1 | 0x011CF474 |
| iAIFriendlyHitMinDisposition | 15 | 1 | 0x011CD6F0 |
| iAINPCRacePowerChance | 5 | 1 | 0x011CEA14 |
| iAINumberActorsComplexScene | 20 | 3 | 0x011CDE2C |
| iAIThread1HWThread:General | 3 | 2 | 0x011DFB34 |
| iAIThread2HWThread:General | 4 | 2 | 0x011DFB18 |
| iAllowAlchemyDuringCombat | 0 | 1 | 0x011D2D78 |
| iAllowRechargeDuringCombat | 1 | 1 | 0x011D261C |
| iAllowRepairDuringCombat | 0 | 1 | 0x011D32AC |
| iAllyHitCombatAllowed | 1000 | 2 | 0x011CD4B4 |
| iAllyHitNonCombatAllowed | 3 | 2 | 0x011CD468 |
| iAttenuationDialogMenuMute:Audio |  | 0 | 0x011F6EB0 |
| iAttractModeIdleTime | 90 | 1 | 0x011D3CD0 |
| iAvoidHurtingNonTargetsResponsibility | 50 | 2 | 0x011CE3CC |
| iBallisticProjectilePathPickSegments | 4 | 2 | 0x011CFD7C |
| iChanceFleeDialog | 25 | 2 | 0x011CD838 |
| iClassCharactergenClass | 143590 | 2 | 0x011D0E7C |
| iCombatCastDrainMinimumValue | 1 | 1 | 0x011CE594 |
| iCombatCrippledTorsoHitStaggerChance | 50 | 2 | 0x011CF308 |
| iCombatDismemberPartChance | 25 | 2 | 0x011CF2EC |
| iCombatExplodePartChance |  | 2 | 0x011CE2FC |
| iCombatHighPriorityModifier | 100 | 1 | 0x011CE690 |
| iCombatSearchMaxSearchDoorFailure | 5 | 2 | 0x011CFC98 |
| iCombatTargetLostRemoveSearchCount | 2 | 2 | 0x011CEF50 |
| iCombatTargetPlayerSoftCap | 15 | 3 | 0x011CF414 |
| iCrimeAlarmRecDistance | 10000 | 6 | 0x011CDBEC |
| iCrimeDaysInPrisonMod | 100 | 1 | 0x011D03AC |
| iCrimeGoldAttack | 40 | 1 | 0x011D0970 |
| iCrimeGoldMinValue | 10 | 1 | 0x011D11C4 |
| iCrimeGoldMurder | 1000 | 1 | 0x011D0244 |
| iCrimeGoldPickpocket | 25 | 1 | 0x011D0250 |
| iCrimeGoldStealHorse | 25 | 1 | 0x011D06A0 |
| iCrimeGoldTresspass | 5 | 1 | 0x011D0208 |
| iDeathDropWeaponChance | 0 | 2 | 0x011D055C |
| iDetectionHighNumPicks | 40 | 1 | 0x011DF6E0 |
| iDetectionPicks:GamePlay | 21 | 1 | 0x011DF804 |
| iDialogueDispositionFriendValue | 50 | 3 | 0x011D0844 |
| iDialogueDummySpeakThisIntOrBelow | 4 | 4 | 0x011D0DC8 |
| iFriendHitCombatAllowed | 3 | 2 | 0x011CD204 |
| iFriendHitNonCombatAllowed | 0 | 2 | 0x011CD5B0 |
| iGuardWarnings | 2 | 1 | 0x011CDAF4 |
| iHairColor00 | 8289918 | 1 | 0x011D4B04 |
| iHairColor01 | 3618617 | 1 | 0x011D2FA0 |
| iHairColor02 | 2039585 | 1 | 0x011D4BE8 |
| iHairColor03 | 4289146 | 1 | 0x011D3C1C |
| iHairColor04 | 4680837 | 1 | 0x011D1F80 |
| iHairColor05 | 3557724 | 1 | 0x011D2970 |
| iHairColor06 |  | 1 | 0x011D3918 |
| iHairColor07 | 2830157 | 1 | 0x011D463C |
| iHairColor08 | 2965094 | 1 | 0x011D406C |
| iHairColor09 | 65 | 1 | 0x011D36B4 |
| iHairColor10 | 67 | 1 | 0x011D23DC |
| iHairColor11 | 1974080 | 1 | 0x011D2E08 |
| iHairColor12 | 2958114 | 1 | 0x011D4C48 |
| iHairColor13 | 2239537 | 1 | 0x011D2550 |
| iHairColor14 | 7237230 | 1 | 0x011D3450 |
| iHairColor15 | 5400188 | 1 | 0x011D46A8 |
| iHeavyArmorStealthPenalty | 20 | 2 | 0x011D1554 |
| iHoursToRespawnCell | 72 | 2 | 0x011CA160 |
| iHoursToSleep:General | 3 | 1 | 0x011E0A9C |
| iHUDMaxCompassNPCTicks | 10 | 4 | 0x011D32D0 |
| iInventoryMenuIdleDelay | 10 | 1 | 0x011CD52C |
| iLowLevelNPCMaxLevel | 3 | 1 | 0x011D0754 |
| iLowProcessingMilliseconds | 2 | 2 | 0x011E0E64 |
| iMagicMaxSummonedCreatureTypes | 10 | 1 | 0x011C34F8 |
| iMaxCharacterLevel | 20 | 12 | 0x011D0C60 |
| iMaxHiPerfCombatCount:Combat | 4 | 3 | 0x011DF780 |
| iMaxHiPerfNPCTargetCount:Combat | 4 | 1 | 0x011F1A1C |
| iMaxPlayerSummonedCreatures | 1 | 2 | 0x011D171C |
| iMaxSandboxRescanSeconds | 6 | 2 | 0x011CDF60 |
| iMediumArmorStealthPenalty | 10 | 2 | 0x011D0538 |
| iMerchantRespawnDay1 | 0 | 2 | 0x011D058C |
| iMerchantRespawnDay2 | 3 | 2 | 0x011D0C3C |
| iMinSandboxRescanSeconds | 3 | 2 | 0x011CD0A4 |
| iNPCBasePerLevelHealthMult | 4 | 1 | 0x011D09B8 |
| iNumberActorsAllowedToFollowPlayer | 6 | 12 | 0x011CDAD0 |
| iNumberActorsGoThroughLoadDoorInCombat | 2 | 1 | 0x011D129C |
| iNumberActorsInCombatPlayer | 20 | 2 | 0x011CCFFC |
| iNumberGuardsCrimeResponse | 4 | 2 | 0x011CD808 |
| iPersuasionBribeCrime | 90 | 1 | 0x011D034C |
| iPostProcessMilliseconds:BackgroundLoad |  | 1 | 0x01202DA8 |
| iPostProcessMillisecondsEditor:BackgroundLoad |  | 0 | 0x01202DC0 |
| iPostProcessMillisecondsLoadingQueuedPriority:BackgroundLoad |  | 1 | 0x01202DB4 |
| iPostProcessTaskWarningMilliseconds:BackgroundLoad |  | 0 | 0x01202DCC |
| iRemoveExcessDeadComplexCount | 3 | 2 | 0x011D0964 |
| iRemoveExcessDeadComplexTotalActorCount | 20 | 2 | 0x011D08F8 |
| iRemoveExcessDeadCount | 15 | 2 | 0x011D0CD8 |
| iRemoveExcessDeadTotalActorCount | 20 | 2 | 0x011D09A0 |
| iSneakLevelBonus | 5 | 2 | 0x011CD13C |
| iSneakSkillUseDistance | 1000 | 2 | 0x011CD850 |
| iSneakStartBonus | 50 | 2 | 0x011CD8C0 |
| iSneakStartBonusLevelPenatly | 10 | 2 | 0x011CD4C0 |
| iStealWarnings | 2 | 2 | 0x011CD6FC |
| iUpdateActorsPerFrame:HeadTracking | 1 | 2 | 0x011DF848 |
| iXenonMenuStickDeadZone:Controls | 20000 | 1 | 0x011D8B5C |
| uActorMemoryBudgetCap:BudgetCaps | 10485760 | 2 | 0x011C59E0 |
| uActorRefCount:BudgetCaps | 20 | 1 | 0x011C5A40 |
| uActorRefCountInterior:BudgetCaps | 20 | 1 | 0x011C5BF8 |
| uDistantTreeBlockCacheSizePerCell:TerrainManager | 1 | 1 | 0x011D85A8 |
| uGridsToLoad:General | 5 | 50 | 0x011C63CC |
| uiFaceGenMaxEGMDataSize:General | 67108864 | 2 | 0x011D59F4 |
| uiFaceGenMaxEGTDataSize:General | 67108864 | 2 | 0x011D5AFC |
| uInterior_Cell_Buffer |  | 10 | 0x011C3E38 |
| uLoadedAreaNonActorMemoryBudgetCap:BudgetCaps | 185597952 | 2 | 0x011C5B20 |
| uMaxSkinDecalPerActor:Decals | 3 | 2 | 0x011C589C |
