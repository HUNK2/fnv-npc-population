"""Post texts (M1 plan task 1.6; M2 names the road, town and good): the morning report's two pages, memo texts and letter texts.

The game (CCCore) writes the same strings with sv_Construct at the tick, so tools/ingame_post.py can
read them back and compare. Every text is at most 200 characters (M0 0.8: JohnnyGuitar copies terminal
text into a 260-byte buffer). Numbers are whole caps with no thousands separator.
"""
import company_model as cm

MAX_TEXT = 200
ROAD_NAME = {1: 'Primm road', 2: 'Sloan road', 3: 'Outpost road'}
GOOD_NAME = {'water': 'water', 'powder': 'healing powder', 'ammo': 'ammo', 'dirty': 'dirty water',
             'herbs': 'herbs', 'materials': 'building materials', 'meat': 'smoked meat'}


def poss(name):
    return name + ("'" if name.endswith('s') else "'s")


def con_words(con):
    """('PR', 'water') -> ('Primm', 'water')."""
    return cm.TOWN_NAME[con[0]], GOOD_NAME[con[1]]


EVENT_TEXT = {
    'bandits_driven_off': ' Bandits tried the %s and our guard drove them off.',
    'bandits_took_cargo': ' Bandits robbed the wagon on the way back: %d caps lost.',
    'bandits_wreck': ' Bandits took the whole strongbox on the way back: %d caps lost.',
    'bandits_empty': ' Bandits stopped the wagon on the way back and found nothing to take.',
}
FORECAST_TEXT = {
    'bandits': 'bandit sign on the %s, about %d strong, our cover %d.',      # road, danger, cover
    'quiet': 'the road looks quiet.',
    'no_wagon': 'no wagon on the road.',
}
BUTTONS = {'road': 'Keep it home|Send as planned|Hire a gun (25)|Later', 'away': 'Ok', 'loss': 'Ok',
           'forecast': 'Ok', 'closed': 'Ok'}
NOTICE_TEXT = {
    'grace': 'Boss, we missed bill day. %d is owed to the lender. Pay it within %d days or a final notice '
             'follows. Strike %d of 3 this season.',
    'final': 'Final notice: %d is owed. Pay %d of it within %d days or the lender takes the wagon and '
             'brahmin. Strike %d of 3 this season.',
    'seized': "The lender's men took the wagon and brahmin. %d is still owed. Pay it within %d days or the "
              'office becomes a Crimson Caravan branch.',
    'takeover': 'Third strike this season: a takeover notice. Pay %d from company cash within %d days or the '
                'lender takes the office. Your own caps will not do.',
    'probation': 'We missed bill day, but it is paid now. The lender still marks a strike, %d of 3 this '
                 'season. Probation for %d days.',
}
CLOSED_TEXT = {
    'receivership': "It is over, boss. The lender's men changed the locks: the office is a Crimson Caravan "
                    'branch now. The company is closed.',
    'takeover': 'The lender used the takeover clause and took the office. The company is closed.',
    'walked': 'You wound the company up. The lender took what was left, and the books are closed.',
}


def days_to_bills(c):
    return 7 - c.day % 7


def bill_estimate(c):
    """The next weekly bill if the rest of the week goes like a quiet day (design: the front page)."""
    due = c.day + days_to_bills(c)
    est = (7 * c.daily_wages() + 7 * cm.FEED + cm.RENT_WEEK + cm.half_up(cm.INTEREST * c.loan)
           + min(cm.MIN_PRINCIPAL, c.loan) + cm.duty(c.week_sales))
    return est + (cm.LICENCE if due % 28 == 0 else 0)


CONTRACT_TEXT = {'delivered': ' %s got its %s.', 'missed': ' We missed the %s %s delivery.',
                 'delivered completed': ' %s got its %s: the contract is done.',
                 'missed completed': ' We missed the last %s delivery: the contract is done.',
                 'walked': ' %s walked away from our counter.'}


def forecast_line(c):
    f = c.forecast()
    if f != 'bandits':
        return FORECAST_TEXT[f]
    road = c.event_road(c.day + 1)
    return FORECAST_TEXT[f] % (ROAD_NAME[road], cm.ROAD_DANGER[road], c.cover())


def contract_line(r):
    town, good = con_words(r.con)
    if r.contract == 'walked' or r.contract == 'missed completed':
        return CONTRACT_TEXT[r.contract] % town
    return CONTRACT_TEXT[r.contract] % (town, good)


def report_pages(c):
    """The morning report after the last tick: page 1 the bookkeeper's letter, page 2 the numbers."""
    if not c.history:
        return None
    r = c.history[-1]
    out, back = r.out, r.back
    dest = {1: 'Primm', 2: 'Sloan', 3: 'the Outpost'}[r.ran]
    if not r.wagon:
        p1 = "Boss. The wagon is in the lender's yard, so nothing moved."
    elif not r.crew:
        p1 = 'Boss. We have no driver on the books, so the wagon stayed in the yard.'
    elif r.road_mode == cm.HOLD and r.runs == 0:
        p1 = 'Boss. The wagon stayed home today, as the memo said: bandit sign on the %s.' % ROAD_NAME[r.ev_road]
    elif r.runs > 1 or r.road_mode == cm.HOLD:
        p1 = 'Boss. %d wagon%s ran: %d crates out, %d back.' % (r.runs, '' if r.runs == 1 else 's', out, back)
        if r.road_mode == cm.HOLD:
            p1 += ' The %s wagon stayed home, as the memo said.' % ROAD_NAME[r.ev_road].split()[0]
    elif out + back == 0:
        p1 = 'Boss. The wagon went to %s and back with no cargo: nothing paid the trip.' % dest
    else:
        p1 = 'Boss. The wagon took %d crates to %s and brought %d back.' % (out, dest, back)
    if r.road_mode == cm.GUN:
        p1 += ' We hired a gun for the road.'
    if r.event == 'bandits_driven_off':
        p1 += EVENT_TEXT[r.event] % ROAD_NAME[r.ev_road]
    elif r.event:
        p1 += EVENT_TEXT[r.event] % r.event_loss if '%' in EVENT_TEXT[r.event] else EVENT_TEXT[r.event]
    if r.bills is not None:
        if r.bills_paid:
            p1 += " The week's bills, %d, are paid." % sum(r.bills.values())
        else:
            p1 += ' We could not pay all the bills: %d is owed.' % c.arrears
    if r.prepaid:
        p1 += ' We paid %d off the loan.' % r.prepaid
    if r.signed:
        p1 += ' We signed the %s %s contract at %d.' % (con_words(r.con) + (r.signed,))
    if r.contract:
        p1 += contract_line(r)
    p2 = ('Day %d: sales %d, costs %d, net %d. Cash %d, runway %dd. Bills in %dd, about %d. Tomorrow: %s'
          % (r.day, r.sales, r.costs, r.margin, c.cash, c.runway(), days_to_bills(c), bill_estimate(c),
             forecast_line(c)))
    return p1, p2


def memo_title(c, m):
    due = m.due - c.day
    if m.kind == 'road':
        return 'BANDIT SIGN, %s  due %dd' % (ROAD_NAME[m.road].upper(), due)
    if m.kind == 'contract':
        return '%s WANTS %s  due %dd' % (cm.TOWN_NAME[m.town].upper(), GOOD_NAME[m.good].upper(), due)
    if m.kind == 'raise':
        return 'A RAISE FOR %s  due %dd' % (m.who.upper(), due)
    return 'PAY DOWN THE LOAN?  due %dd' % due


def memo_text(c, m):
    if m.kind == 'road':
        cover, dg = c.cover(), cm.ROAD_DANGER[m.road]
        due = next((x for x in c.contracts if x.next_due == m.due), None)
        what = ("Primm's water" if due and (due.town, due.good) == ('PR', 'water') else 'a delivery')
        tail = ('Unanswered, it goes: %s is due.' % what if c.memo_default(m) == cm.SEND and due
                else 'Unanswered, it stays home.')
        return ('Bandit sign on the %s tomorrow: about %d strong, our cover %d: %d in 100 to get '
                'through clean, %d with a gun (%d). Send, hire a gun, or keep it home? %s'
                % (ROAD_NAME[m.road], dg, cover, c.clean_chance(cover, dg), c.clean_chance(cover + cm.GUN_COVER, dg),
                   cm.GUN_COST, tail))
    if m.kind == 'contract':
        return ('%s store wants %d crates of %s every %d days for %d days, at %d a crate. Accept, '
                'or counter at %d (they may walk)? If you say nothing, we decline.'
                % (poss(cm.TOWN_NAME[m.town]), cm.CONTRACT_CRATES, GOOD_NAME[m.good], cm.CONTRACT_EVERY,
                   cm.CONTRACT_DAYS, m.price, cm.half_up(m.price * (1 + cm.COUNTER_PREMIUM))))
    if m.kind == 'raise':
        p = next((x for x in c.staff if x.name == m.who), None)
        loyal, wage = (p.loyalty, p.wage) if p else (0, 0)
        return ('%s asks for a raise: loyalty %d, wage %d a day. Give a quarter more (%d a day), or refuse? If you say '
                'nothing, we refuse.' % (m.who, loyal, wage, cm.half_up(wage * cm.RAISE)))
    return ('The bills are paid and we hold %d caps. Pay %d off the loan now and save %d a week in '
            'interest? If you say nothing, we keep the cash.'
            % (c.cash, cm.PREPAY, cm.half_up(cm.INTEREST * cm.PREPAY)))


def answer_label(m, i, c=None):
    mark = '[x]' if m.pick == i else '[ ]'
    default = ' (default)' if (c.memo_default(m) if c else cm.MEMO_DEFAULT[m.kind]) == i else ''
    return '  %s %s%s' % (mark, m.answers[i], default)


def notice_text(values):
    stage, owed, need, days, strikes = values
    if stage == 'grace':
        return NOTICE_TEXT[stage] % (owed, days, strikes)
    if stage == 'final':
        return NOTICE_TEXT[stage] % (owed, need, days, strikes)
    if stage in ('seized', 'takeover'):
        return NOTICE_TEXT[stage] % (owed, days)
    return NOTICE_TEXT['probation'] % (strikes, days)


def forecast_text(short, days):
    return ('Boss, cash is thin: at this rate we are short by about %d caps on bill day, in %d days, '
            'unless sales pick up.' % (short, days))


def notice_buttons(c, acts):
    """A notice letter's buttons for the actions Company.letter_buttons gave."""
    words = {'later': 'Later', 'rescue': 'Pay %d from my pocket' % c.rescue_amount(),
             'sell': 'Sell the wagon for %d' % c.sell_value()}
    return '|'.join(words[a] for a in acts)


TIER_TEXT = ('Boss, we are an Outfit now. Our office next to the Prospector Saloon is open and Primm gave us '
             'a stall. The Build screen is open at the terminal: purifier, apothecary, well rig, forager hut.')
TIER3_TEXT = ('Boss, we are a caravan company now. Sloan and the Outpost gave us branches, the route manager '
              'can be hired, and the smokehouse and stone yard are on the Build screen.')


def letter_title(letter):
    if letter.kind == 'notice':
        word = {'grace': 'notice served', 'final': 'final notice', 'seized': 'wagon seized',
                'takeover': 'takeover notice', 'probation': 'strike'}[letter.values[0]]
    else:
        word = {'away': 'while you were away', 'road': 'bandit sign', 'loss': 'robbed',
                'forecast': 'short on bill day', 'closed': 'company closed',
                'tier': 'an Outfit now' if letter.values[:1] != (3,) else 'a caravan company'}[letter.kind]
    return 'LETTER day %d  %s' % (letter.day, word)


def letter_text(letter):
    v = letter.values
    if letter.kind == 'away':
        return ('Boss, you have been away %d days. Since day %d: sales %d, costs %d. Cash %d, runway %dd. '
                'Memos waiting at the office: %d.' % v)
    if letter.kind == 'notice':
        return notice_text(v)
    if letter.kind == 'forecast':
        return forecast_text(*v)
    if letter.kind == 'closed':
        return CLOSED_TEXT[v[0]]
    if letter.kind == 'tier':
        return TIER3_TEXT if v[:1] == (3,) else TIER_TEXT
    if letter.kind == 'road':
        danger, cover, chance, due = v[:4]
        road = v[4] if len(v) > 4 else 1
        con = v[5] if len(v) > 5 and v[5] else ('PR', 'water')
        return ('Bandit sign on the %s tomorrow: about %d strong, our cover %d: %d in 100 to get '
                'through clean. Keep the wagon home tomorrow?%s'
                % (ROAD_NAME[road], danger, cover, chance,
                   ' %s %s is due tomorrow.' % (poss(cm.TOWN_NAME[con[0]]), GOOD_NAME[con[1]]) if due else ''))
    event, loss = v[:2]
    road = ROAD_NAME[v[2] if len(v) > 2 else 1]
    if event == 'bandits_wreck':
        return 'Bandits took the whole strongbox on the %s: %d caps lost. The crew is unhurt.' % (road, loss)
    return 'Bandits robbed the wagon on the %s: %d caps lost. The crew is unhurt.' % (road, loss)
