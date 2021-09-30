import nltk
import os

play = "yes"

while play == "yes":
    print("\nWELCOM TO HANGMAN")
    print("\nLets Start playing\n\n")

    nltk.download('words')
    from nltk.corpus import words

    setofwords = set(words.words())

    
    
    player_input = input("Challenger enter the word you want player to guess here:-  \n")

    if player_input == 'quit':
      break


    while (player_input not in setofwords):
        print("That is not a word please enter a 'real word'")
        player_input = input("Challenger plese enter word here:-  \n")

    print("\nYou have suscesfuly Chosen your hangman Word as", player_input)
    x = input("press enter and let player start playing ")
    if x == "quit":
      break

    os.system('clear')

    print("Guess the word")
    gueses = ""
    lives = 8

    if gueses == "quit":
      break

    while lives > 0:
        failed = 0

        for i in player_input:
            if i in gueses:
                print(i, end=" ")
            else:
                print("_", end=" ")
                failed = failed + 1

        if failed == 0:
            print("you WIN")
            print("the word is", player_input)
            play = input("would you like to play again? yes or no?")
            break

        gueses_2 = input("guess a word or letter:--  ")

        if gueses_2 == "quit":
          break

        gueses = gueses + gueses_2

        if gueses_2 not in player_input:
            lives = lives - 1
            print("incorect guess")
            print("you have", lives, "remaining")

            if lives == 0:
                print("you are out of lives")
                print("sorry, You have LOST the game")
                print("the correct word is", player_input)
                play = input("would you like to play again? yes or no? ")
    if gueses == "quit":
      break
    elif gueses_2 =="quit":
      break
    
    
