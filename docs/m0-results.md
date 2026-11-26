# M0 results

One row per proof: the answer, the evidence, and what it changes for M1. Filled in as each test
runs (plan: `docs/plans/2026-11-27-m0-proofs.md`). Evidence screenshots stay on the test machine
(they show a local game install); the facts they show are written here.

| Test | Answer | Evidence | What it changes in M1 |
|---|---|---|---|
| 0.1 Ledger model | PASS. `tools/ledger_model.py` reproduces the worked first week exactly. | `tools/test_ledger_model.py`, 8 tests | The model is the reference for the in-game ledger (same numbers, same rounding). |
| 0.2 Tooling | PASS, with a workaround. Plugins build from `mod/proofs/proofs.spec.json`; scripts compile in game. | `tools/fnvmcp_call.py`, `tools/rebuild.sh` | Build through `tools/rebuild.sh`. See "Tool notes". |
| 0.3 Dependencies | PASS. xNVSE, JIP LN and JohnnyGuitar 5.28 load in the Dev profile. | NVSE log | None. |
| 0.4 Live labels | PASS. `SetTerminalMenuItemText` plus `RefreshTerminalMenu` relabels rows while the terminal is open; the list redraws in place. About 10 rows fit on screen. | Screenshots `m0-term-*` | The office terminal can show live prices and margins. |
| 0.5 Which row was clicked | PASS, route C (new): the engine's click handler sets flag 4 on the clicked row (`ComputersMenu::DoClick` 0x00757F70 calls `SetFlag4(true)` before the row's result script). A click on Row 30 gave `GetTerminalMenuItemFlags CCProofsTerm 29` = 4 and 0 on every other row; `SetTerminalMenuItemFlags ... 0` clears it. | Console output, result text "Row 30 picked." | No builder change needed. The terminal script polls row flags in MenuMode, acts on the row with flag 4, then clears it. Routes A and B are not needed. |
| 0.6 Terminal from an item | Half. From a script: PASS, `CCProofsTermRef.Activate player 1` opens the terminal (flag 1 is needed; the default 0 skips the reference's OnActivate block). From a Pip-Boy item: NOT PROVEN. A BOOK and an ARMO item with a script never ran `OnEquip` when equipped by console `EquipItem`, even with script locals present. | Console; script variables stayed 0 | The fallback in the design stands: the ledger is opened at the runner's desk and the relay desks. M1 retries the item as an ALCH (the engine's `Actor::EquipItem` 0x0088C830 sets the OnEquip flag in its ALCH case) and keeps the desk route either way. |
| 0.7 Labels on open | PASS. Labels set in the terminal reference's `OnActivate`, before its `Activate`, show on the first draw. | Screenshot, row 2 read "Opened 1 times (set in OnActivate)" | No menu-open event handler is needed: each terminal's script relabels its rows in OnActivate. |
| 0.8 Limits | 30 rows: PASS (Row 30 shows and clicks). Text length: JohnnyGuitar copies into a 260-byte stack buffer with no length check; a 262-character text closed the game with no crash log. | JG source `fn_terminal.cpp` (`char cText[MAX_PATH]`) | Hard rule: every string sent to `SetTerminalMenuItemText` is cut to 200 characters first. A row shows about 50 characters on one line. |
| 0.9 Day tick | PASS. 5 days gave 5 steps; 20 days gave 1 summary plus 14 steps; the seeded rolls match Python. | Quest variables | The day tick works without `while`; one day per script run spreads catch-up over frames. |
| 0.10 Letters | Partly. `MessageBoxEx` opens at once even over the Pip-Boy; nothing queues it. | Screenshot | Letters are shown only from a GameMode block (it does not run in menus or dialogue) and only when `player.IsInCombat == 0`. A MESG with buttons is built in M1. |
| 0.11 Moving people | PASS. 10 round trips of 3 settlers (MoveTo to `GoodspringsBoundaryMarker01` and back) plus 2 brahmin made with PlaceAtMe then Disable and MarkForDelete: nothing left behind, created ids are reused. Save size: 1,952,964 bytes at the start, 2,027,501 after 10 cycles (a one-off +77 vanilla change forms), 2,027,882 after 20 (+381 bytes). | Test saves `ccm0_base`, `ccm0_after10`, `ccm0_after20` | MoveTo for named people and PlaceAtMe plus MarkForDelete for animals and goods do not grow the save. |
| 0.12 Which world | PASS. `GetSourceModIndex` of the player's parent cell: 18 in the proofs room, 9 in Honest Hearts' Zion, 0 in Mojave interiors and exteriors. | Console | "Is the player in the Mojave" is `GetSourceModIndex == 0` (FalloutNV.esm). DLC worlds are compared with `GetModIndex "<dlc>.esm"`, because the numbers depend on load order. |
| 0.13 Old saves | PASS. The quest starts on a save made before the plugin was installed. | Test save `rotf_release_car` | Install mid-playthrough is supported; the start-up script must not assume a new game. |
| 0.14 Crowd | PASS with room to spare. Goodsprings at noon: 8 NPCs in 6,000 units, 59.8 fps, 16.2 ms a frame. With 30 extra settlers (38 NPCs, all 30 in high process; 49 high-process actors in all): 59.6 fps, 16.4 ms. The game is held at 60 by vsync, so the cost shows in the CPU parts: audio 0.5 to 1.8 ms, post-render (animation) 0.5 to 1.6 ms, process lists 0.16 to 0.18 ms; AI runs on worker threads. The engine's close-actor list (`ProcessLists::InsertActorCloseToPlayer` 0x0096E3C0) holds the nearest min(50, `iAINumberActorsComplexScene` = 20) actors and is read only by face animation (`BSFaceGenNiNode::UpdateMorphing` via `CanAddActorToList` 0x0096E7D0): actors past the nearest 20 just stop moving their faces. | `fnv_profile frame`, 5 s each | No hard engine limit is near at 30 extra people, so the towns core question (G4) is answered **plugin-first** (my call): towns are built from ordinary placed NPCs, packages and scripts, with no engine plugin. The towns design still keeps extra people well under 30 per town to leave room for other mods and older PCs. |

## Tool notes (fnv-mcp, logged for its issue list)

- The MCP server did not reload its project spec after the project file changed. Workaround:
  `tools/fnvmcp_call.py` runs fnv-mcp's tools in-process with our spec.
- In-game compile: statements after a `while ... loop` block never ran in plugin scripts. Cause
  (read from the bytecode): xNVSE writes a 4-byte scriptname statement before compiling and stores
  the `while` exit jump as an absolute offset into that buffer (58 in a probe script); fnv-mcp's
  `compile_spec_scripts` dropped those 4 bytes, so the exit landed 4 bytes inside the next
  statement. First fix kept the 4 bytes (proven: a loop in `CCProofsQuestScript` set `iLoopI` 3
  and the line after it set `iLoopOut` 103), but then xNVSE could not find a `Begin Function` block
  (it reads the block type at byte 8, after one scriptname). Final fix (M1 1.3, fnv-mcp working tree,
  not committed there): `drop_partial_scriptname` drops the extra statement and moves each
  `While` (0x153B) and `ForEach` (0x153D) exit offset back by 4; unit test
  `tests/test_partial_scriptname.py`. Snippets run by `fnv_run_script` never had the bug.
- In-game compile reports `array_var` and `string_var` as float. xNVSE reads the stored variable
  type at run time when the script text is not loaded (`Script::GetVariableType`), so fnv-mcp now
  writes SLSD type 3 / 2 from the source declarations (same uncommitted change).
- Quest scripts stop while the pause menu or a message box is up: a fresh coc start shows the DLC
  "has been loaded" boxes, and focus loss opens the pause menu. `tools/ingame_run.py` sets
  `fnv_window background` and presses the boxes first.
- `return` in any block ends the whole script for that frame, so a later block of the same type
  never runs after an early `return`.
- `fnv_ui_do click` cannot pick one terminal row: every row has the same tile path and id -1, so
  it clicks the first child (the last row). Keyboard arrows do not move the terminal highlight.
- The builder refuses a change that renumbers script variables, even new variables added at the
  end; keep unused variables in place. `tools/allow_new_vars.py` checks that the old variables are
  an unchanged prefix and then drops the cached entry, so appends are accepted.
- Runtime-compiled scripts cannot pass a `string_var` (`$sVar`) to a plugin command ("Missing
  parameter string"). Workaround: JIP `Console "Cmd ... %q%.0f%q" fVar` builds the line (`%q` is a
  quote mark).
- `fnv_run_script`: statements after a `while ... loop` do not run (same compile bug as above).
- MO2 cannot launch the game from the Bash tool (its job object refuses it). `tools/cycle.sh`
  quits and installs; the launch goes through the MCP server's `fnv_game launch`.
- `set GameDaysPassed` from the console has no effect (`Calendar::Update` 0x00867A40 rebuilds it
  from the hour). Tests jump `GameHour` instead: `set GameHour to GameHour + 120` is 5 days.
