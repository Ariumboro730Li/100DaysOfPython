# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

bmi = round(int(weight) / (float(height) ** 2))
#Write your code below this line 👇
info_bmi = f"Your BMI is {bmi}"
if bmi < 18.5:
    print(f"{info_bmi}, you are underweight")
elif bmi < 25:
    print(f"{info_bmi}, you have a normal weight")
elif bmi < 30:
    print(f"{info_bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"{info_bmi}, you are obese")
else:
    print(f"{info_bmi}, you are clinically obese")


