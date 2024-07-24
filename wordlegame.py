
#Wordle  game by Bright Chidozie Onyekachi
username = input("What is your name")

# Start of game
print("Welcome, " + username + " Start the Guessing Game")
def game_instruction():
    print(  username + """This is a word guessing game mostly player by single player game 
A player has to guess a eight letter words
You have seven attempts 
Your Progress Guide "✔❌❌✔➕"  
"✔" Indicates that the letter at that position was guessed correctly 
"➕" indicates that the letter at that position is in the hidden word, but in a different position 
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)


game_instruction()

def check_word():
  words = "chibiara"
  attempt = 7
  while attempt > 0:
    hint = ("HINT....my daughter's second name,")  
    guess = str(input( hint + "   Guess the word: "))
    if guess.lower() == words:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(words, guess):
            if word in words and word in char:
                print(word + " ✔ ")

            elif word in words:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
