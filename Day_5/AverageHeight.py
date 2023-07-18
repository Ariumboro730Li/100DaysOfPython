# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum_list = sum(student_heights)
len_list = len(student_heights)
print(round(sum_list / len_list))
#Write your code below this row 👇




