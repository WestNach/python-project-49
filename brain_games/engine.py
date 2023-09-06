import prompt
from brain_games import games


def start():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(games.RULE_GAME)
    if i != 3:
        Quest,true_answ = games.variables
        print(f"Question: {Quest}")  # Вопрос
        answ = input("You answer: ")  # Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" is wrong answer ;(. Correct answer was "{true_answ}"')
            print(f"Let's try again,{name}!")  # Проверка ответа
    print(f"Congratulations,{name}!")  # Завершение цикла
