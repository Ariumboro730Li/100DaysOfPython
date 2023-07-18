import random  # Importing the 'random' module
from functions import get_english_words, getLetterPositionOfWord, wordToUnderscore, getSingleLetterInput  # Importing functions from the 'functions' module
from arts import stages, logo
from words import word_list
from clear_terminal import clear_terminal

def theGame():
    clear_terminal()
    print(logo)
    """
    The main game function.
    """
    # english_words = get_english_words()  # Get a list of English words
    chosen_word = random.choice(word_list)  # Choose a random word from the list

    # print(f"\nthe solution is {chosen_word}\n")  # Print the chosen word
    underscore = wordToUnderscore(chosen_word, 3)  # Convert the chosen word to underscore format
    print(underscore)  # Print the underscore representation of the chosen word

    attempts = 6  # Set the number of attempts
    while attempts > 0:  # Loop until there are no attempts left        
        user_choice = getSingleLetterInput("Enter a letter: ").lower()  # Get user input for a single letter
        clear_terminal()
        print(logo)
        positions = getLetterPositionOfWord(user_choice, chosen_word)  # Get the positions of the chosen letter in the word

        if positions:  # If the letter is found in the word
            underscore_list = list(underscore)  # Convert the underscore string to a list

            for i in positions:  # Iterate over the positions of the letter in the word
                underscore_list[i] = chosen_word[i]  # Replace the underscore with the letter at the corresponding position

            underscore = ''.join(underscore_list)  # Convert the list back to a string

            if underscore == chosen_word:  # If the underscore becomes the same as the chosen word
                attempts = 0  # Set attempts to 0 to exit the loop
        else:  # If the letter is not found in the word
            attempts -= 1  # Decrease the number of attempts by 1
            print(f"\nUpps\n")  # Print the number of remaining attempts
            print(stages[attempts])
        
        print(f"\n{underscore}")  # Print the updated underscore

    if underscore == chosen_word:  # If the underscore becomes the same as the chosen word
        print(f"\n\n#### yes the word is '{chosen_word}', You are GREAT ###")  # Print a success message
    else:
        print(f"\n\nOuch, one should die. the word is '{chosen_word}'")  # Print a failure message

restart_game = "y"  # Set the initial value for restart_game to "y"

while restart_game == "y":  # Loop until restart_game is not equal to "y"
    theGame()  # Call theGame() function to start the game
    restart_game = input("Do you want to restart the game? y/n ").lower()  # Ask the user if they want to restart the game
    print("\n")  # Print a newline for separation
