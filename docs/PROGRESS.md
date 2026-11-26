# Progress

Updated at every task end. Workflow: `docs/plans/2026-11-26-build-workflow.md`.
The user asked (2026-11-27) for the whole plan to run without stopping at gates G4 to G7; those
calls are mine and are marked "my call" here and in the plans.

## Now

- Milestone: **M0 Proofs** (`docs/plans/2026-11-27-m0-proofs.md`)
- Next task: 0.2 tooling (build our plugins with fnv-mcp)

## Done

- 0.1 Ledger reference model: `tools/ledger_model.py` reproduces the doc's worked first week
  exactly (legs, day margins, sales 8,178, COGS 6,857, operating 842, net 722, cash 2,972, net
  worth 923). Settings found: depth K = 2, spread 6%, a crate is loaded only at margin >= 20.
  Tests: `python -m unittest test_ledger_model` in `tools/` (8 pass).

## My calls (to review)

- Plugins are built with fnv-mcp's builder by pointing its (local) project file at our spec.
