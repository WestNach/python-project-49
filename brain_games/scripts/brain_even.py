#!/usr/bin/env python3
from random import randint
import prompt



def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even. otherwise answer "no"')
    Attempts = 3 
    i = 0
    answ = None
    true_answ = None
    num = None
    while i != 3:
        num = randint(0, 100)  # Генерация числа
        if num % 2 == 0:
            true_answ = "yes"
        else:
            true_answ = "no"  # Проверка на четность
        print(f"Question: {num}")  # Вопрос
        answ = input("You answer: ")  # Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" is wrong answer ;(. Correct answer was "{true_answ}"')
            print(f"Let's try again,{name}!")  # Проверка ответа
    print(f"Congratulations,{name}!")  # Завершение цикла


def main():
    brain_even()
if __name__ == '__main__':
    main()
