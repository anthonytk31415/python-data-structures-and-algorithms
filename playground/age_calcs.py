from datetime import datetime

# calcs bday
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# Example usage of dob
dob = "1983-09-20"
print("Age:", calculate_age(dob))