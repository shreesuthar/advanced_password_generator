from generator import generate_password
from utils import check_strength, save_password
import pyperclip


def main():

    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    symbol_choice = input("Include symbols? (y/n): ").lower()
    use_symbols = symbol_choice == "y"

    password = generate_password(length, use_symbols)

    print("\nGenerated Password:")
    print(password)

    strength = check_strength(password)
    print("Password Strength:", strength)

    copy_choice = input("\nCopy password to clipboard? (y/n): ").lower()

    if copy_choice == "y":
        pyperclip.copy(password)
        print("Password copied to clipboard!")

    save_choice = input("Save password to file? (y/n): ").lower()

    if save_choice == "y":
        save_password(password)
        print("Password saved to passwords.txt")


if __name__ == "__main__":
    main()
