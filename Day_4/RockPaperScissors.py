import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("### Welcome ###")
while(True):
    lists_rps = [rock, paper, scissors]
    choice = int(input("What do you choose ? , 0 for rock, 1 for paper, 2 for scissor\nYour Choice : "))
    if choice <= 2:
        user = lists_rps[choice]
        computer_choice = random.randint(0, len(lists_rps) - 1)
        computer = lists_rps[computer_choice]
        print(user, computer)

        if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
            print("You Lose")
        elif (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1) or (choice == 0 and computer_choice == 2):
            print("You Won")
        elif choice == computer_choice:
            print("Draw")

        print("\n\n")
    else:
        print("YOU LOSEEEEEE")


