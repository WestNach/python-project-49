import random 
RULE_GAME = 'What is the result of the expression?'


def variables():  # Генерация нужных данных
    operators = ['+', '-', '*' ]
    num = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
    operator = random.choice(operators)
    Quest = f'{num} {operator} {num2}'
    true_answ = None
    match operator:
        case '+':
            true_answ = num + num2
        case '-':
            true_answ = num - num2
        case '*':
            true_answ = num * num2
    return Quest,str(true_answ)