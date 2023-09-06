from random import randint
RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def variables():
    Quest = randint(0, 100)
    if Quest % 2 == 0:
        true_answ = "yes"
    else:
        true_answ = "no"
    return true_answ,Quest