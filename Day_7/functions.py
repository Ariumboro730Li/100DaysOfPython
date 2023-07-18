import random 

def get_english_words():
    english_words = []
    with open('/usr/share/dict/words', 'r') as file:
        for line in file:
            word = line.strip()
            # Exclude proper nouns and non-alphabetic words
            if word.islower() and word.isalpha():
                english_words.append(word)
    return english_words

def getLetterPositionOfWord(letter, word):
    positions = [i for i, char in enumerate(word) if char == letter]
    return positions

def wordToUnderscore(word, open_letter = 1):
    underscore = ""
    num_position = wordToNumPosition(word)
    random_word = []
    
    while open_letter > 0:
        random_word.append(random.choice(num_position))
        open_letter -= 1
    
    for i in range(len(word)):
        if str(i) in random_word:
            underscore += f"{word[i]}"
        else:
            underscore += f"_"
                        
    return underscore

def wordToNumPosition(word):
    num_position = ""
    for i in range(len(word)):
        num_position += str(i)
    return list(num_position)
    
def getSingleLetterInput(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Please enter a single letter.")