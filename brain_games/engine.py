import prompt


game = None


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    rule = game.variables()
    print(rule)
    incorrect = 'is wrong answer ;(. Correct answer was'
    i = 0
    while i != 3:
        Quest, true_answ = game.variables()
        print(f"Question: {Quest}")  # Вопрос
        answ = prompt.string("You answer: ")  # Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" {incorrect} "{true_answ}"')
            print(f"Let's try again, {name}!")  # Проверка ответа
            break
    print(f"Congratulations, {name}!")  # Завершение цикла
