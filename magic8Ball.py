import random
answers = ["yes", "no", "maybe", "ask again later", "odds aren't in your favor", "most definitely"]

question = input("What would you like to ask the magic 8 ball? \n")

reply = random.choice(answers)

print("The answer to your question is: " + reply)