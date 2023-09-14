#!/usr/bin/env python3
import random
import prompt
import _game_test
RULE_GAME = 'What number is missing in the progression?'


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULE_GAME)
    i = 0
    while i != 3:
        Quest,true_answ = _game_test.test()
        print('Question:', Quest)  # Вопрос
        answ = prompt.string("Your answer: ")# Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" is wrong answer ;(. Correct answer was "{true_answ}"')
            print(f"Let's try again,{name}!")  # Проверка ответа
    print(f"Congratulations,{name}!")  # Завершение цикла