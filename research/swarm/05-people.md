# 05 People: staff, managers and how they become characters

Angle: hiring, what staff do, why they matter, how they stay people and not rows. Research done 2026-11-26.
Source quality note: Fandom wikis, the CK3 wiki and the PC Gamer caravan page refused automated fetches (HTTP 402 or empty). What I opened is cited; the rest is marked as design reasoning, not source.

## 1. Key findings

### What other games do with staff
- **Mother Base (MGS Peace Walker)**: up to 350 soldiers; staff are assigned to combat, medical, intelligence and tech teams, the mess hall feeds troops and keeps morale, rebels go to the brig, the injured go to sickbay. Outer Ops sends combat units on missions with 8 slots per force; defeated soldiers die or go to sickbay depending on enemy firepower. [D] https://en.wikipedia.org/wiki/Metal_Gear_Solid:_Peace_Walker . Lesson: staff are a pool with places to be (working, hurt, jailed), and the base visibly needs them.
- **AC Brotherhood**: recruits are earned by a deed (destroy a tower, rescue citizens), sent on assignments, gain XP and skill/appearance choices, and can die and never return. [D] https://en.wikipedia.org/wiki/Assassin%27s_Creed:_Brotherhood . Lesson: the hire is a story beat; the assignment is one button plus a risk number.
- **Dragon Age Inquisition war table**: three advisers (Cullen military, Leliana spymaster, Josephine ambassador) run operations; time depends on which adviser you choose (minutes to hours), results vary by adviser, and you must collect the report for rewards to apply. [D] https://en.wikipedia.org/wiki/Dragon_Age:_Inquisition ; timing and report detail from a guide, search snippet only: https://www.gamepressure.com/dragonageiii/the-war-room/za6c89 . Lesson: one operation, several possible owners, different speed and result. That is the cleanest "choice that matters" for a menu-only terminal.
- **XCOM: Enemy Unknown**: four classes, rank-ups with a choice of one of two perks, customisable names, permadeath as a core pillar "to make consequences feel real". [D] https://en.wikipedia.org/wiki/XCOM:_Enemy_Unknown . The page does not discuss attachment itself; the link between naming, perk choice, risk and attachment is [O], widely repeated.
- **Darkest Dungeon**: stress from adventuring (no food or light, ally wounded or killed); high stress gives afflictions, sometimes virtues; the game tracks afflictions so patterns recur; dead heroes are lost for good; rest in town lowers stress. [D] https://en.wikipedia.org/wiki/Darkest_Dungeon . Lesson: a flaw that is also a story hook ("Calder will not travel at night") is worth more than a stat. (The article did not cover quirks; the quirk idea here is my design.)
- **RimWorld mood**: a 0-100% bar moving toward a sum of thoughts; falls up to 8 per hour, rises up to 12; break risk below 35% (minor), 20% (major), 5% (extreme); thoughts are named causes (hungry -6, pain, crowding). [D] https://rimworldwiki.com/wiki/Mood . Lesson: every mood has a readable list of reasons; the player fixes reasons, not a hidden number.
- **Two Point Hospital**: staff have personalities and specialisations, earn qualifications by training, are happier in higher-prestige rooms and quit if unhappy. [D] https://en.wikipedia.org/wiki/Two_Point_Hospital
- **Big Ambitions**: developer reply on Steam says happiness must stay above about 50%; new hires often start at low happiness; wages raise difficulty; players advise firing before people get too expensive; a player reports stylists quitting at about 70% average happiness. [O] search snippets from forums, some may be a different game, so treat as weak.
- **Bannerlord caravans**: need a companion with Trade, helped by Scouting (see threats early) and Tactics (win fights when the player is away); NPC-run caravans earn roughly 80-120 denars a day without skill; starting one needs a free companion and about 15,000 denars. [O] https://progameguides.com/mount-and-blade/best-companions-for-caravans-in-mount-and-blade-ii-bannerlord/ via search snippets; figures vary by version and one claimed wage figure could not be confirmed. Lesson: the leader's skill is the lever, the caravan is the vessel.
- **Football Manager, CK3 vassals, Kenshi, Game Dev Tycoon**: pages unreadable. From design knowledge only, not sourced: FM gives staff a handful of attributes, a contract and morale, and lets rivals approach them; CK3 gives every vassal an opinion number built from named modifiers. Both make poaching and disloyalty visible and answerable states.

### Cross-game patterns that matter to us
1. A person is a name, one or two numbers that change what they do, a readable flaw, and a history of things that happened to them. Not more.
2. The best automation is a role with a policy (Dragon Age advisers): you choose who, not how.
3. Mood works when it lists reasons (RimWorld). It fails when hidden (Big Ambitions complaint).
4. Death and loss must be foreshadowed and attributable ("you sent him with 2 guards through Powder Ganger land").
5. Theft by staff is fair when the player had a cheap way to see it coming (references, audits, a bookkeeper) and a cheap way to fix it.

## 2. What this means for our mod

### (a) The staff model

**Roles**
| Role | Does | Skill that matters |
|---|---|---|
| Trader | Rides with a caravan; sets margin on each stop | Barter, Speech |
| Caravan master | Leads one caravan; decides to run or fight | Survival, Guns (Speech to talk past bandits) |
| Guard | Raises the caravan's Defence | Guns |
| Brahmin handler | Cargo capacity, spoilage, keeps pack animals alive | Survival |
| Clerk | Runs the office; each clerk adds one route slot | Speech, Barter |
| Workshop hand | Production rate; recipe unlock needs skill (Science 70 for stimpaks, per brief) | Repair, Science, Medicine |
| Medic (optional) | Cuts injury and death rolls on the road | Medicine |

Manager types (one per area, tier gated, see (b)): route manager, purchasing manager, workshop foreman, bookkeeper, fixer.

**Attributes: 4 numbers (0-100) plus up to 2 traits**
- **Skill**: their role skill, one number, shown with the FNV skill name ("Barter 62").
- **Nerve**: how they handle danger; drives injury, panic and heroics.
- **Honesty**: skim or steal risk; shown to the player only as a band after a reference check or audit.
- **Loyalty**: chance to quit, be poached or strike; moves with named reasons.
- **Traits**, from a list of about 24: Cautious, Reckless, Charming, Haggler, Drinker, Family man, Ex-Legion, NCR veteran, Gambler, Soft-hearted, Grudge (against a faction), Ambitious. Each has one upside and one cost.

**Wages** (design numbers, tune against route income): weekly wage = 8 + Skill/4 caps for line staff (Skill 60 = 23 caps), x3 for managers. A tenure ladder Rookie, Hand, Veteran, Master at 4, 12 and 30 completed runs or workshop weeks; each step +25% wage and +10 on the Skill cap. A raise request appears as a memo when Loyalty is under 50 and a rung is due; refusing costs 10 Loyalty, granting costs the wage forever. Rough payroll: Outfit tier (8 staff) about 140 caps/week; Trading house (30 staff plus 4 managers) about 700 caps/week. Cap the Master rung so there is no endless spiral.

**Loyalty with reasons** (shown as a list on each staff terminal page, RimWorld-style):
- Plus: +10 paid on time, +10 shared a good week, +5 company bunk, +15 you saved them in person, +8 promoted.
- Minus: -10 wages late, -10 hurt with no sick pay, -15 colleague died on the same run, -8 dangerous route, -12 Crimson Caravan offered more.
- Loyalty under 35: asks for a raise or quits. Under 20: may sell route info to the Crimson Caravan. Honesty under 40 and Loyalty under 35: skims.
- New hires start at 55 plus or minus the wage offer, not at zero.

**Injury and death on the road** (paper-resolved when the player is away, so it must be explainable): each fight, every staff member on the caravan rolls Defence against Danger. Outcomes: unhurt, hurt (out 2-6 game days, a medic halves it), crippled (permanent -10 Skill; becomes a clerk or retires on a pension), dead. Death only occurs when the danger exceeded the Defence by a margin the player could see in the route page beforehand, and a medic or enough guards prevents it. The dead leave a ledger line, a name plate in the HQ terminal and a family member NPC whose Loyalty matters later.

### (b) Managers as automation (terminal menus only)
Rule: a manager automates exactly one chore, costs a wage plus a cut, has a visible policy preset, and has one realistic way to go wrong. The player never types numbers; every policy is a 3-5 item menu.

| Manager | Automates | Policy presets | Cost | What can go wrong |
|---|---|---|---|---|
| Route manager | Sends and re-routes caravans on a fixed list, resupplies from a depot | Safe (avoid red towns, slower) / Balanced / Fast / Opportunist (chases price spikes) | wage x3; 2% of route revenue | Opportunist chases a spike into Powder Ganger land; the report names the policy |
| Purchasing manager | Buys inputs for workshops and cargo | Stock up when cheap (under 85% of base) / Just in time / Never above base / Starve the Crimson Caravan of X | wage; capital tied up | Over-buys perishable cargo; can be bribed by a supplier (Honesty check) |
| Workshop foreman | Recipe order and bench staffing | Highest margin / Fill shortages first / Medicine first / Ammo first | wage | Chases margin, stops water, a town goes dry and trust drops |
| Bookkeeper | Weekly books, finds skimming, forecasts wages | Strict / Normal / Lenient | wage; strict audits cost morale | Lenient misses fraud; strict annoys a clerk into leaving |
| Fixer | Pays off NCR inspectors, hides smuggle cargo | Quiet / Standard / Loud | big wage plus a bribe fund | Each refused bribe adds heat; a badly fired fixer becomes a witness |

Each manager has an **Autonomy** setting: Ask me (a memo for each decision), Within budget (acts up to a cap limit), Full (acts, tells me afterwards). Higher autonomy grows faster and fails bigger. Full unlocks only at Trading house tier.

**Anti-micromanagement rules**
1. Anything a manager can do appears as a memo only if it crosses the player's budget threshold.
2. One daily report; at most 3 decisions, ranked by the cost of ignoring them. Everything else follows policy.
3. A manager's mistake always cites the policy that allowed it ("Dell took the fast route because Route policy is Fast"). Blame lands on the player's own choice.
4. No chores. Showing up (escorting, interviewing) is always a bonus, never a requirement.

### (c) Hiring flow in the terminal
1. HQ terminal > Staff > Hire. Each week 3-6 candidates are listed, drawn from the town's mod-tagged residents plus a drifter or two. A row shows name, role fit, asking wage and one rumour line ("lost a cousin to Powder Gangers").
2. Open a candidate: shows Skill, an Honesty band, one visible trait. Three optional actions, each costing caps or time:
   - **Check references** (5-20 caps, 1 game day): reveals Honesty as a band and one past event quoted from a named NPC (former employer, the bartender, a sergeant at Mojave Outpost).
   - **Test run** (1 trip at half wage): real Skill and Nerve appear in the report.
   - **Interview in person** (key hires only: managers and the fixer): a marker is placed ("meet at the Prospector Saloon"); a short conversation reveals the hidden trait and gives +10 Loyalty.
3. **Offer**: Low / Fair / Generous wage. Low gives -10 starting Loyalty, Generous +10. Answer arrives on the next report.
4. Hire appears as a placed NPC at their home and walks to work.

### (d) Staff stories (14 events; each is a memo with 2-3 menu choices)
1. **Promotion demand**: "Dell wants 34 caps a week or he looks at the Crimson Caravan." Grant / Counter at half / Refuse (-10 Loyalty, 40% chance he quits within a week).
2. **Poaching by the Crimson Caravan**: Alice's agent offers Rosa 30% more; memo comes a day early. Match / Offer a profit share / Let her go. If she goes she appears on a Crimson route and rival share rises in that town.
3. **Embezzlement caught**: a Strict bookkeeper finds 120 caps missing. Confront (money back, Loyalty -30, stays) / Fire quietly / Hand to the NCR (heat falls, a town story). With a Lenient bookkeeper the loss surfaces a month later.
4. **A guard's heroism**: on a paper ambush a guard with Nerve over 70 holds a pass; "Cruz held Goodsprings Road alone." Caravan saved, Cruz gains the trait Steady and the town mentions him.
5. **Family matter**: a clerk's mother is sick; wants 3 days off and a 60-cap advance. Grant (permanent Loyalty bump) / Deny / Send the medic.
6. **A manager's bad call**: Opportunist routing sends two wagons through Quarry Junction for a price spike. Report shows the loss and cites the policy; player changes policy or accepts.
7. **Drunk on the job**: a handler with the Drinker trait loses 50 caps of cargo. Warn / Dock pay / Pay a doctor.
8. **Ex-Legion hire**: cheap and fierce, but NCR towns lose 5 trust when he is seen with the company; a hook for the NCR versus dodgy path.
9. **Smuggler in the ranks**: a clerk moves Powder Ganger powder on the side. A fixer deals with it quietly; without one, heat +3 at the next inspection.
10. **Hurt but brave**: a wounded trader wants to go back out after a day; it saves a contract but doubles injury risk.
11. **Retirement with a recommendation**: a Master retires after 30 runs and sends a replacement with +10 Loyalty and a trait.
12. **Mutiny over a death**: two deaths on one route in 10 days and the guards refuse it until you add a medic or reroute.
13. **Alice invites your clerk to dinner**: an Ambitious clerk leaves unless you counter; shown as a memo before it happens.
14. **A debt to the dead**: the family of a dead guard asks for owed wages. Pay (+10 Loyalty across staff, word spreads) or ignore (-10 across staff).

### (e) Tie to the lived-in towns
- Every hire is a **mod-tagged resident** of a town, so they already have a home, a bed and a routine from the town part. The job adds one package: walk to the office or wagon yard in the morning, home at night. Only those near the player are simulated; the rest are ledger lines (about 20 complex actors near the player is the engine cap).
- **The town notices**: staff events show up as town bark text ("Cruz is the one who held the road"); a death shifts the town's trust by a few points, up if you pay the family, down if you do not.
- **Hiring drains the town**: hiring more than about 20% of a small town's residents reduces its guards and shop stock and lowers trust. That forces recruiting across towns.
- **Placed NPCs are real**: if a staff member dies in a fight the player is present for, their placed NPC dies, and the next visit has a visible gap and a funeral note.

### FNV grounding: who could be hired
Records checked read-only in FalloutNV.esm, no overrides: Trudy GSTrudy 00104C6C, Chomps Lewis QJChompsLewis 000E5958, Johnson Nash PrimmJohnsonNash 000DA729, Easy Pete GSEasyPete 00104C7F, Sunny Smiles GSSunnySmiles 00104E84, Deputy Beagle PrimmDeputy 000D7F57. I did not find Chet, Doc Mitchell, Jas Lewis or Mojave Outpost residents (not searched; verify).
- Trudy has class SettlerNV, a script (GSTrudyScript), a gunfight package and a bar package, and her DNAM skill bytes put Barter and Speech near 10 with Guns near 49 (my byte reading, not verified by the tool). Vanilla NPC skills come from class and are low in Barter and Speech, so the mod should **overlay its own role stats** and treat vanilla values only as a seed.
- Plausible fits by role: Trudy (fixer or bookkeeper, knows everyone), Chet (purchasing, Barter), Sunny Smiles (caravan master or guard captain; Survival, Guns), Easy Pete (explosives workshop hand; Reckless or Drinker), Doc Mitchell (medic, only after the player finishes his quest), Johnson Nash (Primm trader; partner more than employee), Deputy Beagle (guard, after Primm's sheriff story is settled), Chomps Lewis and Jas Lewis (Sloan; stone foreman after Quarry Junction is cleared), Mojave Outpost soldiers (ex-NCR guards).
- The brief says vanilla named NPCs are untouched and these have quest scripts. So: **vanilla named NPCs are references and partners, not employees.** They give the quote in a reference check, offer a "letter of introduction", or sign a supply deal; the actual staff are mod-tagged relatives, apprentices and neighbours placed by the mod. Their vanilla records and scripts are never edited.
- Mod-tagged residents (the lived-in towns part): roughly 15-20 per first-test town, each with a role tag (farmer, guard, merchant, drifter) and hidden Skill, Nerve and Honesty seeded from role. The hire list reads from that tag.

## 3. Bold ideas
1. **Apprentice line**: a Veteran can take an apprentice from the same town; when the master retires or dies the apprentice inherits one trait. Cheap (one record per NPC); gives long arcs.
2. **Gossip references**: the reference check is three quotes from townsfolk, one of them false. The player picks whom to believe (Speech lowers the chance of the false one). Terminal-only, cheap.
3. **Wage Book**: one terminal page, per person, "worth versus cost" in plain words ("Dell: carries his weight. Mara: underpaid, will leave"). Cheap.
4. **Take the lead**: when a walking caravan is near the player, the terminal can offer "take over as caravan master" for a real fight. Doing it gives that crew +15 Loyalty. Medium cost; falls back to the paper roll.
5. **Poached by reputation**: the more famous a staff member (heroism events), the more Alice wants them; a star is both an asset and a liability, and can be sold as a contract to Alice.
6. **Veteran hall**: retired and crippled staff become a clerk pool and a rumour source; better treatment gives better route tips. Cheap.

## 4. Pitfalls and design flaws
- **Too many numbers**: more than 4 attributes plus 2 traits makes terminal pages unreadable.
- **Hidden Loyalty**: Big Ambitions players complain that staff quit at seemingly fine happiness. Always list reasons.
- **Death without cause**: paper deaths must name the cause and the earlier warning, or players reload.
- **Embezzlement as a gotcha**: only when the player skipped a visible, affordable control. Never steal from a Strict-audited company.
- **Hiring vanilla NPCs directly**: conflicts with "vanilla named NPCs untouched" and may break quests. Use references and partnerships.
- **Wage spiral**: cap the Master rung and give it a benefit (can train others).
- **Full autonomy too early**: gate it to the Trading house tier.
- **Simulation limits**: do not promise individually walking staff everywhere; most are ledger rows.
- **Save size**: a fixed array with a cap (about 60 staff) and recycled slots, not a record per person.
- **Poaching without defence**: if Alice can take anyone with no warning, players quit hiring. Keep the one-day-early memo.

## 5. Questions only the user can answer
1. Should vanilla named NPCs (Trudy, Chet, Sunny, Easy Pete) ever be hireable, or only references and partners (my pick)?
2. Do you want optional real-time moments (interview in person, take over as caravan master), or everything in the terminal with just a marker to visit?
3. Death rules: permanent death of staff, or retirement with rare real death? (Brotherhood and XCOM show permanence is memorable; Sunless Sea's later move to Legacy shows it can feel unfair.)
4. Is a cap of about 60 staff acceptable for version 1?
