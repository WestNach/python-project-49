import random
RULE_GAME = 'What number is missing in the progression?'


def generate_data():
    start = random.randint(0, 10)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)
    miss_index = random.randint(0, length - 1)
    return start, diff, length, miss_index

def make_quest(start,diff,length,miss_index):
    Quest = []
    ind = 0
    for ind in range(length):
        if ind == miss_index:
            true_answ = start + ind * diff
            Quest.append("..")
        else:
            Quest.append(start + ind * diff)
        return Quest, true_answ


def variables(Quest, true_answ):
    Quest = " ".join(map(str, Quest))
    return Quest, str(true_answ)
