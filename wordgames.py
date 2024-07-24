#Wordle  game by Bright Chidozie Onyekachi
username = input("What is your name")

# Start of game
print("Welcome " + username.upper() +"" ", Start the Guessing Game")

def game_instruction():
    print(  username.upper() + """ This is a word guessing game
A player has to guess  eight letter words
You may attempt 7 times  
Hint 1: The Secret word is the second name of someone's Daughter
Hint 2: The Secret Word is and Igbo name.""")


game_instruction()

# this is the secret word to guess
secreted = "chibiara"


# Starts the guess count
attempt = 0

# Looping: Stops when the guess is correct
while True:
    print ("HINT:_ _ _ _ _ _ _ _")
    # Prompt the user for a guess
    guess = input("What is your guess? ")
# Confirm if the user guessed the secret word correctly
    if guess == secreted:
        print("Congratulations!!, You are Correct ")
        break
    #  checks if the lenght of the guess confirms with the secret word
    elif len(guess) != len(secreted):
        print("Ensure that the inputed Guess is  eight letters")
        continue

    # Prompt for hint
    hints = [""]
    for i in range(len(secreted)):
        if guess[i] == secreted[i]:
            hints.append(guess[i].upper())
            
        elif guess[i] in secreted:
            hints.append(guess[i].lower())
        elif guess[i] != secreted:
            hints.append("_")   
        else:
            hints.append("")
            
    # Print the hint to the user
    print("Hint:", " ".join(hints))
    # adds the guess count
    attempt += 1
    # If the user attempts is above the maximum number of attempt, end the game
    if attempt > 7:
        print("Sorry, you have exceeded the maximum number of attempt.")
        print("GAME OVER")
        break

# Shows the total number of guesses / attempt
print("You guessed the secret word in {} attempt.✔".format(attempt))