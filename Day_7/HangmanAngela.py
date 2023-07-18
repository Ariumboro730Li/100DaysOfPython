#Step 2

import random
from functions import wordToUnderscore

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(len(stages))

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
underscore = wordToUnderscore(chosen_word)
underscore_list = list(underscore)
print(underscore_list)

while underscore_list != list(chosen_word):

    guess = input("Guess a letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            underscore_list[i] = letter

    print(underscore_list)
    
print("You Won")
