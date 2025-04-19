import re

def check_password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not re.search(r"\d", password):
        print("Password must contain at least one number.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character.")
    else:
        print("Password is valid.")

check_password()
