from generator import generate_password


def main():

    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    symbol_choice = input("Include symbols? (y/n): ").lower()

    if symbol_choice == "y":
        use_symbols = True
    else:
        use_symbols = False

    password = generate_password(length, use_symbols)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
