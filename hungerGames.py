import random
hunger_games_characters = [
    # From "The Hunger Games"
    "Katniss Everdeen", "Peeta Mellark", "Gale Hawthorne", "Prim Everdeen", "Effie Trinket",
    "Haymitch Abernathy", "Rue", "Cinna", "President Snow", "Seneca Crane", "Portia", "Madge Undersee",
    
    # From "Catching Fire"
    "Johanna Mason", "Finnick Odair", "Annie Cresta", "Beetee", "Wiress", "Mags", "District 13",
    "Coin", "Plutarch Heavensbee", "Chaff", "Tigris", "Brutus", "Gloss", "Cashmere",

    # From "Mockingjay"
    "President Coin", "Boggs", "Pollux", "Peeta Mellark", "Gale Hawthorne", "Katniss Everdeen",
    "Prim Everdeen", "Finnick Odair", "Annie Cresta", "Cressida", "Delly Cartwright", "Pollux", "Plutarch Heavensbee",
    "Greasy Sae", "Madge Undersee", "Tigris", "Beetee", "Wiress",

    # From "The Ballad of Songbirds and Snakes" (Prequel)
    "Coriolanus Snow", "Lucy Gray Baird", "Sejanus Plinth", "Tigris Snow", "Dr. Gaul", "Clemencia Dovecote",
    "Festus Creed", "Dean Highbottom", "Coriolanus' Grandmother", "Julius", "Commander Hoff"

]

you = random.choice(hunger_games_characters) 

hunger_games_characters.remove(you)

print(" Your character is: " + you +". \n")

ally1 =random.choice(hunger_games_characters) 

hunger_games_characters.remove(ally1)


ally2 = random.choice(hunger_games_characters) 

hunger_games_characters.remove(ally2)

ally3 = random.choice(hunger_games_characters) 

hunger_games_characters.remove(ally3)

print("Your allies are: " + ally1 + ", " + ally2 + ", "+ ally3 + ".\n")

enemy = random.choice(hunger_games_characters) 

hunger_games_characters.remove(enemy)

print(" Your main enemy is: " + enemy)

pick= []

pick.append(you)
pick.append(ally1)
pick.append(ally2)
pick.append(ally3)
pick.append(enemy)

victor = random.choice(pick)

print("The victor in your Hunger games is: " + victor)