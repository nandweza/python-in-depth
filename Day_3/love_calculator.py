print("The Love calculator is calculating your score...")

name1 = input("What is your name: ")
name2 = input("What is their name: ")

name = name1 + name2

name_to_lower = name.lower()

t = name_to_lower.count("t")
r = name_to_lower.count("r")
u = name_to_lower.count("u")
e = name_to_lower.count("e")

result1 = t + r + u + e

l = name_to_lower.count("l")
o = name_to_lower.count("o")
v = name_to_lower.count("v")
e = name_to_lower.count("e")

result2 = l + o + v + e

result = str(result1) + str(result2)

if int(result) < 10 or int(result) > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif int(result) > 40 and int(result) < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
        
