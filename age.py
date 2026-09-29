from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age = age - 1

    return age


date = input("Enter your date of birth (YYYY-MM-DD): ")

print("Your age is: ", calculate_age(date))
