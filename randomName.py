import random

names=[]
rangeNum = int(input("How many names do you need to enter? \n"))

for i in range(rangeNum):
    names.append(input("Enter a name: "))

randomName = random.choice(names)

names.remove(randomName)

print(str(randomName) + " is the chosen one! \n" + "These are the names left: \n" + str(names))