import datetime

birthYear = int(input("What year were you born? \n"))

current_year = datetime.datetime.now().year

birthMonth =  int(input("What month were you born? (1-12) \n"))
current_month = datetime.datetime.now().month
if current_month < birthMonth:
    
    age = current_year - birthYear-1
else:
    age = current_year - birthYear
 


print("You are " + str(age) +" years old.")