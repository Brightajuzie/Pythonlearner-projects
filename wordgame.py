
#Wordle  game by Bright Chidozie Onyekachi
username = input("What is your name")

# Start of game
print("Welcome, " + username + " Start the Guessing Game")
def game_instruction():
    print(  username + """This is a word guessing game
A player has to guess a eight letter words
You may attempt 7 times   """)


game_instruction()

def check_word():
  words = "chibiara"
  
  attempt = 7
  while attempt > 0:
    hint = ("HINT....my daughter's second name,")  
    guess = str(input( hint + "   Guess the word: "))
    
    if guess.lower() == words:
      print("You are Correct..WINNER ")
      print(f"you made {attempt} attempt(s),,\n")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for letter in words:
            if letter.lower() == guess:
                print( guess, "_",end ="")

            elif guess in words:
                print("_ ",end ="")
            else:
                print(guess,"_",end ="")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
