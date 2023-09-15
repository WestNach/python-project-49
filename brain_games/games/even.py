import random
RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def variables():
    Quest = random.randint(0, 100)
    if Quest % 2 == 0:
        true_answ = "yes"
    else:
        true_answ = "no"
    return Quest,true_answ
