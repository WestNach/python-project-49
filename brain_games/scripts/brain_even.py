from random import randint
from ..cli import welcome_user
from ..brain_games.py import main


def brain_even():
    main()
    print('Answer "yes" if the number is even. otherwise answer "no"')
    i = 0
    answ = None
    true_answ = None
    num = None
    if i <= 3:
        num = randint(0, 100)  # Генерация числа
        if num % 2 == 0:
            true_answ = "yes"
        else:
            true_answ = "no"  # Проверка на четность
        print("Question: " + num)  # Вопрос
        answ = input("You answer: ")  # Ввод ответа
        if answ == true_answ:
            print("Correct")
            i += 1
        else:
            print("Let's try again, " + name + "!")  # Проверка ответа
    print("Congratulations, " + name + "!")  # Завершение цикла
