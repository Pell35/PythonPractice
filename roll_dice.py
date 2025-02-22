import random

roll = random.randint(1,6) 

guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Good job! You were correct, the dice rolled: " + str(roll))
else:
    print("You were incorrect. The dice rolled: " + str(roll))