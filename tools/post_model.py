"""M1 post texts (plan task 1.6): the morning report's two pages, memo texts and letter texts.

The game (CCCore) writes the same strings with sv_Construct at the tick, so tools/ingame_post.py can
read them back and compare. Every text is at most 200 characters (M0 0.8: JohnnyGuitar copies terminal
text into a 260-byte buffer). Numbers are whole caps with no thousands separator.
"""
import company_model as cm

MAX_TEXT = 200
EVENT_TEXT = {
    'bandits_driven_off': ' Bandits tried the Primm road and our guard drove them off.',
    'bandits_took_cargo': ' Bandits robbed the wagon on the way back: %d caps lost.',
    'bandits_wreck': ' Bandits took the whole strongbox on the way back: %d caps lost.',
    'bandits_empty': ' Bandits stopped the wagon on the way back and found nothing to take.',
}
FORECAST_TEXT = {
    'bandits': 'bandit sign on the Primm road, about %d strong, our cover %d.' % (cm.DANGER, cm.COVER),
    'quiet': 'the road looks quiet.',
    'no_wagon': 'no wagon on the road.',
}
BUTTONS = {'road': 'Keep it home|Send as planned|Hire a gun (25)|Later', 'away': 'Ok', 'loss': 'Ok'}


def days_to_bills(c):
    return 7 - c.day % 7


def bill_estimate(c):
    """The next weekly bill if the rest of the week goes like a quiet day (design: the front page)."""
    due = c.day + days_to_bills(c)
    est = (7 * c.daily_wages() + 7 * cm.FEED + cm.RENT_WEEK + cm.half_up(cm.INTEREST * c.loan)
           + min(cm.MIN_PRINCIPAL, c.loan) + cm.duty(c.week_sales))
    return est + (cm.LICENCE if due % 28 == 0 else 0)


def report_pages(c):
    """The morning report after the last tick: page 1 the bookkeeper's letter, page 2 the numbers."""
    if not c.history:
        return None
    r = c.history[-1]
    out = sum(n for (o, _), n in r.loads.items() if o == 'GS')
    back = sum(n for (o, _), n in r.loads.items() if o == 'PR')
    if not r.wagon:
        p1 = "Boss. The wagon is in the lender's yard, so nothing moved."
    elif r.road_mode == cm.HOLD:
        p1 = 'Boss. The wagon stayed home today, as the memo said: bandit sign on the Primm road.'
    elif out + back == 0:
        p1 = 'Boss. The wagon went to Primm and back with no cargo: nothing paid the trip.'
    else:
        p1 = 'Boss. The wagon took %d crates to Primm and brought %d back.' % (out, back)
    if r.road_mode == cm.GUN:
        p1 += ' We hired a gun for the road.'
    if r.event:
        p1 += EVENT_TEXT[r.event] % r.event_loss if '%' in EVENT_TEXT[r.event] else EVENT_TEXT[r.event]
    if r.bills is not None:
        if r.bills_paid:
            p1 += " The week's bills, %d, are paid." % sum(r.bills.values())
        else:
            p1 += ' We could not pay all the bills: %d is owed.' % c.arrears
    if r.prepaid:
        p1 += ' We paid %d off the loan.' % r.prepaid
    p2 = ('Day %d: sales %d, costs %d, net %d. Cash %d, runway %dd. Bills in %dd, about %d. Tomorrow: %s'
          % (r.day, r.sales, r.costs, r.margin, c.cash, c.runway(), days_to_bills(c), bill_estimate(c),
             FORECAST_TEXT[c.forecast()]))
    return p1, p2


def memo_title(c, m):
    due = m.due - c.day
    if m.kind == 'road':
        return 'BANDIT SIGN, PRIMM ROAD  due %dd' % due
    return 'PAY DOWN THE LOAN?  due %dd' % due


def memo_text(c, m):
    if m.kind == 'road':
        return ('Bandit sign on the Primm road tomorrow: about %d strong, our cover is %d. Send the wagon, '
                'hire a gun for %d, or keep it home? If you say nothing, it stays home.'
                % (cm.DANGER, cm.COVER, cm.GUN_COST))
    return ('The bills are paid and we hold %d caps. Pay %d off the loan now and save %d a week in '
            'interest? If you say nothing, we keep the cash.'
            % (c.cash, cm.PREPAY, cm.half_up(cm.INTEREST * cm.PREPAY)))


def answer_label(m, i):
    mark = '[x]' if m.pick == i else '[ ]'
    default = ' (default)' if cm.MEMO_DEFAULT[m.kind] == i else ''
    return '  %s %s%s' % (mark, m.answers[i], default)


def letter_title(letter):
    word = {'away': 'while you were away', 'road': 'bandit sign', 'loss': 'robbed'}[letter.kind]
    return 'LETTER day %d  %s' % (letter.day, word)


def letter_text(letter):
    v = letter.values
    if letter.kind == 'away':
        return ('Boss, you have been away %d days. Since day %d: sales %d, costs %d. Cash %d, runway %dd. '
                'Memos waiting at the office: %d.' % v)
    if letter.kind == 'road':
        return ('Bandit sign on the Primm road tomorrow: about %d strong, our cover is %d. '
                'Keep the wagon home tomorrow?' % v)
    event, loss = v
    if event == 'bandits_wreck':
        return 'Bandits took the whole strongbox on the Primm road: %d caps lost. The crew is unhurt.' % loss
    return 'Bandits robbed the wagon on the Primm road: %d caps lost. The crew is unhurt.' % loss
