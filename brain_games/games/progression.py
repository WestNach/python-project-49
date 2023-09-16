import random
RULE_GAME = 'What number is missing in the progression?'


def variables():
    start = random.randint(0, 10)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)
    miss_index = random.randint(0, length - 1)
    Quest = []
    ind = 0
    for ind in range(length):
        if ind == miss_index:
            true_answ = start + ind * diff
            Quest.append("..")
        else:
            Quest.append(start + ind * diff)
    return Quest, str(true_answ)
