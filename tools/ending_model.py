"""M4 model: the "20 years on" pages (docs/plans/2026-11-28-m4-ending.md, "The ending").

pages(c) reads the ledger of a closed (or retiring) company and returns three pages, each a title and a
list of short lines. Every line comes from a tag: the tag picks one of its 2 to 4 variants by the seeded
roll (key 40 + the tag's number), so two runs with different seeds read differently, and the same run
always reads the same. A variant has at most one blank, filled with a town's or a person's name or a
number, so the game can build it with one sv_Construct.

  page 1  The company      how it ended, the towns, the roads
  page 2  The people       the crew, Alice Mclafferty and the Crimson Caravan
  page 3  The ledger       the NCR, the patron, the loans, the laws, the side taken at the Dam
"""

ROLL_END = 40

# tag -> its variants; the tag's number is its index in TAGS (the roll key is ROLL_END + that number)
TAGS = (
    # 0-4: how it ended
    ('end_retired', (
        'Twenty years on, the Mojave Caravan Company still runs. You handed it on and never looked back.',
        'Twenty years on, the wagons still carry your mark. You retired to a porch in Goodsprings.',
        'Twenty years on, the company outlived its founder\'s working days. You sold your desk, not the name.')),
    ('end_receivership', (
        'Twenty years on, the old office is a Crimson Caravan branch. Few remember it was ever yours.',
        'Twenty years on, the ledger that sank you sits in a Crimson Caravan archive.')),
    ('end_takeover', (
        'Twenty years on, Alice Mclafferty still tells the story of the company she took for its debts.',
        'Twenty years on, your wagons wear red. Alice took the office, and kept the drivers.')),
    ('end_walked', (
        'Twenty years on, people ask why you closed the doors. You never gave the same answer twice.',
        'Twenty years on, the office is a general store. You wound the company up yourself.')),
    ('end_revoked', (
        'Twenty years on, the NCR still cites your company in its licensing lectures.',
        'Twenty years on, the revoked licence hangs framed in a Mojave Outpost office.')),
    # 5-8: the towns
    ('towns_many', (
        'In %s towns the name still opens doors.',
        'Folk in %s towns still say a Company wagon never came late.')),
    ('towns_few', (
        'Only %s town remembered you kindly.',
        'Trust came slowly: %s town ever took you to heart.')),
    ('towns_none', (
        'No town ever quite trusted you.',
        'The towns took your goods and kept their distance.')),
    ('town_best', (
        '%s was always home.',
        'In %s they named a street for the depot.',
        '%s still keeps a Company bell at the crossroads.')),
    # 9-10: the roads
    ('roads_three', (
        'At its height, %s roads ran on your schedule.',
        'Your wagons kept %s roads open through the worst years.')),
    ('roads_one', (
        'It never grew past the one road.',
        'One road and one wagon: it was enough for a while.')),
    # 11-13: the people
    ('crew_big', (
        'At the last count %s people drew Company wages.',
        '%s drivers, guards and clerks called the company theirs.')),
    ('crew_small', (
        'The crew was never more than %s strong.',
        'You ran it with %s people and a lot of nerve.')),
    ('crew_poached', (
        'Some of your best people left for red wagons. %s never came back.',
        '%s went to the Crimson Caravan, and you never forgave it.')),
    # 14-17: Alice
    ('alice_out', (
        'Her board voted Alice out. You bought the shares that did it.',
        'Alice Mclafferty lost the Crimson Caravan to her own board, and to your three share blocks.',
        'The Crimson Caravan still trades, but no longer against you.')),
    ('alice_angry', (
        'Alice never stopped fighting you. The price wars are still talked about.',
        'The Crimson Caravan and the Company stayed at war to the end.')),
    ('alice_calm', (
        'Alice came to treat you as a fellow trader, if never a friend.',
        'The Crimson Caravan and the Company learned to share the roads.')),
    ('alice_lender', (
        'You lent to small outfits as Alice once lent to you.',
        'Like Alice before you, you became the one the small outfits came to.')),
    # 18-21: the NCR
    ('ncr_good', (
        'The NCR called you its most reliable carrier.',
        'NCR quartermasters still ask for Company wagons by name.')),
    ('ncr_outlaw', (
        'To the NCR you were outlaws. Rangers still keep your file.',
        'The NCR never forgot the raid.')),
    ('ncr_plain', (
        'The NCR taxed you and left you alone.',
        'To the NCR you were one licence among many.')),
    ('ncr_laws', (
        'You had %s of the three laws passed in New Vegas.',
        'Your favour in the capital bought %s of the three laws.')),
    # 22-24: the patron
    ('patron_kept', (
        'The quartermaster\'s deal held to the end.',
        'Preferred carrier status: the NCR\'s patronage kept the company fed.')),
    ('patron_broken', (
        'The quartermaster\'s deal broke, and with it the NCR\'s trust.',
        'You broke the quartermaster\'s strings, and paid for every one.')),
    ('loans_bad', (
        '%s outfits failed on your loans.',
        'You took the wagons of %s outfits that could not pay.')),
    # 25-28: the side taken at the Dam
    ('side_ncr', (
        'When the NCR held the Dam, the Company carried its supplies.',
        'The Republic won the Dam, and its contracts came to you.')),
    ('side_house', (
        'Under Mr. House the Strip prospered, and so did its carriers.',
        'Mr. House kept his city, and your wagons kept it stocked.')),
    ('side_legion', (
        'The Legion took the Dam. The Company paid its tribute and survived.',
        'Under the Legion the roads were safe, and the price was steep.')),
    ('side_independent', (
        'With no one ruling the Mojave, the Company was as close to a government as some towns had.',
        'An independent Vegas needed carriers more than masters.')),
    # 29-30: the closing line
    ('close_good', (
        'It was a good company.',
        'The roads were kinder for it.')),
    ('close_bad', (
        'It was a hard lesson, and the Mojave learned it with you.',
        'Some debts outlive the debtor.')),
)
TAG_INDEX = {t: i for i, (t, _) in enumerate(TAGS)}
SIDES = {'NCR': 'side_ncr', 'House': 'side_house', 'Legion': 'side_legion', 'Independent': 'side_independent'}


def _cm():
    import company_model
    return company_model


def line(c, tag, fill=None):
    """The variant of `tag` the seed picks, with its blank filled."""
    i = TAG_INDEX[tag]
    variants = TAGS[i][1]
    text = variants[_cm().roll(c.seed, c.day, ROLL_END + i) % len(variants)]
    return text % fill if fill is not None else text


def tags(c):
    """The three pages' tags, each (tag, fill) in page order."""
    cm = _cm()
    reason = c.end_reason or 'retired'
    p1 = [('end_' + reason, None)]
    trusted = [t for t in cm.TOWNS if c.trust[t] >= 50]
    if len(trusted) >= 2:
        p1.append(('towns_many', len(trusted)))
    elif trusted:
        p1.append(('towns_few', 1))
    else:
        p1.append(('towns_none', None))
    best = max(cm.TOWNS, key=lambda t: (c.trust[t], -cm.TOWNS.index(t)))
    if c.trust[best] > 0:
        p1.append(('town_best', cm.TOWN_NAME[best]))
    roads = len(c.running_roads())
    p1.append(('roads_three', roads) if roads >= 2 else ('roads_one', None))

    p2 = [('crew_big', len(c.staff)) if len(c.staff) >= 6 else ('crew_small', max(1, len(c.staff)))]
    if getattr(c, 'poached_name', ''):
        p2.append(('crew_poached', c.poached_name))
    if c.rival_out:
        p2.append(('alice_out', None))
    elif c.aggr >= 40:
        p2.append(('alice_angry', None))
    else:
        p2.append(('alice_calm', None))
    if c.lent_ever:
        p2.append(('alice_lender', None))

    p3 = []
    if c.outlaw:
        p3.append(('ncr_outlaw', None))
    elif c.ncr_standing >= 60:
        p3.append(('ncr_good', None))
    else:
        p3.append(('ncr_plain', None))
    if c.laws:
        p3.append(('ncr_laws', len(c.laws)))
    if c.qm:
        p3.append(('patron_kept', None))
    elif c.qm_offered and c.qm_since:
        p3.append(('patron_broken', None))
    if c.seized_n:
        p3.append(('loans_bad', c.seized_n))
    if c.side in SIDES:
        p3.append((SIDES[c.side], None))
    p3.append(('close_good', None) if reason == 'retired' else ('close_bad', None))
    return p1, p2, p3


TITLES = ('20 YEARS ON: THE COMPANY', '20 YEARS ON: THE PEOPLE', '20 YEARS ON: THE LEDGER')


MAX_PAGE = 200                           # a page is one Post letter: at most 200 characters


def fit(lines):
    """The lines that fit a page, in order: a line that would take the page past MAX_PAGE is left out."""
    kept = []
    for ln in lines:
        if len(' '.join(kept + [ln])) <= MAX_PAGE:
            kept.append(ln)
    return kept


def pages(c):
    """Three (title, [lines]) pages for the company's end."""
    return [(TITLES[i], fit([line(c, t, f) for t, f in page])) for i, page in enumerate(tags(c))]


def line_count():
    return sum(len(v) for _, v in TAGS)
