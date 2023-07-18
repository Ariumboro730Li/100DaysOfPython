import sys

print("Welcome to the RollerCoaster")
height = int(input("What is your height in CM ?"))

if height > 120:
    print("You can ride the RollerCoaster")
    age = int(input("What is your age ?"))
    if age >= 50:
        print("You are too OLD")
        sys.exit()
    elif age < 6:
        print("You are too young")
        sys.exit()
    elif  age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    wants_photo = input("do you want to take photo ? Y or N\nYour Answer :")
    if wants_photo.upper() == "Y":
        bill += 3
    elif wants_photo.upper() == "N":
        bill = bill
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        sys.exit()
    
    print(f"Please pay {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")