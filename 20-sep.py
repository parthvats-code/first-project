import random 
def get_choices():
    player_choice = input("enter your choice \n (rock , paper , scissors ) : ")
  
    options = ["rpck" , "paper" , "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices
def check_win(player , computer):
 print (f"you entered {player} , computer entered {computer}")
 if player == computer :
   return "its a tie" 
 elif (player == "rock" and computer == "paper") or \
     (player == "paper" and computer == "scissors") or \
     (player == "scissors" and computer == "rock"):
    return "you lose boho"
 else:
   return "you won somehow mf"
x = get_choices() 
result = check_win(x["player"] , x["computer"])
print(result)
 
    