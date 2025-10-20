import random

options = ("rock", "paper", "scissors")
running = True
while running :

  player = None
  computer = random.choice(options)


  player = input("Enter a choice (rock, paper, scissors)")

  while player not in options:
    player = input("Enter a choice(rock, paper, scissors)")
  print(f"player : {player}")
  print(f"Computer : {computer}")

  if player == computer:
    print("it is tie")
  elif player == "rock" and computer == "scissors" :
    print("You win")
  elif player == "paper" and computer == "rock" :
    print(" You Win")
  elif player == "scissors" and computer == "paper" :
    print("You win!")
  else :
    print("You loose!")
  
  play_again = input("play Again ? (y/n) : ").lower()
  
  if  not play_again == "y":
    running = False
  
    
    
    
