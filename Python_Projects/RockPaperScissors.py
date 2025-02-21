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

user = int(input("Enter your choice: 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
user = game_images[user]
computer = game_images[random.randint(0, 2)]

print(f"Your choice:\n{user}")
print(f"Computer's choice:\n{computer}")
if user == paper and computer == rock:
    print("Congratulations! You win!")
elif user == rock and computer == scissors:
    print("Congratulations! You win!")
elif user == scissors and computer == paper:
    print("Congratulations! You win!")
elif user == computer:
    print("It's a draw!")
else:
    print("Oops! You lose. Better luck next time!")