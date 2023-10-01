import random


def variables():  # Генерация нужных данных
    operators = ['+', '-', '*']
    num1 = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
    operator = random.choice(operators)
    Quest = f'{num1} {operator} {num2}'
    true_answ = None
    match operator:
        case '+':
            true_answ = num1 + num2
        case '-':
            true_answ = num1 - num2
        case '*':
            true_answ = num1 * num2
    return Quest, str(true_answ)

def rule():
    rule = 'What is the result of the expression?'
    return rule