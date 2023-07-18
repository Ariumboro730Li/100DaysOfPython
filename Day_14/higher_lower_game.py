import random
from art import logo, vs
from game_data import data
from clear_terminal import clear_terminal


def random_choice_data():
    return random.choice(data)


def format_data(data):
    name = data['name']
    follower_count = data['follower_count']
    description = data['description']
    country = data['country']

    return f"{name}, {follower_count}, {description}, {country}"


def check_answer(follower_a, follower_b):
    if follower_a > follower_b:
        return "a"
    else:
        return "b"


def fetch_data():
    account_a = random_choice_data()
    account_b = random_choice_data()
    while account_b == account_a:
        account_b = random_choice_data()

    return account_a, account_b


def game():
    score = 0
    game_playing = True

    account_a, account_b = fetch_data()

    while game_playing:
        compare_a = format_data(account_a)
        compare_b = format_data(account_b)

        print(f"Compare A : {compare_a}\n{vs}\nCompare B : {compare_b}\n")
        guess = input("Which one has more followers? A or B\n").lower()
        answer = check_answer(account_a["follower_count"], account_b["follower_count"])

        clear_terminal()

        if guess == answer:
            account_a = account_b
            account_b = random_choice_data()
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_playing = False
            print("i am handsome")
            print(f"Sorry, that's wrong. Your final score: {score}")

clear_terminal()
game()