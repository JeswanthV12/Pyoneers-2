import datetime, time, random

# gathering current date
date = datetime.date.today()

# gathering famous person birthday
print("Think of the birthday of a famous person.")
year = random.randint(1500,2020)
month = 12
day = 10
br_date = datetime.date(year,month,day)

# calculating difference of two dates
diff = date.month - br_date.month
diff2 = date.day - br_date.day

print(f"\nBirthday Date: {br_date} \nCurrent Date: {date}")
if date.month > br_date.month:
  print(f"The birthday has passed.")
elif date.month == br_date.month & date.day > br_date.day:
  print("The birthday has passed.")
elif date.month == br_date.month & date.day == br_date.day:
  print("It's there birthday!!")

#year = int(input("What year they were born? \n"))
#month = int(input("What month were they born? \n"))
#day = int(input("On what day were they born? \n"))