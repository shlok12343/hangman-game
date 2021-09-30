print("Guess the word")
  gueses = ""
  lives = 8
  
  while lives > 0:
    failed = 0

    for i in player_input:
      if i in gueses:
        print(i, end = " ")
      else:
        print("_",end = " ")
        failed = failed + 1
      
    if failed == 0:
      print("you WIN")
      print("the word is",player_input)
      play = input("would you like to play again? yes or no? ")

    gueses_2 = input("guess a word or letter:--  ")
    gueses = gueses + gueses_2

      if gueses_2 not in player_input:
        lives = lives - 1
        print("incorect guess")
        print("you have",lives,"remaining")
      
        if lives == 0:
          print("sorry, You have LOST the game")
          print("the correct word is",player_input)
          play = input("would you like to play again? yes or no? ")