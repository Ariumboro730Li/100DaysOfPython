# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
formula_1 = int(weight) / (float(height) * float(height))
formula_2 = int(weight) / (float(height) ** 2)

print(int(formula_1))
print(int(formula_2))

