from datetime import datetime

user_input = input(
    "Please enter your birthdate in the format of day-month-year: ")
birth_date = datetime.strptime(user_input, "%d-%m-%Y")
current_date = datetime.now()

age = (current_date - birth_date).days // 365

print(f"You are {age} years old.")

# 1. Write a short programme that, when given a date, calculates the age between the current date and the given date.
#   1. An example input and output might look like:
#     1. 01-01-1990 should return 31
#     2. 04-12-1972 should return 48
