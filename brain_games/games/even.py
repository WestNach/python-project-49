import random
RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def cut_even(Quest):
    bull = None
    if Quest % 2 == 0:
        bull = True
    else:
        bull = False
    return bull


def variables():
    Quest = random.randint(0, 100)
    cut_even(Quest)
    if cut_even.bull == True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return Quest, str(true_answ)

