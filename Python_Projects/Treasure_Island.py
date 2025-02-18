print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island! 🌴\nYour mission is to find the legendary treasure hidden deep within the island.")
print("You stand at a crossroad. The path ahead splits into two. Do you go 'left' or 'right'?")
direction = str(input()).lower()

if direction == 'right':
    print("Oh no! The ground crumbles beneath you, and you fall into a deep, dark hole. Game over! 💀")
elif direction == 'left':
    swim_wait = str(input("You arrive at a raging river. Do you 'wait' for a boat or attempt to 'swim' across?\n")).lower()
    if swim_wait == 'swim':
        print("A crocodile emerges from the water and attacks! Game over! 🐊")
    elif swim_wait == 'wait':
        door = str(input("You find yourself in a mysterious room with three glowing doors: 'red', 'blue', and 'yellow'. Which door do you choose?\n")).lower()
        if door == 'red':
            print("As you open the red door, flames burst out and engulf you. Game over! 🔥")
        elif door == 'blue':
            print("The blue door leads to a den of hungry beasts. Game over! 🐾")
        elif door == 'yellow':
            print("You found the treasure! You won!")
        else:
            print("You hesitate too long, and the room collapses around you. Game over!")
    else:
        print("Invalid choice. You are lost forever. Game over!")
else:
    print("Invalid choice. You are lost forever. Game over!")