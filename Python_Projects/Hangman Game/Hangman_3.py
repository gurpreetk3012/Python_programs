import random

words = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Testing the code
print(f"The chosen word is: {chosen_word}")

# Creating blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter").lower()

    # Checking the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Won!")