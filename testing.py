import random

# Define a list of words
word = "hello"

# Choose a random word from the list
#word = words

# Initialize the game state
guesses = 0
correct_letters = word
incorrect_letters = []

# Start the game loop
while guesses < 6:
    # Prompt the player to enter a guess
    guess = input("Guess a 5-letter word: ")

    # Check if the guess is correct
    if guess == word:
        print("Correct! You guessed the word in {} guesses.".format(guesses + 1))
        break

    # Otherwise, update the game state
    for i in range(5):
        if guess[i] in word:
            if guess[i] in correct_letters:
                continue
            else:
                correct_letters.append(guess[i])
        elif guess[i] not in word:
            if guess[i] in incorrect_letters:
                continue
            else:
                incorrect_letters.append(guess[i])
                

    # Provide feedback to the player
    feedback = ""
    for letter in correct_letters:
        feedback += letter
    for letter in incorrect_letters:
        feedback = guess + " _"
    print(feedback)
    guesses += 1

# If the player runs out of guesses, tell them that they lost
if guesses == 6:
    print("You lost! The word was {}.".format(word))