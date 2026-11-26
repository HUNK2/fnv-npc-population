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
| 0.8 Limits | 30 rows: PASS (Row 30 shows and clicks). Text length: JohnnyGuitar copies into a 260-byte stack buffer with no length check; a 262-character text closed the game with no crash log. | JG source `fn_terminal.cpp` (`char cText[MAX_PATH]`) | Hard rule: every string sent to `SetTerminalMenuItemText` is cut to 200 characters first. A row shows about 50 characters on one line. |
| 0.9 Day tick | PASS. 5 days gave 5 steps; 20 days gave 1 summary plus 14 steps; the seeded rolls match Python. | Quest variables | The day tick works without `while`; one day per script run spreads catch-up over frames. |

## Tool notes (fnv-mcp, logged for its issue list)

- The MCP server did not reload its project spec after the project file changed. Workaround:
  `tools/fnvmcp_call.py` runs fnv-mcp's tools in-process with our spec.
- In-game compile: statements after a `while ... loop` block never ran (the jump after the loop
  seems off by 4 bytes). Workaround: no `while` in our scripts.
- `fnv_ui_do click` cannot pick one terminal row: every row has the same tile path and id -1, so
  it clicks the first child (the last row). Keyboard arrows do not move the terminal highlight.
- The builder refuses a change that renumbers script variables; keep unused variables in place.
- `set GameDaysPassed` from the console has no effect (`Calendar::Update` 0x00867A40 rebuilds it
  from the hour). Tests jump `GameHour` instead: `set GameHour to GameHour + 120` is 5 days.
