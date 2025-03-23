import datetime

birthYear = int(input("What year were you born? \n"))

current_year = datetime.datetime.now().year

birthMonth =  int(input("What month were you born? (1-12) \n"))
current_month = datetime.datetime.now().month

birthDay = int(input("What day were you born? (1-31) \n"))
current_day = datetime.datetime.now().day

if current_month == birthMonth and current_day == birthDay:   
    age = current_year - birthYear
    print("You are " + str(age) +" years old. Happy Birthday! ")
elif current_month == birthMonth and current_day < birthDay:
    age = current_year - birthYear-1
    print("You are " + str(age) +" years old.")    
elif current_month == birthMonth and current_day > birthDay:
    age = current_year - birthYear
    print("You are " + str(age) +" years old.")    
elif current_month<birthMonth:
    age = current_year - birthYear-1
    print("You are " + str(age) +" years old.")        
else:
    age = current_year - birthYear
    print("You are " + str(age) +" years old.")


