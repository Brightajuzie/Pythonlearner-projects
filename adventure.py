#adventure game by Bright Chidozie Onyekachi
username = input("What is your name")

# Start of game
print("Welcome, " + username + " Start the venture!")
print("As you walk throught the caves of Umunze")
print("Be careful and take note of the sounds that you will hear ")
sound = input("What did you hear? a SHOUT or ROAR ")
if sound.lower() == ("roar"):
    print ("you heard a large "  + sound + "  sound, this is a lion!")
    # Stage one  of game
    decision = input("will you RUN or STAY?")
    if decision.lower() == ("run"):
        print("you are safe, to "+ decision + "is a wise decision" )
        print("Congrats,"+ username+ "you taking a decision to"+ decision + "is for good" )
        print ("YOU win")
    elif decision.lower() == ("stay"):
        print("You are dead")
        print("Too bad,"+username+ "you taking a decision to"+ decision + "isnt good" )
        print("GAME OVER")
        quit()
    else:
        print("you are wrong") 
        print("start all over")   
    quit()
elif sound.lower() == ("shout"):
    # Next part of game
    print ("you are in the land of the living dead, you are now interacting with the gods")
    print ("perform sacrifices to appease ezumezu the greatest oracle ")
    word = input ("SACRIFICE or DISOBEY?")
    if word.lower == ("sacrifice"):
        print("You are a true warrior")
        print("You shall return with the crown")
        print("YOU WIN")
    elif word.lower == ("disobey"):
       print("you are dead")
       print("GAME OVER")
       quit()
    
   #refreshes game if user input is wrong    
else:
    print("Start Afresh")   
    print("this time follow the rules and appease the gods")  
    quit() 
     