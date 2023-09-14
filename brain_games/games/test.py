import random
RULE_GAME = 'What number is missing in the progression?'


def variables():
    start = random.randint(0,10)
    diff = random.randint(1,10)
    length = random.randint(5,10)
    miss_index = random.randint(0, length - 1)
    Quest = []
    true_answ = None
    for i in range(length):
        if i == miss_index:
            true_answ = start + i * diff
            Quest.append('..')
        else:
            Quest.append(start + i * diff)
    Quest = str(Quest)[1:-1]
    return Quest, str(true_answ)