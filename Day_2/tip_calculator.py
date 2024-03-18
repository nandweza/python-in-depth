print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip = bill * tip_as_percentage
total_bill = bill + total_tip

pay = total_bill / people
final_pay = round(pay, 2)

print("Each person should pay: $", final_pay)