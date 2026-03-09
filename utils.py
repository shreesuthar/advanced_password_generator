import string


def check_strength(password):

    score = 0

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def save_password(password):

    with open("passwords.txt", "a") as file:
        file.write(password + "\n")


def view_passwords():

    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()

        if not passwords:
            print("No saved passwords.")
        else:
            print("\nSaved Passwords:")
            for p in passwords:
                print(p.strip())

    except FileNotFoundError:
        print("No passwords saved yet.")
