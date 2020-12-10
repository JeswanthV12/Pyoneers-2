import datetime, random 

# random number
r_num = random.randint(1,10)
print(f"You're random number is {r_num} days. \n You're random number adds to the current date. \n Current Date:")

# adding new days to current date
date = datetime.date.today()
print(f"Current Date: {date}")
new_day = date.day + r_num

# calculating new month and day if the new day is > max month days
if date.month == 4 or date.month == 6 or date.month == 9 or date.month == 11:
  if new_day > 30:
    new_month = date.month + 1
    new_day2 = new_day - 30 
    new_date = datetime.date(date.year,new_month,new_day2)
    print(new_date)
  else:
    new_date = datetime.date(date.year,date.month,new_day)
elif date.month == 1 or date.month == 3 or  date.month == 5 or date.month == 7 or date.month == 8 or date.month == 10 or date.month == 12:
  if new_day > 31:
    new_month = date.month + 1
    new_day2 = new_day - 31
    new_date = datetime.date(date.year,new_month,new_day2)
    print(new_date)
  else:
    new_date = datetime.date(date.year, date.month, new_day)
    print(new_date)
else:
  if new_day > 28:
    new_month = date.month + 1
    new_day2 = new_day - 28
    new_date = datetime.date(date.year, new_month, new_day2)
    print(new_date)
  else:
    new_date = datetime.date(date.year,date.month,new_day)
    print(new_date)

