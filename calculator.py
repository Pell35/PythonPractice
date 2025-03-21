number1 = int(input("What is your first number? \n"))
number2 = int(input("What is your second number? \n"))
action = input("Enter the symbol of what you would like to do add +, subtract -, multiply *, or divide /. \n")

if action == "+":
    final = number1+number2
    print("Your answer is: " + str(final))
elif action == "-":
    final = number1-number2
    print("Your answer is: " + str(final))    
elif action == "*":
    final = number1*number2
    print("Your answer is: " + str(final))  
elif action == "/":
    if number2 != 0:
        final = number1 / number2
        print("Your answer is: " + str(final))
    else:
        print("Error: Cannot divide by zero.") 
else:
    print("Answer could not be solved, try again.")