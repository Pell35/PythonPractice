toDo = []
rangeNum = int(input("How many things do you need to do today? "))
for i in range(rangeNum):
    toDo.append(input("What do you need to do today?\n"))
deleteWord = input("Would you like to delete something off your to do list? If so please type what to delete, otherwise type no. ")  
if deleteWord.lower() == "no":
    print("Here is your to-do list: " + ", ".join(toDo))
elif deleteWord in toDo:
    toDo.remove(deleteWord)
    print("Updated to-do list: " + ", ".join(toDo))
else:
    print(f"'{deleteWord}' was not found in your to-do list.")