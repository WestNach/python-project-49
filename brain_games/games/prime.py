import random
RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def cut_prime(Quest):
    bull = None
    if Quest < 2:
        bull = False
    elif Quest == 2:
        bull = True
    else:
        bull = True
        for i in range(2, int(Quest ** 0.5) + 1):
            if Quest % i == 0:
                bull = False
                break
    return bull


def variables():
    Quest = random.randint(1, 100)
    cut_prime(Quest)
    if cut_prime.bull == True:
        true_answ = 'yes'
    else:
        true_answ = 'no'
    return Quest, true_answ
