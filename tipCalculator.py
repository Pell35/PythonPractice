cost = input("What was the price of your meal? \n")

percent = input("What percentage would you like to tip? 10,15,20,25 \n")

decimal = int(percent) / 100

tip = float(cost)*decimal

total = float(cost)+tip
print("To tip " + percent +"% Your tip will be: $" + str(tip) + ". Your total cost will be : $" + str(total))