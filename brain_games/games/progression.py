import random
RULE = 'What number is missing in the progression?'
INDEX_CORRECT = 1
MIN_VALUE = 0
MIN_LENGTH = 5
MAXIMUM_VALUE = 10


def generate_data():
    initial_term = random.randint(MIN_VALUE, MAXIMUM_VALUE )
    common_difference = random.randint(MIN_VALUE + INDEX_CORRECT, MAXIMUM_VALUE )
    length = random.randint(MIN_LENGTH, MAXIMUM_VALUE )
    miss_index = random.randint(MIN_VALUE, length - INDEX_CORRECT)
    return initial_term, common_difference, length, miss_index


def create_progression(initial_term, common_difference, length):
    progression = []
    for i in range(length):
        progression.append(initial_term + i * common_difference)
    return progression


def question_answer():
    initial_term, common_difference, length, miss_index = generate_data()
    progression = create_progression(initial_term, common_difference, length)
    create_quest = list(progression)
    create_true_answ = progression[miss_index]
    create_quest[miss_index] = ".."
    quest = " ".join(map(str, create_quest))
    true_answ = str(create_true_answ)
    return quest, true_answ
