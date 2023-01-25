word_list = ['advark','baboon','camel']
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Randomly choose a word from the word_list
# Ask a user to guess a letter and assign them to a variable called guess
# check if letter guessed is one of the letter in the chosen word.

import random

lives = 1
chosen_word = random.choice(word_list)
print(chosen_word)
dash = '_'
blank = list(dash*len(chosen_word))
print(blank)
word_length = len(chosen_word)

end_of_game = False

while not end_of_game:
    guess = input('Choose a letter which contains in chosen word\n').lower()


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          blank[position] = letter

    if guess not in chosen_word:
        lives += 1

        if lives == 7:
            end_of_game = True
            print ('You Loose')
    print(blank)
    print(stages[-lives])

    if '_' not in blank:
        end_of_game = True
        print('You Win')

