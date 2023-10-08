import random
import math
RULE = 'Find the greatest common divisor of given numbers.'


def question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    quest = f'{num1} {num2}'
    true_answ = str(math.gcd(num1, num2))
    return quest, true_answ
