# 09 - Wildcard: gameplay a normal tycoon would not have

Written 2026-11-26. Angle: new gameplay approaches that fit a caravan company run from a menu-only terminal inside an
RPG. Tags: [D] documented by a page I opened, [O] opinion, [M] from my own memory of a game or history, page NOT opened
this session (treat as unverified). Pages opened are listed per finding.

## 1. Key findings (what the sources actually say)

- **Lloyd's coffee house sold information first, insurance second.** Edward Lloyd served sailors, merchants and
  shipowners "dependable shipping news"; from 1691 a pulpit announced shipping news and auction prices; he printed
  Lloyd's News (1696) and a List followed in 1734; insurance was arranged among members at the tables, and the
  members formed the Society of Lloyd's in 1774 [D] (en.wikipedia.org/wiki/Lloyd's_Coffee_House). Lesson: a place
  where news is read aloud and risk is split among many is a game of its own.
- **Dojima rice exchange: the futures idea came from paper money.** Daimyo and samurai were paid in rice; brokers
  stored it in warehouses, kept what were effectively bank accounts for lords, and issued paper against rice; futures
  trading (nobemai) appears around 1710; speculators tried to corner the market; the shogunate set a price floor in 1735
  (42 momme per koku, fine for selling below) and re-founded the exchange under government sponsorship in 1773 [D]
  (en.wikipedia.org/wiki/Dōjima_Rice_Exchange). The article does not explain contract terms, so I do not claim them.
  Lesson: a promise to deliver later is a product, and a government that fixes a price creates a smuggling market.
- **Pony Express: a heroic business that lost money.** 186-190 stations 5-25 miles apart, swing stations for fresh
  horses, riders doing 75-100 miles a run, 10 days for 1,900 miles; grossed about 90,000 dollars, lost about 200,000;
  the Paiute War cost about 75,000 in stock and killed 16 staff; the telegraph ended it two days after it reached Salt
  Lake City; assets sold to Wells Fargo for 1.5 million in 1866 [D] (en.wikipedia.org/wiki/Pony_Express). Lesson: a
  company can be loved, famous and bankrupt, and it can be bought by a bigger one with its name kept.
- **Pax Pamir: you are never independent.** Players work for one of three empires, can switch coalition, and score
  according to how favoured they are within the winning coalition; market cards get cheaper as others are bought and
  every cheaper column collects your coins [D] (en.wikipedia.org/wiki/Pax_Pamir). Lesson: patrons whose success
  and yours are tied, with a way to defect, make a good strings system.
- **King of Dragon Pass: two big decisions per season, events shaped by past choices, and a seven-member ring you
  have to keep calm** [D] (en.wikipedia.org/wiki/King_of_Dragon_Pass). This is almost exactly our "1-3 memos a day"
  cadence, and the "people around the table have opinions" part is what a manager roster could copy.
- **Cultist Simulator: verbs with slots and timers.** You put cards (people, items, money) into a verb box, commit,
  a timer runs, you collect output cards; harmful timed verbs eat wealth and create Hunger if you have none [D]
  (en.wikipedia.org/wiki/Cultist_Simulator). A terminal menu can do "pick three things for one job, wait" with no
  typing.
- **Sunless Skies: death becomes inheritance.** New captain after death; some belongings and all story progress
  carry over, the map is re-obscured [D] (en.wikipedia.org/wiki/Sunless_Skies; BUSINESS-RESEARCH.md says the developer
  moved to Legacy because death felt too punishing).
- **Hudson's Bay Company: a unit of account and a standard of trade.** The Made Beaver (a prime pelt) priced every
  good, other pelts quoted in MB equivalents (two otter = 1 MB), one Standard of Trade across Rupert's Land;
  trading was a formal ceremony; factors ran posts [D] (en.wikipedia.org/wiki/Hudson%27s_Bay_Company). The page
  also records the trade in enslaved people, so that part of history stays out of our design. Lesson: your own unit of
  account (a "load" or a company chit) makes a company feel like an institution.
- **Food Chain Magnate**: the wiki page had almost nothing on mechanics (2-5 players, 180-420 min, no chance after
  setup) [D]. What I know about its milestones and employee tree is [M]: milestones are one-shot cards that only
  the first claimant gets, so rivals are locked out. I use it only as a pattern.
- Not opened (so [M] only): Papers, Please inspection loop, Frostpunk laws, Reigns, Concordia, Brass, Merchants of
  Venus, Offworld, EVE, Victoria, 80 Days (the Wikipedia page was only a disambiguation), Oregon Trail, Banner Saga.

## 2. Concepts (17), each with play, feeling, fit, cost, risk

Cost: S under a week, M a few weeks, L a month or more of mod work. All fit the terminal rules (menu choices,
notes, submenus, JohnnyGuitar menu edits).

### C1. The Pulpit: rumours as goods (Lloyd's)
- **Plays:** Each morning the terminal shows 3 "word on the road" lines, each 60-90% reliable: "Water short in Primm
  this week", "Powder Gangers moving on the Nipton road". You can act now, or buy a scout's report for 40c to firm one
  up, or sell a rumour you hold to Alice for 60c (and she acts on it). Rumours are cargo-sized items in your ledger.
  Example: you pay a Sloan miner 30c, learn the stone yard price will jump; you front-load a run and clear +120c.
- **Fun:** being the one who knew first; detective-ish; sometimes being wrong.
- **Fit:** pure numbers plus text. Ties to vanilla state (a rumour can be true because a quest flag moved).
- **Cost:** S-M. **Risk:** low; needs a believable accuracy model so lies are not just noise.

### C2. Forward contracts: "the Dojima ticket"
- **Plays:** At the Wednesday terminal you may sell next week's water at today's price: "Mojave Outpost garrison:
  400 purified water at 3c each, delivered by Day 14." You must then make it, even if the spring dries. A guaranteed
  buyer lets you borrow against it. Missing a delivery costs the penalty and trust. Speculators (Alice) will buy your
  tickets cheap if you are short.
- **Fun:** planning, a real bet you can feel; the thrill of a delivery landing on the last day.
- **Fit:** the whole thing is a menu row with a deadline; the game already has weekly bills. Pairs naturally with
  the loan (a ticket is how you get out of a hole).
- **Cost:** M. **Risk:** moderate; contract rows need clear on-screen deadlines (visible fixed deadlines were a
  lesson from BUSINESS-RESEARCH.md).

### C3. Syndicate insurance (Lloyd's tables)
- **Plays:** Before a run you choose cover: none, "half" (premium 8% of cargo value), or "full" (15%). The underwriters
  are named NPCs (Mr. House's rep, a Followers doctor, a Primm bar owner), each with their own appetite. After a loss
  the claim is paid, but your premium rises and one underwriter may drop you. In reverse: at tier 4 you can underwrite
  small outfits (Primm's traders) and earn premiums until a bad year.
- **Fun:** safety nets you design, then a nail-biting road event where cover decides whether you survive; the
  late-game flip to being the bank.
- **Fit:** converts the "caravan lost on the road" penalty (already proposed as piece loss) into a choice made in
  advance, which makes the loss feel fair.
- **Cost:** M. **Risk:** low-moderate; premium table must not trivialise danger.

### C4. Patrons with strings (Pax Pamir, with FNV factions)
- **Plays:** From tier 3 you may take an investor: NCR Quartermaster (cheap money, must hold NCR contracts and refuse
  smuggling), the Kings (Freeside goods only, protection from Freeside gangs), the Omertas (cash, ask for shipments
  you must not inspect), Mr. House (large capital, asks to see your ledger and may veto routes), Brotherhood
  (sells you old-world machines, wants nothing but tech on your caravans). Each gives a lump sum and a standing "strings"
  line on your terminal. Break a string and the patron calls the loan or leaves. A second patron from a rival faction is
  possible, and then a vanilla quest may force a choice.
- **Fun:** political choice with consequences; players already have faction opinions.
- **Fit:** replaces the single Alice loan with a rotating cast; ties company to the vanilla main-quest map.
- **Cost:** M-L (one strings table each; start with 3 factions). **Risk:** conflicts with faction-quest scripts and
  reputation; I must not change vanilla reputation values, only read them.

### C5. The board meeting (King of Dragon Pass)
- **Plays:** Every game week (5.6 real hours), a meeting: your four managers each want something. The route manager
  wants a longer road, the bookkeeper wants dividends held back, the fixer wants a favour done. You get two big decisions.
  Each manager has a loyalty bar; ignore one three weeks running and they leave or sabotage. The text is a short
  argument, not a menu of effects, so you read and choose.
- **Fun:** managers as characters, feeling heard or overruled.
- **Fit:** two decisions per cycle matches the proposed 1-3 memos; terminal notes carry the text.
- **Cost:** M (writing is the work, about 40 meeting cards for variety). **Risk:** repetition; gate cards on past
  choices so the table remembers.

### C6. Named crews, a roll call and caravan songs
- **Plays:** Each caravan is a crew with a name, two or three named people, a history line ("Lucky Pete's
  brahmin run, 14 deliveries, one ambush survived"). Deaths go on a wall in your HQ (an in-world list). Famous crews are
  sung about: after a feat a town's bar gains a line, which gives a small trust bonus there. Alice poaching the best crew is
  a headline.
- **Fun:** attachment, grief, pride, "my" people; the strongest way to make a spreadsheet matter.
- **Fit:** names and histories are data; only crews near the player are real NPCs.
- **Cost:** M. **Risk:** low; needs a name and history generator that does not repeat.

### C7. The courier line: sealed dispatches (Pony Express, and the player is a Mojave Express courier)
- **Plays:** A new high-margin job class: "dispatches", sealed letters or parcels carried in person by the player from HQ to
  a named recipient before a deadline (for example Goodsprings to Mojave Outpost in 12 game hours). Pay is high, no
  ledger math: the player rides. Later you can hire relay riders at stations (swing stations at Primm, Outpost) and the
  line runs itself at a slower rate. Pony Express numbers [D] show relays beat a single rider on speed (about 10
  days over 1,900 miles); our version: each station you own cuts delivery time by a fixed amount.
- **Fun:** a pure active-play bridge; the player is still the courier from the opening.
- **Fit:** uses existing travel; no AI cost; an obvious nod to vanilla.
- **Cost:** M. **Risk:** can turn into a chore if forced; keep it optional with strong payout so it feels like a quest,
  not a pickup trip.

### C8. Letters that arrive while you quest (asynchronous decisions)
- **Plays:** The company writes to you. A courier NPC finds you in the wild ("a letter from Goodsprings") or a Pip-Boy
  note appears. The letter holds one decision with a deadline in game days ("Sloan wants a 200-stone order, yes or
  no by Friday"). You answer at the next terminal, or the default fires (your manager decides, with a cut). Away from
  terminals the default is a sensible policy you set before leaving ("standing orders": a short set of menu toggles).
- **Fun:** the world calls you back; doing quests with the company breathing down your neck; and a policy that works when you
  do not.
- **Fit:** solves "business must not need babysitting but needs decisions".
- **Cost:** S-M. **Risk:** nag fatigue; cap at one letter per game day.

### C9. Laws and lobbying (Frostpunk-style charters)
- **Plays:** The NCR council in Mojave sets rules: a tariff on powder imports, a licence cap on caravan count, a
  curfew for unlit roads. Once a season you may spend "favour" (earned by NCR contracts and escort deeds) to push one
  law: "Powder tariff +20%" helps you if you make powder locally, hurts Alice's imports. Laws stay until repealed; your
  rival lobbies too.
- **Fun:** shaping the rules of the game you play, a late-game power feeling.
- **Fit:** laws are just modifiers in the ledger. A small set (8 to 10) is enough.
- **Cost:** M. **Risk:** balance; each law must be readable in one sentence.

### C10. The Mojave calendar (seasons without seasons)
- **Plays:** FNV has no seasons, so the mod defines a 4-week "company year" with scheduled shocks the player can plan
  for: NCR payday (ammo and drink demand up), the Strip's fight night (Freeside food up), a rad storm week (roads shut),
  harvest at Goodsprings. They are shown on a rolling calendar page.
- **Fun:** anticipation, a rhythm; players plan stock for the storm.
- **Fit:** pure data, uses game weather as flavour.
- **Cost:** S. **Risk:** low.

### C11. The mark: branding as a choice
- **Plays:** At tier 2 you pick a reputation line: Honest Measure (lower margin, trust grows 2x), Cheap and Quick
  (volume, trust decays), or Hard Bargain (higher margin, towns grumble). The sign on your wagons and warehouse changes.
  Alice's mark is fixed; you can copy hers and anger her. Choice is changeable once, at a cost.
- **Fun:** identity; roleplay.
- **Fit:** two numbers and a texture swap.
- **Cost:** S. **Risk:** low; make sure each mark has a real upside.

### C12. Franchising independents (affiliates)
- **Plays:** Vanilla small traders in towns (a vendor with a stall) can be offered your banner: they pay you a fee and
  stock your goods, and you guarantee supply and protection. If your supply fails, they walk away and tell the town.
- **Fun:** growing without hiring; sense of an expanding network.
- **Fit:** vanilla named NPCs are untouchable per decision 7, so only mod-placed traders can be affiliates; this
  shrinks the idea.
- **Cost:** M. **Risk:** high given the rule about vanilla NPCs; park it unless town residents are traders.

### C13. Hostile takeover of the Crimson Caravan (endgame as a proxy fight)
- **Plays:** At tier 5 you can buy shares in Alice's company, one block per route you out-trade her on. Her
  board has named members (a Strip investor, an NCR officer, the family of Cass). You woo them with contracts and
  favours, vote at a shareholder meeting. Win and Alice becomes your employee or exits; lose and you have made an enemy
  who now targets your debt.
- **Fun:** payoff for hours of rivalry; a boss fight made of ledgers.
- **Fit:** menu only, rewards the market-share number already proposed.
- **Cost:** L. **Risk:** must not break "Heartache by the Number"; make it after that quest, or only touch vanilla
  state through flags the quest does not use.

### C14. Legacy: the company outlives you
- **Plays:** If you lose, a successor company is founded by one of your former staff (the Sunless Skies model [D]:
  some belongings and story progress carry over). If you win or the main quest ends, the company goes on: a final
  page, "20 years on", is written from the ledger (towns you fed, crews lost). A "hardcore" setting makes loss permanent.
- **Fun:** failure that stays a story; a reason to try a second approach.
- **Fit:** the proposal "start over smaller" becomes a gameplay feature, not a reset.
- **Cost:** M. **Risk:** low.

### C15. The Ledger as narrator (NV's voice)
- **Plays:** Every weekly page ends with a few lines by an in-world bookkeeper (an old accountant who writes like a
  Mojave local): "Week 4. The brahmin ate better than the guards. Primm owes us 200 caps and a favour." The same voice
  writes the loss letter, the takeover note and the epilogue. Generated from event tags.
- **Fun:** personality; reading the report is not a chore.
- **Fit:** all text, terminal native.
- **Cost:** M (phrase library, about 150 lines). **Risk:** repetition; tag lines by event so 4 weeks do not repeat.

### C16. Customs table: the declaration game (Papers, Please [M])
- **Plays:** On the dodgy path, each run needs a declared manifest. You choose: declare honestly, mislabel "stimpaks" as
  "bandages" (cheaper tax, higher heat if audited), or split into small loads. The NCR checks 1 in 5 loads; a good fixer
  raises your odds. After an audit you see what the sergeant found.
- **Fun:** a small bluff, risk judged on your own numbers.
- **Fit:** menus only; reuses the heat ladder already proposed.
- **Cost:** S-M. **Risk:** low.

### C17. Rival diplomacy and collusion (EVE-like cartels [M])
- **Plays:** Alice writes to you. Offers: fix prices at Primm for 3 weeks (both earn more, towns pay more and trust you
  both less, NCR antitrust may notice), split the map, or sell her a route. Refusing has a cost, accepting has a leash.
- **Fun:** personality duels; "I could cheat the villain".
- **Fit:** letters again; ties to Alice as a character.
- **Cost:** S-M. **Risk:** must not fight with Alice's vanilla dialogue and quest lines.

## 3. Ranking (top 5) and how they combine

1. **C8 Letters + standing orders** (answers the biggest problem: a company that runs while you quest).
2. **C6 Named crews, roll call and songs** (what makes growth personal).
3. **C2 Forward contracts** (a clear, original decision with a deadline).
4. **C4 Patrons with strings** (replaces a lone loan with politics; fits FNV's factions better than any other game's).
5. **C14 + C15 Legacy and the narrating ledger** (makes failure and endgame memorable; counts as one unit).

Close runners-up: C1 rumours, C13 takeover, C7 courier line.

### The combined hook

**"A company with a memory, run by post."** You never open a spreadsheet; you read your company's mail. Letters arrive
while you adventure, each carrying one bet: a forward contract to fill by Friday, a patron's demand, a rumour to act on,
a rival's offer. You answer at the terminal or set standing orders. The crews that carry your goods are named people
who earn songs or end up on the wall of the dead. An old bookkeeper writes every week's page in the Mojave's own voice.
If the company falls, it is not a game over but a chapter: a successor starts from your ashes, and Alice's sign hangs on your
old door. This is not a tycoon with a prettier skin: the loop is letters, bets, patrons and people, and the numbers are
only the way it keeps score. No tycoon game I know of ties fixed-deadline bets, named crews and an inheritable
company to the main quest map and an RPG courier player.

**Build order for the hook:** (1) letters and standing orders with 4 letter types, (2) crews with names and a roll
call, (3) forward contracts, (4) one patron (NCR) then others, (5) narrator and legacy. Each step ships alone.

## 4. Pitfalls and flaws I see (including in the current proposals)

- **Too many decisions per day.** The board shows 1-3 memos; with C1, C2, C3, C5, C8, C17 added it would be 8. Cap at one
  letter per game day and let every one default sensibly.
- **Standing orders must be real.** If away-time defaults are bad, players punish themselves for quest time. Test with
  an away week and require a floor (no worse than 0 profit, loan on schedule).
- **Alice is a vanilla NPC.** Letters in her voice, a takeover and a loan all touch her quest; the mod must only read
  vanilla flags and never write them.
- **Faction patrons collide with vanilla reputation.** Do not edit vanilla reputation; keep patron standing in the
  mod's own variable.
- **Writing is the hidden cost.** C5, C15, C6, C8 all need hundreds of lines. Budget it; generate from tags and
  templates, not hand-written one-offs, and keep tone consistent.
- **Terminal text space.** Body text on a terminal is short; letters must fit about 6-8 lines.
- **A forward contract with a hidden deadline is a trap.** Always show the day count on the front page.
- **Hostile takeover and loss ladder together can feel like a pile-on.** Keep takeover of Alice's firm optional and
  late; the loan ladder alone is the lose condition for the early game.
- **Pony Express lesson [D]:** a famous, heroic company can have a negative P&L. If "heroic" runs (dispatches) are the
  most fun, keep them marginally profitable, not a loss leader, or the best play will be to ignore the rest.

## 5. Rejected ideas

1. **Typed text for naming your company and crews.** FNV terminals only take menus. Instead offer 6 preset names and
   a generated crew name; a typed-name hack would break on load orders.
2. **A live commodities exchange you watch in real time (EVE/Offworld [M]).** The market numbers would update once a
   game day anyway (48 real minutes); a ticking price board needs live terminal text refresh, which is untested
   (`ComputersMenu::DisplayTerminal` hook), and it rewards sitting at a terminal, against the "no babysitting" rule.
3. **Combat card battler for road events (a Reigns/Inscryption-style deck [M]).** Fun in isolation, but it
   duplicates the real fights the player already has and adds a big UI-less build with no terminal fit. Resolve
   road events by guards versus danger on paper, as already proposed.

## 6. Questions only the user can answer

1. Letters: a Pip-Boy note (simple) or an in-world courier NPC delivering paper (nicer, costs more)?
2. Is "named crews who can die" welcome, given it makes losses emotional? The alternative is anonymous crews.
3. Is a one-time permanent patron (NCR, House, Kings, Omertas, Brotherhood) acceptable even if it excludes the others
   for a while?
4. Should a failing company ever be allowed to end with a permanent "you lose" (hardcore) or only a chapter?
5. Is it OK for the mod to write a bookkeeper's voice with some dark humour, or must it stay neutral?
