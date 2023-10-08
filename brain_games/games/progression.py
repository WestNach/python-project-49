import random
RULE = 'What number is missing in the progression?'


def question_answer(create_quest, create_true_answ):
    quest = " ".join(map(str, create_quest))
    true_answ = str(create_true_answ)
    return quest, true_answ


def generate_data():
    index_correction = 1
    min_value = 0
    min_length = 5
    maximum_value = 10
    initial_term = random.randint(min_value, maximum_value)
    common_difference = random.randint(min_value + index_correction, maximum_value)
    length = random.randint(min_length, maximum_value)
    miss_index = random.randint(min_value, length - index_correction)
    return initial_term, common_difference, length, miss_index


def create_progression(initial_term, common_difference, length):
    progression = []
    for i in range(length):
        progression.append(initial_term + i * common_difference)
    return progression


def replace_element_with_missing(progression, miss_index):
    create_quest = list(progression)
    create_true_answ = progression[miss_index]
    create_quest[miss_index] = ".."
    return create_quest, create_true_answ
