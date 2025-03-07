import random

# Housing options
housing = ["Mansion", "Apartment", "Shack", "House", "Castle", "Van down by the river"]

# Spouse options
spouse = ["Taylor Swift", "Ryan Gosling", "SpongeBob", "Elsa", "Your crush", "A random AI chatbot"]

# Vehicle options
vehicles = ["Sports car", "Bicycle", "Horse", "Skateboard", "Spaceship"]

# Job options
jobs = ["Rockstar", "Software Engineer", "Professional Gamer", "Circus Clown", "Billionaire Investor"]

# Location options
locations = ["New York City", "Paris", "Underwater", "The Moon"]

# Pet options
pets = ["Dog", "Cat", "Dinosaur", "Talking Parrot"]


house = random.choice(housing)

spouse = random.choice(spouse)

vehicle = random.choice(vehicles)

job = random.choice(jobs)

location = random.choice(locations)

pet = random.choice(pets)

answer = input("Do you want to play MASH? YES or NO\n")

if answer == "YES":
    print("\nYou will live in a " + str(house) + ". \nYou will drive a " + str(vehicle) + ". \nYou will work as a " + str(job) + ". \nYou will live in " + str(location) + ". \nYou will have a pet " + str(pet) +".")
else:
    print("Ok, Goodbye.")