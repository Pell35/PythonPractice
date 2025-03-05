import random

card_values = {
    "A": 1,
    "A2": 11, 
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
    "7": 7, "8": 8, "9": 9, "10": 10, 
    "J": 10, "Q": 10, "K": 10
}

random_card1 = random.choice(list(card_values.keys()))

random_card2 = random.choice(list(card_values.keys()))

random_card1_val = card_values[random_card1]  

random_card2_val =  card_values[random_card2]  

player_card_val = random_card1_val + random_card2_val

dealer_card1 = random.choice(list(card_values.keys()))

dealer_card2 = random.choice(list(card_values.keys()))

dealer_card1_val = card_values[dealer_card1 ]  

dealer_card2_val = card_values[dealer_card2]  

dealer_card_val = int(dealer_card1_val) + int(dealer_card2_val)


answer = input("You were dealt: " + str(random_card1) + " & " + str(random_card2) + ". \nThere value is: " +  str(player_card_val) + ". \n Dealer card value is: " + str(dealer_card_val) + ". \n Would you like to hold or hit? ")

if answer == "hit":
    random_card3 = random.choice(list(card_values.keys()))
    random_card3_val = card_values[random_card3]  
    player_card_val = random_card1_val + random_card2_val + random_card3_val
    if player_card_val >dealer_card_val and player_card_val <=21:
        print("You have: "+ str(player_card_val) + ", you win!")
    elif player_card_val >= dealer_card_val:
        print("It's a tie.")
    else:
        print("You're points are: "+ str(player_card_val) + "You lose!")
else:
    if player_card_val >dealer_card_val and player_card_val <=21:
        print("You have: "+ str(player_card_val) + ", you win!")
    elif player_card_val >= dealer_card_val:
        print("It's a tie.")
    else:
        print("You're points are: "+ str(player_card_val) + "You lose!")