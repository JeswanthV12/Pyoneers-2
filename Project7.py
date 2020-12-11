import datetime, time, random

# gathering current date
date = datetime.date.today()

# gathering famous person birthday
print("Think of the birthday of a famous person.")
time.sleep(3)
year = int(input("What year they were born? \n"))
month = int(input("What month were they born? \n"))
day = int(input("On what day were they born? \n"))
br_date = datetime.date(year,month,day)

# calculating difference 
diff = date.month - br_date.month
diff2 = date.day - br_date.day
diff3 = diff2 * -1

# determining status of birthday
print(f"\nBirthday Date: {br_date} \nCurrent Date: {date}")
if date.month > br_date.month:
  print(f"The birthday has passed. It's been {diff} months and {diff2} days")
elif date.month == br_date.month and date.day > br_date.day:
  print(f"The birthday has passed. It's been {diff} months and {diff2} days")
elif date.month == br_date.month and date.day == br_date.day:
  print("It's their birthday!!")
else:
  print(f"The birthday is upcoming in {diff} months and {diff3} days")
