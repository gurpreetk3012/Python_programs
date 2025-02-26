# This Python code is for solving a maze in 'Reeborg's World', an online maze game.
# You can test this code on the website using the following link:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Function to turn the robot right (since Reeborg only has a turn_left() function)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main loop to navigate through the maze until the goal is reached
while not at_goal():
    if right_is_clear():  # If there's an open path to the right, turn right and move forward
        turn_right()
        move()
    elif front_is_clear():  # If the front path is open, move forward
        move()
    else:  # If both front and right paths are blocked, turn left
        turn_left()