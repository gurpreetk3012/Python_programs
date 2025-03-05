import random
import Hangman_words
import Hangman_art

words = Hangman_words.words
chosen_word = random.choice(words)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(Hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        print(f"{' '.join(display)}")
        print(Hangman_art.stages[lives])
        continue
    
    # Checking the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"{' '.join(display)}")
            
    # Checking if the user is wrong.
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lost a life.")
        lives -= 1
        print(Hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("Game over! You ran out of lives.")

print(f"{' '.join(display)}")
print(f"The correct word was: {chosen_word}")

if "_" not in display:
        end_of_game = True
        print("Congratulations! You've guessed the word correctly!")

print(Hangman_art.stages[lives])