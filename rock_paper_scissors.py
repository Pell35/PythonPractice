computer_choice = "scissors"
user_choice = input("Do you want rock, paper, or scissors?")

if computer_choice == user_choice:
    print("TIE")
elif (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "rock" and user_choice == "scissors"):
    print("Computer Wins!")
elif (computer_choice == "scissors" and user_choice == "rock") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "rock" and user_choice == "paper"):
    print("You Win!")