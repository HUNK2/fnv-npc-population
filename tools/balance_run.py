"""Balance run (M1 plan task 1.10, M2 task 2.2): 100 model days for three kinds of player, against the design's
balance targets (docs/design.md, Balance targets). Prints one table; no game needed.

  passive   the bookkeeper's plan every day, nothing else (Ghost Town Gunfight done)
  careful   + accepts Primm's contract, hires a gun on bandit sign, pays 300 off the loan when the
            prepay memo comes and 28 days of runway stay, builds the well rig and purifier at tier 2
            when 14 days of runway stay after paying
  good      + pays 300 off the loan whenever the prepay memo comes, builds all four at tier 2
            M2: has Primm's sheriff (the deputy quest done); at tier 2 hires the bookkeeper (Normal),
            buys the Sloan wagon and hires its driver and clerk; at tier 3 buys the Outpost wagon,
            hires the route manager (Balanced) and builds the tier 3 buildings it can
  careful   M2: buys the Sloan wagon at tier 2 (driver and clerk), no managers, no sheriff

A week's net is the change in cash and owner money, not counting loan repaid or buildings bought:
the trade margin after the weekly bills. 'worth 28' is earned worth on day 28 (tier 3 asks 8,000 by
about week 4 in the design; it comes in M2).

    python tools/balance_run.py [days] [seed]
"""
import sys

import company_model as cm

PLAYERS = ('passive', 'careful', 'good')


def play(kind, days=100, seed=1234):
    c = cm.Company(seed)
    c.found()
    c.auto = True
    c.ghost_town_done = True
    c.sheriff = kind == 'good'
    out = {'tier3': None, 'kind': kind, 'day1': None, 'tier2': None, 'loan_paid': None, 'ended': None,
           'worst_event_runway': 0.0, 'weeks': [], 'contract_income': 0, 'income': 0, 'worth28': None}
    # a week's net: the change in cash and owner money, not counting loan repaid or buildings bought:
    # trade margin after the weekly bills (wages, feed, rent, interest, duty, licence)
    week_start = c.cash + c.owner_funds - c.loan + c.buildings
    for d in range(1, days + 1):
        burn = max(1, c.daily_burn())
        r = c.tick()
        if d == 1:
            out['day1'] = r.margin
        out['income'] += r.sales
        if r.contract.startswith('delivered') and c.history:
            out['contract_income'] += cm.CONTRACT_CRATES * (c.contract.price if c.contract else 0)
        if r.event_loss:
            out['worst_event_runway'] = max(out['worst_event_runway'], r.event_loss / burn)
        if d % 7 == 0:
            now = c.cash + c.owner_funds - c.loan + c.buildings
            out['weeks'].append(now - week_start)
            week_start = now
        if d == 28:
            out['worth28'] = c.earned_worth()
        if c.tier >= 2 and out['tier2'] is None:
            out['tier2'] = d
        if c.tier >= 3 and out['tier3'] is None:
            out['tier3'] = d
        if c.loan == 0 and out['loan_paid'] is None:
            out['loan_paid'] = d
        if c.ended:
            out['ended'] = (d, c.end_reason)
            break
        if kind == 'passive':
            continue
        for m in list(c.memos):
            if m.kind == 'contract':
                c.answer(m, 0)
            elif m.kind == 'road':
                c.answer(m, cm.GUN)
            elif m.kind == 'prepay' and (kind == 'good' or c.cash - cm.PREPAY >= 28 * c.daily_burn()):
                c.answer(m, 0)
        if c.tier >= 2:
            wanted = cm.BUILD_ORDER if kind == 'good' else ('well', 'purifier')
            if kind == 'good' and c.tier >= 3:
                wanted = wanted + ('corral', 'smokehouse', 'sandpit', 'scrapyard')
            for b in wanted:
                if c.can_build(b) and c.cash + c.owner_funds - c.build_cost(b) >= 14 * c.daily_burn():
                    c.build(b)
            m2(c, kind)
    out['cash'], out['loan'], out['tier'], out['worth'] = c.cash, c.loan, c.tier, c.earned_worth()
    out['built'] = c.workshops + c.sites
    return out


def m2(c, kind):
    """The M2 moves: wagons, their drivers and clerks, managers."""
    if kind == 'good' and c.can_hire_manager('bookkeeper'):
        c.hire_manager('bookkeeper', 'Normal')
    if kind == 'good' and c.can_hire_manager('route'):
        c.hire_manager('route', 'Balanced')
    for road in (2, 3) if kind == 'good' else (2,):
        if c.can_buy_road(road) and c.cash + c.owner_funds - cm.WAGON - cm.BRAHMIN_PAIR >= 14 * c.daily_burn():
            c.buy_road(road)
    drivers = sum(1 for p in c.staff if p.role == 'driver')
    clerks = sum(1 for p in c.staff if p.role == 'clerk')
    for role, have in (('driver', drivers - 1), ('clerk', clerks)):
        if have < len(c.wagons):
            i = next((i for i, p in enumerate(c.candidates) if p.role == role and c.can_hire(i)), None)
            if i is not None:
                c.hire(i)


def main(argv):
    days = int(argv[1]) if len(argv) > 1 else 100
    seed = int(argv[2]) if len(argv) > 2 else 1234
    print('%d days, seed %d' % (days, seed))
    print('%-8s %6s %6s %6s %9s %9s %8s %6s %6s %7s %6s %s' % ('player', 'day 1', 'tier2', 'tier3', 'loan paid', 'worst ev',
                                                         'worth 28', 'cash', 'loan', 'worth', 'ended', 'weeks (net)'))
    for kind in PLAYERS:
        o = play(kind, days, seed)
        print('%-8s %6d %6s %6s %9s %8.1fd %8s %6d %6d %7d %6s %s' % (
            kind, o['day1'], o['tier2'], o['tier3'], o['loan_paid'] and 'wk %d' % ((o['loan_paid'] + 6) // 7),
            o['worst_event_runway'], o['worth28'], o['cash'], o['loan'], o['worth'], o['ended'] and o['ended'][0],
            ' '.join('%d' % w for w in o['weeks'])))
        print('%-8s built %s, contract share of sales %.0f%%' % ('', o['built'] or '-',
                                                               100.0 * o['contract_income'] / max(1, o['income'])))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
