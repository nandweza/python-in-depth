import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock, paper, scissors]

user_choice = int(input("What do you choose?, Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid input, You lose.")
else:
    print(game[user_choice])

    Computer_choice = random.randint(0, 2)
    print("Computer choose:")
    print(game[Computer_choice])

    if Computer_choice == user_choice:
        print("Its a draw!!!")
    else:
        if Computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif Computer_choice == 2 and user_choice == 1:
            print("You lose")
        elif Computer_choice == 1 and user_choice == 0:
            print("You lose")
        else:
            print("You win")
