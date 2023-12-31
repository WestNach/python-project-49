import random
RULE = 'What is the result of the expression?'
MIN_VALUE = 0
MAXIMUM_VALUE = 100


def question_answer():  # Генерация нужных данных
    operators = ['+', '-', '*']
    num1 = random.randint(MIN_VALUE, MAXIMUM_VALUE)  # Генерация чисел
    num2 = random.randint(MIN_VALUE, MAXIMUM_VALUE)
    operator = random.choice(operators)
    quest = f'{num1} {operator} {num2}'
    true_answ = None
    match operator:
        case '+':
            true_answ = num1 + num2
        case '-':
            true_answ = num1 - num2
        case '*':
            true_answ = num1 * num2
    return quest, str(true_answ)
