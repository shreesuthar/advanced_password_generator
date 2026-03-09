import random
import string


def generate_password(length, use_symbols):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters + digits

    if use_symbols:
        characters += symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password
