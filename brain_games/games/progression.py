import random
RULE_GAME = 'What number is missing in the progression?'

def variables():
    start, diff, length, miss_index = generate_data()
    Quest, true_answ = make_quest(start,diff,length,miss_index)
    Quest = " ".join(map(str, Quest))
    true_answ = str(true_answ)
    return Quest, true_answ


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
