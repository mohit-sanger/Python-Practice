from random import randint
number_of_trial = 0

def check_answer(Guess_number,answer,number_of_trial):
    if Guess_number > answer:
        print('The Guess number is grater')
        return number_of_trial-1
    elif Guess_number < answer:
        print('The guess number is smaller')
        return number_of_trial-1
    elif Guess_number == answer:
        print('Hurray you guess the correct number')
        return number_of_trial == 0
    else:
        print('Please provide correct input')

def set_difficulty():
    level = input('Choose a difficulty Type "easy" or "hard":  ')

    if level == 'easy':
        number_of_trial == 10
    elif level == 'hard':
        number_of_trial == 5



print('Welcome to number guessing game')
set_difficulty()



while number_of_trial != 0:
    print(f'You are left with {number_of_trial}  number of trials')
    print('Guess the number between 1 to 100')
    answer = randint(1,101)
    Guess_number = int(input())
    check_answer()

