import random


def question_answer():  # Генерация нужных данных
    operators = ['+', '-', '*']
    num1 = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
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


def rule():
    rule = 'What is the result of the expression?'
    return rule
