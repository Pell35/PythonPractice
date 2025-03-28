question1 = (input("What is your favorite animal? \n Enter the number that corresponds with your answer: \n 1. Dog \n 2. Bird \n 3. Rat \n 4. Whale \n"))

question2 = (input("What is your favorite food? \n Enter the number that corresponds with your answer: \n 1. Pizza \n 2. Chicken Strips \n 3. Salmon \n 4. Chocolate Cake \n"))

question3 = (input("What is your favorite shoe? \n Enter the number that corresponds with your answer: \n 1. Sneakers \n 2. Boots \n 3. Sandals \n 4. Crocs \n"))

question4 = (input("What is your favorite cartoon character? \n Enter the number that corresponds with your answer: \n 1. Scooby Doo \n 2. Elmo \n 3. Mickey Mouse \n 4. Spongebob \n"))

if question1 == "4" and question2 == "3" and question3 == "3"and question4 == "4":
    print("Based on your answers, the vacation place you should visit is: Greece")
elif question1 == "1" and question2 == "2" and question3 == "4" and question4 == "1":
    print("Based on your answers, the vacation place you should visit is: Missouri. ")
elif question1 == "3" and question2 == "1" and question3 == "1" and question4 == "4":
    print("Based on your answers, the vacation place you should visit is: New York City ")
elif question1 == "2" and question2 == "4" and question3 == "1" and question4 == "3":
    print("Based on your answers, the vacation place you should visit is: Disney World ")
elif question1 == "2" and question2 == "4" and question3 == "3" and question4 == "3":
    print("Based on your answers, the vacation place you should visit is: Italy ")
elif question1 == "4" and question2 == "1" and question3 == "4" and question4 == "4":
    print("Based on your answers, the vacation you should go on is: a Cruise ")
else:
    print("Based on your answers, the vacation place you should visit is: Canada") 