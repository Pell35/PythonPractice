import random
fruits = ["lemon", "cherry", "orange"]
fruit1 = random.choice(fruits)
fruit2 = random.choice(fruits)
fruit3 = random.choice(fruits)
if fruit1 == "lemon" and fruit2 == "lemon" and fruit3 == "lemon":
     print(str(fruit1) + " "+ str(fruit2)+ " " + str(fruit3) + " You WIN!!!")
elif fruit1 == "orange" and fruit2 == "orange" and fruit3 == "orange":
     print(str(fruit1) + " "+ str(fruit2)+ " " + str(fruit3) + " You WIN!!!")
elif fruit1 == "cherry" and fruit2 == "cherry" and fruit3 == "cherry":
     print(str(fruit1) + " "+ str(fruit2)+ " " + str(fruit3) + " You WIN!!!")     
else:
    print(str(fruit1) + " "+ str(fruit2)+ " " + str(fruit3) + " You Lose!")