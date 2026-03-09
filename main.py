from generator import generate_password
from utils import check_strength, save_password, view_passwords
import pyperclip


def generate_single():

    length = int(input("Enter password length: "))

    symbol_choice = input("Include symbols? (y/n): ").lower()
    use_symbols = symbol_choice == "y"

    password = generate_password(length, use_symbols)

    print("\nGenerated Password:", password)

    strength = check_strength(password)
    print("Password Strength:", strength)

    copy_choice = input("Copy password to clipboard? (y/n): ").lower()
    if copy_choice == "y":
        pyperclip.copy(password)
        print("Password copied!")

    save_choice = input("Save password? (y/n): ").lower()
    if save_choice == "y":
        save_password(password)
        print("Password saved.")


def generate_multiple():

    count = int(input("How many passwords to generate? "))
    length = int(input("Password length: "))

    symbol_choice = input("Include symbols? (y/n): ").lower()
    use_symbols = symbol_choice == "y"

    print("\nGenerated Passwords:")

    for i in range(count):
        password = generate_password(length, use_symbols)
        print(password)


def main():

    while True:

        print("\n=== Password Generator ===")
        print("1 Generate password")
        print("2 Generate multiple passwords")
        print("3 View saved passwords")
        print("4 Exit")

        choice = input("Select option: ")

        if choice == "1":
            generate_single()

        elif choice == "2":
            generate_multiple()

        elif choice == "3":
            view_passwords()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
