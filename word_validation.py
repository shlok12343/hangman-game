def valid_enteries():

 import nltk
 nltk.download('words')

 from nltk.corpus import words
 setofwords = set(words.words())

 player_input = input("Challenger plese enter word here:-  \n")

 while (player_input not in setofwords):
   print("That is not a word please enter a 'real word'")
   player_input = input("Challenger plese enter word here:-  \n")
 return print("You have suscesfuly Chosen your hangman Word as",player_input)
 

valid_enteries("hellow")