#!/usr/bin/env python3
from random import randint
import prompt 


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    answ = None
    true_answ = None
    num = None
    num2 = None
    while i != 3:
        num = randint(0, 100) # Генерация чисел
        num2 = randint(0, 100)
        true_answ = str(num + num2)
        print(f"Question: {num} + {num2}")  # Вопрос
        answ = input("You answer: ")  # Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" is wrong answer ;(. Correct answer was "{true_answ}"')
            print(f"Let's try again,{name}!")  # Проверка ответа
    print(f"Congratulations,{name}!")  # Завершение цикла


def main():
    brain_calc()
if __name__ == '__main__':
    main()
