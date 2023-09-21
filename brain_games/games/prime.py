import random
RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def variables():
    Quest = random.randint(1, 100)
    if Quest < 2:
        true_answ = "no"
    elif Quest == 2:
        true_answ = "yes"
    else:
        true_answ = "yes"
        for i in range(2, int(Quest ** 0.5) + 1):
            if Quest % i == 0:
                true_answ = "no"
                break
    return Quest, true_answ
