import prompt


game = None


def game_process(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    incorrect = 'is wrong answer ;(. Correct answer was'
    i = 0
    rounds = 3
    while i != rounds:
        quest, true_answ = game.question_answer()
        print(f"Question: {quest}")  # Вопрос
        answ = prompt.string("You answer: ")  # Ввод ответа
        if answ == true_answ:
            i += 1
            print("Correct")
        else:
            print(f'"{answ}" {incorrect} "{true_answ}"')
            print(f"Let's try again, {name}!")  # Проверка ответа
            break
    print(f"Congratulations, {name}!")  # Завершение цикла
