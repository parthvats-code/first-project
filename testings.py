import random
def albert():
 player_choice = input("enter your choice :")
 options = ["rock" , "paper" , "scissors"]
 computer_choice = random.choice(options)
 print(computer_choice)
 if player_choice == computer_choice :
  print ("fucking tie")

 elif (player_choice == "rock" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "rock"):
    return "you lose boho"
 elif :
  print("you win")
  print("\n \t still wanna play?")
  agane = input("yes or no :")
  if agane == "yes" :
   albert()
  else : 
   print("game over gotta play again")
   albert()
albert()

