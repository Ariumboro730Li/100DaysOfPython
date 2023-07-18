import random

min = 0
max = 100
the_number = random.randint(0, 100)
print("Welcome to Guess the Number game")
print(f"i am thinking number from {min} to {max}")
level = input("Choose your level of game : easy | hard : ")
attempts = 10 if level == "easy" else 5
print(f"You have {attempts} attempts")
while attempts > 0 :
    attempts -= 1
    answer = int(input("Your guess : "))
    if answer > the_number:
        print("Too High")
    elif answer < the_number:
        print("Too Low")
    else: 
        attempts = 0
        print(f"you got it, the number is {the_number}")
        
    if attempts == 0 and answer != the_number:
        print("You have ran out of attempts, You Fail")
    else:
        print(f"You have reamining {attempts} attempts")
