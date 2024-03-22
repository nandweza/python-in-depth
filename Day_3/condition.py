print("Welcome to rollercoaster!")

height = int(input("Enter your height in centimeters: "))

if height >= 120:
    print("You can ride a rollercoaster")

    age = int(input("What is your age: "))

    if age < 12:
        print("Pay $5")
    elif age >= 12 and age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("You cannot ride a rollercoaster!!!")
