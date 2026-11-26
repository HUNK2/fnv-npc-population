"""Render the NPC catalogue CSVs into markdown.

usage: python -I render.py <catalogue dir with CSVs> <engine_map.json> <out dir>
"""
import collections
import csv
import json
import os
import shutil
import sys

cat, emap_path, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
E = json.load(open(emap_path, encoding="utf-8"))
BY_ADDR = {f["address"].upper(): f for f in E["functions"]}


def rd(name):
    return list(csv.DictReader(open(os.path.join(cat, name), encoding="utf-8")))


funcs, classes, cmds, sets = rd("npc_functions.csv"), rd("npc_classes.csv"), rd("npc_commands.csv"), rd("npc_settings.csv")
stats = json.load(open(os.path.join(cat, "stats.json")))
for n in ("npc_functions.csv", "npc_classes.csv", "npc_commands.csv", "npc_settings.csv"):
    shutil.copy(os.path.join(cat, n), os.path.join(out, n))

STATUS = {"proven": "proven", "class_proven": "class", "probable": "probable", "decomp": "decomp",
          "unnamed": "unnamed", "rejected": "rejected"}


def esc(s):
    return (s or "").replace("|", "\\|").replace("`", "'")


GROUP_NOTE = {
    "1 Spawning and population": "Creating references at runtime (PlaceAtMe), leveled actors, encounter zones, "
        "cell respawn timers, and the background loader that builds an actor's 3D.",
    "2 Actor references (the NPC in the world)": "Actor, Character, Creature and MobileObject: the live NPC object.",
    "2b Player (shares the Actor code)": "PlayerCharacter is an Actor too; listed apart so it is easy to skip.",
    "3 Base records (what an NPC is made of)": "TESNPC / TESCreature records and their parts: race, class, faction, "
        "voice, hair, eyes, head parts, leveled lists, combat style.",
    "4 Process levels and the AI update loop": "Every actor has a process (High, MiddleHigh, MiddleLow, Low). "
        "ProcessLists updates them each frame. This is where the cost of more NPCs goes.",
    "5 AI packages and daily routines": "Packages (sandbox, patrol, guard, escort, eat, sleep...) and the procedures "
        "that run them: what makes an NPC look busy.",
    "6 Movement and pathfinding": "ActorMover, the path handlers (Detailed for loaded actors, Virtual for unloaded "
        "ones) and pathing requests.",
    "6b Navmesh (the data paths run on)": "NavMesh data and searches the path code uses.",
    "7 Combat": "CombatController, combat groups, goals, actions and procedures.",
    "8 Detection, crime and reactions": "Detection, alarms and crime tracking.",
    "9 Dialogue, barks and companions": "Topics, conversations between NPCs, follower barks, companion wheel.",
    "10 Animation, faces and bodies": "FaceGen heads, biped models, animation data and idle animations.",
    "11 Cells and world loading (where NPCs live)": "Grid and cell loading that decides which NPCs are loaded at all.",
    "12 Other code in the AI source files": "Functions that live in src/fallout/ai/ but whose names did not place "
        "them in a group above (mostly decomp or unnamed). Worth a look; many are NPC logic without a good name yet.",
}

# ---------------------------------------------------------------- CLASSES.md
L = ["# NPC classes", "",
     "Every class the catalogue counts as NPC-related, by subsystem. `Bases` is the full RTTI chain, nearest first. "
     "`Size` is the checked size from the decomp headers when known. `Funcs` is how many functions in "
     "[FUNCTIONS.md](FUNCTIONS.md) belong to the class.", ""]
by = collections.defaultdict(list)
for c in classes:
    by[c["group"]].append(c)
for g in sorted(by, key=lambda x: (x.startswith("("), int(x.lstrip("(partly) ").split()[0].rstrip("b")) if x.lstrip("(partly) ")[0].isdigit() else 99, x)):
    L += ["## " + g, ""]
    note = GROUP_NOTE.get(g.replace("(partly) ", ""))
    if g.startswith("(partly)"):
        L += ["Big shared classes: only their NPC-related methods are in the function list.", ""]
    elif note:
        L += [note, ""]
    L += ["| Class | Bases | Size | Vtable | Virtuals | Funcs |", "|---|---|---|---|---|---|"]
    for c in sorted(by[g], key=lambda r: r["class"].lower()):
        L.append("| %s | %s | %s | %s | %s | %s |" % (esc(c["class"]), esc(c["bases"]), c["size"], c["vtable"],
                                                     c["virtuals"], c["functions"]))
    L.append("")
open(os.path.join(out, "CLASSES.md"), "w", encoding="utf-8").write("\n".join(L))

# ---------------------------------------------------------------- FUNCTIONS.md
L = ["# NPC functions", "",
     "All %d NPC-related functions of FalloutNV.exe 1.4.0.525, by subsystem, then class. "
     "Status: **proven** = name proven from evidence (fnvsym), **class** = owning class proven, method name not, "
     "**probable** = strong evidence, not proven, **decomp** = the decomp's own name (machine-made, treat as a guess), "
     "**unnamed** = no name yet, **rejected** = the decomp name was checked and found wrong. "
     "The same rows are in [npc_functions.csv](npc_functions.csv) with signatures." % len(funcs), "",
     "## Contents", ""]
groups = sorted({f["group"] for f in funcs}, key=lambda x: (int(x.split()[0].rstrip("b")), x))
for g in groups:
    n = sum(1 for f in funcs if f["group"] == g)
    anchor = g.lower().replace(" ", "-").replace(",", "").replace("(", "").replace(")", "")
    L.append("- [%s](#%s) (%d)" % (g, anchor, n))
L.append("")
for g in groups:
    rows = [f for f in funcs if f["group"] == g]
    L += ["## " + g, "", GROUP_NOTE.get(g, ""), ""]
    cls = collections.defaultdict(list)
    for f in rows:
        cls[f["class"] or "(free functions)"].append(f)
    for k in sorted(cls, key=lambda x: (x == "(free functions)", x.lower())):
        L += ["### %s (%d)" % (k, len(cls[k])), "", "| Address | Name | Status | Source |", "|---|---|---|---|"]
        for f in sorted(cls[k], key=lambda r: (r["method"].lower(), r["address"])):
            nm = f["method"] if f["class"] else f["name"]
            if f["status"] in ("unnamed", "decomp", "rejected") and f["decomp_name"] and f["decomp_name"] != f["name"]:
                nm += " (decomp: %s)" % f["decomp_name"]
            L.append("| %s | %s | %s | %s |" % (f["address"], esc(nm), STATUS[f["status"]], esc(f["file"])))
        L.append("")
open(os.path.join(out, "FUNCTIONS.md"), "w", encoding="utf-8").write("\n".join(L))

# ---------------------------------------------------------------- COMMANDS.md
L = ["# NPC script and console commands", "",
     "%d vanilla commands that act on or ask about NPCs. `Execute` is the engine handler address (the function "
     "that runs when a script or the console calls the command). Optional parameters are in brackets." % len(cmds), "",
     "| Command | Short | Opcode | Execute | Parameters | Help |", "|---|---|---|---|---|---|"]
for c in cmds:
    L.append("| %s | %s | %s | %s | %s | %s |" % (esc(c["command"]), esc(c["short"]), c["opcode"], c["execute"],
                                                esc(c["params"]), esc(c["help"])))
open(os.path.join(out, "COMMANDS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---------------------------------------------------------------- SETTINGS.md
L = ["# NPC settings", "",
     "%d game settings (GMST) and INI settings that touch NPCs. INI settings carry their section after the colon "
     "(`bUseThreadedAI:General` goes under `[General]` in FalloutNV.ini / FalloutCustom.ini). `Used by` counts "
     "the engine functions that read the setting; the CSV lists their addresses." % len(sets), "",
     "| Setting | Default | Used by | Address |", "|---|---|---|---|"]
for s in sets:
    L.append("| %s | %s | %s | %s |" % (esc(s["setting"]), s["default"], s["used_by"], s["address"]))
open(os.path.join(out, "SETTINGS.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---------------------------------------------------------------- key list check
KEY = [l.split()[0] for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "key_addrs.txt"))
       if l.strip() and not l.startswith("#")]
missing = [a for a in KEY if a.upper() not in BY_ADDR]
bad = [(a, BY_ADDR[a.upper()]["name"], BY_ADDR[a.upper()]["status"]) for a in KEY if a.upper() in BY_ADDR]
print("key addresses:", len(KEY), "missing:", missing)
for a, n, s in bad:
    print(a, s, n)
print("by group:", collections.Counter(f["group"] for f in funcs))
