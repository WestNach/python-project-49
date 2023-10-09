import random
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 0
MAXIMUM_VALUE = 100


def cut_even(quest):
    bull = None
    if quest % 2 == 0:
        bull = True
    else:
        bull = False
    return bull


def question_answer():
    quest = random.randint(MIN_VALUE, MAXIMUM_VALUE)
    bull = cut_even(quest)
    if bull is True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return quest, str(true_answ)
