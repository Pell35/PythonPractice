question1 = int(input("What is your favorite animal? \n Enter the number that corresponds with your answer: \n 1. Dog \n 2. Bird \n 3. Rat \n 4. Whale \n"))

question2 = int(input("What is your favorite food? \n Enter the number that corresponds with your answer: \n 1. Pizza \n 2. Chicken Strips \n 3. Salmon \n 4. Chocolate Cake \n"))

question3 = int(input("What is your favorite shoe? \n Enter the number that corresponds with your answer: \n 1. Sneakers \n 2. Boots \n 3. Sandals \n 4. Crocs \n"))

question4 = int(input("What is your favorite cartoon character? \n Enter the number that corresponds with your answer: \n 1. Scooby Doo \n 2. Elmo \n 3. Mickey Mouse \n 4. Bugs Bunny \n"))

if question1 == "4" and question2 == "3" and question3 == "3":
    print("Based on your answers, the vacation place you should visit is: Greece")
elif question1 == "1" and question2 == "2" and question3 == "4" and question4 == "1":
    print("Based on your answers, the vacation place you should visit is: Missouri. ")
elif question1 == "" and question2 == "" and question3 == "" and question4 == "":
    print("Based on your answers, the vacation place you should visit is: ")
elif question1 == "" and question2 == "" and question3 == "" and question4 == "":
    print("Based on your answers, the vacation place you should visit is: ")
elif question1 == "" and question2 == "" and question3 == "" and question4 == "":
    print("Based on your answers, the vacation you should go on is: ")
elif question1 == "" and question2 == "" and question3 == "" and question4 == "":
    print("Based on your answers, the vacation you should go on is: ")
else:
    print("Based on your answers, the vacation you should go on is: Canada") 