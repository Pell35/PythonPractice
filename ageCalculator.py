age = int(input("How old are you? \n"))
decades = (age // 10)
years = age%10
message = "You are " + str(decades) + " decades old \n" + "and " + str(years) + " year(s) old."
print(message)