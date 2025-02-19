import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = game_images[user]
computer = game_images[random.randint(0, 2)]

print(f"You chose\n{user}")
print(f"Computer chose\n{computer}")
if user == paper and computer == rock:
    print("You Win!")
elif user == rock and computer == scissors:
    print("You Win!")
elif user == scissors and computer == paper:
    print("You Win!")
elif user == computer:
    print("Draw!")
else:
    print("You Lose!")