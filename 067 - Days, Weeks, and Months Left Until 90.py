from datetime import datetime

def time_left_until_90(birth_year):
    current_date = datetime.now()
    birth_date = datetime(birth_year, current_date.month, current_date.day)
    age = current_date.year - birth_date.year
    days_left = (90 - age) * 365.25
    weeks_left = days_left / 7
    months_left = (90 - age) * 12

    print(f"Days left: {int(days_left)}")
    print(f"Weeks left: {int(weeks_left)}")
    print(f"Months left: {int(months_left)}")

birth_year = int(input("Enter your birth year: "))
time_left_until_90(birth_year)
