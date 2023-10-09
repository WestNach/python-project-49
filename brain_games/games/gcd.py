import random
import math
RULE = 'Find the greatest common divisor of given numbers.'
MIN_VALUE = 1
MAXIMUM_VALUE = 100


def question_answer():
    num1 = random.randint(MIN_VALUE, MAXIMUM_VALUE)
    num2 = random.randint(MIN_VALUE, MAXIMUM_VALUE)
    quest = f'{num1} {num2}'
    true_answ = str(math.gcd(num1, num2))
    return quest, true_answ
