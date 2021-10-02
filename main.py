# I am importing nltk a standard python library
import nltk

# downloding the pakage words
nltk.download('words')
# Using the corpus reader objects importing word module from package
from nltk.corpus import words
# creating a set(data structure) to store words in english dictionary
valid_word = set(words.words())

# importing os module
import os

play = "yes"

# A loop so the player can play again if he wants
while play == "yes":

    # Introducing the game
    print("\nWELCOM TO HANGMAN")
    print("\nLets Start playing\n\n")

    # The player choses the word to be gussed
    player_input = input(
        "Challenger enter the word you want player to guess here:-  \n")

    # lests the player quit
    if player_input == 'quit':
        break

    # The check if the chosen word is a valid word in the english dictionary
    while (player_input not in valid_word):
        print("That is not a word please enter a 'real word'")

        # if invalid inputs another word
        player_input = input("Challenger plese enter word here:-  \n")

    # telling the player what has chosen
    print("\nYou have suscesfuly Chosen your hangman Word as", player_input)

    # this when you switch to the player who is guessing
    x = input("press enter and let player start playing ")

    # lests the player quit
    if x == "quit":
        break

    #this functions used to clear the consoule
    os.system('clear')

    
    print("Guess the word")

    # Setting guesses so the player can add to it.
    gueses = ""

    # Setting lives as 8 so it can be reduced with    wrong guesses
    lives = 8

    # lests the player quit
    if gueses == "quit":
        break

    #Checking condition until player has no lives left
    while lives > 0:
        failed = 0


        # As lives decrease hangman gets smaller
        if lives == 8:
            print("""
          |------|
          |      0 
          |     /|\      
          |      |
          |     / \   
          |_______________
          [_______________]
          """)

        if lives == 7:
            print("""
          |------
          |      0 
          |     /|\      
          |      |
          |     / \   
          |_______________
          [_______________]
          """)

        if lives == 6:
            print("""
          |------
          |      0 
          |     /|\      
          |      |
          |     /    
          |_______________
          [_______________]
          """)

        if lives == 5:
            print("""
          |------
          |      0 
          |      |\      
          |      |
          |     /   
          |_______________
          [_______________]
          """)

        if lives == 4:
            print("""
          |------
          |      0 
          |      |\     
          |      |
          |        
          |_______________
          [_______________]
          """)

        if lives == 3:
            print("""
          |------
          |      0 
          |      |      
          |      |
          |         
          |_______________
          [_______________]
          """)

        if lives == 2:
            print("""
          |------
          |      0 
          |      |     
          |      
          |        
          |_______________
          [_______________]
          """)

        if lives == 1:
            print("""
          |------
          |      0
          |          
          |      
          |      
          |_______________
          [_______________]
          """)

    #Checking every charecter in player_input
        for i in player_input:
            #Print charector if in player_input
            if i in gueses:
                print(i, end=" ")
    #Print a dash if not in player_input
            else:
                print("_", end=" ")
                failed = failed + 1

        # when failed = 0 and all charectors guesed correct player wins
        if failed == 0:
            print("you WIN")
            print("the word is", player_input)

           # lets the play choes to play again or not
            play = input("would you like to play again? yes or no?")
            break
        
        #The player guesses a word or letter
        gueses_2 = input("guess a word or letter:--  ")

        # lests the player quit
        if gueses_2 == "quit":
            break
        
        # if the guess in equal to the full word failed variable 0
        if gueses_2 == player_input:
            failed = 0

        #Forming word by adding charectors
        gueses = gueses + gueses_2
    
        # for every incorect guess one live is lost
        if gueses_2 not in player_input:
            lives = lives - 1
            print("incorect guess")
            print("you have", lives, "Lives remaining")


             # if lives is equal to 0 player loses
            if lives == 0:
                print("you are out of lives")
                print("sorry, You have LOST the game")
                print("the correct word is", player_input)

                # lets the play choes to play again or not 
                play = input("would you like to play again? yes or no?")

   
  # lets the player brack the while loop
    if gueses == "quit":
        break
    elif gueses_2 == "quit":
        break
