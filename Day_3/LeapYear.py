# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# divisible_four = year / 4 
# divisible_hundred = year / 100 
# divisible_fourhundred = year / 400 

# is_divisible_four_leap = True if divisible_four.is_integer() else False
# is_divisible_hundred_leap = False if divisible_hundred.is_integer() else True
# is_divisible_fourhundred_leap = True if divisible_fourhundred.is_integer() else False

# if is_divisible_four_leap:
#     if is_divisible_hundred_leap == False:
#         if is_divisible_fourhundred_leap:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


## REFACTORED VERSION OF CHAT GPT ##

year = int(input("Which year do you want to check? "))

is_divisible_four = year % 4 == 0
is_divisible_hundred = year % 100 == 0
is_divisible_fourhundred = year % 400 == 0

if is_divisible_four and (not is_divisible_hundred or is_divisible_fourhundred):
    print("Leap year")
else:
    print("Not leap year")
