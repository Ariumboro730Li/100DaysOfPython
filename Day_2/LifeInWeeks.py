# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
print("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")