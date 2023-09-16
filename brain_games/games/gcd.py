import random
import math
RULE_GAME = 'Find the greatest common divisor of given numbers.'


def variables():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    Quest = f'{num1},{num2}'
    true_answ = str(math.gcd(num1, num2))
    return Quest, true_answ
