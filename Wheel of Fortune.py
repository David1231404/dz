import random

def Game():
    World_For_Game = {
        'Moscow',
        'Picle',
        'Tea',
        'Cat',
        'Apple',
        'House',
        'Bed',
        'Washington'
    }

    word = random.choice(list(World_For_Game))
    the_hidden_word = '_' * len(word)
    guessed_letters = set()


    print("Добро пожаловать в игру 'Колесо фортуны'!")
    print("Отгадайте слово, угадывая по одной букве.")
    print("Загаданное слово:", the_hidden_word) 

    while '_' in the_hidden_word:
        guess = input("Введите букву: ").capitalize()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите только одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву, попробуйте другую!")
            continue

        guessed_letters.add(guess)

        new_hidden_word = ''
        for i in range(len(word)):
            if word[i].capitalize() == guess:
                new_hidden_word += word[i]
            else:
                new_hidden_word += the_hidden_word[i]
        
        the_hidden_word = new_hidden_word
        print("Загаданное слово:", the_hidden_word)

    print("Поздравляем! Вы угадали слово: ", word)

Game()