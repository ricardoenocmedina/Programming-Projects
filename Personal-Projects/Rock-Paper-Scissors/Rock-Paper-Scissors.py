
import random

print("\n          Welcome to the Rock-Paper-Scissors Machine           ")
print("-----------------------------------------------------------------")
print("Please type either 'rock', 'paper', 'scissors', or 'stop' to stop")

while True:
  computer = random.choice(["rock", "paper", "scissors"]) 
  my_choice = input("\nRock, paper, or scissors? ")
  
  if my_choice == computer:
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nDraw! Go again!")
    continue

  elif my_choice == "rock" and computer == "paper":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nThe computer wins. Try again!")
    continue

  elif my_choice == "rock" and computer == "scissors":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nYou smashed the computer's scissors!")
    continue

  elif my_choice == "paper" and computer == "rock":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nYou wrapped up the computer's rock!")
    continue

  elif my_choice == "paper" and computer == "scissors":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nThe computer wins. Try again!")
    continue

  elif my_choice == "scissors" and computer == "rock":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nThe computer wins. Try again!")
    continue

  elif my_choice == "scissors" and computer == "paper":
    print(f"\nYou chose {my_choice}!""\n"f"The computer chose {computer}!\nYou sliced up the computer's paper!")
    continue

  elif my_choice == "stop":
    print("Thank you for playing!\n")
    break
  
  elif my_choice != "scissors" or my_choice != "rock" or my_choice != "paper" or my_choice != "stop":
    print("\nNOT A VALID RESPONSE. PLEASE TYPE EITHER 'rock', 'paper', OR 'scissors'")
    continue
