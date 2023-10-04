import random


def question_answer():
    initial_term, common_difference, length, miss_index = generate_data()
    quest, true_answ = replace_element_with_missing(initial_term, common_difference, length, miss_index)
    quest = " ".join(map(str, quest))
    true_answ = str(true_answ)
    return quest, true_answ


def rule():
    rule = 'What number is missing in the progression?'
    return rule


def generate_data():
    min_value = 0
    min_length = 5
    maximum_value = 10
    initial_term = random.randint(min_value, maximum_value)
    common_difference = random.randint(min_value + 1, maximum_value)
    length = random.randint(min_length, maximum_value)
    miss_index = random.randint(min_value, length - 1)
    return initial_term, common_difference, length, miss_index


def create_progression(initial_term, common_difference, length):
    progression = []
    for i in range(length):
        progression.append(initial_term + i * common_difference)
    return progression

def replace_element_with_missing(progression, miss_index):
    quest = list(progression)
    true_answ = progression[miss_index]
    quest[miss_index] = ".."
    return quest, true_answ
