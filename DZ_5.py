# Step 1
import datetime
# Step 2
birth_day = int(input("Day of birth: "))
birth_month = int(input("Month of birth: "))
birth_year = int(input("Year of birth: "))
day = int(datetime.date.today().day)
month = int(datetime.date.today().month)
year = int(datetime.date.today().year)
# Step 3
if month > birth_month:
 age = year - birth_year
else:
 age = (year - birth_year) - 1
# Step 4
a = age
# Исправила не верный подсчет месяцев
if month >= birth_month:
    b = month - birth_month
else:
    b = 12 - birth_month + month
c = abs(day - birth_day)
print(f"Your age: {a} years, {b} months, {c} days")
