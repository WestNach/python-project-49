import random


def cut_even(quest):
    bull = None
    if quest % 2 == 0:
        bull = True
    else:
        bull = False
    return bull


def rule():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rule


def question_answer():
    quest = random.randint(0, 100)
    bull = cut_even(quest)
    if bull is True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return quest, str(true_answ)
