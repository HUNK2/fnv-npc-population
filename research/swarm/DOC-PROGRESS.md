# Doc progress (for recovery after a context compaction)

Doc: "Mojave Caravan Company: full business design" https://claude.ai/artifact/C2FeS7JVVZXkTiDsAuQKLr
- project id 59414b69-47ea-4c41-a082-086947d153ff, tab file f649b8ef-b502, body node 9fb50fc4-71f9
- 2026-11-26 later: ALL sections filled except s1 .51 read-me-first and s21 .71 critic log (rev 23). Headings carry no
  numbers; cross-refs use section names ("see The road"). Export -> DOC-EXPORT.md (decode data.bytes_b64). Next: Opus
  critic on DOC-EXPORT.md + BRIEF.md, verdict file CRITIC-ROUND-N.md; revise; fill s21, s1; memory; shutdown.
- Round 1 REJECTED, round 2 REJECTED (CRITIC-ROUND-2.md: two-pot cash + deferred-strike fixes); all fixed, doc rev 113.
- Round 3 APPROVED (CRITIC-ROUND-3.md). All 7 non-blocking points + "Cassidy Caravans, reborn" applied, critic log and
  s1 verdict filled: doc rev 126. TASK COMPLETE. Left: memory, then shutdown /s /t 120.
  Output file CRITIC-ROUND-1.md. Max 3 rounds.
- Replacing a written block needs "ifHash" (h from the ack) + "ifRev" (rev of that ack) beside "op".
- Done (rev 13): s2 fantasy, s3 goals, s6 chains (heading id .16891, prose only, no diagram yet), s7 money, s8 growth
  (tiers table), s9 people, s10 road, s11 rival, s12 NCR/dodgy, s13 losing, s14 adventuring
- Still pending block ids (m7dx4trh9pg.N): s1 .51 read-me-first, s4 .54 loops, s5 .55 map, s15 .65 terminal,
  s16 .66 endgame, s17 .67 numbers, s18 .68 tech, s19 .69 build order, s20 .70 risks, s21 .71 critic log, s22 .72 sources
- Diagrams planned (topic.diagram, one batch each: widget create parent file f649b8ef-b502 + prose update):
  loop diagram in s4, chain flow after s6 heading, milestone roadmap in s19. Chart in s17 (day margins week 1).

Content notes for the pending sections (all decided by Claude, from the swarm reports):
- s4 loops: 5-minute visit; game day (06:00 morning report as a bookkeeper letter + table, tomorrow's forecast, <=3
  memos each with a default and a deadline); week (Sunday bills, statement, bookkeeper page, NCR bids); season of 28
  days (licence renewal, decrees, calendar: NCR payday, Strip fight night, rad storm week, Goodsprings harvest); the
  run (tiers). Away: standing orders, at most 1 letter a day (Pip-Boy note), while-you-were-away letter = what
  happened / money / <=3 decisions caused by the absence / one hook; postbag cap 5; served-notice rule.
- s5 map: Goodsprings HQ, Primm, Sloan, Mojave Outpost; routes GS-Primm, GS-Sloan, Sloan-Primm, Primm-Outpost; later
  Novac (Hwy 95), NCRCF contact; Nipton ruins = closed road. Interactive map in the visualiser
  https://claude.ai/artifact/XiPe2UdjwvPXT23HSCEvPd.
- s15 terminal: body text static; dashboard = button labels (<=259 chars); detail = result text pages; pooled
  pre-authored items with result scripts; screens = TERM forms: Front page, Report/letter, Memos, Price board (the
  Tape: best spreads, crates left to saturate), Routes and crews, Chains (bottleneck bars), Towns, Staff, Contracts and
  NCR, Ledger (P&L), Rival, Dodgy (hidden until a contact), Standing orders, Settings. Orders queue applied at the tick.
  Branch terminals in each town; portable "company ledger" item = live test. ASCII sparklines `_.-=*#`.
- s16 endgame: tier 5 politics: laws and lobbying (8-10 laws, favour points), patrons with strings (NCR quartermaster,
  Omertas, Mr. House's rep), Crimson merger or takeover, Dam regime switch, "20 years on" epilogue page written from
  the ledger, successor chapter.
- s17 numbers: worked week 1 (economy agent sim): day margins +746, +288, +94, +94, -117 (bandits), +124, +91; sales
  8,178, COGS 6,857, op profit 842, interest 120, net 722; principal 300; day-7 net worth 923. Balance targets table.
- s18 tech: quests CCCore (tick, 15 s), CCLedger (UDF maths), CCTerm (terminal bridge), CCWorld (near-player crews,
  tier visuals), CCEvents (load handlers); critical state mirrored in quest vars; arrays in cosave; enable-parent
  XMarkers per tier; new interiors, refs only, never edit vanilla; Alice offer via own quest topic; 5 live tests.
- s19 build order: M0 five live tests; M1 Goodsprings-Primm trade slice (tiers 1-2, loan, debt ladder, report,
  terminal, events lite); M2 chains, town levels, staff and managers (tier 3); M3 rival, NCR, dodgy (tier 4);
  M4 tier 5 and polish; then new towns.
- s20 open questions for the user: lose = successor vs gone (pick successor); goods mix (pick FNV + materials);
  one mod vs towns core + add-on; transient spawned road crews OK?; vanilla NPCs hireable? (pick no); permadeath of
  staff?; first raid always real?; chems and stolen gear in contraband?; Legion/House regimes in scope?; typed text
  box for naming?; HQ door refs in vanilla exterior cells OK?; letter as Pip-Boy note vs courier NPC.

Process left: fill sections -> export doc to markdown for the Opus critic -> revise (max 3 rounds) -> fill s21 + s1
-> update memory -> shut down the PC (user asked): `shutdown /s /t 120` (no /f, so unsaved apps can block it).
Usage: user on Pro plan, warned about usage; no more Sonnet agents; one Opus critic only.

Numbers fixed so far (keep consistent):
- Loan from Alice 3,000 caps at 4%/week on the balance, min 300 principal/week, early payoff free; equity 500; setup ~1,000.
- Crate = cargo unit; starting wagon + 2 brahmin = 8 crates. Anchors per crate: water 200, healing powder 100, ammo
  (100 rounds) 200, meat 100, stimpak 375, building materials 150, herbs 60.
- Price: r = stock/(3 x daily use); m = 0.5 + 1/(1+r); spread 10% -> 2% with trust and Barter; shortage refill 25%/day,
  glut drain 12%/day; news factor decays 25%/day.
- Wages per DAY: driver 10, guard 12, trader 20, workshop hand 14, manager 40, Science-70 chemist 60.
- Duty 2% of sales (3.5% above 5,000/wk, 5% above 20,000/wk); licence 150/month; brahmin feed 3/day; till limit 5,000.
- Debt ladder: Forecast (runway<5) -> Missed (10% fee) -> Grace 3d -> Final notice 2d (cure 60%) -> Seizure (60%)
  -> Receivership d+7. Served-notice rule. Probation 14d. Rescue lenders NCR 6%/wk, Alice 8%/wk, Omertas 25%/wk.
- Heat 0-100: 20 Noticed, 40 Watched, 60 Hot (raid possible, NCR contracts frozen), 80 Raid imminent, 100 raid now;
  revocation = second raid within 28 days at heat >= 80. Decay 2/day (4/day when clean 7 days).
- Tier net-worth targets (to tune): T2 Outfit 2,000; T3 Caravan company 8,000; T4 Trading house 25,000; T5 Mojave
  concern 80,000.
- Vanilla flags: Goodsprings safe GetStageDone VMS16 100; lost VMS16b 100; Primm sheriff VStoryEventPrimm==1,
  VStoryEventPrimmSheriff 1 NCR/2 Meyers/3 Primm Slim; Quarry cleared vFreeformSloan.bDeathclawLeadersDead==1;
  Heartache VCassCompanion 100/110; You Can Depend on Me VMS05; Alice AliceMcLafferty 000EC7A1 (may be dead).
- Tech: terminal body text is static; live numbers in button labels and result text (259 chars each); actions need
  pre-authored pooled items; JG RefreshTerminalMenu redraws; Computers menu 1057; day tick by GameDaysPassed compare;
  arrays in cosave, mirror critical state in quest vars; caravans = transient spawned crews near the player (user Q).
- 2026-11-26 later: user answered all 15 decisions; all picks kept except #15 ride the wagon (NO, removed from the doc). Doc rev 143. DOC-EXPORT.md is from rev 126 (before this).
