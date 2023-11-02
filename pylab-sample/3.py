#Write a program to :
#1)read your date of birth as input, find your age in days and seconds.
#2)find on which weekday India turned independent.
#3)Count the number of days till today from the beginning of this year.

import datetime

# Task 1: Read date of birth and calculate age in days and seconds
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
current_date = datetime.datetime.now()
age_in_days = (current_date - dob).days
age_in_seconds = (current_date - dob).total_seconds()

print(f"Your age in days is: {age_in_days} days")
print(f"Your age in seconds is: {age_in_seconds} seconds")

# Task 2: Find the weekday when India turned independent (August 15, 1947)
independence_day = datetime.datetime(1947, 8, 15)
weekday = independence_day.strftime('%A')
print(f"India turned independent on a {weekday}.")

# Task 3: Count the number of days from the beginning of the year till today
current_year = datetime.datetime.now().year
start_of_year = datetime.datetime(current_year, 1, 1)
days_till_today = (current_date - start_of_year).days
print(f"Number of days from the beginning of the year till today: {days_till_today} days")

