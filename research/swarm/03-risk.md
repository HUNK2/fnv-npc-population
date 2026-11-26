# 03 - Failure, risk, tension and pacing

Agent angle: lose condition that does not feel cheap, growth that stays earned. Written 2026-11-26.
[D] = documented by the page opened. [O] = player/reviewer opinion. Pages that refused (Fandom wikis, 402; Fextralife, DNS) were skipped.
Time base: timescale 30, 1 game day = 48 real min, 1 game hour = 2 real min, 1 week = 7 days = about 5.6 real hours.

---

## 1. Key findings

**RimWorld: growth attracts danger, with a soft cap and a mercy valve.**
Raid Points = (Wealth Points + Pawn Points) x Threat Scale x Starting Factor x Adaption Factor. Wealth counts items + creatures + 50% of buildings. The wealth curve is flat at 0 below 14,000, 2,400 at 400k, 3,600 at 700k, 4,200 at 1M and above, linear between. Starting Factor is 0.7 for the first 10 days, 1.0 from day 40. Adaption Factor falls when colonists die or are downed (a 30-day grace first), so a battered colony gets gentler raids. Base total capped at 10,000. [D] https://rimworldwiki.com/wiki/Raid_points (community wiki, flagged by its own editors as possibly dated; use the shape, not the numbers). RimWorld's storytellers differ in downtime: Cassandra rises and falls, Phoebe gives longer rests, Randy is random. [D] https://en.wikipedia.org/wiki/RimWorld
Lesson: three dials (wealth, grace for new players, adaptation after losses) make a director fair without a difficulty cliff. The soft cap stops late-game rich players being deleted.

**Frostpunk: the final warning is a menu, not a timer.**
Hope 0 or Discontent 100 triggers a "city in dire trouble" message with solutions: two need specific buildings, the third is an ultimatum: move an indicator by 15% within two days or be banished and lose. [D] https://www.gamepressure.com/frostpunk/what-happens-when-discontent-or-hope-reach-critical-values/zfad7c . Hope was added because the developers saw it as essential to survival; both meters must be balanced. [D] https://en.wikipedia.org/wiki/Frostpunk
Lesson: a short, specific, achievable cure with named options turns losing into a puzzle. Both a "good" meter and a "bad" meter give two things to watch.

**FTL: pressure is a clock that makes waiting costly.** Each jump spends fuel and advances the rebel fleet, so lingering costs; more beacons = more reward and more exposure; designers tuned for about a 10% win rate and made restarts cheap, framing each loss as learning. [D] https://en.wikipedia.org/wiki/FTL:_Faster_Than_Light
Lesson: risk is a choice of how many nodes to touch, not a dice roll on a screen the player cannot influence.

**Into the Breach: telegraph everything.** Enemy attack targets are shown a turn ahead; the loss resource (grid power) is lost in visible chunks; losing a run lets one pilot time-travel to a new run keeping experience. [D] https://en.wikipedia.org/wiki/Into_the_Breach . Slay the Spire switched from hidden enemy moves to visible "Intents" after playtesting. [D] https://en.wikipedia.org/wiki/Slay_the_Spire
Lesson: losses feel fair when the player saw the threat and had a response. A forecast line on the terminal is the single best anti-cheapness device.

**This War of Mine: a fixed-length ordeal.** The war ends in a ceasefire after a randomized duration, so players know it ends. Moral choices at night decide what ending each survivor gets. [D] https://en.wikipedia.org/wiki/This_War_of_Mine
Lesson: dilemmas (help, rob, ignore) with consequences that are remembered, not just paid in caps.

**Darkest Dungeon: stress as a second health bar, relief costs money.** Stress rises from darkness, hunger, deaths and blights; afflictions repeat in patterns players can learn; extreme stress can cause a heart attack; the Hamlet sells stress relief and recruitment. [D] https://en.wikipedia.org/wiki/Darkest_Dungeon
Lesson: a staff "Nerves" meter makes loss cumulative and gives cash a second use (relief).

**Banished: danger collapses once you are big.** Reviewers said difficulty drops as the town grows and survival gives way to management, with no late goal. [O] https://en.wikipedia.org/wiki/Banished_(video_game)
Lesson: if threat does not rise with the company, growth feels free. Hence wealth-scaled danger.

**Recettear: one hard deadline, restart keeps the player, not the money.** Miss the debt deadline and you restart keeping merchant level and items, not pix. Survival mode adds weekly rising payments. [D] https://en.wikipedia.org/wiki/Recettear:_An_Item_Shop%27s_Tale

**Rogue Legacy: legacy via heirs and an unavoidable toll.** Heirs inherit equipment and improvements bought with gold; unspent gold is paid to Charon to enter the castle (reducible by upgrades). [D] https://en.wikipedia.org/wiki/Rogue_Legacy . Hades: death is framed as progress and narrative (fresh dialogue after each death); meta-upgrades mostly change how runs play rather than raw stats. [O, search snippets only] https://www.avclub.com/hades-and-failure , https://saschb2b.github.io/game-mechanics/games/hades/meta-progression
Lesson: what survives death should be the player's knowledge and relationships, not their money.

**Sunless Sea:** permadeath, successors inherit some possessions, players can write a will to leave lodging and wealth. [D] https://en.wikipedia.org/wiki/Sunless_Sea . (Port reports as an away-time mechanic: nothing found.)

**Left 4 Dead director:** adjusts content to each player's stress to keep "constant tension"; cycles Build Up, Peak, Relax; stronger players get more hordes and fewer kits, struggling players fewer enemies and more first aid. [D] https://en.wikipedia.org/wiki/Left_4_Dead ; the cycle and adaptive behaviour [O, snippet] https://techraptor.net/content/10-years-of-left-4-dead . Valve's talk PDF (cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf) saved but unreadable here (no pdftoppm), so the exact numbers (intensity decay, relax timers) are unverified; I do not quote any.

**Idle/away design:** caps per resource set a return rhythm (cows cap every 20 minutes, creameries every 5 hours; players can fail one timer and win another). [D, author's design] https://ericguan.substack.com/p/idle-game-design-principles . Clicker Heroes chose no offline cap. [D] https://blog.clickerheroes.com/offline-progression-in-clicker-heroes/embed/ (snippet only). Opinion that a long absence should give a reason to return, versus caps that feel better: [O] snippets in the same search.

**Borrowing and bailouts:** Railroad Tycoon starts with $1M, half equity half loan, with more cash from bonds at rates tied to the economy. [D via search snippet] https://en.wikipedia.com/wiki/Railroad_Tycoon . A bailout as "a lump sum to keep insolvency away for a short while" appears only as a forum proposal. [O] https://forum.simutrans.com/index.php?msg=72810 . I found no shipped tycoon with a true insurance mechanic; the insurance design below is therefore original.

---

## 2. What this means for our mod

### (a) Refined lose design

**Principle:** you can lose the company, never the save. Failure is a ladder of visible rungs, every rung offers a cure, and no clock runs while the player is unaware or busy.

**Numbers shown on every terminal screen:** Cash, Weekly Bills (wages + rent + tax + loan service), and **Runway** = Cash / (Weekly Bills / 7), in game days. This is the Into the Breach "intent": the player always sees the next hit.

**Debt-ladder (cash path), in game days from the first missed bill (day 0):**

| Stage | Trigger | What happens | Clock |
|---|---|---|---|
| Green | Runway 5+ | nothing | - |
| Amber "Forecast" | Runway < 5 | Terminal banner + one Pip-Boy note: "Ledger forecast: short by ~X on bill day". No penalty. | gives up to 5 days notice |
| Red "Frozen" | Runway < 2 | New hires and purchases locked; the memo lists the cure menu | up to 2 days notice |
| Missed | Bill day, Cash < Bills | Pay what you can in this order: wages (staff walk if unpaid), tax, rent, loan. 10% late fee on the unpaid part. Notice is served. | day 0 |
| Grace | day 0 to +3 | Normal play; income continues; any sale or advance counts | 3 days |
| Final Notice | day +3 | The Frostpunk ultimatum: arrears (plus fee) must be cured to 60% within **2 days** or an asset is seized. Menu below. | 2 days |
| Seizure | day +5 | The creditor takes your highest-resale non-HQ asset, credited at 60% of value. If arrears now cleared: Probation. Else continue. | 2 days |
| Receivership | day +7 | Creditor takes the rest. Company ends. | - |

Total from first missed bill: **7 game days (about 5.6 real hours)**, preceded by up to 5 days of forecast. A player can sleep through the Amber banner but not through a Final Notice.

**Probation:** cleared arrears puts you on Probation for 14 days. A second miss during probation skips Grace (goes to Final Notice at day 0). This is the Papers Please "one strike" feel without a hard game over.

**Served-notice rule (the anti-punish-away device):** a stage clock starts when the notice is *served*: a courier NPC (placed, mod-tagged) walks to the player in a settlement, or the player opens the HQ terminal, or 10 game days pass and the Pip-Boy note fires. Until then Missed holds at Grace. Busy flags (section b) also freeze clocks. A player on a main quest in the Strip can never wake up to a dead company.

**Final Notice menu (the Frostpunk three-option ultimatum, extended):**
1. **Sell assets** (instant): wagons and cargo at 60%, workshops at 50%, warehouse stock at 70% to a named buyer. Terminal shows each item with its sale price and "what you lose with it".
2. **Contract advance**: a town or the NCR pays 50% of a booked contract now; you must deliver within 6 days; failing it costs 1.5x the advance and a Standing hit. Creates a real mission the player can escort personally.
3. **Rescue loan** (see below): one creditor, one price, one strings list.
4. **Personal injection**: move caps from your own pocket (the company/personal wall is real, so this is a real choice). Interest-free, but you can never take it back as dividend until Probation ends.
5. **Walk away**: wind up the company yourself (section a, "what you keep"), which gives better terms than Receivership.

**Rescue loans (all three are bailouts with teeth):**

| Lender | Amount cap | Price | Strings | Failure aftermath |
|---|---|---|---|---|
| NCR Treasury Office (Mojave Outpost) | 3x Weekly Bills | 6% per week, over 4 weeks | NCR priority: you must run 2 NCR contracts per week at set rates; **heat cap 20** (no smuggling); an auditor NPC inspects the office monthly | Assets seized, licence "under review" |
| The Kings (Freeside) | 2x Weekly Bills | 10% per week, 3 weeks | A Kings guard rides on every Freeside route (free guard, 25% less profit there); they get a seat in the Freeside warehouse | Kings take the Freeside lines |
| The Omertas (Gomorrah) | 5x Weekly Bills | 25% per week, 2 weeks, no paperwork, no Standing check | A silent partner takes 20% of profit; you carry their sealed crates (unlisted, raises heat 5 per trip) | Collectors break assets (lose 1 wagon/week) and a hit-squad encounter at your HQ |
| Alice McLafferty (Crimson Caravan) | 4x Weekly Bills | 8% per week, 4 weeks | **Takeover clause**: a missed payment gives her a branch in your office (the vanilla Alice-buys-failing-company story, so it fits) | Takeover, see below |

Rates are numbers to tune; the shape matters: cheap and legal comes with tight rules, quick and dirty comes with consequences you can see. Standing (0-100 credit score with each lender) shifts the rate by up to 4 points either way.

**Second lose condition, NCR shutdown (dodgy path).** Heat 0-100, decay 3 per day. 40: "Notice of inquiry" (letter). 60: audit + raid on the office; contraband confiscated and fined 2x its value (one hit, not a death). 80: licence suspended 5 days, no NCR roads. 100: revoked, same as Receivership but the NCR owns the leftovers and the player is **barred from Mojave Outpost registry for 14 game days** (can still walk in, cannot trade licensed). Stage language mirrors the debt ladder: Inquiry, Hearing (+3), Suspension (+5), Revocation (+8). Cure at the Hearing: pay a fixer (Kings lawyers, 2x heat in caps), turn informant on a rival (Crimson Caravan, risky), or burn the contraband. Heat is visible on the terminal next to Runway.

**Pick: start over smaller, not gone for good.**
Arguments: (1) The mod runs inside one save with the main quest; "gone forever" makes a bug or a bad week a reason to reload or uninstall. (2) Sunless Sea's author moved to Legacy because death felt too punishing (from BUSINESS-RESEARCH sec 1; [D]), and Recettear keeps levels on restart [D]. (3) Rogue Legacy's heirs keep upgrades but pay a toll [D]; the toll principle (you do not keep your money) keeps stakes real. (4) Gone-for-good teaches nothing; there is no second attempt to use what you learned.
Counter: pure "start over with everything" removes sting. So the pick is **a Legacy with a real price**:

*Kept:* the company name and founder's reputation as a story (towns remember: Standing in each town halved, Goodsprings kept), unlocked recipes and production chains (knowledge), discovered routes, one loyal manager (your top-rated; others scatter and can be re-hired at 120% wage), the player's own caps (the company/personal wall pays off here), 5% of old peak net worth as seed (cap 1,500 caps) so the restart is a Peddler with a wagon and one guard.
*Lost:* every building, wagon, cargo, contract, all market share (rival gets it), tier, and the HQ: Goodsprings office becomes a Crimson Caravan branch (visible sign, her clerk NPC). Buy-back later costs 2x the original building price, and must be earned with a rival-reclaim quest.
*Debt tail:* Receivership leaves a **Receiver's Note**: 25% of the unpaid arrears, interest-free, due over 4 weeks, but with no seizure risk. Walking away yourself (before Seizure) waives this. This is the sting and the reward for acting early.

### (b) Pacing director

**Inputs (recomputed each morning):**
- W = Cash + Stock value + Wagons + 0.5 x Buildings (RimWorld counts buildings at half [D]).
- WealthPts(W): linear interpolation of: 0 at W <= 500; 80 at 5,000; 300 at 40,000; 700 at 250,000; 1,000 at >= 1,000,000. (Soft cap like RimWorld [D].)
- RoutePts = 12 per active route + 6 per wagon in the field.
- Visibility V = 1.0 + 0.1 per town where your share is above 40%, + 0.05 per Crimson Caravan "war" memo outstanding (range 0.8 to 1.4).
- Grace Gr = 0.6 for the first 10 company days, rising to 1.0 by day 30. (RimWorld Starting Factor [D].)
- Adapt A = 1.0 at start; -0.12 for each serious loss (floor 0.7); +0.02 per quiet day after day 7 (cap 1.2). (RimWorld Adaption [D].)
- Setting D = difficulty slider (0.6 / 1.0 / 1.4).

**ThreatPts = (WealthPts + RoutePts) x V x Gr x A x D.**

**Event danger by class:** nuisance 0.35 x ThreatPts, standard 0.6, crisis 0.9. Example: Peddler, W 1,500 (WealthPts 24), 1 route + 1 wagon (18), Gr 0.6: ThreatPts about 25. Caravan company, W 60,000 (WealthPts about 340), 6 routes + 8 wagons (120), V 1.1: ThreatPts about 500. Trading house, W 600,000: about 1,100 and rising slowly.

**Guard Cover G:** rookie 20, veteran 45, elite 90, armoured wagon +15%, scout +10% per road, brahmin escort +5.
**Paper resolution:** Success chance P = r^2 / (1 + r^2) with r = G / D, clamped 5%-95%. So r = 1.0 gives 50%, 1.5 gives 69%, 2.0 gives 80%. Outcomes: success = clean pass; otherwise 70% pyrrhic (lose 30% of the cargo, a guard wounded, 1 day delay), 30% loss (lose cargo and wagon, a guard killed, named). Rule of thumb shown on the terminal: **"Keep G at 0.7 x ThreatPts to meet standard events at about 66%."** Peddler (ThreatPts 25): one rookie (G 20) vs nuisance D 9 (r 2.2, 83%), standard D 15 (r 1.3, 63%), crisis D 22 (r 0.9, 45%). A caravan company at ThreatPts 500 with 10 guards (4 veterans, 6 rookies = G 300): standard D 300, 50%; crisis D 450, 31%. So wealth growth outruns a lazy guard budget and the player must keep paying for safety, which is the intended RimWorld-style feel.

**Cadence (L4D-style, tracked by a Stress meter S 0-100):** S += 25 per crisis, +10 standard, +5 nuisance, +3 per unresolved memo, +5 when Runway < 3; -8 per game day. Rules: no crisis if S >= 30; after any crisis, 2 Relax days with only good or dilemma events; max 1 crisis per 3 days at Outfit, 1 per 2 days at Trading house; no bad event on bill day or the day before. Roll the director once per game day at 06:00 inside the morning report. Event frequency by tier: Peddler 1 per 3 days, Outfit 1 per 2.5, Caravan company 1 per 2, Trading house 1 per 1.5, Mojave concern 1 per 1. Mix: 45% bad, 30% good, 25% dilemma, with a 3 percentage point shift toward good for every quiet day beyond 4. Cassandra/Phoebe-style presets: "Cassandra" (default, rises and falls), "Phoebe" (long relaxes, half crisis rate), "Randy" (random, +-50%).

**Never hit the player in a main quest (Busy shield).** Busy = any of: in combat or dialogue; inside a quest-flagged cell or within 300 units of a quest marker for an active quest on a short list (we maintain: all main-line quests of the four factions, DLC main quests); in a hostile interior; player level below 5 for the first 4 game days; Cass's "Heartache by the Number" while Crimson Caravan stage is active. While Busy: (1) no *Real* events (no radio calls), (2) paper events queue up to 3, shown next morning, (3) paper losses capped at **cargo only** (no guard deaths, no wagon loss, no asset seizure) and a total of 15% of Net Worth per day, (4) debt-ladder clocks freeze. This is the Valve "protect the player from overload" principle applied with a hard flag.

**Away mode (idle-game rule):** if the HQ terminal has not been opened for 5 days, enter Away: ThreatPts x 0.7, events at half rate, bills auto-paid from cash. Good events accumulate in a **Postbag** capped at 5 items (rhythm cap like the idle designers' creameries [D, Eric Guan]). The return screen: "While you were away: 3 deliveries, 1 skirmish held, 2 offers waiting." Fleet effects (market share lost to Crimson) happen at half pace.

### (c) Road event deck (24 events)

Format: trigger / choices / outcome / paper vs real. "Paper" = resolved at the 06:00 report with the formulas above. "Real" = a radio call (6 game hours = 12 real minutes window) lets the player go; if they ignore it the event resolves on paper with Guard x 0.9. Danger D class in brackets.

**Bad (11)**
1. **Jackal-Viper Ambush on the Primm road.** Trigger: route Goodsprings-Primm active and Powder Gangers freed or no sheriff in Primm (vanilla state). [standard] Choices: guards fight / pay toll (10% of cargo) / reroute (+1 day). Paper: P as above. Real: placed raider group spawned on the road; killing them gives +Standing and removes this route's danger +20% for 5 days.
2. **Cazador swarm at night, Sloan route.** Trigger: caravan travels 20:00-04:00 on Hustle setting. [crisis] Choices: camp till dawn (delay 6h) / press on / burn flares (cost 20 caps, halves D). Paper: roll. Real: spawn 3 cazadors near a wagon; poison kills the brahmin if unsaved.
3. **Deathclaw on the Quarry Junction road.** Trigger: Quarry Junction not cleared (vanilla quest state) and a route touches Sloan. [crisis] Choices: abandon route 5 days / hire an escort (player can go) / pay hunters (400 caps). Paper: D at 0.9 with armoured wagon bonus; losing means a wagon plus guard. Real: the player kills it, and the route's stone yard opens early.
4. **Axle break / lame brahmin.** [nuisance] Choices: repair (Repair 25 hire or 60 caps), leave wagon and carry on with half cargo, hail the nearest town. Paper: 1 day delay and a repair bill. Real: player fixes it with scrap metal.
5. **Dust storm.** [nuisance] Choices: wait (lose one day, lose nothing) / press on (+Hustle bonus, +25% loss risk). Paper: random. Real: weather swap for the player's trip.
6. **Powder Ganger toll.** Trigger: any route near Primm, escape-state vanilla. [standard] Choices: pay 15% / fight / bribe boss with 5 lead boxes. Paper: P. Real: a stop-and-talk scene.
7. **Crimson Caravan price war.** Trigger: your share in a town above 35%. Alice's agents undercut by 20%. Choices: match (-10% margin for 7 days) / concede the town for 14 days / sabotage (dodgy, heat +10, 40% they find out). Paper only; the terminal shows both numbers.
8. **Rival poaches a manager.** Trigger: manager skill above 60 and wage below market. Choices: counter-offer (+25% wage), let go, bluff (Speech check by the player: success keeps him at no cost; fail he leaves and tells her your margins). Paper; Speech check is a terminal option gated on Barter/Speech.
9. **Spoilage in the sun.** Trigger: food or medicine cargo in heat plus delay. Choices: rush-sell at half price / mark the loss / mix batches to preserve one. Paper only.
10. **Insider theft.** Trigger: warehouse stock count off 5%+ and a low-morale clerk. Choices: audit (costs a day of ledger) / fire the suspect / ignore. Paper only; if the player ignores it, three days later a "mystery" attracts heat.
11. **NCR inspection with contraband aboard.** Trigger: smuggling crates in transit. Choices: bribe (30% of crate value) / hand over crates / hide (Sneak roll for player; auto for a trained hire) / run. Paper: P by hire skill; Real: the player talks to the patrol sergeant at a checkpoint.

**Good (6)**
12. **Stranded caravan found.** Trigger: Away mode or quiet day. A rival's lost wagon on the road. Choices: salvage (take cargo), rescue (they owe you, +Standing +10, an offer to join), report to NCR. Paper: good by default. Real: a scene on the road.
13. **Price spike.** Trigger: a vanilla event (Powder Ganger raid, NCR sweep) closes a market. Choices: sell now at +40% / hold and gamble for more (+70% or fall to -10% in 3 days). Paper.
14. **NCR bulk order.** Trigger: NCR operational need. Fixed price -10% for 100 units in 6 days. Choices: accept, decline, counter at +10% (Speech). Real: the player can go meet the quartermaster.
15. **Veteran drifter.** Offers service as an elite guard (rating 90) at half wage for 14 days, but he wants a favour: a name on a manifest. Choices: hire / hire and do the favour / refuse. A callback event 7 days later reveals why.
16. **Town honours you.** Trigger: town trust 60+. The mayor offers an exclusive: only you may sell medicine there for 10 days, but he asks that prices be capped. Choices: accept, decline. Paper; shows "Your sign now hangs in the main street".
17. **Windfall buyer.** A visiting trader buys a surplus at +25%. Paper only. A tiny reward for staying alert.

**Dilemma (7)**
18. **Wounded NCR trooper hitchhikes.** Choices: carry (+2 days, +NCR Standing, trooper offers a Ranger contact) / refuse (no cost, the trooper may later turn up on a "told of your refusal" line). Real: a short escort.
19. **Unmarked crates.** Found on an abandoned wagon. Choices: keep (value 300, heat +8) / return to owner (small reward, Standing) / report (NCR Standing +5, no cash). Paper picks the safe default if Busy.
20. **Captured raider.** Guards win and hold a raider. Choices: release (heat unchanged, a chance he warns others), ransom (150 caps, he returns), hire as a guard (rating 20, 20% chance of a theft event later), execute (morale +, NCR dislikes if witnessed).
21. **The Kings' protection offer, Freeside.** Pay 10% of Freeside profit: guaranteed safe passage there and Kings Standing up, but Alice hears of it (her Standing cools). Choices: pay / refuse / negotiate (Speech).
22. **Credit request.** A town trader asks for 14 days' credit on 400 caps of goods. Choices: grant (+Standing, 25% chance of default, otherwise +10% margin) / refuse / partial (200 caps now). Paper; outcome shows as a ledger line a week later.
23. **Informant.** A clerk says NCR will visit within 3 days. Choices: pay him (80 caps) to learn when and which route, hide the contraband (cost 1 day), ignore. Heat-linked; this one is a gift to the dodgy path, where it reduces raid damage by half.
24. **Overnight at the shack.** Wagon stops at a roadside shack where a stranger sells "cheap" water. Choices: buy 20 purified water at 50% (30% chance it is irradiated, ruin one cargo slot), decline, test it (Science check, hired chemist reveals). Real: the player talks to the stranger and can inspect.

Every event keeps the terminal output short: a headline, the telegraphed threat, 2-4 menu choices with a preview of expected cost, and a link to "Details". Choices are limited by terminal menu constraints; Speech and Sneak checks are done on the player's skill read from script, not typed.

### (d) Insurance, guards and risk as player decisions

- **Route stance dial (per route):** Cautious (danger x0.7, profit x0.85, +1 day), Standard, Hustle (danger x1.5, profit +30%, spoilage +20%). The player sets it in the route menu; Hustle is the FTL "touch more beacons" choice. [FTL D]
- **Guards:** hire per wagon (rookie 20 caps/day wage, veteran 45, elite 90 plus a quarterly bonus). A guard that survives three fights gets a name and a trait ("Hank Brightwell, steady"). Elite guards must be recruited by a deed (clear a place with the player).
- **Armoured wagon** (workshop item): +15% G, costs 400 caps; **scouts**: +10% G and visible forecast of a route's danger next day.
- **Insurance, original design:** Four ways to buy cover, each with a distinct price and catch.
  1. **Crimson Cover** from Alice: 3% of cargo value per trip, pays 60% of lost cargo and wagon within 2 days, no deductible. Catch: she gets your route manifests (her raid events target your routes more cheaply; her price war chance +10%).
  2. **NCR war-risk indemnity**: free, but only for NCR-contract cargo and requires no contraband and a Standing 40+. Pays 80%.
  3. **Reserve fund** (self-insure): set aside 10% of weekly profit; pays out up to the fund, no strings, no cap on events covered, but empty at the start.
  4. **Omerta "assurance"**: 5% of cargo value per trip, pays 100% and covers contraband, but a Gomorrah "collector" visit follows every claim.
  Premiums and payouts show on the ledger as separate lines so the player can compute whether insurance is worth it. Contraband is never covered by 1-3 (an excluded loss), which pushes the dodgy path toward 4.
- **Heat and nerves:** the Heat meter is the dodgy-path risk; staff **Nerves** (Darkest Dungeon stress [D]) rise on every violent event and fall with a day off at the Prospector Saloon (cost 15 caps per head) or a bunkhouse upgrade at HQ (the Hamlet [D] equivalent, 600 caps, halves Nerves growth). At Nerves 80 a manager quits mid-week.
- **The "Hail Mary" contract:** at Final Notice, one high-risk contract (150% pay, D x1.5) appears; if it succeeds before the clock ends it cures the ultimatum. Fail and the seizure still happens. It is a decision, not a free pass.

### (e) Loss that stings but heals in 1-3 game days

1. **Event losses are capped**: no single event removes more than 30% of Net Worth; shielded events (Busy) cap at 15%.
2. **Named losses**: "Wagon 'Dusty' lost, driver Hank dead" appears in the morning report in red, then the ledger. Names make it sting without costing more caps.
3. **Salvage window (2 game days)**: a lost wagon leaves a wreck marker; if the player goes there, they recover 50-80% of cargo. If not, the Salvage tab expires.
4. **Rebuild fast, not free**: the Wainwright (workshop) rebuilds a wagon in 2 game days at 60% cost; hired guards can be re-hired the same day.
5. **Underdog contracts**: after a serious loss, for 3 game days towns post contracts at +15% ("People are rooting for you"). Opposite of death spiral; aligns with Hades's "failure feeds progress" [O].
6. **Adapt falls**: ThreatPts drops (A -0.12) after a serious loss, so the next 7 days are gentler, [RimWorld D].
7. **Loss must have a cause on the screen**: every bad event ends with a "What went wrong" line that names the cheap fix ("Guards below cover for this road; add one veteran").
8. **No loss on the day you first reach a tier** (a 2-day amnesty). Growth must feel earned before the director punishes it.

---

## 3. Bold ideas

1. **Intents on the terminal.** The morning report opens with tomorrow's forecast in Into the Breach style: "Jackal band near Primm road, est. strength 60 +-20. Your cover on that road: 45." Choose: stay, reroute, reinforce, or go yourself. Build: medium, because it only needs the director to pre-roll the event one day early and store it. Fun: the player is making decisions with information, not being surprised.
2. **Walk-away wind-down.** At Final Notice, option 5 is a graceful exit. You keep more than in Receivership, and the company name gets a "wound-up" memorial plaque in the Goodsprings office. Build: easy (a different end state). Fun: a controlled, dignified way to quit a doomed run.
3. **The takeover arc.** If Alice takes you over, the player is offered a job as branch manager of their own former company; run it as hers for 14 days to earn a buy-back option at 1.5x. Build: hard (requires a second UI mode), but strong narrative. [D from the brief: vanilla Alice bought out Cass's family company]
4. **Dead man's route.** After you lose a wagon on a road, that road gets a roadside grave and a persistent note on the map; clearing the threat lets you "lay the wagon to rest" for a Standing bonus. Build: easy with placed refs.
5. **Contract sweat.** The "Hail Mary" contract (above) is a signature moment: one job, one chance, a clear price. Build: easy (a contract with big numbers and a deadline).
6. **The Reckoning memo.** A weekly one-line verdict from your accountant NPC with the real cause of your numbers ("Runway 4 days; two bills, one wagon's wage, one 'creative' expense"). Gives the P&L a voice.
7. **Insurance spy.** Crimson Cover as a Trojan horse: the player chooses cheap cover, then watches Alice's undercutting become surgically precise on their routes. Build: easy (a flag).

---

## 4. Pitfalls and design flaws to avoid

- **Hidden losses.** Capitalism-style takeovers that happen unseen are hated [O, BUSINESS-RESEARCH sec 1]; every stage must be in the terminal first.
- **A clock that runs while the player is away.** Fix: served-notice rule, Busy freeze, Away mode.
- **Bills killing a rich-but-illiquid company.** A company with huge stock and no cash gets seized while worth millions. Fix: sell-assets option is always one menu away with a fair price; auto-liquidate lowest-value stock at 70% (opt-in) at Missed.
- **Death spiral.** Seizure takes the best asset, income falls, next bill is worse. Fix: Probation (14 days) and underdog contracts; Receivership pays out 40% of net assets to the player as founder's payout (Walk away).
- **Wealth-scaled danger deleting the late game.** RimWorld uses a soft cap [D]; so do we (WealthPts max 1,000). Without it, a Mojave concern with 5M caps would face 10,000 ThreatPts.
- **Banished's collapse of tension** [O]: tying danger to wealth avoids "easy when large". But also avoid the opposite: do not let a lazy player be unbeatable. The guard rule-of-thumb tells them how much to invest.
- **Events that need the player to be there.** Radio calls are optional; the paper default must be about as good as an average player, so busy players are not punished and attentive players earn a bonus (bonus = no roll, plus Standing).
- **Insurance as a free lunch.** Cover should be a small net loss in expectation unless the player gets the exact event it was designed for; otherwise it is a "must buy". Premium 3% vs average loss 2% of cargo (so slightly negative EV, positive variance reduction). Tune later.
- **Alice as both lender and rival and insurer.** Three hats on one NPC may feel contrived. Keep her as the only one who can *take* your company; NCR, Kings, Omertas are the others.
- **Copy-paste events.** 24 events cycle every 2-3 weeks; add variation by town, vanilla quest state, named crew and company tier. Adding a "memory" (the Kings remember if you refused them) makes repeats feel different.
- **Terminal text.** Walls of text bury the choice. Limit: headline + 3 lines + 2-4 options, no scrolling.
- **Frostpunk-style exile as the end.** Our final stage must not look like an unfair game over; the ending card is a memorial, not a failure screen.

---

## 5. Questions only the user can answer

1. Pick between "start over smaller with a Legacy" (my pick) and "gone for good (new company name, nothing kept)". If the second, does the player keep their own caps and perks?
2. Should the Crimson Caravan (Alice) be both rival and lender-of-first-resort? It makes the takeover story but may feel like one NPC does everything.
3. Is a visible "Heat" meter acceptable, or should the NCR path stay hidden and only show letters?
4. Is a per-event cap (30% of Net Worth, 15% when Busy) too soft for players who want a harsh game? Offer a "Hard" preset that removes the cap and the Busy shield?
5. May the mod freeze debt clocks while the player is in main quests (the Busy flag needs a maintained quest list)? Or should it be "ask the player at first launch: harsh or kind"?
6. Are insurance products (including the Alice Trojan horse) welcome, or too much to read on a terminal?
