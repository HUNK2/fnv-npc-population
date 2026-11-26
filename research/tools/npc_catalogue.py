"""Build the NPC catalogue (classes, functions, script commands, settings) from the fnv-mcp engine map.

usage: python -I npc_catalogue.py <engine_map.json> <out dir>
Writes npc_functions.csv, npc_classes.csv, npc_commands.csv, npc_settings.csv and stats.json.
"""
import collections
import csv
import json
import os
import re
import sys

emap_path, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
E = json.load(open(emap_path, encoding="utf-8"))
R = E["rtti"]
C = E["classes"]

# (group, owner-class regex, optional method regex). First match wins, so the order matters.
G_SPAWN = "1 Spawning and population"
G_ACTOR = "2 Actor references (the NPC in the world)"
G_PLAYER = "2b Player (shares the Actor code)"
G_BASE = "3 Base records (what an NPC is made of)"
G_PROC = "4 Process levels and the AI update loop"
G_PKG = "5 AI packages and daily routines"
G_MOVE = "6 Movement and pathfinding"
G_NAV = "6b Navmesh (the data paths run on)"
G_COMBAT = "7 Combat"
G_DETECT = "8 Detection, crime and reactions"
G_TALK = "9 Dialogue, barks and companions"
G_LOOK = "10 Animation, faces and bodies"
G_CELL = "11 Cells and world loading (where NPCs live)"
G_OTHER_AI = "12 Other code in the AI source files"

RULES = [
    (G_SPAWN, r"BGSEncounterZone|ExtraEncounterZone|ExtraLeveledCreature|ExtraStartingPosition|ExtraPersistentCell|"
              r"ExtraPackageStartLocation|ExtraStartingWorldOrCell|ExtraOriginalReference|SummonCreatureEffect|"
              r"ReanimateEffect|Queued(Reference|Actor|Character|Creature|Player|Head|Helmet|FaceGenFile)|ModelLoader|"
              r"TESQueuedCellManager|BGSLoadedReferenceCollection|LoadedReferenceMap|TeleportableReference|"
              r"ExteriorCellNewReferencesMap|InteriorCellNewReferencesMap", None),
    (G_SPAWN, r"TESDataHandler", r"CreateReference|PlaceObject|CreateRef|Leveled|NewRef|AddFormToDataHandler"),
    (G_SPAWN, r"TESObjectREFR", r"Respawn|Reset|Persistent|StartingPos|EncounterZone|Leveled|PlaceAtMe|Clone|"
                                r"InitItem|Enable|Disable|MoveTo|SetLocationOnReference|InitHavok|Load3D|Set3D|Unload|"
                                r"Detach|Attach|IsPersistent|GetStartingPos|Delete|MarkForDelete"),
    (G_PLAYER, r"PlayerCharacter|PlayerMover|ConditionPlayerCharacter", None),
    (G_BASE, r"TESActorBase(Data)?|TESNPC|TESCreature|TESAIForm|TESRace(Form)?|TESClass|TESFaction(_.*)?|FactionAccess|"
             r"TESCombatStyle|BGSVoiceType|TESHair|TESEyes|BGSHeadPart|BGSBodyPart(Data)?|TESAttributes|TESLevCharacter|"
             r"TESLevCreature|TESLeveledList|CreatureSounds|BGSRagdoll|TESAnimation|ActorValueInfo|TESSkill|"
             r"BGSEntryPointFunctionDataLeveledList|ExtraFactionChanges|ExtraLeveledItem", None),
    (G_PROC, r"BaseProcess|LowProcess|MiddleLowProcess|MiddleHighProcess|HighProcess|ProcessLists|ProcessArray|"
             r"HighActorCuller|AITaskThread|AILinearTaskThread(Manager)?|AIThreadManager|AITaskManager|ActorUpdateTaskData|"
             r"ActorsScriptTaskData|AnimationTaskData|MobileObjectTaskletData|CachedValues|"
             r"BSPlayerDistanceCheckController|FurnitureProcess|ActorPathingMessageQueue|"
             r"ActorValueCache|ModifierList|ActorValueModifierList", None),
    (G_PKG, r".*Package(Data|Operations|UnitOperations|Context|Location|Target|TargetRecord|List|Time|Event.*)?|"
            r"ActorPackage.*|Procedure[A-Za-z]*|PackageEventActionData.*|IdleAnimationManager|IdleSystem|BGSIdleMarker|"
            r"BGSIdleCollection|TESIdleForm|AnimIdle|BSFurnitureMarker|ExtraPatrolRefInUseData|ExtraGuardedRefData|"
            r"TES[A-Za-z]*PackageData|ExtraAction|ExtraFollower|ExtraPackage(Data)?", None),
    (G_MOVE, r"ActorMover|ActorPathHandler|DetailedActorPathHandler|VirtualActorPathHandler|Pathing[A-Za-z]*|"
             r"PathSmoother[A-Za-z]*|PathBuilder|PathManager|PathSearch|bhkCharacterController|bhkCharacterProxy|"
             r"bhkCharacterStateOnGround|bhkCharacterState[A-Za-z]*|CharacterMoveParams|CharacterCollision[A-Za-z]*|"
             r"ActorPathingMessage[A-Za-z]*|DoorObstacle[A-Za-z]*", None),
    (G_NAV, r"NavMesh[A-Za-z]*|NavMeshInfo[A-Za-z]*|ObstacleTaskData|ObstacleData|NavMeshObstacle[A-Za-z]*|"
            r"BGSNavMesh[A-Za-z]*|TESNavMesh[A-Za-z]*|PathingLOS[A-Za-z]*", None),
    (G_COMBAT, r"Combat[A-Za-z]*|ActorCombatGroup|CombatTargetTimestamp", None),
    (G_DETECT, r"Detection[A-Za-z]*|Crime[A-Za-z]*|ExtraPlayerCrimeList|ActorCause|ExtraActorCause|DetectLifeEffect|"
               r"Alarm[A-Za-z]*|ExtraOwnership", None),
    (G_TALK, r"Conversation|FollowerBarks|DialogueItem|TESTopic|TESTopicInfo(Data)?|ExtraInfoGeneralTopic|"
             r"LipSync[A-Za-z]*|LipTask|DialogueResponse|MenuTopic|TopicMenuController|DialogMenu|LocalDialogMenu|"
             r"CompanionWheelMenu|GreetingsManager|ExtraSayTopicInfo[A-Za-z]*|ExtraSayToTopicInfo|"
             r"BGSSpeechChallenge|SpeechChallenge[A-Za-z]*|RadioConvTask", None),
    (G_LOOK, r"BSFaceGen[A-Za-z:]*|FaceGen[A-Za-z<>]*|BipedAnim|Animation|AnimData|ActorAnimData|TESAnimGroup|"
             r"AnimSequence[A-Za-z]*|BSAnimGroupSequence|QueuedKF|QueuedAnimIdle|QueuedReplacementKF[A-Za-z]*|"
             r"BodyPartDisplay|BSAnimNote[A-Za-z]*|LocalhkaAnimation|BGSBipedModelList", None),
    (G_CELL, r"TESObjectCELL|Cell", r"Actor|Ref|Reset|Respawn|Load|Unload|Attach|Detach|Persistent|Mobile|Process|"
                                    r"Character|Creature|Encounter|Owner|Spawn|Population|AddReference|RemoveReference"),
    (G_CELL, r"GridCellArray|GridArray|ExteriorCellLoaderTask|BGSCellNumericIDArrayMap|BGSReconstructCell[A-Za-z]*", None),
    (G_CELL, r"TES", r"Cell|Grid|Load|Unload|Actor|Ref|Process"),
    (G_CELL, r"TESWorldSpace", r"Persistent|Cell|Ref|Actor|Load"),
    (G_ACTOR, r"Actor|Character|Creature|MobileObject|ActorValueOwner|CachedValuesOwner|ActorValue|"
              r"ActorValueStore|XActor|xActor|ActorX|MatchActor|NonActorMagicTarget|ExtraActorValueModifierList", None),
]
RULES = [(g, re.compile(r"(?:%s)\Z" % o), re.compile(m, re.I) if m else None) for g, o, m in RULES]

# Free functions: keyword -> group (first match wins)
FREE = [
    (G_SPAWN, r"PlaceAtMe|PlaceLeveled|Respawn|EncounterZone|LeveledActor|LeveledCreature|CreateReference|"
              r"Summon|Reanimate|QueuedActor|QueuedCharacter|QueuedCreature|QueuedHead|Spawn(Actor|NPC|Creature)|DoorSpawn"),
    (G_PLAYER, r"PlayerCharacter|PlayerMover"),
    (G_PROC, r"ProcessLists|HighProcess|LowProcess|MiddleHigh|MiddleLow|BaseProcess|ProcessLevel|HighActorCuller|"
             r"AITask|AILinear|AIThread|ActorUpdate|ProcessActors|MoveProcess"),
    (G_PKG, r"Package|Procedure|Sandbox|Patrol|Escort|Wander|Ambush|IdleMarker|IdleAnim|Furniture"),
    (G_MOVE, r"Pathing|PathHandler|ActorMover|PathSmooth|PathFind|CharacterController|CharController"),
    (G_NAV, r"NavMesh"),
    (G_COMBAT, r"Combat"),
    (G_DETECT, r"Detection|Detected|Detectable|Crime|Alarm|Trespass|Pickpocket|Murder|Assault"),
    (G_TALK, r"Conversation|Dialogue|Topic|Bark|Follower|Companion|Teammate|Greet|LipSync|Say(To)?_"),
    (G_LOOK, r"FaceGen|BipedAnim|AnimGroup|AnimSequence|Ragdoll|HeadPart|Hair(?!pin)|Eyes"),
    (G_BASE, r"TESNPC|TESCreature|TESActorBase|ActorBase|TESRace|TESClass|TESFaction|Faction|CombatStyle|VoiceType|"
             r"LevCharacter|LevCreature|LeveledList"),
    (G_ACTOR, r"Actor|NPC|Creature|Character|MobileObject"),
]
FREE = [(g, re.compile(k)) for g, k in FREE]
SKIP_FREE = re.compile(r"^(Init_|AtExit_|InitializeRuntime|ForiginalRuntime|Cmd_|`|finishLoadedObject_|cleanupLoadedObject_|getVtable_|hk)")
SKIP_FREE_FILE = re.compile(r"^src/(havok|gamebryo2\.2|bssystemutilities|bsshader|speedtree)/")


def owner_method(name):
    if not name:
        return "", ""
    head = name.split("(")[0]
    if "::" in head:
        parts = head.split("::")
        return "::".join(parts[:-1]), parts[-1]
    return "", head


def classify(owner, method, name, file):
    last = owner.split("::")[-1] if owner else ""
    if last:
        for g, o, m in RULES:
            if o.match(last) and (m is None or m.search(method)):
                return g
        return None
    if SKIP_FREE.match(name or "") or SKIP_FREE_FILE.match(file):
        return None
    for g, k in FREE:
        if k.search(name or ""):
            return g
    return None


funcs = []
for f in E["functions"]:
    name = f.get("name") or ""
    owner, method = owner_method(name)
    g = classify(owner, method, name, f.get("file") or "")
    if g is None:
        # second chance: the decomp's own spelling (proven names are preferred, decomp names catch the rest)
        dn = f.get("decompName") or ""
        o2, m2 = owner_method(dn)
        if f["status"] in ("decomp", "unnamed", "rejected"):
            g = classify(o2, m2, dn, f.get("file") or "")
    if g is None and (f.get("file") or "").startswith("src/fallout/ai/"):
        if not SKIP_FREE.match(name):
            g = G_OTHER_AI
    if g is None:
        continue
    funcs.append({
        "group": g, "address": f["address"], "name": name or f.get("decompName") or "",
        "class": owner, "method": method, "status": f["status"], "size": f.get("size", 0),
        "decomp_name": f.get("decompName") or "", "signature": f.get("signature") or "",
        "file": "%s:%s" % (f.get("file") or "", (f.get("lines") or [""])[0]),
    })
funcs.sort(key=lambda r: (r["group"], r["class"], r["name"]))

# Classes: every RTTI class or owner class that one of the group rules accepts as a whole class
fcount = collections.Counter(r["class"].split("::")[-1] for r in funcs if r["class"])
cls_rows = []
names = set(R) | {k for k in fcount}
for k in sorted(names):
    g = None
    for gg, o, m in RULES:
        if o.match(k.split("::")[-1]) and m is None:
            g = gg
            break
    if g is None:
        continue
    if re.search(r"(_shell|StandIn|Stub|View|_Class|_cls|^[0-9A-F]{4,})", k):
        continue
    rt = R.get(k, {})
    ci = C.get(k, {})
    vt = rt.get("vtables") or []
    cls_rows.append({
        "group": g, "class": k, "bases": " > ".join(rt.get("bases", [])),
        "size": ("0x%X" % ci["size"]) if ci.get("size") else "",
        "vtable": vt[0]["address"] if vt else "", "virtuals": len(vt[0]["slots"]) if vt else "",
        "functions": fcount.get(k, 0), "header": ci.get("file", ""),
    })
# methods only matched for some classes (TESObjectREFR, TESObjectCELL, TES, TESDataHandler, TESWorldSpace)
for k in ("TESObjectREFR", "TESObjectCELL", "TES", "TESDataHandler", "TESWorldSpace"):
    rt, ci = R.get(k, {}), C.get(k, {})
    vt = rt.get("vtables") or []
    cls_rows.append({
        "group": "(partly) " + (G_SPAWN if k in ("TESObjectREFR", "TESDataHandler") else G_CELL), "class": k,
        "bases": " > ".join(rt.get("bases", [])), "size": ("0x%X" % ci["size"]) if ci.get("size") else "",
        "vtable": vt[0]["address"] if vt else "", "virtuals": len(vt[0]["slots"]) if vt else "",
        "functions": fcount.get(k, 0), "header": ci.get("file", ""),
    })
cls_rows.sort(key=lambda r: (r["group"], r["class"]))

# Script commands
CMD = re.compile(
    r"Actor|AI|Package|Combat|Alert|Detect|Faction|Crime|PlaceAtMe|Leveled|MoveTo|Follow|Companion|Teammate|"
    r"Conversation|Say|Greet|Idle|Sit|Sleep|Unconscious|Restrained|Resurrect|Kill|Race|Hair|Eyes|Disposition|"
    r"Aggression|Confidence|Assistance|Encounter|Respawn|Ghost|Essential|Pursue|Ignore|Talk|Dialogue|Sandbox|"
    r"Patrol|Path|Wander|LookAt|PlayGroup|PlayIdle|Ragdoll|Knock|Process|NPC|Creature|Character|Dead|Enable|"
    r"Disable|Disintegrate|Voice|Head|Faction|Class|Crowd|Hostile|Ally|Enemy|Reaction|Fight|Flee|Evaluate|"
    r"Animation|Weapon|SetPos|SetAngle|Height|Scale|Dismember|Limb|Mood|Emotion|Trespass|Steal|Crim")
CMD_SKIP = re.compile(r"Weapon|Mines|Hardcore|PlayerControls|FastTravel|LoadingMenu|RenderPass|ImageSpace|QuestUpdates|"
                      r"SpellConditions|PCSleep|SleepWait|Gore|VatsTarget|RadioToDialogue")
cmds = []
for c in E["commands"]:
    text = c["name"] + " " + (c.get("short") or "")
    if c.get("source") != "vanilla" or not CMD.search(text) or CMD_SKIP.search(c["name"]):
        continue
    h = c.get("handlers") or {}
    cmds.append({
        "command": c["name"], "short": c.get("short") or "", "opcode": c["opcode"], "table": c["table"],
        "execute": h.get("execute") or "", "eval": h.get("eval") or "",
        "params": ", ".join(("[%s]" if p.get("optional") else "%s") % (p.get("label") or p.get("type")) for p in c.get("params", [])),
        "help": c.get("help") or "",
    })
cmds.sort(key=lambda r: r["command"].lower())

# Settings
SET = re.compile(
    r"AI|Actor|NPC|Creature|Combat|Package|Process|Detect|Sandbox|Patrol|Crowd|Encounter|Respawn|Leveled|Path|"
    r"Avoid|Follow|Conversation|Greet|Hello|Dialog|Idle|Wander|Flee|Alarm|Crime|Trespass|Sneak|LowProc|HighProc|"
    r"MiddleProc|Cull|FaceGen|Head|Hair|Mover|Movement|Navmesh|NavMesh|Bark|Murder|Assault|Pickpocket|Steal|"
    r"Ambush|Guard|Escort|Companion|Teammate|Furniture|Sit|Sleep|Eat|Character|Population|Spawn|Reset|Detach|"
    r"Ragdoll|Death|Dead|Corpse|Body|Cell|Grid")
SET_SKIP = re.compile(r"^s|^fFurnitureMarker\d|^iXP|^bDebug|^iDebug|^fDebug")
sets = []
for s in E["statics"]:
    if s["kind"] != "Setting" or not SET.search(s["name"]) or SET_SKIP.search(s["name"]):
        continue
    sets.append({
        "setting": s.get("setting") or s["name"], "address": s["address"], "default": s.get("default"),
        "used_by": len([u for u in s.get("usedBy", []) if u != s.get("initializer")]),
        "used_by_addresses": " ".join(u for u in s.get("usedBy", [])[:12] if u != s.get("initializer")),
    })
sets.sort(key=lambda r: r["setting"].lower())


def write(name, rows):
    with open(os.path.join(out, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


write("npc_functions.csv", funcs)
write("npc_classes.csv", cls_rows)
write("npc_commands.csv", cmds)
write("npc_settings.csv", sets)
stats = {
    "functions": len(funcs), "classes": len(cls_rows), "commands": len(cmds), "settings": len(sets),
    "by_group": collections.Counter(r["group"] for r in funcs),
    "by_status": collections.Counter(r["status"] for r in funcs),
    "classes_by_group": collections.Counter(r["group"] for r in cls_rows),
    "engine_map": E["generated"],
}
json.dump(stats, open(os.path.join(out, "stats.json"), "w"), indent=1, default=str)
print(json.dumps(stats, indent=1, default=str))
