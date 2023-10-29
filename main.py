# Sebastian Pena
def encoder(string):
    result = ''
    for num in string:
        new_digit = str((int(num) + 3) % 10)
        result += new_digit
    return result


def main():
    while True:
        print('Menu')
        print('-------------')
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Please enter an option: ")
        if choice == "1":
            string = input("Please enter your password to encode: ")
            print('Your password has been encoded and stored!')
            string_encoded = encoder(string)
        elif choice == "2":
            print(f'The encoded password is {string_encoded}, and the original password is {string}.')
        elif choice == "3":
            break
        else:
            print("Invalid")
        print()


if __name__ == "__main__":
    main()
