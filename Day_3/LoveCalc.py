# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_combinations = name1.lower() + name2.lower()

t = name_combinations.count("t")
r = name_combinations.count("r")
u = name_combinations.count("u")
e = name_combinations.count("e")
l = name_combinations.count("l")
o = name_combinations.count("o")
v = name_combinations.count("v")
e = name_combinations.count("e")

total = int(str(t + r + u + e) + str(l + o + v + e))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")