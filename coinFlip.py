import random

coin = ["heads", "tails"]


call = input("Would you like heads or tails? \n")

outcome = random.choice(coin)

if outcome == call:

    print("You called: " + call + ". \nThe outcome is: " + outcome + ". You win!")
else: 
        print("You called: " + call + ". \nThe outcome is: " + outcome + ". You lose!") 