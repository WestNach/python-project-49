import random
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def cut_prime(quest):
    bull = None
    if quest < 2:
        bull = False
    elif quest == 2:
        bull = True
    else:
        bull = True
        for i in range(2, int(quest ** 0.5) + 1):
            if quest % i == 0:
                bull = False
                break
    return bull


def question_answer():
    quest = random.randint(1, 100)
    bull = cut_prime(quest)
    if bull is True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return quest, true_answ
