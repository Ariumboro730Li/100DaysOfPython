payment = input("What was the total bill ? Rp.")
members = input("How many people to split the bill ?")
tip = input("what percentage tip you want to share ?")

float_payment = float(payment)
int_members = int(members)
tip_percentage = 1 + int(tip) / 100

payment_per_person = (float_payment / int_members) * tip_percentage
final_amount = round(payment_per_person,2)
final_amount_formatted = "{:.2f}".format(final_amount)
print(f"Each person should pay: Rp.{final_amount}")
print(f"Each person should pay (Decimal 2): Rp.{final_amount_formatted}")