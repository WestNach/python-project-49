import random


def cut_even(Quest):
    bull = None
    if Quest % 2 == 0:
        bull = True
    else:
        bull = False
    return bull

def rule():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rule

def variables():
    Quest = random.randint(0, 100)
    bull = cut_even(Quest)
    if bull is True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return Quest, str(true_answ)
